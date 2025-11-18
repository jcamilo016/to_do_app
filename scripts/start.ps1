# To-Do API Server Startup Script
# This script activates the virtual environment and starts the FastAPI server

Write-Host "Starting To-Do API Server..." -ForegroundColor Green
Write-Host "===================================`n" -ForegroundColor Green

# Get the script directory and navigate to project root
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir

# Change to project root directory
Set-Location $projectRoot

# Check if virtual environment exists
if (-Not (Test-Path ".\arauco_venv\Scripts\Activate.ps1")) {
    Write-Host "Error: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please create a virtual environment first." -ForegroundColor Yellow
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& .\arauco_venv\Scripts\Activate.ps1

# Check if FastAPI and Uvicorn are installed
Write-Host "Checking dependencies..." -ForegroundColor Cyan
$fastapi = python -c "import fastapi; print('OK')" 2>$null
$uvicorn = python -c "import uvicorn; print('OK')" 2>$null

if ($fastapi -ne "OK" -or $uvicorn -ne "OK") {
    Write-Host "`nDependencies not found. Installing..." -ForegroundColor Yellow
    python -m pip install --upgrade pip
    python -m pip install "fastapi[standard]" uvicorn
}

# Start the server
Write-Host "`nStarting FastAPI server..." -ForegroundColor Cyan
Write-Host "Server URL: http://localhost:8000" -ForegroundColor Green
Write-Host "Swagger UI: http://localhost:8000/swagger" -ForegroundColor Green
Write-Host "ReDoc UI: http://localhost:8000/redoc`n" -ForegroundColor Green
Write-Host "Press CTRL+C to stop the server`n" -ForegroundColor Yellow

python scripts\run_server.py
