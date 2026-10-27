#!/usr/bin/env python3
"""BigCatWise static site builder.

Usage: python3 _build/build.py   (run from the repo root)

Switching to a custom domain later: set BASE_URL to "https://<domain>/" and BASE_PATH to "/",
add a CNAME file containing the bare domain, rebuild, commit, push. That is the whole change.
"""
import json, os, re, sys, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

# ---- single place to change for a custom domain ------------------------------------------
BASE_URL = "https://bigcatwise.com/"   # must end with /
BASE_PATH = "/"                                   # absolute path prefix, used by 404.html only
# ------------------------------------------------------------------------------------------
SITE = "BigCatWise"
LEGAL = "Joshua Israel Ventures LLC"
INDEXNOW_KEY = "ae0cfa5bdd787ac71a16b2a7f4e0107d"
CF_BEACON_TOKEN = "6b018b7e4d3e4a4cb75ba8fb4a680c46"      # Cloudflare Web Analytics site token; leave empty until issued
ADSENSE_ID = "ca-pub-5681559774142917"
GSC_TOKEN = "2F1VFGs8_miZpH24IQ4s5HMDbRBVf1ToSahl87wllWQ"            # Google Search Console HTML tag content value; leave empty until issued
TODAY = "2026-10-08"
OG_IMAGE = BASE_URL + "og.png"

NAV = [("index.html", "Home"), ("lion.html", "Lion"), ("tiger.html", "Tiger"), ("leopard.html", "Leopard"),
       ("jaguar.html", "Jaguar"), ("cheetah.html", "Cheetah"), ("snow-leopard.html", "Snow Leopard"),
       ("which-big-cat-is-it.html", "ID Guide"), ("compare.html", "Compare"), ("behavior.html", "Behavior"), ("habitats.html", "Habitats"),
       ("conservation.html", "Conservation"), ("faq.html", "FAQ"), ("glossary.html", "Glossary"),
       ("blog/index.html", "Blog"), ("games/index.html", "Games"), ("teachers/index.html", "Teachers"), ("contact.html", "Contact")]

LOGO = ('<svg role="img" width="34" height="34" viewBox="0 0 64 64" aria-hidden="true"><title>BigCatWise logo</title>'
        '<path d="M12 26 L14 6 L28 18 Q32 17 36 18 L50 6 L52 26 Q56 34 52 44 Q46 58 32 58 Q18 58 12 44 Q8 34 12 26Z" fill="#f0a830"/>'
        '<path d="M22 34 q4 -4 8 0 M34 34 q4 -4 8 0" stroke="#1a140c" stroke-width="3" fill="none" stroke-linecap="round"/>'
        '<path d="M28 44 L36 44 L32 48Z" fill="#1a140c"/><path d="M32 48 v4 M32 52 q-5 3 -9 0 M32 52 q5 3 9 0" stroke="#1a140c" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
        '<path d="M18 22 l5 6 M46 22 l-5 6 M32 20 v8" stroke="#1a140c" stroke-width="3" stroke-linecap="round"/></svg>')

# Brand is the publisher everywhere (LLC/name rule, 23-24 Oct 2026); the LLC appears only in the visible text of the 4 legal pages (no parentOrganization in JSON-LD, 25 Oct 2026).
LEGAL_LINE = ("&copy; 2026 Joshua Israel Ventures LLC. All rights reserved. BigCatWise is a trade name of Joshua Israel Ventures LLC, "
              "a Florida limited liability company.")
GA4_ID = "G-HH5ZTBVW42"
CONSENT_REGIONS = '["AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IE","IT","LV","LT","LU","MT","NL","PL","PT","RO","SK","SI","ES","SE","IS","LI","NO","GB","CH"]'
LEGAL_PAGES = {"terms.html", "privacy.html", "disclaimer.html", "copyright.html"}
PUBLISHER = {"@type": "Organization", "@id": BASE_URL + "#organization", "name": SITE, "url": BASE_URL,
             "brand": {"@type": "Brand", "name": SITE, "logo": OG_IMAGE},
             "logo": {"@type": "ImageObject", "url": OG_IMAGE}}

def esc(s):
    return html.escape(s, quote=True)

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def beacon():
    if not CF_BEACON_TOKEN:
        return ""
    return ("<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
            "data-cf-beacon='{\"token\": \"%s\"}'></script><!-- End Cloudflare Web Analytics -->" % CF_BEACON_TOKEN)

