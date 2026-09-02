# Artifact 3026

> **What will 3026 think this was?**

English · [简体中文](README.zh-CN.md)

[![skills.sh installs](https://skills.sh/b/xxwzkdwz/artifact-3026)](https://skills.sh/xxwzkdwz/artifact-3026)
[![License: MIT](https://img.shields.io/badge/License-MIT-b28a50.svg)](LICENSE)

Artifact 3026 is an open-source skill **for AI assistants that support the open Agent Skills standard**. It turns a photo or description of an everyday object into a clearly fictional museum artifact from the future. The host agent handles curation and optional image creation; a dependency-free local script renders the final 1080×1440 share card.

<p align="center">
  <img src="examples/cards/meeting-room-paper-cup.png" width="400" alt="A meeting-room paper cup misread as an artifact from 3026">
</p>

## Install in one command

```bash
npx skills add https://github.com/xxwzkdwz/artifact-3026 --skill artifact-3026
```

Then attach a photo and ask: `What will 3026 think this was?` The installer detects supported agents and lets you choose where to add the skill. Platform-specific and manual options remain under [Install](#install).

## See the present through the eyes of 3026

Here are six ordinary objects, reimagined as artifacts from the future. The collection moves between Chinese and English, and from deadpan to tender and absurd. Click an image for the editable SVG; each artifact also includes its [JSON data](examples/), generated [museum scene](examples/scenes/), and [1080×1440 PNG](examples/cards/). Image provenance remains in [examples/SOURCES.md](examples/SOURCES.md).

<table>
  <tr>
    <td width="50%" align="center"><a href="examples/meeting-room-paper-cup.svg"><img src="examples/cards/meeting-room-paper-cup.png" width="180" alt="一次性共识容器"></a><br><strong>一次性共识容器</strong><br><sub>Chinese · deadpan</sub></td>
    <td width="50%" align="center"><a href="examples/tangled-charging-cable.svg"><img src="examples/cards/tangled-charging-cable.png" width="180" alt="Portable Energy Umbilical"></a><br><strong>Portable Energy Umbilical</strong><br><sub>English · deadpan</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="examples/forgotten-folding-umbrella.svg"><img src="examples/cards/forgotten-folding-umbrella.png" width="180" alt="Rain Negotiation Device"></a><br><strong>Rain Negotiation Device</strong><br><sub>English · absurd</sub></td>
    <td align="center"><a href="examples/worn-wired-earbuds.svg"><img src="examples/cards/worn-wired-earbuds.png" width="180" alt="私人声音脐带"></a><br><strong>私人声音脐带</strong><br><sub>Chinese · tender</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="examples/faded-brass-key.svg"><img src="examples/cards/faded-brass-key.png" width="180" alt="Permission to Return"></a><br><strong>Permission to Return</strong><br><sub>English · tender</sub></td>
    <td align="center"><a href="examples/used-pencil-stub.svg"><img src="examples/cards/used-pencil-stub.png" width="180" alt="可消耗思想探针"></a><br><strong>可消耗思想探针</strong><br><sub>Chinese · absurd</sub></td>
  </tr>
</table>

## Make it a shared ritual

- **Post a daily artifact:** Photograph one small object each day and share what people in 3026 might think it was. Over time, it becomes your own future museum.
- **Make a reveal video:** Open with the real object, then cut to its future exhibit card and read the deadpan museum label aloud. Let the comments choose the next artifact.
- **Play with friends:** Swap object photos, guess how the future will misunderstand them, and reveal the generated cards. Try a couples, roommates, coworkers, or family collection.
- **Build a personal exhibition:** Turn someone's keys, earbuds, tickets, and desk objects into a birthday keepsake, travel archive, or year-in-review collection.

Share your result with **#Artifact3026**, link back to this repository, or post it in [GitHub Discussions](https://github.com/xxwzkdwz/artifact-3026/discussions). Selected community artifacts may join a future showcase with the creator's permission.

## Compatibility

Artifact 3026 is not tied to one model vendor. Some agents load the skill directly; ordinary chat products can use the same creative workflow by reading the uploaded files or a copied prompt.

| Platform | How to use it |
|---|---|
| OpenAI / Codex, Cursor, GitHub Copilot | Read `.agents/skills/artifact-3026/` in place or install it at user scope |
| Claude / Claude Code | Use the installer to place the canonical skill under `.claude/skills/` |
| Qwen Code | Use `--platform qwen` to install under `.qwen/skills/` |
| Kimi Code CLI | Reads the project `.agents/skills/` path; `--platform kimi` installs at user scope |
| Doubao models / Volcengine AgentKit | Build the portable ZIP and upload it as an AgentKit custom skill |
| Zhipu GLM / GLM Coding Plan | Load it through a coding-agent host that supports Agent Skills; the host, not the model, owns installation |

Ordinary chat products—including the Doubao app, Zhipu Qingyan, Qwen chat, Kimi, and DeepSeek—can still create an artifact from a photo, but they should not all be described as native one-click skill hosts. Attach `SKILL.md` or the portable ZIP and use this prompt; image generation and the local renderer depend on the product:

> Read the attached Artifact 3026 skill. Reimagine this object as an exhibit in a museum in the year 3026 while keeping the object recognizable. Create a future-archaeology display image and provide an artifact name, original purpose, future misinterpretation, curator note, and accession number. If you cannot run the repository renderer, return the copy and image directly.

The repository keeps one canonical `SKILL.md`. See [COMPATIBILITY.md](COMPATIBILITY.md) for official sources, support boundaries, and local test status.

## Install

The one-command installer above is the easiest option. To inspect or develop the skill locally, clone the repository; hosts that support project-level `.agents/skills/` can read the canonical directory in place:

```bash
git clone https://github.com/xxwzkdwz/artifact-3026.git
cd artifact-3026
```

Copy it to the common user path used by Codex, Cursor, and GitHub Copilot:

```bash
python3 scripts/install_skill.py --platform agents --scope user --mode copy
```

Adapt it to Claude or Claude Code:

```bash
python3 scripts/install_skill.py --platform claude --scope user --mode copy
```

Adapt it to Qwen Code or Kimi Code CLI:

```bash
python3 scripts/install_skill.py --platform qwen --scope user --mode copy
python3 scripts/install_skill.py --platform kimi --scope user --mode copy
```

Use `--mode symlink` for development or `--dry-run` to inspect the target. The installer stops if a different target already exists and never silently overwrites it.

For Volcengine AgentKit and ordinary chat products without an automatic loader, build a portable ZIP. Upload it as a custom skill in AgentKit, or attach it manually in a chat product:

```bash
python3 scripts/package_skill.py
```

AgentKit uses its documented custom-skill upload flow. Ordinary chat products are **manually compatible**: attachment reading and local script execution depend on the product and are not presented as one-click installation.

## Try it

Attach a photo or describe an object, then ask the host agent to use `artifact-3026`:

```text
Use artifact-3026: What will 3026 think this tangled charging cable was? Render a vertical share card.
```

The project page and [examples/SOURCES.md](examples/SOURCES.md) transparently describe the AI-assisted workflow and image provenance; the finished card artwork does not embed an AI-generation label. Every interpretation remains creative fiction and never claims real provenance, appraisal, valuation, authentication, or museum affiliation. The project operates without a repository-hosted inference service, shared API key, account, analytics, or upload endpoint.

## Render and validate

```bash
python3 .agents/skills/artifact-3026/scripts/render_exhibit_card.py \
  examples/meeting-room-paper-cup.json \
  --output examples/meeting-room-paper-cup.svg

python3 -m unittest discover -s tests -v
python3 scripts/validate_release.py
skills-ref validate .agents/skills/artifact-3026
```

The final command requires the reference validator to be installed. The first two checks still verify the directory structure, metadata, single `SKILL.md`, vendor-neutral canonical content, gallery consistency, and renderer behavior.

## Repository map

- `.agents/skills/artifact-3026/`: the only canonical skill, references, and renderer
- `examples/`: bilingual inputs, scenes, SVGs, and PNG cards
- `scripts/install_skill.py`: copy/symlink platform adapter
- `scripts/package_skill.py`: manual ZIP delivery for ordinary chat products
- `scripts/validate_release.py` and `tests/`: structural, compatibility, and behavior checks
- [CONTRIBUTING.md](CONTRIBUTING.md): community showcase and contribution guide

## Privacy and boundaries

- Inspect source images for faces, addresses, badges, account details, or other identifiers.
- Do not add unsupported logos or imply that a real museum authenticated the object.
- Treat every date, accession number, institution, and interpretation as fiction.
- Keep confidential, proprietary, client, and personal material out of examples.

## License and author

MIT © 2026 [WANG ZHEN](https://github.com/xxwzkdwz)
