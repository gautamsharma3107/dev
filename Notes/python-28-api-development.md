# API Development: Complete Guide

---

## Table of Contents
1. [Introduction to API Development](#introduction-to-api-development)
2. [REST API Design](#rest-api-design)
3. [Request/Response Handling](#requestresponse-handling)
4. [API Documentation](#api-documentation)
5. [API Features](#api-features)
6. [API Testing](#api-testing)
7. [Practical Examples](#practical-examples)
8. [Best Practices](#best-practices)
9. [Practice Exercises](#practice-exercises)

---

## Introduction to API Development

### What is an API?

An API (Application Programming Interface) is a set of rules that allows different software applications to communicate.

### REST vs Other Paradigms

```
REST (Representational State Transfer):
- Resource-oriented
- HTTP-based
- Stateless
- Simple and scalable
- Most common

SOAP:
- XML-based
- Complex
- Enterprise
- Heavier

GraphQL:
- Query language
- Precise data fetching
- More complex
- Better for complex queries

gRPC:
- Binary protocol
- Fast
- Streaming
- For internal services
```

### API Maturity Model

```
Level 0: RPC Style
- Single endpoint
- Multiple methods
- Example: /api/getData

Level 1: Resources
- Multiple endpoints
- Resource-based URLs
- Example: /api/users, /api/posts

Level 2: HTTP Verbs
- Correct HTTP methods
- Proper status codes
- Example: GET /users, POST /users

Level 3: HATEOAS
- Hypermedia links
- Self-descriptive
- Example: Response includes links
```

---

## REST API Design

### Resource Naming Conventions

```
✓ GOOD - Plural nouns for collections
GET /api/users              → Get all users
POST /api/users             → Create user
GET /api/users/1            → Get user 1

✓ GOOD - Resource hierarchy
GET /api/users/1/posts      → Get user 1's posts
POST /api/users/1/posts     → Create post for user 1
GET /api/users/1/posts/5    → Get post 5 of user 1

✗ BAD - Verbs in URLs
GET /api/getUsers
POST /api/createUser
PUT /api/updateUser

✗ BAD - Singular nouns
GET /api/user
POST /api/post

✓ GOOD - Use IDs, not names
GET /api/users/1            → Good
GET /api/users/alice        → Avoid

✓ GOOD - Use hyphens for multi-word resources
GET /api/user-preferences   → Good
GET /api/user_preferences   → Avoid
GET /api/userPreferences    → Avoid
```

### HTTP Method Usage

```
GET - Retrieve resource
├── Safe (doesn't modify)
├── Idempotent
├── Cacheable
└── Example: GET /users/1

POST - Create resource
├── Not safe
├── Not idempotent
├── Response: 201 Created
└── Example: POST /users

PUT - Replace entire resource
├── Not safe
├── Idempotent
├── Requires all fields
└── Example: PUT /users/1

PATCH - Partial update
├── Not safe
├── Not idempotent (depends on patch)
├── Only changed fields
└── Example: PATCH /users/1

DELETE - Remove resource
├── Not safe
├── Idempotent
├── Response: 204 No Content
└── Example: DELETE /users/1

HEAD - Get headers without body
├── Like GET but no body
└── Check if resource exists

OPTIONS - Get available methods
├── CORS preflight
└── Return allowed methods
```

### Versioning Strategies

```
URL Versioning (Most common):
GET /api/v1/users
GET /api/v2/users
✓ Clear and explicit
✓ Easy to route
✗ URL changes

Header Versioning:
GET /users
Accept: application/vnd.api+json;version=1
✓ Keeps URLs clean
✗ Less obvious

Query Parameter Versioning:
GET /users?version=1
✓ Simple
✗ Conflicting with filters

Accept Header:
GET /users
Accept: application/vnd.company.v1+json
✓ REST pure
✗ Complex
```

### HATEOAS (Hypermedia As The Engine Of Application State)

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "_links": {
    "self": {
      "href": "/api/users/1"
    },
    "all_users": {
      "href": "/api/users"
    },
    "posts": {
      "href": "/api/users/1/posts"
    },
    "edit": {
      "href": "/api/users/1",
      "method": "PUT"
    },
    "delete": {
      "href": "/api/users/1",
      "method": "DELETE"
    }
  }
}
```

---

## Request/Response Handling

### Request Validation

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator, EmailStr, Field
from typing import Optional

app = FastAPI()

# Validate required fields
class User(BaseModel):
    name: str  # Required
    email: EmailStr  # Required, email format
    age: Optional[int] = None  # Optional

# Validate field constraints
class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

# Custom validators
class Post(BaseModel):
    title: str
    content: str
    tags: list[str] = []
    
    @validator('title')
    def title_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()
    
    @validator('tags')
    def max_tags(cls, v):
        if len(v) > 10:
            raise ValueError('Maximum 10 tags')
        return v

@app.post("/posts")
def create_post(post: Post):
    # Automatic validation!
    return post
```

### Response Formatting

```python
# Standard response format
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "status": "success",
        "data": {
            "id": user_id,
            "name": "Alice"
        }
    }

# Error response format
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 1:
        return {
            "status": "error",
            "error": {
                "code": "INVALID_ID",
                "message": "User ID must be positive"
            }
        }

# Paginated response
@app.get("/users")
def list_users(page: int = 1, limit: int = 10):
    return {
        "status": "success",
        "data": [...],
        "pagination": {
            "page": page,
            "limit": limit,
            "total": 100,
            "pages": 10
        }
    }

# List response
@app.get("/users")
def list_users():
    return {
        "status": "success",
        "data": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ],
        "meta": {
            "count": 2
        }
    }
```

### Error Handling

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# 400 Bad Request
@app.post("/users")
def create_user(user: dict):
    if 'name' not in user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Name is required"
        )
    return user

# 401 Unauthorized
@app.get("/private")
def private_endpoint(token: str = None):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return {"data": "private"}

# 403 Forbidden
@app.delete("/users/{user_id}")
def delete_user(user_id: int, current_user: dict):
    if current_user['id'] != user_id and not current_user['is_admin']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this user"
        )
    return {"deleted": True}

# 404 Not Found
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = find_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

# 422 Unprocessable Entity
from pydantic import ValidationError

@app.post("/users")
def create_user(user: dict):
    try:
        validated = User(**user)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.errors()
        )
    return validated

# 500 Internal Server Error
@app.get("/data")
def get_data():
    try:
        result = external_api_call()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

# Custom exception handler
from fastapi.responses import JSONResponse

class CustomException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

@app.exception_handler(CustomException)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )
```

### Status Code Selection

```
1xx Informational:
100 Continue

2xx Success:
200 OK                  - General success
201 Created             - Resource created
202 Accepted            - Request accepted for processing
204 No Content          - Success, no body

3xx Redirection:
301 Moved Permanently
302 Found
304 Not Modified        - Client cache valid

4xx Client Error:
400 Bad Request         - Invalid request
401 Unauthorized        - Authentication required
403 Forbidden           - Authentication OK, not authorized
404 Not Found           - Resource doesn't exist
405 Method Not Allowed  - Method not supported
408 Request Timeout
409 Conflict            - Request conflicts with state
410 Gone                - Resource permanently deleted
422 Unprocessable       - Validation error
429 Too Many Requests   - Rate limited

5xx Server Error:
500 Internal Server Error
501 Not Implemented
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

---

## API Documentation

### Swagger/OpenAPI

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="My API",
    description="A sample API",
    version="1.0.0",
)

@app.get("/users/{user_id}", tags=["users"])
def read_user(user_id: int):
    """
    Get a user by ID.
    
    - **user_id**: The ID of the user
    
    Returns:
    - **id**: User ID
    - **name**: User name
    - **email**: User email
    """
    return {"id": user_id, "name": "Alice", "email": "alice@example.com"}

@app.post("/users/", tags=["users"], response_model=dict)
def create_user(user: dict):
    """
    Create a new user.
    
    Request body:
    - **name**: User name (required)
    - **email**: User email (required)
    
    Returns created user with ID.
    """
    return {"id": 1, **user}

# Custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="My Custom API",
        version="2.0.0",
        description="Custom API description",
        routes=app.routes,
    )
    
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/logo.png"
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

### Interactive Documentation

```
Swagger UI:     http://localhost:8000/docs
ReDoc:          http://localhost:8000/redoc
OpenAPI JSON:   http://localhost:8000/openapi.json
```

---

## API Features

### Pagination

```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Offset/limit pagination
@app.get("/users")
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    return {
        "data": [],
        "pagination": {
            "skip": skip,
            "limit": limit,
            "total": 1000
        }
    }

# Cursor-based pagination
@app.get("/posts")
def list_posts(cursor: Optional[str] = None, limit: int = 10):
    return {
        "data": [],
        "pagination": {
            "next_cursor": "abc123"
        }
    }

# Page number pagination
@app.get("/products")
def list_products(page: int = Query(1, ge=1), per_page: int = Query(10, ge=1, le=100)):
    skip = (page - 1) * per_page
    return {
        "data": [],
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": 1000,
            "pages": 100
        }
    }
```

### Filtering

```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Simple filtering
@app.get("/users")
def list_users(
    status: Optional[str] = Query(None),
    role: Optional[str] = Query(None)
):
    # Filter by status and role
    return {"data": []}

# Range filtering
@app.get("/products")
def list_products(
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0)
):
    return {"data": []}

# Date range filtering
@app.get("/posts")
def list_posts(
    from_date: Optional[str] = Query(None),
    to_date: Optional[str] = Query(None)
):
    return {"data": []}

# Multiple values filtering
@app.get("/items")
def list_items(tags: Optional[list[str]] = Query(None)):
    # URL: /items?tags=python&tags=fastapi&tags=api
    return {"data": []}
```

### Sorting

```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Simple sorting
@app.get("/users")
def list_users(
    sort_by: str = Query("name"),
    order: str = Query("asc", regex="^(asc|desc)$")
):
    return {
        "data": [],
        "sort": {"by": sort_by, "order": order}
    }

# Multiple sort fields
@app.get("/posts")
def list_posts(
    sort: Optional[list[str]] = Query(None)
    # URL: /posts?sort=-created_at&sort=title
):
    return {"data": []}
```

### Field Selection

```python
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Include specific fields
@app.get("/users")
def list_users(fields: Optional[list[str]] = Query(None)):
    # URL: /users?fields=id&fields=name&fields=email
    all_fields = ["id", "name", "email", "created_at"]
    selected = fields if fields else all_fields
    return {"data": [], "fields": selected}

# Sparse fieldsets (GraphQL style)
@app.get("/posts")
def list_posts(include: Optional[str] = Query(None)):
    # URL: /posts?include=author,comments
    return {"data": []}
```

### Rate Limiting

```python
from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests"},
        headers={"Retry-After": "60"}
    )

# Rate limiting per endpoint
@app.get("/users")
@limiter.limit("100/minute")
def list_users(request):
    return {"data": []}

@app.post("/users")
@limiter.limit("10/minute")
def create_user(request, user: dict):
    return user
```

### Caching Strategies

```python
from fastapi import FastAPI
from fastapi.responses import Response
from datetime import datetime, timedelta

app = FastAPI()

# Browser caching
@app.get("/users/{user_id}")
def get_user(user_id: int):
    response = Response(content="...")
    response.headers["Cache-Control"] = "max-age=3600"
    return response

# ETag-based caching
@app.get("/data")
def get_data():
    data = {"value": "data"}
    etag = hash(str(data))
    return Response(
        content=str(data),
        headers={"ETag": f'"{etag}"'}
    )

# Server-side caching
from functools import lru_cache
import asyncio

@lru_cache(maxsize=128)
def expensive_computation(user_id: int):
    return {"result": user_id * 2}

@app.get("/compute/{user_id}")
def compute(user_id: int):
    return expensive_computation(user_id)

# Time-based cache invalidation
cache_data = {}
cache_time = {}
CACHE_DURATION = 3600  # 1 hour

def get_cached_data(key: str):
    if key in cache_data:
        if datetime.now() - cache_time[key] < timedelta(seconds=CACHE_DURATION):
            return cache_data[key]
    
    # Compute and cache
    data = expensive_operation(key)
    cache_data[key] = data
    cache_time[key] = datetime.now()
    return data
```

---

## API Testing

### Postman

```
Postman is a tool for testing APIs.

Features:
- Send HTTP requests
- Save collections
- Automatic documentation
- Environment variables
- Pre-request scripts
- Tests

Example Request:
Method: GET
URL: http://localhost:8000/users/1
Headers: 
  - Authorization: Bearer token123
Params:
  - format: json

Example Test:
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response is object", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('object');
});
```

### pytest for API Testing

```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test GET request
def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

# Test POST request
def test_create_user():
    user = {"name": "Alice", "email": "alice@example.com"}
    response = client.post("/users", json=user)
    assert response.status_code == 201
    assert response.json()["name"] == "Alice"

# Test error handling
def test_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404

# Test with authentication
def test_protected_endpoint():
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.get("/protected", headers=headers)
    assert response.status_code == 401

# Test with fixtures
@pytest.fixture
def user_data():
    return {"name": "Bob", "email": "bob@example.com"}

def test_create_and_get_user(user_data):
    # Create
    response = client.post("/users", json=user_data)
    user_id = response.json()["id"]
    
    # Get
    response = client.get(f"/users/{user_id}")
    assert response.json()["name"] == "Bob"

# Parametrized tests
@pytest.mark.parametrize("user_id,expected_status", [
    (1, 200),
    (2, 200),
    (999, 404),
])
def test_get_user_parametrized(user_id, expected_status):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == expected_status
```

### Request and httpx Libraries

```python
import requests
import httpx
import asyncio

# Requests (synchronous)
def test_with_requests():
    # GET
    response = requests.get("http://localhost:8000/users")
    assert response.status_code == 200
    data = response.json()
    
    # POST
    response = requests.post(
        "http://localhost:8000/users",
        json={"name": "Alice", "email": "alice@example.com"}
    )
    assert response.status_code == 201
    
    # With headers
    headers = {"Authorization": "Bearer token"}
    response = requests.get("http://localhost:8000/protected", headers=headers)
    
    # With timeout
    response = requests.get("http://localhost:8000/slow", timeout=5)

# httpx (supports async)
async def test_with_httpx():
    # Synchronous
    response = httpx.get("http://localhost:8000/users")
    assert response.status_code == 200
    
    # Asynchronous
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/users")
        assert response.status_code == 200
    
    # Multiple concurrent requests
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            client.get("http://localhost:8000/users/1"),
            client.get("http://localhost:8000/users/2"),
            client.get("http://localhost:8000/users/3"),
        )
        for result in results:
            assert result.status_code == 200

# Run async test
asyncio.run(test_with_httpx())

# Session for multiple requests
session = requests.Session()
session.headers.update({"Authorization": "Bearer token"})

response1 = session.get("http://localhost:8000/users")
response2 = session.get("http://localhost:8000/posts")
```

---

## Practical Examples

### Complete Blog API

```python
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Setup
DATABASE_URL = "sqlite:///./blog.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Models
class DBPost(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), unique=True)
    content = Column(Text)
    author = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Schemas
class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=10)
    author: str = Field(..., min_length=1)

class Post(PostCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# App
app = FastAPI(title="Blog API", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.get("/posts", response_model=list[Post], tags=["posts"])
def list_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    sort_by: str = Query("created_at"),
    db: Session = Query(..., include_in_schema=False)
):
    """List all blog posts with filtering and pagination."""
    query = db.query(DBPost)
    
    if search:
        query = query.filter(DBPost.title.ilike(f"%{search}%"))
    if author:
        query = query.filter(DBPost.author == author)
    
    if sort_by == "created_at":
        query = query.order_by(DBPost.created_at.desc())
    elif sort_by == "title":
        query = query.order_by(DBPost.title)
    
    total = query.count()
    posts = query.skip(skip).limit(limit).all()
    
    return posts

@app.get("/posts/{post_id}", response_model=Post, tags=["posts"])
def get_post(post_id: int, db: Session = Query(..., include_in_schema=False)):
    """Get a specific post by ID."""
    post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts", response_model=Post, status_code=201, tags=["posts"])
def create_post(post: PostCreate, db: Session = Query(..., include_in_schema=False)):
    """Create a new blog post."""
    db_post = DBPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.put("/posts/{post_id}", response_model=Post, tags=["posts"])
def update_post(
    post_id: int,
    post_update: PostCreate,
    db: Session = Query(..., include_in_schema=False)
):
    """Update an existing post."""
    post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    for key, value in post_update.dict().items():
        setattr(post, key, value)
    post.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(post)
    return post

@app.delete("/posts/{post_id}", status_code=204, tags=["posts"])
def delete_post(post_id: int, db: Session = Query(..., include_in_schema=False)):
    """Delete a post."""
    post = db.query(DBPost).filter(DBPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(post)
    db.commit()
```

---

## Best Practices

### API Design

```
✓ Use nouns for resources
✓ Use plural names
✓ Use HTTP verbs correctly
✓ Use proper status codes
✓ Validate input
✓ Handle errors gracefully
✓ Version your API
✓ Use pagination
✓ Document thoroughly
```

### Performance

```
✓ Use pagination
✓ Implement caching
✓ Rate limiting
✓ Database indexing
✓ Query optimization
✓ Async/await
✓ Connection pooling
```

### Security

```
✓ HTTPS only
✓ Authentication
✓ Authorization
✓ Input validation
✓ Rate limiting
✓ CORS properly
✓ SQL injection prevention
✓ XSS prevention
```

---

## Practice Exercises

### 1. Basic CRUD API
- Create resource endpoints
- Proper HTTP methods
- Error handling

### 2. Filtering and Sorting
- Implement filtering
- Implement sorting
- Pagination

### 3. Authentication
- Token-based auth
- Protected endpoints

### 4. Complete API
- Database integration
- Full CRUD
- Documentation
- Testing

---

# End of Notes
