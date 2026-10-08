# BigCatWise ops notes (Big Cat Site Bot)

Last updated 8 Oct 2026. Operated by Joshua Israel Ventures LLC.

## Where things are
- Repo: https://github.com/joshuaofisrael/bigcatwise (public). Local clone: /workspace/bigcatwise
- Live: https://bigcatwise.com/ (custom domain since 8 Oct 2026; GitHub Pages, deploy from branch main, folder /, same as snakewise; no Actions). www.bigcatwise.com redirects to the apex. The old https://joshuaofisrael.github.io/bigcatwise/ URLs redirect to the domain.
- Copy of these notes: /workspace/animal-sites/big-cats/OPS-NOTES.md
- Push with the box gh CLI login (account joshuaofisrael, https). Always `git pull --rebase` before pushing.

## How the site is built
- `python3 _build/build.py` from the repo root regenerates every HTML page, sitemap.xml, robots.txt, llms.txt and the IndexNow key file. Commit the built output.
- `_build/build.py` holds all config: BASE_URL, BASE_PATH, INDEXNOW_KEY, CF_BEACON_TOKEN, GSC_TOKEN, TODAY, nav.
- Signature asset: which-big-cat-is-it.html (`_build/content3.py`), ID guide plus big cats by region with anchors.
- Content: `_build/content.py` (6 species pages), `_build/content2.py` (compare, behavior, habitats, conservation, FAQ, glossary, home, about, contact, privacy, 404, llms.txt), `_build/blog.py` (posts + blog index), `_build/sources.py` (verified source URLs).
- `python3 _build/check.py` checks JSON-LD parses, footer text, Contact us mailto, canonicals, no em/en dashes, no broken internal links, unique titles/descriptions.
- Jekyll (Pages default) ignores the `_build` folder, so build scripts are not published.
- All internal links are relative, so the site works under /bigcatwise/ and at a domain root. Only 404.html uses absolute paths (BASE_PATH).
- When updating a page, bump its `modified=` date so sitemap lastmod and Article dateModified change.

## Owner rules baked in
- Footer on every page: "Contact us" box with mailto:joshuaofisrael@gmail.com plus link to contact form, then "Operated by Joshua Israel Ventures LLC".
- Contact form (contact.html) posts to https://formsubmit.co/joshuaofisrael@gmail.com with honeypot. FormSubmit needs a one time activation: the FIRST submission triggers an activation email to joshuaofisrael@gmail.com that must be clicked. Not yet triggered as of v1 (needs approval to send the one test submission).
- No ads, affiliates, shop, social accounts or spending. Images: own artwork (inline SVG logo, og.png drawn with PIL, game art) plus licence checked Wikimedia Commons photos (CC0 or CC BY-SA only; see Photos below and /credits/).
- Facts sourced mainly from IUCN SSC Cat Specialist Group species pages (catsg.org), plus zoos, WWF, Panthera and peer reviewed papers (DOIs checked on Crossref). Never invent numbers.

## Custom domain (DONE 8 Oct 2026: bigcatwise.com)
CNAME file contains bigcatwise.com; BASE_URL is https://bigcatwise.com/ and BASE_PATH is /. DNS (Namecheap, set by Joshua): four apex A records to 185.199.108.153 to 185.199.111.153, www CNAME joshuaofisrael.github.io. Steps used, for reference:
1. In `_build/build.py` set `BASE_URL = "https://<domain>/"` and `BASE_PATH = "/"`.
2. Create `CNAME` containing just `<domain>`. Rebuild, run check.py, commit, push.
3. Joshua enters on Namecheap: A @ 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153; CNAME www joshuaofisrael.github.io. ; delete the parking records.
4. Set the custom domain via `gh api -X PUT repos/joshuaofisrael/bigcatwise/pages -f cname=<domain>`, wait for the cert, then `-F https_enforced=true`.
5. Update indexnow.sh HOST and BASE to the domain and resubmit all URLs.
- robots.txt and llms.txt now sit at the domain root, so crawlers read them as the real host files.

## IndexNow
- Key: ae0cfa5bdd787ac71a16b2a7f4e0107d, file at https://bigcatwise.com/ae0cfa5bdd787ac71a16b2a7f4e0107d.txt (indexnow.sh HOST=bigcatwise.com)
- `./indexnow.sh` submits every sitemap URL; `./indexnow.sh <url>...` submits changed URLs. Log the HTTP code in seo-log.md.

## Analytics and Search Console
- Cloudflare Web Analytics: both box tokens return "Authentication error" (code 10000) on rum/site_info list and create for account 8cd83313cf8eab3f126fdc1ce82c76f9. Need a beacon token for bigcatwise.com from Personal assistant; put it in CF_BEACON_TOKEN, rebuild (privacy page text switches automatically), push, and append to /workspace/seo/cf-web-analytics-tokens-2026-09-27.json.
- Google Search Console: put the HTML tag content value in GSC_TOKEN and rebuild; it is added to index.html only. Joshua verifies and submits sitemap.xml himself. Never sign in to Google from the box.

