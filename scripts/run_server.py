#!/usr/bin/env python3
"""
Script to start the To-Do API server.

This script starts the FastAPI application using Uvicorn server
with appropriate configuration for development.
"""

import sys
from pathlib import Path
import uvicorn


# Add the project root directory to Python path
# This allows the 'app' module to be imported correctly
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def start_server() -> None:
    """
    Start the FastAPI application server.
    
    Configures and runs the Uvicorn server with the following settings:
    - Host: 0.0.0.0 (accessible from all network interfaces)
    - Port: 8000
    - Reload: True (auto-reload on code changes for development)
    """
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    print("Starting To-Do API server...")
    print("Server will be available at: http://localhost:8000")
    print("Swagger documentation: http://localhost:8000/swagger")
    print("ReDoc documentation: http://localhost:8000/redoc")
    print("\nPress CTRL+C to stop the server\n")
    start_server()
