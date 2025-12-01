"""
EXERCISES: Celery and Background Tasks
======================================
Complete all exercises below

Note: These exercises are conceptual/code writing exercises.
Running Celery requires Redis/RabbitMQ setup.
"""

# Exercise 1: Basic Task Definition
# TODO: Write a Celery task that sends an email
# The task should:
# - Take parameters: to_email, subject, body
# - Simulate sending with time.sleep(2)
# - Return a dict with status and timestamp

print("Exercise 1: Basic Task Definition")
print("-" * 40)
# Your code here:
# from celery import Celery
# import time
# from datetime import datetime




# Exercise 2: Task with Retry
# TODO: Write a Celery task that processes a payment
# The task should:
# - Have max_retries=3 and bind=True
# - Simulate a 50% failure rate
# - On failure, retry with 30 second countdown
# - Return success message or raise after max retries

print("\n\nExercise 2: Task with Retry")
print("-" * 40)
# Your code here




# Exercise 3: Task Chain
# TODO: Write pseudocode/code for a chain of tasks:
# 1. download_file(url) - downloads a file
# 2. process_file(file_path) - processes the file
# 3. upload_result(processed_data) - uploads the result
# Show how to chain these tasks

print("\n\nExercise 3: Task Chain")
print("-" * 40)
# Your code here




# Exercise 4: Periodic Task Schedule
# TODO: Write a beat_schedule configuration for:
# - Daily backup at midnight
# - Hourly health check
# - Every 5 minutes cache cleanup

print("\n\nExercise 4: Periodic Task Schedule")
print("-" * 40)
# Your code here:
# beat_schedule = {
#     ...
# }




# Exercise 5: Integration with FastAPI
# TODO: Write a FastAPI endpoint that:
# - Accepts an image URL
# - Queues a Celery task to process the image
# - Returns the task ID immediately
# Also write a status endpoint to check task status

print("\n\nExercise 5: Integration with FastAPI")
print("-" * 40)
# Your code here
