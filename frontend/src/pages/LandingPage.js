import React from 'react';
import './LandingPage.css';

const LandingPage = ({ onStartDemo }) => {
  return (
    <div className="landing-page">
      <header className="landing-header">
        <h1>🚨 EmergeVision</h1>
        <p className="tagline">AI-Powered Emergency Detection System</p>
        <p className="description">
          Protect lives with real-time emergency detection using advanced computer vision technology.
          Detect fires, falls, drowning, smoke, and overdose incidents instantly.
        </p>
      </header>

      <main className="landing-main">
        <div className="demo-section">
          <h2>Ready to Experience EmergeVision?</h2>
          <p>Start a demo to see our AI-powered emergency detection in action</p>
          <button onClick={onStartDemo} className="demo-button primary">
            Start Demo
          </button>
        </div>

        <div className="emergency-types">
          <h2>Supported Emergency Detection</h2>
          <div className="types-grid">
            <div className="emergency-type">
              <span className="type-icon">🔥</span>
              <span className="type-name">Fire Detection</span>
            </div>
            <div className="emergency-type">
              <span className="type-icon">💨</span>
              <span className="type-name">Smoke Detection</span>
            </div>
            <div className="emergency-type">
              <span className="type-icon">🏃</span>
              <span className="type-name">Fall Detection</span>
            </div>
            <div className="emergency-type">
              <span className="type-icon">🏊</span>
              <span className="type-name">Drowning Detection</span>
            </div>
            <div className="emergency-type">
              <span className="type-icon">💊</span>
              <span className="type-name">Overdose Detection</span>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default LandingPage;
