# To-Do API

A simple and elegant REST API built with FastAPI for managing to-do tasks. This application provides a clean interface for creating, reading, updating, and deleting tasks with an in-memory database.

## Features

- ✅ Create new tasks
- ✅ List all tasks
- ✅ Update task descriptions
- ✅ Mark tasks as done
- ✅ Delete tasks
- ✅ Automatic Swagger/OpenAPI documentation
- ✅ Proper HTTP status codes and error handling
- ✅ In-memory data storage
- ✅ Type-safe with Pydantic models

## Project Structure

```
to_do_app/
├── app/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # FastAPI application and endpoints
│   ├── models.py            # Pydantic models for data validation
│   └── database.py          # In-memory database implementation
│
├── scripts/
│   ├── run_server.py        # Python script to start the server
│   ├── start.ps1            # PowerShell startup script (Windows)
│   └── start.sh             # Bash startup script (Linux/Mac)
│
├── arauco_venv/             # Python virtual environment
│
└── README.md                # This file
```

### Directory Explanation

- **app/**: Contains the main application code
  - `main.py`: Defines all REST API endpoints and application configuration
  - `models.py`: Pydantic models for request/response validation
  - `database.py`: Simple in-memory database for storing tasks
  
- **scripts/**: Contains scripts to run the application
  - `run_server.py`: Core server startup script
  - `start.ps1`: Windows PowerShell wrapper script
  - `start.sh`: Unix/Linux/Mac bash wrapper script

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd to_do_app
   ```

2. **Create and activate a virtual environment**:
   
   On Windows (PowerShell):
   ```powershell
   python -m venv arauco_venv
   .\arauco_venv\Scripts\Activate.ps1
   ```
   
   On Linux/Mac:
   ```bash
   python3 -m venv arauco_venv
   source arauco_venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install "fastapi[standard]" uvicorn
   ```

## Running the Application

### Option 1: Using the startup scripts (Recommended)

**Windows (PowerShell)**:
```powershell
.\scripts\start.ps1
```

**Linux/Mac**:
```bash
chmod +x scripts/start.sh
./scripts/start.sh
```

### Option 2: Using Python directly

```bash
python scripts/run_server.py
```

### Option 3: Using Uvicorn directly

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The server will start at `http://localhost:8000`

## API Documentation

Once the server is running, you can access the interactive documentation at:

- **Swagger UI**: http://localhost:8000/swagger
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### 1. Create a new task

**Endpoint**: `POST /tasks/`

**Request Body**:
```json
{
  "description": "Buy groceries",
  "done": false
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "description": "Buy groceries",
  "done": false
}
```

**cURL Example**:
```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{"description": "Buy groceries", "done": false}'
```

**PowerShell Example**:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks/" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"description": "Buy groceries", "done": false}'
```

---

### 2. List all tasks

**Endpoint**: `GET /tasks/`

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "done": false
  },
  {
    "id": 2,
    "description": "Write documentation",
    "done": true
  }
]
```

**cURL Example**:
```bash
curl -X GET "http://localhost:8000/tasks/"
```

**PowerShell Example**:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks/" -Method GET
```

---

### 3. Update task description

**Endpoint**: `PUT /tasks/{id}/description`

**Request Body**:
```json
{
  "description": "Buy groceries and cook dinner"
}
```

**Response** (200 OK):
```json
{
  "id": 1,
  "description": "Buy groceries and cook dinner",
  "done": false
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "Task with id 999 not found"
}
```

**cURL Example**:
```bash
curl -X PUT "http://localhost:8000/tasks/1/description" \
  -H "Content-Type: application/json" \
  -d '{"description": "Buy groceries and cook dinner"}'
```

**PowerShell Example**:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks/1/description" `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"description": "Buy groceries and cook dinner"}'
```

---

### 4. Mark a task as done

**Endpoint**: `PATCH /tasks/{id}/done`

**Response** (200 OK):
```json
{
  "id": 1,
  "description": "Buy groceries",
  "done": true
}
```

**Error Response** (404 Not Found):
```json
{
  "detail": "Task with id 999 not found"
}
```

**cURL Example**:
```bash
curl -X PATCH "http://localhost:8000/tasks/1/done"
```

**PowerShell Example**:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks/1/done" -Method PATCH
```

---

### 5. Delete a task

**Endpoint**: `DELETE /tasks/{id}`

**Response** (204 No Content):
No response body returned on success.

**Error Response** (404 Not Found):
```json
{
  "detail": "Task with id 999 not found"
}
```

**cURL Example**:
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

**PowerShell Example**:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/tasks/1" -Method DELETE
```

---

## Complete Testing Example

Here's a complete workflow to test all endpoints:

**PowerShell**:
```powershell
# 1. Create tasks
$task1 = Invoke-RestMethod -Uri "http://localhost:8000/tasks/" `
  -Method POST -ContentType "application/json" `
  -Body '{"description": "Buy groceries", "done": false}'

$task2 = Invoke-RestMethod -Uri "http://localhost:8000/tasks/" `
  -Method POST -ContentType "application/json" `
  -Body '{"description": "Write code", "done": true}'

# 2. List all tasks
$allTasks = Invoke-RestMethod -Uri "http://localhost:8000/tasks/" -Method GET
$allTasks | ConvertTo-Json

# 3. Update a task description
$updated = Invoke-RestMethod -Uri "http://localhost:8000/tasks/1/description" `
  -Method PUT -ContentType "application/json" `
  -Body '{"description": "Buy groceries and cook dinner"}'

# 4. Mark a task as done
$done = Invoke-RestMethod -Uri "http://localhost:8000/tasks/1/done" -Method PATCH

# 5. Delete a task
Invoke-RestMethod -Uri "http://localhost:8000/tasks/2" -Method DELETE

# 6. Verify remaining tasks
$remainingTasks = Invoke-RestMethod -Uri "http://localhost:8000/tasks/" -Method GET
$remainingTasks | ConvertTo-Json
```

**Bash/cURL**:
```bash
# 1. Create tasks
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{"description": "Buy groceries", "done": false}'

curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{"description": "Write code", "done": true}'

# 2. List all tasks
curl -X GET "http://localhost:8000/tasks/"

# 3. Update a task description
curl -X PUT "http://localhost:8000/tasks/1/description" \
  -H "Content-Type: application/json" \
  -d '{"description": "Buy groceries and cook dinner"}'

# 4. Mark a task as done
curl -X PATCH "http://localhost:8000/tasks/1/done"

# 5. Delete a task
curl -X DELETE "http://localhost:8000/tasks/2"

# 6. Verify remaining tasks
curl -X GET "http://localhost:8000/tasks/"
```

## HTTP Status Codes

The API uses the following HTTP status codes:

- `200 OK`: Successful GET, PUT, or PATCH request
- `201 Created`: Successful POST request (task created)
- `204 No Content`: Successful DELETE request
- `404 Not Found`: Task with specified ID doesn't exist
- `422 Unprocessable Entity`: Invalid request data
- `500 Internal Server Error`: Unexpected server error

## Data Validation

The API uses Pydantic for automatic data validation:

- **description**: Must be between 1 and 500 characters
- **done**: Boolean value (true/false)
- **id**: Integer, automatically assigned

## Development Notes

- The application uses an **in-memory database**, so all data is lost when the server stops
- The server runs in **reload mode** during development for automatic code updates
- Swagger UI provides an interactive interface to test all endpoints
- All endpoints include proper error handling and return appropriate status codes

## Future Enhancements

Potential improvements for production use:

- Add persistent database (PostgreSQL, MongoDB, etc.)
- Implement user authentication and authorization
- Add task filtering and sorting capabilities
- Add pagination for large task lists
- Add task priority and due date fields
- Implement task categories/tags
- Add comprehensive unit and integration tests

## License

This project is provided as-is for educational and demonstration purposes.

## Author

Created as a demonstration of FastAPI best practices and REST API design.
