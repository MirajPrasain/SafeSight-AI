import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './WebcamView.css';

const WebcamView = ({ onBack }) => {
  const [isConnected, setIsConnected] = useState(false);
  const [videoUrl, setVideoUrl] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  const [detectedEvents, setDetectedEvents] = useState([]);
  const [error, setError] = useState('');

  // Check backend connection
  useEffect(() => {
    const checkConnection = async () => {
      try {
        const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
        const response = await axios.get(`${API_URL}/health`);
        setIsConnected(true);
        setError('');
      } catch (err) {
        setIsConnected(false);
        setError('Backend server is not running. Please start the backend server.');
      }
    };

    checkConnection();
    const interval = setInterval(checkConnection, 5000); // Check every 5 seconds

    return () => clearInterval(interval);
  }, []);

  const startStream = async () => {
    try {
      setError('');
      const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
      const response = await axios.post(`${API_URL}/analyze_camera`);
      setVideoUrl(response.data.video_url);
      setIsStreaming(true);
    } catch (err) {
      setError('Failed to start video stream: ' + err.message);
    }
  };

  const stopStream = async () => {
    try {
      const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
      await axios.post(`${API_URL}/stop_stream`);
      setIsStreaming(false);
      setVideoUrl('');
      setDetectedEvents([]);
    } catch (err) {
      setError('Failed to stop video stream: ' + err.message);
    }
  };

  return (
    <div className="webcam-view">
      <header className="webcam-header">
        <button onClick={onBack} className="back-link">← Back</button>
        <h1>📹 Live Webcam Monitoring</h1>
        <p>Real-time emergency detection through live video streams</p>
        
        <div className="connection-status">
          <span className={`status-indicator ${isConnected ? 'status-online' : 'status-offline'}`}></span>
          {isConnected ? 'Backend Connected' : 'Backend Disconnected'}
        </div>
      </header>

      <main className="webcam-main">
        {error && (
          <div className="alert alert-danger">
            {error}
          </div>
        )}

        <div className="stream-controls">
          <button 
            className="button primary" 
            onClick={startStream} 
            disabled={!isConnected || isStreaming}
          >
            Start Live Stream
          </button>
          <button 
            className="button secondary" 
            onClick={stopStream} 
            disabled={!isStreaming}
          >
            Stop Stream
          </button>
        </div>

        {isStreaming && videoUrl && (
          <div className="video-container">
            <video 
              src={videoUrl} 
              autoPlay 
              muted 
              controls
              width="100%"
              height="auto"
              className="stream-video"
            />
          </div>
        )}

        {detectedEvents.length > 0 && (
          <div className="detection-results">
            <h3>Live Detection Results</h3>
            {detectedEvents.map((event, index) => (
              <div key={index} className="event-item">
                <strong>{event.type}</strong>
                {event.confidence && (
                  <span className="confidence">
                    (Confidence: {(event.confidence * 100).toFixed(1)}%)
                  </span>
                )}
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
};

export default WebcamView;
