"""
Data models for the To-Do application.

This module defines the Pydantic models used for request/response
validation and documentation in the FastAPI application.
"""

from typing import Optional
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """
    Base model for Task with common attributes.
    
    Attributes:
        description (str): A brief description of the task.
        done (bool): Indicates whether the task is completed.
    """
    
    description: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Task description"
    )
    done: bool = Field(
        default=False,
        description="Task completion status"
    )


class TaskCreate(TaskBase):
    """
    Model for creating a new task.
    
    Inherits from TaskBase with required fields for task creation.
    """
    
    pass


class TaskUpdate(BaseModel):
    """
    Model for updating task description.
    
    Attributes:
        description (str): The new description for the task.
    """
    
    description: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Updated task description"
    )


class Task(TaskBase):
    """
    Complete Task model including ID.
    
    Attributes:
        id (int): Unique identifier for the task.
        description (str): Task description.
        done (bool): Task completion status.
    """
    
    id: int = Field(..., description="Unique task identifier")
    
    class Config:
        """Pydantic configuration for the Task model."""
        
        json_schema_extra = {
            "example": {
                "id": 1,
                "description": "Buy groceries",
                "done": False
            }
        }
