from schema import AnalyzeRequest, AnalyzeResponse, Evidence, Event, Box


def analyze_smoke(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Lesson-1 stub:
    - If req.mock is True, return a deterministic 'smoke' scenario.
    - Otherwise, return a neutral low-severity response.
    Later lessons plug real model outputs here.
    """
    if req.mock:
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


def calculate_smoke_severity(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Calculate smoke severity based on detection confidence and scene context.
    """
    # Placeholder for future implementation
    return analyze_smoke(req)
