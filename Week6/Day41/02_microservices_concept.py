"""
Day 41 - Microservices Concept
==============================
Learn: Microservices architecture, patterns, and best practices

Key Concepts:
- Microservices vs Monolithic architecture
- Service communication patterns
- Key design patterns
- Benefits and challenges
"""

# ========== MICROSERVICES OVERVIEW ==========
print("=" * 60)
print("MICROSERVICES ARCHITECTURE")
print("=" * 60)

"""
Microservices Architecture:
- Application broken into small, independent services
- Each service handles a specific business function
- Services communicate via APIs (HTTP/REST, gRPC, message queues)
- Each service can be deployed, scaled, and updated independently

Monolithic vs Microservices:

Monolithic:
┌────────────────────────────┐
│          App               │
│  ┌────┐ ┌────┐ ┌────────┐ │
│  │User│ │Shop│ │Payments│ │
│  └────┘ └────┘ └────────┘ │
│     Single Database        │
└────────────────────────────┘

Microservices:
┌─────────┐   ┌─────────┐   ┌──────────┐
│User Svc │   │Shop Svc │   │Payment Svc│
│   DB    │   │   DB    │   │    DB     │
└─────────┘   └─────────┘   └──────────┘
     ↕            ↕              ↕
    ─────── API Gateway ─────────
"""

# ========== SERVICE COMMUNICATION ==========
print("\n" + "=" * 60)
print("SERVICE COMMUNICATION PATTERNS")
print("=" * 60)

import json
from typing import Dict, Any, Optional
from dataclasses import dataclass

# Simulate HTTP client for demonstration
@dataclass
class HTTPResponse:
    status_code: int
    data: Dict[str, Any]

