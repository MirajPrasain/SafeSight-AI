# backend/events/fire.py

from schema import AnalyzeResponse, Evidence, Event, Box
from typing import List, Dict, Any

# Define a confidence threshold for fire detection
FIRE_CONFIDENCE_THRESHOLD = 0.5

def analyze_fire(detections: List[Dict[str, Any]], mock: bool = False) -> AnalyzeResponse:
    """
    Analyzes raw detections from a vision model to detect fire.
    """
    # if mock:
    #     # The mock logic from your original code is still here for testing
    #     #... (your mock code here)
    #     return ...
    
    # Real-world logic using model output
    for det in detections:
        # Check if the detection type is 'fire' and confidence is high
        if det.get("type") == "fire" and det.get("confidence") > FIRE_CONFIDENCE_THRESHOLD:
            # Extract the bounding box and create a Box object
            box_data = det.get("box")
            if box_data:
                detected_box = Box(
                    x=box_data["x"],
                    y=box_data["y"],
                    w=box_data["w"],
                    h=box_data["h"]
                )
                
                # Build the evidence object with the real bounding box
                evid = Evidence(
                    boxes=[detected_box],
                    scene="indoor",
                    notes={"model": "YOLOv8", "why": "Detected fire object"},
                )
                
                # Build the event object with real confidence
                evt = Event(
                    type="fire",
                    confidence=det.get("confidence"),
                    evidence=evid,
                    window_seconds=0.0,
                    timestamp=0.0,
                )
                
                return AnalyzeResponse(
                    severity=0.85,
                    explanation="Fire detected. Visible flames are present.",
                    recommended_actions=[
                        "Call emergency services.",
                        "Evacuate immediately."
                    ],
                    evidence=[evid],
                    categories=["fire"],
                    events=[evt],
                )
                
    # If no fire is detected
    return AnalyzeResponse(
        severity=0.05,
        explanation="No fire detected in the current window.",
        recommended_actions=["Stay aware. If you see flames, evacuate immediately."],
        evidence=[],
        categories=[],
        events=[],
    )