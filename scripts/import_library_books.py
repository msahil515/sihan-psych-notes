#!/usr/bin/env python3
"""Copy the newer books from the prep site's Library (sihan-met-flashcards/notes-app/content)
into the Textbook Library as their own books, one chapter per section.

Sihan, 06 Aug: "I want all the newer builds to replace the old textbooks in the textbook
library app". These had no shelf here at all: Statistics & Research Methods,
DSM-5-TR (exam cut), RML CET-166 study material, SGT study material, Psycho Didi notes,
and the Final Exam Textbook (all 9 JSS subjects, one chapter per section).

Writes notes/<book>/chNN-<slug>.html (an HTML fragment, used as-is by build.py) and adds
the book to notes/manifest.json. Re-running replaces the same files.

Usage: python3 scripts/import_library_books.py [path/to/notes-app/content]
"""
import html as htmllib, json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"
SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/sihan-met-flashcards/notes-app/content")
SITE = "/sihan-met-flashcards/"  # same origin as this app, so the prep site's figures load as-is

PD = ["history", "research", "biology", "psychopathology", "testing", "interventions", "health",
      "cognitive", "personality", "developmental", "social", "cheatsheets"]

BOOKS = {
    "final-textbook": dict(
        title="The Final Exam Textbook (short edition, all 9 JSS subjects)",
        subject="Final Textbook", final=[f"final-book-{n:02d}" for n in range(1, 10)]),
    "statistics-research": dict(
        title="Statistics and Research Methods (Library edition, 27 sections)",
        subject="Statistics & Research Methods", split=["statistics"]),
    "dsm5tr-exam-cut": dict(
        title="DSM-5-TR, the Exam Cut (81 disorders)",
        subject="DSM-5-TR", split=["dsm5tr"]),
    "psycho-didi": dict(
        title="Psycho Didi Notes (12 subjects, with her diagrams)",
        subject="Psycho Didi Notes", whole=[f"psycho-didi-{s}" for s in PD]),
    "rml-study-material": dict(
        title="RML Clinical Psychology, CET-166 (study material from scratch)",
        subject="RML CET-166", split=["rml-study-material"]),
    "sgt-study-material": dict(
        title="SGT MA Clinical Psychology Entrance (study material from scratch)",
        subject="SGT Entrance", split=["sgt-study-material"]),
}

def article(name):
    s = (SRC / f"{name}.html").read_text()
    m = re.search(r'<article class="wrap nfe-article">(.*)</article>', s, re.S)
    if not m:
        sys.exit(f"{name}: no <article class=\"wrap nfe-article\">")
    a = m.group(1)
    a = re.sub(r'<script\b.*?</script>', '', a, flags=re.S)
    # the in-page contents boxes only jump within one long page; the reader has its own contents
    a = drop_div(a, "toc")
    a = drop_div(a, "booktoc")
    a = a.replace('href="../../', f'href="{SITE}').replace('src="../../', f'src="{SITE}')
    return a

def drop_div(html, cls):
    """Remove every <div class="cls"> ... </div>, counting nested divs."""
    while True:
        m = re.search(rf'<div class="{cls}"[^>]*>', html)
        if not m:
            return html
        depth, i = 1, m.end()
        for t in re.finditer(r'<(/?)div\b[^>]*>', html[i:]):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                html = html[:m.start()] + html[i + t.end():]
                break
        else:
            sys.exit(f"unbalanced <div class={cls}>")

def text(h):
    return htmllib.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip())

def no_em_dash(h):
    """House rule: no em dashes. Psycho Didi's notes use them as label separators."""
    h = h.replace('</b> \u2014 ', '</b>: ').replace('<td>\u2014</td>', '<td>-</td>')
    return h.replace(' \u2014 ', ': ').replace('\u2014', '-')

def unlink_missing_anchors(h):
    """A '#id' link whose target ended up in another chapter would do nothing; keep its text."""
    ids = set(re.findall(r'\bid="([^"]+)"', h))
    return re.sub(r'<a href="#([^"]+)"[^>]*>(.*?)</a>',
                  lambda m: m.group(0) if m.group(1) in ids else m.group(2), h, flags=re.S)

def h2_title(h2):
    h2 = re.sub(r'<span class="cn">.*?</span>', '', h2, flags=re.S)
    t = text(h2)
    return re.sub(r'^\d+\s*[·.:]\s*', '', t)

def slugify(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:48]

def wrap(body, cls="nb"):
    body = unlink_missing_anchors(no_em_dash(body.strip()))
    return f'<div class="nfe-article {cls}">\n{body}\n</div>\n'

