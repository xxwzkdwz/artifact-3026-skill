import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents" / "skills" / "artifact-3026" / "scripts" / "render_exhibit_card.py"
SPEC = importlib.util.spec_from_file_location("render_exhibit_card", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class RenderCardTests(unittest.TestCase):
    def sample(self):
        return {
            "future_year": "3026",
            "artifact_name": "Cup & Cable",
            "object_identity": "desk object <2026>",
            "interpretation": "A short institutional misunderstanding.",
            "curator_note": "Ordinary life survived in the wear.",
        }

    def test_renders_without_ai_badge_and_escapes_content(self):
        svg = MODULE.render(self.sample())
        self.assertNotIn("AI-ASSISTED FICTION", svg)
        self.assertNotIn("AI辅助虚构内容", svg)
        self.assertNotRegex(svg, r"(?i)\bAI[- ](?:generated|assisted)\b")
        self.assertIn("Cup &amp; Cable", svg)
        self.assertIn("desk object &lt;2026&gt;", svg)
        self.assertIn('width="1080" height="1440"', svg)

    def test_accession_is_deterministic(self):
        first = MODULE.accession_number(self.sample())
        second = MODULE.accession_number(self.sample())
        self.assertEqual(first, second)
        self.assertRegex(first, r"^FM-3026-\d{4}$")

    def test_embeds_local_image(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            image = Path(temp_dir) / "tiny.png"
            image.write_bytes(b"\x89PNG\r\n\x1a\n")
            data = self.sample() | {"image_path": str(image)}
            self.assertIn("data:image/png;base64,", MODULE.render(data))

    def test_wraps_chinese_by_visual_width(self):
        text = "这是一段没有空格的中文说明，用来验证分享卡不会把整段文字放在同一行。"
        lines = MODULE.wrap_text(text, 16)
        self.assertGreater(len(lines), 1)
        self.assertTrue(all(MODULE.visual_width(line) <= 16 for line in lines))

    def test_real_continuous_cjk_copy_stays_inside_card(self):
        text = (
            "研究者认为，这类器物曾被固定分配给单个人类，用来暂时保存水、咖啡等维持工作能力的液体。"
            "把手仅允许一只手操作，说明补水时另一只手仍被键盘占用。"
        )
        self.assertNotIn("\n", text)
        svg = MODULE.render(self.sample() | {"interpretation": text})
        root = ET.fromstring(svg)
        bodies = root.findall(".//{http://www.w3.org/2000/svg}text[@data-role='interpretation']")
        self.assertTrue(bodies)
        lines = [body.text or "" for body in bodies]
        self.assertEqual("".join(lines), text)
        self.assertGreaterEqual(len(lines), 3)
        self.assertNotIn("<tspan", svg)

        # Check the actual SVG line geometry, not merely that the source text appears.
        # The independent estimate intentionally uses a wider 0.70 em for Latin glyphs.
        for body, line in zip(bodies, lines):
            x = float(body.attrib["x"])
            font_size = float(body.attrib["font-size"])
            width = sum(
                font_size if unicodedata.east_asian_width(char) in "WFA" else font_size * 0.70
                for char in line
            )
            self.assertLessEqual(x + width, MODULE.TEXT_RIGHT_EDGE, line)

    def test_mixed_cjk_latin_copy_uses_independent_svg_lines(self):
        text = (
            "研究者将USB-C与PD 3.0标记误认为能源等级，"
            "并推测20W是使用者每天获准领取的电量。重复弯折痕迹则被解释为一种手工校准仪式。"
        )
        svg = MODULE.render(self.sample() | {"interpretation": text})
        root = ET.fromstring(svg)
        bodies = root.findall(".//{http://www.w3.org/2000/svg}text[@data-role='interpretation']")
        self.assertGreaterEqual(len(bodies), 2)
        self.assertEqual("".join(body.text or "" for body in bodies), text)
        self.assertEqual([body.attrib["data-line"] for body in bodies], [str(i) for i in range(len(bodies))])
        self.assertTrue(all(not list(body) for body in bodies), "wrapped lines must not use nested tspan nodes")

    def test_invalid_accent_falls_back_to_archival_red(self):
        data = self.sample() | {"accent": "url(javascript:alert(1))"}
        svg = MODULE.render(data)
        self.assertIn(MODULE.DEFAULT_ACCENT, svg)
        self.assertNotIn("javascript", svg)

    def test_missing_required_fields_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "missing required fields"):
            MODULE.render({"artifact_name": "Only a title"})

    def test_cli_writes_the_expected_svg(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            input_path = temp / "exhibit.json"
            output_path = temp / "card.svg"
            input_path.write_text(json.dumps(self.sample()), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), str(input_path), "--output", str(output_path)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertTrue(output_path.is_file())
            self.assertIn(str(output_path), completed.stdout)
            self.assertEqual(output_path.read_text(encoding="utf-8"), MODULE.render(self.sample()))


if __name__ == "__main__":
    unittest.main()
