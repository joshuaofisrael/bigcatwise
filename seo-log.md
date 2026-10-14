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
- Screenshots (headless Chrome, flock+timeout): /workspace/animal-sites/big-cats/screens/home-desktop.png, home-mobile.png, games-desktop.png, games-mobile.png. Visual check OK: neon glow borders, hero tiger cub with CC0 credit, games hub three teal tiles, no layout breakage on 1280 or 390.

## 2026-10-11 daily slot (01:33 London)
- Fact article: blog/how-big-is-a-tigers-territory.html ("How big is a tiger's territory?"), targets the question query "how big is a tiger's territory" / "tiger home range size". Cites Goodrich et al. 2010 J Mammal 10.1644/09-MAMM-A-293.1, Simcharoen et al. 2014 Oryx 10.1017/S0030605312001408, Barlow et al. 2011 Oryx 10.1017/S0030605310001456 (all Crossref 200; claims taken from the abstracts). Added to blog index, research page (new "Tiger territory and home range" group), sitemap, llms.txt; linked from tiger.html#life. Commit 4e9a918. IndexNow (4 URLs): HTTP 200.
- SEO action (priority 7, internal linking / topic cluster): no GSC or analytics data yet, so no winners to compound. Made behavior.html#territory ("How big are big cat territories?") the hub for a territory and social life cluster: added contextual links to the tiger territory and lion pride deep dives, and both in its related list. Shortened blog index meta description from 197 to 147 characters so it is not truncated in results. check.py 0 problems.
- Why: the new article and the pride article were only reachable from the blog index and one species page; linking from the topical hub passes relevance and gives crawlers a clear cluster.

## 2026-10-12 daily slot (01:31 London)
- Fact article: blog/why-do-leopards-drag-their-kills-into-trees.html ("Why do leopards drag their kills into trees?"), aimed at the question query "why do leopards drag their kills into trees" / "why do leopards put food in trees". Cites Balme, Miller, Pitman and Hunter 2017 J Anim Ecol 10.1111/1365-2656.12654 and Hayward et al. 2006 J Zool 10.1111/j.1469-7998.2006.00139.x (both Crossref 200; claims taken from the abstracts via Europe PMC and OpenAlex). Added to blog index, research page (new "Leopard feeding and kill caching" group), sitemap, llms.txt; linked from leopard.html#hunting. Commit d1c9356.
- SEO action (priority 5 and 7, topic cluster and internal linking): still no GSC or analytics data, so no winners to compound. Built a hunting and feeding cluster around the new article: contextual link plus related link from behavior.html#hunting (the behavior hub), a visible FAQ entry "Why do leopards put their kills in trees?" on faq.html (included in its FAQPage JSON-LD), and two glossary terms (Food caching, Kleptoparasitism) on glossary.html. Bumped modified dates on those three pages. check.py 0 problems.
- Why: question style query with strong search interest; answering it on the FAQ hub and the behavior hub gives crawlers and AI answer engines several entry points to the deep dive, and the glossary terms cover the jargon people search alongside it.
- IndexNow (8 URLs: new article, blog index, research, leopard, behavior, faq, glossary, home): HTTP 200. Live checks: article 200, FAQ entry live.

## 2026-10-13 daily slot (routine fired late, about 01:50 London; box load 0.5)
- Fact article: blog/what-do-snow-leopards-eat.html ("What do snow leopards eat?"), aimed at the question queries "what do snow leopards eat" / "snow leopard diet" / "snow leopard prey". Cites Lyngdoh, Shrotriya, Goyal, Clements, Hayward and Habib 2014 PLoS ONE 10.1371/journal.pone.0088349 and Shehzad et al. 2012 PLoS ONE 10.1371/journal.pone.0032104 (both Crossref 200; claims taken from the abstracts via Europe PMC), plus Hayward et al. 2006 and the IUCN Cat Specialist Group profile for the leopard comparison and livestock share. Added to blog index, research page (new "Snow leopard diet and prey" group), sitemap, llms.txt; linked from snow-leopard.html#diet. Commit 76a3b9d.
- SEO action (priority 5 and 7, topic cluster and internal linking): still no GSC or analytics data, so no winners to compound. Built the diet cluster around the new article: contextual link plus related link from behavior.html#hunting, a visible FAQ entry "What do snow leopards eat?" on faq.html (in its FAQPage JSON-LD), and glossary term "Scat analysis". Also shortened the research page meta description from 222 to 152 characters and made it stop listing topics, so it no longer grows (and gets truncated) with every new paper group. Bumped modified dates on behavior, faq, glossary and snow leopard pages. check.py 0 problems. Commit ac2755b.
- Why: high volume species question; answering it on the hub pages gives search and AI answer engines several routes to the deep dive, and the research description was the only one over 200 characters.
- IndexNow (8 URLs: new article, blog index, research, snow leopard, behavior, faq, glossary, home): HTTP 200. Live checks: article 200, FAQ entry live.

## 2026-10-14 daily slot (routine fired late, about 01:34 London)
- Fact article: blog/do-jaguars-hunt-in-water.html ("Do jaguars hunt in water?"), aimed at the question queries "do jaguars hunt in water" / "do jaguars eat fish" / "jaguar aquatic hunting". Cites Eriksson et al. 2022 Ecology 10.1002/ecy.3543 and Hayward et al. 2016 Front Ecol Evol 10.3389/fevo.2015.00148 (both Crossref 200; claims taken from the abstracts via OpenAlex), plus the IUCN Cat Specialist Group jaguar profile for the skull bite. Added to blog index, research page (new "Jaguar aquatic hunting and prey" group), sitemap, llms.txt; linked from jaguar.html#water. Commit 2b8f34f.
- SEO action (priority 5 and 7, topic cluster and internal linking): still no GSC or analytics data, so no winners to compound. Built an aquatic hunting cluster around the new article: contextual link plus related link from behavior.html#hunting, a visible FAQ entry "Do jaguars hunt in water?" on faq.html (in its FAQPage JSON-LD), and glossary terms "Aquatic subsidy" and "Frequency of occurrence". Bumped modified dates on behavior, faq and glossary. check.py 0 problems.
- Why: jaguar had no daily deep dive yet; water hunting is a distinctive long-tail query and pairs with the species page #water section. Hub and glossary entry points give search and AI answer engines several routes to the article.
- News: no relevant big-cat news today (skipped).
- Outreach: skipped (no approved edu/Pinterest path yet; default skip).
- IndexNow (8 URLs: new article, blog index, research, jaguar, behavior, faq, glossary, home): HTTP 200. Live checks: article 200 with Pantanal figures live; FAQ entry "Do jaguars hunt in water?" live.
