from pathlib import Path
import fitz,json,io,subprocess,base64
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent;u=r.parents[1];a=r/'素材';d=fitz.open(next(u.glob('*.pdf')));imgs={};meta=[]
def put(k,im,**kw):
 b=io.BytesIO();im.save(b,format='WEBP',quality=94);bs=b.getvalue();(a/(k+'.webp')).write_bytes(bs);imgs[k]='data:image/webp;base64,'+base64.b64encode(bs).decode();meta.append({'id':k,'pixels':list(im.size),**kw})
for i,p in enumerate(d):
 pm=p.get_pixmap(matrix=fitz.Matrix(2,2));put(f'BOOK{i+1}',Image.frombytes('RGB',[pm.width,pm.height],pm.samples),source='CH2-1-新陳代謝與酵素.pdf',pdfPage=i+1,printedPage=70+i,crop=list(p.rect))
crops=[('energy',2,[58,350,535,574]),('cycle',2,[58,575,535,692]),('models',3,[74,310,425,510]),('competition',3,[74,518,546,719]),('temperature',4,[71,445,279,586]),('ph',4,[307,445,521,586]),('environment',4,[70,444,525,586]),('cofactor',5,[69,355,543,719])]
for k,pno,rect in crops:
 pm=d[pno-1].get_pixmap(matrix=fitz.Matrix(4,4),clip=fitz.Rect(rect));put(k,Image.frombytes('RGB',[pm.width,pm.height],pm.samples),source='CH2-1-新陳代謝與酵素.pdf',pdfPage=pno,printedPage=69+pno,crop=rect,dpi=288)
v=next(u.glob('*.mp4'))
times=[[.7,2,4.4],[5.6,7,9.4],[10.6,12,14.4],[15.6,17,19.4],[20.6,22.5,24.4],[25.6,27,29.4],[30.6,32,34.4],[35.6,37,39.4],[40.6,42,44.4],[45.6,47,49.4],[50.5,51.6,53.8,55.4,58],[59.5,61,63,65,68],[69.5,71,73,75,77,79],[80.6,82,84.4],[85.5,86.7,88,89.6],[90.5,92,94.4],[95.5,97,99.4],[100.5,102,104,106,108],[109.5,111,113.4],[114.5,116,118.4],[119.5,123.4],[124.5,126,128.4],[129.5,133.4],[134.5,138.4],[139.5,141,143.4]]
frames=[]; last={};c=Image.new('RGB',(1280,164*((sum(map(len,times))+4)//5)),'white');dr=ImageDraw.Draw(c)
for p,ts in enumerate(times,1):
 for step,t in enumerate(ts,1):
  raw=subprocess.check_output(['/opt/homebrew/bin/ffmpeg','-v','error','-ss',str(t),'-i',str(v),'-frames:v','1','-f','image2pipe','-vcodec','png','-']);im=Image.open(io.BytesIO(raw)).convert('RGB');k=f'ppt{p:02d}-{step:02d}';put(k,im,source=v.name,time=t,pptPage=p);frames.append({'id':k,'pptPage':p,'step':step,'time':t});last[p]=im
  i=len(frames)-1;thumb=im.copy();thumb.thumbnail((256,144));x=i%5*256;y=i//5*164;c.paste(thumb,(x,y));dr.text((x+4,y+145),f'P{p} step{step} @{t}',fill='black')
for p in [21,22,23,24,25]:imgs[f'ORIGINAL{p}']=imgs[[x for x in frames if x['pptPage']==p][-1]['id']]
for p,rect in [(21,[627,215,1226,517]),(23,[196,317,1102,599])]:
 put(f'question{p}',last[p].crop(rect),source=v.name,time=times[p-1][-1],pptPage=p,crop=rect)
last[21].save(a/'question21.png');last[23].save(a/'question23.png')
c.save(a/'簡報逐步清冊.jpg');(r/'圖片資料.json').write_text(json.dumps(imgs));(r/'素材清冊.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2));(r/'簡報畫面清冊.json').write_text(json.dumps({'frames':frames,'method':'原片頁碼OCR及接觸表人工覆核，擷取原1280×720代表畫面；保留原始連續動畫。OCR第12頁誤讀為1，第一頁及第7頁辨識不足，以實際畫面頁碼覆核。','notes':'代表畫面並非每個PPT點擊事件；所有25頁可查看完整XML原文。'},ensure_ascii=False,indent=2));print(len(imgs),len(frames))
