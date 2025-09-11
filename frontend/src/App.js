import React, { useState } from 'react';
import LandingPage from './pages/LandingPage';
import StartDemo from './pages/StartDemo';
import StartSession from './pages/StartSession';
import './App.css';

const App = () => {
  const [currentScreen, setCurrentScreen] = useState('landing');

  const renderScreen = () => {
    switch (currentScreen) {
      case 'demo':
        return <StartDemo onBack={() => setCurrentScreen('landing')} onStartSession={(mode) => setCurrentScreen(`session-${mode}`)} />;
      case 'session-webcam':
        return <StartSession mode="webcam" onBack={() => setCurrentScreen('demo')} />;
      case 'session-upload':
        return <StartSession mode="upload" onBack={() => setCurrentScreen('demo')} />;
      default:
        return <LandingPage onStartDemo={() => setCurrentScreen('demo')} />;
    }
  };

  return (
    <div className="app">
      {renderScreen()}
    </div>
  );
};

export default App;

