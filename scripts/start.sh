#!/bin/bash
# To-Do API Server Startup Script for Unix-like systems
# This script activates the virtual environment and starts the FastAPI server

echo "Starting To-Do API Server..."
echo "==================================="
echo ""

# Get the script directory and navigate to project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( dirname "$SCRIPT_DIR" )"

# Change to project root directory
cd "$PROJECT_ROOT"

# Check if virtual environment exists
if [ ! -d "./arauco_venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please create a virtual environment first."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source ./arauco_venv/bin/activate

# Check if FastAPI and Uvicorn are installed
echo "Checking dependencies..."
python -c "import fastapi" 2>/dev/null
if [ $? -ne 0 ]; then
    echo ""
    echo "Dependencies not found. Installing..."
    python -m pip install --upgrade pip
    python -m pip install "fastapi[standard]" uvicorn
fi

# Start the server
echo ""
echo "Starting FastAPI server..."
echo "Server URL: http://localhost:8000"
echo "Swagger UI: http://localhost:8000/swagger"
echo "ReDoc UI: http://localhost:8000/redoc"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

python scripts/run_server.py
