#!/usr/bin/env python3
"""Pinel topic-coverage check for the rewritten Pinel chapters.

The topic list is every heading in the contents of Pinel & Barnes,
Biopsychology 11th ed. (chapters 1-18, down to the smallest run-in heading,
cases included; the end-of-chapter "Themes Revisited" / "Key Terms" and bare
"Conclusion" / "Part One/Two" dividers are left out).

  python3 scripts/pinel_coverage.py extract /path/to/pinel11.pdf
      rebuild scripts/pinel_topics.json from the PDF's contents (needs PyMuPDF)
  python3 scripts/pinel_coverage.py page OLD_CHAPTERS_DIR
      write the report page notes/pinel-biopsychology/ch19-coverage-check.md
      (OLD_CHAPTERS_DIR = the pre-rewrite chapters, e.g. git archive b2a30d8)
  python3 scripts/pinel_coverage.py [--json out.json] [--dir chapters_dir]
      score each chapter in notes/pinel-biopsychology (or another copy of it,
      e.g. an older version exported from git)

A topic counts as covered when either
  (a) its key words all turn up close together in the chapter (within
      WINDOW words; topics with 4+ key words need 3 in 4 of them), or
  (b) scripts/pinel_coverage_verified.json gives a passage for it and that
      passage really is in the chapter text (checked here, word for word).
"""
import json, math, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = ROOT / "scripts" / "pinel_topics.json"
VERIFIED = ROOT / "scripts" / "pinel_coverage_verified.json"
CHAPTERS = ROOT / "notes" / "pinel-biopsychology"
WINDOW = 120

STOP = set("""a an the of and or in on to for from by with as at into onto about
between among within without through during after before over under than then
is are was were be been being it its this that these those there their they
them his her he she we our you your who whom whose which what when where why
how do does did can could should would will may might must not no nor so
anyway versus vs also more most much many some any all each other another
one two three four five first second part using use used role""".split())


def norm(text):
    text = text.replace("’", "'").replace("‘", "'").lower()
    text = re.sub(r"'s\b", "", text).replace("n't", " not")
    return re.findall(r"[a-z0-9]+", text)


# The rewrite uses British spelling, Pinel uses American: fold both to one.
UK_US = [(r"our(al|s|ed|ing)?$", r"or\1"), (r"is(e|ed|es|ing|ation|ations|er|ers)$", r"iz\1"),
         (r"^haem", "hem"), (r"aemia$", "emia"), (r"^oestr", "estr"), (r"^defence$", "defense"),
         (r"tre$", "ter"), (r"ogue$", "og")]


def stem(w):
    if len(w) > 5:
        for pat, rep in UK_US:
            w = re.sub(pat, rep, w)
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 5 and w.endswith("ing"):
        return w[:-3]
    if len(w) > 4 and w.endswith("ed"):
        return w[:-2]
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def keywords(title):
    return sorted({stem(w) for w in norm(title) if w not in STOP and len(w) > 1})


def found_close(positions, need):
    """Word positions where `need` distinct key words occur within WINDOW words."""
    hits = sorted((p, k) for k, ps in positions.items() for p in ps)
    count, lo, starts = {}, 0, []
    for p, k in hits:
        count[k] = count.get(k, 0) + 1
        while p - hits[lo][0] > WINDOW:
            k0 = hits[lo][1]
            count[k0] -= 1
            if not count[k0]:
                del count[k0]
            lo += 1
        if len(count) >= need:
            starts.append(p)
    return starts


END_MATTER = ("Worked example", "MCQ traps", "Likely exam points", "Key terms",
              "How the chapter fits together", "Themes Revisited", "Chapter ")


def best_section(starts, line_of, topic):
    """Section of the rewrite that treats the topic: a teaching section before end matter
    (exam points, MCQ traps...), then the one sharing most key words with the topic and its
    Pinel module heading, then the one where the topic's words turn up most."""
    tk = set(keywords(topic["title"]) + keywords(topic["section"]))
    secs = [line_of[s] for s in starts]
    return max(secs, key=lambda sec: (bool(sec) and not sec.startswith(END_MATTER),
                                      len(tk & set(keywords(sec))), secs.count(sec)))


def chapter_file(ch, chapters):
    return next(chapters.glob(f"ch{ch:02d}-*.md"))


def chapter_body(ch, chapters):
    """Chapter text without the YAML front matter (its tags list is not coverage)."""
    text = chapter_file(ch, chapters).read_text()
    return text.split("---", 2)[2] if text.startswith("---") else text


def extract(pdf):
    import fitz
    rows, ch, parent = [], None, ""
    for lvl, title, page in fitz.open(pdf).get_toc():
        title = title.replace("\x00", "").strip()
        if lvl == 1:
            ch = ch if title.startswith("Part") else None
            continue
        if lvl == 2:
            m = re.match(r"Chapter (\d+)\.", title)
            ch = int(m.group(1)) if m else None
            continue
        if not ch or title in ("Themes Revisited", "Key Terms", "Conclusion") \
                or re.match(r"Part (One|Two)\b", title):
            continue
        if lvl == 3 and "Case" not in title:
            parent = title
        rows.append({"id": f"{ch}.{len([r for r in rows if r['ch'] == ch]) + 1}",
                     "ch": ch, "level": lvl, "title": title, "page": page,
                     "section": parent})
    TOPICS.write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(rows)} topics -> {TOPICS}")


