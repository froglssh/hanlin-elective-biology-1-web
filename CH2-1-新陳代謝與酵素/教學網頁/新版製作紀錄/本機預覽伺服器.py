from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[2]
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT),**kw)
 def send_head(self):
  self._range=None
  p=Path(self.translate_path(self.path));value=self.headers.get('Range')
  if value and p.is_file():
   m=re.fullmatch(r'bytes=(\d*)-(\d*)',value)
   if m:
    size=p.stat().st_size;start=int(m[1]) if m[1] else max(0,size-int(m[2]));end=min(size-1,int(m[2])) if m[1] and m[2] else size-1
    if start>=size or end<start:self.send_error(416);return None
    f=p.open('rb');f.seek(start);self.send_response(206);self.send_header('Content-Type',self.guess_type(str(p)));self.send_header('Accept-Ranges','bytes');self.send_header('Content-Range',f'bytes {start}-{end}/{size}');self.send_header('Content-Length',str(end-start+1));self.send_header('Last-Modified',self.date_time_string(p.stat().st_mtime));self.end_headers();self._range=end-start+1;return f
  return super().send_head()
 def end_headers(self):
  if self._range is None:self.send_header('Accept-Ranges','bytes')
  super().end_headers()
 def copyfile(self,source,out):
  if self._range is None:return super().copyfile(source,out)
  left=self._range
  while left:
   chunk=source.read(min(65536,left))
   if not chunk:break
   out.write(chunk);left-=len(chunk)
 def log_message(self,*a):pass
ThreadingHTTPServer(('127.0.0.1',8777),Handler).serve_forever()
