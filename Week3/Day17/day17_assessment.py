"""
DAY 17 ASSESSMENT TEST
=======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 17 ASSESSMENT TEST - FastAPI Introduction")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. Which command is used to run a FastAPI application?
a) python main.py
b) flask run
c) uvicorn main:app --reload
d) fastapi run main.py

Your answer: """)

print("""
Q2. What library does FastAPI use for data validation?
a) Marshmallow
b) Pydantic
c) Cerberus
d) Django Forms

Your answer: """)

print("""
Q3. Where can you access the automatic Swagger documentation in FastAPI?
a) /swagger
b) /api-docs
c) /docs
d) /documentation

Your answer: """)

print("""
Q4. Which decorator is used for a POST endpoint in FastAPI?
a) @app.route("/", methods=["POST"])
b) @app.post("/")
c) @post("/")
d) @app.create("/")

Your answer: """)

print("""
Q5. What happens when a Pydantic model validation fails in FastAPI?
a) Returns 500 Internal Server Error
b) Returns 400 Bad Request
c) Returns 422 Unprocessable Entity
d) Silently ignores the error

Your answer: """)

print("""
Q6. How do you make a query parameter optional in FastAPI?
a) Use Optional[str] = None
b) Use required=False
c) Use optional=True
d) Query parameters are always optional

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a FastAPI endpoint that:
- Uses GET method at path "/items/{item_id}"
- Accepts an integer path parameter "item_id"
- Accepts an optional query parameter "q" (string)
- Returns a dictionary with item_id and q
""")

# Write your code here:




print("""
Q8. (2 points) Create a Pydantic model for a Product with:
- name: required string (min 1 char, max 100 chars)
- price: required float (must be greater than 0)
- description: optional string
- in_stock: boolean with default True
""")

# Write your code here:




print("""
Q9. (2 points) Write a POST endpoint "/users/" that:
- Accepts a User model (name: str, email: str)
- Returns a 201 status code
- Uses response_model to return UserResponse (id: int, name: str, email: str)
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain why FastAPI is considered faster than Flask.
List at least 2 technical reasons.

Your answer:
""")

# Write your explanation here as comments:
# 




# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: c) uvicorn main:app --reload
Q2: b) Pydantic
Q3: c) /docs
Q4: b) @app.post("/")
Q5: c) Returns 422 Unprocessable Entity
Q6: a) Use Optional[str] = None

Section B (Coding):

Q7:
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


Q8:
from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    description: Optional[str] = None
    in_stock: bool = True


Q9:
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return {
        "id": 1,
        "name": user.name,
        "email": user.email
    }


Section C:
Q10: FastAPI is faster than Flask because:

1. ASGI vs WSGI: FastAPI uses ASGI (Asynchronous Server Gateway Interface) 
   which supports async/await, while Flask uses WSGI (synchronous). This 
   allows FastAPI to handle multiple requests concurrently without blocking.

2. Built on Starlette: FastAPI is built on Starlette, a high-performance 
   async framework that provides very efficient request handling.

3. Native async support: FastAPI natively supports async/await, allowing 
   for non-blocking I/O operations which is crucial for I/O-bound tasks.

4. Type hints and Pydantic: FastAPI uses type hints and Pydantic for 
   validation which is implemented in Rust (via pydantic-core), making 
   validation extremely fast.

5. No reflection at runtime: FastAPI generates OpenAPI schema at startup, 
   not at runtime, reducing per-request overhead.

(Any 2 of these reasons is acceptable)
"""
