#!/usr/bin/env python3
"""Build verification tests for the Psych Notes PWA.
Run: python3 tests/test_build.py  (builds first, then asserts). Exit 0 = all pass."""
import json, re, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NOTES = ROOT / "notes"
EXPECT = {"schultz-personality": 15, "baron-social-psychology": 12, "pinel-biopsychology": 18, "key-acts-law": 1, "cognitive-eysenck-keane": 6, "singh-research-methods": 5}

fails = []
def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL"), name, ("" if cond else "-> " + detail))
    if not cond:
        fails.append(name)

# build fresh
r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build.py")], capture_output=True, text=True)
check("build runs cleanly", r.returncode == 0, r.stderr[-300:])

# source notes present and full-length
for book, n in EXPECT.items():
    mds = sorted((NOTES / book).glob("ch*.md"))
    check(f"{book} has {n} chapter notes", len(mds) == n, f"found {len(mds)}")
    small = [f.name for f in mds if f.stat().st_size < 8000]
    check(f"{book} notes all >=8KB (no duds)", not small, f"undersized: {small}")

# built artifacts exist
for art in ("index.html", "manifest.webmanifest", "sw.js", "icon-192.png", "icon-512.png"):
    check(f"docs/{art} exists", (DOCS / art).exists())

# index.html self-contained + all 45 chapters embedded
if (DOCS / "index.html").exists():
    html = (DOCS / "index.html").read_text()
    check("index.html has no external script src", "src=\"http" not in html and "src='http" not in html)
    ndocs=sum(EXPECT.values()); check(f"index.html embeds {ndocs} docs", html.count('"title":') == ndocs + len(EXPECT), f'count={html.count(chr(34)+"title"+chr(34))}')  # docs + books
    check("index.html registers service worker", "serviceWorker" in html)
    check("index.html has search box", 'id="q"' in html)

# manifest validity
if (DOCS / "manifest.webmanifest").exists():
    m = json.load(open(DOCS / "manifest.webmanifest"))
    check("manifest display standalone", m.get("display") == "standalone")
    check("manifest has 192+512 icons", {i["sizes"] for i in m.get("icons", [])} >= {"192x192", "512x512"})
    check("manifest start_url set", bool(m.get("start_url")))

# sw caches core assets
if (DOCS / "sw.js").exists():
    sw = (DOCS / "sw.js").read_text()
    check("sw caches index.html", "index.html" in sw)
    check("sw has fetch handler", "addEventListener('fetch'" in sw)

print()
if fails:
    print(f"{len(fails)} FAILED: {fails}"); sys.exit(1)
print("ALL TESTS PASSED")
