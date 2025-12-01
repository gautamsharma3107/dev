"""
Day 19 - Background Tasks with Celery Basics
=============================================
Learn: Distributed task queue with Celery

Key Concepts:
- What is Celery and why use it
- Celery architecture (broker, workers, backend)
- Defining and calling tasks
- Task states and results
- Basic configuration patterns

Note: Celery requires a message broker (Redis/RabbitMQ) to run.
This file shows concepts and code patterns.
"""

print("=" * 60)
print("BACKGROUND TASKS WITH CELERY BASICS")
print("=" * 60)

# ========== WHAT IS CELERY? ==========
print("\n" + "=" * 60)
print("WHAT IS CELERY?")
print("=" * 60)

print("""
Celery is a distributed task queue that allows you to:

1. RUN TASKS ASYNCHRONOUSLY
   - Don't block web requests for long operations
   - Send emails, process images, generate reports in background

2. SCHEDULE TASKS
   - Run tasks at specific times
   - Periodic tasks (every hour, daily, etc.)

3. DISTRIBUTE WORK
   - Multiple workers can process tasks
   - Scale horizontally by adding workers

ARCHITECTURE:
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Your   │────>│ Message │────>│ Celery  │
│  App    │     │ Broker  │     │ Worker  │
└─────────┘     └─────────┘     └─────────┘
                (Redis/RQ)      (Processes tasks)
""")

# ========== BASIC CELERY SETUP ==========
print("\n" + "=" * 60)
print("BASIC CELERY SETUP")
print("=" * 60)

# This is how you would set up Celery in a real project
celery_setup_code = '''
# celery_app.py - Celery configuration

from celery import Celery

# Create Celery instance with broker URL
app = Celery(
    'myproject',
    broker='redis://localhost:6379/0',      # Message broker
    backend='redis://localhost:6379/1',      # Result backend
    include=['myproject.tasks']              # Task modules
)

# Optional configuration
app.conf.update(
    result_expires=3600,           # Results expire after 1 hour
    task_serializer='json',        # Use JSON for serialization
    accept_content=['json'],       # Only accept JSON
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

if __name__ == '__main__':
    app.start()
'''

print("celery_app.py:")
print(celery_setup_code)

# ========== DEFINING TASKS ==========
print("\n" + "=" * 60)
print("DEFINING CELERY TASKS")
print("=" * 60)

task_definition_code = '''
# tasks.py - Define your tasks

from celery_app import app
import time

# Simple task
@app.task
def add(x, y):
    """Add two numbers."""
    return x + y

# Task with name
@app.task(name='emails.send')
def send_email(to, subject, body):
    """Send an email (simulated)."""
    print(f"Sending email to {to}...")
    time.sleep(2)  # Simulate sending
    return f"Email sent to {to}"

# Task with retry
@app.task(bind=True, max_retries=3)
def fetch_data(self, url):
    """Fetch data from URL with retries."""
    try:
        # Simulate API call
        import random
        if random.random() < 0.5:
            raise Exception("Connection failed")
        return f"Data from {url}"
    except Exception as exc:
        # Retry in 60 seconds
        raise self.retry(exc=exc, countdown=60)

# Task with time limit
@app.task(time_limit=30)  # Max 30 seconds
def long_task():
    """Task with time limit."""
    # Will be killed if takes > 30 seconds
    pass

# Task with ignore_result
@app.task(ignore_result=True)
def fire_and_forget():
    """Task where we don't need the result."""
    print("Doing something...")
'''

print("tasks.py:")
print(task_definition_code)

# ========== CALLING TASKS ==========
print("\n" + "=" * 60)
print("CALLING CELERY TASKS")
print("=" * 60)

