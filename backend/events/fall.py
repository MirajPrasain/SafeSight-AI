# backend/events/fall.py

from schema import AnalyzeResponse

# The aspect ratio threshold for a "fall"
FALL_ASPECT_RATIO_THRESHOLD = 1.5
FALL_CONFIDENCE_THRESHOLD = 0.5

def analyze_fall(detections: list, mock: bool = False) -> AnalyzeResponse:
    """
    Analyzes raw detections to determine if a fall event has occurred.
    
    Args:
        detections: A list of structured dictionaries from the VisionEngine.
        mock: If True, returns a mock response for testing.
        
    Returns:
        An AnalyzeResponse object.
    """
    if mock:
        return AnalyzeResponse(
            severity=0.7,
            explanation="[MOCK] A fall has been detected.",
            recommended_actions=["Call emergency services.", "Check on the individual."]
        )

    for detection in detections:
        # We only care about detections with a bounding box and person type
        if detection.get("type") == "person" and "box" in detection:
            box = detection["box"]
            confidence = detection["confidence"]
            
            if confidence > FALL_CONFIDENCE_THRESHOLD:
                # Calculate the aspect ratio (width / height)
                aspect_ratio = box["w"] / box["h"]
                
                # If the person is horizontal (e.g., on the ground)
                if aspect_ratio > FALL_ASPECT_RATIO_THRESHOLD:
                    return AnalyzeResponse(
                        severity=0.8,
                        explanation="Potential fall detected. The person appears to be on the ground.",
                        recommended_actions=["Review the camera feed immediately.", "Alert a team member."]
                    )
    
    # If no fall is detected after checking all detections
    return AnalyzeResponse(
        severity=0.05,
        explanation="No fall event detected. The area is clear.",
        recommended_actions=["Continue monitoring."]
    )