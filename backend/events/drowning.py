from schema import AnalyzeResponse, Evidence, Event, Box
from typing import List, Dict, Any


def analyze_drowning(detections: List[Dict[str, Any]], mock: bool = False) -> AnalyzeResponse:
    """
    Analyzes raw detections to determine if a drowning event has occurred.
    
    Args:
        detections: A list of structured dictionaries from the VisionEngine.
        mock: If True, returns a mock response for testing.
        
    Returns:
        An AnalyzeResponse object.
    """
    if mock:
        evid = Evidence(
            boxes=[Box(x=200, y=150, w=100, h=80)],
            scene="pool",
            notes={"model": "stub", "why": "Lesson-1 mock drowning detection"},
        )
        evt = Event(
            type="drowning",
            confidence=0.78,
            evidence=evid,
            window_seconds=3.0,
            timestamp=0.0,
        )
        return AnalyzeResponse(
            severity=0.90,
            explanation="Person appears to be struggling in water; potential drowning situation.",
            recommended_actions=[
                "Call emergency services immediately.",
                "Throw a flotation device if available.",
                "Do not enter water unless trained in water rescue."
            ],
            evidence=[evid],
            categories=["drowning"],
            events=[evt],
        )
    
    # Non-mock neutral response
    return AnalyzeResponse(
        severity=0.05,
        explanation="No drowning risk detected in the current window.",
        recommended_actions=["Stay aware. If someone appears to be struggling in water, call for help."],
        evidence=[],
        categories=[],
        events=[],
    )

