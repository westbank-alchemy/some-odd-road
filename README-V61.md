# Some Odd Road — v6.1 design integration

**Private working update. Not a publication.**

This update uses the user-supplied saved version **6.1** of the former developer's design. The original v6.1 CSS values, rules, masthead SVG, measurements, grain filter, and featured photograph are retained. Jekyll-specific wiring and new pages are separate.

## Changes

- `index.html` — original v6.1 hero, sample dispatch, and ledger; real `_posts/` entries populate the ledger automatically. A real post only replaces the sample featured dispatch when it has `featured: true` in its front matter.
- `_layouts/default.html` — shared original masthead, fonts, paper styling, and footer.
- `_layouts/post.html` — individual stories styled to match v6.1.
- `stories/index.html` and `about/index.html` — themed archive and About pages.
- `_includes/v61-*.html` — original masthead, SVG, and subscribe section.
- `assets/css/v61-original.css` — original v6.1 CSS, preserved intact (not generated anew).
- `assets/css/v61-fonts.css` — the Google Fonts stylesheet bundled with the saved page. The font files themselves are hosted by Google and are **not** included in the ZIP.
- `assets/images/v61-mestia.jpg` — image saved with the original HTML page (temporary for the final site).
- `assets/css/v61-site.css`, `assets/js/v61-site.js` — minimal functional adaptations, separate from the original styling.
- `v61-reference.html` — near-exact saved page reproduction for comparison at `/some-odd-road/v61-reference.html`.

The existing `_posts/`, `_drafts/`, `_config.yml`, and `.gitignore` are **not modified or deleted**. Existing older `assets/css/style.css` is left alone but is no longer loaded.

## Apply in GitHub Codespaces

1. Open the existing Codespace. Save your working files and, ideally, commit them before applying these replacements.
2. Download `SOR-v6.1-Jekyll-update.zip` to your computer.
3. In Codespaces Explorer, drag the ZIP **into the repository's top-level `some-odd-road` folder**, beside `index.html` (not inside `_site`).
4. Open a **second Terminal** (keep Jekyll running in the original), then run:

   ```bash
   unzip -o SOR-v6.1-Jekyll-update.zip -d .
   rm SOR-v6.1-Jekyll-update.zip
   ```

5. Refresh the private preview at the Codespaces port 4000 URL ending in `/some-odd-road/`. If Jekyll is not running, start it with:

   ```bash
   jekyll serve --host 0.0.0.0 --port 4000
   ```

6. Compare `/some-odd-road/` with `/some-odd-road/v61-reference.html`. The reference page retains the original static mockup, while the homepage shows real ledger entries if posts exist.
7. Check a story URL and `/some-odd-road/stories/`. **Do not enable GitHub Pages or make the port public.**
8. After reviewing, commit and sync changes to your existing private repository.

## Publishing new stories

Create `_posts/YYYY-MM-DD-story-slug.md` with:

```markdown
---
layout: post
title: "Story title"
location: "City, Country"
summary: "One-line description."
cover: "/assets/images/example.jpg"
cover_alt: "Description of image"
caption: "Photograph caption."
# featured: true  # Uncomment only when this story should replace the sample hero
---

Write the story here.
```

The original v6.1 content about Mestia and the three original ledger entries are **developer demonstration text**; they are not your published writing. Remove or replace them before public launch. Also, **the subscription box is not connected to a mailing list**; we prevent it from claiming a sign-up occurred.

## Ownership and publication note

This is a private technical integration of a saved third-party prototype provided by the user. Before making a public site from copied code, SVG art, photography, or copy, check your agreement with the original developer and the rights to each asset. A project being publicly viewable does not itself grant reuse rights.
