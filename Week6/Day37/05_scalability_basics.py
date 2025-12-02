"""
Scalability Basics
==================
Day 37 - System Design Basics

Learn fundamental concepts for building scalable applications.
"""

# ============================================================
# 1. WHAT IS SCALABILITY?
# ============================================================

"""
Scalability: The ability of a system to handle increased load
by adding resources.

Types of Scaling:

1. Vertical Scaling (Scale Up)
   - Add more power to existing machine
   - More CPU, RAM, Storage
   - Limited by hardware constraints
   - Simple but has ceiling

2. Horizontal Scaling (Scale Out)
   - Add more machines
   - Distribute load across servers
   - More complex but unlimited
   - Requires load balancing

Key Metrics:
- Throughput: Requests per second
- Latency: Time to respond
- Availability: Uptime percentage
- Consistency: Data accuracy across nodes
"""

# ============================================================
# 2. LOAD BALANCING
# ============================================================

"""
Load Balancer: Distributes traffic across multiple servers

Load Balancing Algorithms:

1. Round Robin
   - Requests go to servers in sequence
   - Simple, equal distribution
   - Doesn't consider server load

2. Weighted Round Robin
   - Assign weights based on capacity
   - More powerful servers get more traffic

3. Least Connections
   - Send to server with fewest active connections
   - Good for long-lived connections

4. IP Hash
   - Hash client IP to determine server
   - Same client always hits same server
   - Good for session affinity

5. Least Response Time
   - Send to fastest responding server
   - Combines latency and connections
"""

# Load Balancer Configuration Example (Nginx)
nginx_load_balancer = """
# nginx.conf - Load Balancer Configuration

upstream backend_servers {
    # Round Robin (default)
    server backend1.example.com:8000;
    server backend2.example.com:8000;
    server backend3.example.com:8000;
}

upstream weighted_backend {
    # Weighted Round Robin
    server backend1.example.com:8000 weight=5;  # Gets 50% traffic
    server backend2.example.com:8000 weight=3;  # Gets 30% traffic
    server backend3.example.com:8000 weight=2;  # Gets 20% traffic
}

upstream least_conn_backend {
    # Least Connections
    least_conn;
    server backend1.example.com:8000;
    server backend2.example.com:8000;
    server backend3.example.com:8000;
}

upstream ip_hash_backend {
    # IP Hash (sticky sessions)
    ip_hash;
    server backend1.example.com:8000;
    server backend2.example.com:8000;
    server backend3.example.com:8000;
}

server {
    listen 80;
    
    location / {
        proxy_pass http://backend_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
"""

# Health Checks
health_check_config = """
upstream backend_servers {
    server backend1.example.com:8000;
    server backend2.example.com:8000;
    server backend3.example.com:8000;
    
    # Mark server as down after 3 failed health checks
    # Check every 5 seconds, timeout after 2 seconds
}

server {
    location /health {
        return 200 'healthy';
        add_header Content-Type text/plain;
    }
}
"""

# ============================================================
# 3. DATABASE SCALING
# ============================================================

"""
Database Scaling Strategies:

1. Vertical Scaling
   - Upgrade hardware
   - Faster CPU, more RAM
   - Limited by hardware

2. Read Replicas
   - Master handles writes
   - Replicas handle reads
   - Eventually consistent

3. Sharding (Horizontal Partitioning)
   - Split data across databases
   - Each shard has subset of data
   - Complex queries harder

4. Connection Pooling
   - Reuse database connections
   - Reduce connection overhead
"""

