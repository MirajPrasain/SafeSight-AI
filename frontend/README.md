# EmergeVision Frontend

A React-based frontend application for the EmergeVision AI-powered emergency detection system.

## Features

- **Live Video Streaming**: Real-time video stream with emergency detection
- **Video Upload**: Upload and analyze video files for emergency events
- **Real-time Status**: Connection status monitoring with the backend
- **Event Detection**: Support for fire, smoke, fall, drowning, and overdose detection
- **Responsive Design**: Modern, mobile-friendly interface

## Getting Started

### Prerequisites

- Node.js (version 18 or higher)
- npm or yarn
- Backend server running on port 8000

### Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The application will open in your browser at `http://localhost:3000`.

### Docker

To run the frontend with Docker:

```bash
# Build and run with docker-compose (from project root)
docker-compose up frontend

# Or build and run individually
docker build -t emergevision-frontend .
docker run -p 3000:3000 emergevision-frontend
```

## API Integration

The frontend communicates with the backend API endpoints:

- `GET /health` - Check backend connection
- `POST /start_stream` - Start live video stream
- `POST /stop_stream` - Stop video stream
- `POST /analyze_video` - Upload and analyze video file

## Project Structure

```
frontend/
├── public/
│   ├── index.html
│   └── manifest.json
├── src/
│   ├── App.js          # Main application component
│   ├── App.css         # Application styles
│   ├── index.js        # Application entry point
│   └── index.css       # Global styles
├── Dockerfile
├── .dockerignore
└── package.json
```

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm build` - Builds the app for production
- `npm test` - Launches the test runner
- `npm eject` - Ejects from Create React App (one-way operation)

## Technologies Used

- **React 18** - Frontend framework
- **Axios** - HTTP client for API calls
- **CSS3** - Styling with modern features
- **Docker** - Containerization