class SimpleHTTPClient:
    """Simulated HTTP client for microservice communication"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
    
    def get(self, endpoint: str) -> HTTPResponse:
        """Simulate GET request"""
        # In real implementation, use requests library
        print(f"GET {self.base_url}{endpoint}")
        return HTTPResponse(200, {"message": "success"})
    
    def post(self, endpoint: str, data: Dict) -> HTTPResponse:
        """Simulate POST request"""
        print(f"POST {self.base_url}{endpoint}")
        print(f"Data: {json.dumps(data, indent=2)}")
        return HTTPResponse(201, {"id": "new-123", **data})

# Pattern 1: Synchronous Communication (HTTP/REST)
print("\n--- Pattern 1: Synchronous (HTTP/REST) ---")

class UserService:
    """User microservice"""
    
    def __init__(self):
        self.client = SimpleHTTPClient("http://user-service:8001")
    
    def get_user(self, user_id: str) -> Dict:
        response = self.client.get(f"/api/users/{user_id}")
        return response.data
    
    def create_user(self, name: str, email: str) -> Dict:
        response = self.client.post("/api/users", {"name": name, "email": email})
        return response.data

class OrderService:
    """Order microservice that depends on User service"""
    
    def __init__(self):
        self.client = SimpleHTTPClient("http://order-service:8002")
        self.user_service = UserService()
    
    def create_order(self, user_id: str, items: list) -> Dict:
        # First, verify user exists (sync call to another service)
        user = self.user_service.get_user(user_id)
        
        # Then create order
        response = self.client.post("/api/orders", {
            "user_id": user_id,
            "items": items
        })
        return response.data

# Demonstrate
user_svc = UserService()
print("\nCreating a user:")
user_svc.create_user("John Doe", "john@example.com")

order_svc = OrderService()
print("\nCreating an order (calls User service first):")
order_svc.create_order("user-123", ["item1", "item2"])

# Pattern 2: Asynchronous Communication (Message Queue)
print("\n--- Pattern 2: Asynchronous (Message Queue) ---")

class MessageQueue:
    """Simulated message queue"""
    
    def __init__(self):
        self.queues: Dict[str, list] = {}
        self.subscribers: Dict[str, list] = {}
    
    def publish(self, queue_name: str, message: Dict):
        """Publish message to queue"""
        if queue_name not in self.queues:
            self.queues[queue_name] = []
        self.queues[queue_name].append(message)
        print(f"Published to '{queue_name}': {message}")
        
        # Notify subscribers
        if queue_name in self.subscribers:
            for callback in self.subscribers[queue_name]:
                callback(message)
    
    def subscribe(self, queue_name: str, callback):
        """Subscribe to queue"""
        if queue_name not in self.subscribers:
            self.subscribers[queue_name] = []
        self.subscribers[queue_name].append(callback)
        print(f"Subscribed to '{queue_name}'")

# Event-driven microservices
message_queue = MessageQueue()

def handle_user_created(message):
    """Email service handles user created event"""
    print(f"📧 Email Service: Sending welcome email to {message['email']}")

def handle_order_created(message):
    """Inventory service handles order created event"""
    print(f"📦 Inventory Service: Reserving items for order {message['order_id']}")

# Subscribe services to events
message_queue.subscribe("user.created", handle_user_created)
message_queue.subscribe("order.created", handle_order_created)

print("\nPublishing events:")
message_queue.publish("user.created", {"user_id": "123", "email": "john@example.com"})
message_queue.publish("order.created", {"order_id": "456", "items": ["item1", "item2"]})

# ========== KEY MICROSERVICES PATTERNS ==========
print("\n" + "=" * 60)
print("KEY MICROSERVICES PATTERNS")
print("=" * 60)

# Pattern: API Gateway
print("\n--- Pattern: API Gateway ---")

class APIGateway:
    """
    API Gateway Pattern:
    - Single entry point for all clients
    - Routes requests to appropriate services
    - Handles cross-cutting concerns (auth, logging, rate limiting)
    """
    
    def __init__(self):
        self.services = {
            "/users": "http://user-service:8001",
            "/orders": "http://order-service:8002",
            "/payments": "http://payment-service:8003",
        }
        self.auth_enabled = True
    
    def authenticate(self, token: str) -> bool:
        """Verify authentication token"""
        # In real implementation, validate JWT token
        return token == "valid-token"
    
    def route_request(self, path: str, method: str, token: str, data: Dict = None) -> Dict:
        """Route request to appropriate service"""
        
        # Authentication
        if self.auth_enabled and not self.authenticate(token):
            return {"error": "Unauthorized", "status": 401}
        
        # Find service
        service_url = None
        for prefix, url in self.services.items():
            if path.startswith(prefix):
                service_url = url
                break
        
        if not service_url:
            return {"error": "Service not found", "status": 404}
        
        print(f"Routing {method} {path} -> {service_url}")
        return {"message": "Request routed successfully", "status": 200}

gateway = APIGateway()
print(gateway.route_request("/users/123", "GET", "valid-token"))
print(gateway.route_request("/orders", "POST", "valid-token", {"items": ["item1"]}))
print(gateway.route_request("/users", "GET", "invalid-token"))

# Pattern: Circuit Breaker
print("\n--- Pattern: Circuit Breaker ---")

import time
from datetime import datetime

class CircuitBreaker:
    """
    Circuit Breaker Pattern:
    - Prevents cascading failures
    - Three states: CLOSED (normal), OPEN (failing), HALF_OPEN (testing)
    - Opens circuit after threshold failures
    - Periodically tests if service recovered
    """
    
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"
    
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 30):
        self.state = self.CLOSED
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.last_failure_time = None
    
    def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        
        if self.state == self.OPEN:
            # Check if recovery timeout has passed
            if self._should_attempt_recovery():
                self.state = self.HALF_OPEN
                print("Circuit Breaker: HALF_OPEN - Testing service")
            else:
                raise Exception("Circuit breaker is OPEN - Service unavailable")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_recovery(self) -> bool:
        if self.last_failure_time is None:
            return True
        elapsed = time.time() - self.last_failure_time
        return elapsed >= self.recovery_timeout
    
    def _on_success(self):
        """Called when request succeeds"""
        self.failure_count = 0
        if self.state == self.HALF_OPEN:
            self.state = self.CLOSED
            print("Circuit Breaker: Service recovered - CLOSED")
    
    def _on_failure(self):
        """Called when request fails"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = self.OPEN
            print(f"Circuit Breaker: OPEN after {self.failure_count} failures")

# Demonstrate circuit breaker
def unreliable_service(should_fail: bool = False):
    """Simulated unreliable service"""
    if should_fail:
        raise Exception("Service failed!")
    return "Success!"

breaker = CircuitBreaker(failure_threshold=3)

print("\nTesting Circuit Breaker:")
for i in range(5):
    try:
        # Simulate failures
        result = breaker.call(unreliable_service, should_fail=(i < 3))
        print(f"Call {i+1}: {result}")
    except Exception as e:
        print(f"Call {i+1}: {e}")
print(f"Circuit state: {breaker.state}")

# Pattern: Service Registry
print("\n--- Pattern: Service Registry ---")

class ServiceRegistry:
    """
    Service Registry Pattern:
    - Central directory of all services
    - Services register themselves on startup
    - Other services lookup locations dynamically
    - Enables service discovery
    """
    
    def __init__(self):
        self.services: Dict[str, list] = {}
    
    def register(self, service_name: str, host: str, port: int):
        """Register a service instance"""
        if service_name not in self.services:
            self.services[service_name] = []
        
        instance = {"host": host, "port": port, "healthy": True}
        self.services[service_name].append(instance)
        print(f"Registered: {service_name} at {host}:{port}")
    
    def deregister(self, service_name: str, host: str, port: int):
        """Remove a service instance"""
        if service_name in self.services:
            self.services[service_name] = [
                s for s in self.services[service_name]
                if not (s["host"] == host and s["port"] == port)
            ]
            print(f"Deregistered: {service_name} at {host}:{port}")
    
    def get_instance(self, service_name: str) -> Optional[Dict]:
        """Get a healthy service instance (simple round-robin)"""
        if service_name not in self.services:
            return None
        
        healthy = [s for s in self.services[service_name] if s["healthy"]]
        if not healthy:
            return None
        
        # Simple load balancing - return first healthy instance
        return healthy[0]
    
    def get_all_instances(self, service_name: str) -> list:
        """Get all instances of a service"""
        return self.services.get(service_name, [])

