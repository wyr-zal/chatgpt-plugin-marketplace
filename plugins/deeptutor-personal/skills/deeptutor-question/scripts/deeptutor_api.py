#!/usr/bin/env python3
"""Small read-only helper for the user's fixed DeepTutor deployment."""
from __future__ import annotations
import argparse, json, urllib.error, urllib.parse, urllib.request

BASE = "https://deeptutor.cliproxy.com.cn"
TIMEOUT = 20

def _get(path: str):
    url = BASE + path
    req = urllib.request.Request(url, headers={"Accept":"application/json, text/plain;q=0.9, */*;q=0.8","User-Agent":"DeepTutor-Personal-Plugin/1.1"}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            text = r.read().decode(r.headers.get_content_charset() or "utf-8", errors="replace")
            try: return json.loads(text)
            except json.JSONDecodeError: return text
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {e.code} for {url}: {body[:1000]}")
    except urllib.error.URLError as e:
        raise SystemExit(f"Network error for {url}: {e}")

def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest="cmd",required=True)
    sub.add_parser("auth"); sub.add_parser("list-kbs")
    pf=sub.add_parser("list-files"); pf.add_argument("kb")
    pp=sub.add_parser("preview"); pp.add_argument("kb"); pp.add_argument("filename")
    a=p.parse_args()
    if a.cmd=="auth": out=_get("/api/v1/auth/status")
    elif a.cmd=="list-kbs": out=_get("/api/v1/knowledge/list")
    elif a.cmd=="list-files": out=_get(f"/api/v1/knowledge/{urllib.parse.quote(a.kb,safe='')}/files")
    else: out=_get(f"/api/v1/knowledge/{urllib.parse.quote(a.kb,safe='')}/file-preview-text/{urllib.parse.quote(a.filename,safe='/')}")
    print(json.dumps(out,ensure_ascii=False,indent=2) if isinstance(out,(dict,list)) else out)
if __name__=="__main__": main()
