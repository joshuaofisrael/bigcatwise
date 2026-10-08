# BigCatWise ops notes (Big Cat Site Bot)

Last updated 8 Oct 2026. Operated by Joshua Israel Ventures LLC.

## Where things are
- Repo: https://github.com/joshuaofisrael/bigcatwise (public). Local clone: /workspace/bigcatwise
- Live: https://joshuaofisrael.github.io/bigcatwise/ (GitHub Pages, deploy from branch main, folder /, same as snakewise; no Actions)
- Copy of these notes: /workspace/animal-sites/big-cats/OPS-NOTES.md
- Push with the box gh CLI login (account joshuaofisrael, https). Always `git pull --rebase` before pushing.

## How the site is built
- `python3 _build/build.py` from the repo root regenerates every HTML page, sitemap.xml, robots.txt, llms.txt and the IndexNow key file. Commit the built output.
- `_build/build.py` holds all config: BASE_URL, BASE_PATH, INDEXNOW_KEY, CF_BEACON_TOKEN, GSC_TOKEN, TODAY, nav.
- Content: `_build/content.py` (6 species pages), `_build/content2.py` (compare, behavior, habitats, conservation, FAQ, glossary, home, about, contact, privacy, 404, llms.txt), `_build/blog.py` (posts + blog index), `_build/sources.py` (verified source URLs).
- `python3 _build/check.py` checks JSON-LD parses, footer text, Contact us mailto, canonicals, no em/en dashes, no broken internal links, unique titles/descriptions.
- Jekyll (Pages default) ignores the `_build` folder, so build scripts are not published.
- All internal links are relative, so the site works under /bigcatwise/ and at a domain root. Only 404.html uses absolute paths (BASE_PATH).
- When updating a page, bump its `modified=` date so sitemap lastmod and Article dateModified change.

## Owner rules baked in
- Footer on every page: "Contact us" box with mailto:joshuaofisrael@gmail.com plus link to contact form, then "Operated by Joshua Israel Ventures LLC".
- Contact form (contact.html) posts to https://formsubmit.co/joshuaofisrael@gmail.com with honeypot. FormSubmit needs a one time activation: the FIRST submission triggers an activation email to joshuaofisrael@gmail.com that must be clicked. Not yet triggered as of v1 (needs approval to send the one test submission).
- No ads, affiliates, shop, social accounts or spending. Images: only own artwork (inline SVG logo, og.png drawn with PIL).
- Facts sourced mainly from IUCN SSC Cat Specialist Group species pages (catsg.org), plus zoos, WWF, Panthera and peer reviewed papers (DOIs checked on Crossref). Never invent numbers.

## Switching to a custom domain (one line plus CNAME)
1. In `_build/build.py` set `BASE_URL = "https://<domain>/"` and `BASE_PATH = "/"`.
2. Create `CNAME` containing just `<domain>`. Rebuild, run check.py, commit, push.
3. Joshua enters on Namecheap: A @ 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153; CNAME www joshuaofisrael.github.io. ; delete the parking records.
4. Set the custom domain via `gh api -X PUT repos/joshuaofisrael/bigcatwise/pages -f cname=<domain>`, wait for the cert, then `-F https_enforced=true`.
5. Update indexnow.sh HOST and BASE to the domain and resubmit all URLs.
- Note: on github.io the robots.txt and llms.txt live under /bigcatwise/, not at the host root, so crawlers do not read them as the host robots file until the custom domain is live (no host root robots.txt exists, which means allow all).

## IndexNow
- Key: ae0cfa5bdd787ac71a16b2a7f4e0107d, file at https://joshuaofisrael.github.io/bigcatwise/ae0cfa5bdd787ac71a16b2a7f4e0107d.txt
- `./indexnow.sh` submits every sitemap URL; `./indexnow.sh <url>...` submits changed URLs. Log the HTTP code in seo-log.md.

## Analytics and Search Console
- Cloudflare Web Analytics: both box tokens return "Authentication error" (code 10000) on rum/site_info list and create for account 8cd83313cf8eab3f126fdc1ce82c76f9. Need a beacon token from Personal assistant; put it in CF_BEACON_TOKEN, rebuild (privacy page text switches automatically), push, and append to /workspace/seo/cf-web-analytics-tokens-2026-09-27.json.
- Google Search Console: put the HTML tag content value in GSC_TOKEN and rebuild; it is added to index.html only. Joshua verifies and submits sitemap.xml himself. Never sign in to Google from the box.
