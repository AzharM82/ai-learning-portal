#!/usr/bin/env python3
"""Add a generated topic page to the portal index.

Usage:
    python3 publish.py --slug 2026-09-15-rag-architectures \\
        --title "RAG Architectures" --date 2026-09-15 \\
        --summary "One-paragraph teaser." --skill rag-architectures

    python3 publish.py --rebuild   # regenerate index data from published.json

Expects topics/<slug>.html to exist (without the .html suffix in --slug).
Updates the <!-- TOPIC-DATA --> JSON block (drives the date-picker browser)
and the <!-- TOPIC-NOSCRIPT --> fallback list, rebuilds the upcoming list
from queue.json, appends to published.json, and dequeues the title if it
came from the user's queue.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def esc(s):
    return html.escape(s, quote=True)


def topic_li(t):
    return (
        "<li>"
        f'<h4><a href="topics/{esc(t["slug"])}.html">{esc(t["title"])}</a></h4>'
        f'<p>{esc(t.get("summary", ""))}</p>'
        f'<div class="tskill">{esc(t.get("skill", ""))}</div>'
        "</li>"
    )


def rebuild_index(published):
    """Rewrite the TOPIC-DATA JSON block and TOPIC-NOSCRIPT list (newest first)."""
    index = ROOT / "index.html"
    page = index.read_text()

    ordered = sorted(published, key=lambda t: t["date"], reverse=True)

    m = re.search(r"(<!-- TOPIC-DATA -->)(.*?)</script>", page, flags=re.S)
    if not m:
        sys.exit("marker <!-- TOPIC-DATA --> not found in index.html")
    data_json = json.dumps(ordered, ensure_ascii=False)
    page = page[: m.start(2)] + data_json + page[m.end(2):]

    m = re.search(r"(<!-- TOPIC-NOSCRIPT -->)(.*?)(</ul>)", page, flags=re.S)
    if not m:
        sys.exit("marker <!-- TOPIC-NOSCRIPT --> not found in index.html")
    items = "\n            ".join(topic_li(t) for t in ordered)
    page = page[: m.start(2)] + "\n            " + items + "\n          " + page[m.end(2):]

    qpath = ROOT / "queue.json"
    queue = json.loads(qpath.read_text()).get("queue", [])
    if queue:
        items = "\n".join(f"      <li>{esc(t)}</li>" for t in queue[:8])
    else:
        items = "      <li>Queue is empty — the next topics are chosen automatically.</li>"
    m = re.search(r'(<ul class="upcoming-list">)(.*?)(</ul>)', page, flags=re.S)
    if not m:
        sys.exit("upcoming list not found in index.html")
    inner = "\n      <!-- UPCOMING -->\n" + items + "\n    "
    page = page[: m.start(2)] + inner + page[m.end(2):]

    index.write_text(page)


def load_published():
    pub_path = ROOT / "published.json"
    return json.loads(pub_path.read_text()) if pub_path.exists() else []


def save_published(published):
    (ROOT / "published.json").write_text(json.dumps(published, indent=2) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--slug")
    ap.add_argument("--title")
    ap.add_argument("--date")
    ap.add_argument("--summary")
    ap.add_argument("--skill")
    args = ap.parse_args()

    if args.rebuild:
        rebuild_index(load_published())
        print("index rebuilt from published.json")
        return

    for f in ("slug", "title", "date", "summary", "skill"):
        if not getattr(args, f):
            sys.exit(f"--{f} is required (or use --rebuild)")

    page = ROOT / "topics" / f"{args.slug}.html"
    if not page.exists():
        sys.exit(f"missing page: {page}")

    published = load_published()
    published.append(
        {
            "slug": args.slug,
            "title": args.title,
            "date": args.date,
            "summary": args.summary,
            "skill": args.skill,
        }
    )
    save_published(published)
    rebuild_index(published)

    qpath = ROOT / "queue.json"
    qd = json.loads(qpath.read_text())
    if args.title in qd.get("queue", []):
        qd["queue"].remove(args.title)
        qpath.write_text(json.dumps(qd, indent=2) + "\n")

    print(f"published {args.slug}")


if __name__ == "__main__":
    raise SystemExit(main())
