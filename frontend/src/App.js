import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [isConnected, setIsConnected] = useState(false);
  const [videoUrl, setVideoUrl] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  const [detectedEvents, setDetectedEvents] = useState([]);
  const [error, setError] = useState('');

  // Check backend connection
  useEffect(() => {
    const checkConnection = async () => {
      try {
        const response = await axios.get('/health');
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
      const response = await axios.post('/start_stream');
      setVideoUrl(response.data.video_url);
      setIsStreaming(true);
    } catch (err) {
      setError('Failed to start video stream: ' + err.message);
    }
  };

  const stopStream = async () => {
    try {
      await axios.post('/stop_stream');
      setIsStreaming(false);
      setVideoUrl('');
      setDetectedEvents([]);
    } catch (err) {
      setError('Failed to stop video stream: ' + err.message);
    }
  };

  const uploadVideo = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      setError('');
      const response = await axios.post('/analyze_video', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      if (response.data.events && response.data.events.length > 0) {
        setDetectedEvents(response.data.events);
      } else {
        setDetectedEvents([{ type: 'No events detected', confidence: 0 }]);
      }
    } catch (err) {
      setError('Failed to analyze video: ' + err.message);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🚨 EmergeVision</h1>
        <p>AI-Powered Emergency Detection System</p>
        <div className="connection-status">
          <span className={`status-indicator ${isConnected ? 'status-online' : 'status-offline'}`}></span>
          {isConnected ? 'Backend Connected' : 'Backend Disconnected'}
        </div>
      </header>

      <main className="App-main">
        {error && (
          <div className="alert alert-danger">
            {error}
          </div>
        )}

        <div className="card">
          <h2>Live Video Stream</h2>
          <p>Start a live video stream for real-time emergency detection</p>
          
          <div className="stream-controls">
            <button 
              className="button" 
              onClick={startStream} 
              disabled={!isConnected || isStreaming}
            >
              Start Stream
            </button>
            <button 
              className="button" 
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
              />
            </div>
          )}
        </div>

        <div className="card">
          <h2>Video Analysis</h2>
          <p>Upload a video file for emergency event detection</p>
          
          <div className="upload-section">
            <input 
              type="file" 
              accept="video/*" 
              onChange={uploadVideo}
              disabled={!isConnected}
              className="file-input"
            />
            <p className="upload-hint">Select a video file to analyze</p>
          </div>

          {detectedEvents.length > 0 && (
            <div className="detection-results">
              <h3>Detection Results</h3>
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
        </div>

        <div className="card">
          <h2>Supported Emergency Events</h2>
          <div className="event-types">
            <div className="event-type">🔥 Fire Detection</div>
            <div className="event-type">💨 Smoke Detection</div>
            <div className="event-type">🏃 Fall Detection</div>
            <div className="event-type">🏊 Drowning Detection</div>
            <div className="event-type">💊 Overdose Detection</div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;