calling_tasks_code = '''
from tasks import add, send_email, fetch_data

# ===== DIFFERENT WAYS TO CALL TASKS =====

# 1. Call synchronously (blocking - defeats purpose!)
result = add(4, 4)  # Returns 8 immediately

# 2. Call asynchronously with .delay() (most common)
async_result = add.delay(4, 4)
# Returns AsyncResult immediately, task runs in background

# 3. Call with .apply_async() (more options)
async_result = add.apply_async(args=[4, 4])

# With options:
async_result = send_email.apply_async(
    args=['user@example.com', 'Hello', 'Body'],
    countdown=60,        # Delay 60 seconds before executing
    expires=3600,        # Task expires in 1 hour
    retry=True,          # Retry on failure
    retry_policy={
        'max_retries': 3,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.5,
    }
)

# Schedule for specific time
from datetime import datetime, timedelta
async_result = add.apply_async(
    args=[4, 4],
    eta=datetime.now() + timedelta(hours=1)  # Run in 1 hour
)
'''

print("Calling tasks:")
print(calling_tasks_code)

# ========== WORKING WITH RESULTS ==========
print("\n" + "=" * 60)
print("WORKING WITH TASK RESULTS")
print("=" * 60)

results_code = '''
from tasks import add

# Call task asynchronously
result = add.delay(4, 4)

# Check if task is complete
print(result.ready())     # True/False

# Get task state
print(result.state)       # PENDING, STARTED, SUCCESS, FAILURE, etc.

# Wait for result (blocking)
value = result.get(timeout=10)  # Wait max 10 seconds
print(value)  # 8

# Get result without waiting (returns None if not ready)
value = result.result

# Check if successful
if result.successful():
    print(f"Result: {result.result}")

# Handle failures
if result.failed():
    print(f"Error: {result.result}")  # Exception info

# Task states:
# PENDING  - Task is waiting to be executed
# STARTED  - Task has started
# RETRY    - Task is being retried
# FAILURE  - Task raised an exception
# SUCCESS  - Task completed successfully
'''

print("Working with results:")
print(results_code)

# ========== TASK CHAINS AND GROUPS ==========
print("\n" + "=" * 60)
print("TASK CHAINS AND GROUPS")
print("=" * 60)

chains_code = '''
from celery import chain, group, chord
from tasks import add, multiply

# ===== CHAIN: Execute tasks sequentially =====
# Each task passes result to next task
result = chain(
    add.s(2, 2),      # Returns 4
    add.s(4),         # 4 + 4 = 8
    add.s(8)          # 8 + 8 = 16
)()

# Shorthand with pipe operator
result = (add.s(2, 2) | add.s(4) | add.s(8))()

# ===== GROUP: Execute tasks in parallel =====
result = group(
    add.s(2, 2),
    add.s(4, 4),
    add.s(8, 8)
)()
# result.get() returns [4, 8, 16]

# ===== CHORD: Group followed by callback =====
# All tasks in group run in parallel, then callback runs
result = chord(
    (add.s(i, i) for i in range(10)),  # Group of tasks
    add.s(10)                           # Callback: sum all + 10
)()

# ===== SIGNATURES (s and si) =====
# .s() - signature with arguments
# .si() - immutable signature (ignores previous result)

result = chain(
    add.s(2, 2),      # Uses result from previous
    add.si(5, 5)      # Ignores previous result, always 10
)()
'''

print("Task chains and groups:")
print(chains_code)

# ========== PERIODIC TASKS ==========
print("\n" + "=" * 60)
print("PERIODIC/SCHEDULED TASKS")
print("=" * 60)

periodic_code = '''
# celery_app.py - Add beat schedule

from celery import Celery
from celery.schedules import crontab

app = Celery('myproject')

# Periodic task schedule
app.conf.beat_schedule = {
    # Run every 30 seconds
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
    
    # Run every Monday morning at 7:30 AM
    'monday-morning-report': {
        'task': 'tasks.generate_report',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
    },
    
    # Run daily at midnight
    'daily-cleanup': {
        'task': 'tasks.cleanup',
        'schedule': crontab(hour=0, minute=0),
    },
    
    # Run every hour
    'hourly-check': {
        'task': 'tasks.health_check',
        'schedule': crontab(minute=0),  # Every hour at :00
    },
}

# Run celery beat:
# celery -A celery_app beat --loglevel=info
'''

print("Periodic tasks configuration:")
print(periodic_code)

# ========== REAL-WORLD EXAMPLE ==========
print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE: EMAIL SERVICE")
print("=" * 60)

