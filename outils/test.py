import sys,os,glob,re
from playwright.sync_api import sync_playwright
R="/home/claude/atout-vert-idf/"
pages=sys.argv[1:] or ["index.html"]
JS="""()=>{const o=[];const de=document.documentElement;
if(de.scrollWidth>innerWidth+1)o.push('overflowX '+de.scrollWidth);
const sm=new Set();document.querySelectorAll('body *').forEach(e=>{if(!e.childNodes.length)return;let t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());if(!t)return;const r=e.getBoundingClientRect();if(!r.width||!r.height||getComputedStyle(e).display=='none')return;const f=parseFloat(getComputedStyle(e).fontSize);if(f<15.99)sm.add(e.tagName+'.'+e.className+' '+f)});
if(sm.size)o.push('small:'+[...sm].join('|'));
const tp=[];document.querySelectorAll('a,button').forEach(e=>{const r=e.getBoundingClientRect();if(!r.width)return;if(e.classList.contains('skip'))return;if(r.height<43.5||r.width<43.5)tp.push((e.textContent.trim()||e.className).slice(0,20)+' '+Math.round(r.width)+'x'+Math.round(r.height))});
if(tp.length)o.push('tap:'+tp.join('|'));
const sec=[...document.querySelectorAll('section')].map(s=>Math.round(s.getBoundingClientRect().height/innerHeight*100));o.push('sec%:'+sec);
const f=document.querySelector('footer');if(f)o.push('ft%:'+Math.round(f.getBoundingClientRect().height/innerHeight*100));
return o}"""
with sync_playwright() as p:
    b=p.chromium.launch()
    for pg in pages:
        txt=open(R+pg,encoding="utf-8").read()
        refs=re.findall(r'(?:src|href)="((?!https?:|tel:|mailto:|sms:|#|data:)[^"]+)"',txt)
        miss=[r for r in refs if not os.path.exists(R+r.split('#')[0])]
        print(pg,"missing:",miss)
        sz=sum(os.path.getsize(R+r) for r in set(refs) if r.startswith('images/') and os.path.exists(R+r))
        print(pg,"imgKB:",sz//1024)
        for w,h in [(360,740),(390,844),(414,896),(768,1024),(821,900),(980,800),(981,800),(1280,800),(1920,1000)]:
            c=b.new_page(viewport={'width':w,'height':h}); c.goto("file://"+R+pg); c.wait_for_timeout(400)
            r=c.evaluate(JS); print(pg,w,r)
            if pg=="index.html" and w==390 and "--shot" in os.environ.get("X",""):
                c.screenshot(path="/tmp/w/m390.png",full_page=True)
            c.close()
    b.close()
