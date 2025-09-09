from schema import AnalyzeRequest, AnalyzeResponse, Evidence, Event, Box


def analyze_overdose(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Lesson-1 stub:
    - If req.mock is True, return a deterministic 'overdose' scenario.
    - Otherwise, return a neutral low-severity response.
    Later lessons plug real model outputs here.
    """
    if req.mock:
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


def calculate_overdose_severity(req: AnalyzeRequest) -> AnalyzeResponse:
    """
    Calculate overdose severity based on detection confidence and scene context.
    """
    # Placeholder for future implementation
    return analyze_overdose(req)
