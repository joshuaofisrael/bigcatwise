import re,json,os,glob,html
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files=sorted(f for f in glob.glob(root+'/**/*.html',recursive=True) if '/_build/' not in f and '/outreach/' not in f)
titles={};descs={};bad=0
for f in files:
    s=open(f).read(); rel=os.path.relpath(f,root)
    t=re.search(r'<title>(.*?)</title>',s).group(1); d=re.search(r'name="description" content="(.*?)"',s).group(1)
    titles.setdefault(t,[]).append(rel); descs.setdefault(d,[]).append(rel)
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(b)
    legal = rel in ('terms.html','privacy.html','disclaimer.html','copyright.html')
    vis = re.sub(r'<script.*?</script>|<head>.*?</head>','',s,flags=re.S)
    if 'contact.html">contact form</a>' not in s: print('NO FOOTER CONTACT',rel); bad+=1
    if not legal and re.search(r'(?i)joshua|ventures|all rights reserved',vis): print('LLC/NAME ON NON-LEGAL',rel); bad+=1
    if legal and 'BigCatWise is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company.' not in s: print('NO TRADE LINE',rel); bad+=1
    if rel!='404.html' and 'rel="canonical"' not in s: print('NO CANON',rel); bad+=1
    for ch in ['\u2014','\u2013']:
        if ch in s: print('DASH',repr(ch),rel); bad+=1
    for h in re.findall(r'href="([^"#:]+)(?:#[^"]*)?"',s):
        if h.startswith('/') or h.startswith('http'): continue
        tgt=os.path.normpath(os.path.join(os.path.dirname(f),h))
        if not os.path.exists(tgt): print('BROKEN',rel,h); bad+=1
    text=re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>','',s,flags=re.S)); n=len(text.split())
    print(f'{rel:45s} {n:5d} words  title {len(t):3d}  desc {len(d):3d}')
for k,v in list(titles.items())+list(descs.items()):
    if len(v)>1: print('DUP',k,v); bad+=1
print('problems:',bad)
