# Psych Notes — MET Prep

An offline, installable study app of granular psychology textbook notes for the **MET 2026 MSc/MA Clinical Psychology** entrance exam. Built for Sihan (Galaxy Tab S11 Ultra), works fully offline once loaded.

**Live:** https://msahil515.github.io/sihan-psych-notes/

## What's inside

45 chapter notes across three textbooks, each note walking every section with bolded key terms + definitions, key studies (researcher + year), classifications/stages, and a Key Terms glossary, Key People table, and "Likely Exam Points":

| Book | Chapters |
|------|----------|
| Schultz & Schultz — *Theories of Personality* (11e) | 15 |
| Baron & Branscombe — *Social Psychology* (13e) | 12 |
| Pinel — *Biopsychology* (8e) | 18 |

## App features

- Sidebar grouped by book → chapter; tap to read.
- Full-text search across all 45 notes.
- Fully offline (PWA: service worker caches everything; "Add to Home screen" to install as an app).
- Single self-contained page, no external dependencies.

## Project layout

```
notes/                 source markdown (the 45 chapter notes + per-book INDEX + manifest.json)
scripts/build.py       bundles notes -> docs/ PWA (markdown -> HTML, inlined, + manifest + service worker + icons)
scripts/app_shell.html UI template (sidebar, search, reader)
tests/test_build.py    build verification (counts, no duds, PWA artifacts, manifest/SW validity)
docs/                  built PWA, served by GitHub Pages
```

## Build & test

```bash
python3 scripts/build.py      # regenerate docs/ from notes/
python3 tests/test_build.py   # build + verify (exit 0 = all pass)
```

Requires Python 3 with `markdown` and `Pillow`.

## Notes provenance

Notes were generated from the source textbooks via a local `claude -p` pipeline (`~/.sihan-textbook-kb/`) and curated into `notes/`. To regenerate or add a book, see that pipeline.

## Android APK (optional)

The PWA installs to the home screen on Android/Chrome and runs standalone offline. For a sideloadable `.apk`, wrap this hosted PWA with [PWABuilder](https://pwabuilder.com) or Bubblewrap (TWA) — no change to this repo required.
