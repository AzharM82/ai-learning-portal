# AI Engineering Learning Portal

A static site (Azure Static Web Apps) that grows by one topic every day.
Focus: AI engineering, software engineering, and everything around the
loop / graph / harness trio.

## Layout

- `index.html` — the launch page (loop/graph/harness trio) plus the daily topic grid.
- `topics/` — one standalone HTML page per daily topic (`YYYY-MM-DD-<slug>.html`).
- `queue.json` — Azharuddin's requested topics, in order. He adds them by messaging
  Azhar.AI in chat. The daily publisher takes from here first.
- `curriculum.md` — backlog used when the queue is empty (skips `published.json`).
- `published.json` — log of published topics (created on first publish).
- `TEMPLATE.md` — the spec every daily page follows (skill card, visual, references,
  sample prompts, quiz, flashcards).
- `publish.py` — wires a new topic page into `index.html`.

## Daily publishing (cron: learning-portal-daily, 8:00 AM PT)

1. Read `queue.json`; pop the first topic. If empty, take the next unchecked item
   from `curriculum.md` not in `published.json`.
2. Generate `topics/<date>-<slug>.html` per `TEMPLATE.md` (verify every link).
3. Run `publish.py` to add the card to the index.
4. Commit and push to `main` — the SWA CI/CD workflow deploys automatically.
5. Email Azharuddin (reachazhar@hotmail.com, via Gmail) with the topic title,
   the live URL, and one line on why it matters.

## Deployment

GitHub repo: `AzharM82/ai-learning-portal`, branch `main`.
Azure Static Web App: `ai-learning-portal`, resource group `rg-learning-portal`.
Every push to `main` redeploys via the `Azure Static Web Apps CI/CD` workflow.
