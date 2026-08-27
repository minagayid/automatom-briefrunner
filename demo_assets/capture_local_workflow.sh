#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:8010}"
OUTPUT_DIR="$(cd "$(dirname "$0")" && pwd)"

health=$(curl -fsS "$BASE_URL/health")
created=$(curl -fsS -X POST "$BASE_URL/demo-runs" \
  -H 'content-type: application/json' \
  -d '{"intent":"Prepare a weekly competitor brief for a small professional team"}')
run_uid=$(printf '%s' "$created" | sed -n 's/.*"runUid":"\([^"]*\)".*/\1/p')

if [[ -z "$run_uid" ]]; then
  echo "Unable to parse run UID." >&2
  exit 1
fi

sleep 1
before=$(curl -fsS "$BASE_URL/runs/$run_uid")
approved=$(curl -fsS -X POST "$BASE_URL/runs/$run_uid/approve")

export health created before approved
python3 "$OUTPUT_DIR/render_workflow_evidence.py" "$OUTPUT_DIR/local_workflow_evidence.html"
