# Some Odd Road — starter website

A lightweight, newspaper-inspired starter site based on the supplied visual reference. It uses **GitHub Pages + Jekyll**, with no paid hosting, no web fonts, no trackers, and no external image dependencies. It is a *working starting point*, not the full existing developer design.

## Publish it using GitHub Pages

1. Create a **new repository named `some-odd-road`** in **your own GitHub account**. (Do not replace an existing `USERNAME.github.io` repository.)
2. Extract this ZIP. Upload the **files and folders inside** `some-odd-road-starter`, not the ZIP itself, to the new repo via **Add file → Upload files**, then commit to `main`. Ensure `_config.yml`, `index.html`, `_layouts`, `assets`, and the other folders are at the **repository root**.
3. In the repository go to **Settings → Pages → Build and deployment → Source → Deploy from a branch**. Set **Branch: `main`**, folder **`/(root)`**, and save.
4. The site should appear at `https://YOUR-USERNAME.github.io/some-odd-road/`. GitHub says publication can take up to about 10 minutes.
5. If the repo name is **not** `some-odd-road`, update `baseurl` in `_config.yml` to `/<actual-repo-name>` before deploying.

**Important privacy note:** GitHub Pages sites are public once published. Do not upload private or unpublished content to a public repository unless you are comfortable with that. Nothing is published by merely unzipping or inspecting these files.

## Add your first story

1. Open `_drafts/story-template.md`. Copy its content to a new file in a folder named `_posts`.
2. Name it `YYYY-MM-DD-your-story-title.md` (e.g. `2026-11-14-crossing-the-border.md`). Use a real date in the filename.
3. Edit `title`, `location`, `summary`, and the Markdown text. Remove the instructional lines.
4. Optional: upload your own photograph to `assets/images/`, uncomment `cover:` in the story front matter, and point it to `/assets/images/filename.jpg`.
5. Commit. Jekyll automatically adds the new story to the homepage and **All Stories** page. The newest-dated story is featured.

Do not put drafts in `_posts` until you want them publicly visible. Files in `_drafts` are ignored by the normal build.

## Make the site yours

- Masthead, top navigation and footer: `_layouts/default.html`
- Colors, fonts, spacing, and responsive layout: `assets/css/style.css`
- Homepage feature and latest story list: `index.html`
- Story archive: `stories/index.html`
- About: `about/index.html`
- Story template: `_layouts/post.html`
- Temporary illustrated cover: `assets/images/landscape-placeholder.svg`
- URL configuration: `_config.yml`

## Custom domain later

Once you purchase/configure a domain, update `baseurl: ""` and `url: "https://your-domain.example"` in `_config.yml`, then follow GitHub's custom-domain setup instructions. Do not remove the old URL until your new domain is working.

## Local preview

To preview the Jekyll-based version locally you need Jekyll installed. GitHub Pages will compile it automatically after deployment. A separate desktop preview screenshot is supplied alongside the ZIP.
