#Helper function to capture frame and process it 
import cv2
import numpy as np

def _get_frame(source: str) -> np.ndarray:
    """
    Captures a single frame from the specified source.
    
    Args:
        source: The source of the video feed (e.g., "webcam", "file").
    
    Returns:
        A single video frame as a numpy array.
    """
    if source == "webcam":
        cap = cv2.VideoCapture(0)
    elif source.endswith(('.mp4', '.avi')):  # Check for common video file extensions
        cap = cv2.VideoCapture(source)
    else:
        raise ValueError("Unsupported video source type.")

    if not cap.isOpened():
        raise IOError(f"Could not open video source: {source}")

    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        raise IOError("Failed to read frame from video source.")

    return frame