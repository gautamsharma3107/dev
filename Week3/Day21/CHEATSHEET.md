# Day 21 Quick Reference Cheat Sheet

## FastAPI Setup
```python
# Install
pip install fastapi uvicorn sqlalchemy pydantic python-jose passlib bcrypt

# Create app
from fastapi import FastAPI
app = FastAPI(title="My API", version="1.0.0")

# Run server
uvicorn main:app --reload
```

## CRUD Operations
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    
# In-memory database
items = {}

# CREATE
@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, **item.dict()}

# READ (all)
@app.get("/items/")
def get_items():
    return items

# READ (one)
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.dict()}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}
```

## Authentication
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Create token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
```

## SQLAlchemy Models with Relationships
```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Many-to-Many association table
post_tags = Table(
    'post_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

# User model (One-to-Many with Post)
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    # One-to-Many: User has many posts
    posts = relationship("Post", back_populates="author")

# Post model
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    
    # Many-to-One: Post belongs to User
    author = relationship("User", back_populates="posts")
    
    # Many-to-Many: Post has many Tags
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

# Tag model
class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    # Many-to-Many: Tag has many Posts
    posts = relationship("Post", secondary=post_tags, back_populates="tags")
```

## Testing with pytest
```python
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

# Test CREATE
def test_create_item():
    response = client.post("/items/", json={"name": "Test", "price": 10.5})
    assert response.status_code == 200
    assert response.json()["name"] == "Test"

# Test READ
def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test UPDATE
def test_update_item():
    response = client.put("/items/1", json={"name": "Updated", "price": 20.0})
    assert response.status_code == 200

# Test DELETE
def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200

# Test with authentication
def test_protected_route():
    # First login
    response = client.post("/token", data={"username": "test", "password": "test"})
    token = response.json()["access_token"]
    
    # Then access protected route
    response = client.get(
        "/protected/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200

# Test fixture for database
@pytest.fixture
def test_db():
    # Setup test database
    Base.metadata.create_all(bind=engine)
    yield
    # Cleanup
    Base.metadata.drop_all(bind=engine)
```

## Pydantic Schemas
```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# Base schema
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Create schema (input)
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

# Response schema (output)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True  # For SQLAlchemy

# Schema with relationships
class PostWithAuthor(BaseModel):
    id: int
    title: str
    content: str
    author: UserResponse
    tags: List[str]
    
    class Config:
        from_attributes = True
```

## API Documentation
```python
from fastapi import FastAPI

app = FastAPI(
    title="My Full-Featured API",
    description="A complete REST API with CRUD, Auth, and Tests",
    version="1.0.0",
    docs_url="/docs",        # Swagger UI
    redoc_url="/redoc",      # ReDoc
    openapi_url="/openapi.json"
)

# Add tags for organization
@app.get("/users/", tags=["users"])
def get_users():
    """Get all users"""
    pass

@app.post("/users/", tags=["users"], summary="Create a new user")
def create_user():
    """
    Create a new user with:
    - **username**: unique username
    - **email**: valid email address
    - **password**: at least 8 characters
    """
    pass
```

## Error Handling
```python
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

# Raise HTTP exception
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Resource not found"
)

# Custom exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "message": "Validation Error"}
    )
```

## Quick Commands
```bash
# Run FastAPI server
uvicorn main:app --reload

# Run tests
pytest test_main.py -v

# Run tests with coverage
pytest --cov=. --cov-report=html

# Generate requirements
pip freeze > requirements.txt
```

---
**Keep this handy for quick reference!** 🚀
