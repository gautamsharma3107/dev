# Day 17 Quick Reference Cheat Sheet

## FastAPI Installation
```bash
pip install fastapi uvicorn[standard]
uvicorn main:app --reload
```

## Basic App Structure
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

## HTTP Methods
```python
@app.get("/items")       # Read
@app.post("/items")      # Create
@app.put("/items/{id}")  # Update (full)
@app.patch("/items/{id}")# Update (partial)
@app.delete("/items/{id}")# Delete
```

## Path Parameters
```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# With validation
from fastapi import Path

@app.get("/items/{item_id}")
def get_item(item_id: int = Path(..., gt=0, le=1000)):
    return {"item_id": item_id}
```

## Query Parameters
```python
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# With validation
from fastapi import Query

@app.get("/items")
def get_items(q: str = Query(None, min_length=3, max_length=50)):
    return {"q": q}
```

## Pydantic Models
```python
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    description: Optional[str] = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

## Response Models
```python
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    return {"id": 1, **item.dict()}
```

## Status Codes
```python
from fastapi import status

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return item

# Common codes:
# 200 - OK
# 201 - Created
# 204 - No Content
# 400 - Bad Request
# 404 - Not Found
# 422 - Validation Error
```

## Error Handling
```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Not found")
    return items_db[item_id]
```

## Headers and Cookies
```python
from fastapi import Header, Cookie, Response

# Reading headers
@app.get("/items/")
def read_items(x_token: str = Header(None)):
    return {"X-Token": x_token}

# Setting cookies
@app.post("/login/")
def login(response: Response):
    response.set_cookie(key="session", value="abc123")
    return {"message": "Logged in"}
```

## File Uploads
```python
from fastapi import File, UploadFile

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}
```

## Form Data
```python
from fastapi import Form

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
```

## Custom Validators
```python
from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    
    @validator("name")
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v.title()
```

## Nested Models
```python
class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    address: Address
```

## API Documentation
```
Swagger UI: http://localhost:8000/docs
ReDoc:      http://localhost:8000/redoc
OpenAPI:    http://localhost:8000/openapi.json
```

## App Configuration
```python
app = FastAPI(
    title="My API",
    description="API description",
    version="1.0.0"
)
```

## Tags for Organization
```python
@app.get("/users/", tags=["users"])
def get_users():
    return []

@app.get("/items/", tags=["items"])
def get_items():
    return []
```

## Common Patterns
```python
# CRUD operations
@app.post("/", status_code=201)   # Create
@app.get("/")                      # Read all
@app.get("/{id}")                  # Read one
@app.put("/{id}")                  # Update full
@app.patch("/{id}")                # Update partial
@app.delete("/{id}", status_code=204)  # Delete

# Pagination
def get_items(skip: int = 0, limit: int = 10):
    return items[skip: skip + limit]

# Search
def search(q: str = Query(None)):
    if q:
        return [i for i in items if q in i["name"]]
    return items
```

---
**Keep this handy for quick reference!** 🚀
