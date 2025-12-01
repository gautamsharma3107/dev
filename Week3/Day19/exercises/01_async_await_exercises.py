"""
EXERCISES: Async/Await
======================
Complete all 5 exercises below
"""

import asyncio

# Exercise 1: Basic Async Function
# TODO: Create an async function that takes a name and delay
# It should wait for the delay (using asyncio.sleep) and return a greeting
# Example: greet("Alice", 1) -> "Hello, Alice!" (after 1 second)

print("Exercise 1: Basic Async Function")
print("-" * 40)
# Your code here




# Exercise 2: Concurrent Fetching
# TODO: Create 3 async functions that simulate fetching from different sources
# - fetch_users() - takes 1 second, returns ["user1", "user2"]
# - fetch_products() - takes 1.5 seconds, returns ["product1", "product2"]
# - fetch_orders() - takes 0.5 seconds, returns ["order1", "order2"]
# Then create a main function that fetches all concurrently using asyncio.gather

print("\n\nExercise 2: Concurrent Fetching")
print("-" * 40)
# Your code here




# Exercise 3: Timeout Handling
# TODO: Create an async function that might take too long
# Use asyncio.wait_for to add a timeout of 2 seconds
# If it times out, catch the exception and return "Timeout!"

print("\n\nExercise 3: Timeout Handling")
print("-" * 40)
# Your code here




# Exercise 4: Rate-Limited Requests
# TODO: Create a function that simulates making API requests
# Use asyncio.Semaphore to limit concurrent requests to 3
# Process 10 total requests

print("\n\nExercise 4: Rate-Limited Requests")
print("-" * 40)
# Your code here




# Exercise 5: Async Generator
# TODO: Create an async generator that yields numbers 1-5
# with a 0.3 second delay between each
# Then consume it using async for

print("\n\nExercise 5: Async Generator")
print("-" * 40)
# Your code here