registry = ServiceRegistry()
registry.register("user-service", "192.168.1.10", 8001)
registry.register("user-service", "192.168.1.11", 8001)
registry.register("order-service", "192.168.1.20", 8002)

print(f"\nLooking up user-service: {registry.get_instance('user-service')}")
print(f"All user-service instances: {registry.get_all_instances('user-service')}")

# ========== SAGA PATTERN ==========
print("\n" + "=" * 60)
print("SAGA PATTERN (Distributed Transactions)")
print("=" * 60)

class OrderSaga:
    """
    SAGA Pattern:
    - Manages distributed transactions across services
    - Each step has a compensating action (rollback)
    - If a step fails, previous steps are compensated
    """
    
    def __init__(self):
        self.completed_steps = []
    
    def create_order(self, user_id: str, items: list, amount: float):
        """Execute order creation saga"""
        print(f"\nStarting Order Saga for user {user_id}")
        
        try:
            # Step 1: Reserve inventory
            self._reserve_inventory(items)
            self.completed_steps.append("inventory")
            
            # Step 2: Process payment
            self._process_payment(user_id, amount)
            self.completed_steps.append("payment")
            
            # Step 3: Create order record
            order_id = self._create_order_record(user_id, items)
            self.completed_steps.append("order")
            
            # Step 4: Send notification
            self._send_notification(user_id, order_id)
            self.completed_steps.append("notification")
            
            print(f"✅ Order saga completed successfully! Order ID: {order_id}")
            return order_id
            
        except Exception as e:
            print(f"❌ Saga failed at step: {e}")
            self._compensate()
            raise
    
    def _reserve_inventory(self, items: list):
        print(f"  1. Reserving inventory for {items}")
        # Simulate success/failure
        # raise Exception("inventory") to test compensation
    
    def _process_payment(self, user_id: str, amount: float):
        print(f"  2. Processing payment of ${amount} for user {user_id}")
        # raise Exception("payment") to test compensation
    
    def _create_order_record(self, user_id: str, items: list) -> str:
        print(f"  3. Creating order record")
        return "ORDER-123"
    
    def _send_notification(self, user_id: str, order_id: str):
        print(f"  4. Sending notification for order {order_id}")
    
    def _compensate(self):
        """Rollback completed steps in reverse order"""
        print("\nCompensating (rolling back)...")
        
        for step in reversed(self.completed_steps):
            if step == "notification":
                print("  - Nothing to compensate for notification")
            elif step == "order":
                print("  - Cancelling order record")
            elif step == "payment":
                print("  - Refunding payment")
            elif step == "inventory":
                print("  - Releasing inventory reservation")
        
        self.completed_steps = []

# Demonstrate saga
saga = OrderSaga()
saga.create_order("user-123", ["item1", "item2"], 99.99)

# ========== BENEFITS AND CHALLENGES ==========
print("\n" + "=" * 60)
print("MICROSERVICES: BENEFITS AND CHALLENGES")
print("=" * 60)

summary = """
✅ BENEFITS:
1. Independent Deployment
   - Deploy services without affecting others
   - Faster release cycles

2. Technology Diversity
   - Use best technology for each service
   - Teams can choose their stack

3. Scalability
   - Scale individual services based on demand
   - Cost-effective resource usage

4. Fault Isolation
   - Failure in one service doesn't crash entire system
   - Easier to identify and fix issues

5. Team Autonomy
   - Small teams own specific services
   - Faster decision making

❌ CHALLENGES:
1. Network Complexity
   - Service-to-service communication
   - Network latency and failures

2. Data Consistency
   - No shared database
   - Eventual consistency challenges

3. Testing Difficulty
   - Integration testing is complex
   - Need to mock other services

4. Operational Overhead
   - More services to monitor
   - Need robust DevOps practices

5. Distributed Tracing
   - Debugging across services is hard
   - Need specialized tools

🎯 WHEN TO USE:
✓ Large, complex applications
✓ Need independent scaling
✓ Multiple teams working on same product
✓ Different parts have different tech requirements
✓ High availability requirements

🚫 WHEN NOT TO USE:
✗ Small applications or MVPs
✗ Small teams
✗ Simple domain models
✗ Limited DevOps expertise
✗ Tight deadlines (start monolith first)
"""

print(summary)

print("\n" + "=" * 60)
print("✅ Microservices Concept - Complete!")
print("=" * 60)
