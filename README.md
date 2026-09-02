# Future Museum Curator

> **What will 3026 think this was?**

[中文说明](README.zh-CN.md)

Future Museum Curator is an open-source Codex skill that turns a photo or description of an everyday object into a fictional museum artifact from the future. Codex develops the curatorial idea and can use the image capability already available in the user's environment; a dependency-free local script handles the final 1080×1440 share-card layout.

![Example: a meeting-room paper cup misread as an artifact from 3026](examples/cards/meeting-room-paper-cup.png)

## Gallery

Six objects, three voices, two languages. Each example includes its [exhibit data](examples/), generated [museum scene](examples/scenes/), editable SVG, and final PNG card. Image provenance is recorded in [examples/SOURCES.md](examples/SOURCES.md).

<table>
  <tr>
    <td width="50%"><img src="examples/cards/meeting-room-paper-cup.png" alt="Meeting-room paper cup future museum card"><br><strong>一次性共识容器</strong> · 中文 · deadpan<br><a href="examples/meeting-room-paper-cup.json">data</a> · <a href="examples/scenes/meeting-room-paper-cup.jpg">scene</a> · <a href="examples/meeting-room-paper-cup.svg">SVG</a></td>
    <td width="50%"><img src="examples/cards/tangled-charging-cable.png" alt="Tangled charging cable future museum card"><br><strong>Portable Energy Umbilical</strong> · English · deadpan<br><a href="examples/tangled-charging-cable.json">data</a> · <a href="examples/scenes/tangled-charging-cable.jpg">scene</a> · <a href="examples/tangled-charging-cable.svg">SVG</a></td>
  </tr>
  <tr>
    <td><img src="examples/cards/forgotten-folding-umbrella.png" alt="Forgotten folding umbrella future museum card"><br><strong>Rain Negotiation Device</strong> · English · absurd<br><a href="examples/forgotten-folding-umbrella.json">data</a> · <a href="examples/scenes/forgotten-folding-umbrella.jpg">scene</a> · <a href="examples/forgotten-folding-umbrella.svg">SVG</a></td>
    <td><img src="examples/cards/worn-wired-earbuds.png" alt="Worn wired earbuds future museum card"><br><strong>私人声音脐带</strong> · 中文 · tender<br><a href="examples/worn-wired-earbuds.json">data</a> · <a href="examples/scenes/worn-wired-earbuds.jpg">scene</a> · <a href="examples/worn-wired-earbuds.svg">SVG</a></td>
  </tr>
  <tr>
    <td><img src="examples/cards/faded-brass-key.png" alt="Faded brass key future museum card"><br><strong>Permission to Return</strong> · English · tender<br><a href="examples/faded-brass-key.json">data</a> · <a href="examples/scenes/faded-brass-key.jpg">scene</a> · <a href="examples/faded-brass-key.svg">SVG</a></td>
    <td><img src="examples/cards/used-pencil-stub.png" alt="Used pencil stub future museum card"><br><strong>可消耗思想探针</strong> · 中文 · absurd<br><a href="examples/used-pencil-stub.json">data</a> · <a href="examples/scenes/used-pencil-stub.jpg">scene</a> · <a href="examples/used-pencil-stub.svg">SVG</a></td>
  </tr>
</table>

## Why people try it

The hook is simple: give the future one ordinary object and see what it gets wrong.

- A tangled cable becomes a portable energy umbilical.
- A forgotten umbrella becomes a rain-negotiation device.
- A paper cup becomes evidence of an ancient meeting ritual.

The best result is not random science fiction. It is a specific present-day habit, misunderstood with museum-grade confidence.

It is also a repeatable format, not a one-shot filter: curate one object from a desk, bag, kitchen, or family archive, then build a recognizable series with the same question and card system. Each new object supplies a new human habit; the format stays familiar enough to share.

## Why this is a Codex skill

The creative workflow runs in the user's own Codex environment:

- no hosted inference service maintained by this project;
- no shared API key;
- no account, analytics, or upload endpoint;
- no per-image bill paid by the repository maintainer.

When image generation or editing is available, the skill uses the user's existing capability to place the real object in a future museum scene. Without image generation, it still creates the label, a reusable image prompt, and a typographic share card.

The default scene treats the object as an archaeological survivor: recognizable but plausibly faded, worn, repaired, and photographed obliquely inside a collection space with depth. Ask for `original-condition preservation` when you want the object kept exactly as it is today.

## Install

Ask Codex to install the skill:

```text
$skill-installer install https://github.com/xxwzkdwz/future-museum-curator
```

For local development:

```bash
git clone https://github.com/xxwzkdwz/future-museum-curator.git
cd future-museum-curator
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/skills/future-museum-curator" "$HOME/.agents/skills/future-museum-curator"
```

Codex normally detects skill changes automatically. Restart it if the skill does not appear.

## Try it

Attach a photo or describe an object, then invoke:

```text
$future-museum-curator What will 3026 think this tangled charging cable was?
```

Useful directions:

- `Keep the voice dry and institutionally serious.`
- `Make it tender, not funny.`
- `Preserve every scratch and replace only the background.`
- `Keep the object in its original condition; add no future damage.`
- `Give me three curator-note variants.`
- `Create a vertical share card.`

Every rendered card visibly identifies itself as AI-assisted fiction. The workflow does not claim real provenance, appraisal, valuation, or historical authenticity.

## How it works

```text
object photo or description
        ↓
object-specific human habit
        ↓
fictional future interpretation
        ↓
optional Codex image generation or editing
        ↓
local deterministic SVG renderer
        ↓
self-contained 1080×1440 share card
```

The split is deliberate: AI handles scene transformation and curatorial writing; the local script handles stable typography, disclosure, and export.

## Render a card directly

```bash
python3 skills/future-museum-curator/scripts/render_exhibit_card.py \
  examples/meeting-room-paper-cup.json \
  --output examples/meeting-room-paper-cup.svg
```

The renderer uses only the Python standard library. It accepts UTF-8 Chinese or English copy and can embed a local PNG, JPEG, GIF, WebP, or SVG into a self-contained SVG card.

## Repository map

- `skills/future-museum-curator/SKILL.md`: reusable Codex workflow
- `skills/future-museum-curator/references/`: voice and card-format guidance
- `skills/future-museum-curator/scripts/render_exhibit_card.py`: deterministic SVG renderer
- `examples/`: bilingual input records and generated cards
- `examples/SOURCES.md`: image-generation provenance for the public gallery
- `.codex-plugin/plugin.json`: minimal skills-only plugin manifest
- `scripts/validate_release.py`: repository-level release checks
- `tests/`: renderer behavior and CLI tests

## Development

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_release.py
python3 /path/to/skill-creator/scripts/quick_validate.py skills/future-museum-curator
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
```

The first two commands need only Python 3.11+ and are suitable for any clean CI environment. The final two use the validators bundled with Codex during local development.

## Privacy and boundaries

- Inspect source images for faces, addresses, badges, account details, or other identifiers before reuse.
- Do not introduce unsupported logos or imply that a real museum authenticated the object.
- Treat every date, accession number, institution, and interpretation as fiction.
- Keep employer-confidential, proprietary, or client material out of examples and generated cards.

## License and author

MIT © 2026 [WANG ZHEN](https://github.com/xxwzkdwz)
