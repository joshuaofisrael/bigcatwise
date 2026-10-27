"""Pre-publish legal hold gate (JI Ventures rule, Joshua, 27 Oct 2026 18:13 London).
Rule text: /workspace/content-review/RULE.md. Runs on every built HTML page (and any extra paths given).
Any flag => status HOLD_REVIEW: one JSON line per item appended to /workspace/content-review/queue.jsonl,
exit code 1, so build.py, the git pre-commit / pre-push hooks and CI refuse to publish.
A flagged file passes ONLY if /workspace/content-review/approvals.jsonl has an entry from Joshua for
site=bigcatwise.com, that draft_path and the exact sha256 of the file. Bots must never write approvals.
Code-enforced: 2 (contact data), 3 (image rights record), 4 (blog source links), 6 (election wording),
8 (legal notice holds list), plus keyword tripwires for 1, 5, 7. Final judgement on 1, 4, 5, 7 stays human.
Usage: python3 _build/legal_gate.py [--no-queue] [paths...]"""
import re, os, sys, json, glob, hashlib, datetime, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CR = os.environ.get("CONTENT_REVIEW_DIR", "/workspace/content-review")
QUEUE, APPROVALS = os.path.join(CR, "queue.jsonl"), os.path.join(CR, "approvals.jsonl")
HOLDS = os.path.join(ROOT, "_build", "legal_holds.json")   # rule 8: paths under notice / embargo / complaint
SITE = "bigcatwise.com"
LEGAL = {"terms.html", "privacy.html", "disclaimer.html", "copyright.html", "corrections.html", "contact.html"}
EMAIL_OK = {"privacy.html", "disclaimer.html", "copyright.html", "corrections.html", "terms.html"}

def mod(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "_build", name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def licensed_images():
    """Rule 3: image files with a documented rights record."""
    ok = set()
    for p in mod("photos").PHOTOS_LIST:              # Wikimedia CC0 / CC BY-SA, licence page recorded
        if p.get("lic") and p.get("page") and p.get("licurl"):
            ok.add(p["slug"])
    ai = mod("aiphotos")                              # our own generated images, originals kept
    for p in ai.AI.values(): ok.add("ai-" + p["slug"])
    return ok

R1 = re.compile(r"(?i)\b(fraud\w*|corrupt\w*|convicted|indicted|arrested|charged with|lawsuit|sued|scam\w*|embezzl\w*|misconduct|dishonest\w*|cover[ -]?up|abused? by|accused of|allegedly)\b")
R5 = re.compile(r"(?i)\b(guaranteed returns?|you should (buy|invest|sell)|investment advice|dosage|take \d+ ?mg|legal advice for your|how to (make|build) (a )?(weapon|explosive|trap|snare|poison))\b")
R6 = re.compile(r"(?i)\b(election|ballot|polling (place|station|location)|voter registration|register to vote|voting (day|date|deadline)|certified results?|absentee|primary vote)\b")
R7 = re.compile(r"(?i)\b(official (partner|site of)|endorsed by|in partnership with|accredited by|approved by (the )?(IUCN|WWF|AZA|Panthera)|breaking news|shocking|exclusive)\b")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"(?<![\d.])(\+?\d{1,2}[ .-])?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}(?!\d)")
STREET = re.compile(r"(?i)\b\d{2,5} [A-Z][a-z]+ (Rd|Road|St|Street|Ave|Avenue|Dr|Drive|Lane|Ln|Blvd)\b")

def visible(s):
    s = re.sub(r"10\.\d{4,9}/[^\s\"<]+", " ", s)
    return re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<script.*?</script>|<style.*?</style>|<head>.*?</head>", " ", s))

def ctx(text, m, w=60):
    return " ".join(text[max(0, m.start()-w): m.end()+w].split())

