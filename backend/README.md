# Emergency Vision Copilot

A real-time emergency event detection system using computer vision and machine learning.

## Features

- **Real-time Event Detection**: Detects fire, smoke, falls, drowning, and overdose situations
- **RESTful API**: FastAPI-based backend with comprehensive endpoints
- **Modular Architecture**: Clean separation of concerns with event-specific handlers
- **Mock Testing**: Built-in mock responses for development and testing

## Quick Start

### 1. Install Dependencies

```bash
# Install core dependencies
pip install -r requirements.txt

# For development (optional)
pip install -r requirements-dev.txt
```

### 2. Run the Server

```bash
# Start the FastAPI server
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### 3. Test the API

```bash
# Health check
curl http://localhost:8000/health

# Mock analysis
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"source": "webcam", "mock": true}'
```

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /analyze` - Analyze emergency events from video input

## Project Structure

```
backend/
├── app.py              # FastAPI application
├── classifyEvent.py    # Event classification logic
├── schema.py          # Pydantic data models
├── requirements.txt   # Production dependencies
├── requirements-dev.txt # Development dependencies
└── events/            # Event detection handlers
    ├── fire.py
    ├── fall.py
    ├── drowning.py
    ├── overdose.py
    └── smoke.py
```

## Event Types

- **Fire**: Detects visible flames and fire hazards
- **Smoke**: Identifies smoke patterns and potential fire sources
- **Fall**: Recognizes person falling or lying motionless
- **Drowning**: Detects struggling in water environments
- **Overdose**: Identifies unresponsive persons

## Development

The system uses a clean architecture pattern:

1. **API Layer** (`app.py`) - Handles HTTP requests/responses
2. **Classification Layer** (`classifyEvent.py`) - Routes to appropriate event handlers
3. **Event Handlers** (`events/`) - Specific detection logic for each event type

## Dependencies

- **ultralytics**: YOLOv8 for object detection
- **fastapi**: Modern web framework for APIs
- **pydantic**: Data validation and settings management
- **opencv-python**: Computer vision operations
- **torch**: PyTorch for deep learning models
