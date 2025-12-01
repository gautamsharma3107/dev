"""
MINI PROJECT: Task Management API
=================================
Build a complete REST API for task management

Features to implement:
1. User registration and authentication
2. Projects (CRUD) - belongs to user
3. Tasks (CRUD) - belongs to project
4. Task assignment - assign tasks to users

Requirements:
- FastAPI or Django REST Framework
- SQLAlchemy for database
- JWT authentication
- At least 5 unit tests
"""

# ============================================================
# PROJECT STRUCTURE
# ============================================================

project_structure = """
task_api/
├── main.py                 # Application entry point
├── config.py               # Configuration
├── database.py             # Database setup
├── models/
│   ├── __init__.py
│   ├── user.py            # User model
│   ├── project.py         # Project model
│   └── task.py            # Task model
├── schemas/
│   ├── __init__.py
│   ├── user.py            # User schemas
│   ├── project.py         # Project schemas
│   └── task.py            # Task schemas
├── routers/
│   ├── __init__.py
│   ├── auth.py            # Auth routes
│   ├── projects.py        # Project routes
│   └── tasks.py           # Task routes
├── services/
│   ├── __init__.py
│   └── auth.py            # Auth service
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_projects.py
│   └── test_tasks.py
└── requirements.txt
"""
print(project_structure)

# ============================================================
# STARTER CODE
# ============================================================

print("=" * 60)
print("STARTER CODE")
print("=" * 60)

# Database models
models_code = '''
# models/user.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    projects = relationship("Project", back_populates="owner")
    assigned_tasks = relationship("Task", back_populates="assignee")

# models/project.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")

# models/task.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

class TaskStatus(enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.TODO)
    created_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Relationships
    project = relationship("Project", back_populates="tasks")
    assignee = relationship("User", back_populates="assigned_tasks")
'''
print(models_code)

# API Endpoints to implement
print("\n" + "=" * 60)
print("ENDPOINTS TO IMPLEMENT")
print("=" * 60)

endpoints = """
Authentication:
- POST /auth/register    - Register new user
- POST /auth/login       - Login and get token
- GET  /auth/me          - Get current user

Projects:
- GET    /projects/      - List user's projects
- POST   /projects/      - Create new project
- GET    /projects/{id}  - Get project details
- PUT    /projects/{id}  - Update project
- DELETE /projects/{id}  - Delete project

Tasks:
- GET    /projects/{id}/tasks      - List tasks in project
- POST   /projects/{id}/tasks      - Create task in project
- GET    /tasks/{id}               - Get task details
- PUT    /tasks/{id}               - Update task
- DELETE /tasks/{id}               - Delete task
- PATCH  /tasks/{id}/assign        - Assign task to user
- PATCH  /tasks/{id}/status        - Update task status
"""
print(endpoints)

# Tests to write
print("\n" + "=" * 60)
print("TESTS TO WRITE")
print("=" * 60)

tests = """
Required Tests (minimum 5):
1. test_register_user - Test user registration
2. test_login_user - Test user login
3. test_create_project - Test project creation
4. test_create_task - Test task creation
5. test_assign_task - Test task assignment

Bonus Tests:
- test_get_user_projects
- test_update_task_status
- test_delete_project_cascades_tasks
- test_unauthorized_access
- test_pagination
"""
print(tests)

# Grading rubric
print("\n" + "=" * 60)
print("GRADING RUBRIC")
print("=" * 60)

rubric = """
Functionality (40 points):
- User auth working (10)
- Projects CRUD working (10)
- Tasks CRUD working (10)
- Task assignment working (5)
- Error handling (5)

Code Quality (20 points):
- Clean code structure (10)
- Proper use of Pydantic (5)
- Proper use of SQLAlchemy (5)

Best Practices (20 points):
- Separation of concerns (5)
- Input validation (5)
- Proper HTTP status codes (5)
- Security best practices (5)

Testing (10 points):
- At least 5 tests (5)
- Tests cover main flows (5)

Documentation (10 points):
- API docs accessible (5)
- README with setup instructions (5)

Total: 100 points
Pass: 70 points
"""
print(rubric)

print("\n" + "=" * 60)
print("Good luck building your Task Management API! 🚀")
print("=" * 60)
