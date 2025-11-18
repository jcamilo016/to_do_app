"""
In-memory database for storing tasks.

This module provides a simple in-memory storage solution for tasks
using Python dictionaries. In a production environment, this would
be replaced with a persistent database solution.
"""

from typing import Dict, List, Optional
from app.models import Task


class TaskDatabase:
    """
    In-memory database for managing tasks.
    
    Attributes:
        _tasks (Dict[int, Task]): Dictionary storing tasks by ID.
        _next_id (int): Counter for generating unique task IDs.
    """
    
    def __init__(self) -> None:
        """Initialize the task database with empty storage."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1
    
    def create_task(self, description: str, done: bool = False) -> Task:
        """
        Create a new task in the database.
        
        Parameters:
            description (str): The task description.
            done (bool): Initial completion status (default: False).
        
        Returns:
            Task: The newly created task with assigned ID.
        """
        task = Task(id=self._next_id, description=description, done=done)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.
        
        Parameters:
            task_id (int): The unique identifier of the task.
        
        Returns:
            Optional[Task]: The task if found, None otherwise.
        """
        return self._tasks.get(task_id)
    
    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks from the database.
        
        Returns:
            List[Task]: A list of all tasks.
        """
        return list(self._tasks.values())
    
    def update_task_description(
        self,
        task_id: int,
        description: str
    ) -> Optional[Task]:
        """
        Update the description of an existing task.
        
        Parameters:
            task_id (int): The unique identifier of the task.
            description (str): The new description.
        
        Returns:
            Optional[Task]: The updated task if found, None otherwise.
        """
        task = self._tasks.get(task_id)
        if task:
            # Create a new Task instance with updated description
            updated_task = Task(
                id=task.id,
                description=description,
                done=task.done
            )
            self._tasks[task_id] = updated_task
            return updated_task
        return None
    
    def mark_task_undone(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as not completed (undone).
        
        Parameters:
            task_id (int): The unique identifier of the task.
        
        Returns:
            Optional[Task]: The updated task if found, None otherwise.
        """
        task = self._tasks.get(task_id)
        if task:
            # Create a new Task instance with done=False
            updated_task = Task(
                id=task.id,
                description=task.description,
                done=False
            )
            self._tasks[task_id] = updated_task
            return updated_task
        return None
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the database.
        
        Parameters:
            task_id (int): The unique identifier of the task to delete.
        
        Returns:
            bool: True if the task was deleted, False if not found.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False


# Global database instance
# In a production app, this would be managed with dependency injection
task_db = TaskDatabase()
