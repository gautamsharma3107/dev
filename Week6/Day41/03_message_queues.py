"""
Day 41 - Message Queues (Celery & RabbitMQ)
===========================================
Learn: Asynchronous task processing, message brokers, and event-driven architecture

Key Concepts:
- Message queues for async processing
- Celery for task queues in Python
- RabbitMQ as message broker
- Producer-Consumer pattern
"""

# ========== MESSAGE QUEUES OVERVIEW ==========
print("=" * 60)
print("MESSAGE QUEUES BASICS")
print("=" * 60)

"""
What is a Message Queue?
- System for async communication between services
- Producer sends messages to queue
- Consumer processes messages from queue
- Decouples sender and receiver

Benefits:
- Async processing (don't wait for slow tasks)
- Load balancing (distribute work)
- Reliability (messages persist if consumer is down)
- Scalability (add more consumers)

Common Use Cases:
- Email sending
- Image processing
- Report generation
- Data synchronization
- Notification delivery
"""

# ========== SIMPLE QUEUE IMPLEMENTATION ==========
print("\n" + "=" * 60)
print("SIMPLE QUEUE IMPLEMENTATION")
print("=" * 60)

import queue
import threading
import time
from typing import Callable, Any, Dict, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Message:
    id: str
    body: Any
    timestamp: datetime
    retry_count: int = 0

class SimpleMessageQueue:
    """
    Basic message queue implementation for learning.
    In production, use RabbitMQ, Redis, or similar.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.queue = queue.Queue()
        self.message_count = 0
    
    def publish(self, message: Any) -> str:
        """Add message to queue"""
        self.message_count += 1
        msg_id = f"msg-{self.message_count}"
        msg = Message(
            id=msg_id,
            body=message,
            timestamp=datetime.now()
        )
        self.queue.put(msg)
        print(f"📤 Published: {msg.body} (ID: {msg_id})")
        return msg_id
    
    def consume(self, timeout: float = 1.0) -> Message:
        """Get message from queue"""
        try:
            msg = self.queue.get(timeout=timeout)
            print(f"📥 Consumed: {msg.body} (ID: {msg.id})")
            return msg
        except queue.Empty:
            return None
    
    def size(self) -> int:
        return self.queue.qsize()

# Demonstrate basic queue
print("\n--- Basic Queue Demo ---")
mq = SimpleMessageQueue("demo-queue")

# Publish messages
mq.publish({"task": "send_email", "to": "user@example.com"})
mq.publish({"task": "process_image", "file": "photo.jpg"})
mq.publish({"task": "generate_report", "user_id": 123})

print(f"\nQueue size: {mq.size()}")

# Consume messages
print("\nConsuming messages:")
while mq.size() > 0:
    msg = mq.consume()
    # Process message here

# ========== PRODUCER-CONSUMER PATTERN ==========
print("\n" + "=" * 60)
print("PRODUCER-CONSUMER PATTERN")
print("=" * 60)

class TaskQueue:
    """Enhanced queue with worker threads"""
    
    def __init__(self, num_workers: int = 2):
        self.queue = queue.Queue()
        self.workers: List[threading.Thread] = []
        self.running = False
        self.num_workers = num_workers
        self.results: Dict[str, Any] = {}
    
    def start_workers(self):
        """Start worker threads"""
        self.running = True
        for i in range(self.num_workers):
            worker = threading.Thread(target=self._worker, args=(i,))
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
        print(f"Started {self.num_workers} workers")
    
    def stop_workers(self):
        """Stop all workers"""
        self.running = False
        # Add None to signal workers to stop
        for _ in self.workers:
            self.queue.put(None)
    
    def _worker(self, worker_id: int):
        """Worker thread that processes tasks"""
        while self.running:
            try:
                task = self.queue.get(timeout=0.5)
                if task is None:
                    break
                
                task_id, func, args = task
                print(f"Worker {worker_id}: Processing task {task_id}")
                
                try:
                    result = func(*args)
                    self.results[task_id] = {"status": "success", "result": result}
                except Exception as e:
                    self.results[task_id] = {"status": "error", "error": str(e)}
                
                self.queue.task_done()
            except queue.Empty:
                continue
    
    def submit(self, task_id: str, func: Callable, *args):
        """Submit a task to the queue"""
        self.queue.put((task_id, func, args))
        print(f"Submitted task: {task_id}")
    
    def wait_completion(self):
        """Wait for all tasks to complete"""
        self.queue.join()

# Task functions
def send_email(to: str, subject: str):
    time.sleep(0.3)  # Simulate sending email
    return f"Email sent to {to}"

def process_image(filename: str):
    time.sleep(0.5)  # Simulate processing
    return f"Processed {filename}"

def generate_report(user_id: int):
    time.sleep(0.4)  # Simulate report generation
    return f"Report generated for user {user_id}"

# Demonstrate producer-consumer
print("\n--- Producer-Consumer Demo ---")
task_queue = TaskQueue(num_workers=3)
task_queue.start_workers()

# Submit tasks (producer)
task_queue.submit("email-1", send_email, "alice@example.com", "Welcome!")
task_queue.submit("image-1", process_image, "photo.jpg")
task_queue.submit("report-1", generate_report, 42)
task_queue.submit("email-2", send_email, "bob@example.com", "Newsletter")

# Wait for completion
task_queue.wait_completion()
time.sleep(0.5)  # Allow workers to finish

print("\nResults:")
for task_id, result in task_queue.results.items():
    print(f"  {task_id}: {result}")

task_queue.stop_workers()

# ========== CELERY CONCEPTS ==========
print("\n" + "=" * 60)
print("CELERY TASK QUEUE")
print("=" * 60)

print("""
Celery is a distributed task queue for Python.

