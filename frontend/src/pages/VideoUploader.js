import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './VideoUploader.css';

const VideoUploader = ({ onBack }) => {
  const [isConnected, setIsConnected] = useState(false);
  const [detectedEvents, setDetectedEvents] = useState([]);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [error, setError] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadProgress, setUploadProgress] = useState(0);

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
    const interval = setInterval(checkConnection, 30000); // Check every 30 seconds instead of 5

    return () => clearInterval(interval);
  }, []);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setDetectedEvents([]);
    setError('');
  };

  const uploadVideo = async () => {
    if (!selectedFile) {
      setError('Please select a video file first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      setIsAnalyzing(true);
      setError('');
      setUploadProgress(0);
      
      // Simulate progress for better UX
      const progressInterval = setInterval(() => {
        setUploadProgress(prev => Math.min(prev + 10, 90));
      }, 200);
      
      const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
      const response = await axios.post(`${API_URL}/analyze_video`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        timeout: 60000, // 60 second timeout
      });
      
      clearInterval(progressInterval);
      setUploadProgress(100);
      
      if (response.data.events && response.data.events.length > 0) {
        setDetectedEvents(response.data.events);
      } else {
        setDetectedEvents([{ type: 'No events detected', confidence: 0 }]);
      }
    } catch (err) {
      setError('Failed to analyze video: ' + err.message);
    } finally {
      setIsAnalyzing(false);
      setUploadProgress(0);
    }
  };

  return (
    <div className="video-uploader">
      <header className="uploader-header">
        <button onClick={onBack} className="back-link">← Back</button>
        <h1>📁 Video Analysis</h1>
        <p>Upload a video file for emergency event detection</p>
        
        <div className="connection-status">
          <span className={`status-indicator ${isConnected ? 'status-online' : 'status-offline'}`}></span>
          {isConnected ? 'Backend Connected' : 'Backend Disconnected'}
        </div>
      </header>

      <main className="uploader-main">
        {error && (
          <div className="alert alert-danger">
            {error}
          </div>
        )}

        <div className="upload-section">
          <div className="file-input-container">
            <input 
              type="file" 
              accept="video/*" 
              onChange={handleFileSelect}
              disabled={!isConnected}
              className="file-input"
              id="video-upload"
            />
            <label htmlFor="video-upload" className="file-input-label">
              {selectedFile ? selectedFile.name : 'Choose Video File'}
            </label>
          </div>
          
          {selectedFile && (
            <div className="file-info">
              <p>Selected: {selectedFile.name}</p>
              <p>Size: {(selectedFile.size / (1024 * 1024)).toFixed(2)} MB</p>
            </div>
          )}

          <button 
            className="button primary"
            onClick={uploadVideo}
            disabled={!isConnected || !selectedFile || isAnalyzing}
          >
            {isAnalyzing ? 'Analyzing...' : 'Analyze Video'}
          </button>
          
          {isAnalyzing && (
            <div className="progress-container">
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{ width: `${uploadProgress}%` }}
                ></div>
              </div>
              <p className="progress-text">{uploadProgress}% Complete</p>
            </div>
          )}
        </div>

        {detectedEvents.length > 0 && (
          <div className="detection-results">
            <h3>Analysis Results</h3>
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

        <div className="supported-formats">
          <h3>Supported Video Formats</h3>
          <p>MP4, AVI, MOV, WMV, FLV, WebM</p>
        </div>
      </main>
    </div>
  );
};

export default VideoUploader;
