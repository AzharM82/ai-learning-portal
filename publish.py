#!/usr/bin/env python3
"""Add a generated topic page to the portal index.

Usage:
    python3 publish.py --slug 2026-09-15-rag-architectures \\
        --title "RAG Architectures" --date 2026-09-15 \\
        --summary "One-paragraph teaser." --skill rag-architectures

Expects topics/<slug>.html to exist (without the .html suffix in --slug).
Inserts a card at <!-- TOPIC-GRID --> (newest first), rebuilds the upcoming
list from queue.json, appends to published.json, and dequeues the title if
it came from the user's queue.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--summary", required=True)
    ap.add_argument("--skill", required=True)
    args = ap.parse_args()

    page = ROOT / "topics" / f"{args.slug}.html"
    if not page.exists():
        sys.exit(f"missing page: {page}")

    index = ROOT / "index.html"
    html = index.read_text()

    if "<!-- TOPIC-GRID -->" not in html:
        sys.exit("marker <!-- TOPIC-GRID --> not found in index.html")
    card = (
        '<article class="tcard">\n'
        f'  <div class="tdate">{args.date}</div>\n'
        f'  <h3><a href="topics/{args.slug}.html">{args.title}</a></h3>\n'
        f'  <p>{args.summary}</p>\n'
        f'  <div class="tskill">${args.skill}</div>\n'
        "</article>\n    <!-- TOPIC-GRID -->"
    )
    html = html.replace("<!-- TOPIC-GRID -->", card, 1)

    qpath = ROOT / "queue.json"
    queue = json.loads(qpath.read_text()).get("queue", [])
    if queue:
        items = "\n".join(f"      <li>{t}</li>" for t in queue[:8])
    else:
        items = "      <li>Queue is empty — the next topics are chosen automatically.</li>"
    m = re.search(r'(<ul class="upcoming-list">)(.*?)(</ul>)', html, flags=re.S)
    if not m:
        sys.exit("upcoming list not found in index.html")
    inner = "\n      <!-- UPCOMING -->\n" + items + "\n    "
    html = html[: m.start(2)] + inner + html[m.end(2):]
    index.write_text(html)

    pub_path = ROOT / "published.json"
    published = json.loads(pub_path.read_text()) if pub_path.exists() else []
    published.append({"slug": args.slug, "title": args.title, "date": args.date})
    pub_path.write_text(json.dumps(published, indent=2) + "\n")

    qd = json.loads(qpath.read_text())
    if args.title in qd.get("queue", []):
        qd["queue"].remove(args.title)
        qpath.write_text(json.dumps(qd, indent=2) + "\n")

    print(f"published {args.slug}")


if __name__ == "__main__":
    raise SystemExit(main())
