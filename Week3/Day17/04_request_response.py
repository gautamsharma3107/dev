"""
Day 17 - Request/Response Handling in FastAPI
==============================================
Learn: Handling requests and responses effectively

Key Concepts:
- Request body handling
- Response models and status codes
- Headers and cookies
- Error handling with HTTPException
"""

# ========== REQUEST BODY ==========
print("=" * 60)
print("REQUEST BODY HANDLING")
print("=" * 60)

request_body_example = '''
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Request body model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int = 1

# POST with request body
@app.post("/items/")
def create_item(item: Item):
    # item is automatically parsed and validated
    return {
        "name": item.name,
        "price": item.price,
        "total": item.price * item.quantity
    }

# Request body with path and query parameters
@app.put("/items/{item_id}")
def update_item(
    item_id: int,           # Path parameter
    item: Item,             # Request body
    q: Optional[str] = None # Query parameter
):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result["q"] = q
    return result

# Multiple request bodies
class User(BaseModel):
    username: str
    email: str

class Order(BaseModel):
    item_id: int
    quantity: int

@app.post("/orders/")
def create_order(user: User, order: Order):
    return {
        "user": user.dict(),
        "order": order.dict()
    }
'''

print("Request Body Example:")
print(request_body_example)

# ========== RESPONSE MODELS ==========
print("\n" + "=" * 60)
print("RESPONSE MODELS")
print("=" * 60)

response_model_example = '''
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI()

# Input model (includes password)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Output model (excludes password!)
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

# Using response_model to filter output
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    # Even if we return the password, it won't be in the response
    fake_user = {
        "id": 1,
        "username": user.username,
        "email": user.email,
        "password": user.password  # This will be excluded!
    }
    return fake_user

# List response
@app.get("/users/", response_model=List[UserResponse])
def get_users():
    return [
        {"id": 1, "username": "alice", "email": "alice@example.com"},
        {"id": 2, "username": "bob", "email": "bob@example.com"}
    ]

# Response model with exclude/include
@app.get("/users/{user_id}", response_model=UserResponse, response_model_exclude={"email"})
def get_user(user_id: int):
    return {"id": user_id, "username": "alice", "email": "alice@example.com"}
    # email will be excluded from response
'''

print("Response Model Example:")
print(response_model_example)

# ========== STATUS CODES ==========
print("\n" + "=" * 60)
print("STATUS CODES")
print("=" * 60)

status_codes_example = '''
from fastapi import FastAPI, status

app = FastAPI()

# 201 Created for POST
@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: dict):
    return item

# 204 No Content for DELETE
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    # Return None for 204
    return None

# Custom status code
@app.post("/upload/", status_code=202)  # Accepted
def upload_file():
    return {"message": "File accepted for processing"}

# Common status codes:
# 200 OK - Success
# 201 Created - Resource created
# 204 No Content - Success with no response body
# 400 Bad Request - Client error
# 401 Unauthorized - Authentication required
# 403 Forbidden - Not allowed
# 404 Not Found - Resource not found
# 422 Unprocessable Entity - Validation error
# 500 Internal Server Error - Server error

# Using status module
from fastapi import status

status.HTTP_200_OK
status.HTTP_201_CREATED
status.HTTP_204_NO_CONTENT
status.HTTP_400_BAD_REQUEST
status.HTTP_401_UNAUTHORIZED
status.HTTP_403_FORBIDDEN
status.HTTP_404_NOT_FOUND
status.HTTP_422_UNPROCESSABLE_ENTITY
status.HTTP_500_INTERNAL_SERVER_ERROR
'''

print("Status Codes Example:")
print(status_codes_example)

# ========== ERROR HANDLING ==========
print("\n" + "=" * 60)
print("ERROR HANDLING")
print("=" * 60)

error_handling_example = '''
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# In-memory database
items_db = {1: {"name": "Item 1"}, 2: {"name": "Item 2"}}

# Raise HTTPException for errors
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return items_db[item_id]

# Custom headers in exception
@app.get("/protected/")
def protected_route():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

# Detailed error response
@app.post("/items/")
def create_item(item: dict):
    if "name" not in item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "validation_error",
                "message": "Name is required",
                "field": "name"
            }
        )
    return item

# Custom exception handler
from fastapi import Request
from fastapi.responses import JSONResponse

class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something wrong."}
    )

@app.get("/custom-error/")
def custom_error():
    raise CustomException(name="Something")
'''

print("Error Handling Example:")
print(error_handling_example)

# ========== HEADERS AND COOKIES ==========
print("\n" + "=" * 60)
print("HEADERS AND COOKIES")
print("=" * 60)

headers_cookies_example = '''
from fastapi import FastAPI, Header, Cookie, Response
from typing import Optional

app = FastAPI()

# Reading headers
@app.get("/items/")
def read_items(
    user_agent: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    x_token: Optional[str] = Header(None)
):
    return {
        "User-Agent": user_agent,
        "Accept-Language": accept_language,
        "X-Token": x_token
    }

# Reading cookies
@app.get("/cookies/")
def read_cookies(
    session_id: Optional[str] = Cookie(None),
    user_id: Optional[str] = Cookie(None)
):
    return {
        "session_id": session_id,
        "user_id": user_id
    }

# Setting headers in response
@app.get("/custom-headers/")
def custom_headers(response: Response):
    response.headers["X-Custom-Header"] = "Custom Value"
    response.headers["X-Process-Time"] = "0.5"
    return {"message": "Headers set!"}

# Setting cookies
@app.post("/login/")
def login(response: Response):
    response.set_cookie(
        key="session_id",
        value="abc123",
        max_age=3600,  # 1 hour
        httponly=True,
        secure=True,  # HTTPS only
        samesite="lax"
    )
    return {"message": "Logged in!"}

# Deleting cookies
@app.post("/logout/")
def logout(response: Response):
    response.delete_cookie(key="session_id")
    return {"message": "Logged out!"}
'''

