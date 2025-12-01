# Day 19 Quick Reference Cheat Sheet

## Async/Await Basics
```python
import asyncio

# Define async function
async def fetch_data():
    await asyncio.sleep(1)  # Non-blocking sleep
    return "Data fetched"

# Run async function
result = asyncio.run(fetch_data())

# Multiple concurrent tasks
async def main():
    tasks = [fetch_data() for _ in range(3)]
    results = await asyncio.gather(*tasks)
    return results

# Create tasks for concurrent execution
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())
    result1 = await task1
    result2 = await task2
```

## Asyncio Patterns
```python
# Async context manager
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()

# Async iterator
async for item in async_generator():
    process(item)

# Timeout handling
try:
    result = await asyncio.wait_for(fetch_data(), timeout=5.0)
except asyncio.TimeoutError:
    print("Operation timed out")
```

## Celery Basics
```python
# celery_app.py
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

# Call task asynchronously
result = add.delay(4, 4)  # Returns AsyncResult
result.get(timeout=10)    # Wait for result

# Task with retry
@app.task(bind=True, max_retries=3)
def unreliable_task(self):
    try:
        # Task logic
        pass
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
```

## Celery Commands
```bash
# Start worker
celery -A celery_app worker --loglevel=info

# Start beat (scheduler)
celery -A celery_app beat --loglevel=info

# Monitor with flower
celery -A celery_app flower
```

## WebSockets Basics
```python
# Server (FastAPI)
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")

# Client (websockets library)
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8000/ws") as ws:
        await ws.send("Hello!")
        response = await ws.recv()
        print(response)
```

## CORS Configuration
```python
# FastAPI CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Django CORS (django-cors-headers)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True

# Flask CORS
from flask_cors import CORS
CORS(app, origins=["http://localhost:3000"])
```

## Security Headers
```python
# Important security headers
headers = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=31536000",
    "Content-Security-Policy": "default-src 'self'"
}
```

## Environment Variables
```python
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get environment variable
database_url = os.getenv("DATABASE_URL")
secret_key = os.environ.get("SECRET_KEY", "default-key")

# Required variable (raises error if missing)
api_key = os.environ["API_KEY"]

# Check if variable exists
if os.getenv("DEBUG"):
    print("Debug mode enabled")
```

## .env File Format
```env
# .env file (never commit this!)
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=your-super-secret-key
DEBUG=True
API_KEY=abc123xyz
REDIS_URL=redis://localhost:6379/0
```

## Secrets Management Best Practices
```python
# Using pydantic-settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()

# Access settings
print(settings.database_url)
```

## Common Patterns
```python
# Async HTTP client
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# Async database operations
async def get_user(user_id):
    async with database.transaction():
        user = await database.fetch_one(
            "SELECT * FROM users WHERE id = :id",
            values={"id": user_id}
        )
        return user

# Background task in FastAPI
from fastapi import BackgroundTasks

@app.post("/send-email")
async def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_task, email)
    return {"message": "Email will be sent"}
```

---
**Keep this handy for Day 19 topics!** 🚀