# Read Replica Pattern
read_replica_example = '''
import random

class DatabaseCluster:
    """Database with master and read replicas"""
    
    def __init__(self, master_host, replica_hosts):
        self.master = DatabaseConnection(master_host)
        self.replicas = [DatabaseConnection(host) for host in replica_hosts]
    
    def write(self, query, params=None):
        """All writes go to master"""
        return self.master.execute(query, params)
    
    def read(self, query, params=None):
        """Reads distributed across replicas"""
        replica = random.choice(self.replicas)
        return replica.execute(query, params)
    
    def read_from_master(self, query, params=None):
        """Read from master when consistency required"""
        return self.master.execute(query, params)

# Usage
db = DatabaseCluster(
    master_host='master.db.example.com',
    replica_hosts=[
        'replica1.db.example.com',
        'replica2.db.example.com',
        'replica3.db.example.com'
    ]
)

# Write operation - goes to master
db.write("INSERT INTO users (name) VALUES (?)", ['John'])

# Read operation - goes to random replica
users = db.read("SELECT * FROM users")

# Read that needs latest data - goes to master
user = db.read_from_master("SELECT * FROM users WHERE id = ?", [1])
'''

# Sharding Example
sharding_example = '''
class ShardedDatabase:
    """
    Sharding: Distribute data across multiple databases
    
    Sharding strategies:
    1. Range-based: user_id 1-1000 -> shard1, 1001-2000 -> shard2
    2. Hash-based: hash(user_id) % num_shards
    3. Directory-based: Lookup table for shard mapping
    """
    
    def __init__(self, shard_hosts):
        self.shards = [DatabaseConnection(host) for host in shard_hosts]
        self.num_shards = len(self.shards)
    
    def get_shard(self, user_id):
        """Hash-based sharding"""
        shard_index = hash(user_id) % self.num_shards
        return self.shards[shard_index]
    
    def get_user(self, user_id):
        """Get user from appropriate shard"""
        shard = self.get_shard(user_id)
        return shard.execute(
            "SELECT * FROM users WHERE id = ?",
            [user_id]
        )
    
    def create_user(self, user_id, data):
        """Create user in appropriate shard"""
        shard = self.get_shard(user_id)
        return shard.execute(
            "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
            [user_id, data['name'], data['email']]
        )
    
    def get_all_users(self):
        """Query all shards (expensive!)"""
        all_users = []
        for shard in self.shards:
            users = shard.execute("SELECT * FROM users")
            all_users.extend(users)
        return all_users

# Sharding considerations:
# - Cross-shard queries are expensive
# - Need to handle rebalancing when adding shards
# - Choose shard key carefully (user_id, tenant_id)
'''

# Connection Pooling
connection_pooling = '''
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Create engine with connection pool
engine = create_engine(
    'postgresql://user:pass@localhost/db',
    poolclass=QueuePool,
    pool_size=10,          # Number of connections to keep
    max_overflow=20,       # Additional connections if pool is full
    pool_timeout=30,       # Seconds to wait for connection
    pool_recycle=1800,     # Recycle connections after 30 minutes
    pool_pre_ping=True     # Test connections before use
)

# Connection is returned to pool after use
with engine.connect() as conn:
    result = conn.execute("SELECT * FROM users")
'''

# ============================================================
# 4. CACHING FOR SCALABILITY
# ============================================================

"""
Caching Layers for Scale:

1. Application-level Cache (Redis/Memcached)
   - Cache database queries
   - Cache computed results
   - Session storage

2. CDN (Content Delivery Network)
   - Static assets
   - Geographic distribution
   - Edge caching

3. HTTP/Browser Cache
   - Cache headers
   - Client-side caching
"""

# Multi-level Caching
multi_level_cache = '''
class MultiLevelCache:
    """
    Multi-level caching for scalability
    L1: In-memory (fastest, limited size)
    L2: Redis (fast, distributed)
    L3: Database (slowest, persistent)
    """
    
    def __init__(self):
        self.l1_cache = {}  # Local memory
        self.l2_cache = redis.Redis()  # Redis
        self.database = Database()  # PostgreSQL
    
    def get(self, key):
        # Try L1 (memory)
        if key in self.l1_cache:
            return self.l1_cache[key]
        
        # Try L2 (Redis)
        value = self.l2_cache.get(key)
        if value:
            self.l1_cache[key] = value  # Populate L1
            return value
        
        # Get from database
        value = self.database.get(key)
        if value:
            # Populate all cache levels
            self.l2_cache.setex(key, 3600, value)
            self.l1_cache[key] = value
        
        return value
    
    def set(self, key, value):
        # Update all levels
        self.database.set(key, value)
        self.l2_cache.setex(key, 3600, value)
        self.l1_cache[key] = value
    
    def invalidate(self, key):
        # Clear from all levels
        self.l1_cache.pop(key, None)
        self.l2_cache.delete(key)
'''

