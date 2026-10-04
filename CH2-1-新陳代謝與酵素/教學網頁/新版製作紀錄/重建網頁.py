from pathlib import Path
import json
r=Path(__file__).resolve().parent
J=lambda p:json.loads((r/p).read_text())
img=J('圖片資料.json');content=J('內容對照.json');frames=J('簡報畫面清冊.json')['frames'];deck=[[x['id'],x['pptPage'],f"原PPT第{x['pptPage']}頁 · 第{x['step']}步"] for x in frames]
data='const IMG='+json.dumps(img,ensure_ascii=False)+';\nconst CONTENT='+json.dumps(content,ensure_ascii=False)+';\nconst DECK='+json.dumps(deck,ensure_ascii=False)+';\n'
helpers=(r/'資料初始化.js').read_text()
html=(r/'網頁外框.html').read_text().replace('__CSS__',(r/'網頁樣式.css').read_text()).replace('</body>','<script>'+data+helpers+'</script><script>'+(r/'網頁互動.js').read_text()+'</script></body>')
(r.parent/'代謝與酵素驛站_質感新版.html').write_text(html)
print('Generated',len(html.encode()),'bytes;',len(img),'assets;',len(deck),'source frames')
