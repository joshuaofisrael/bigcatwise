#!/usr/bin/env bash
# Ping IndexNow for BigCatWise. Usage: ./indexnow.sh URL [URL...]   (no args = every URL in the live sitemap)
# Key file sits at the domain root: https://bigcatwise.com/<key>.txt
# After moving to a custom domain: set BASE to https://<domain>/ and HOST to <domain>.
KEY=ae0cfa5bdd787ac71a16b2a7f4e0107d
HOST=bigcatwise.com
BASE=https://bigcatwise.com/
if [ $# -eq 0 ]; then set -- $(curl -s ${BASE}sitemap.xml | grep -o '<loc>[^<]*' | sed 's/<loc>//'); fi
LIST=$(printf '%s\n' "$@" | python3 -c 'import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))')
curl -s -o /dev/null -w "IndexNow HTTP %{http_code} ($# URLs)\n" -X POST https://api.indexnow.org/indexnow \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"${BASE}$KEY.txt\",\"urlList\":$LIST}"
