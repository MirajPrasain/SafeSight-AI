# backend/vision.py
from typing import List, Dict, Any
import cv2
from ultralytics import YOLO

class VisionEngine:
    """
    A class to encapsulate all computer vision logic.
    This separates the model from the API, improving
    maintainability and testability.
    """
    def __init__(self, model_name: str = 'yolov8n.pt'):
        """
        Loads the YOLO model during object initialization.
        """
        self.model = YOLO(model_name)
        # Note: 'yolov8n.pt' is a good general-purpose model.
        # 'yolov8n-pose.pt' is for pose estimation (falls, drowning).
        # We can switch models easily here.

    def analyze_frame(self, frame) -> List[Dict[str, Any]]:
        """
        Analyzes a single video frame for objects and poses.
        
        Args:
            frame: A numpy array representing the video frame.
            
        Returns:
            A list of structured detections, ready to be converted
            into our Pydantic schema.
        """
        # The stream=True argument is key for real-time video processing.
        # It's a generator object that is memory-efficient. avoids loading all result object (for each video frame) into memory at once, 
        results = self.model(frame, stream=True, verbose=False) 
        
        detections = []
        for r in results:
            if r.boxes: # Check for object detections
                for box in r.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append({
                        "type": self.model.names[int(box.cls)],
                        "confidence": float(box.conf),
                        "box": {"x": x1, "y": y1, "w": x2 - x1, "h": y2 - y1}
                    })
            
            if r.keypoints: # Check for pose detections
                for i, keypoints in enumerate(r.keypoints.xyn):
                    pose_points = {}
                    for j, p in enumerate(keypoints[0]):
                        pose_points[f"point_{j}"] = {
                            "x": float(p[0]),
                            "y": float(p[1]),
                            "score": float(r.keypoints.conf[0][i])
                        }
                    detections.append({
                        "type": "pose",
                        "confidence": float(r.keypoints.conf[0][i]),
                        "pose": pose_points
                    })
        return detections