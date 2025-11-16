# FastAPI Modern Framework: Complete Guide

---

## Table of Contents
1. [Introduction to FastAPI](#introduction-to-fastapi)
2. [FastAPI Basics](#fastapi-basics)
3. [Path Operations](#path-operations)
4. [Request Body](#request-body)
5. [Response Models](#response-models)
6. [Dependency Injection](#dependency-injection)
7. [Security](#security)
8. [Database Integration](#database-integration)
9. [Async Programming](#async-programming)
10. [Advanced Features](#advanced-features)
11. [Documentation](#documentation)
12. [Practical Examples](#practical-examples)
13. [Best Practices](#best-practices)
14. [Practice Exercises](#practice-exercises)

---

## Introduction to FastAPI

### What is FastAPI?

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+, based on standard Python type hints.

### FastAPI Philosophy

```
Modern Standards:
- Type hints (Python 3.6+)
- Async/await support
- Automatic validation
- Auto-generated documentation
- High performance (near Node.js/Go speeds)

Built on Standards:
- OpenAPI (Swagger)
- JSON Schema
- OAuth2
- Pydantic for data validation
```

### FastAPI vs Flask vs Django vs Others

```
FastAPI:
✓ Modern async
✓ Automatic validation
✓ Auto docs (Swagger, ReDoc)
✓ Type hints
✓ Fastest Python framework
✓ APIs focused
✗ Newer (less ecosystem)

Flask:
✓ Lightweight
✓ Flexible
✓ Easy to learn
✗ Synchronous
✗ No auto validation

Django:
✓ Full-featured
✓ Admin panel
✓ Batteries included
✗ Heavier
✗ Synchronous

FastAPI Use Cases:
- Modern APIs
- Microservices
- High-performance backends
- Real-time applications
```

---

## FastAPI Basics

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install FastAPI
pip install fastapi

# Install Uvicorn (ASGI server)
pip install uvicorn[standard]

# Or both together
pip install fastapi uvicorn[standard]
```

### Creating Your First App

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Running the App

```bash
# Run development server
uvicorn main:app --reload

# Run on specific host/port
uvicorn main:app --host 0.0.0.0 --port 8000

# Production server (multiple workers)
uvicorn main:app --workers 4

# With auto reload
uvicorn main:app --reload
```

### Application Factory Pattern

```python
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    # Middleware setup
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
    
    app = FastAPI(middleware=middleware)
    
    # Include routers
    from routers import users, posts
    app.include_router(users.router, prefix="/api/users", tags=["users"])
    app.include_router(posts.router, prefix="/api/posts", tags=["posts"])
    
    return app

app = create_app()
```

---

## Path Operations

### HTTP Methods

```python
from fastapi import FastAPI

app = FastAPI()

# GET
@app.get("/items")
def get_items():
    return {"items": []}

# POST
@app.post("/items")
def create_item(item: dict):
    return {"created": item}

# PUT
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"updated": item}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}

# PATCH
@app.patch("/items/{item_id}")
def partial_update(item_id: int, item: dict):
    return {"partially_updated": item}

# Multiple methods
@app.api_route("/items/{item_id}", methods=["GET", "POST"])
def handle_item(item_id: int):
    return {"item_id": item_id}
```

### Path Parameters

```python
# Integer parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# String parameter
@app.get("/users/{user_name}")
def read_user(user_name: str):
    return {"user_name": user_name}

# Path parameter with validation
from fastapi import Path

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., gt=0, le=1000)):
    return {"item_id": item_id}

# Multiple path parameters
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: int):
    return {"user_id": user_id, "item_id": item_id}

# Path with file path
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}
```

### Query Parameters

```python
# Optional query parameters
@app.get("/items")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Query parameter validation
from fastapi import Query

@app.get("/items")
def read_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    return {"skip": skip, "limit": limit}

# Query parameter with regex
@app.get("/items")
def read_items(
    q: str = Query(..., regex="^[a-zA-Z]+$")
):
    return {"q": q}

# Multiple values for same query parameter
@app.get("/items")
def read_items(q: list[str] = Query(None)):
    # URL: /items?q=apple&q=banana&q=cherry
    return {"q": q}
```

---

## Request Body

### Pydantic Models

```python
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime

# Basic model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Model with default values and validation
class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    age: int = Field(..., ge=0, le=150)
    is_active: bool = True

# Model with validators
class Post(BaseModel):
    title: str
    content: str
    tags: list[str] = []
    
    @validator('title')
    def title_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty')
        return v
    
    @validator('tags')
    def validate_tags(cls, v):
        if len(v) > 10:
            raise ValueError('Maximum 10 tags allowed')
        return v

# Nested models
class Author(BaseModel):
    name: str
    email: str

class Blog(BaseModel):
    title: str
    author: Author
    content: str

# Model with complex types
class Article(BaseModel):
    title: str
    published_at: datetime
    tags: list[str]
    metadata: dict
```

### Data Validation

```python
from pydantic import BaseModel, validator, root_validator

class Product(BaseModel):
    name: str
    price: float
    quantity: int
    
    @validator('price')
    def price_positive(cls, v):
        if v < 0:
            raise ValueError('Price must be positive')
        return v
    
    @validator('quantity')
    def quantity_valid(cls, v):
        if v < 0:
            raise ValueError('Quantity must be non-negative')
        return v
    
    @root_validator
    def validate_stock(cls, values):
        price = values.get('price')
        quantity = values.get('quantity')
        if price > 1000 and quantity < 10:
            raise ValueError('High-price items need minimum 10 units')
        return values
```

### Request Body with Path and Query

```python
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float

app = FastAPI()

# All three combined
@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item,
    q: str = None,
    short: bool = False
):
    result = {"item_id": item_id, "item": item}
    if q:
        result["q"] = q
    if short:
        result["short"] = "Item updated"
    return result

# Multiple body parameters
class User(BaseModel):
    username: str
    email: str

class Item(BaseModel):
    name: str
    price: float

@app.post("/users/{user_id}/items")
def create_user_item(user_id: int, user: User, item: Item):
    return {
        "user_id": user_id,
        "user": user,
        "item": item
    }
```

---

## Response Models

### Response Models

```python
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = 0

app = FastAPI()

# Simple response model
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item

# Response with status code
@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    return item

# Multiple response models
from typing import Union

@app.get("/items/{item_id}", response_model=Union[Item, dict])
def get_item(item_id: int):
    if item_id == 1:
        return Item(name="Item", description="Desc", price=10.0)
    return {"error": "Not found"}

# List response
@app.get("/items/", response_model=list[Item])
def get_items():
    return [
        Item(name="Item1", description="Desc1", price=10.0),
        Item(name="Item2", description="Desc2", price=20.0),
    ]
```

### Status Codes

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: dict):
    return item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None

@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def get_item(item_id: int):
    return {"item_id": item_id}

# Custom status codes
@app.post(
    "/items/",
    status_code=201,
    responses={
        201: {"description": "Item created"},
        400: {"description": "Invalid data"},
    }
)
def create_item(item: dict):
    return item
```

### Response Customization

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
from pydantic import BaseModel

app = FastAPI()

# Custom JSON response
@app.get("/items/")
def get_items():
    return JSONResponse(
        status_code=200,
        content={"items": []},
        headers={"X-Custom-Header": "value"}
    )

# File response
@app.get("/download")
def download_file():
    return FileResponse("file.pdf", media_type="application/pdf")

# Streaming response
@app.get("/stream")
def stream_data():
    def generator():
        for i in range(100):
            yield f"data: {i}\n"
    return StreamingResponse(generator(), media_type="text/event-stream")
```

---

## Dependency Injection

### Basic Dependencies

```python
from fastapi import FastAPI, Depends

app = FastAPI()

# Simple dependency
def get_query(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(get_query)):
    return commons

# Dependency with validation
from fastapi import Query

def validate_pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def read_items(params: dict = Depends(validate_pagination)):
    return params
```

### Classes as Dependencies

```python
from fastapi import FastAPI, Depends

class Pagination:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit

class CommonParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit

app = FastAPI()

@app.get("/items/")
def read_items(commons: CommonParams = Depends(CommonParams)):
    return commons

# Simplified (FastAPI infers from __init__)
@app.get("/items/")
def read_items(commons: CommonParams = Depends()):
    return {"q": commons.q, "skip": commons.skip}
```

### Sub-dependencies

```python
from fastapi import FastAPI, Depends

def get_db():
    db = "database_connection"
    return db

def get_current_user(db = Depends(get_db)):
    return {"username": "alice", "db": db}

def get_user_posts(user = Depends(get_current_user)):
    return {"user": user, "posts": []}

app = FastAPI()

@app.get("/posts/")
def read_posts(posts = Depends(get_user_posts)):
    return posts
```

---

## Security

### OAuth2 with Password Flow

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt

app = FastAPI()

# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

class User(BaseModel):
    username: str
    email: str

# Mock database
fake_users = {
    "alice": {"username": "alice", "password": "hashed_password"}
}

# Functions
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401)
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401)
    
    return username

# Endpoints
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users.get(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user, "email": f"{current_user}@example.com"}
```

### JWT Tokens

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthCredentials
import jwt
from datetime import datetime, timedelta

app = FastAPI()
security = HTTPBearer()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def verify_jwt(credentials: HTTPAuthCredentials = Depends(security)):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401)
        return username
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401)

@app.get("/protected")
async def protected_route(username: str = Depends(verify_jwt)):
    return {"username": username}
```

### API Key Security

```python
from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security import APIKey, APIKeyCookie, APIKeyHeader, APIKeyQuery

app = FastAPI()

# API Key in header
api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "your-api-key":
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

@app.get("/protected")
async def protected_route(api_key: str = Depends(verify_api_key)):
    return {"message": "Access granted"}

# API Key in query
api_key_query = APIKeyQuery(name="api_key")

@app.get("/data")
async def get_data(api_key: str = Depends(api_key_query)):
    if api_key != "correct-key":
        raise HTTPException(status_code=403)
    return {"data": "value"}
```

---

## Database Integration

### SQLAlchemy Integration

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from datetime import datetime

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model
class DBUser(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Pydantic schema
class UserSchema(BaseModel):
    username: str
    email: str
    
    class Config:
        from_attributes = True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI app
app = FastAPI()

@app.post("/users/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = DBUser(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=list[UserSchema])
def read_users(db: Session = Depends(get_db)):
    return db.query(DBUser).all()

@app.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(DBUser).filter(DBUser.id == user_id).first()
```

### Async Database Operations

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import asyncio

# Async engine
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Async endpoint
@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    from sqlalchemy import select
    result = await db.execute(select(DBUser))
    return result.scalars().all()
```

### Databases Library

```bash
pip install databases
pip install sqlalchemy
```

```python
from databases import Database
from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine
from fastapi import FastAPI

DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("email", String),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/")
async def create_user(username: str, email: str):
    query = users_table.insert().values(username=username, email=email)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, "username": username, "email": email}

@app.get("/users/")
async def get_users():
    query = users_table.select()
    return await database.fetch_all(query)
```

---

## Async Programming

### Async/Await

```python
import asyncio
from fastapi import FastAPI

app = FastAPI()

async def slow_operation():
    await asyncio.sleep(1)
    return "Done"

@app.get("/slow")
async def slow_endpoint():
    result = await slow_operation()
    return {"result": result}

# Multiple concurrent operations
async def fetch_data():
    await asyncio.sleep(1)
    return "data"

@app.get("/concurrent")
async def concurrent_endpoint():
    results = await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data()
    )
    return {"results": results}
```

### Async Path Operations

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/items/")
async def read_items():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/items")
        return response.json()

@app.post("/items/")
async def create_item(item: dict):
    # Async database operation
    result = await save_to_db(item)
    return result
```

### Background Tasks

```python
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse

app = FastAPI()

def write_notification(email: str, message: str = ""):
    with open("log.txt", "a") as f:
        content = f"Email: {email}, Message: {message}\n"
        f.write(content)

@app.post("/send-notification/")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="Notification sent")
    return {"message": "Notification sent in background"}

# Multiple background tasks
@app.post("/send-multiple/")
async def send_multiple(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="First")
    background_tasks.add_task(write_notification, email, message="Second")
    return {"message": "Multiple tasks queued"}
```

---

## Advanced Features

### WebSockets

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except Exception:
        pass

# Broadcast to multiple clients
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/chat/{room_id}")
async def websocket_chat(websocket: WebSocket, room_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Room {room_id}: {data}")
    except Exception:
        manager.disconnect(websocket)
```

### File Uploads

```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(await file.read())
    }

@app.post("/upload-multiple/")
async def upload_multiple(files: list[UploadFile] = File(...)):
    return [{"filename": file.filename} for file in files]

# Save file to disk
from pathlib import Path

@app.post("/save-file/")
async def save_file(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Save to disk
    path = Path("uploads") / file.filename
    path.parent.mkdir(exist_ok=True)
    path.write_bytes(contents)
    
    return {"filename": file.filename, "saved": True}
```

### CORS Middleware

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (development only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://example.com",
        "https://www.example.com",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

---

## Documentation

### Automatic Interactive Docs

FastAPI automatically generates documentation from your code:

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="A sample API",
    version="1.0.0",
)

@app.get("/items/{item_id}", tags=["items"])
async def read_item(item_id: int):
    """
    Get an item by ID.
    
    - **item_id**: The ID of the item to retrieve
    """
    return {"item_id": item_id}

@app.post("/items/", tags=["items"])
async def create_item(item: dict):
    """
    Create a new item.
    """
    return item
```

### Swagger UI and ReDoc

```bash
# Automatic endpoints:
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
# OpenAPI JSON: http://localhost:8000/openapi.json
```

### Custom Documentation

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Custom API",
        version="1.0.0",
        description="Custom API description",
        routes=app.routes,
    )
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

---

## Practical Examples

### Complete Todo API

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoCreate):
    id: int
    created_at: datetime

# In-memory storage
todos_db = []
next_id = 1

@app.get("/todos/", response_model=list[Todo])
async def get_todos(skip: int = 0, limit: int = 10):
    return todos_db[skip: skip + limit]

@app.post("/todos/", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(
        id=next_id,
        **todo.dict(),
        created_at=datetime.utcnow()
    )
    todos_db.append(new_todo)
    next_id += 1
    return new_todo

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_update: TodoCreate):
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            updated = Todo(id=todo_id, **todo_update.dict(), created_at=todo.created_at)
            todos_db[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Todo not found")
```

---

## Best Practices

### Code Organization

```
✓ Use routers for modular code
✓ Separate models, schemas, dependencies
✓ Use dependency injection
✓ Proper error handling
✓ Type hints everywhere
✓ Async all the way
```

### Performance

```
✓ Use async/await
✓ Database query optimization
✓ Connection pooling
✓ Caching
✓ Pagination
✓ Proper indexing
```

### Security

```
✓ Use HTTPS in production
✓ Validate input strictly
✓ Use parameterized queries
✓ Secure password hashing
✓ Rate limiting
✓ CORS properly configured
```

---

## Practice Exercises

### 1. Basic CRUD
- Create simple todo API
- All CRUD operations
- Proper status codes

### 2. Authentication
- Implement JWT auth
- Protected endpoints
- Token refresh

### 3. Database
- SQLAlchemy integration
- Async operations
- Relationships

### 4. Advanced
- WebSockets
- File uploads
- Background tasks

### 5. Complete Application
- Full API with auth
- Database integration
- Proper error handling
- Documentation

---

# End of Notes
