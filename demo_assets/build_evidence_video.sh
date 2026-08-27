#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
OUT="$ROOT/automatom_brief_runner_evidence_demo.mp4"

ffmpeg -y \
  -loop 1 -t 36 -i "$ROOT/01_local_review_workflow.webp" \
  -loop 1 -t 22 -i "$ROOT/02_local_api_routes.webp" \
  -loop 1 -t 35 -i "$ROOT/03_cloud_run_service.webp" \
  -loop 1 -t 28 -i "$ROOT/04_cloud_run_logs.webp" \
  -loop 1 -t 20 -i "$ROOT/05_architecture.png" \
  -i "$ROOT/automatom_evidence_narration.wav" \
  -filter_complex "
    [0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x071d2e,setsar=1[v0];
    [1:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x071d2e,setsar=1[v1];
    [2:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x071d2e,setsar=1[v2];
    [3:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x071d2e,setsar=1[v3];
    [4:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x071d2e,setsar=1[v4];
    [v0][v1][v2][v3][v4]concat=n=5:v=1:a=0[v]
  " \
  -map "[v]" -map 5:a -shortest \
  -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -movflags +faststart "$OUT"

printf 'Created %s\n' "$OUT"
