#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Usage: render_workflow_evidence.py OUTPUT_PATH")

raw = {key: os.environ[key] for key in ("health", "created", "before", "approved")}
data = {key: json.loads(value) for key, value in raw.items()}
run_before = json.loads(data["before"]["result"])
run_approved = json.loads(data["approved"]["result"])

rows = [
    ("Runtime label", data["health"]["agentMode"], "The local demonstration explicitly identifies itself as offline review mode."),
    ("Run created", data["created"]["status"], f"Asynchronous run UID: {data['created']['runUid']}"),
    ("Before approval", run_before["status"], f"Approval required: {run_before['approvalRequired']}; sent: {run_before['sent']}"),
    ("After approval", run_approved["status"], f"Notification: {run_approved['notificationStatus']}; sent: {run_approved['sent']}"),
]

tr = "\n".join(
    f"<tr><th>{html.escape(label)}</th><td><code>{html.escape(str(value))}</code></td><td>{html.escape(note)}</td></tr>"
    for label, value, note in rows
)
brief = html.escape(run_approved["brief"]).replace("\n", "<br>")
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
output = f"""<!doctype html>
<html lang=\"en\"><head><meta charset=\"utf-8\"><title>Automatom BriefRunner — Local Review Evidence</title>
<style>
body {{ margin:0; min-height:100vh; background:#071d2e; color:#eaf6fb; font-family:Inter,Arial,sans-serif; }}
main {{ max-width:1280px; margin:0 auto; padding:58px 72px; }}
header {{ border-left:7px solid #30d1c9; padding-left:24px; margin-bottom:30px; }}
h1 {{ margin:0 0 8px; font-size:46px; }} h2 {{ color:#30d1c9; font-size:26px; margin-top:36px; }}
.lead {{ font-size:22px; color:#bcd8e8; line-height:1.45; }}
.warning {{ background:#533d10; border:1px solid #e8bb4d; padding:22px 26px; border-radius:12px; font-size:20px; line-height:1.45; }}
table {{ width:100%; border-collapse:collapse; font-size:18px; background:#0c2a40; }} th,td {{ padding:18px; border-bottom:1px solid #2b526a; text-align:left; vertical-align:top; }} th {{ width:22%; color:#8dd9e5; }} code {{ color:#8fe5b2; font-family:ui-monospace,monospace; }}
pre {{ white-space:pre-wrap; font-size:17px; line-height:1.45; padding:24px; background:#0c2a40; border-radius:12px; color:#d6ebf5; }} .meta {{ color:#87aebb; }}
</style></head><body><main>
<header><h1>Automatom — BriefRunner</h1><p class=\"lead\">Local review-mode workflow evidence: asynchronous work, explicit approval, and no automatic send.</p></header>
<p class=\"warning\"><strong>Accuracy note:</strong> This is a reproducible local offline review run, not a live Gemini request. Historical Google Cloud Run deployment evidence is shown separately in the submission video.</p>
<h2>Observed state transitions</h2><table>{tr}</table>
<h2>Reviewed professional brief</h2><pre>{brief}</pre>
<p class=\"meta\">Captured {now}. Endpoint: http://127.0.0.1:8010. The approval endpoint records a handoff only; it does not send any external message.</p>
</main></body></html>"""
Path(sys.argv[1]).write_text(output, encoding="utf-8")
