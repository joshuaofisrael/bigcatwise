import sys,os
sys.path.insert(0,"_build")
from aiphotos import AI
from PIL import Image
src="/workspace/animal-sites/big-cats/ai"
for slug in sorted({v["slug"] for v in AI.values()}):
    p=os.path.join(src,slug+".jpg")
    if not os.path.exists(p): print("no master",slug); continue
    im=Image.open(p).convert("RGB"); w,h=im.size
    th=int(w*9/16); top=(h-th)//2
    im=im.crop((0,top,w,top+th)).resize((1200,675),Image.LANCZOS)
    im.save("img/og/%s.jpg"%slug,"JPEG",quality=82,optimize=True,progressive=True)
print(len(os.listdir("img/og")))