# ============================================================
# 5. ASYNCHRONOUS PROCESSING
# ============================================================

"""
Async Processing for Scale:

1. Message Queues
   - Decouple components
   - Handle bursts of traffic
   - Retry failed operations

2. Background Jobs
   - Email sending
   - Image processing
   - Report generation

3. Event-Driven Architecture
   - Publish-subscribe pattern
   - Loose coupling
"""

# Message Queue Example (Celery)
celery_example = '''
from celery import Celery

# Configure Celery
app = Celery('tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

# Define tasks
@app.task
def send_email(to, subject, body):
    """Send email asynchronously"""
    # Email sending logic
    print(f"Sending email to {to}")
    return True

@app.task
def process_image(image_path):
    """Process image in background"""
    # Image processing logic
    print(f"Processing {image_path}")
    return f"processed_{image_path}"

@app.task
def generate_report(user_id, date_range):
    """Generate report asynchronously"""
    # Report generation logic
    print(f"Generating report for user {user_id}")
    return {"report": "data"}

# Usage in API endpoint
@app.route('/api/register', methods=['POST'])
def register():
    user = create_user(request.json)
    
    # Send welcome email asynchronously
    send_email.delay(
        user['email'],
        'Welcome!',
        'Thanks for signing up!'
    )
    
    return jsonify(user)

@app.route('/api/upload', methods=['POST'])
def upload():
    image = save_uploaded_file(request.files['image'])
    
    # Process image in background
    task = process_image.delay(image['path'])
    
    return jsonify({
        'image_id': image['id'],
        'task_id': task.id,
        'status': 'processing'
    })

# Check task status
@app.route('/api/task/<task_id>')
def task_status(task_id):
    task = AsyncResult(task_id)
    return jsonify({
        'task_id': task_id,
        'status': task.status,
        'result': task.result if task.ready() else None
    })
'''

# ============================================================
# 6. MICROSERVICES BASICS
# ============================================================

"""
Microservices: Break application into small, independent services

Benefits:
- Independent deployment
- Technology diversity
- Team autonomy
- Fault isolation
- Scalability per service

Challenges:
- Network complexity
- Data consistency
- Service discovery
- Monitoring
"""

# Microservices Architecture
microservices_arch = """
                    ┌─────────────────┐
                    │   API Gateway   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ User Service  │   │ Order Service │   │Product Service│
│   (FastAPI)   │   │   (Django)    │   │   (Node.js)   │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        ▼                   ▼                   ▼
   ┌─────────┐        ┌─────────┐        ┌─────────┐
   │ User DB │        │Order DB │        │Product  │
   │(Postgres)│       │(Postgres)│       │DB(Mongo)│
   └─────────┘        └─────────┘        └─────────┘
"""

