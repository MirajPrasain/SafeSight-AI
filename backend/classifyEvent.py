# backend/classifyEvent.py

from typing import List, Dict, Any, Callable
import cv2
import numpy as np
# Absolute imports for backend modules
from schema import AnalyzeRequest, AnalyzeResponse
from vision import VisionEngine
from events.fall import analyze_fall
from events.fire import analyze_fire
from events.drowning import analyze_drowning
from events.overdose import analyze_overdose
from events.smoke import analyze_smoke

# Initialize the vision engine globally to avoid reloading the model on every request
vision_engine = None

def initialize_vision_engine():
    """Initialize the vision engine once at startup."""
    global vision_engine
    if vision_engine is None:
        vision_engine = VisionEngine()

# Map detection types to their corresponding analysis functions
# Note: The functions now take a list of detections, not the full request.
EVENT_ANALYZE_FUNCTIONS: Dict[str, Callable[[List[Dict[str, Any]], bool], AnalyzeResponse]] = {
    "person": analyze_fall, # This maps YOLO's "person" detection to a fall analysis
    "fire": analyze_fire, # This maps YOLO's "fire" detection to a fire analysis
    "smoke": analyze_smoke, # This maps YOLO's "smoke" detection to a smoke analysis
    "drowning": analyze_drowning, # This maps YOLO's "drowning" detection to a drowning analysis
    "overdose": analyze_overdose, # This maps YOLO's "overdose" detection to an overdose analysis
}



def classifyEvent(file_bytes: bytes, source: str = "webcam", mock: bool = False) -> AnalyzeResponse:
    """
    Classifies emergency events based on real-time vision analysis.
    
    This function acts as the central orchestrator, handling multiple input sources.
    
    Args:
        file_bytes: Raw video file bytes
        source: Source type (webcam, file, stream)
        mock: If True, returns mock responses for testing
        
    Returns:
        Analysis response with detected events and recommendations.
    """
    try:
        # Ensure vision engine is initialized
        if vision_engine is None:
            initialize_vision_engine()
        
        # Step 1: Perception - Process file bytes and get raw detections from the Vision Engine
        # Optimize video processing by using memory buffer instead of temporary file
        import tempfile
        import os
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
            temp_file.write(file_bytes)
            temp_file_path = temp_file.name
        
        try:
            # Use VideoCapture to read the video file
            cap = cv2.VideoCapture(temp_file_path)
            if not cap.isOpened():
                raise ValueError("Could not open video file")
            
            # Read the first frame
            ret, frame = cap.read()
            cap.release()
            
            if not ret or frame is None:
                raise ValueError("Could not read frame from video file")
                
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
            
        raw_detections = vision_engine.analyze_frame(frame)
        
        # Initialize an empty list to store all detected event responses
        all_event_responses: List[AnalyzeResponse] = []
        
        # Step 2: Reasoning - Iterate through detections and call relevant event handlers
        for detection in raw_detections:
            detection_type = detection.get("type", "none")
            
            if detection_type in EVENT_ANALYZE_FUNCTIONS:
                # Route the specific detection to its corresponding event function
                response = EVENT_ANALYZE_FUNCTIONS[detection_type]([detection], mock)
                all_event_responses.append(response)
                
        # Return the most severe response if any were found
        if all_event_responses:
            # Sort by severity and return the highest one.
            all_event_responses.sort(key=lambda resp: resp.severity, reverse=True)
            return all_event_responses[0]

        # No detections found - return a neutral response
        return AnalyzeResponse(
            severity=0.05,
            explanation="No high-risk event or specific object detected in the current window.",
            recommended_actions=["Continue monitoring."],
            evidence=[],
            categories=[],
            events=[],
        )
        
    except Exception as e:
        # Return a safe fallback response for any errors
        return AnalyzeResponse(
            severity=0.0,
            explanation=f"Analysis error: {str(e)}. Check technical logs.",
            recommended_actions=["Contact technical support if this error persists."],
            evidence=[],
            categories=[],
            events=[],
        )