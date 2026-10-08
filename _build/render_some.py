#!/usr/bin/env python3
"""Render only the named pages (plus optionally sitemap/llms) with the same templates as build.py.
Light alternative to a full rebuild during box blackout hours. Output is identical to build.py for those files.
Usage: python3 _build/render_some.py blog/foo.html index.html [--sitemap] [--llms]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build, content  # noqa
want = [a for a in sys.argv[1:] if not a.startswith("--")]
byp = {p.path: p for p in build.PAGES}
for w in want:
    p = byp[w]; dest = os.path.join(build.ROOT, w); os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w").write(build.render(p)); print("rendered", w)
if "--sitemap" in sys.argv:
    urls = [p for p in build.PAGES if p.sitemap and not p.noindex]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += ['<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (build.url_for(p.path), p.modified, p.priority) for p in urls]
    sm += ['<url><loc>%sllms.txt</loc><lastmod>%s</lastmod><priority>0.3</priority></url>' % (build.BASE_URL, build.TODAY), '</urlset>']
    open(os.path.join(build.ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n"); print("sitemap", len(urls) + 1)
if "--llms" in sys.argv:
    open(os.path.join(build.ROOT, "llms.txt"), "w").write(content.llms(build.BASE_URL)); print("llms.txt")
