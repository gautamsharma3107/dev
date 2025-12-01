"""
MINI PROJECT 2: User Management API
====================================
Build a User Management API with FastAPI demonstrating all concepts from Day 17.

Requirements:
1. User Model:
   - id: auto-generated integer
   - username: string (3-20 chars, alphanumeric only)
   - email: valid email address
   - full_name: string
   - is_active: boolean (default True)
   - created_at: datetime (auto-generated)

2. Endpoints:
   - POST /users/ - Register new user
   - GET /users/ - List users with pagination and search
   - GET /users/me - Get current user (simulated)
   - GET /users/{user_id} - Get user by ID
   - PUT /users/{user_id} - Update user
   - DELETE /users/{user_id} - Delete user
   - POST /users/{user_id}/deactivate - Deactivate user

3. Features:
   - Proper input validation
   - Custom validators for username
   - Error handling with appropriate status codes
   - Search by username or email
   - Response models that hide sensitive data

Run with: uvicorn 02_user_api:app --reload
"""

from fastapi import FastAPI, HTTPException, status, Query, Path
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional, List
from datetime import datetime
import re

# ========== MODELS ==========

class UserCreate(BaseModel):
    """Model for creating a new user."""
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=100)
    password: str = Field(..., min_length=8)
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username must be alphanumeric (letters, numbers, underscores only)')
        return v.lower()


class UserUpdate(BaseModel):
    """Model for updating a user (all fields optional)."""
    username: Optional[str] = Field(None, min_length=3, max_length=20)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, min_length=1, max_length=100)
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if v and not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username must be alphanumeric')
        return v.lower() if v else v


class UserResponse(BaseModel):
    """Model for user responses (no password!)."""
    id: int
    username: str
    email: str
    full_name: str
    is_active: bool
    created_at: datetime


# ========== APP SETUP ==========

app = FastAPI(
    title="User Management API",
    description="A complete user management API built with FastAPI",
    version="1.0.0"
)

# In-memory database
users_db = {}
next_id = 1

# Seed some data
def seed_data():
    global next_id
    sample_users = [
        {"username": "alice", "email": "alice@example.com", "full_name": "Alice Smith", "password": "password123"},
        {"username": "bob", "email": "bob@example.com", "full_name": "Bob Johnson", "password": "password123"},
    ]
    for user_data in sample_users:
        users_db[next_id] = {
            "id": next_id,
            "username": user_data["username"],
            "email": user_data["email"],
            "full_name": user_data["full_name"],
            "hashed_password": f"hashed_{user_data['password']}",
            "is_active": True,
            "created_at": datetime.utcnow()
        }
        next_id += 1

seed_data()


# ========== HELPER FUNCTIONS ==========

def get_user_or_404(user_id: int):
    """Get user by ID or raise 404."""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return users_db[user_id]


def check_username_exists(username: str, exclude_id: int = None):
    """Check if username already exists."""
    for uid, user in users_db.items():
        if user["username"] == username and uid != exclude_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )


def check_email_exists(email: str, exclude_id: int = None):
    """Check if email already exists."""
    for uid, user in users_db.items():
        if user["email"] == email and uid != exclude_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )


# ========== ENDPOINTS ==========

@app.get("/", tags=["root"])
def root():
    """Welcome endpoint."""
    return {"message": "Welcome to User Management API", "docs": "/docs"}


@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["users"])
def create_user(user: UserCreate):
    """
    Register a new user.
    
    - **username**: Unique username (3-20 alphanumeric characters)
    - **email**: Valid email address
    - **full_name**: User's full name
    - **password**: Password (min 8 characters)
    """
    global next_id
    
    check_username_exists(user.username)
    check_email_exists(user.email)
    
    new_user = {
        "id": next_id,
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": f"hashed_{user.password}",
        "is_active": True,
        "created_at": datetime.utcnow()
    }
    
    users_db[next_id] = new_user
    next_id += 1
    
    return new_user


@app.get("/users/", response_model=List[UserResponse], tags=["users"])
def get_users(
    skip: int = Query(0, ge=0, description="Number of users to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max users to return"),
    search: Optional[str] = Query(None, min_length=2, description="Search in username or email"),
    is_active: Optional[bool] = Query(None, description="Filter by active status")
):
    """
    Get all users with optional filtering and pagination.
    
    - **skip**: Number of users to skip
    - **limit**: Maximum number of users to return
    - **search**: Search term for username or email
    - **is_active**: Filter by active status
    """
    users = list(users_db.values())
    
    # Filter by active status
    if is_active is not None:
        users = [u for u in users if u["is_active"] == is_active]
    
    # Search filter
    if search:
        search_lower = search.lower()
        users = [
            u for u in users 
            if search_lower in u["username"].lower() or search_lower in u["email"].lower()
        ]
    
    # Pagination
    return users[skip: skip + limit]


@app.get("/users/me", response_model=UserResponse, tags=["users"])
def get_current_user():
    """
    Get the current logged-in user.
    
    Note: This is simulated - in a real app, this would use authentication.
    """
    # Simulating a logged-in user (first user in database)
    if 1 in users_db:
        return users_db[1]
    raise HTTPException(status_code=401, detail="Not authenticated")


@app.get("/users/{user_id}", response_model=UserResponse, tags=["users"])
def get_user(user_id: int = Path(..., gt=0, description="User ID")):
    """
    Get a specific user by ID.
    
    - **user_id**: The ID of the user to retrieve
    """
    return get_user_or_404(user_id)


@app.put("/users/{user_id}", response_model=UserResponse, tags=["users"])
def update_user(
    user_id: int = Path(..., gt=0),
    user_update: UserUpdate = ...
):
    """
    Update a user's information.
    
    - **user_id**: The ID of the user to update
    """
    stored_user = get_user_or_404(user_id)
    
    update_data = user_update.dict(exclude_unset=True)
    
    if "username" in update_data:
        check_username_exists(update_data["username"], exclude_id=user_id)
    
    if "email" in update_data:
        check_email_exists(update_data["email"], exclude_id=user_id)
    
    for field, value in update_data.items():
        stored_user[field] = value
    
    return stored_user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(user_id: int = Path(..., gt=0)):
    """
    Delete a user.
    
    - **user_id**: The ID of the user to delete
    """
    get_user_or_404(user_id)
    del users_db[user_id]
    return None


@app.post("/users/{user_id}/deactivate", response_model=UserResponse, tags=["users"])
def deactivate_user(user_id: int = Path(..., gt=0)):
    """
    Deactivate a user account.
    
    - **user_id**: The ID of the user to deactivate
    """
    user = get_user_or_404(user_id)
    user["is_active"] = False
    return user


@app.post("/users/{user_id}/activate", response_model=UserResponse, tags=["users"])
def activate_user(user_id: int = Path(..., gt=0)):
    """
    Activate a user account.
    
    - **user_id**: The ID of the user to activate
    """
    user = get_user_or_404(user_id)
    user["is_active"] = True
    return user


# Run with: uvicorn 02_user_api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
