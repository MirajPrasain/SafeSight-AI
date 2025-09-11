import React from 'react';
import './StartDemo.css';

const StartDemo = ({ onBack, onStartSession }) => {
  return (
    <div className="start-demo">
      <header className="demo-header">
        <button onClick={onBack} className="back-link">← Back to Home</button>
        <h1>🚨 EmergeVision Demo</h1>
        <p className="demo-description">
          Experience our AI-powered emergency detection system in action
        </p>
      </header>

      <main className="demo-main">
        <div className="demo-intro">
          <h2>Choose Your Demo Experience</h2>
          <p>
            Select how you'd like to experience EmergeVision's emergency detection capabilities.
            Our system can detect fires, falls, drowning, smoke, and overdose incidents in real-time.
          </p>
        </div>

        <div className="demo-options">
          <div className="demo-card">
            <div className="demo-icon">📹</div>
            <h3>Live Webcam Demo</h3>
            <p>
              Start a live video stream from your webcam and see real-time emergency detection in action.
              Perfect for testing the system with your own environment.
            </p>
            <button onClick={() => onStartSession('webcam')} className="demo-button primary">
              Start Live Demo
            </button>
          </div>

          <div className="demo-card">
            <div className="demo-icon">📁</div>
            <h3>Video Upload Demo</h3>
            <p>
              Upload a pre-recorded video file to analyze it for emergency events.
              Great for testing with sample emergency scenarios.
            </p>
            <button onClick={() => onStartSession('upload')} className="demo-button primary">
              Upload Video Demo
            </button>
          </div>
        </div>

        <div className="demo-features">
          <h3>What You'll See</h3>
          <div className="features-list">
            <div className="feature-item">
              <span className="feature-icon">⚡</span>
              <span>Real-time emergency detection</span>
            </div>
            <div className="feature-item">
              <span className="feature-icon">🎯</span>
              <span>High accuracy AI analysis</span>
            </div>
            <div className="feature-item">
              <span className="feature-icon">📊</span>
              <span>Confidence scores for each detection</span>
            </div>
            <div className="feature-item">
              <span className="feature-icon">🔔</span>
              <span>Instant alerts for emergency events</span>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default StartDemo;
