"""
Emergency Vision Copilot FastAPI Application
Main API server for emergency event detection and analysis.
"""

from __future__ import annotations
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from schema import AnalyzeRequest, AnalyzeResponse
from classifyEvent import classifyEvent




app = FastAPI(title="Emergency Vision Copilot", version="0.1.0")

# CORS: allow local UI (Tauri/Electron/React) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "emergency-vision-copilot", "version": "0.1.0"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(
    source: str = Form(...),
    mock: bool = Form(False),
    video_file: UploadFile = File(...)
) -> AnalyzeResponse:
    """
    Accepts a video file upload and analyzes it.
    """
    try:
        file_bytes = video_file.file.read()
        # Pass the bytes and other params to the classifyEvent function
        # You'll need to update classifyEvent to accept bytes from a file instead of using cv2.VideoCapture
        # ... (further logic to process the bytes)
        return classifyEvent(file_bytes, source=source, mock=mock)
    except Exception as e:
        return AnalyzeResponse(
            severity=0.0,
            explanation=f"Service error: {str(e)}",
            recommended_actions=["Contact technical support if this error persists."],
            evidence=[],
            categories=[],
            events=[],
        )