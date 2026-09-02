# Visual direction

The default image should look like a surviving object under study, not a product awaiting sale. Keep the real object identifiable while allowing the future museum to leave believable evidence on it.

## Default: archaeological survivor

Preserve identity-bearing features:

- silhouette, proportions, handles, lid, straw, connectors, or other functional parts;
- distinctive pattern placement and a few key motifs;
- present-day repairs or wear that reveal how the object was used.

Allow restrained thousand-year change:

- abrasion, faded pigment, hairline cracks, crazed glaze, oxidized hardware, mineral deposits, dust, or a small conservation repair;
- material aging appropriate to the object rather than generic rust on everything;
- partial loss that does not erase the object's identity or invent a different product.

Default composition and space:

- three-quarter or slightly oblique view rather than a flat front elevation;
- off-center placement with meaningful negative space;
- dark stone, aged timber, or oxidized-metal collection architecture;
- thick vitrine glass, subtle reflections, dust, and one controlled shaft of light;
- quiet archaeological or conservation atmosphere, with background artifacts subordinate to the subject.

Avoid bright white showrooms, centered symmetry, glossy catalogue lighting, spotless new surfaces, sterile modern galleries, neon cyberpunk, dramatic fantasy ruins, invented logos, and long generated text.

## Override: original-condition preservation

When the user asks to keep the object intact, preserve its current materials, color, graphics, scratches, and cleanliness. Do not add future damage, fading, cracks, mineral deposits, or restoration marks. The museum setting may still use oblique composition, controlled light, and archival materials; it should remain documentary rather than commercial.

## Prompt structure

Build the image prompt in this order:

1. **Identity lock:** name the object, silhouette, functional parts, colors, pattern, and details that must remain.
2. **Condition mode:** choose `archaeological survivor` by default or `original-condition preservation` when requested.
3. **Material change:** list only two or three plausible aging or conservation effects.
4. **Display space:** specify vitrine material, surrounding architecture, light, and atmosphere.
5. **Composition:** request a three-quarter angle, off-center placement, and readable negative space.
6. **Exclusions:** no product photo, bright sterile showroom, symmetry, unsupported logo, added text, or identity-changing redesign.

## Example: patterned straw cup

> Edit the supplied dark space-pattern straw cup as an archaeological survivor displayed in 3026. Preserve its tapered silhouette, lid, vertical straw, dark ground, and recognizable astronaut and planet motifs. Add restrained pigment fading, fine surface abrasion, mineral dust around the lid, and one small conservation support; do not replace the pattern or invent lettering. Show it from a three-quarter angle, slightly off center, inside thick glass in a dim stone-and-oxidized-metal collection room with subtle reflections and one dusty light beam. Avoid a bright modern gallery, glossy product lighting, centered symmetry, pristine new plastic, neon science fiction, and generated text.

For the preservation override, replace the condition sentence with:

> Preserve the cup exactly as photographed, including its current color, graphics, cleanliness, and wear; change only the museum setting, camera angle, and light.
