"""
Day 21 - FastAPI Project Setup
==============================
Learn: Project structure, configuration, and setup

Key Concepts:
- FastAPI application setup
- Project organization
- Configuration management
- Database setup with SQLAlchemy
"""

# ========== FASTAPI BASICS ==========
print("=" * 60)
print("FASTAPI PROJECT SETUP")
print("=" * 60)

# Installation (run in terminal):
# pip install fastapi uvicorn sqlalchemy pydantic python-jose passlib bcrypt

# ========== BASIC APP STRUCTURE ==========
print("\n1. BASIC APPLICATION STRUCTURE")
print("-" * 40)

example_code = """
# main.py - Entry point
from fastapi import FastAPI
from routers import users, posts
from database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Full-Featured API",
    description="A complete REST API with CRUD, Auth, and Tests",
    version="1.0.0"
)

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
"""
print(example_code)

# ========== PROJECT STRUCTURE ==========
print("\n2. RECOMMENDED PROJECT STRUCTURE")
print("-" * 40)

project_structure = """
my_api/
├── main.py              # Application entry point
├── config.py            # Configuration settings
├── database.py          # Database connection
├── models/              # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py
│   └── post.py
├── schemas/             # Pydantic schemas
│   ├── __init__.py
│   ├── user.py
│   └── post.py
├── routers/             # API routes
│   ├── __init__.py
│   ├── users.py
│   └── posts.py
├── services/            # Business logic
│   ├── __init__.py
│   └── auth.py
├── tests/               # Test files
│   ├── __init__.py
│   ├── test_users.py
│   └── test_posts.py
├── requirements.txt     # Dependencies
└── README.md           # Documentation
"""
print(project_structure)

# ========== DATABASE SETUP ==========
print("\n3. DATABASE SETUP (database.py)")
print("-" * 40)

database_code = '''
# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite for development
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# PostgreSQL for production
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Only for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''
print(database_code)

# ========== CONFIGURATION ==========
print("\n4. CONFIGURATION (config.py)")
print("-" * 40)

config_code = '''
# config.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Full-Featured API"
    debug: bool = True
    database_url: str = "sqlite:///./app.db"
    secret_key: str = "your-super-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
'''
print(config_code)

# ========== ENVIRONMENT VARIABLES ==========
print("\n5. ENVIRONMENT VARIABLES (.env)")
print("-" * 40)

env_file = """
# .env file (DO NOT commit to git!)
DEBUG=true
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
"""
print(env_file)

# ========== RUNNING THE APPLICATION ==========
print("\n6. RUNNING THE APPLICATION")
print("-" * 40)

run_commands = """
# Development (with auto-reload)
uvicorn main:app --reload

# Production
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Access API documentation
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
"""
print(run_commands)

# ========== DEPENDENCIES (requirements.txt) ==========
print("\n7. DEPENDENCIES (requirements.txt)")
print("-" * 40)

requirements = """
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.2
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
pytest==7.4.3
httpx==0.25.2
"""
print(requirements)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Minimal Working API")
print("=" * 60)

minimal_example = '''
# Save this as main.py and run: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API", version="1.0.0")

# In-memory database
tasks = {}
task_counter = 0

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Task(TaskCreate):
    id: int

@app.get("/")
def root():
    return {"message": "Task API - Go to /docs for documentation"}

@app.get("/tasks")
def get_tasks():
    return list(tasks.values())

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global task_counter
    task_counter += 1
    new_task = Task(id=task_counter, **task.dict())
    tasks[task_counter] = new_task
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted"}
'''
print(minimal_example)

print("\n" + "=" * 60)
print("✅ FastAPI Project Setup - Complete!")
print("=" * 60)
print("\nNext: Learn about CRUD operations in 02_crud_operations.py")
