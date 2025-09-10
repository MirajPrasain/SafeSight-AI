#!/bin/bash

# Start the Emergency Vision Copilot FastAPI server
# This script ensures the server runs from the correct directory

cd "$(dirname "$0")/../backend"

echo "Starting Emergency Vision Copilot server..."
echo "Server will be available at: http://127.0.0.1:8001"
echo "Health check: http://127.0.0.1:8001/health"
echo "API docs: http://127.0.0.1:8001/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 -m uvicorn app:app --reload --host 127.0.0.1 --port 8001
