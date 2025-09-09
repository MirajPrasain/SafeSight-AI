from __future__ import annotations
from typing import List, Literal, Optional, Dict, Any
from pydantic import BaseModel, Field

# This file is a collection of Pydantic models. Each class inherits from BaseModel, which gives it powerful validation and parsing features.


EventType = Literal["fire", "smoke", "fall", "drowning", "overdose"]

class Box(BaseModel):
    x: int
    y: int
    w: int
    h: int

class PosePoint(BaseModel):
    name: str
    x: float
    y: float
    score: float

class Evidence(BaseModel):
    boxes: Optional[List[Box]] = None
    pose: Optional[Dict[str, PosePoint]] = None
    scene: Optional[Literal["pool", "indoor", "street", "unknown"]] = "unknown"
    notes: Optional[Dict[str, Any]] = None  # extra model-specific evidence

class Event(BaseModel):
    type: EventType
    confidence: float = Field(ge=0.0, le=1.0)
    evidence: Evidence
    window_seconds: float = 3.0
    timestamp: float

class AnalyzeRequest(BaseModel):
    # For Lesson 1 we keep it simple: metadata + optional mock flag.
    source: Literal["webcam", "file", "stream"] = "webcam"
    mock: bool = False  # if true, i.e no input from frontend server returns deterministic fake event(s)

class AnalyzeResponse(BaseModel):
    severity: float = Field(ge=0.0, le=1.0)
    explanation: str
    recommended_actions: List[str]
    evidence: List[Evidence] = []
    categories: List[EventType] = []
    events: List[Event] = []