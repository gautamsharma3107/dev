"""
DAY 21 ASSESSMENT TEST - COMPREHENSIVE WEEK 3 REVIEW
=====================================================
Total: 14 points
Pass: 10+ points (70%)
Time: 20 minutes

Topics Covered:
- Django REST Framework
- FastAPI
- API Authentication
- Database Relationships
- Testing APIs

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 21 ASSESSMENT - Week 3 Comprehensive Review")
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
Q1. In FastAPI, which decorator is used to create a POST endpoint?
a) @app.post()
b) @app.create()
c) @app.route("POST")
d) @post.app()

Your answer: """)

print("""
Q2. What HTTP status code should be returned when a resource is successfully created?
a) 200 OK
b) 201 Created
c) 204 No Content
d) 202 Accepted

Your answer: """)

print("""
Q3. In JWT authentication, where should the token typically be included in requests?
a) In the URL parameters
b) In the request body
c) In the Authorization header
d) In cookies only

Your answer: """)

print("""
Q4. What is the purpose of Pydantic models in FastAPI?
a) Database ORM
b) Request/Response validation and serialization
c) Authentication only
d) Routing configuration

Your answer: """)

print("""
Q5. In SQLAlchemy, which function creates a Many-to-Many relationship?
a) ForeignKey()
b) relationship() with secondary parameter
c) Column(ManyToMany)
d) join()

Your answer: """)

print("""
Q6. What is the correct way to test FastAPI endpoints?
a) Using unittest only
b) Using FastAPI's TestClient
c) Using Django's test client
d) Only manual testing

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a FastAPI endpoint that creates a new user.
The endpoint should:
- Accept POST requests at "/users/"
- Take a username and email in the request body
- Return the created user with a 201 status code
""")

# Write your code here:
print("# Your code:")
print("""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: Define UserCreate schema and create_user endpoint

""")


print("""
Q8. (2 points) Write a test function using pytest and TestClient to test the GET /items/ endpoint.
The test should verify:
- Status code is 200
- Response is a list
""")

# Write your code here:
print("# Your code:")
print("""
from fastapi.testclient import TestClient
import pytest

# TODO: Write test_get_items function

""")


print("""
Q9. (2 points) Write SQLAlchemy models for a One-to-Many relationship:
- User model with id and username
- Post model with id, title, and author_id (foreign key to User)
- Include the relationship on both sides
""")

# Write your code here:
print("# Your code:")
print("""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# TODO: Define User and Post models with One-to-Many relationship

""")


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between Token-based authentication 
and Session-based authentication. What are the advantages of using JWT tokens 
for API authentication?

Your answer:
""")

# Write your explanation here as comments:
# 


# ============================================================
# WEEK 3 MINI-PROJECT REQUIREMENTS
# ============================================================

print("\n" + "=" * 60)
print("WEEK 3 MINI-PROJECT REQUIREMENTS")
print("=" * 60)

print("""
Build a Full-Featured REST API with the following requirements:

MINIMUM REQUIREMENTS (70 points to pass):
-----------------------------------------
1. Core Features (40 points):
   - [ ] User registration endpoint
   - [ ] User login with JWT token
   - [ ] At least one protected resource with CRUD operations
   - [ ] Proper error handling (404, 400, 401, etc.)

2. Database (20 points):
   - [ ] At least 2 models with a relationship
   - [ ] Proper database migrations
   - [ ] Data validation

3. Testing (10 points):
   - [ ] At least 5 unit tests
   - [ ] Tests for both success and error cases

4. Documentation (10 points):
   - [ ] API documentation (Swagger/ReDoc)
   - [ ] README with setup instructions

BONUS FEATURES (+30 points):
----------------------------
- [ ] Role-based access control (+10)
- [ ] Pagination for list endpoints (+5)
- [ ] Search/filter functionality (+5)
- [ ] Many-to-Many relationship (+5)
- [ ] Docker containerization (+5)

PROJECT IDEAS:
--------------
1. Task Management API - Users, Projects, Tasks
2. Blog API - Users, Posts, Comments, Tags
3. E-commerce API - Products, Categories, Orders
4. Library API - Books, Authors, Members, Borrowings
""")


# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Scoring:
- Section A: 6 points (1 point each)
- Section B: 6 points (2 points each)
- Section C: 2 points
- Total: 14 points

Remember:
- Review topics you got wrong
- Complete the mini-project
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: a) @app.post()
Q2: b) 201 Created
Q3: c) In the Authorization header
Q4: b) Request/Response validation and serialization
Q5: b) relationship() with secondary parameter
Q6: b) Using FastAPI's TestClient

Section B (Coding):
Q7: FastAPI user creation endpoint
```python
from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

users_db = {}
user_counter = 0

@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    global user_counter
    user_counter += 1
    new_user = {"id": user_counter, **user.dict()}
    users_db[user_counter] = new_user
    return new_user
```

Q8: Test function for GET /items/
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

Q9: SQLAlchemy One-to-Many models
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    
    author = relationship("User", back_populates="posts")
```

Section C:
Q10: Token vs Session Authentication

Token-based (JWT):
- Stateless: Server doesn't store session data
- Token contains user info, signed by server
- Client stores token (localStorage, etc.)
- Token sent with each request in header
- Scalable: Works across multiple servers

Session-based:
- Stateful: Server stores session data
- Session ID stored in cookie
- Server looks up session on each request
- Requires session storage (Redis, DB)
- Harder to scale horizontally

JWT Advantages:
1. Stateless - No server-side session storage
2. Scalable - Works with load balancers easily
3. Cross-domain - Works with multiple services
4. Mobile-friendly - No cookies needed
5. Self-contained - Contains user claims/permissions
"""