def footer(rel):
    return ('<footer><section class="contact-us" aria-labelledby="contact-us"><h2 id="contact-us">Contact us</h2>'
            '<p>Questions, corrections or suggestions? Use our <a href="%scontact.html">contact form</a>.</p></section>' % rel +
            '<p>%s: original educational content about lions, tigers, leopards, jaguars, cheetahs and snow leopards. Text and drawings are original; photos are credited on our photo credits page, and some are AI generated.</p>'
            '<p class="flinks"><a href="%sterms.html">Terms of use</a> | <a href="%sprivacy.html">Privacy</a> | <a href="%sdisclaimer.html">Disclaimer</a> | '
            '<a href="%sdisclaimer.html#affiliate">Advertising disclosure</a> | <a href="%scopyright.html">Copyright and takedown</a> | <a href="%scorrections.html">Corrections</a> | '
            '<a href="%scontact.html">Contact</a> | <a href="%sabout.html">About</a> | <a href="%scredits/">Photo credits</a> | <a href="/privacy.html#google-analytics" data-consent-open>Cookie settings</a></p></footer>') % (SITE, rel, rel, rel, rel, rel, rel, rel, rel, rel)

def header(rel, current):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ''
        links.append('<a href="%s%s"%s>%s</a>' % (rel, href, cur, label))
    return ('<header><a class="brand" href="%sindex.html">%s<span>%s</span></a>'
            '<button class="menu" aria-label="Menu" onclick="document.body.classList.toggle(\'open\')">&#9776;</button>'
            '<nav>%s</nav></header>') % (rel, LOGO, SITE, "".join(links))

def url_for(path):
    if path == "index.html":
        return BASE_URL
    if path.endswith("/index.html"):
        return BASE_URL + path[:-len("index.html")]
    return BASE_URL + path

class Page:
    def __init__(self, path, title, description, h1, body, kind="article", crumbs=None, faq=None,
                 sources=None, related=None, lead=None, published=TODAY, modified=TODAY, sitemap=True,
                 priority="0.7", headline=None, extra_ld=None, noindex=False, show_dates=True, reviewed=None, cite=None):
        self.__dict__.update(locals()); del self.__dict__["self"]

from photos import PHOTOS, photo_html  # noqa: E402
from aiphotos import insert_ai, AI as AI_PHOTOS  # noqa: E402

PAGES = []
def add(*a, **k):
    p = Page(*a, **k); PAGES.append(p); return p

