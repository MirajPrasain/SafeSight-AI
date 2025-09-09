#!/usr/bin/env bash
set -e

# --- Backend ---
if [ -d ".venv" ]; then
  source .venv/bin/activate || true
fi

echo "[run] Starting backend @ http://127.0.0.1:8000"
uvicorn backend.app:app --reload --host 127.0.0.1 --port 8000