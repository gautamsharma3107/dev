"""
Day 18 - Redis Caching
======================
Learn: Key-value storage and caching concepts

Key Concepts:
- Redis as a cache layer
- Cache-aside pattern
- TTL (Time To Live)
- Common caching strategies

Note: This tutorial simulates Redis concepts using Python dicts.
      For real Redis, install: pip install redis
"""

import time
import json
import sqlite3
import os
from datetime import datetime, timedelta
from typing import Any, Callable

# ========== WHAT IS REDIS ==========
print("=" * 60)
print("REDIS CACHING BASICS")
print("=" * 60)

print("""
Redis is an in-memory data structure store:

Key Features:
- Lightning fast (data in memory)
- Key-value storage
- Supports multiple data types
- TTL (expiration) support
- Persistence options

Common Use Cases:
1. Caching - Speed up database queries
2. Session storage - User session data
3. Rate limiting - API throttling
4. Real-time analytics - Counters, leaderboards
5. Message queues - Pub/sub messaging

Why Cache?
┌─────────────────────────────────────────────┐
│ Without Cache:                              │
│ Client → Server → Database (100ms)          │
│                                             │
│ With Cache:                                 │
│ Client → Server → Cache (1ms) ✓ Hit         │
│ Client → Server → Cache → Database (Miss)   │
└─────────────────────────────────────────────┘
""")

# ========== SIMULATED REDIS ==========
print("\n" + "=" * 60)
print("SIMULATED REDIS CLIENT")
print("=" * 60)

class SimpleRedis:
    """Simulates Redis for learning purposes"""
    
    def __init__(self):
        self._data = {}
        self._expires = {}
        self.stats = {"hits": 0, "misses": 0}
    
    def set(self, key: str, value: Any, ex: int = None) -> bool:
        """Set a key-value pair with optional expiration (seconds)"""
        self._data[key] = value
        if ex:
            self._expires[key] = datetime.now() + timedelta(seconds=ex)
        return True
    
    def get(self, key: str) -> Any | None:
        """Get value by key, returns None if expired or not found"""
        self._cleanup_expired(key)
        
        if key in self._data:
            self.stats["hits"] += 1
            return self._data[key]
        self.stats["misses"] += 1
        return None
    
    def delete(self, key: str) -> int:
        """Delete a key, returns 1 if deleted, 0 otherwise"""
        if key in self._data:
            del self._data[key]
            if key in self._expires:
                del self._expires[key]
            return 1
        return 0
    
    def exists(self, key: str) -> bool:
        """Check if key exists and is not expired"""
        self._cleanup_expired(key)
        return key in self._data
    
    def ttl(self, key: str) -> int:
        """Get time to live in seconds, -1 if no expiry, -2 if not exists"""
        self._cleanup_expired(key)
        if key not in self._data:
            return -2
        if key not in self._expires:
            return -1
        remaining = (self._expires[key] - datetime.now()).total_seconds()
        return max(0, int(remaining))
    
    def expire(self, key: str, seconds: int) -> bool:
        """Set expiration on existing key"""
        if key in self._data:
            self._expires[key] = datetime.now() + timedelta(seconds=seconds)
            return True
        return False
    
    def incr(self, key: str) -> int:
        """Increment value by 1"""
        if key not in self._data:
            self._data[key] = 0
        self._data[key] += 1
        return self._data[key]
    
    def keys(self, pattern: str = "*") -> list:
        """Get all keys (simplified, pattern not fully implemented)"""
        self._cleanup_all_expired()
        if pattern == "*":
            return list(self._data.keys())
        return [k for k in self._data.keys() if pattern.strip("*") in k]
    
    def flushall(self) -> bool:
        """Clear all data"""
        self._data.clear()
        self._expires.clear()
        self.stats = {"hits": 0, "misses": 0}
        return True
    
    def _cleanup_expired(self, key: str):
        """Remove key if expired"""
        if key in self._expires:
            if datetime.now() > self._expires[key]:
                del self._data[key]
                del self._expires[key]
    
    def _cleanup_all_expired(self):
        """Remove all expired keys"""
        expired = [k for k, v in self._expires.items() if datetime.now() > v]
        for key in expired:
            del self._data[key]
            del self._expires[key]

# Create Redis client
redis = SimpleRedis()
print("✅ Created simulated Redis client")

# ========== BASIC OPERATIONS ==========
print("\n" + "=" * 60)
print("BASIC REDIS OPERATIONS")
print("=" * 60)

# SET and GET
print("\n1. SET and GET:")
redis.set("user:1:name", "Alice")
redis.set("user:1:email", "alice@example.com")
print(f"   SET user:1:name = 'Alice'")
print(f"   GET user:1:name = '{redis.get('user:1:name')}'")

