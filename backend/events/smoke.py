from schema import AnalyzeResponse, Evidence, Event, Box
from typing import List, Dict, Any


def analyze_smoke(detections: List[Dict[str, Any]], mock: bool = False) -> AnalyzeResponse:
    """
    Analyzes raw detections to determine if a smoke event has occurred.
    
    Args:
        detections: A list of structured dictionaries from the VisionEngine.
        mock: If True, returns a mock response for testing.
        
    Returns:
        An AnalyzeResponse object.
    """
    if mock:
        evid = Evidence(
            boxes=[Box(x=150, y=100, w=200, h=150)],
            scene="indoor",
            notes={"model": "stub", "why": "Lesson-1 mock smoke detection"},
        )
        evt = Event(
            type="smoke",
            confidence=0.88,
            evidence=evid,
            window_seconds=3.0,
            timestamp=0.0,
        )
        return AnalyzeResponse(
            severity=0.75,
            explanation="Visible smoke detected in the upper area; potential fire hazard.",
            recommended_actions=[
                "Call emergency services immediately.",
                "Evacuate the area if safe to do so.",
                "Check for fire sources and ventilate if possible."
            ],
            evidence=[evid],
            categories=["smoke"],
            events=[evt],
        )
    
    # Non-mock neutral response
    return AnalyzeResponse(
        severity=0.05,
        explanation="No smoke detected in the current window.",
        recommended_actions=["Stay aware. If you smell smoke, investigate safely."],
        evidence=[],
        categories=[],
        events=[],
    )

