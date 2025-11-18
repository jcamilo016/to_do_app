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
        agent (Optional[str]): The cloud agent to whom the task is delegated.
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
    agent: Optional[str] = Field(
        default=None,
        max_length=100,
        description="Cloud agent assigned to this task"
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


class TaskDelegate(BaseModel):
    """
    Model for delegating a task to a cloud agent.
    
    Attributes:
        agent (str): The name or identifier of the cloud agent.
    """
    
    agent: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Cloud agent to delegate the task to"
    )


class Task(TaskBase):
    """
    Complete Task model including ID.
    
    Attributes:
        id (int): Unique identifier for the task.
        description (str): Task description.
        done (bool): Task completion status.
        agent (Optional[str]): Cloud agent assigned to this task.
    """
    
    id: int = Field(..., description="Unique task identifier")
    
    class Config:
        """Pydantic configuration for the Task model."""
        
        json_schema_extra = {
            "example": {
                "id": 1,
                "description": "Buy groceries",
                "done": False,
                "agent": "cloud-agent-1"
            }
        }
