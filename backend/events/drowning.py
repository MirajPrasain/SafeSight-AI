from schema import AnalyzeRequest, AnalyzeResponse, Evidence, Event, Box


def analyze_drowning(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Lesson-1 stub:
    - If req.mock is True, return a deterministic 'drowning' scenario.
    - Otherwise, return a neutral low-severity response.
    Later lessons plug real model outputs here.
    """
    if req.mock:
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


def calculate_drowning_severity(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Calculate drowning severity based on detection confidence and scene context.
    """
    # Placeholder for future implementation
    return analyze_drowning(req)
