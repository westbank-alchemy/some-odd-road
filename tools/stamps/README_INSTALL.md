# Installing the Some Odd Road stamp assets

The **99 approved site PNGs** are distributed in a separate file: `Some_Odd_Road_C059_stamps_01-99_FINAL.zip`. This ZIP contains `assets/branding/pelican_stamp_01.png` ... `pelican_stamp_99.png`, matching the live Jekyll template's naming pattern.

The **production kit** is `Some_Odd_Road_Stamp_Production_Kit.zip`. Unzipping it at the repository root creates `tools/stamps/` with the source PNGs, script and specifications. It does not replace website images by itself.

From Codespaces in `/workspaces/some-odd-road` on branch `main`:

```bash
pwd
mkdir -p ../sor-stamp-backup
cp -n assets/branding/pelican_stamp_*.png ../sor-stamp-backup/ 2>/dev/null || true
unzip -o Some_Odd_Road_C059_stamps_01-99_FINAL.zip 'assets/branding/*' -d .
unzip -o Some_Odd_Road_Stamp_Production_Kit.zip -d .
ls assets/branding/pelican_stamp_[0-9][0-9].png | wc -l
```

Expected result of last line: `99`. This only verifies filenames, not rendering. Browse story pages in the Codespaces preview (your Jekyll site has used a `/some-odd-road/` base URL). In particular review Dispatches 01–05. Check `_layouts/post.html` for the Liquid variable that builds stamp paths. **Do not commit** until the preview looks right.

When happy:

```bash
git status --short
git add assets/branding/pelican_stamp_*.png tools/stamps
git commit -m "Add numbered pelican stamps 01-99 and reproduction sources"
git push origin main
```

The GitHub Pages deployment then serves the stamp files. No special asset registration or GitHub Pages configuration should be needed if the existing `_layouts/post.html` already looks up numbered stamp filenames.

For reproduction in a future Codespace where Pillow may not be installed:

```bash
python -m pip install --user Pillow
python tools/stamps/generate_stamps.py --start 1 --end 99
```

The generated files are created under `tools/stamps/output/assets/branding/` by default. Compare them to the approved files *before copying or replacing anything*. Avoid committing `tools/stamps/output/` by mistake.

For 100–200, see `STAMP_MASTER_SPEC.md`; the three-digit layout has **not** yet been approved. Before publishing 100+ verify `_layouts/post.html` handles three-digit `dispatch_number` without slicing to two digits.
