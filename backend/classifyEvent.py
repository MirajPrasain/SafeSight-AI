# backend/classifyEvent.py

from typing import List, Dict, Any, Callable
import cv2
import numpy as np
from .schema import AnalyzeRequest, AnalyzeResponse
from .vision import VisionEngine
from .events.fall import analyze_fall
from .events.fire import analyze_fire
# Add other event imports here

# Initialize the vision engine globally to avoid reloading the model on every request
vision_engine = VisionEngine()

# Map detection types to their corresponding analysis functions
# Note: The functions now take a list of detections, not the full request.
EVENT_ANALYZE_FUNCTIONS: Dict[str, Callable[[List[Dict[str, Any]], bool], AnalyzeResponse]] = {
    "person": analyze_fall, # This maps YOLO's "person" detection to a fall analysis
    "fire": analyze_fire, # This maps YOLO's "fire" detection to a fire analysis
    # Add other mappings for "smoke", "drowning", etc.
}

def _get_frame(source: str) -> np.ndarray:
    """
    Captures a single frame from the specified source.
    
    Args:
        source: The source of the video feed (e.g., "webcam", "file").
    
    Returns:
        A single video frame as a numpy array.
    """
    if source == "webcam":
        cap = cv2.VideoCapture(0)
    elif source.endswith(('.mp4', '.avi')):  # Check for common video file extensions
        cap = cv2.VideoCapture(source)
    else:
        raise ValueError("Unsupported video source type.")

    if not cap.isOpened():
        raise IOError(f"Could not open video source: {source}")

    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        raise IOError("Failed to read frame from video source.")

    return frame

def classifyEvent(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Classifies emergency events based on real-time vision analysis.
    
    This function acts as the central orchestrator, handling multiple input sources.
    
    Args:
        req: Analysis request containing source and mock flag.
        
    Returns:
        Analysis response with detected events and recommendations.
    """
    try:
        # Step 1: Perception - Capture frame and get raw detections from the Vision Engine
        frame = _get_frame(req.source)
        raw_detections = vision_engine.analyze_frame(frame)
        
        # Initialize an empty list to store all detected event responses
        all_event_responses: List[AnalyzeResponse] = []
        
        # Step 2: Reasoning - Iterate through detections and call relevant event handlers
        for detection in raw_detections:
            detection_type = detection.get("type", "none")
            
            if detection_type in EVENT_ANALYZE_FUNCTIONS:
                # Route the specific detection to its corresponding event function
                response = EVENT_ANALYZE_FUNCTIONS[detection_type]([detection], req.mock)
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