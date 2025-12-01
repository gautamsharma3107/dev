"""
Day 19 - Async/Await in Python
==============================
Learn: Asynchronous programming with asyncio

Key Concepts:
- Synchronous vs Asynchronous execution
- Event loop and coroutines
- async/await syntax
- Concurrent execution with asyncio
- Practical async patterns
"""

import asyncio
import time

# ========== SYNCHRONOUS VS ASYNCHRONOUS ==========
print("=" * 60)
print("SYNCHRONOUS VS ASYNCHRONOUS")
print("=" * 60)

# Synchronous (blocking) - executes one after another
def sync_task(name, duration):
    """Simulates a blocking task."""
    print(f"  {name}: Starting...")
    time.sleep(duration)
    print(f"  {name}: Completed after {duration}s")
    return f"{name} result"

def run_sync():
    """Run tasks synchronously."""
    start = time.time()
    sync_task("Task 1", 1)
    sync_task("Task 2", 1)
    sync_task("Task 3", 1)
    end = time.time()
    print(f"  Total time: {end - start:.2f}s")

print("\nSynchronous Execution:")
run_sync()

# Asynchronous (non-blocking) - can run concurrently
async def async_task(name, duration):
    """Simulates a non-blocking task."""
    print(f"  {name}: Starting...")
    await asyncio.sleep(duration)  # Non-blocking sleep
    print(f"  {name}: Completed after {duration}s")
    return f"{name} result"

async def run_async():
    """Run tasks asynchronously."""
    start = time.time()
    # Run all tasks concurrently
    await asyncio.gather(
        async_task("Task 1", 1),
        async_task("Task 2", 1),
        async_task("Task 3", 1)
    )
    end = time.time()
    print(f"  Total time: {end - start:.2f}s")

print("\nAsynchronous Execution:")
asyncio.run(run_async())

# ========== BASIC ASYNC/AWAIT ==========
print("\n" + "=" * 60)
print("BASIC ASYNC/AWAIT SYNTAX")
print("=" * 60)

# Define an async function (coroutine)
async def greet(name):
    """Simple async function."""
    await asyncio.sleep(0.5)  # Simulate I/O operation
    return f"Hello, {name}!"

# Run a single coroutine
async def demo_basic():
    result = await greet("Gautam")
    print(f"Result: {result}")

print("\nBasic async function:")
asyncio.run(demo_basic())

# ========== ASYNCIO.GATHER ==========
print("\n" + "=" * 60)
print("CONCURRENT EXECUTION WITH GATHER")
print("=" * 60)

async def fetch_data(source, delay):
    """Simulate fetching data from a source."""
    print(f"  Fetching from {source}...")
    await asyncio.sleep(delay)
    return f"Data from {source}"

async def fetch_all_data():
    """Fetch from multiple sources concurrently."""
    start = time.time()
    
    # gather() runs all coroutines concurrently
    results = await asyncio.gather(
        fetch_data("Database", 1),
        fetch_data("API", 1.5),
        fetch_data("Cache", 0.5)
    )
    
    end = time.time()
    print(f"\n  Results: {results}")
    print(f"  Total time: {end - start:.2f}s (not 3s!)")

print("\nFetching data concurrently:")
asyncio.run(fetch_all_data())

# ========== ASYNCIO.CREATE_TASK ==========
print("\n" + "=" * 60)
print("CREATING TASKS FOR PARALLEL EXECUTION")
print("=" * 60)

async def process_item(item):
    """Process a single item."""
    print(f"  Processing item {item}...")
    await asyncio.sleep(0.5)
    return item * 2

async def process_items():
    """Process items using tasks."""
    items = [1, 2, 3, 4, 5]
    
    # Create tasks (they start running immediately)
    tasks = [asyncio.create_task(process_item(i)) for i in items]
    
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    print(f"\n  Original: {items}")
    print(f"  Processed: {results}")

print("\nProcessing items with tasks:")
asyncio.run(process_items())

# ========== HANDLING TIMEOUTS ==========
print("\n" + "=" * 60)
print("HANDLING TIMEOUTS")
print("=" * 60)

async def slow_operation():
    """A slow operation that might timeout."""
    await asyncio.sleep(5)
    return "Completed"

async def with_timeout():
    """Execute with a timeout."""
    try:
        # Wait max 2 seconds for the operation
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Operation timed out!")

print("\nTimeout handling:")
asyncio.run(with_timeout())

# ========== ASYNC CONTEXT MANAGERS ==========
print("\n" + "=" * 60)
print("ASYNC CONTEXT MANAGERS")
print("=" * 60)

class AsyncResource:
    """Example async resource with context manager."""
    
    async def __aenter__(self):
        print("  Acquiring resource...")
        await asyncio.sleep(0.3)
        print("  Resource acquired!")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("  Releasing resource...")
        await asyncio.sleep(0.3)
        print("  Resource released!")
    
    async def do_work(self):
        """Do some work with the resource."""
        print("  Working with resource...")
        await asyncio.sleep(0.5)
        return "Work completed"

async def use_resource():
    """Use async context manager."""
    async with AsyncResource() as resource:
        result = await resource.do_work()
        print(f"  Result: {result}")

print("\nAsync context manager:")
asyncio.run(use_resource())

