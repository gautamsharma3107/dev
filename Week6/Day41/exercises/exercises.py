"""
Day 41 - Exercises
==================
Practice exercises for Advanced Topics:
1. GraphQL
2. Microservices
3. Message Queues
4. WebSockets
"""

# ========================================
# EXERCISE 1: GraphQL Query Builder
# ========================================
"""
Create a simple GraphQL query builder class that can:
1. Add fields to select
2. Add arguments/filters
3. Generate a valid GraphQL query string

Example usage:
    builder = GraphQLQueryBuilder("users")
    builder.add_field("id")
    builder.add_field("name")
    builder.add_field("email")
    builder.add_argument("limit", 10)
    query = builder.build()
    
Expected output:
    query {
        users(limit: 10) {
            id
            name
            email
        }
    }
"""

class GraphQLQueryBuilder:
    def __init__(self, root_field: str):
        # TODO: Initialize the builder
        pass
    
    def add_field(self, field_name: str):
        # TODO: Add a field to select
        pass
    
    def add_argument(self, name: str, value):
        # TODO: Add an argument/filter
        pass
    
    def build(self) -> str:
        # TODO: Build and return the query string
        pass


# Test your implementation:
# builder = GraphQLQueryBuilder("users")
# builder.add_field("id")
# builder.add_field("name")
# builder.add_field("email")
# builder.add_argument("limit", 10)
# builder.add_argument("status", "active")
# print(builder.build())


# ========================================
# EXERCISE 2: Service Health Checker
# ========================================
"""
Create a service health checker that:
1. Stores a list of services with their URLs
2. Checks if each service is "healthy" (simulated)
3. Returns overall system health status
4. Implements a simple retry mechanism

Requirements:
- Support adding/removing services
- Check individual service health
- Get overall system status
- Retry failed checks up to 3 times
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class HealthStatus(Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"

@dataclass
class Service:
    name: str
    url: str
    status: HealthStatus = HealthStatus.UNKNOWN

class ServiceHealthChecker:
    def __init__(self):
        # TODO: Initialize services dictionary
        pass
    
    def register_service(self, name: str, url: str):
        # TODO: Add a service to monitor
        pass
    
    def remove_service(self, name: str):
        # TODO: Remove a service
        pass
    
    def check_service(self, name: str, max_retries: int = 3) -> HealthStatus:
        # TODO: Check if a service is healthy with retries
        # Simulate health check (random success/failure)
        pass
    
    def check_all_services(self) -> Dict[str, HealthStatus]:
        # TODO: Check all registered services
        pass
    
    def get_system_status(self) -> Dict:
        # TODO: Return overall system status
        # Example: {"healthy": 3, "unhealthy": 1, "overall": "degraded"}
        pass


# Test your implementation:
# checker = ServiceHealthChecker()
# checker.register_service("user-service", "http://localhost:8001/health")
# checker.register_service("order-service", "http://localhost:8002/health")
# checker.register_service("payment-service", "http://localhost:8003/health")
# print(checker.check_all_services())
# print(checker.get_system_status())


# ========================================
# EXERCISE 3: Priority Task Queue
# ========================================
"""
Create a priority-based task queue that:
1. Accepts tasks with different priorities (1=highest, 10=lowest)
2. Processes higher priority tasks first
3. Supports task retries on failure
4. Tracks task status and history

Requirements:
- Add task with priority
- Process next task (highest priority first)
- Retry failed tasks (max 3 times)
- Get task status
- Get queue statistics
"""

from datetime import datetime
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"

class PriorityTaskQueue:
    def __init__(self):
        # TODO: Initialize task queue and tracking
        pass
    
    def add_task(self, task_id: str, task_data: dict, priority: int = 5) -> str:
        # TODO: Add task to queue with priority
        pass
    
    def get_next_task(self) -> Optional[dict]:
        # TODO: Get highest priority task
        pass
    
    def complete_task(self, task_id: str, result: any):
        # TODO: Mark task as completed
        pass
    
    def fail_task(self, task_id: str, error: str):
        # TODO: Mark task as failed, retry if possible
        pass
    
    def get_task_status(self, task_id: str) -> Optional[dict]:
        # TODO: Get current status of a task
        pass
    
    def get_statistics(self) -> dict:
        # TODO: Return queue statistics
        # Example: {"pending": 5, "completed": 10, "failed": 2}
        pass


# Test your implementation:
# queue = PriorityTaskQueue()
# queue.add_task("email-1", {"type": "email", "to": "user@example.com"}, priority=1)
# queue.add_task("report-1", {"type": "report", "user_id": 123}, priority=5)
# queue.add_task("cleanup-1", {"type": "cleanup"}, priority=10)
# 
# task = queue.get_next_task()
# print(f"Processing: {task}")
# queue.complete_task(task["task_id"], {"status": "sent"})
# print(queue.get_statistics())


# ========================================
# EXERCISE 4: Chat Room Manager
# ========================================
"""
Create a chat room manager that simulates WebSocket behavior:
1. Create and manage multiple chat rooms
2. Allow users to join/leave rooms
3. Send messages to rooms (broadcast)
4. Send private messages between users
5. Track user presence and activity

