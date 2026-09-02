# Artifact 3026

> **What will 3026 think this was?**

[简体中文](README.md) · English

Artifact 3026 is an open-source skill **for AI assistants that support the open Agent Skills standard**. It turns a photo or description of an everyday object into a clearly fictional museum artifact from the future. The host agent handles curation and optional image creation; a dependency-free local script renders the final 1080×1440 share card.

The repository URL remains <https://github.com/xxwzkdwz/future-museum-curator>. The display brand is **Artifact 3026** and the skill identifier is `artifact-3026`. See [docs/NAMING.md](docs/NAMING.md) for the naming research and collision checks.

<p align="center">
  <img src="examples/cards/meeting-room-paper-cup.png" width="400" alt="A meeting-room paper cup misread as an artifact from 3026">
</p>

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

## Why people come back

Give the future one ordinary object and see what it gets wrong. A tangled cable becomes a portable energy umbilical; a worn key becomes permission to return. Each object from a desk, bag, kitchen, or family archive reveals a different present-day habit, while the shared accession system, curatorial voice, and card layout make the results a recognizable series rather than a one-shot filter.

The default scene treats the object as an archaeological survivor. Ask for `original-condition preservation` to change only its setting and light without adding future damage.

## Compatibility

There is one canonical skill: `.agents/skills/artifact-3026/SKILL.md`. Platform adapters only copy or link that directory; they do not maintain duplicate instructions.

| Platform | Official open-skill support | Delivery in this repository |
|---|---|---|
| OpenAI / Codex | Project and user `.agents/skills/` | Native project discovery; installer for user scope |
| Cursor | `.agents/skills/` plus selected compatibility paths | Native project discovery; installer for user scope |
| GitHub Copilot | `.agents/skills/` across supported agent experiences | Standard project path; official `gh skill` preview is also documented |
| Claude / Claude Code | Open Agent Skills with native `.claude/skills/` paths | Installer copies or links the same canonical directory |

These are documented compatibility paths, not a claim that every AI product supports one-click installation. See [COMPATIBILITY.md](COMPATIBILITY.md) for official sources, boundaries, and runtime test status.

## Install

Clone the repository. Hosts that support project-level `.agents/skills/` can read the canonical directory in place:

```bash
git clone https://github.com/xxwzkdwz/future-museum-curator.git
cd future-museum-curator
```

Copy it to the common user path used by Codex, Cursor, and GitHub Copilot:

```bash
python3 scripts/install_skill.py --platform agents --scope user --mode copy
```

Adapt it to Claude or Claude Code:

```bash
python3 scripts/install_skill.py --platform claude --scope user --mode copy
```

Use `--mode symlink` for development or `--dry-run` to inspect the target. The installer stops if a different target already exists and never silently overwrites it.

For ordinary chat products without an automatic skill loader, build a portable ZIP and attach it manually, or attach `SKILL.md` together with its `references/` and `scripts/` resources:

```bash
python3 scripts/package_skill.py
```

That is **manual compatibility**: attachment reading and local script execution depend on the product and are not presented as one-click installation.

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

## Privacy and boundaries

- Inspect source images for faces, addresses, badges, account details, or other identifiers.
- Do not add unsupported logos or imply that a real museum authenticated the object.
- Treat every date, accession number, institution, and interpretation as fiction.
- Keep confidential, proprietary, client, and personal material out of examples.

## License and author

MIT © 2026 [WANG ZHEN](https://github.com/xxwzkdwz)
