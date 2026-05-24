# CLAUDE.md

Guidance for Claude Code when working in this repo.

## What this is
Offline, installable PWA of granular psych-textbook notes for Sihan's MET 2026 Clinical Psych prep. Static site, no backend. Deployed via GitHub Pages from `docs/` on `main`.

## Principles (same as Teslo / Gift Card Vault)
- Build → test → verify → ship. Never push red or unverified code.
- `python3 tests/test_build.py` must pass (exit 0) before every commit.
- Keep the app self-contained and dependency-free at runtime (no CDNs) so it works fully offline.

## Workflow
- Edit/add notes in `notes/<book>/`. Chapter slugs and counts are tracked in `notes/manifest.json`.
- `python3 scripts/build.py` regenerates `docs/` (the deployed app). Always rebuild after changing notes or `scripts/app_shell.html`.
- Run tests, then commit BOTH the `notes/` change and the regenerated `docs/`.

## Deploy
- GitHub Pages serves `main` branch `/docs`. Pushing to `main` publishes. Live: https://msahil515.github.io/sihan-psych-notes/

## Conventions
- 45 chapters: Schultz 15, Baron 12, Pinel 18. Notes must be >=8KB (smaller = a generation dud; regenerate).
- No em dashes in prose (global rule).
- Tests are the source of truth for "done": counts, no duds, PWA artifacts (index/manifest/sw/icons), manifest standalone + icons, SW caches index.
