#!/bin/bash

# EmergeVision Docker Management Script

case "$1" in
  "dev")
    echo "🚀 Starting EmergeVision in DEVELOPMENT mode..."
    docker-compose up frontend-dev backend
    ;;
  "prod")
    echo "🚀 Starting EmergeVision in PRODUCTION mode..."
    docker-compose up frontend-prod backend
    ;;
  "build")
    echo "🔨 Building all services..."
    docker-compose build
    ;;
  "stop")
    echo "🛑 Stopping all services..."
    docker-compose down
    ;;
  "clean")
    echo "🧹 Cleaning up Docker resources..."
    docker-compose down -v
    docker system prune -f
    ;;
  *)
    echo "EmergeVision Docker Management"
    echo ""
    echo "Usage: $0 {dev|prod|build|stop|clean}"
    echo ""
    echo "Commands:"
    echo "  dev    - Start in development mode (with hot reload)"
    echo "  prod   - Start in production mode (optimized build)"
    echo "  build  - Build all Docker images"
    echo "  stop   - Stop all running services"
    echo "  clean  - Stop services and clean up Docker resources"
    echo ""
    echo "Examples:"
    echo "  $0 dev     # Start development environment"
    echo "  $0 prod    # Start production environment"
    echo "  $0 build   # Build all images"
    ;;
esac


