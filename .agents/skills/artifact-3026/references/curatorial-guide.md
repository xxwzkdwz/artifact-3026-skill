# Curatorial voice guide

Use this guide for variants or copy refinement. The artifact should feel specific enough to be screenshotted before it feels clever enough to be explained.

Write in the user's language. English is useful for global sharing and Chinese is equally supported by the renderer; do not translate unless the user asks for both versions.

## Find the human truth

Choose one observable relationship between the object and its owner:

- ritual: what people repeatedly did with it;
- anxiety: what failure or uncertainty it managed;
- belonging: what group or role it signaled;
- neglect: how it was forgotten, postponed, or left unread;
- tenderness: where wear records an ordinary attachment.

The future interpretation may misunderstand the mechanism, but it should correctly sense the human need.

## Voice patterns

### Deadpan

Use measured museum language, precise material descriptions, and one absurd inference stated without emphasis.

Weak: “People used this funny cable all the time.”

Stronger: “Wear near both connectors suggests the cord was handled during recurrent episodes of low-battery anxiety.”

### Tender

Notice traces of use without becoming sentimental. Prefer a concrete mark, fold, stain, repair, or habit over abstract nostalgia.

Weak: “This object reminds us life was beautiful.”

Stronger: “The polished edge shows where one thumb found the same place each morning.”

### Absurd

Make one plausible scholarly error and support it with sincere evidence. Do not stack jokes.

Weak: “It was probably an alien weapon and also a portal.”

Stronger: “Early researchers classified it as a rain-negotiation device because surviving examples were disproportionately recovered from office doorways.”

## Quality check

- Could this label belong only to this object or behavior?
- Is the object recognizable after the visual transformation?
- Does the last line change how the present-day object feels?
- Is every factual-sounding provenance claim clearly inside a fictional frame?
- Is private information absent from the image and label?

## Visual handoff

Keep image generation and typography separate:

1. Generate or edit a clean exhibition scene with no long text.
2. Save that scene locally.
3. Put its local path in `image_path`.
4. Let the renderer own every title, paragraph, and identifier; keep provenance and creative-fiction framing in the surrounding response or source record rather than in the image pixels.

This split makes the scene expressive while keeping the share-card layout reproducible.

Use the archaeological-survivor direction in [visual-direction.md](visual-direction.md) by default. A museum image should visibly carry time: plausible material aging, an oblique view, and a collection environment with history. Switch to original-condition preservation only when the user asks to keep the object intact.