def chapters_split(name):
    a = article(name)
    a = re.sub(r'<h1[^>]*>.*?</h1>', '', a, count=1, flags=re.S)
    parts = re.split(r'(?=<h2 class="sec")', a)
    intro, secs = parts[0], parts[1:]
    out = []
    for i, sec in enumerate(secs):
        m = re.match(r'<h2 class="sec"[^>]*>(.*?)</h2>', sec, re.S)
        title = h2_title(m.group(1))
        body = sec[m.end():]
        if i == 0:
            body = intro + body  # the book's orientation (lede, chips, focus) opens chapter 1
        out.append((title, body))
    return out

def chapter_whole(name):
    a = article(name)
    m = re.search(r'<h1[^>]*>(.*?)</h1>', a, re.S)
    return text(m.group(1)), a[:m.start()] + a[m.end():]

def chapters_final(name):
    """One Final Textbook subject (final-book-NN) -> one chapter per numbered section, plus two
    end chapters: the review (revisited case, summary, who's who, key terms) and the past papers
    with the high-yield sheet. Returns (num, title, part, body) tuples; bodies use the tb-* classes."""
    a = article(name)
    a = re.sub(r'<h1[^>]*>.*?</h1>', '', a, count=1, flags=re.S)
    defs = re.search(r'<svg id="tb-defs".*?</svg>', a, re.S).group(0)  # arrowheads + B&W patterns the figures use
    a = a.replace(defs, '')
    n = re.search(r'<span class="tb-chn">Chapter (\d+)</span>', a).group(1)
    subject = text(re.search(r'<h2 class="tb-cht"[^>]*><span class="tb-chn">.*?</span>(.*?)</h2>', a, re.S).group(1))
    a = re.sub(r'<section class="tb-ch"[^>]*>', '', a, count=1)
    a = re.sub(r'<div class="tb-body"[^>]*>', '<div class="tb-body">', a, count=1)
    assert a.rstrip().endswith('</div></section>'), name
    a = a.rstrip()[:-len('</div></section>')]
    parts = re.split(r'(?=<h3 class="tb-s)', a)
    head, secs = parts[0], parts[1:]  # head = lead + PDF links + opener + the opening case story
    out, review, hy = [], [], []
    for sec in secs:
        m = re.match(r'<h3 class="(tb-s[^"]*)" id="([^"]+)">(.*?)</h3>', sec, re.S)
        cls, sid, inner = m.groups()
        if "tb-endh" in cls:
            (hy if sid.endswith(("-pyq", "-hy")) else review).append(sec)
            continue
        num = text(re.search(r'<span class="tb-sn">(.*?)</span>', inner).group(1))
        chip = re.search(r'<span class="tb-hy[^"]*"[^>]*>.*?</span>', inner, re.S)
        title = text(re.sub(r'<span class="tb-(sn|hy)[^"]*"[^>]*>.*?</span>', '', inner, flags=re.S))
        body = (f'<p class="tb-yl">{chip.group(0)}</p>' if chip else '') + sec[m.end():]
        if not out:
            body = head + '</div>' + body  # close the opening story's tb-body before section 1
        out.append((num, title, body))
    part = f"{n} {subject}"
    res = [(num, title, part, defs + body) for num, title, body in out]
    res.append((f"{n} Rev", f"{subject}: case revisited, summary, who's who, key terms", part, defs + "".join(review)))
    res.append((f"{n} HY", f"{subject}: past papers and the high-yield sheet", part, defs + "".join(hy)))
    return res

def main():
    man = json.load(open(NOTES / "manifest.json"))
    for key, spec in BOOKS.items():
        chs = []
        for name in spec.get("split", []):
            chs += chapters_split(name)
        for name in spec.get("whole", []):
            chs.append(chapter_whole(name))
        d = NOTES / key
        d.mkdir(exist_ok=True)
        for old in d.glob("ch*.html"):
            old.unlink()
        entries, size = [], 0
        for n, (title, body) in enumerate(chs, 1):
            slug = f"ch{n:02d}-{slugify(title)}"
            html = wrap(body)
            assert "</script" not in html.lower(), (key, slug)
            (d / f"{slug}.html").write_text(html)
            entries.append({"num": n, "title": f"Ch {n}: {title}", "slug": slug})
            size += len(html)
        fin = [c for name in spec.get("final", []) for c in chapters_final(name)]
        for i, (num, title, part, body) in enumerate(fin, 1):
            slug = f"ch{i:03d}-{slugify(num + ' ' + title)}"
            html = wrap(body, "tbk")
            assert "</script" not in html.lower(), (key, slug)
            assert html.count("<div") == html.count("</div>"), (key, slug)
            (d / f"{slug}.html").write_text(html)
            entries.append({"num": num, "title": title, "part": part, "slug": slug})
            size += len(html)
        man[key] = {"title": spec["title"], "subject": spec["subject"], "chapters": entries}
        print(f"{key}: {len(entries)} chapters, {size/1e6:.2f} MB")
    # the Final Textbook is the main exam book, so it is the first card on the home screen
    man = {"final-textbook": man.pop("final-textbook"), **man}
    (NOTES / "manifest.json").write_text(json.dumps(man, indent=2, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()
