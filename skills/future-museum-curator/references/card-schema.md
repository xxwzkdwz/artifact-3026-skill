# Exhibit card schema

The renderer accepts one UTF-8 JSON object.

```json
{
  "museum_name": "MUSEUM OF EVERYDAY ANTIQUITIES",
  "future_year": "3026",
  "artifact_name": "Portable Energy Umbilical",
  "object_identity": "USB-C charging cable · c. 2026 · copper, polymer",
  "interpretation": "Museum interpretation in one short paragraph.",
  "curator_note": "One restrained final turn.",
  "accession_no": "FM-3026-0184",
  "image_path": "/absolute/path/to/exhibit-image.png",
  "accent": "#A7432B"
}
```

Required fields: `artifact_name`, `object_identity`, `interpretation`, and `curator_note`. Values must be strings or values that can be represented as strings. The renderer XML-escapes visible copy.

Optional fields:

- `museum_name` defaults to `MUSEUM OF EVERYDAY ANTIQUITIES`.
- `future_year` defaults to `3026`.
- `accession_no` is derived deterministically when omitted.
- `image_path` may point to a local PNG, JPEG, GIF, WebP, or SVG. Use a local file produced or selected by the user; the renderer never fetches a remote URL. When omitted, the card uses a typographic object monogram.
- `accent` accepts a CSS hex color and defaults to archival red `#A7432B`.

The output always includes `AI-ASSISTED FICTION · AI辅助虚构内容`.

## Layout limits

- The output canvas is fixed at 1080×1440.
- The renderer wraps Chinese and Latin text by approximate visual width.
- Each wrapped line is emitted as an independent SVG text element so local PNG converters do not collapse CJK lines back into one overflowing row.
- If the interpretation and curator note would collide with the footer, rendering stops with a clear error. Shorten the copy rather than removing the disclosure.
- SVG output is self-contained: a local exhibit image is embedded as a data URI.
