import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills" / "future-museum-curator" / "SKILL.md").read_text(encoding="utf-8")
VISUAL = (
    ROOT / "skills" / "future-museum-curator" / "references" / "visual-direction.md"
).read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_archaeological_survivor_is_the_default(self):
        self.assertIn("archaeological survivor", SKILL)
        self.assertIn("three-quarter", VISUAL)
        self.assertIn("off-center", VISUAL)
        self.assertIn("Avoid bright white showrooms", VISUAL)

    def test_original_condition_remains_an_explicit_override(self):
        self.assertIn("original-condition preservation", VISUAL)
        self.assertIn("Do not add future damage", VISUAL)
        self.assertIn("change only the museum setting", VISUAL)

    def test_example_locks_identity_and_excludes_product_photography(self):
        self.assertIn("Preserve its tapered silhouette", VISUAL)
        self.assertIn("recognizable astronaut and planet motifs", VISUAL)
        self.assertIn("Avoid a bright modern gallery", VISUAL)
        self.assertIn("glossy product lighting", VISUAL)


if __name__ == "__main__":
    unittest.main()
