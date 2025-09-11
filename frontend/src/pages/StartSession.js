import React, { useState } from 'react';
import VideoUploader from './VideoUploader';
import WebcamView from './WebcamView';

const StartSession = ({ mode, onBack }) => {
  const [currentMode, setCurrentMode] = useState(mode || 'webcam');

  const renderContent = () => {
    if (currentMode === 'upload') {
      return <VideoUploader onBack={onBack} />;
    }
    return <WebcamView onBack={onBack} />;
  };

  return (
    <div className="start-session">
      <div className="session-header">
        <button onClick={onBack} className="back-button">← Back</button>
        <div className="mode-toggle">
          <button 
            className={currentMode === 'webcam' ? 'active' : ''}
            onClick={() => setCurrentMode('webcam')}
          >
            📹 Live Webcam
          </button>
          <button 
            className={currentMode === 'upload' ? 'active' : ''}
            onClick={() => setCurrentMode('upload')}
          >
            📁 Upload Video
          </button>
        </div>
      </div>
      {renderContent()}
    </div>
  );
};

export default StartSession;