Installation:
    pip install celery redis

Key Components:
1. Celery App - Main application configuration
2. Tasks - Functions decorated with @app.task
3. Broker - Message transport (Redis, RabbitMQ)
4. Worker - Process that executes tasks
5. Backend - Stores task results (optional)

Architecture:
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Client │ -> │  Broker │ -> │ Worker  │ -> │ Backend │
│  (app)  │    │ (Redis) │    │(celery) │    │ (Redis) │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
""")

# Celery configuration example
celery_config = '''
# celery_app.py - Celery Application Setup
from celery import Celery

# Create Celery app with Redis as broker
app = Celery(
    'myapp',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
    include=['myapp.tasks']  # Module with task definitions
)

# Optional configuration
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    worker_prefetch_multiplier=1,
    task_acks_late=True,
)
'''
print("Celery App Configuration:")
print(celery_config)

# Task examples
celery_tasks = '''
# tasks.py - Celery Task Definitions
from celery_app import app
from celery import shared_task
import time

# Basic task
@app.task
def add(x, y):
    return x + y

# Task with retry
@app.task(bind=True, max_retries=3, default_retry_delay=60)
def send_email(self, to, subject, body):
    try:
        # Send email logic here
        print(f"Sending email to {to}")
        return {"status": "sent", "to": to}
    except Exception as e:
        # Retry on failure
        self.retry(exc=e)

# Task with progress updates
@app.task(bind=True)
def long_running_task(self, items):
    total = len(items)
    for i, item in enumerate(items):
        # Process item
        process_item(item)
        
        # Update progress
        self.update_state(
            state='PROGRESS',
            meta={'current': i + 1, 'total': total}
        )
    
    return {'status': 'complete', 'processed': total}

# Periodic task (needs celery beat)
@app.task
def cleanup_old_data():
    """Run daily to clean up old data"""
    delete_old_records()
    return {"cleaned": True}
'''
print("\nCelery Task Definitions:")
print(celery_tasks)

# Using tasks
celery_usage = '''
# Using Celery Tasks

# Async execution (returns immediately)
result = add.delay(4, 4)  # or add.apply_async((4, 4))

# Get result (blocks until complete)
value = result.get(timeout=10)  # Returns 8

# Check task status
result.ready()      # True if complete
result.successful() # True if succeeded
result.failed()     # True if failed
result.status       # 'PENDING', 'STARTED', 'SUCCESS', 'FAILURE'

# Task with options
result = send_email.apply_async(
    args=('user@example.com', 'Hello', 'Body'),
    countdown=60,           # Execute after 60 seconds
    expires=3600,           # Task expires after 1 hour
    retry=True,             # Retry on failure
    retry_policy={
        'max_retries': 3,
        'interval_start': 0,
        'interval_step': 0.2,
        'interval_max': 0.5,
    }
)

# Chain tasks (execute sequentially)
from celery import chain
result = chain(add.s(2, 2), add.s(4), add.s(8))()
# (2+2) -> (4+4) -> (8+8) = 16

# Group tasks (execute in parallel)
from celery import group
result = group(add.s(2, 2), add.s(4, 4))()
# Returns [4, 8]

# Chord (group + callback)
from celery import chord
result = chord([add.s(2, 2), add.s(4, 4)], add.s())()
# sum of [4, 8] = 12
'''
print("\nUsing Celery Tasks:")
print(celery_usage)

# ========== RABBITMQ CONCEPTS ==========
print("\n" + "=" * 60)
print("RABBITMQ MESSAGE BROKER")
print("=" * 60)

print("""
RabbitMQ is a popular message broker.

