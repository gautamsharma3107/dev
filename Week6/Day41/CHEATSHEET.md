# Day 41 Quick Reference Cheat Sheet

## GraphQL Basics
```python
# GraphQL Query Example
query = '''
    query {
        users {
            id
            name
            email
        }
    }
'''

# GraphQL with variables
query = '''
    query GetUser($id: ID!) {
        user(id: $id) {
            name
            email
        }
    }
'''
variables = {"id": "1"}

# GraphQL Mutation
mutation = '''
    mutation CreateUser($input: UserInput!) {
        createUser(input: $input) {
            id
            name
        }
    }
'''

# Using graphene (Python GraphQL library)
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()
    
    def resolve_hello(self, info):
        return "Hello, World!"

schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
```

## GraphQL vs REST
```
REST:
- Multiple endpoints (/users, /users/1, /posts)
- Fixed data structure
- Over-fetching/under-fetching common
- Uses HTTP verbs (GET, POST, PUT, DELETE)

GraphQL:
- Single endpoint (/graphql)
- Client specifies exact data needed
- No over-fetching/under-fetching
- Uses queries/mutations
```

## Microservices Architecture
```python
# Service communication patterns

# 1. Synchronous (HTTP/REST)
import requests
response = requests.get("http://user-service/api/users/1")

# 2. Asynchronous (Message Queue)
# Producer (sends message)
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body='Hello World!'
)

# 3. Service Registry pattern
services = {
    "user-service": "http://localhost:8001",
    "order-service": "http://localhost:8002",
    "payment-service": "http://localhost:8003"
}

# 4. API Gateway pattern
class APIGateway:
    def route_request(self, path, method, data):
        service = self.get_service_for_path(path)
        return service.handle_request(method, data)
```

## Microservices Patterns
```
# Key Patterns:
1. API Gateway - Single entry point
2. Service Discovery - Dynamic service location
3. Circuit Breaker - Handle failures gracefully
4. SAGA Pattern - Distributed transactions
5. Event Sourcing - Store events, not state

# Benefits:
- Independent deployment
- Technology diversity
- Scalability per service
- Fault isolation

# Challenges:
- Network complexity
- Data consistency
- Testing difficulty
- Operational overhead
```

## Celery (Task Queue)
```python
# Install: pip install celery redis

# celery_app.py
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

@app.task
def send_email(to, subject, body):
    # Async email sending
    pass

# Using tasks
result = add.delay(4, 4)       # Async execution
result.get()                    # Wait for result

# Task with retry
@app.task(bind=True, max_retries=3)
def send_notification(self, user_id):
    try:
        # Send notification
        pass
    except Exception as e:
        self.retry(countdown=60)  # Retry after 60 seconds

# Run worker: celery -A celery_app worker --loglevel=info
```

## RabbitMQ (Message Broker)
```python
# Install: pip install pika

import pika

# Producer (Publisher)
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World!'
)
connection.close()

# Consumer (Subscriber)
def callback(ch, method, properties, body):
    print(f"Received: {body}")

channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)
channel.start_consuming()

# Exchange types
# - direct: routing key exact match
# - fanout: broadcast to all queues
# - topic: pattern matching
# - headers: header attribute matching
```

## WebSockets Basics
```python
# Install: pip install websockets

import asyncio
import websockets

# Server
async def handler(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(handler, "localhost", 8765)
)
asyncio.get_event_loop().run_forever()

# Client
async def client():
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send("Hello!")
        response = await ws.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(client())
```

## FastAPI WebSockets
```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")

# Multiple connections (chat room)
connected_clients = []

@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in connected_clients:
                await client.send_text(data)
    except:
        connected_clients.remove(websocket)
```

## WebSocket vs HTTP
```
HTTP:
- Request-Response model
- Stateless
- Client initiates
- Good for: CRUD operations

WebSocket:
- Full-duplex communication
- Persistent connection
- Bidirectional
- Good for: Real-time apps (chat, games, live updates)
```

## Common Patterns
```python
# Circuit Breaker Pattern
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failures = 0
        self.threshold = failure_threshold
        self.timeout = timeout
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def call(self, func, *args):
        if self.state == "OPEN":
            raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args)
            self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            if self.failures >= self.threshold:
                self.state = "OPEN"
            raise e

# Pub/Sub Pattern
class PubSub:
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)
    
    def publish(self, event, data):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)
```

## When to Use Each Technology
```
GraphQL:
✓ Complex nested data requirements
✓ Mobile apps with limited bandwidth
✓ Multiple client types
✗ Simple CRUD with fixed data

Microservices:
✓ Large teams, complex domains
✓ Independent scaling needed
✓ Technology diversity required
✗ Small projects, small teams

Message Queues:
✓ Async processing needed
✓ Decouple services
✓ Handle traffic spikes
✗ Real-time response required

WebSockets:
✓ Real-time updates (chat, notifications)
✓ Live data streaming
✓ Multiplayer games
✗ Simple request-response
```

---
**Keep this handy for quick reference!** 🚀