def render(p):
    depth = p.path.count("/")
    rel = "../" * depth
    if p.path == "404.html":
        rel = BASE_PATH
    canon = url_for(p.path)
    head = ['<!doctype html><html lang="en"><head><meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width,initial-scale=1">']
    # Google Consent Mode v2 defaults: denied in EEA/UK/CH, granted elsewhere; set before AdSense. GA4 (GA4_ID, also in /consent.js) is opt-in everywhere.
    head.append('<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
                'gtag("consent","default",{ad_storage:"denied",analytics_storage:"denied",ad_user_data:"denied",ad_personalization:"denied",wait_for_update:500,region:%s});'
                'gtag("consent","default",{ad_storage:"granted",analytics_storage:"granted",ad_user_data:"granted",ad_personalization:"granted"});'
                '</script><script defer src="/consent.js"></script>' % CONSENT_REGIONS)
    # gtag.js and gtag config load only from /consent.js after the visitor accepts the opt-in banner (SnakeWise protocol).
    head.append('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=%s" crossorigin="anonymous"></script>'
                '<meta name="google-adsense-account" content="%s">' % (ADSENSE_ID, ADSENSE_ID))
    if GSC_TOKEN and p.path == "index.html":
        head.append('<meta name="google-site-verification" content="%s">' % esc(GSC_TOKEN))
    head.append('<title>%s</title><meta name="description" content="%s">' % (esc(p.title), esc(p.description)))
    if p.noindex:
        head.append('<meta name="robots" content="noindex">')
    else:
        head.append('<link rel="canonical" href="%s">' % canon)
    # Fonts are self-hosted (fonts/, @font-face in style.css): no third-party font requests, preloaded so text renders in the final font early.
    head.append('<link rel="preload" href="%sfonts/fredoka-latin.woff2" as="font" type="font/woff2" crossorigin>'
                '<link rel="preload" href="%sfonts/nunito-latin.woff2" as="font" type="font/woff2" crossorigin>' % (rel, rel))
    head.append('<link rel="stylesheet" href="%sstyle.css"><link rel="icon" href="%sfavicon.svg" type="image/svg+xml">' % (rel, rel))
    og_type = "website" if p.kind in ("home", "page") else "article"
    # Per page share image: the page's own photo style AI image (img/og/<slug>.jpg, 1200x675) when it has one, else the generic og.png.
    _ai = AI_PHOTOS.get(p.path)
    if _ai and os.path.exists(os.path.join(ROOT, "img", "og", _ai["slug"] + ".jpg")):
        og_img, og_w, og_h, og_alt = BASE_URL + "img/og/" + _ai["slug"] + ".jpg", 1200, 675, _ai["alt"]
    else:
        og_img, og_w, og_h, og_alt = OG_IMAGE, 1200, 630, SITE + ": sourced big cat facts"
    if not p.noindex:
        head.append('<meta name="robots" content="max-image-preview:large">')
    head.append('<meta property="og:type" content="%s"><meta property="og:site_name" content="%s">'
                '<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
                '<meta property="og:url" content="%s"><meta property="og:image" content="%s">'
                '<meta property="og:image:width" content="%d"><meta property="og:image:height" content="%d"><meta property="og:image:alt" content="%s">'
                '<meta name="twitter:card" content="summary_large_image">' % (og_type, SITE, esc(p.title), esc(p.description), canon, og_img, og_w, og_h, esc(og_alt)))
    blocks = []
    if p.kind == "home":
        blocks.append({"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE_URL, "inLanguage": "en",
                       "publisher": PUBLISHER})
        blocks.append(dict({"@context": "https://schema.org"}, **PUBLISHER))
    elif not p.noindex:
        if p.kind == "article":
            blocks.append({"@context": "https://schema.org", "@type": "Article", "headline": p.headline or p.h1,
                           "description": p.description, "image": {"@type": "ImageObject", "url": og_img, "width": og_w, "height": og_h},
                           "author": {"@type": "Organization", "@id": BASE_URL + "#organization", "name": SITE, "url": BASE_URL},
                           "publisher": PUBLISHER, "datePublished": p.published, "dateModified": p.modified,
                           "mainEntityOfPage": canon, "inLanguage": "en"})
        elif p.kind == "page":
            blocks.append({"@context": "https://schema.org", "@type": "WebPage", "name": p.h1, "url": canon,
                           "description": p.description, "publisher": PUBLISHER})
        crumbs = [("Home", BASE_URL)] + [(n, url_for(u)) for n, u in (p.crumbs or [])] + [(p.headline or p.h1, canon)]
        blocks.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
    if p.faq:
        blocks.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in p.faq]})
    # machine-readable sources (20 Oct 2026): every visible source becomes a schema.org citation on the page's Article/WebPage block
    if p.sources and not p.noindex:
        main_block = next((b for b in blocks if b.get("@type") in ("Article", "WebPage")), None)
        if main_block is not None:
            main_block["citation"] = [
                {"@type": "ScholarlyArticle" if "doi.org/" in u else "CreativeWork", "name": html.unescape(re.sub("<[^>]+>", "", n)), "url": u}
                for n, u in p.sources if u.startswith("http")]
    for b in (p.extra_ld or []):
        blocks.append(b)
    head += [ld(b) for b in blocks]
    head.append('</head><body>')
    out = ["".join(head), header(rel, p.path), '<main>']
    if p.kind != "home" and not p.noindex:
        bc = ['<a href="%sindex.html">Home</a>' % rel] + ['<a href="%s%s">%s</a>' % (rel, u, esc(n)) for n, u in (p.crumbs or [])]
        out.append('<p class="crumbs">%s &rsaquo; <span>%s</span></p>' % (" &rsaquo; ".join(bc), esc(p.headline or p.h1)))
    if p.h1:
        out.append('<h1>%s</h1>' % p.h1)
    if p.kind == "article" and p.show_dates:
        rv = p.reviewed or p.modified
        out.append('<p class="meta">By the %s team | Published <time datetime="%s">%s</time> | Last updated <time datetime="%s">%s</time> | '
                   '<span class="reviewed">Last reviewed <time datetime="%s">%s</time></span></p>'
                   % (SITE, p.published, fmt(p.published), p.modified, fmt(p.modified), rv, fmt(rv)))
    elif p.cite:
        rv = p.reviewed or p.modified
        out.append('<p class="meta"><span class="reviewed">Last reviewed <time datetime="%s">%s</time></span></p>' % (rv, fmt(rv)))
    if p.lead:
        out.append('<p class="lead">%s</p>' % p.lead)
    if p.path in PHOTOS and p.kind != "home":
        out.append(photo_html(p.path, rel, lazy=True))
    body = p.body.replace("{rel}", rel).replace("{photo}", photo_html(p.path, rel, lazy=False) if p.path in PHOTOS else "")
    out.append(insert_ai(body, p.path, rel))
    if p.path in LEGAL_PAGES:
        out.append('<p class="legal-owner">%s</p>' % LEGAL_LINE)
    if p.faq:
        out.append('<section class="card" id="faq"><h2>Frequently asked questions</h2>')
        for q, a in p.faq:
            out.append('<h3>%s</h3><p>%s</p>' % (esc(q), a.replace("{rel}", rel)))
        out.append('</section>')
    if p.related:
        out.append('<aside class="card related"><h2>Keep exploring</h2><ul>%s</ul></aside>' %
                   "".join('<li><a href="%s%s">%s</a></li>' % (rel, u, esc(n)) for n, u in p.related))
    if (p.kind == "article" and p.show_dates and not p.noindex) or p.cite:
        out.append(cite_box(p, canon))
    if p.sources:
        out.append('<section class="card sources"><h2>Sources</h2><ul>%s</ul><p class="note">Figures are rounded summaries of the sources above. Wild populations are hard to count, so estimates change as new surveys are published.</p></section>' %
                   "".join('<li><a href="%s" rel="noopener">%s</a></li>' % (esc(u), esc(n)) for n, u in p.sources))
    out.append('</main>' + footer(rel) + beacon() + '</body></html>\n')
    # Link to directory URLs (/, blog/, games/...) rather than .../index.html so internal links match the canonicals (24 Oct 2026).
    return re.sub(r'href="([^"#:]*?)index\.html', lambda m: 'href="%s' % (m.group(1) or "./"), "\n".join(out))