def check(chapters=CHAPTERS, json_out=None, quiet=False):
    topics = json.loads(TOPICS.read_text())
    verified = json.loads(VERIFIED.read_text()) if VERIFIED.exists() else {}
    report, bad_quotes = {}, []
    for ch in range(1, 19):
        body, line_of, heading, section = [], [], {}, ""
        for n, line in enumerate(chapter_body(ch, chapters).split("\n")):
            if line.startswith("## "):
                section = line[3:].strip()
            elif line.startswith("# "):
                heading = line[2:].strip()
            toks = norm(line)
            body += toks
            line_of += [section] * len(toks)
        words = [stem(w) for w in body]
        flat = " ".join(body)
        index = {}
        for i, w in enumerate(words):
            index.setdefault(w, []).append(i)
        rows = []
        for t in (t for t in topics if t["ch"] == ch):
            keys = keywords(t["title"])
            pos = {k: index[k] for k in keys if k in index}
            need = len(keys) if len(keys) < 4 else math.ceil(0.75 * len(keys))
            starts = found_close(pos, need) if keys else []
            how = "words" if starts else ""
            quote = verified.get(t["id"], {}).get("quote")
            if quote:  # a hand-checked passage also fixes where the topic is pointed to
                q = " ".join(norm(quote))
                if q in flat:
                    how, starts = how or "passage", [flat[:flat.index(q)].count(" ")]
                else:
                    bad_quotes.append(t["id"])
            rows.append({**t, "covered": bool(how), "how": how,
                         "where": best_section(starts, line_of, t) if starts else "",
                         "missing_words": [k for k in keys if k not in pos]})
        report[ch] = {"title": heading, "topics": rows}
    total = sum(len(r["topics"]) for r in report.values())
    hit = sum(t["covered"] for r in report.values() for t in r["topics"])
    if not quiet:
        for ch, r in report.items():
            n = sum(t["covered"] for t in r["topics"])
            print(f"ch{ch:02d}  {n:3d}/{len(r['topics']):3d}  {100 * n / len(r['topics']):5.1f}%")
            for t in r["topics"]:
                if not t["covered"]:
                    print(f"      MISSING {t['id']:7s} {t['title']}")
        print(f"ALL   {hit}/{total}  {100 * hit / total:.1f}%")
        if bad_quotes:
            print("passages not found in the chapter:", ", ".join(bad_quotes))
    if json_out:
        Path(json_out).write_text(json.dumps(report, indent=1, ensure_ascii=False))
    return report, hit, total, bad_quotes


PAGE = CHAPTERS / "ch19-coverage-check.md"


def pct(n, d):
    return f"{n} of {d} ({round(100 * n / d)}%)"


def write_page(old_dir):
    """The coverage report Sihan reads in the Textbook Library (Pinel, last chapter)."""
    now, hit, total, _ = check(quiet=True)
    old, old_hit, _, _ = check(Path(old_dir), quiet=True)
    out = ["# Coverage check: every Pinel topic", "",
           f"**What was checked.** Every heading in the contents of Pinel and Barnes, *Biopsychology*, 11th edition, "
           f"chapters 1 to 18, down to the smallest sub-heading, the named cases included: **{total} topics**. "
           "Only the end-of-chapter Themes Revisited and Key Terms pages are left out.", "",
           f"**Result.** This rewrite covers **{pct(hit, total)}**. "
           f"The old short version of these notes, before the rewrite, covered {pct(old_hit, total)}.", "",
           "**How.** A script looks for each topic's key words close together in the chapter. "
           "Where the rewrite words a topic differently from Pinel's heading, the passage that covers it "
           "was found by hand and the script checks that passage is really in the chapter. "
           "The list below shows, for every topic, the section of this rewrite that covers it, "
           "so it also works as a checklist for revising Pinel.", "",
           "| Chapter | Topics | Old version | This rewrite |", "|---|---|---|---|"]
    for ch in range(1, 19):
        rows, orows = now[ch]["topics"], old[ch]["topics"]
        n, o = sum(t["covered"] for t in rows), sum(t["covered"] for t in orows)
        name = re.sub(r"^Chapter \d+:\s*", "", now[ch]["title"])
        out.append(f"| {ch}. {name} | {len(rows)} | {round(100 * o / len(rows))}% | {round(100 * n / len(rows))}% |")
    out.append(f"| **All 18** | **{total}** | **{round(100 * old_hit / total)}%** | **{round(100 * hit / total)}%** |")
    for ch in range(1, 19):
        out += ["", f"## {now[ch]['title']}", ""]
        for t in now[ch]["topics"]:
            pad = "    " * (t["level"] - 3)
            name = f"**{t['title']}**" if t["level"] == 3 else t["title"]
            where = f" &rarr; {t['where'] or 'chapter opening'}" if t["covered"] else " &rarr; **NOT COVERED**"
            out.append(f"{pad}- {name} (p. {t['page'] - 1}){where}")
    PAGE.write_text("\n".join(out) + "\n")
    print(f"wrote {PAGE} ({hit}/{total} now, {old_hit}/{total} old)")


if __name__ == "__main__":
    if sys.argv[1:2] == ["extract"]:
        extract(sys.argv[2])
    elif sys.argv[1:2] == ["page"]:
        write_page(sys.argv[2])
    else:
        out = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else None
        d = Path(sys.argv[sys.argv.index("--dir") + 1]) if "--dir" in sys.argv else CHAPTERS
        check(d, out)
