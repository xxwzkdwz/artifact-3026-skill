---
name: artifact-3026
description: Curate an everyday object or photo as a clearly fictional artifact from the future, with a museum label, optional generated exhibit scene, and deterministic share card. Use for creative requests to reimagine, archive, exhibit, or memorialize ordinary present-day objects; do not use for factual appraisal, provenance, valuation, or authentication.
license: MIT
metadata:
  author: WANG ZHEN
  version: "0.2.0"
  repository: https://github.com/xxwzkdwz/artifact-3026
---

# Artifact 3026

Create an emotionally recognizable artifact from ordinary life, not generic science fiction. Reveal what the object means to people today by letting a future curator misunderstand it just enough.

The host agent must be able to read the skill resources. Rendering requires a local execution environment with Python 3.11 or later; image generation or editing remains optional.

## Curate the object

- Start from the supplied photo or description. Inspect an attached image before transforming it.
- Infer harmless creative choices instead of interviewing the user. Default to 1,000 years in the future and a dry, institutionally serious voice.
- Preserve the object's defining silhouette, wear, labels, and imperfections when editing a photo. The result should remain recognizably the user's object.
- Build the joke or emotional turn from one true present-day behavior around the object. Avoid random surrealism, generic dystopia, and lore that could fit any object.
- Treat all provenance, dates, interpretations, accession numbers, and museum institutions as fiction. Never present the result as an appraisal or historical fact.
- Do not expose private details visible in the source photo. Blur, crop, omit, or ask before reproducing faces, addresses, badges, account details, or other identifying information.
- Match the user's language. Keep the fictional framing clear in the accompanying response and structured source data, without placing an AI-generation badge or similar notice inside the finished image or share card.

## Produce the exhibit

Create these elements as one coherent concept:

1. A concise future artifact name: 2-8 English words or roughly 2-12 Chinese characters.
2. A one-line identity: the present-day object, estimated era, and material.
3. A museum interpretation that includes the inferred historical use: 35-65 English words or roughly 70-160 Chinese characters.
4. A curator note that supplies the sharpest joke or emotional turn: 5-14 English words or roughly 10-28 Chinese characters.
5. A fictional accession number in `FM-<future-year>-<four digits>` form.
6. A short visual direction for the exhibit scene.

If the user specifies a tone, honor it. Otherwise choose the tone that best fits the object:

- `deadpan`: scholarly confidence applied to a mundane behavior.
- `tender`: gentle attention to wear, habit, or attachment.
- `absurd`: a plausible institutional misunderstanding with one restrained comic leap.

Read [references/curatorial-guide.md](references/curatorial-guide.md) when the user asks for several variants, a particular voice, or help refining weak copy.

## Create the image

When an available image-generation or image-editing tool exists, create a museum-display image before laying out the card:

- With a source photo, prefer image editing. Keep the silhouette and identity-bearing details faithful while replacing the surroundings with a museum display.
- Without a source photo, generate the artifact from the description, but do not add unsupported logos or identifying marks.
- Keep the exhibit image free of long text. Typography belongs in the deterministic card renderer.
- Unless the user asks for pristine preservation, treat the object as an archaeological survivor rather than a new product: allow plausible age, restrained repair, and material change while keeping it recognizable.
- Default to a three-quarter or slightly oblique view, an off-center composition, a dark stone or oxidized-metal collection space, thick display glass, and a restrained dust beam. Avoid bright, centered, symmetrical, sterile product photography and modern showroom styling.
- If the user asks to preserve the original condition, keep the object's present-day wear and materials intact; change only the setting and light, without adding a thousand years of damage.
- Use an available image-generation tool already accessible to the host agent. Do not require a repository-owned API key, hosted inference service, paid account, or third-party upload.

Read [references/visual-direction.md](references/visual-direction.md) before generating or editing the exhibit scene. It contains the default prompt structure, preservation override, and an example based on a patterned straw cup.

If image generation is unavailable, continue with the original photo when one exists. Otherwise deliver the label, a ready-to-use image prompt, and a typographic share card; do not pretend an image was generated.

## Render the share card

For a shareable artifact, write the exhibit fields to JSON using the schema in [references/card-schema.md](references/card-schema.md), then run:

```bash
python3 <skill-directory>/scripts/render_exhibit_card.py exhibit.json \
  --output future-museum-card.svg
```

Resolve `<skill-directory>` to the folder containing this `SKILL.md`. Pass the generated exhibit image as `image_path` in the JSON. The renderer uses only the Python standard library and creates an editable 1080×1440 SVG.

Show the finished image and provide the label as copyable text. In the surrounding response, identify the concept as a creative fictional exhibit and preserve image provenance in structured source records when available. Do not place AI-generation wording, badges, watermarks, or equivalent notices inside the finished image or share card.

## Completion check

- The present-day object is still identifiable.
- The interpretation contains one object-specific human truth, not a generic future joke.
- The card includes no unsupported logo, private detail, or factual appraisal claim.
- The rendered SVG contains no AI-generation badge, watermark, or equivalent notice.
- The surrounding response still makes clear that the exhibit interpretation is creative fiction, not a real appraisal or historical record.
- If rendering fails because copy is too long, shorten the copy instead of shrinking it below readable size.
