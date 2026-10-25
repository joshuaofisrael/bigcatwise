"""AI generated, photorealistic images of the page subject (added 23 Oct 2026). No people, no news events.
Files: img/ai-<slug>-960.webp and -480.webp (3:2). Generated with the Grok Bot image tool, originals in /workspace/animal-sites/big-cats/ai/.
Placed after the Nth </section> of the page body (after=2 by default). They carry no per image caption; the credits and about pages disclose AI imagery."""
import html, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AI = {
 "index.html": dict(slug="home-lioness-savanna", alt="A lioness walking through golden grass on the African savanna at sunrise, with acacia trees behind her", after=1),
 "lion.html": dict(slug="lion-cubs-play", alt="Two young lion cubs play fighting on short grass"),
 "tiger.html": dict(slug="tiger-water", alt="A Bengal tiger wading through shallow water in a green forest stream"),
 "leopard.html": dict(slug="leopard-branch", alt="A leopard resting on a thick, lichen covered tree branch at dusk"),
 "jaguar.html": dict(slug="jaguar-rainforest", alt="A jaguar resting on a mossy branch in dense rainforest"),
 "cheetah.html": dict(slug="cheetah-mound", alt="A cheetah standing on a termite mound and scanning the open plains"),
 "snow-leopard.html": dict(slug="snow-leopard-rocky", alt="A snow leopard with a thick pale coat walking across a rocky mountain slope"),
 "compare.html": dict(slug="leopard-portrait", alt="Close up of a leopard's face showing the small dense rosettes on its golden coat"),
 "behavior.html": dict(slug="lions-shade", alt="A pride of lionesses and cubs resting together in the shade of an acacia tree"),
 "habitats.html": dict(slug="habitat-savanna", alt="African savanna at golden hour with scattered acacia trees and grazing antelope"),
 "conservation.html": dict(slug="conservation-tigers", alt="A tigress and her cub walking side by side along a misty forest track"),
 "blog/do-jaguars-hunt-in-water.html": dict(slug="jaguar-swim", alt="A jaguar swimming across a muddy river with its head and shoulders above the water"),
 "blog/what-do-snow-leopards-eat.html": dict(slug="snow-leopard-ledge", alt="A snow leopard crouched on a snowy rock ledge looking down a mountain valley"),
 "blog/are-tigers-nocturnal.html": dict(slug="tiger-dusk", alt="A tiger walking along a forest track in the blue light of dusk"),
 "blog/how-big-is-a-tigers-territory.html": dict(slug="tiger-territory", alt="A tiger scent marking a tree trunk in a green forest"),
 "blog/never-enter-a-tiger-enclosure.html": dict(slug="tiger-generic", alt="A generic tiger standing in tall green grass and looking at the camera", cap="Generic AI generated image of a tiger. It does not show the incident described in this article."),
 "blog/why-do-so-few-cheetah-cubs-survive.html": dict(slug="cheetah-cubs", alt="A cheetah mother resting in dry grass with three small cubs that still have grey mantle fur"),
 "blog/why-do-male-lions-have-manes.html": dict(slug="lion-mane-portrait", alt="A male lion with a full dark mane resting in the shade of a tree"),
 "blog/can-leopards-live-near-people.html": dict(slug="leopard-scrub", alt="A leopard walking through dry scrub and tall grass at dusk with a rocky hill behind"),
 "blog/what-do-lions-eat.html": dict(slug="lions-shade", alt="A pride of lionesses and cubs resting together in the shade of an acacia tree"),
 "blog/how-often-do-lion-hunts-succeed.html": dict(slug="home-lioness-savanna", alt="A lioness walking through golden grass on the African savanna at sunrise, with acacia trees behind her"),
 "blog/why-do-leopards-drag-their-kills-into-trees.html": dict(slug="leopard-larder-tree", alt="A leopard lying on a tree branch above a carcass wedged in the fork of the tree"),
}
# image cards on the home page tiles: href -> thumbnail slug
TILE_THUMBS = {
 "lion.html": "lion", "tiger.html": "tiger", "leopard.html": "leopard", "jaguar.html": "jaguar", "cheetah.html": "cheetah",
 "snow-leopard.html": "snow-leopard", "compare.html": "ai-leopard-portrait", "behavior.html": "ai-lions-shade",
 "habitats.html": "ai-habitat-savanna", "conservation.html": "ai-conservation-tigers",
}
TILE_ALT = {
 "lion.html": "A male African lion with a golden mane", "tiger.html": "A Bengal tigress sitting on a sandy track",
 "leopard.html": "A leopard resting in a tree", "jaguar.html": "A jaguar walking through grass",
 "cheetah.html": "A cheetah standing in long grass", "snow-leopard.html": "A snow leopard walking past green plants",
 "compare.html": "Close up of a leopard's face", "behavior.html": "Lions resting in the shade of a tree",
 "habitats.html": "African savanna with acacia trees", "conservation.html": "A tigress and her cub in a misty forest",
}

def have(slug):
    return all(os.path.exists(os.path.join(ROOT, "img", "ai-%s-%d.webp" % (slug, w))) for w in (480, 960))

def ai_html(path, rel):
    p = AI.get(path)
    if not p or not have(p["slug"]):
        return ""
    s = rel + "img/ai-" + p["slug"]
    cap = '<figcaption>%s</figcaption>' % html.escape(p["cap"]) if p.get("cap") else ""
    return ('<figure class="photo ai"><img src="%s-960.webp" srcset="%s-480.webp 480w, %s-960.webp 960w" sizes="(max-width: 1000px) 94vw, 940px" '
            'width="960" height="640" alt="%s" loading="lazy" decoding="async">%s</figure>') % (s, s, s, html.escape(p["alt"]), cap)

def insert_ai(body, path, rel):
    fig = ai_html(path, rel)
    if not fig:
        return body
    n = AI[path].get("after", 2)
    parts = body.split("</section>")
    if len(parts) <= n:
        return body + fig
    return "</section>".join(parts[:n]) + "</section>" + fig + "</section>".join(parts[n:])

def tile_thumb(href, rel=""):
    slug = TILE_THUMBS.get(href)
    if not slug:
        return ""
    base = "img/%s" % slug
    if not all(os.path.exists(os.path.join(ROOT, "%s-%d.webp" % (base, w))) for w in (480,)):
        return ""
    return '<img src="%s-480.webp" width="480" height="320" alt="%s" loading="lazy" decoding="async">' % (base, html.escape(TILE_ALT[href]))
