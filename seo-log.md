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