real_world_code = '''
# tasks/email.py
from celery_app import app
from email_service import EmailClient
import logging

logger = logging.getLogger(__name__)

@app.task(bind=True, max_retries=3, default_retry_delay=60)
def send_welcome_email(self, user_id, email):
    """Send welcome email to new user."""
    try:
        logger.info(f"Sending welcome email to {email}")
        
        client = EmailClient()
        client.send(
            to=email,
            subject="Welcome to Our App!",
            template="welcome.html",
            context={"user_id": user_id}
        )
        
        logger.info(f"Welcome email sent to {email}")
        return {"status": "sent", "email": email}
        
    except EmailClient.ConnectionError as exc:
        logger.warning(f"Email failed, retrying: {exc}")
        raise self.retry(exc=exc)
        
    except Exception as exc:
        logger.error(f"Email failed permanently: {exc}")
        raise

@app.task
def send_bulk_emails(user_emails, subject, body):
    """Send same email to multiple users."""
    results = []
    for email in user_emails:
        result = send_single_email.delay(email, subject, body)
        results.append(result.id)
    return results

# Usage in your web app (Flask/Django/FastAPI)
# views.py
from tasks.email import send_welcome_email

def register_user(request):
    user = create_user(request.data)
    
    # Don't block - send email in background
    send_welcome_email.delay(user.id, user.email)
    
    return {"message": "User created! Welcome email coming soon."}
'''

print("Real-world email service example:")
print(real_world_code)

# ========== RUNNING CELERY ==========
print("\n" + "=" * 60)
print("RUNNING CELERY COMMANDS")
print("=" * 60)

print("""
# Start Redis (message broker)
$ redis-server

# Start Celery worker
$ celery -A celery_app worker --loglevel=info

# Start worker with specific queues
$ celery -A celery_app worker -Q emails,default --loglevel=info

# Start multiple workers (concurrency)
$ celery -A celery_app worker --concurrency=4 --loglevel=info

# Start Celery Beat (scheduler for periodic tasks)
$ celery -A celery_app beat --loglevel=info

# Start worker and beat together
$ celery -A celery_app worker --beat --loglevel=info

# Monitor with Flower (web UI)
$ pip install flower
$ celery -A celery_app flower
# Open http://localhost:5555

# Inspect active tasks
$ celery -A celery_app inspect active

# Purge all tasks
$ celery -A celery_app purge
""")

# ========== CELERY WITH FASTAPI ==========
print("\n" + "=" * 60)
print("CELERY WITH FASTAPI")
print("=" * 60)

fastapi_celery_code = '''
# main.py - FastAPI with Celery
from fastapi import FastAPI, BackgroundTasks
from celery_app import app as celery_app
from tasks import process_image, send_notification

app = FastAPI()

@app.post("/process-image/")
async def process_image_endpoint(image_url: str):
    """Process image in background."""
    task = process_image.delay(image_url)
    return {
        "task_id": task.id,
        "status": "Processing started"
    }

@app.get("/task/{task_id}")
async def get_task_status(task_id: str):
    """Check task status."""
    result = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": result.state,
        "result": result.result if result.ready() else None
    }
'''

print("FastAPI with Celery:")
print(fastapi_celery_code)

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("CELERY BEST PRACTICES")
print("=" * 60)

print("""
✅ DO:
   - Use .delay() for simple calls, .apply_async() for options
   - Set task timeouts to prevent hanging tasks
   - Use retry with exponential backoff
   - Log task progress for debugging
   - Use idempotent tasks (safe to retry)
   - Monitor with Flower or similar tools

❌ DON'T:
   - Don't pass large objects to tasks (use IDs instead)
   - Don't use database connections inside task definitions
   - Don't ignore task failures silently
   - Don't run Celery without proper monitoring

📝 ALTERNATIVES TO CELERY:
   - FastAPI BackgroundTasks (simple, no broker needed)
   - RQ (Redis Queue) - simpler than Celery
   - Dramatiq - modern alternative to Celery
   - Huey - lightweight task queue
""")

print("\n" + "=" * 60)
print("✅ Background Tasks with Celery - Complete!")
print("=" * 60)
