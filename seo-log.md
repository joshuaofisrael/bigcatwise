# BigCatWise SEO log

## Scorecard
| Metric | 7d | 28d | 90d |
|---|---|---|---|
| Impressions (GSC) | n/a | n/a | n/a |
| Clicks (GSC) | n/a | n/a | n/a |
| CTR | n/a | n/a | n/a |
| Avg position | n/a | n/a | n/a |
| Indexed pages | n/a | n/a | n/a |
| Page views (Cloudflare) | n/a | n/a | n/a |

No GSC or analytics data yet (no verification token, no beacon token).

## 2026-10-08 v1 launch
- Pages: home, 6 species pillars (lion, tiger, leopard, jaguar, cheetah, snow leopard), compare (unique asset: big cat comparison table with #row-<species> anchors), behavior, habitats, conservation, FAQ (myths + FAQPage), glossary, about, contact (FormSubmit), privacy, 404, blog index + 5 posts.
- SEO: unique titles and descriptions, canonical, OG + og:image, JSON-LD (WebSite, Organization, Article with dates and image, WebPage, BreadcrumbList, FAQPage), sitemap with lastmod, robots.txt allowing all listed AI and search crawlers, llms.txt, custom 404 (noindex).
- Contact us box with mailto on every page (owner rule 8 Oct 11:00).
- Why: launch scope per BRIEF.md and SNAKE-BOT-PLAYBOOK.md, fixing Snake Bot's gaps (sources, dates, trust pages, og:image, breadcrumbs, lastmod).

## 2026-10-08 signature asset: Which big cat is it?
- Added which-big-cat-is-it.html: quick ID key, all six species side by side, leopard vs jaguar vs cheetah steps, snow leopard/tiger/lion, colour variants, lookalikes, and a big cats by region section with anchors (#africa, #asia, #south-asia, #southeast-asia, #east-asia, #central-asia, #middle-east, #americas, #north-america, #central-america, #south-america, #europe, #australia, #elsewhere). FAQPage JSON-LD for the 5 visible Q&As.
- Linked from nav (ID Guide), home hero and tiles, every species page, compare, habitats, FAQ and the spotted cats blog post; added to llms.txt Tools and sitemap.
- Why: Snake Bot's region by region guide is its strongest asset; this is the big cat equivalent.

## 2026-10-08 live checks (about 12:00 London)
- Pages build: built (commit 184842a). All 24 sitemap URLs return 200; robots.txt, sitemap.xml, llms.txt, IndexNow key file, og.png 200; unknown URL returns custom 404; /_build not published (404).
- Footer "Operated by Joshua Israel Ventures LLC" and Contact us mailto present live.
- Crawler UA check on the ID guide: Googlebot, Bingbot, OAI-SearchBot, GPTBot, PerplexityBot, ClaudeBot, Applebot, Amazonbot, DuckAssistBot all 200.
- IndexNow: ./indexnow.sh submitted all 24 sitemap URLs (host joshuaofisrael.github.io, keyLocation /bigcatwise/<key>.txt): HTTP 202.
- Cloudflare Web Analytics: API create and list return Authentication error (10000) with both box tokens. No beacon yet.
- GSC: no token yet. FormSubmit: not yet activated (first submission sends the activation email).

## 2026-10-08 custom domain bigcatwise.com
- DNS confirmed via dns.google: apex A 185.199.108.153/109/110/111, www CNAME joshuaofisrael.github.io.
- Added CNAME (bigcatwise.com), BASE_URL https://bigcatwise.com/, BASE_PATH /. Rebuilt: canonicals, og:url, og:image, JSON-LD, sitemap, robots Sitemap line, llms.txt now on bigcatwise.com. No github.io or /bigcatwise/ paths left in built files. indexnow.sh HOST switched.
- Pages custom domain set via API; certificate approved for bigcatwise.com and www.bigcatwise.com (expires 2027-01-06); Enforce HTTPS enabled at 12:31 London.
- Live checks 12:31: https://bigcatwise.com/ 200; http and www redirect 301 to https://bigcatwise.com/; old github.io URLs 301 to the domain. robots.txt, sitemap.xml, llms.txt, tiger.html, which-big-cat-is-it.html, blog post, IndexNow key file all 200 over HTTPS. All 24 sitemap URLs 200.
- IndexNow on bigcatwise.com (key at https://bigcatwise.com/ae0cfa5bdd787ac71a16b2a7f4e0107d.txt): 24 URLs submitted, HTTP 202.

## 2026-10-08 restyle + legal pages
- Restyle (Joshua via PA): light savanna theme (sandy #fbf3e4 background, soft orange and gold accents, rounded cards and pill buttons), Fredoka 500/600 from Google Fonts for headings (preconnect, display=swap), CSS only paw print and spot doodles as inline SVG data URIs. All text colours checked for WCAG AA (body 12.4:1, links 5.9:1, headings 6.8:1, muted 6.3:1 on the page background). No URL, content or structure changes apart from the font link tags.
- Legal rule: footer now says "© 2026 Joshua Israel Ventures LLC. All rights reserved. BigCatWise is owned and operated by Joshua Israel Ventures LLC." plus Terms, Privacy, Disclaimer, Contact links; Contact us mailto and "Operated by" line kept. New terms.html and disclaimer.html; privacy rewritten (LLC as data controller, FormSubmit, conditional analytics wording, Google Fonts, no ads or affiliate cookies); About says "BigCatWise is a brand of Joshua Israel Ventures LLC." JSON-LD publisher and author are now Organization "Joshua Israel Ventures LLC" with brand BigCatWise.

## 2026-10-09 neon redesign photos live (about 00:26 London)
- Image batch finally run (it was held during the 8 Oct freeze): 14 Wikimedia Commons photos, 960x640 and 480x320 WebP, 11 CC0 and 3 CC BY-SA 3.0. Licences rechecked on Commons just before download; none had changed.
- Full build (41 pages) and check.py: 0 problems. Every photo has alt, width, height and a credit figcaption; loading=lazy everywhere except the home hero (eager, fetchpriority=high). /credits/ lists all 14.
- Commit 32d9f51 pushed; Pages built. Live 200: /, lion, tiger, leopard, jaguar, cheetah, snow-leopard, /games/, /teachers/, /research/, /credits/, img/home-tiger-cub-960.webp.
- IndexNow: ./indexnow.sh (all 41 sitemap URLs): HTTP 200.