Key Concepts:
1. Producer - Sends messages
2. Exchange - Routes messages to queues
3. Queue - Stores messages
4. Consumer - Receives messages
5. Binding - Links exchange to queue

Exchange Types:
- Direct: Exact routing key match
- Fanout: Broadcast to all queues
- Topic: Pattern matching (*.log, orders.#)
- Headers: Header attribute matching

Installation:
    pip install pika

Docker:
    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
""")

# RabbitMQ examples
rabbitmq_producer = '''
# producer.py - RabbitMQ Producer
import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

# Declare queue (creates if doesn't exist)
channel.queue_declare(queue='task_queue', durable=True)

# Publish message
message = {"task": "process_order", "order_id": 123}
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=json.dumps(message),
    properties=pika.BasicProperties(
        delivery_mode=2,  # Make message persistent
        content_type='application/json'
    )
)

print(f" [x] Sent: {message}")
connection.close()
'''
print("RabbitMQ Producer:")
print(rabbitmq_producer)

rabbitmq_consumer = '''
# consumer.py - RabbitMQ Consumer
import pika
import json

def callback(ch, method, properties, body):
    """Process received message"""
    message = json.loads(body)
    print(f" [x] Received: {message}")
    
    # Process the message
    process_task(message)
    
    # Acknowledge message (remove from queue)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='task_queue', durable=True)

# Fair dispatch - don't give more messages until previous is done
channel.basic_qos(prefetch_count=1)

# Start consuming
channel.basic_consume(
    queue='task_queue',
    on_message_callback=callback
)

print(' [*] Waiting for messages. Press CTRL+C to exit')
channel.start_consuming()
'''
print("\nRabbitMQ Consumer:")
print(rabbitmq_consumer)

# Exchange example
exchange_example = '''
# Using Exchanges for Pub/Sub

# Publisher
channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.basic_publish(
    exchange='logs',
    routing_key='',  # Ignored for fanout
    body='Log message here'
)

# Subscriber 1 (creates own queue)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)
channel.basic_consume(queue=queue_name, on_message_callback=callback)

# Topic Exchange (pattern matching)
channel.exchange_declare(exchange='events', exchange_type='topic')

# Publish with routing key
channel.basic_publish(
    exchange='events',
    routing_key='order.created',  # or 'user.updated', etc.
    body=message
)

# Subscribe to specific patterns
channel.queue_bind(exchange='events', queue=queue_name, routing_key='order.*')
channel.queue_bind(exchange='events', queue=queue_name, routing_key='*.created')
'''
print("\nRabbitMQ Exchanges:")
print(exchange_example)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Email Queue System")
print("=" * 60)

class EmailQueue:
    """Simulated email queue system"""
    
    def __init__(self):
        self.queue = []
        self.sent_emails = []
        self.failed_emails = []
    
    def enqueue_email(self, to: str, subject: str, body: str, priority: int = 5):
        """Add email to queue"""
        email = {
            "id": f"email-{len(self.queue) + 1}",
            "to": to,
            "subject": subject,
            "body": body,
            "priority": priority,
            "status": "queued",
            "attempts": 0
        }
        self.queue.append(email)
        print(f"📝 Queued: Email to {to} - {subject}")
        return email["id"]
    
    def process_queue(self, batch_size: int = 5):
        """Process emails in queue"""
        # Sort by priority (lower = higher priority)
        self.queue.sort(key=lambda x: x["priority"])
        
        batch = self.queue[:batch_size]
        self.queue = self.queue[batch_size:]
        
        for email in batch:
            self._send_email(email)
        
        return len(batch)
    
    def _send_email(self, email: dict):
        """Simulate sending email"""
        email["attempts"] += 1
        
        # Simulate 90% success rate
        import random
        success = random.random() > 0.1
        
        if success:
            email["status"] = "sent"
            self.sent_emails.append(email)
            print(f"✅ Sent: {email['to']} - {email['subject']}")
        else:
            if email["attempts"] < 3:
                email["status"] = "retry"
                self.queue.append(email)
                print(f"🔄 Retry: {email['to']} (attempt {email['attempts']})")
            else:
                email["status"] = "failed"
                self.failed_emails.append(email)
                print(f"❌ Failed: {email['to']} after {email['attempts']} attempts")
    
    def get_stats(self) -> dict:
        return {
            "queued": len(self.queue),
            "sent": len(self.sent_emails),
            "failed": len(self.failed_emails)
        }

# Demonstrate email queue
print("\n--- Email Queue Demo ---")
email_q = EmailQueue()

# Enqueue emails
email_q.enqueue_email("user1@example.com", "Welcome!", "Welcome to our service", priority=1)
email_q.enqueue_email("user2@example.com", "Newsletter", "Monthly newsletter", priority=5)
email_q.enqueue_email("admin@example.com", "Alert!", "System alert", priority=0)
email_q.enqueue_email("user3@example.com", "Promotion", "Special offer", priority=10)

# Process queue
print("\nProcessing queue...")
email_q.process_queue()

# Stats
print(f"\nStats: {email_q.get_stats()}")

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("MESSAGE QUEUE BEST PRACTICES")
print("=" * 60)

best_practices = """
✅ BEST PRACTICES:

1. Message Design:
   - Keep messages small and simple
   - Use JSON for serialization
   - Include message ID and timestamp
   - Design idempotent consumers

2. Error Handling:
   - Implement retry logic with backoff
   - Use dead letter queues for failed messages
   - Log failures for debugging
   - Set message TTL (time to live)

3. Reliability:
   - Use message acknowledgments
   - Enable message persistence
   - Implement circuit breakers
   - Monitor queue depth

4. Performance:
   - Batch messages when possible
   - Use appropriate prefetch count
   - Scale consumers based on queue depth
   - Use connection pooling

5. Monitoring:
   - Track message throughput
   - Monitor queue depth
   - Alert on consumer lag
   - Log processing times

⚠️ COMMON PITFALLS:
- Not handling duplicate messages
- Blocking on slow tasks
- Not persisting important messages
- Ignoring failed messages
- Not monitoring queue health

🎯 WHEN TO USE:
✓ Long-running tasks (email, reports)
✓ Spike handling (order processing)
✓ Service decoupling
✓ Event-driven architecture
✓ Batch processing
"""

print(best_practices)

print("\n" + "=" * 60)
print("✅ Message Queues - Complete!")
print("=" * 60)