print("Headers and Cookies Example:")
print(headers_cookies_example)

# ========== CUSTOM RESPONSES ==========
print("\n" + "=" * 60)
print("CUSTOM RESPONSES")
print("=" * 60)

custom_responses_example = '''
from fastapi import FastAPI
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    FileResponse,
    StreamingResponse
)

app = FastAPI()

# JSON Response (default)
@app.get("/json/")
def json_response():
    return JSONResponse(
        content={"message": "Hello"},
        status_code=200,
        headers={"X-Custom": "Header"}
    )

# HTML Response
@app.get("/html/", response_class=HTMLResponse)
def html_response():
    return """
    <html>
        <head><title>Hello</title></head>
        <body><h1>Hello World!</h1></body>
    </html>
    """

# Plain Text Response
@app.get("/text/", response_class=PlainTextResponse)
def text_response():
    return "Hello, plain text!"

# Redirect Response
@app.get("/redirect/")
def redirect():
    return RedirectResponse(url="/")

# File Response
@app.get("/download/")
def download_file():
    return FileResponse(
        path="document.pdf",
        filename="download.pdf",
        media_type="application/pdf"
    )

# Streaming Response (for large data)
@app.get("/stream/")
def stream_response():
    def generate():
        for i in range(100):
            yield f"data: {i}\\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )
'''

print("Custom Responses Example:")
print(custom_responses_example)

# ========== FORM DATA AND FILE UPLOADS ==========
print("\n" + "=" * 60)
print("FORM DATA AND FILE UPLOADS")
print("=" * 60)

form_upload_example = '''
from fastapi import FastAPI, Form, File, UploadFile
from typing import List

app = FastAPI()

# Form data (application/x-www-form-urlencoded)
@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

# File upload
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)
    }

# Multiple file upload
@app.post("/upload-many/")
async def upload_files(files: List[UploadFile] = File(...)):
    return [{"filename": f.filename} for f in files]

# Form data with file
@app.post("/submit/")
async def submit_form(
    title: str = Form(...),
    description: str = Form(None),
    file: UploadFile = File(...)
):
    return {
        "title": title,
        "description": description,
        "filename": file.filename
    }

# Save uploaded file
import shutil
from pathlib import Path

@app.post("/save-file/")
async def save_file(file: UploadFile = File(...)):
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)
    
    file_path = upload_dir / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"saved": str(file_path)}
'''

print("Form Data and File Upload Example:")
print(form_upload_example)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: COMPLETE CRUD API")
print("=" * 60)

practical_example = '''
from fastapi import FastAPI, HTTPException, status, Header
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

app = FastAPI(title="Task API", version="1.0.0")

# Models
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

# In-memory database
tasks_db = {}
next_id = 1

# Helper function
def get_task_or_404(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )
    return tasks_db[task_id]

# Endpoints
@app.get("/tasks/", response_model=List[TaskResponse], tags=["tasks"])
def get_all_tasks(
    skip: int = 0,
    limit: int = 10,
    completed: Optional[bool] = None
):
    """Get all tasks with optional filtering."""
    tasks = list(tasks_db.values())
    
    # Filter by completed status
    if completed is not None:
        tasks = [t for t in tasks if t["completed"] == completed]
    
    return tasks[skip: skip + limit]

@app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED, tags=["tasks"])
def create_task(task: TaskCreate):
    """Create a new task."""
    global next_id
    
    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": datetime.utcnow(),
        "updated_at": None
    }
    
    tasks_db[next_id] = new_task
    next_id += 1
    
    return new_task

@app.get("/tasks/{task_id}", response_model=TaskResponse, tags=["tasks"])
def get_task(task_id: int):
    """Get a specific task by ID."""
    return get_task_or_404(task_id)

@app.put("/tasks/{task_id}", response_model=TaskResponse, tags=["tasks"])
def update_task(task_id: int, task: TaskCreate):
    """Full update of a task."""
    get_task_or_404(task_id)
    
    updated_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": tasks_db[task_id]["created_at"],
        "updated_at": datetime.utcnow()
    }
    
    tasks_db[task_id] = updated_task
    return updated_task

@app.patch("/tasks/{task_id}", response_model=TaskResponse, tags=["tasks"])
def partial_update_task(task_id: int, task: TaskUpdate):
    """Partial update of a task."""
    stored_task = get_task_or_404(task_id)
    
    # Only update provided fields
    update_data = task.dict(exclude_unset=True)
    for field, value in update_data.items():
        stored_task[field] = value
    
    stored_task["updated_at"] = datetime.utcnow()
    return stored_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"])
def delete_task(task_id: int):
    """Delete a task."""
    get_task_or_404(task_id)
    del tasks_db[task_id]
    return None

@app.post("/tasks/{task_id}/complete", response_model=TaskResponse, tags=["tasks"])
def mark_complete(task_id: int):
    """Mark a task as complete."""
    task = get_task_or_404(task_id)
    task["completed"] = True
    task["updated_at"] = datetime.utcnow()
    return task
'''

print("Complete CRUD API Example:")
print(practical_example)

print("\n" + "=" * 60)
print("✅ Request/Response Handling - Complete!")
print("=" * 60)
print("""
Key Points to Remember:
1. Use Pydantic models for request body validation
2. response_model controls what data is returned
3. Use status codes appropriately (201 for create, 204 for delete)
4. Raise HTTPException for error responses
5. Access headers with Header(), cookies with Cookie()
6. Use Response object to set custom headers/cookies
7. Form() for form data, File() for file uploads
8. Different response classes: JSON, HTML, File, Streaming
""")
