from schema import AnalyzeRequest, AnalyzeResponse, Evidence, Event, Box


def analyze_fire(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Lesson-1 stub:
    - If req.mock is True, return a deterministic 'fire' scenario.
    - Otherwise, return a neutral low-severity response.
    Later lessons plug real model outputs here.
    """
    if req.mock:
        evid = Evidence(
            boxes=[Box(x=100, y=120, w=180, h=200)],
            scene="indoor",
            notes={"model": "stub", "why": "Lesson-1 mock fire detection"},
        )
        evt = Event(
            type="fire",
            confidence=0.92,
            evidence=evid,
            window_seconds=3.0,
            timestamp=0.0,
        )
        return AnalyzeResponse(
            severity=0.85,
            explanation="Visible flames detected near the lower-right quadrant; likely active fire.",
            recommended_actions=[
                "Call emergency services immediately.",
                "Use a Class A extinguisher if safe.",
                "Evacuate occupants and close doors to contain smoke."
            ],
            evidence=[evid],
            categories=["fire"],
            events=[evt],
        )
    
    # Non-mock neutral response
    return AnalyzeResponse(
        severity=0.05,
        explanation="No fire detected in the current window.",
        recommended_actions=["Stay aware. If you see flames, evacuate immediately."],
        evidence=[],
        categories=[],
        events=[],
    )


def calculate_fire_severity(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Calculate fire severity based on detection confidence and scene context.
    """
    # Placeholder for future implementation
    return analyze_fire(req)
