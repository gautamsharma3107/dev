"""
Day 17 - FastAPI Basics
========================
Learn: FastAPI introduction, setup, and why it's popular

Key Concepts:
- FastAPI is a modern, fast web framework for building APIs
- Built on Python type hints for automatic validation
- Auto-generates interactive API documentation
- Supports async/await for high performance
"""

# ========== WHAT IS FASTAPI? ==========
print("=" * 60)
print("INTRODUCTION TO FASTAPI")
print("=" * 60)

"""
FastAPI is a modern, high-performance web framework for building APIs 
with Python 3.7+ based on standard Python type hints.

Key Features:
1. FAST - One of the fastest Python frameworks (on par with NodeJS and Go)
2. AUTO DOCUMENTATION - Swagger UI and ReDoc automatically generated
3. TYPE HINTS - Uses Python type hints for validation and documentation
4. ASYNC SUPPORT - Built-in support for async/await
5. PYDANTIC - Uses Pydantic for data validation
6. STANDARDS - Based on OpenAPI and JSON Schema standards
"""

# ========== INSTALLATION ==========
print("\n" + "=" * 60)
print("INSTALLATION")
print("=" * 60)

print("""
# Install FastAPI and ASGI server (Uvicorn)
pip install fastapi uvicorn[standard]

# Or install all dependencies
pip install fastapi[all]
""")

# ========== YOUR FIRST FASTAPI APP ==========
print("\n" + "=" * 60)
print("YOUR FIRST FASTAPI APP")
print("=" * 60)

# Save this as main.py and run with: uvicorn main:app --reload
example_code = '''
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
'''

print("Example FastAPI App:")
print(example_code)

print("""
To run this app:
1. Save the code as main.py
2. Run: uvicorn main:app --reload
3. Open: http://localhost:8000
4. Docs: http://localhost:8000/docs
""")

# ========== WHY FASTAPI IS POPULAR ==========
print("\n" + "=" * 60)
print("WHY FASTAPI IS POPULAR")
print("=" * 60)

print("""
1. SPEED & PERFORMANCE
   - Very fast due to Starlette and Pydantic
   - Comparable to NodeJS and Go
   - Async support built-in

2. DEVELOPER EXPERIENCE
   - Intuitive and easy to learn
   - Great code completion in IDEs
   - Reduces bugs with type hints

3. AUTOMATIC DOCUMENTATION
   - Swagger UI at /docs
   - ReDoc at /redoc
   - Generated from your code

4. DATA VALIDATION
   - Automatic request validation
   - Clear error messages
   - Powered by Pydantic

5. MODERN PYTHON
   - Uses type hints
   - Async/await support
   - Python 3.7+ features
""")

# ========== FASTAPI VS FLASK VS DJANGO ==========
print("\n" + "=" * 60)
print("FASTAPI VS FLASK VS DJANGO")
print("=" * 60)

print("""
╔════════════════╦════════════════╦════════════════╦════════════════╗
║    Feature     ║    FastAPI     ║     Flask      ║     Django     ║
╠════════════════╬════════════════╬════════════════╬════════════════╣
║ Speed          ║ ⭐⭐⭐⭐⭐     ║ ⭐⭐⭐         ║ ⭐⭐⭐         ║
║ Easy to Learn  ║ ⭐⭐⭐⭐       ║ ⭐⭐⭐⭐⭐     ║ ⭐⭐⭐         ║
║ Auto Docs      ║ ⭐⭐⭐⭐⭐     ║ ⭐⭐           ║ ⭐⭐⭐         ║
║ Async Support  ║ ⭐⭐⭐⭐⭐     ║ ⭐⭐           ║ ⭐⭐⭐         ║
║ Validation     ║ ⭐⭐⭐⭐⭐     ║ ⭐⭐           ║ ⭐⭐⭐⭐       ║
║ Full-Featured  ║ ⭐⭐⭐         ║ ⭐⭐           ║ ⭐⭐⭐⭐⭐     ║
║ Community      ║ ⭐⭐⭐⭐       ║ ⭐⭐⭐⭐⭐     ║ ⭐⭐⭐⭐⭐     ║
╚════════════════╩════════════════╩════════════════╩════════════════╝

Use FastAPI when:
- Building modern APIs
- Need high performance
- Want auto documentation
- Working with microservices
""")

# ========== BASIC APP STRUCTURE ==========
print("\n" + "=" * 60)
print("BASIC APP STRUCTURE")
print("=" * 60)

app_structure = '''
# Project Structure
my_fastapi_project/
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app
│   ├── routers/        # Route handlers
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── items.py
│   ├── models/         # Pydantic models
│   │   ├── __init__.py
│   │   └── schemas.py
│   └── database/       # Database connection
│       ├── __init__.py
│       └── db.py
└── tests/              # Test files
    └── test_main.py
'''

print(app_structure)

# ========== RUNNING THE APP ==========
print("\n" + "=" * 60)
print("RUNNING THE APP")
print("=" * 60)

print("""
# Development mode (with auto-reload)
uvicorn main:app --reload

# Specify host and port
uvicorn main:app --host 0.0.0.0 --port 8000

# Production mode (multiple workers)
uvicorn main:app --workers 4

# Run programmatically
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
""")

# ========== API DOCUMENTATION ==========
print("\n" + "=" * 60)
print("AUTOMATIC API DOCUMENTATION")
print("=" * 60)

print("""
FastAPI automatically generates interactive API documentation:

1. SWAGGER UI
   - URL: http://localhost:8000/docs
   - Interactive API testing
   - Try out endpoints directly

2. REDOC
   - URL: http://localhost:8000/redoc
   - Clean, readable documentation
   - Great for sharing with others

3. OPENAPI JSON
   - URL: http://localhost:8000/openapi.json
   - Machine-readable API spec
   - Can import into tools like Postman
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE")
print("=" * 60)

complete_example = '''
from fastapi import FastAPI

# Create app with metadata
app = FastAPI(
    title="My First API",
    description="A sample API built with FastAPI",
    version="1.0.0"
)

# Root endpoint
@app.get("/", tags=["root"])
def read_root():
    """Returns a welcome message."""
    return {"message": "Welcome to FastAPI!"}

# Health check endpoint
@app.get("/health", tags=["health"])
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

# Get item by ID
@app.get("/items/{item_id}", tags=["items"])
def read_item(item_id: int, q: str = None):
    """
    Get an item by ID.
    
    - **item_id**: The ID of the item (integer)
    - **q**: Optional query parameter
    """
    result = {"item_id": item_id}
    if q:
        result["query"] = q
    return result

# Run with: uvicorn filename:app --reload
'''

print("Complete Example:")
print(complete_example)

print("\n" + "=" * 60)
print("✅ FastAPI Basics - Complete!")
print("=" * 60)
print("""
Key Points to Remember:
1. FastAPI uses Python type hints for validation
2. Auto-generates Swagger and ReDoc documentation
3. Run with uvicorn: uvicorn main:app --reload
4. Access docs at /docs and /redoc
5. One of the fastest Python web frameworks
""")
