# Asynchronous Programming: Complete Guide

---

## Table of Contents
1. [Introduction to Async](#introduction-to-async)
2. [Concurrency Concepts](#concurrency-concepts)
3. [Threading](#threading)
4. [Multiprocessing](#multiprocessing)
5. [asyncio](#asyncio)
6. [Async Libraries](#async-libraries)
7. [Task Queues](#task-queues)
8. [Practical Examples](#practical-examples)
9. [Best Practices](#best-practices)
10. [Practice Exercises](#practice-exercises)

---

## Introduction to Async

### Why Asynchronous Programming?

```
Synchronous (Blocking):
- Wait for I/O (network, disk, database)
- CPU idle during wait
- Simple to understand
- One task at a time

Asynchronous (Non-blocking):
- Multiple operations concurrently
- Better resource utilization
- Higher throughput
- More complex

Use Async For:
✓ I/O-bound operations (network, file I/O)
✓ High concurrency needs
✓ Web servers
✓ Database clients
✓ API calls

Don't Use Async For:
✗ CPU-bound operations
✗ Simple scripts
✗ Offline processing
✗ When synchronous works fine
```

### Python's Concurrency Options

```
Threading:
- Lightweight threads
- Shared memory
- GIL limits true parallelism
- Good for I/O-bound tasks
- Easy synchronization

Multiprocessing:
- Multiple processes
- Separate memory
- True parallelism
- Good for CPU-bound tasks
- Complex communication

asyncio:
- Event loop
- Single-threaded
- Very lightweight
- Best for I/O-bound
- No GIL issues for I/O

Choosing:
I/O-bound + high concurrency → asyncio
I/O-bound + moderate concurrency → threading
CPU-bound → multiprocessing
Mixed → combination
```

---

## Concurrency Concepts

### Parallelism vs Concurrency

```
Concurrency:
├── Multiple tasks progress
├── May not run simultaneously
├── Context switching
└── Example: Switching between tasks
    Task A ──X── Task B ──X── Task A

Parallelism:
├── Multiple tasks run simultaneously
├── Multiple cores/CPUs
├── True simultaneous execution
└── Example: Multiple cores
    Task A (Core 1) ──→
    Task B (Core 2) ──→

Python Threading:
├── Concurrent but NOT parallel
├── GIL prevents true parallelism
├── Only one thread executes bytecode at a time
└── Good for I/O (I/O releases GIL)

Python Multiprocessing:
├── True parallelism
├── Multiple processes
├── No GIL
└── Good for CPU-bound
```

### Global Interpreter Lock (GIL)

```
What is GIL?
- Lock that allows only one thread
- Executes Python bytecode at a time
- Protects Python objects
- Built into CPython

Implications:
✗ Threading doesn't provide parallelism for CPU-bound tasks
✓ Threading works well for I/O-bound (I/O releases GIL)
✓ Multiprocessing needed for CPU-bound parallelism
✓ asyncio avoids GIL for I/O

Releasing GIL:
- I/O operations release GIL
- NumPy operations release GIL
- C extensions can release GIL
- Calling external libraries

Example:
# CPU-bound: Threading won't help
def cpu_task():
    total = 0
    for i in range(100_000_000):
        total += i
    return total

# I/O-bound: Threading helps
def io_task():
    response = requests.get('http://api.example.com')
    return response.json()
```

### When to Use Async

```
✓ Use Async When:
- High concurrency (100s-1000s of connections)
- I/O-bound operations
- Web servers/API servers
- Database-heavy applications
- Many concurrent network calls
- Real-time applications

✗ Don't Use Async When:
- CPU-bound operations (use multiprocessing)
- Simple single-threaded scripts
- Team unfamiliar with async
- Frequent blocking operations
- Everything is synchronous library

Async I/O Operations:
- HTTP requests (aiohttp)
- Database queries (asyncpg, motor)
- File I/O (aiofiles)
- WebSockets
- Database connections
```

---

## Threading

### Threading Module

```python
import threading
import time

# Create and start thread
def worker(name, duration):
    print(f"Worker {name} starting")
    time.sleep(duration)
    print(f"Worker {name} finished")

# Method 1: Instantiate Thread
thread = threading.Thread(target=worker, args=("A", 2))
thread.start()
thread.join()  # Wait for completion

# Method 2: Multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f"Worker-{i}", 1))
    threads.append(t)
    t.start()

# Wait for all
for t in threads:
    t.join()

print("All threads finished")
```

### Thread Synchronization

```python
import threading

# Lock (Mutex)
lock = threading.Lock()
shared_resource = 0

def increment():
    global shared_resource
    with lock:  # Acquire lock
        temp = shared_resource
        temp += 1
        shared_resource = temp
    # Lock released

# RLock (Reentrant Lock)
rlock = threading.RLock()

def recursive_function(n):
    with rlock:
        if n > 0:
            print(n)
            recursive_function(n - 1)

# Semaphore
semaphore = threading.Semaphore(3)  # Allow 3 concurrent

def limited_resource():
    with semaphore:
        print("Using resource")
        time.sleep(1)

# BoundedSemaphore
bounded = threading.BoundedSemaphore(5)

# Event
event = threading.Event()

def waiter():
    event.wait()  # Wait for signal
    print("Event triggered!")

def signaler():
    time.sleep(2)
    event.set()  # Signal

# Start
t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=signaler)
t1.start()
t2.start()
t1.join()
t2.join()

# Condition Variable
condition = threading.Condition()
data = []

def producer():
    with condition:
        data.append("item")
        condition.notify_all()  # Signal consumers

def consumer():
    with condition:
        condition.wait()  # Wait for notification
        if data:
            print(data.pop())
```

### Thread Pools

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return n * 2

# ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit individual tasks
    future = executor.submit(task, 5)
    result = future.result()  # Wait for result
    print(result)  # 10
    
    # Map function over iterable
    results = executor.map(task, [1, 2, 3, 4, 5])
    for result in results:
        print(result)  # 2, 4, 6, 8, 10
    
    # Submit multiple tasks
    futures = [executor.submit(task, i) for i in range(5)]
    
    # Wait for all/first
    from concurrent.futures import as_completed, wait
    
    for future in as_completed(futures):
        print(future.result())
    
    # Wait for all with timeout
    done, not_done = wait(futures, timeout=5)
    print(f"Done: {len(done)}, Not done: {len(not_done)}")
```

---

## Multiprocessing

### Process Creation

```python
from multiprocessing import Process, Queue
import os

def worker(name):
    print(f"Worker {name} in process {os.getpid()}")

# Create and start process
process = Process(target=worker, args=("Worker-1",))
process.start()
process.join()  # Wait for completion

# Multiple processes
processes = []
for i in range(4):
    p = Process(target=worker, args=(f"Worker-{i}",))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("All processes finished")
```

### Process Pools

```python
from multiprocessing import Pool
import time

def cpu_task(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Pool of processes
with Pool(processes=4) as pool:
    # Map
    results = pool.map(cpu_task, [1_000_000, 2_000_000, 3_000_000, 4_000_000])
    print(results)
    
    # Apply async
    result = pool.apply_async(cpu_task, (1_000_000,))
    print(result.get(timeout=5))
    
    # Multiple results
    async_results = [
        pool.apply_async(cpu_task, (n,))
        for n in [1_000_000, 2_000_000, 3_000_000]
    ]
    results = [r.get() for r in async_results]
```

### Inter-process Communication

```python
from multiprocessing import Process, Queue, Pipe

# Queue
queue = Queue()

def producer(q):
    q.put("message1")
    q.put("message2")

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Received: {item}")

# Start
p1 = Process(target=producer, args=(queue,))
p2 = Process(target=consumer, args=(queue,))
p1.start()
p2.start()

p1.join()
queue.put(None)  # Signal stop
p2.join()

# Pipe
conn1, conn2 = Pipe()

def sender():
    conn1.send("Hello")

def receiver():
    msg = conn2.recv()
    print(f"Received: {msg}")

p1 = Process(target=sender)
p2 = Process(target=receiver)
p1.start()
p2.start()
p1.join()
p2.join()
```

---

## asyncio

### Event Loop

```python
import asyncio

# Basic event loop
async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Run coroutine
asyncio.run(hello())

# Get running loop
async def example():
    loop = asyncio.get_running_loop()
    print(f"Running loop: {loop}")

asyncio.run(example())

# Create custom event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(hello())
loop.close()
```

### Coroutines

```python
import asyncio

# Define coroutine
async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(2)  # Simulate network delay
    print(f"Done fetching {url}")
    return {"url": url, "data": "some data"}

# Coroutine object
coro = fetch_data("http://example.com")

# Run with asyncio.run
result = asyncio.run(fetch_data("http://example.com"))
print(result)
```

### async/await Syntax

```python
import asyncio

# Basic async/await
async def function():
    await asyncio.sleep(1)
    return "Done"

# Await can only be used in async function
async def main():
    result = await function()
    print(result)

asyncio.run(main())

# Multiple awaits
async def example():
    result1 = await function()
    result2 = await function()
    return result1 + " " + result2

asyncio.run(example())
```

### Tasks

```python
import asyncio

async def task_func(name, duration):
    print(f"Task {name} starting")
    await asyncio.sleep(duration)
    print(f"Task {name} finished")
    return f"Result {name}"

async def main():
    # Create tasks
    task1 = asyncio.create_task(task_func("A", 2))
    task2 = asyncio.create_task(task_func("B", 1))
    
    # Wait for specific tasks
    result1 = await task1
    result2 = await task2
    print(result1, result2)

asyncio.run(main())

# Check if done
task = asyncio.create_task(task_func("C", 1))
print(task.done())  # False
asyncio.run(asyncio.sleep(2))
print(task.done())  # True

# Cancel task
task = asyncio.create_task(task_func("D", 10))
await asyncio.sleep(2)
task.cancel()
```

### gather() and wait()

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    # gather: Run concurrently, return results in order
    results = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3"),
        return_exceptions=False
    )
    print(results)
    
    # wait: More control over completion
    tasks = [
        asyncio.create_task(fetch("url1")),
        asyncio.create_task(fetch("url2")),
        asyncio.create_task(fetch("url3"))
    ]
    
    # Wait for all
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    for task in done:
        print(task.result())
    
    # Wait for first
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()

asyncio.run(main())
```

---

## Async Libraries

### aiohttp (Async HTTP)

```bash
pip install aiohttp
```

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        # Single request
        data = await fetch(session, "http://api.example.com/users")
        print(data)
        
        # Multiple concurrent requests
        urls = [
            "http://api.example.com/users/1",
            "http://api.example.com/users/2",
            "http://api.example.com/users/3"
        ]
        
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())
```

### asyncpg (Async PostgreSQL)

```bash
pip install asyncpg
```

```python
import asyncpg
import asyncio

async def main():
    # Create connection
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='database',
        host='localhost'
    )
    
    try:
        # Query
        rows = await conn.fetch('SELECT * FROM users')
        print(rows)
        
        # Single row
        row = await conn.fetchrow('SELECT * FROM users WHERE id = $1', 1)
        print(row)
        
        # Insert
        await conn.execute('INSERT INTO users (name, email) VALUES ($1, $2)',
                          'Alice', 'alice@example.com')
        
        # Transaction
        async with conn.transaction():
            await conn.execute('UPDATE users SET name = $1 WHERE id = $2',
                              'Alice Updated', 1)
        
        # Connection pool
        pool = await asyncpg.create_pool(
            user='user',
            password='password',
            database='database',
            host='localhost',
            min_size=10,
            max_size=10
        )
        
        # Use pool
        async with pool.acquire() as conn:
            rows = await conn.fetch('SELECT * FROM users')
            print(rows)
        
        await pool.close()
    
    finally:
        await conn.close()

asyncio.run(main())
```

### motor (Async MongoDB)

```bash
pip install motor
```

```python
import motor.motor_asyncio
import asyncio

async def main():
    # Create client
    client = motor.motor_asyncio.AsyncMongoClient('mongodb://localhost:27017')
    db = client['mydatabase']
    collection = db['users']
    
    # Insert
    result = await collection.insert_one({'name': 'Alice', 'age': 25})
    print(result.inserted_id)
    
    # Find
    user = await collection.find_one({'name': 'Alice'})
    print(user)
    
    # Find many
    async for user in collection.find({'age': {'$gt': 20}}):
        print(user)
    
    # Update
    result = await collection.update_one(
        {'name': 'Alice'},
        {'$set': {'age': 26}}
    )
    
    # Delete
    result = await collection.delete_one({'name': 'Alice'})
    
    client.close()

asyncio.run(main())
```

---

## Task Queues

### Celery Basics

```bash
pip install celery redis
```

```python
from celery import Celery

# Create Celery app
app = Celery('myapp', broker='redis://localhost:6379/0')

# Configure
app.conf.update(
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

# Define tasks
@app.task
def add(x, y):
    return x + y

@app.task
def multiply(x, y):
    return x * y

# Call task
result = add.delay(4, 6)
print(result.get())  # 10

# Task with options
result = add.apply_async((4, 6), countdown=5)  # Run after 5 seconds
result = add.apply_async((4, 6), expires=60)  # Expires in 60 seconds

# Check status
task_id = result.id
status = result.status
print(status)  # PENDING, SUCCESS, FAILURE

# Get result
result_value = result.get(timeout=10)
```

### Task Definition

```python
from celery import Celery, Task
import time

app = Celery('tasks', broker='redis://localhost:6379/0')

# Basic task
@app.task
def simple_task():
    return "Done"

# Task with parameters
@app.task
def task_with_params(name, age):
    return f"{name} is {age} years old"

# Task with retry
@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3})
def task_with_retry(self):
    try:
        # Risky operation
        result = risky_operation()
        return result
    except Exception as exc:
        raise self.retry(exc=exc)

# Long-running task
@app.task
def long_task():
    for i in range(10):
        print(f"Step {i}")
        time.sleep(1)
    return "Completed"

# Task with error handling
@app.task
def task_with_error_handling():
    try:
        result = some_operation()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None
```

### Workers and Brokers

```bash
# Start worker
celery -A myapp worker --loglevel=info

# Multiple workers
celery -A myapp worker --concurrency=4

# Worker with specific queue
celery -A myapp worker -Q high_priority

# Monitor tasks
celery -A myapp events
```

```python
# RabbitMQ broker
app = Celery('myapp', broker='amqp://guest:guest@localhost:5672//')

# Redis broker
app = Celery('myapp', broker='redis://localhost:6379/0')

# SQS broker
app = Celery('myapp', broker='sqs://AWS_ACCESS_KEY_ID:AWS_SECRET_ACCESS_KEY@')
```

### Periodic Tasks

```python
from celery.schedules import crontab
from celery import Celery

app = Celery('myapp', broker='redis://localhost:6379/0')

# Configure periodic tasks
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
    'every-morning': {
        'task': 'tasks.send_email',
        'schedule': crontab(hour=7, minute=30),
    },
    'every-monday': {
        'task': 'tasks.weekly_report',
        'schedule': crontab(day_of_week=1, hour=0, minute=0),
    },
}

# Start Celery beat scheduler
# celery -A myapp beat --loglevel=info

# Or with worker
# celery -A myapp worker --beat --loglevel=info
```

### Task Monitoring

```python
from celery import Celery
from celery.result import AsyncResult

app = Celery('myapp', broker='redis://localhost:6379/0')

# Check task status
def check_task_status(task_id):
    result = AsyncResult(task_id, app=app)
    return {
        'task_id': task_id,
        'status': result.status,
        'result': result.result if result.ready() else None
    }

# Revoke task
def revoke_task(task_id):
    app.control.revoke(task_id, terminate=True)

# Get active tasks
def get_active_tasks():
    return app.control.inspect().active()

# Get registered tasks
def get_registered_tasks():
    return app.control.inspect().registered()

# Get stats
def get_stats():
    return app.control.inspect().stats()
```

---

## Practical Examples

### Concurrent Web Scraper

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h1')
    return [title.text for title in titles]

async def scrape_sites(urls):
    async with aiohttp.ClientSession() as session:
        # Fetch all concurrently
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        # Parse all
        parsed = []
        for html in results:
            titles = await parse_page(html)
            parsed.append(titles)
        
        return parsed

# Usage
urls = [
    'http://example.com/page1',
    'http://example.com/page2',
    'http://example.com/page3',
]

results = asyncio.run(scrape_sites(urls))
print(results)
```

### Async Database Operations

```python
import asyncpg
import asyncio

async def batch_insert_users(users):
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='database',
        host='localhost'
    )
    
    try:
        # Batch insert
        async with conn.transaction():
            await conn.executemany(
                'INSERT INTO users (name, email) VALUES ($1, $2)',
                users
            )
    finally:
        await conn.close()

async def main():
    users = [
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com'),
        ('Charlie', 'charlie@example.com'),
    ]
    
    await batch_insert_users(users)

asyncio.run(main())
```

### Task Queue Application

```python
from celery import Celery
from celery.result import AsyncResult

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Tasks
@app.task
def send_email(to_email, subject, body):
    # Simulate email sending
    import time
    time.sleep(2)
    return f"Email sent to {to_email}"

@app.task
def generate_report(user_id):
    # Simulate report generation
    import time
    time.sleep(5)
    return f"Report generated for user {user_id}"

@app.task
def process_image(image_path):
    # Simulate image processing
    import time
    time.sleep(3)
    return f"Image processed: {image_path}"

# Application code
def send_email_async(to_email, subject, body):
    result = send_email.delay(to_email, subject, body)
    return result.id

def get_task_result(task_id):
    result = AsyncResult(task_id, app=app)
    if result.ready():
        return {
            'status': 'completed',
            'result': result.result
        }
    else:
        return {
            'status': result.status,
            'result': None
        }
```

---

## Best Practices

### Async

```
✓ Use for I/O-bound operations
✓ Keep async functions pure
✓ Avoid blocking operations
✓ Use proper error handling
✓ Don't mix sync and async carelessly
✓ Use context managers
✓ Cancel tasks properly
✓ Monitor task status
```

### Threading

```
✓ Use for I/O-bound
✓ Use ThreadPoolExecutor
✓ Proper synchronization
✓ Avoid shared state
✓ Use locks correctly
✓ Avoid deadlocks
```

### Multiprocessing

```
✓ Use for CPU-bound
✓ Use Process pools
✓ Pickle-able objects
✓ Proper IPC
✓ Resource limits
```

### Task Queues

```
✓ For long-running tasks
✓ For background jobs
✓ For scheduled tasks
✓ Proper monitoring
✓ Error handling and retry
✓ Result cleanup
```

---

## Practice Exercises

### 1. Basic Async
- Create async functions
- Use await properly
- Run with asyncio.run()

### 2. Concurrent Operations
- gather() and wait()
- Multiple tasks
- Error handling

### 3. Async Libraries
- aiohttp requests
- Database operations
- Concurrent I/O

### 4. Threading
- Create threads
- Synchronization
- ThreadPoolExecutor

### 5. Multiprocessing
- Create processes
- Process pools
- IPC

### 6. Task Queues
- Celery tasks
- Workers
- Monitoring

---

# End of Notes
