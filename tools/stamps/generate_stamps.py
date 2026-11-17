#!/usr/bin/env python3
"""Rebuild Some Odd Road pelican numbered stamps from approved raster masters.

Requires Pillow (pip install Pillow). No font files, network, or image generation.

Examples:
  python tools/stamps/generate_stamps.py --start 1 --end 99
  python tools/stamps/generate_stamps.py --start 100 --end 200 --experimental-three-digit

The 2-digit layout is approved and reproduces the existing 01 exactly.
The 3-digit layout is ONLY A PROPOSAL and must be visually approved before use.
"""
import argparse
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
BG_FILE = HERE / 'unnumbered_transparent_master.png'
APPROVED_01 = HERE / 'approved_numbered_01.png'
TWO_CENTERS = (560, 805)
THREE_CENTERS_EXPERIMENTAL = (430, 670, 910)
TOP = 417
ANGLE = 12
ROTATE_CENTER = (670.0, 630.5)


def generate(n, base, glyphs, allow_three_digit):
    if not 1 <= n <= 999:
        raise ValueError('Numbers must be from 1 to 999')
    code = f'{n:02d}' if n <= 99 else str(n)
    if len(code) == 2:
        centers = TWO_CENTERS
    elif len(code) == 3 and allow_three_digit:
        centers = THREE_CENTERS_EXPERIMENTAL
    else:
        raise ValueError('For three-digit numbers, pass --experimental-three-digit after reviewing a prototype')

    layer = Image.new('RGBA', base.size, (0, 0, 0, 0))
    for digit, cx in zip(code, centers):
        glyph = glyphs[digit]
        b = glyph.getbbox()
        left = round(cx - (b[0] + b[2]) / 2)
        layer.alpha_composite(glyph, (left, TOP))
    layer = layer.rotate(
        ANGLE, Image.Resampling.BICUBIC,
        expand=False, center=ROTATE_CENTER, fillcolor=(0, 0, 0, 0)
    )
    result = Image.alpha_composite(base, layer)
    if n == 1:
        reference = Image.open(APPROVED_01).convert('RGBA')
        if result.tobytes() != reference.tobytes():
            raise RuntimeError('FAIL: regenerated 01 differs from approved reference pixel-for-pixel')
    return code, result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', type=int, default=1)
    parser.add_argument('--end', type=int, default=99)
    parser.add_argument('--out', type=Path, default=HERE / 'output' / 'assets' / 'branding')
    parser.add_argument('--experimental-three-digit', action='store_true',
                        help='Allow the unapproved 100-999 three-digit layout')
    args = parser.parse_args()
    if not 1 <= args.start <= args.end <= 999:
        parser.error('Need 1 <= start <= end <= 999')
    if args.end >= 100 and not args.experimental_three_digit:
        parser.error('Three-digit layout is not yet approved; explicitly pass --experimental-three-digit')

    base = Image.open(BG_FILE).convert('RGBA')
    glyphs = {
        str(i): Image.open(HERE / f'digit_{i}.png').convert('RGBA')
        for i in range(10)
    }
    args.out.mkdir(parents=True, exist_ok=True)
    for n in range(args.start, args.end + 1):
        code, result = generate(n, base, glyphs, args.experimental_three_digit)
        result.save(args.out / f'pelican_stamp_{code}.png')
        if n % 20 == 0 or n == args.end:
            print(f'Generated through {code}')
    print(f'Finished {args.end - args.start + 1} stamps in {args.out}')


if __name__ == '__main__':
    main()
