#!/usr/bin/env python3
"""Build the offline PWA from the markdown notes in notes/.
Emits a self-contained, installable, offline web app into docs/ (GitHub Pages root).

Outputs:
  docs/index.html            self-contained app (notes inlined, search + nav)
  docs/manifest.webmanifest  PWA manifest (installable, standalone)
  docs/sw.js                 service worker (cache-first, full offline)
  docs/icon-192.png/512.png  app icons
"""
import json, re, pathlib, markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)
MAN = json.load(open(NOTES / "manifest.json"))

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"])

def build_docs():
    docs = []
    for key, b in MAN.items():
        for c in b["chapters"]:
            f = NOTES / key / (c["slug"] + ".md")
            if not f.exists():
                continue
            raw = f.read_text()
            body = re.sub(r'^---\n.*?\n---\n', '', raw, count=1, flags=re.S)
            md.reset()
            docs.append({
                "book": key, "bookTitle": b["title"], "subject": b["subject"],
                "num": c["num"], "title": c["title"],
                "html": md.convert(body),
                "text": re.sub(r'\s+', ' ', body).lower()[:20000],
            })
    return docs

def main():
    docs = build_docs()
    books = [{"key": k, "title": v["title"], "subject": v["subject"]} for k, v in MAN.items()]
    payload = json.dumps({"books": books, "docs": docs}, ensure_ascii=False)

    shell = (ROOT / "scripts" / "app_shell.html").read_text()
    (DOCS / "index.html").write_text(shell.replace("__PAYLOAD__", payload))

    manifest = {
        "name": "Psych Notes — MET Prep", "short_name": "Psych Notes",
        "start_url": "./index.html", "scope": "./", "display": "standalone",
        "background_color": "#0f1115", "theme_color": "#0f1115",
        "description": "Offline psychology textbook notes for MET 2026 Clinical Psych prep.",
        "icons": [
            {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
        ],
    }
    (DOCS / "manifest.webmanifest").write_text(json.dumps(manifest, indent=2))

    sw = """const CACHE='psych-notes-v3';
const ASSETS=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)));self.skipWaiting();});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))));self.clients.claim();});
self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));});
"""
    (DOCS / "sw.js").write_text(sw)

    make_icons()
    print(f"built docs/: {len(docs)} chapters across {len(books)} books, "
          f"index.html {(DOCS/'index.html').stat().st_size/1048576:.1f} MB")

def make_icons():
    """Generate simple app icons (book glyph on dark bg). Uses PIL if present, else minimal PNG."""
    try:
        from PIL import Image, ImageDraw, ImageFont
        for sz in (192, 512):
            img = Image.new("RGB", (sz, sz), "#171a21")
            d = ImageDraw.Draw(img)
            d.rounded_rectangle([sz*0.18, sz*0.16, sz*0.82, sz*0.84], radius=sz*0.06, fill="#5b9cff")
            d.rectangle([sz*0.49, sz*0.16, sz*0.51, sz*0.84], fill="#171a21")
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", int(sz*0.30))
            except Exception:
                font = ImageFont.load_default()
            d.text((sz*0.5, sz*0.5), "ψ", fill="#fff", anchor="mm", font=font)
            img.save(DOCS / f"icon-{sz}.png")
    except ImportError:
        # 1x1 fallback so manifest references resolve
        import base64
        png = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
        (DOCS / "icon-192.png").write_bytes(png)
        (DOCS / "icon-512.png").write_bytes(png)

if __name__ == "__main__":
    main()
