"""
FastAPI application for a To-Do task manager.

This module defines the REST API endpoints for creating, reading,
updating, and deleting tasks. The application uses an in-memory
database for storage and includes Swagger documentation.
"""

from typing import List
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse

from app.models import Task, TaskCreate, TaskUpdate
from app.database import task_db


# Initialize FastAPI application with metadata for documentation
app = FastAPI(
    title="To-Do API",
    description="A simple REST API for managing to-do tasks",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/redoc"
)


@app.get("/", tags=["Root"])
async def root() -> dict:
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        dict: Welcome message with API information.
    """
    return {
        "message": "Welcome to the To-Do API",
        "docs": "/swagger",
        "version": "1.0.0"
    }


@app.post(
    "/tasks/",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"],
    summary="Create a new task",
    response_description="The created task"
)
async def create_task(task: TaskCreate) -> Task:
    """
    Create a new task.
    
    This endpoint creates a new task with the provided description
    and completion status. The task is assigned a unique ID
    automatically.
    
    Parameters:
        task (TaskCreate): The task data including description
                           and optional done status.
    
    Returns:
        Task: The newly created task with assigned ID.
    
    Raises:
        HTTPException: If task creation fails.
    """
    new_task = task_db.create_task(
        description=task.description,
        done=task.done
    )
    return new_task


@app.get(
    "/tasks/",
    response_model=List[Task],
    status_code=status.HTTP_200_OK,
    tags=["Tasks"],
    summary="List all tasks",
    response_description="List of all tasks"
)
async def get_tasks() -> List[Task]:
    """
    Retrieve all tasks.
    
    This endpoint returns a list of all tasks currently stored
    in the database.
    
    Returns:
        List[Task]: A list containing all tasks.
    """
    tasks = task_db.get_all_tasks()
    return tasks


@app.put(
    "/tasks/{id}/description",
    response_model=Task,
    status_code=status.HTTP_200_OK,
    tags=["Tasks"],
    summary="Update task description",
    response_description="The updated task"
)
async def update_task_description(id: int, task_update: TaskUpdate) -> Task:
    """
    Update the description of an existing task.
    
    This endpoint updates only the description field of a task
    identified by its ID. The completion status remains unchanged.
    
    Parameters:
        id (int): The unique identifier of the task to update.
        task_update (TaskUpdate): Object containing the new description.
    
    Returns:
        Task: The updated task with the new description.
    
    Raises:
        HTTPException: 404 error if the task is not found.
    """
    updated_task = task_db.update_task_description(
        task_id=id,
        description=task_update.description
    )
    
    if updated_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {id} not found"
        )
    
    return updated_task


@app.patch(
    "/tasks/{id}/undone",
    response_model=Task,
    status_code=status.HTTP_200_OK,
    tags=["Tasks"],
    summary="Mark task as not completed",
    response_description="The updated task marked as undone"
)
async def mark_task_undone(id: int) -> Task:
    """
    Mark a task as not completed (undone).
    
    This endpoint updates the completion status of a task to False,
    marking it as not completed. The operation is idempotent, so
    calling it multiple times on the same task has the same effect
    as calling it once.
    
    Parameters:
        id (int): The unique identifier of the task to mark as undone.
    
    Returns:
        Task: The updated task with done=False.
    
    Raises:
        HTTPException: 404 error if the task is not found.
    """
    updated_task = task_db.mark_task_undone(task_id=id)
    
    if updated_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {id} not found"
        )
    
    return updated_task


@app.delete(
    "/tasks/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Tasks"],
    summary="Delete a task",
    response_description="Task successfully deleted"
)
async def delete_task(id: int) -> None:
    """
    Delete a task by its ID.
    
    This endpoint permanently removes a task from the database.
    
    Parameters:
        id (int): The unique identifier of the task to delete.
    
    Returns:
        None: Returns 204 No Content on successful deletion.
    
    Raises:
        HTTPException: 404 error if the task is not found.
    """
    deleted = task_db.delete_task(task_id=id)
    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {id} not found"
        )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc: Exception) -> JSONResponse:
    """
    Global exception handler for unhandled errors.
    
    This handler catches any unhandled exceptions and returns
    a standardized error response.
    
    Parameters:
        request: The request that caused the exception.
        exc (Exception): The exception that was raised.
    
    Returns:
        JSONResponse: A JSON response with error details.
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error occurred"}
    )