## Other writers
- Personal assistant's scheduled routine publishes a daily fact article to this repo (first run 8 Oct 12:53 London). Always `git pull --rebase` before pushing, and make sure new posts use https://bigcatwise.com/ URLs and are in sitemap.xml.

## 2026-10-08 daily article, games, neon restyle, photos, teachers hub, research, credits
- Daily article: https://bigcatwise.com/blog/why-do-lions-live-in-prides.html ("Why do lions live in prides? It is not mainly about hunting"), papers Packer, Scheel and Pusey 1990 (10.1086/285079), Heinsohn and Packer 1995 (10.1126/science.7652573), Packer et al. 1991 (10.1038/351562a0), all checked on Crossref, doi.org 302. Logged in /workspace/animal-sites/big-cats/daily-facts-log.md.
- Games (commit ae5cbe5): /games/ hub plus Rosette Detective, Cheetah Burst, Range Roundup. Original code and SVG art, credits in games/CREDITS.md. USPTO search 0 hits for each name. localStorage best scores only (bcwRosetteBest, bcwCheetahBurstBest, bcwRangeRoundupBest); no sign up, no trackers. Sound off by default.
- `_build/render_some.py <paths> [--sitemap] [--llms]` renders only the named pages (same output as build.py). Use it during the 14:00 to 19:45 blackout instead of a full rebuild.
- check.py now globs **/*.html recursively (excludes _build and outreach).

### Neon "sunset savanna" palette (style.css)
Cream page #fffaf0, ink #1d1206, muted #5a3d1c, headings #b03a00, links #a33400, electric orange #ff6a00, hot gold #ffc400, amber #ff9a1f, jungle teal #00e6c3, night header/footer #2a1305. Glow (text-shadow/box-shadow) only on headings, accents, buttons, tiles and borders; never on paragraph text; neon colours never used for body text on white. prefers-reduced-motion disables transitions and animations. Distinct from SnakeWise (lime/cyan/pink/violet), MeowWise (pink/lavender/mint), TuskWise (blue/coral), PandasWise (green).
Contrast ratios (WCAG, all AA 4.5:1 or better):
- body #1d1206 on #fffaf0 17.68; on white 18.40
- muted on page / card / tile 9.53 / 9.91 / 9.03
- links on card / page 6.89 / 6.62
- headings on card / page / tile / teal tint / fact card 6.08 / 5.85 / 5.55 / 5.81 / 5.85
- table head #7a2c00 on #ffe2b8 7.69
- button text on orange / gold / teal 6.41 / 11.52 / 11.48
- nav white on night 17.59; brand and footer links gold on night 11.01; footer text #fff3df on night 16.03
- contact box text / links 14.18 / 9.74; correct / wrong answer states 17.15 / 14.99; reviewed badge 17.55; fact green 6.57; myth red 7.29

### Photos
- 14 photos from Wikimedia Commons, licence checked on each file page: 11 CC0, 3 CC BY-SA 3.0. No NC/ND, no people, logos or signage, no AI images. Data: _build/photos.py (PHOTOS_LIST) and /workspace/animal-sites/big-cats/photos/chosen.json.
- Files: img/<slug>-960.webp and -480.webp (3:2, 960x640 and 480x320), made by /workspace/animal-sites/big-cats/photos/batch.py (run under the flock). Inserted after the lead on species pages and key posts (loading=lazy), home hero via `{photo}` (eager, fetchpriority=high). Each has width/height, alt and a credit line.
- Credits page: https://bigcatwise.com/credits/ (file, source page, author, licence link, used on), linked as "Photo credits" in the footer next to the legal links.
- To add a photo: add a dict to PHOTOS_LIST, add it to chosen.json, run batch.py under the flock, rebuild.

### Education
- Teachers hub https://bigcatwise.com/teachers/ with fact sheets, worksheets, answer keys, vocabulary, lesson ideas K-2/3-5/6-8/9-12, games as classroom activities. Teacher search pages: big-cat-adaptations-lesson-plan.html, cheetah-worksheet-3rd-grade.html, lion-pride-lesson-plan.html. Source: _build/edu.py. NGSS codes verified on nextgenscience.org (notes in /workspace/animal-sites/big-cats/edu/ngss-verified.md). LearningResource JSON-LD with educationalLevel and the LLC as publisher.
- Research page https://bigcatwise.com/research/ (9 papers, DOIs checked on Crossref 8 Oct 2026). Add new papers to PAPERS in edu.py.
- Cite this page box (APA, MLA, Chicago) and "Last reviewed" date: automatic on articles; set `cite=True` (and optionally `reviewed=`) for other pages.
- Outreach research (outside the repo, nothing sent or submitted): /workspace/animal-sites/big-cats/edu-targets.csv (33 rows), edu-directories.md, edu-outreach-template.md.
