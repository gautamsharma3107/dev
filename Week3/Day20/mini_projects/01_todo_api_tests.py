"""
MINI PROJECT 1: Test Suite for a Todo API
==========================================
Create a comprehensive test suite for a Todo application API

Requirements:
1. Test all CRUD operations
2. Test authentication
3. Test error handling
4. Use fixtures for setup
5. Use parametrized tests
6. Achieve 80%+ code coverage
"""

import pytest
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


# ========== TODO APPLICATION ==========

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


@dataclass
class Todo:
    """Todo item model."""
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    priority: Priority = Priority.MEDIUM
    status: Status = Status.PENDING
    user_id: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    due_date: Optional[datetime] = None


@dataclass
class User:
    """User model."""
    id: int
    username: str
    email: str


class TodoAPIError(Exception):
    """Base exception for Todo API."""
    def __init__(self, message: str, code: str):
        super().__init__(message)
        self.message = message
        self.code = code


class ValidationError(TodoAPIError):
    """Validation error."""
    def __init__(self, message: str):
        super().__init__(message, "VALIDATION_ERROR")


class NotFoundError(TodoAPIError):
    """Resource not found error."""
    def __init__(self, resource: str, id: int):
        super().__init__(f"{resource} with id {id} not found", "NOT_FOUND")


class UnauthorizedError(TodoAPIError):
    """Unauthorized access error."""
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, "UNAUTHORIZED")


class TodoRepository:
    """Repository for Todo operations."""
    
    def __init__(self):
        self._todos: Dict[int, Todo] = {}
        self._next_id = 1
    
    def save(self, todo: Todo) -> Todo:
        if todo.id is None:
            todo.id = self._next_id
            self._next_id += 1
        self._todos[todo.id] = todo
        return todo
    
    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        return self._todos.get(todo_id)
    
    def get_by_user(self, user_id: int) -> List[Todo]:
        return [t for t in self._todos.values() if t.user_id == user_id]
    
    def delete(self, todo_id: int) -> bool:
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False
    
    def list_all(self) -> List[Todo]:
        return list(self._todos.values())


class TodoService:
    """Service for Todo business logic."""
    
    def __init__(self, repository: TodoRepository):
        self._repository = repository
    
    def create_todo(
        self,
        user_id: int,
        title: str,
        description: str = "",
        priority: str = "medium",
        due_date: datetime = None
    ) -> Todo:
        """Create a new todo."""
        # Validation
        if not title:
            raise ValidationError("Title is required")
        if len(title) < 3:
            raise ValidationError("Title must be at least 3 characters")
        if len(title) > 100:
            raise ValidationError("Title must be at most 100 characters")
        
        try:
            priority_enum = Priority(priority)
        except ValueError:
            raise ValidationError(f"Invalid priority: {priority}")
        
        todo = Todo(
            title=title,
            description=description,
            priority=priority_enum,
            user_id=user_id,
            due_date=due_date
        )
        
        return self._repository.save(todo)
    
    def get_todo(self, todo_id: int, user_id: int) -> Todo:
        """Get a todo by ID."""
        todo = self._repository.get_by_id(todo_id)
        if not todo:
            raise NotFoundError("Todo", todo_id)
        if todo.user_id != user_id:
            raise UnauthorizedError("You don't have access to this todo")
        return todo
    
    def update_todo(
        self,
        todo_id: int,
        user_id: int,
        **updates
    ) -> Todo:
        """Update a todo."""
        todo = self.get_todo(todo_id, user_id)
        
        if "title" in updates:
            title = updates["title"]
            if not title or len(title) < 3:
                raise ValidationError("Title must be at least 3 characters")
            todo.title = title
        
        if "description" in updates:
            todo.description = updates["description"]
        
        if "priority" in updates:
            try:
                todo.priority = Priority(updates["priority"])
            except ValueError:
                raise ValidationError(f"Invalid priority: {updates['priority']}")
        
        if "status" in updates:
            try:
                todo.status = Status(updates["status"])
            except ValueError:
                raise ValidationError(f"Invalid status: {updates['status']}")
        
        return self._repository.save(todo)
    
    def delete_todo(self, todo_id: int, user_id: int) -> bool:
        """Delete a todo."""
        todo = self.get_todo(todo_id, user_id)
        return self._repository.delete(todo_id)
    
    def list_todos(
        self,
        user_id: int,
        status: str = None,
        priority: str = None
    ) -> List[Todo]:
        """List todos for a user with optional filters."""
        todos = self._repository.get_by_user(user_id)
        
        if status:
            try:
                status_enum = Status(status)
                todos = [t for t in todos if t.status == status_enum]
            except ValueError:
                raise ValidationError(f"Invalid status filter: {status}")
        
        if priority:
            try:
                priority_enum = Priority(priority)
                todos = [t for t in todos if t.priority == priority_enum]
            except ValueError:
                raise ValidationError(f"Invalid priority filter: {priority}")
        
        return todos
    
    def complete_todo(self, todo_id: int, user_id: int) -> Todo:
        """Mark a todo as completed."""
        return self.update_todo(todo_id, user_id, status="completed")


# ========== YOUR TASK: WRITE COMPREHENSIVE TESTS ==========

"""
TODO: Implement the following tests:

1. TestTodoRepository
   - test_save_new_todo
   - test_get_by_id_existing
   - test_get_by_id_nonexistent
   - test_get_by_user
   - test_delete_existing
   - test_delete_nonexistent

2. TestTodoServiceCreate
   - test_create_valid_todo
   - test_create_without_title
   - test_create_with_short_title
   - test_create_with_long_title
   - test_create_with_invalid_priority
   - test_create_with_all_priorities

3. TestTodoServiceRead
   - test_get_existing_todo
   - test_get_nonexistent_todo
   - test_get_other_users_todo
   - test_list_user_todos
   - test_list_with_status_filter
   - test_list_with_priority_filter

4. TestTodoServiceUpdate
   - test_update_title
   - test_update_status
   - test_update_priority
   - test_update_invalid_fields
   - test_update_nonexistent_todo
   - test_update_other_users_todo

5. TestTodoServiceDelete
   - test_delete_existing_todo
   - test_delete_nonexistent_todo
   - test_delete_other_users_todo

6. TestTodoWorkflow (Integration Tests)
   - test_complete_workflow
   - test_todo_lifecycle

Write your tests below:
"""

# Example fixture (expand on this)
@pytest.fixture
def repository():
    """Provide a fresh TodoRepository."""
    return TodoRepository()


@pytest.fixture
def service(repository):
    """Provide a TodoService with fresh repository."""
    return TodoService(repository)


# Start writing your tests here:


"""
Run your tests with: pytest 01_todo_api_tests.py -v --cov=. --cov-report=term-missing
"""
