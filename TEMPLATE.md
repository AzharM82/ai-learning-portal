# Daily topic page template

Every daily topic page is a standalone HTML file at `topics/<slug>.html`, visually
consistent with `index.html` (same CSS variables, fonts, card language, light theme).
It teaches ONE topic using Codex skill-design principles: front-loaded trigger,
imperative concrete steps, scope boundaries, progressive disclosure.

## Required sections, in order

1. **Portal nav** — same sticky nav as `index.html` (brand links back to `../index.html`).
2. **Skill card** — rendered like SKILL.md frontmatter in a code block:
   ```
   ---
   name: <kebab-case-topic>
   description: <one line: exactly when to reach for this>
   ---
   ```
3. **The one-idea version** — the single mental model, 2–3 sentences.
4. **Visual** — an inline SVG diagram that makes the idea click (page palette,
   subtle animation OK, no external assets).
5. **How it works** — 5–7 mechanics. Imperative, concrete, no fluff.
6. **Code sketch** — short, realistic Python (<30 lines).
7. **Failure modes** — 3–5 named pitfalls, each with a one-line fix.
8. **Go deeper (references)** — curated and REAL: 2–3 articles/docs, 1–2 videos
   (YouTube), each with a one-line "why this one". Never invent URLs — verify each
   link with a web search before publishing. No placeholder links, ever.
9. **Sample prompts** — 2–3 copy-paste prompts with a working copy button
   (reuse the copy-button pattern from `index.html`).
10. **Quiz** — 5 multiple-choice questions, interactive JS: clicking an answer shows
    right/wrong immediately with a one-line explanation; a final score is shown at
    the end. Questions must test understanding, not trivia.
11. **Flashcards** — 8–10 cards; click to flip (front: term/question, back: answer).
    Grid layout, keyboard accessible (Enter/Space flips).
12. **Reach for this when…** — 3 bullets of trigger conditions.
13. **Back link** to `../index.html#daily-topics`.

## Rules

- No lorem ipsum, no placeholder links, no invented facts or URLs.
- Every external link verified by search before publishing.
- Quiz answers and flashcard backs must be correct — double-check them.
- Keep total page under ~120KB.
- File name: `topics/YYYY-MM-DD-<slug>.html` (e.g. `topics/2026-09-15-rag-architectures.html`).
