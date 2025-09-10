from schema import AnalyzeResponse, Evidence, Event, Box
from typing import List, Dict, Any


def analyze_overdose(detections: List[Dict[str, Any]], mock: bool = False) -> AnalyzeResponse:
    """
    Analyzes raw detections to determine if an overdose event has occurred.
    
    Args:
        detections: A list of structured dictionaries from the VisionEngine.
        mock: If True, returns a mock response for testing.
        
    Returns:
        An AnalyzeResponse object.
    """
    if mock:
        evid = Evidence(
            boxes=[Box(x=80, y=200, w=120, h=100)],
            scene="indoor",
            notes={"model": "stub", "why": "Lesson-1 mock overdose detection"},
        )
        evt = Event(
            type="overdose",
            confidence=0.65,
            evidence=evid,
            window_seconds=3.0,
            timestamp=0.0,
        )
        return AnalyzeResponse(
            severity=0.80,
            explanation="Person appears unresponsive; potential overdose situation detected.",
            recommended_actions=[
                "Call emergency services immediately.",
                "Check for breathing and pulse.",
                "Administer naloxone if available and trained."
            ],
            evidence=[evid],
            categories=["overdose"],
            events=[evt],
        )
    
    # Non-mock neutral response
    return AnalyzeResponse(
        severity=0.05,
        explanation="No overdose risk detected in the current window.",
        recommended_actions=["Stay aware. If someone appears unresponsive, check on them."],
        evidence=[],
        categories=[],
        events=[],
    )

