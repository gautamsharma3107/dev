"""
DAY 19 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 19 ASSESSMENT - Advanced Web Concepts")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What keyword is used to define an asynchronous function in Python?
a) await
b) async
c) asyncio
d) coroutine

Your answer: """)

print("""
Q2. What is the main purpose of CORS (Cross-Origin Resource Sharing)?
a) To speed up API requests
b) To allow servers to specify which origins can access their resources
c) To encrypt data between client and server
d) To cache API responses

Your answer: """)

print("""
Q3. Which of the following is TRUE about Celery?
a) It runs tasks synchronously in the main thread
b) It requires a message broker like Redis or RabbitMQ
c) It can only run scheduled tasks, not immediate tasks
d) It doesn't support task retry mechanisms

Your answer: """)

print("""
Q4. What HTTP method does the browser send for a CORS preflight request?
a) GET
b) POST
c) OPTIONS
d) HEAD

Your answer: """)

print("""
Q5. Which of the following is the correct way to load a .env file using python-dotenv?
a) dotenv.load()
b) load_dotenv()
c) env.load()
d) os.load_dotenv()

Your answer: """)

print("""
Q6. What is the key difference between HTTP and WebSockets?
a) HTTP is faster than WebSockets
b) WebSockets require more server resources
c) WebSockets maintain a persistent bidirectional connection
d) HTTP supports real-time communication better

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write an async function that fetches data from 3 different
sources concurrently and returns all results. Use asyncio.gather().
Simulate the fetch with asyncio.sleep(0.5) for each source.

Example:
async def fetch_source(name):
    # Simulate fetch
    return f"Data from {name}"

async def fetch_all():
    # Your code here - fetch from "API", "Database", "Cache"
    pass
""")

# Write your code here:
import asyncio




print("""
Q8. (2 points) Write a simple Pydantic Settings class that:
- Has a required DATABASE_URL field (str)
- Has a DEBUG field with default False (bool)
- Has a PORT field that must be between 1000 and 65535 (int)
- Loads from a .env file

from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Your code here
    pass
""")

# Write your code here:




print("""
Q9. (2 points) Write CORS configuration for FastAPI that:
- Allows origins: "http://localhost:3000" and "https://myapp.com"
- Allows credentials
- Allows all methods
- Allows headers: "Authorization" and "Content-Type"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Your code here - add CORS middleware
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain when you would use:
a) async/await vs Celery for background tasks
b) Give one use case for each

Your answer:
""")

# Write your explanation here as comments:
# 


print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) async
Q2: b) To allow servers to specify which origins can access their resources
Q3: b) It requires a message broker like Redis or RabbitMQ
Q4: c) OPTIONS
Q5: b) load_dotenv()
Q6: c) WebSockets maintain a persistent bidirectional connection

Section B:
Q7:
import asyncio

async def fetch_source(name):
    await asyncio.sleep(0.5)
    return f"Data from {name}"

async def fetch_all():
    results = await asyncio.gather(
        fetch_source("API"),
        fetch_source("Database"),
        fetch_source("Cache")
    )
    return results

# Run: asyncio.run(fetch_all())

Q8:
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    database_url: str
    debug: bool = False
    port: int = Field(default=8000, ge=1000, le=65535)
    
    class Config:
        env_file = ".env"

Q9:
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://myapp.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)

Section C:
Q10:
a) async/await:
   - Best for I/O-bound operations within the same process
   - Good for: concurrent API calls, database queries, file operations
   - Lightweight, no external dependencies
   - Use case: Fetching data from multiple APIs concurrently in a single request

b) Celery:
   - Best for long-running or CPU-intensive tasks
   - Runs tasks in separate worker processes
   - Good for: sending emails, processing images, generating reports
   - Supports scheduling and retry mechanisms
   - Use case: Sending welcome emails after user registration (don't block the response)

Key difference: 
- async/await: Concurrent operations within request lifecycle
- Celery: Offload work to background workers, outside request lifecycle
"""