# API Gateway Pattern
api_gateway_example = '''
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Service registry
services = {
    'users': 'http://user-service:8001',
    'orders': 'http://order-service:8002',
    'products': 'http://product-service:8003'
}

@app.route('/api/users/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_users(path):
    """Proxy requests to user service"""
    url = f"{services['users']}/{path}"
    resp = requests.request(
        method=request.method,
        url=url,
        headers={k: v for k, v in request.headers if k != 'Host'},
        data=request.get_data(),
        params=request.args
    )
    return jsonify(resp.json()), resp.status_code

@app.route('/api/orders/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_orders(path):
    """Proxy requests to order service"""
    url = f"{services['orders']}/{path}"
    resp = requests.request(
        method=request.method,
        url=url,
        headers={k: v for k, v in request.headers if k != 'Host'},
        data=request.get_data(),
        params=request.args
    )
    return jsonify(resp.json()), resp.status_code

# Aggregation endpoint
@app.route('/api/dashboard')
def dashboard():
    """Aggregate data from multiple services"""
    user_id = request.args.get('user_id')
    
    # Fetch from multiple services
    user = requests.get(f"{services['users']}/users/{user_id}").json()
    orders = requests.get(f"{services['orders']}/orders?user_id={user_id}").json()
    
    return jsonify({
        'user': user,
        'orders': orders,
        'order_count': len(orders)
    })
'''

# ============================================================
# 7. CAP THEOREM
# ============================================================

"""
CAP Theorem: Distributed systems can only guarantee 2 of 3:

C - Consistency: All nodes see same data at same time
A - Availability: System responds to every request
P - Partition Tolerance: System works despite network failures

Real-world choices:
- CP: Choose consistency over availability (banking)
- AP: Choose availability over consistency (social media)
- CA: Not possible in distributed systems (network partitions happen)

Examples:
- CP Systems: MongoDB, HBase, Redis (single master)
- AP Systems: Cassandra, CouchDB, DynamoDB
"""

# Consistency Models
consistency_models = """
Consistency Models:

1. Strong Consistency
   - Read always returns latest write
   - Simple for developers
   - Lower availability, higher latency
   - Example: Traditional RDBMS

2. Eventual Consistency
   - Reads may return stale data
   - Eventually converges to latest
   - Higher availability
   - Example: DNS, CDN, Cassandra

3. Causal Consistency
   - Related operations in order
   - Unrelated operations may be out of order
   - Compromise between strong and eventual

4. Read-Your-Writes Consistency
   - User sees their own writes immediately
   - Others may see stale data
"""

# ============================================================
# 8. RATE LIMITING & THROTTLING
# ============================================================

"""
Rate Limiting: Protect system from overload

Algorithms:
1. Fixed Window
2. Sliding Window
3. Token Bucket
4. Leaky Bucket
"""

# Rate Limiting Implementation
rate_limiting = '''
import time
from collections import defaultdict

class RateLimiter:
    """Token Bucket Rate Limiter"""
    
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity  # Max tokens
        self.refill_rate = refill_rate  # Tokens per second
        self.buckets = defaultdict(lambda: {
            'tokens': capacity,
            'last_refill': time.time()
        })
    
    def _refill(self, bucket):
        """Refill bucket based on time elapsed"""
        now = time.time()
        elapsed = now - bucket['last_refill']
        refill_amount = elapsed * self.refill_rate
        bucket['tokens'] = min(
            self.capacity,
            bucket['tokens'] + refill_amount
        )
        bucket['last_refill'] = now
    
    def allow_request(self, client_id, tokens_needed=1):
        """Check if request should be allowed"""
        bucket = self.buckets[client_id]
        self._refill(bucket)
        
        if bucket['tokens'] >= tokens_needed:
            bucket['tokens'] -= tokens_needed
            return True
        return False
    
    def get_remaining(self, client_id):
        """Get remaining tokens for client"""
        bucket = self.buckets[client_id]
        self._refill(bucket)
        return bucket['tokens']

# Usage
limiter = RateLimiter(capacity=100, refill_rate=10)  # 100 tokens, 10/second

def rate_limited_endpoint(client_id):
    if not limiter.allow_request(client_id):
        return {'error': 'Rate limit exceeded'}, 429
    
    # Process request
    return {'data': 'response'}

# With Redis for distributed rate limiting
class RedisRateLimiter:
    """Distributed rate limiter using Redis"""
    
    def __init__(self, redis_client, limit, window_seconds):
        self.redis = redis_client
        self.limit = limit
        self.window = window_seconds
    
    def allow_request(self, client_id):
        key = f"rate_limit:{client_id}"
        current = self.redis.incr(key)
        
        if current == 1:
            self.redis.expire(key, self.window)
        
        return current <= self.limit
'''