def cite_box(p, canon):
    title = esc(p.headline or p.h1)
    d = datetime.date.fromisoformat(p.modified)
    apa = '%s. (%d, %s %d). <i>%s</i>. %s' % (SITE, d.year, d.strftime("%B"), d.day, title, canon)
    mon = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."][d.month - 1]
    mla = '"%s." <i>%s</i>, %d %s %d, %s.' % (title, SITE, d.day, mon, d.year, canon.replace("https://", ""))
    chi = '%s. "%s." Last modified %s %d, %d. %s.' % (SITE, title, d.strftime("%B"), d.day, d.year, canon)
    return ('<section class="cite" aria-labelledby="cite-h"><h2 id="cite-h">Cite this page</h2>'
            '<p><b>APA:</b> %s</p><p><b>MLA:</b> %s</p><p><b>Chicago:</b> %s</p>'
            '<p class="note">Please check the date you accessed the page and adjust to your teacher\'s or journal\'s style guide.</p></section>') % (apa, mla, chi)

def fmt(d):
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")

def main():
    import content  # noqa: registers pages
    for p in PAGES:
        dest = os.path.join(ROOT, p.path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as f:
            f.write(render(p))
    # sitemap
    urls = [p for p in PAGES if p.sitemap and not p.noindex]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        sm.append('<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (url_for(p.path), p.modified, p.priority))
    sm.append('<url><loc>%sllms.txt</loc><lastmod>%s</lastmod><priority>0.3</priority></url>' % (BASE_URL, TODAY))
    sm.append('</urlset>')
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    # robots
    bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "Perplexity-User",
            "ClaudeBot", "Claude-SearchBot", "Claude-User", "Google-Extended", "Applebot", "Applebot-Extended",
            "DuckAssistBot", "Amazonbot", "CCBot", "anthropic-ai", "Bytespider", "Meta-ExternalAgent", "cohere-ai"]
    rb = ["User-agent: *", "Allow: /", ""]
    for b in bots:
        rb += ["User-agent: %s" % b, "Allow: /", ""]
    rb.append("Sitemap: %ssitemap.xml" % BASE_URL)
    open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(rb) + "\n")
    # llms.txt
    open(os.path.join(ROOT, "llms.txt"), "w").write(content.llms(BASE_URL))
    # ads.txt (Google AdSense authorised sellers, exactly one line)
    open(os.path.join(ROOT, "ads.txt"), "w").write("google.com, pub-5681559774142917, DIRECT, f08c47fec0942fa0\n")
    # IndexNow key
    open(os.path.join(ROOT, INDEXNOW_KEY + ".txt"), "w").write(INDEXNOW_KEY)
    print("built %d pages, %d sitemap urls" % (len(PAGES), len(urls) + 1))

if __name__ == "__main__":
    import build  # run inside the importable module so content modules share PAGES
    build.main()
    # Legal hold gate (RULE.md, 27 Oct 2026): any HOLD_REVIEW makes the build fail, so nothing gets committed or pushed.
    import subprocess, sys
    rc = subprocess.call([sys.executable, os.path.join(ROOT, "_build", "legal_gate.py")])
    if rc:
        print("BUILD BLOCKED: HOLD_REVIEW items, see /workspace/content-review/queue.jsonl. Do not publish."); sys.exit(rc)
