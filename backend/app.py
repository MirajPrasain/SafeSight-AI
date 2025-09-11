"""
Emergency Vision Copilot FastAPI Application
Main API server for emergency event detection and analysis.
"""

from __future__ import annotations
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from schema import AnalyzeRequest, AnalyzeResponse
from classifyEvent import classifyEvent, initialize_vision_engine




app = FastAPI(title="Emergency Vision Copilot", version="0.1.0")

# Initialize the vision engine at startup to avoid reloading the model on every request
@app.on_event("startup")
async def startup_event():
    initialize_vision_engine()

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

@app.post("/analyze_video")
def analyze_video(file: UploadFile = File(...)):
    """
    Simplified endpoint for video analysis that matches frontend expectations.
    """
    try:
        file_bytes = file.file.read()
        result = classifyEvent(file_bytes, source="file", mock=False)
        
        # Convert AnalyzeResponse to the format expected by frontend
        events = []
        if result.events:
            for event in result.events:
                events.append({
                    "type": event.get("type", "Unknown"),
                    "confidence": event.get("confidence", 0.0)
                })
        
        return {
            "events": events,
            "explanation": result.explanation,
            "severity": result.severity,
            "recommended_actions": result.recommended_actions
        }
    except Exception as e:
        return {
            "events": [],
            "explanation": f"Analysis error: {str(e)}",
            "severity": 0.0,
            "recommended_actions": ["Contact technical support if this error persists."]
        }