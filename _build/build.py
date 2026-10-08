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
CF_BEACON_TOKEN = ""      # Cloudflare Web Analytics site token; leave empty until issued
GSC_TOKEN = ""            # Google Search Console HTML tag content value; leave empty until issued
TODAY = "2026-10-08"
OG_IMAGE = BASE_URL + "og.png"

NAV = [("index.html", "Home"), ("lion.html", "Lion"), ("tiger.html", "Tiger"), ("leopard.html", "Leopard"),
       ("jaguar.html", "Jaguar"), ("cheetah.html", "Cheetah"), ("snow-leopard.html", "Snow Leopard"),
       ("which-big-cat-is-it.html", "ID Guide"), ("compare.html", "Compare"), ("behavior.html", "Behavior"), ("habitats.html", "Habitats"),
       ("conservation.html", "Conservation"), ("faq.html", "FAQ"), ("glossary.html", "Glossary"),
       ("blog/index.html", "Blog")]

LOGO = ('<svg role="img" width="34" height="34" viewBox="0 0 64 64" aria-hidden="true"><title>BigCatWise logo</title>'
        '<path d="M12 26 L14 6 L28 18 Q32 17 36 18 L50 6 L52 26 Q56 34 52 44 Q46 58 32 58 Q18 58 12 44 Q8 34 12 26Z" fill="#f0a830"/>'
        '<path d="M22 34 q4 -4 8 0 M34 34 q4 -4 8 0" stroke="#1a140c" stroke-width="3" fill="none" stroke-linecap="round"/>'
        '<path d="M28 44 L36 44 L32 48Z" fill="#1a140c"/><path d="M32 48 v4 M32 52 q-5 3 -9 0 M32 52 q5 3 9 0" stroke="#1a140c" stroke-width="2.2" fill="none" stroke-linecap="round"/>'
        '<path d="M18 22 l5 6 M46 22 l-5 6 M32 20 v8" stroke="#1a140c" stroke-width="3" stroke-linecap="round"/></svg>')

PUBLISHER = {"@type": "Organization", "@id": BASE_URL + "#organization", "name": LEGAL, "legalName": LEGAL, "url": BASE_URL,
             "email": "joshuaofisrael@gmail.com", "brand": {"@type": "Brand", "name": SITE, "logo": OG_IMAGE},
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
            '<p>Questions, corrections or suggestions? Email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a> '
            'or use our <a href="%scontact.html">contact form</a>.</p></section>' % rel +
            '<p>%s: original educational content about lions, tigers, leopards, jaguars, cheetahs and snow leopards. All text and illustrations are original.</p>'
            '<p class="legal">&copy; 2026 Joshua Israel Ventures LLC. All rights reserved. %s is owned and operated by Joshua Israel Ventures LLC.</p>'
            '<p class="legal">Operated by %s</p>'
            '<p class="flinks"><a href="%sterms.html">Terms</a> | <a href="%sprivacy.html">Privacy</a> | <a href="%sdisclaimer.html">Disclaimer</a> | '
            '<a href="%scontact.html">Contact</a> | <a href="%sabout.html">About</a></p></footer>') % (SITE, SITE, LEGAL, rel, rel, rel, rel, rel)

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
                 priority="0.7", headline=None, extra_ld=None, noindex=False, show_dates=True):
        self.__dict__.update(locals()); del self.__dict__["self"]

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
    if GSC_TOKEN and p.path == "index.html":
        head.append('<meta name="google-site-verification" content="%s">' % esc(GSC_TOKEN))
    head.append('<title>%s</title><meta name="description" content="%s">' % (esc(p.title), esc(p.description)))
    if p.noindex:
        head.append('<meta name="robots" content="noindex">')
    else:
        head.append('<link rel="canonical" href="%s">' % canon)
    head.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&amp;display=swap">')
    head.append('<link rel="stylesheet" href="%sstyle.css"><link rel="icon" href="%sfavicon.svg" type="image/svg+xml">' % (rel, rel))
    og_type = "website" if p.kind in ("home", "page") else "article"
    head.append('<meta property="og:type" content="%s"><meta property="og:site_name" content="%s">'
                '<meta property="og:title" content="%s"><meta property="og:description" content="%s">'
                '<meta property="og:url" content="%s"><meta property="og:image" content="%s">'
                '<meta name="twitter:card" content="summary_large_image">' % (og_type, SITE, esc(p.title), esc(p.description), canon, OG_IMAGE))
    blocks = []
    if p.kind == "home":
        blocks.append({"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE_URL, "inLanguage": "en",
                       "publisher": PUBLISHER})
        blocks.append(dict({"@context": "https://schema.org"}, **PUBLISHER))
    elif not p.noindex:
        if p.kind == "article":
            blocks.append({"@context": "https://schema.org", "@type": "Article", "headline": p.headline or p.h1,
                           "description": p.description, "image": OG_IMAGE,
                           "author": {"@type": "Organization", "@id": BASE_URL + "#organization", "name": LEGAL, "url": BASE_URL},
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
        out.append('<p class="meta">By the %s team | Published <time datetime="%s">%s</time> | Last updated <time datetime="%s">%s</time></p>'
                   % (SITE, p.published, fmt(p.published), p.modified, fmt(p.modified)))
    if p.lead:
        out.append('<p class="lead">%s</p>' % p.lead)
    out.append(p.body.replace("{rel}", rel))
    if p.faq:
        out.append('<section class="card" id="faq"><h2>Frequently asked questions</h2>')
        for q, a in p.faq:
            out.append('<h3>%s</h3><p>%s</p>' % (esc(q), a.replace("{rel}", rel)))
        out.append('</section>')
    if p.related:
        out.append('<aside class="card related"><h2>Keep exploring</h2><ul>%s</ul></aside>' %
                   "".join('<li><a href="%s%s">%s</a></li>' % (rel, u, esc(n)) for n, u in p.related))
    if p.sources:
        out.append('<section class="card sources"><h2>Sources</h2><ul>%s</ul><p class="note">Figures are rounded summaries of the sources above. Wild populations are hard to count, so estimates change as new surveys are published.</p></section>' %
                   "".join('<li><a href="%s" rel="noopener">%s</a></li>' % (esc(u), esc(n)) for n, u in p.sources))
    out.append('</main>' + footer(rel) + beacon() + '</body></html>\n')
    return "\n".join(out)

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
            "DuckAssistBot", "Amazonbot"]
    rb = ["User-agent: *", "Allow: /", ""]
    for b in bots:
        rb += ["User-agent: %s" % b, "Allow: /", ""]
    rb.append("Sitemap: %ssitemap.xml" % BASE_URL)
    open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(rb) + "\n")
    # llms.txt
    open(os.path.join(ROOT, "llms.txt"), "w").write(content.llms(BASE_URL))
    # IndexNow key
    open(os.path.join(ROOT, INDEXNOW_KEY + ".txt"), "w").write(INDEXNOW_KEY)
    print("built %d pages, %d sitemap urls" % (len(PAGES), len(urls) + 1))

if __name__ == "__main__":
    import build  # run inside the importable module so content modules share PAGES
    build.main()
