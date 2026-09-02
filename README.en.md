# Artifact 3026

> **What will 3026 think this was?**

[简体中文](README.md) · English

Artifact 3026 is an open-source skill **for AI assistants that support the open Agent Skills standard**. It turns a photo or description of an everyday object into a clearly fictional museum artifact from the future. The host agent handles curation and optional image creation; a dependency-free local script renders the final 1080×1440 share card.

The repository URL remains <https://github.com/xxwzkdwz/future-museum-curator>. The display brand is **Artifact 3026** and the skill identifier is `artifact-3026`. See [docs/NAMING.md](docs/NAMING.md) for the naming research and collision checks.

![A meeting-room paper cup misread as an artifact from 3026](examples/cards/meeting-room-paper-cup.png)

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

Every card visibly identifies itself as AI-assisted fiction. The project does not claim real provenance, appraisal, valuation, or authentication, and it operates without a repository-hosted inference service, shared API key, account, analytics, or upload endpoint.

## Gallery

Six reusable examples cover Chinese and English plus `deadpan`, `tender`, and `absurd` voices. Each includes [JSON data](examples/), a generated [museum scene](examples/scenes/), editable SVG, and a [1080×1440 PNG](examples/cards/). Image provenance is recorded in [examples/SOURCES.md](examples/SOURCES.md).

- [一次性共识容器](examples/meeting-room-paper-cup.svg) · Chinese · deadpan
- [Portable Energy Umbilical](examples/tangled-charging-cable.svg) · English · deadpan
- [Rain Negotiation Device](examples/forgotten-folding-umbrella.svg) · English · absurd
- [私人声音脐带](examples/worn-wired-earbuds.svg) · Chinese · tender
- [Permission to Return](examples/faded-brass-key.svg) · English · tender
- [可消耗思想探针](examples/used-pencil-stub.svg) · Chinese · absurd

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
