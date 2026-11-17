# Some Odd Road — numbered pelican stamp master specification

**Status:** 01–99 APPROVED, 100–200 PROPOSED (not approved).  
**Last assembled:** 16 November 2026.  
**Source of truth:** raster files in this directory; the PNG masters are more authoritative than any prose description.

## Visual design — LOCKED

- Circular, distressed Bulgarian pelican seal, with adult facing left, chicks and nest; original wording: upper **Човек се учи**, lower **докато е жив**.
- Adult, chicks, nest, outer/inner ring, text, ink flecks **do not change between stamps**.
- Pelican and nest intentionally very faded relative to the outer ring and digits.
- Ink uses the existing pixels of the approved master; nominal brick-red ink **#962B22 (RGB 150, 43, 34)**; preserve transparency and source pixel color variations rather than recoloring.
- Distressed numerical glyph artwork derived from **C059 Bold**. Use the included `digit_0.png` through `digit_9.png` pixels, not text rendered from a font and not an image generator.
- All digits have **the same source sizes / shapes**, no per-number scaling, drawing, stretching or re-centering.
- Number pairs share a baseline **before rotation**; the pair is rotated as **one layer by 12° counterclockwise**.
- Distressed ink detail lives in the individual transparent digit PNGs and **must not be regenerated** for exact reproductions.

## Exact two-digit production geometry — APPROVED 01–99

| Setting | Value |
|---|---|
| Canvas | **1322 x 1190 px**, RGBA PNG, transparent background |
| Unnumbered base | `unnumbered_transparent_master.png` (exact asset) |
| Digit sources | `digit_0.png` … `digit_9.png` (360 x 440 px RGBA canvases) |
| Two-digit numbers | `01`–`99` (always zero-pad to two characters) |
| Right/left digit anchors (image X) | **560**, **805** px |
| Top of each full digit image (Y) | **417** px |
| Per-digit X placement | `round(anchor_x - (digit_alpha_bbox_left + digit_alpha_bbox_right)/2)` |
| Rotation | **+12°** via Pillow `Image.rotate`, bicubic, `expand=False` |
| Rotation center | **(670.0, 630.5)** |
| Rotation fill | `(0, 0, 0, 0)` |
| Composition | alpha-composite both digit PNGs onto one transparent layer; rotate layer; alpha-composite over base |
| Output names | `assets/branding/pelican_stamp_01.png` … `_99.png` |
| Output alpha/color | Original raster channels preserved, except for standard alpha compositing with glyphs |

**Regression gate:** Recreating stamp 01 must be **pixel-identical** to `approved_numbered_01.png`. If it isn't, stop; do not silently adapt the design. The program does this automatically.

**Why the canvas differs from the old reference PDF:** `pelican_specs.pdf` described the historical/original **1254×1254** reference. The finalized, approved website asset is **1322×1190**. For new numbered output, **use the finalized dimensions and assets above**.

## 100–200 — NOT YET LOCKED

Three-digit numbers require an extra slot. The provided script offers a **provisional** layout placing three full-size glyphs at X centers **430, 670, 910** while keeping the same Y anchor 417 and rotation center/angle. This is only a proposal for review; **not a guarantee that 100–200 matches the approved visual balance**. A future session should preview **100, 111, 188, 200** at actual stamp display size, inspect overlap/ring clearance, and approve or refine three-digit positions as a *single shared rule* before batch generation. Do not modify the source glyphs or the approved two-digit geometry.

To generate only review prototypes:

```bash
python tools/stamps/generate_stamps.py --start 100 --end 111 --experimental-three-digit
```

To generate the whole 100–200 set **only after prototype approval**:

```bash
python tools/stamps/generate_stamps.py --start 100 --end 200 --experimental-three-digit
```

## Website integration

- Site repo: `westbank-alchemy/some-odd-road` (Jekyll / GitHub Pages).
- Numbered image files belong at `assets/branding/pelican_stamp_XX.png` for 01–99, e.g. `/assets/branding/pelican_stamp_05.png`.
- Existing `_layouts/post.html` chooses a numbered image using `dispatch_number` / `stamp_number`. Verify the formatting of that variable when you first use **100**; it must not truncate numbers to two digits or insert a leading `0` into three-digit numbers.
- To add a story in 01–99, set `dispatch_number` in that post's YAML front matter; the template should select the corresponding file without changing the layout.
- Preview the site first, including mobile; do not modify the original stamp assets to compensate for CSS issues.

## Files and reproducibility

The following source files are sufficient to regenerate approved 01–99 in Python with Pillow: `unnumbered_transparent_master.png`, ten `digit_N.png` files, and `generate_stamps.py`. `approved_numbered_01.png` is included as the exact regression reference. **No font file is needed or should be distributed.** Retain `SHA256SUMS.txt` for provenance of this specific asset set.

See `TASK_FOR_FUTURE_CHAT.txt` for the ready-to-paste prompt and `README_INSTALL.md` for Codespaces instructions.
