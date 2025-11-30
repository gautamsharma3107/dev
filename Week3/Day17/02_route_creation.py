"""
Day 17 - Route Creation in FastAPI
===================================
Learn: HTTP methods, path parameters, query parameters

Key Concepts:
- HTTP methods: GET, POST, PUT, DELETE, PATCH
- Path parameters with type hints
- Query parameters with defaults
- Combining path and query parameters
"""

# ========== HTTP METHODS ==========
print("=" * 60)
print("HTTP METHODS IN FASTAPI")
print("=" * 60)

http_methods_example = '''
from fastapi import FastAPI

app = FastAPI()

# GET - Retrieve data
@app.get("/items")
def get_items():
    return {"items": ["item1", "item2", "item3"]}

# POST - Create new data
@app.post("/items")
def create_item(item: dict):
    return {"created": item}

# PUT - Update existing data (full update)
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"updated": item_id, "data": item}

# DELETE - Remove data
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}

# PATCH - Partial update
@app.patch("/items/{item_id}")
def partial_update(item_id: int, item: dict):
    return {"partially_updated": item_id, "data": item}
'''

print("HTTP Methods Example:")
print(http_methods_example)

# ========== PATH PARAMETERS ==========
print("\n" + "=" * 60)
print("PATH PARAMETERS")
print("=" * 60)

path_params_example = '''
from fastapi import FastAPI

app = FastAPI()

# Basic path parameter (type hint provides automatic validation)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
    # /users/42 -> {"user_id": 42}
    # /users/abc -> Error: value is not a valid integer

# String path parameter
@app.get("/users/{username}")
def get_user_by_name(username: str):
    return {"username": username}
    # /users/john -> {"username": "john"}

# Multiple path parameters
@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}
    # /users/1/posts/5 -> {"user_id": 1, "post_id": 5}

# Path parameter that includes slashes (file paths)
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}
    # /files/home/user/document.txt -> {"file_path": "home/user/document.txt"}
'''

print("Path Parameters Example:")
print(path_params_example)

# ========== PATH PARAMETER VALIDATION ==========
print("\n" + "=" * 60)
print("PATH PARAMETER VALIDATION")
print("=" * 60)

validation_example = '''
from fastapi import FastAPI, Path

app = FastAPI()

# Path parameter with validation
@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(
        ...,  # Required
        title="Item ID",
        description="The ID of the item to retrieve",
        gt=0,  # Greater than 0
        le=1000  # Less than or equal to 1000
    )
):
    return {"item_id": item_id}

# Validation options:
# gt  - Greater than
# ge  - Greater than or equal
# lt  - Less than
# le  - Less than or equal
# min_length - Minimum string length
# max_length - Maximum string length
# regex - Regular expression pattern
'''

print("Path Validation Example:")
print(validation_example)

# ========== QUERY PARAMETERS ==========
print("\n" + "=" * 60)
print("QUERY PARAMETERS")
print("=" * 60)

query_params_example = '''
from fastapi import FastAPI

app = FastAPI()

# Required query parameters (no default value)
@app.get("/search")
def search(q: str):
    return {"query": q}
    # /search?q=python -> {"query": "python"}
    # /search -> Error: field required

# Optional query parameters (with default value)
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
    # /items -> {"skip": 0, "limit": 10}
    # /items?skip=5&limit=20 -> {"skip": 5, "limit": 20}

# Optional with None default
from typing import Optional

@app.get("/products")
def get_products(category: Optional[str] = None):
    if category:
        return {"category": category}
    return {"message": "All products"}

# Boolean query parameters
@app.get("/items")
def get_items(short: bool = False):
    if short:
        return {"items": "short list"}
    return {"items": "full list"}
    # /items?short=true -> {"items": "short list"}
    # /items?short=1 -> {"items": "short list"}
    # /items?short=yes -> {"items": "short list"}
'''

print("Query Parameters Example:")
print(query_params_example)

# ========== QUERY PARAMETER VALIDATION ==========
print("\n" + "=" * 60)
print("QUERY PARAMETER VALIDATION")
print("=" * 60)

query_validation_example = '''
from fastapi import FastAPI, Query

app = FastAPI()

# Query with validation
@app.get("/items")
def get_items(
    q: str = Query(
        None,  # Default value
        min_length=3,
        max_length=50,
        description="Search query"
    ),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    return {"q": q, "skip": skip, "limit": limit}

# Required query parameter with validation
@app.get("/search")
def search(
    q: str = Query(
        ...,  # Required (no default)
        min_length=1,
        title="Search Query",
        description="Query string to search for"
    )
):
    return {"query": q}

# Query with regex validation
@app.get("/users")
def get_users(
    email: str = Query(
        ...,
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )
):
    return {"email": email}

# Multiple values for same query parameter
@app.get("/items")
def get_items(q: list[str] = Query(None)):
    return {"q": q}
    # /items?q=foo&q=bar -> {"q": ["foo", "bar"]}
'''