# ============================================================
# 9. MONITORING & OBSERVABILITY
# ============================================================

"""
Three Pillars of Observability:

1. Logging
   - What happened
   - Structured logs
   - Centralized logging (ELK, Splunk)

2. Metrics
   - Quantitative measurements
   - Time-series data
   - Prometheus, Grafana

3. Tracing
   - Request flow across services
   - Distributed tracing
   - Jaeger, Zipkin
"""

# Logging Example
logging_example = '''
import logging
import json
from datetime import datetime

# Structured logging
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'logger': record.name,
            'path': record.pathname,
            'line': record.lineno
        }
        if hasattr(record, 'extra'):
            log_data.update(record.extra)
        return json.dumps(log_data)

# Setup logger
logger = logging.getLogger('app')
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage
logger.info('User logged in', extra={
    'user_id': 123,
    'ip_address': '192.168.1.1',
    'user_agent': 'Mozilla/5.0'
})
'''

# Metrics Example
metrics_example = '''
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

ACTIVE_CONNECTIONS = Gauge(
    'active_connections',
    'Number of active connections'
)

# Use in application
def handle_request(method, endpoint):
    with REQUEST_LATENCY.labels(method=method, endpoint=endpoint).time():
        ACTIVE_CONNECTIONS.inc()
        try:
            # Handle request
            response = process_request()
            REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=200).inc()
            return response
        except Exception as e:
            REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=500).inc()
            raise
        finally:
            ACTIVE_CONNECTIONS.dec()

# Start metrics server
start_http_server(8000)  # Prometheus scrapes this
'''

# ============================================================
# 10. SCALABILITY CHECKLIST
# ============================================================

"""
Scalability Checklist:

□ Load Balancing
  - Multiple application instances
  - Health checks configured
  - Session handling (sticky or distributed)

□ Database
  - Connection pooling
  - Read replicas for read-heavy workloads
  - Consider sharding for very large data

□ Caching
  - Application-level cache (Redis)
  - HTTP caching headers
  - CDN for static assets

□ Async Processing
  - Message queues for heavy tasks
  - Background job processing
  - Event-driven where appropriate

□ API Design
  - Pagination for list endpoints
  - Rate limiting
  - Compression (gzip)

□ Monitoring
  - Logging (structured)
  - Metrics (Prometheus)
  - Distributed tracing

□ Statelessness
  - No server-side session state
  - External session storage if needed
  - Horizontally scalable
"""

# ============================================================
# SUMMARY
# ============================================================

"""
Scalability Summary:

1. Vertical vs Horizontal Scaling
   - Vertical: Add more power
   - Horizontal: Add more machines

2. Load Balancing
   - Distribute traffic
   - Round robin, least connections, IP hash

3. Database Scaling
   - Read replicas
   - Sharding
   - Connection pooling

4. Caching
   - Application cache (Redis)
   - CDN for static assets
   - HTTP caching

5. Async Processing
   - Message queues
   - Background jobs

6. Monitoring
   - Logs, Metrics, Traces
"""

if __name__ == "__main__":
    print("Scalability Basics")
    print("=" * 50)
    
    print("\nScaling Strategies:")
    print("1. Vertical Scaling (Scale Up)")
    print("2. Horizontal Scaling (Scale Out)")
    
    print("\nLoad Balancing Algorithms:")
    print("- Round Robin")
    print("- Weighted Round Robin")
    print("- Least Connections")
    print("- IP Hash")
    
    print("\nDatabase Scaling:")
    print("- Read Replicas")
    print("- Sharding")
    print("- Connection Pooling")
    
    print("\nCAP Theorem:")
    print("- Consistency")
    print("- Availability")
    print("- Partition Tolerance")
    print("Choose 2 of 3 for distributed systems")