# SET with expiration
print("\n2. SET with TTL (expiration):")
redis.set("session:abc123", "user_data_here", ex=3600)  # 1 hour
print(f"   SET session:abc123 with ex=3600 (1 hour)")
print(f"   TTL: {redis.ttl('session:abc123')} seconds")

# EXISTS and DELETE
print("\n3. EXISTS and DELETE:")
print(f"   EXISTS user:1:name: {redis.exists('user:1:name')}")
redis.delete("user:1:email")
print(f"   DELETE user:1:email")
print(f"   EXISTS user:1:email: {redis.exists('user:1:email')}")

# INCR (counters)
print("\n4. INCR (counter):")
redis.set("page:home:views", 0)
for _ in range(5):
    count = redis.incr("page:home:views")
print(f"   After 5 increments: {count}")

# ========== CACHE-ASIDE PATTERN ==========
print("\n" + "=" * 60)
print("CACHE-ASIDE PATTERN")
print("=" * 60)

print("""
The Cache-Aside pattern:

1. Check cache for data
2. If found (HIT): Return cached data
3. If not found (MISS):
   - Fetch from database
   - Store in cache
   - Return data

┌────────────┐
│   Client   │
└─────┬──────┘
      │
┌─────▼──────┐   HIT    ┌───────────┐
│   Cache    │◄─────────│   Return  │
└─────┬──────┘          └───────────┘
      │ MISS
      │
┌─────▼──────┐          ┌───────────┐
│  Database  │─────────►│   Cache   │
└────────────┘  Store   └───────────┘
""")

# Setup database for demonstration
db_file = "cache_demo.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

# Insert sample data
products = [
    (1, "Laptop", 999.99),
    (2, "Mouse", 29.99),
    (3, "Keyboard", 79.99),
    (4, "Monitor", 299.99),
]
cursor.executemany("INSERT INTO products VALUES (?, ?, ?)", products)
conn.commit()

def get_product_from_db(product_id: int) -> dict | None:
    """Simulates slow database query"""
    time.sleep(0.05)  # Simulate 50ms database latency
    cursor.execute(
        "SELECT * FROM products WHERE id = ?", 
        (product_id,)
    )
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "name": row[1], "price": row[2]}
    return None

def get_product_cached(product_id: int) -> dict | None:
    """Get product with cache-aside pattern"""
    cache_key = f"product:{product_id}"
    
    # Step 1: Check cache
    cached = redis.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Step 2: Cache miss - fetch from database
    product = get_product_from_db(product_id)
    
    if product:
        # Step 3: Store in cache (expire in 5 minutes)
        redis.set(cache_key, json.dumps(product), ex=300)
    
    return product

# Clear stats
redis.flushall()

# Demonstrate cache-aside
print("\n📊 Cache-Aside Demonstration:")
print("-" * 40)

# First call - cache miss
start = time.time()
product = get_product_cached(1)
elapsed = (time.time() - start) * 1000
print(f"First call (MISS): {product['name']} - {elapsed:.1f}ms")

# Second call - cache hit
start = time.time()
product = get_product_cached(1)
elapsed = (time.time() - start) * 1000
print(f"Second call (HIT): {product['name']} - {elapsed:.3f}ms")

print(f"\nCache stats: {redis.stats}")

# ========== CACHING STRATEGIES ==========
print("\n" + "=" * 60)
print("CACHING STRATEGIES")
print("=" * 60)

print("""
1. CACHE-ASIDE (Read-Through)
   ✓ Application manages cache
   ✓ Lazy loading - cache on first access
   ✓ Most common pattern

2. WRITE-THROUGH
   ✓ Write to cache and DB simultaneously
   ✓ Ensures cache consistency
   ✓ Higher write latency

3. WRITE-BEHIND (Write-Back)
   ✓ Write to cache immediately
   ✓ Asynchronously write to DB
   ✓ Risk of data loss

4. REFRESH-AHEAD
   ✓ Proactively refresh before expiry
   ✓ Reduces cache misses
   ✓ More complex to implement
""")

# ========== CACHE INVALIDATION ==========
print("\n" + "=" * 60)
print("CACHE INVALIDATION")
print("=" * 60)

print("""
"There are only two hard things in Computer Science:
 cache invalidation and naming things." - Phil Karlton

Strategies:
1. TTL (Time-To-Live) - Auto-expire after time
2. Manual Invalidation - Delete on update
3. Version Keys - Append version to cache key
4. Pub/Sub - Broadcast invalidation events
""")

# Demonstrate manual invalidation
print("\n📊 Manual Invalidation Example:")

