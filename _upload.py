#!/usr/bin/env python3
"""Upload portal files to GitHub via the contents API (fresh repo, no shas needed)."""
import base64
import json
import sys
import urllib.request

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

API = "https://api.github.com"
REPO = "AzharM82/ai-learning-portal"
ROOT = "/home/hatch/workspace/learning-portal"

FILES = [
    "index.html",
    "README.md",
    "TEMPLATE.md",
    "curriculum.md",
    "publish.py",
    "queue.json",
    ".github/workflows/azure-static-web-apps-ci-cd.yml",
]


def put(path, content_b64):
    url = f"{API}/repos/{REPO}/contents/{path}"
    body = json.dumps(
        {"message": f"portal: add {path}", "content": content_b64, "branch": "main"}
    ).encode()
    req = urllib.request.Request(url, data=body, method="PUT")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, "custom.github", entry_name="access_token",
                             allowed_hosts=["api.github.com"])
    with urllib.request.urlopen(req, timeout=120) as resp:
        return read_json_response(resp)


for f in FILES:
    with open(f"{ROOT}/{f}", "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode()
    r = put(f, b64)
    print(f, "->", r.get("commit", {}).get("sha", "?")[:8], r.get("content", {}).get("sha", "?")[:8])
print("done")