Requirements:
- Create/delete rooms
- Join/leave rooms
- Broadcast to room
- Private messaging
- User presence tracking
"""

from typing import Set

class ChatRoomManager:
    def __init__(self):
        # TODO: Initialize rooms, users, and messages storage
        pass
    
    def create_room(self, room_id: str, room_name: str) -> bool:
        # TODO: Create a new chat room
        pass
    
    def delete_room(self, room_id: str) -> bool:
        # TODO: Delete a room (notify users first)
        pass
    
    def join_room(self, room_id: str, user_id: str) -> bool:
        # TODO: User joins a room
        pass
    
    def leave_room(self, room_id: str, user_id: str) -> bool:
        # TODO: User leaves a room
        pass
    
    def broadcast_to_room(self, room_id: str, sender_id: str, message: str):
        # TODO: Send message to all users in room
        pass
    
    def send_private_message(self, from_user: str, to_user: str, message: str):
        # TODO: Send private message between users
        pass
    
    def get_room_users(self, room_id: str) -> Set[str]:
        # TODO: Get all users in a room
        pass
    
    def get_user_rooms(self, user_id: str) -> List[str]:
        # TODO: Get all rooms a user is in
        pass
    
    def get_room_history(self, room_id: str, limit: int = 50) -> List[dict]:
        # TODO: Get recent messages from a room
        pass


# Test your implementation:
# manager = ChatRoomManager()
# manager.create_room("general", "General Chat")
# manager.create_room("tech", "Tech Discussion")
# 
# manager.join_room("general", "alice")
# manager.join_room("general", "bob")
# manager.join_room("tech", "alice")
# 
# manager.broadcast_to_room("general", "alice", "Hello everyone!")
# manager.send_private_message("alice", "bob", "Hey Bob, private message!")
# 
# print(manager.get_room_users("general"))
# print(manager.get_user_rooms("alice"))
# print(manager.get_room_history("general"))


# ========================================
# EXERCISE 5: Event-Driven Architecture
# ========================================
"""
Create an event bus system that implements pub/sub pattern:
1. Subscribe to events by type
2. Publish events with data
3. Support wildcard subscriptions (e.g., "user.*")
4. Support event middleware (logging, validation)

This simulates how message queues work in microservices.
"""

from typing import Callable

class EventBus:
    def __init__(self):
        # TODO: Initialize subscribers and middleware
        pass
    
    def subscribe(self, event_type: str, handler: Callable):
        # TODO: Subscribe handler to event type
        # Support wildcards like "user.*" or "*"
        pass
    
    def unsubscribe(self, event_type: str, handler: Callable):
        # TODO: Remove handler subscription
        pass
    
    def publish(self, event_type: str, data: dict):
        # TODO: Publish event to all matching subscribers
        # Consider wildcards and middleware
        pass
    
    def add_middleware(self, middleware: Callable):
        # TODO: Add middleware that runs before handlers
        # Middleware signature: (event_type, data) -> (event_type, data) or None
        pass
    
    def get_subscribers(self, event_type: str) -> List[Callable]:
        # TODO: Get all handlers for an event type (including wildcards)
        pass


# Test your implementation:
# bus = EventBus()
# 
# # Add logging middleware
# def log_middleware(event_type, data):
#     print(f"[LOG] Event: {event_type}, Data: {data}")
#     return (event_type, data)
# bus.add_middleware(log_middleware)
# 
# # Subscribe handlers
# def on_user_created(data):
#     print(f"User created: {data['name']}")
# 
# def on_user_event(data):
#     print(f"User event received: {data}")
# 
# bus.subscribe("user.created", on_user_created)
# bus.subscribe("user.*", on_user_event)  # Wildcard
# 
# # Publish events
# bus.publish("user.created", {"name": "Alice", "email": "alice@example.com"})
# bus.publish("user.updated", {"id": 1, "name": "Alice Smith"})


print("=" * 60)
print("Day 41 Exercises")
print("=" * 60)
print("""
Complete the following exercises:

1. GraphQL Query Builder
   - Build a class to construct GraphQL queries

2. Service Health Checker
   - Monitor microservices health status

3. Priority Task Queue
   - Implement a priority-based message queue

4. Chat Room Manager
   - Simulate WebSocket chat functionality

5. Event-Driven Architecture
   - Build a pub/sub event bus

Tips:
- Start with the basic structure
- Add features incrementally
- Test each method as you implement it
- Consider edge cases

Good luck! 🚀
""")
