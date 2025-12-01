"""
MINI PROJECT 1: Simple Todo API
================================
Create a complete Todo API using FastAPI with all CRUD operations.

This is the FastAPI version of the Django REST Framework API from previous days.

Requirements:
1. Create a Todo Pydantic model with:
   - title: string (required)
   - description: string (optional)
   - completed: boolean (default False)

2. Implement these endpoints:
   - GET /todos/ - List all todos (with optional filtering by completed status)
   - POST /todos/ - Create a new todo (return 201)
   - GET /todos/{todo_id} - Get a specific todo (return 404 if not found)
   - PUT /todos/{todo_id} - Update a todo (full update)
   - PATCH /todos/{todo_id} - Partial update a todo
   - DELETE /todos/{todo_id} - Delete a todo (return 204)

3. Add pagination support (skip and limit query parameters)

4. Use proper response models (don't expose internal data)

5. Add proper tags and documentation

Run with: uvicorn 01_todo_api:app --reload
Test at: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, status, Query, Path
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# TODO: Complete the implementation below

# ========== MODELS ==========

# Request model for creating/updating todos
class TodoCreate(BaseModel):
    # TODO: Add fields
    pass

# Response model (what we return to clients)
class TodoResponse(BaseModel):
    # TODO: Add fields
    pass

# Partial update model (all fields optional)
class TodoUpdate(BaseModel):
    # TODO: Add fields
    pass


# ========== APP SETUP ==========

app = FastAPI(
    title="Todo API",
    description="A simple Todo API built with FastAPI",
    version="1.0.0"
)

# In-memory database (replace with real database in production)
todos_db = {}
next_id = 1


# ========== ENDPOINTS ==========

# List all todos
@app.get("/todos/", response_model=List[TodoResponse], tags=["todos"])
def get_todos(
    skip: int = Query(0, ge=0, description="Number of todos to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max todos to return"),
    completed: Optional[bool] = Query(None, description="Filter by completed status")
):
    """
    Get all todos with optional filtering and pagination.
    
    - **skip**: Number of items to skip (for pagination)
    - **limit**: Maximum number of items to return
    - **completed**: Filter by completion status
    """
    # TODO: Implement
    pass


# Create a new todo
@app.post("/todos/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED, tags=["todos"])
def create_todo(todo: TodoCreate):
    """
    Create a new todo item.
    
    - **title**: Title of the todo (required)
    - **description**: Detailed description (optional)
    - **completed**: Whether the todo is completed (default: False)
    """
    # TODO: Implement
    pass


# Get a specific todo
@app.get("/todos/{todo_id}", response_model=TodoResponse, tags=["todos"])
def get_todo(todo_id: int = Path(..., gt=0, description="Todo ID")):
    """
    Get a specific todo by ID.
    
    - **todo_id**: The ID of the todo to retrieve
    """
    # TODO: Implement
    pass


# Update a todo (full update)
@app.put("/todos/{todo_id}", response_model=TodoResponse, tags=["todos"])
def update_todo(
    todo_id: int = Path(..., gt=0),
    todo: TodoCreate = ...
):
    """
    Update a todo completely (all fields required).
    
    - **todo_id**: The ID of the todo to update
    """
    # TODO: Implement
    pass


# Partial update a todo
@app.patch("/todos/{todo_id}", response_model=TodoResponse, tags=["todos"])
def partial_update_todo(
    todo_id: int = Path(..., gt=0),
    todo: TodoUpdate = ...
):
    """
    Partially update a todo (only provided fields are updated).
    
    - **todo_id**: The ID of the todo to update
    """
    # TODO: Implement
    pass


# Delete a todo
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["todos"])
def delete_todo(todo_id: int = Path(..., gt=0)):
    """
    Delete a todo by ID.
    
    - **todo_id**: The ID of the todo to delete
    """
    # TODO: Implement
    pass


# Bonus: Mark todo as complete
@app.post("/todos/{todo_id}/complete", response_model=TodoResponse, tags=["todos"])
def mark_complete(todo_id: int = Path(..., gt=0)):
    """
    Mark a todo as completed.
    
    - **todo_id**: The ID of the todo to mark as complete
    """
    # TODO: Implement
    pass


# Run with: uvicorn 01_todo_api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
