"""
Emergency Vision Copilot FastAPI Application
Main API server for emergency event detection and analysis.
"""

from __future__ import annotations
from fastapi import FastAPI
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
def analyze(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Analyze emergency events from video input.
    
    Args:
        req: Analysis request containing source and mock flag
        
    Returns:
        Analysis response with detected events, severity, and recommendations
    """
    try:
        return classifyEvent(req)
    except Exception as e:
        # Return a safe fallback response for any errors
        return AnalyzeResponse(
            severity=0.0,
            explanation=f"Service error: {str(e)}",
            recommended_actions=["Contact technical support if this error persists."],
            evidence=[],
            categories=[],
            events=[],
        )