def check_file(path, rel, imgs, holds):
    s = open(path, encoding="utf-8").read(); text = visible(s); flags = []
    hd = re.search(r"(?s)<head>.*?</head>", s); hd = hd.group(0) if hd else ""
    head = " ".join(re.findall(r'(?s)<title>(.*?)</title>', hd) + re.findall(r'name="description" content="(.*?)"', hd) + re.findall(r'property="og:(?:title|description)" content="(.*?)"', hd))
    full = text + " " + head
    legal = rel in LEGAL
    if rel in holds: flags.append((8, "path listed in _build/legal_holds.json: " + holds[rel], "Wait for Joshua; do not republish."))
    if not legal:
        for m in R1.finditer(full): flags.append((1, ctx(full, m), "Joshua to review; do not soften wording to pass."))
        for m in R5.finditer(full): flags.append((5, ctx(full, m), "Remove personalised advice / dangerous instructions or get approval."))
        for m in R7.finditer(full): flags.append((7, ctx(full, m), "Check headline strength / implied affiliation."))
    for m in R6.finditer(full): flags.append((6, ctx(full, m), "Needs current election authority confirmation."))
    if rel not in EMAIL_OK:
        for m in EMAIL.finditer(text): flags.append((2, m.group(0), "Remove contact detail; use the contact form."))
    for m in PHONE.finditer(text): flags.append((2, m.group(0), "Remove phone number."))
    if not legal:
        for m in STREET.finditer(text): flags.append((2, m.group(0), "Remove street address."))
    for src in re.findall(r'(?:src|srcset)="([^"]+)"', s):
        for u in src.split(","):
            u = u.strip().split(" ")[0]
            if u.startswith(("http:", "https:", "//")) and "googletagmanager" not in u and "googlesyndication" not in u and not u.endswith(".js"):
                flags.append((3, u, "Hotlinked asset without rights record; drop it or document permission."))
            mm = re.search(r"img/([a-z0-9-]+?)-(480|960)\.webp$", u)
            if mm and mm.group(1) not in imgs:
                flags.append((3, u, "No licence record in photos.py/aiphotos.py; drop the image or document permission."))
    if rel.startswith("blog/") and rel != "blog/index.html":
        ext = [h for h in re.findall(r'href="(https?://[^"]+)"', s) if "bigcatwise.com" not in h and "creativecommons" not in h and "wikimedia" not in h]
        if not ext: flags.append((4, "no external source link in article", "Add sources actually accessed, or hold."))
    return s, flags

def approved(rel, sha):
    if not os.path.exists(APPROVALS): return False
    for line in open(APPROVALS):
        try: a = json.loads(line)
        except Exception: continue
        if a.get("site") == SITE and a.get("draft_path") == rel and a.get("sha256") == sha and str(a.get("approved_by", "")).lower().startswith("joshua"):
            return True
    return False

def main(argv):
    noq = "--no-queue" in argv; paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        paths = sorted(f for f in glob.glob(ROOT + "/**/*.html", recursive=True) if "/_build/" not in f and "/outreach/" not in f)
    imgs = licensed_images()
    holds = json.load(open(HOLDS)) if os.path.exists(HOLDS) else {}
    seen = set()
    if os.path.exists(QUEUE):
        for line in open(QUEUE):
            try: q = json.loads(line); seen.add((q.get("site"), q.get("draft_path"), q.get("sha256"), q.get("rule")))
            except Exception: pass
    held = 0
    for p in paths:
        p = os.path.abspath(p); rel = os.path.relpath(p, ROOT)
        s, flags = check_file(p, rel, imgs, holds)
        if not flags: continue
        sha = hashlib.sha256(s.encode()).hexdigest()
        if approved(rel, sha): print("APPROVED (exact version)", rel); continue
        held += 1
        t = re.search(r"<title>(.*?)</title>", s); title = t.group(1) if t else rel
        srcs = sorted(set(h for h in re.findall(r'href="(https?://[^"]+)"', s) if "bigcatwise.com" not in h))[:15]
        for rule in sorted(set(f[0] for f in flags)):
            fl = [f for f in flags if f[0] == rule]
            print("HOLD_REVIEW rule %d %s: %s" % (rule, rel, " | ".join(f[1] for f in fl[:3])))
            key = (SITE, rel, sha, rule)
            if noq or key in seen: continue
            seen.add(key)
            with open(QUEUE, "a") as q:
                q.write(json.dumps(dict(ts=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), site=SITE, bot="Big Cat Site Bot",
                    title=title, flagged=" | ".join(f[1] for f in fl[:5]), rule=rule, sources=srcs, suggestion=fl[0][2],
                    draft_path=rel, sha256=sha, status="HOLD_REVIEW")) + "\n")
            if rule == 8: print("RULE 8: tell Personal assistant immediately, priority")
    print("legal_gate: %d file(s) checked, %d held" % (len(paths), held))
    return 1 if held else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