print("Query Validation Example:")
print(query_validation_example)

# ========== COMBINING PATH AND QUERY ==========
print("\n" + "=" * 60)
print("COMBINING PATH AND QUERY PARAMETERS")
print("=" * 60)

combined_example = '''
from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

# Path + Query parameters
@app.get("/users/{user_id}/items")
def get_user_items(
    user_id: int = Path(..., title="User ID", ge=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    sort: Optional[str] = Query(None)
):
    return {
        "user_id": user_id,
        "skip": skip,
        "limit": limit,
        "sort": sort
    }
    # /users/1/items?skip=0&limit=5&sort=name

# Order of parameters doesn't matter
# FastAPI identifies path vs query by their position in the path
@app.get("/items/{item_id}")
def get_item(
    q: str,  # Query (not in path)
    item_id: int,  # Path (in path)
    short: bool = False  # Query with default
):
    return {"item_id": item_id, "q": q, "short": short}
'''

print("Combined Example:")
print(combined_example)

# ========== ROUTE ORDERING ==========
print("\n" + "=" * 60)
print("ROUTE ORDERING (IMPORTANT!)")
print("=" * 60)

order_example = '''
from fastapi import FastAPI

app = FastAPI()

# IMPORTANT: Order matters for routes!
# More specific routes should come BEFORE dynamic routes

# This should come FIRST (specific route)
@app.get("/users/me")
def get_current_user():
    return {"user": "current user"}

# This should come AFTER (dynamic route)
@app.get("/users/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id}

# If reversed, /users/me would match the dynamic route
# and "me" would be treated as user_id
'''

print("Route Ordering Example:")
print(order_example)

# ========== ROUTE TAGS AND DESCRIPTIONS ==========
print("\n" + "=" * 60)
print("ROUTE TAGS AND DESCRIPTIONS")
print("=" * 60)

tags_example = '''
from fastapi import FastAPI

app = FastAPI()

# Tags group endpoints in documentation
@app.get("/users/", tags=["users"])
def get_users():
    """Get all users."""
    return {"users": []}

@app.post("/users/", tags=["users"])
def create_user(user: dict):
    """
    Create a new user.
    
    - **name**: User's name (required)
    - **email**: User's email (required)
    """
    return {"user": user}

@app.get("/items/", tags=["items"])
def get_items():
    """Get all items."""
    return {"items": []}

# Deprecated routes
@app.get("/old-endpoint", deprecated=True)
def old_endpoint():
    """This endpoint is deprecated."""
    return {"message": "Use /new-endpoint instead"}
'''

print("Tags and Descriptions Example:")
print(tags_example)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: USER API")
print("=" * 60)

practical_example = '''
from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI(title="User API", version="1.0.0")

# In-memory database
users_db = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}

# GET all users with pagination
@app.get("/users/", tags=["users"])
def get_users(
    skip: int = Query(0, ge=0, description="Number of users to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max users to return")
):
    """Get list of all users with pagination."""
    users = list(users_db.values())
    return users[skip: skip + limit]

# GET current user (must be before /{user_id})
@app.get("/users/me", tags=["users"])
def get_current_user():
    """Get currently logged in user."""
    return {"user": "Current User", "id": 1}

# GET user by ID
@app.get("/users/{user_id}", tags=["users"])
def get_user(
    user_id: int = Path(..., title="User ID", ge=1)
):
    """Get a specific user by ID."""
    if user_id in users_db:
        return users_db[user_id]
    return {"error": "User not found"}

# Search users
@app.get("/users/search/", tags=["users"])
def search_users(
    q: str = Query(..., min_length=2, description="Search query"),
    field: str = Query("name", description="Field to search")
):
    """Search users by name or email."""
    results = []
    for user_id, user in users_db.items():
        if field in user and q.lower() in user[field].lower():
            results.append({"id": user_id, **user})
    return results

# DELETE user
@app.delete("/users/{user_id}", tags=["users"])
def delete_user(user_id: int = Path(..., ge=1)):
    """Delete a user by ID."""
    if user_id in users_db:
        del users_db[user_id]
        return {"deleted": user_id}
    return {"error": "User not found"}
'''

print("Practical User API Example:")
print(practical_example)

print("\n" + "=" * 60)
print("✅ Route Creation - Complete!")
print("=" * 60)
print("""
Key Points to Remember:
1. Use decorators: @app.get(), @app.post(), @app.put(), @app.delete()
2. Path parameters are in the URL path: /users/{user_id}
3. Query parameters are after ?: /users?skip=0&limit=10
4. Use Path() and Query() for validation
5. Order matters: specific routes before dynamic routes
6. Use tags to organize endpoints in documentation
""")