# ========== ASYNC ITERATORS ==========
print("\n" + "=" * 60)
print("ASYNC ITERATORS")
print("=" * 60)

async def async_range(start, end):
    """Async generator that yields numbers."""
    for i in range(start, end):
        await asyncio.sleep(0.2)
        yield i

async def use_async_iterator():
    """Iterate asynchronously."""
    print("  Numbers:", end=" ")
    async for num in async_range(1, 6):
        print(num, end=" ")
    print()

print("\nAsync iteration:")
asyncio.run(use_async_iterator())

# ========== ERROR HANDLING IN ASYNC ==========
print("\n" + "=" * 60)
print("ERROR HANDLING IN ASYNC CODE")
print("=" * 60)

async def risky_operation(should_fail):
    """Operation that might fail."""
    await asyncio.sleep(0.3)
    if should_fail:
        raise ValueError("Operation failed!")
    return "Success"

async def handle_errors():
    """Handle errors in async code."""
    # Single task error handling
    try:
        result = await risky_operation(should_fail=True)
    except ValueError as e:
        print(f"  Caught error: {e}")
    
    # Multiple tasks with return_exceptions
    results = await asyncio.gather(
        risky_operation(should_fail=False),
        risky_operation(should_fail=True),
        risky_operation(should_fail=False),
        return_exceptions=True  # Don't raise, return exceptions
    )
    
    print(f"\n  Results with return_exceptions=True:")
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"    Task {i+1}: Error - {result}")
        else:
            print(f"    Task {i+1}: {result}")

print("\nError handling:")
asyncio.run(handle_errors())

# ========== PRACTICAL EXAMPLE: ASYNC API CALLS ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: SIMULATED API CALLS")
print("=" * 60)

async def fetch_user(user_id):
    """Simulate fetching user from API."""
    await asyncio.sleep(0.5)  # Simulate network delay
    return {"id": user_id, "name": f"User{user_id}"}

async def fetch_posts(user_id):
    """Simulate fetching user's posts."""
    await asyncio.sleep(0.7)
    return [f"Post{i} by User{user_id}" for i in range(3)]

async def fetch_comments(user_id):
    """Simulate fetching user's comments."""
    await asyncio.sleep(0.4)
    return [f"Comment{i} by User{user_id}" for i in range(2)]

async def get_user_data(user_id):
    """Get all user data concurrently."""
    # Fetch all data concurrently
    user, posts, comments = await asyncio.gather(
        fetch_user(user_id),
        fetch_posts(user_id),
        fetch_comments(user_id)
    )
    
    return {
        "user": user,
        "posts": posts,
        "comments": comments
    }

async def main():
    start = time.time()
    
    # Fetch data for multiple users concurrently
    user_ids = [1, 2, 3]
    all_data = await asyncio.gather(
        *[get_user_data(uid) for uid in user_ids]
    )
    
    end = time.time()
    
    for data in all_data:
        print(f"\n  User: {data['user']['name']}")
        print(f"    Posts: {len(data['posts'])}")
        print(f"    Comments: {len(data['comments'])}")
    
    print(f"\n  Total time: {end - start:.2f}s")
    print("  (Sequential would take ~4.8s)")

print("\nFetching data for multiple users:")
asyncio.run(main())

# ========== ASYNC SEMAPHORE FOR RATE LIMITING ==========
print("\n" + "=" * 60)
print("RATE LIMITING WITH SEMAPHORE")
print("=" * 60)

async def limited_fetch(semaphore, url):
    """Fetch with rate limiting."""
    async with semaphore:  # Only N concurrent requests
        print(f"  Fetching {url}...")
        await asyncio.sleep(0.5)  # Simulate request
        print(f"  Completed {url}")
        return f"Data from {url}"

async def rate_limited_requests():
    """Make rate-limited concurrent requests."""
    # Allow max 2 concurrent requests
    semaphore = asyncio.Semaphore(2)
    
    urls = [f"url{i}" for i in range(5)]
    tasks = [limited_fetch(semaphore, url) for url in urls]
    
    start = time.time()
    results = await asyncio.gather(*tasks)
    end = time.time()
    
    print(f"\n  Fetched {len(results)} URLs in {end - start:.2f}s")
    print("  (Only 2 concurrent at a time)")

print("\nRate-limited requests:")
asyncio.run(rate_limited_requests())

# ========== WHEN TO USE ASYNC ==========
print("\n" + "=" * 60)
print("WHEN TO USE ASYNC/AWAIT")
print("=" * 60)

print("""
✅ USE ASYNC FOR:
   - Network I/O (HTTP requests, API calls)
   - Database operations
   - File I/O (reading/writing files)
   - WebSocket connections
   - Any operation waiting for external resources

❌ DON'T USE ASYNC FOR:
   - CPU-bound tasks (use multiprocessing instead)
   - Simple sequential operations
   - Code that doesn't involve waiting

📝 KEY POINTS:
   - async/await is for I/O-bound operations
   - Use asyncio.gather() for concurrent execution
   - Use asyncio.create_task() to run tasks in background
   - Use asyncio.wait_for() for timeouts
   - Use semaphores for rate limiting
   - Remember: async != parallel (it's concurrent)
""")

print("\n" + "=" * 60)
print("✅ Async/Await in Python - Complete!")
print("=" * 60)