def update_product(product_id: int, new_price: float):
    """Update product and invalidate cache"""
    # Update database
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (new_price, product_id)
    )
    conn.commit()
    
    # Invalidate cache
    cache_key = f"product:{product_id}"
    redis.delete(cache_key)
    print(f"   Cache invalidated for {cache_key}")

# Get product (will cache)
product = get_product_cached(1)
print(f"Before update: {product['name']} = ${product['price']}")

# Update (invalidates cache)
update_product(1, 899.99)

# Get again (cache miss, fetches new data)
product = get_product_cached(1)
print(f"After update: {product['name']} = ${product['price']}")

# ========== TTL DEMONSTRATION ==========
print("\n" + "=" * 60)
print("TTL (TIME TO LIVE) DEMONSTRATION")
print("=" * 60)

# Set key with short TTL
redis.set("temp:data", "This will expire!", ex=2)
print("Set 'temp:data' with TTL=2 seconds")

print(f"Immediately: exists={redis.exists('temp:data')}, ttl={redis.ttl('temp:data')}s")

time.sleep(1)
print(f"After 1 second: exists={redis.exists('temp:data')}, ttl={redis.ttl('temp:data')}s")

time.sleep(1.5)
print(f"After 2.5 seconds: exists={redis.exists('temp:data')}, ttl={redis.ttl('temp:data')}")

# ========== COMMON CACHING PATTERNS ==========
print("\n" + "=" * 60)
print("COMMON CACHING PATTERNS")
print("=" * 60)

print("""
1. SESSION CACHING
   redis.set("session:abc123", json.dumps(user_data), ex=3600)
   
2. API RESPONSE CACHING
   key = f"api:/users/{user_id}"
   redis.set(key, json.dumps(response), ex=300)

3. RATE LIMITING
   def check_rate_limit(user_id, limit=100):
       key = f"ratelimit:{user_id}:{current_minute}"
       count = redis.incr(key)
       redis.expire(key, 60)
       return count <= limit

4. LEADERBOARD
   # Using sorted sets (not in our simple implementation)
   redis.zadd("leaderboard", {user_id: score})
   top_10 = redis.zrevrange("leaderboard", 0, 9)

5. RECENT ITEMS
   # Using lists
   redis.lpush(f"recent:{user_id}", item_id)
   redis.ltrim(f"recent:{user_id}", 0, 9)  # Keep last 10
""")

# Rate limiting example
print("\n📊 Rate Limiting Example:")

def check_rate_limit(user_id: str, limit: int = 5) -> tuple[bool, int]:
    """Simple rate limiter - max requests per minute"""
    key = f"ratelimit:{user_id}"
    count = redis.incr(key)
    if count == 1:
        redis.expire(key, 60)  # Reset after 1 minute
    return count <= limit, count

user = "user123"
for i in range(7):
    allowed, count = check_rate_limit(user, limit=5)
    status = "✅ Allowed" if allowed else "❌ Rate limited"
    print(f"   Request {i+1}: {status} (count: {count}/5)")

# ========== REAL REDIS CONNECTION ==========
print("\n" + "=" * 60)
print("REAL REDIS CONNECTION (Reference)")
print("=" * 60)

print("""
# Install redis-py
pip install redis

# Connect to Redis
import redis

# Local connection
r = redis.Redis(host='localhost', port=6379, db=0)

# With password
r = redis.Redis(
    host='localhost',
    port=6379,
    password='mypassword',
    decode_responses=True  # Return strings instead of bytes
)

# Connection pool (recommended for production)
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

# Basic operations
r.set('key', 'value')
r.set('key', 'value', ex=3600)  # With expiration
value = r.get('key')
r.delete('key')

# Lists
r.lpush('mylist', 'item1', 'item2')
r.rpush('mylist', 'item3')
items = r.lrange('mylist', 0, -1)

# Hashes
r.hset('user:1', 'name', 'Alice')
r.hset('user:1', 'email', 'alice@example.com')
user = r.hgetall('user:1')

# Sets
r.sadd('tags', 'python', 'redis', 'database')
tags = r.smembers('tags')

# Sorted Sets
r.zadd('leaderboard', {'alice': 100, 'bob': 85, 'charlie': 92})
top_players = r.zrevrange('leaderboard', 0, 2, withscores=True)
""")

# ========== CLEANUP ==========
print("\n" + "=" * 60)
print("CLEANUP")
print("=" * 60)

conn.close()
if os.path.exists(db_file):
    os.remove(db_file)
print("✅ Database closed and removed")

print("\n" + "=" * 60)
print("✅ Redis Caching - Complete!")
print("=" * 60)
