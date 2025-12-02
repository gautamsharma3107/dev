"""
Caching Strategies
==================
Day 37 - System Design Basics

Learn how to implement effective caching for better performance.
"""

# ============================================================
# 1. CACHING FUNDAMENTALS
# ============================================================

"""
What is Caching?

Caching stores copies of data in a faster storage layer
to reduce the time needed to access that data.

Benefits:
- Faster response times
- Reduced database load
- Lower latency
- Better user experience
- Cost savings

Cache Hit: Data found in cache
Cache Miss: Data not in cache, must fetch from source
"""

# ============================================================
# 2. CACHING LAYERS
# ============================================================

"""
Caching Layers (from fastest to slowest):

1. Browser Cache
   - Static assets (JS, CSS, images)
   - Controlled by HTTP headers

2. CDN (Content Delivery Network)
   - Geographically distributed
   - Static and dynamic content

3. Application Cache
   - In-memory (Redis, Memcached)
   - Session data, API responses

4. Database Cache
   - Query cache
   - Buffer pool

5. Disk Cache
   - SSD vs HDD
   - OS-level caching
"""

# ============================================================
# 3. CACHING STRATEGIES
# ============================================================

"""
Common Caching Strategies:

1. Cache-Aside (Lazy Loading)
   - Application manages cache
   - Check cache first, then database
   - Update cache on miss

2. Write-Through
   - Write to cache and database simultaneously
   - Cache always up to date
   - Slower writes

3. Write-Behind (Write-Back)
   - Write to cache first
   - Async write to database
   - Risk of data loss

4. Read-Through
   - Cache sits between app and database
   - Cache handles fetching
   - Simplified application code

5. Refresh-Ahead
   - Proactively refresh cache
   - Before expiration
   - Complex to implement
"""

# Cache-Aside Implementation
class CacheAside:
    """
    Cache-Aside (Lazy Loading) Pattern
    
    1. Check cache
    2. If miss, get from DB
    3. Store in cache
    4. Return data
    """
    
    def __init__(self, cache, database):
        self.cache = cache  # Redis/Memcached client
        self.database = database  # DB connection
    
    def get_user(self, user_id):
        # Step 1: Check cache
        cache_key = f"user:{user_id}"
        cached_data = self.cache.get(cache_key)
        
        if cached_data:
            print(f"Cache HIT for user:{user_id}")
            return cached_data
        
        # Step 2: Cache miss - get from database
        print(f"Cache MISS for user:{user_id}")
        user = self.database.query(f"SELECT * FROM users WHERE id = {user_id}")
        
        if user:
            # Step 3: Store in cache with TTL
            self.cache.setex(cache_key, 3600, user)  # 1 hour TTL
        
        return user
    
    def update_user(self, user_id, data):
        # Update database
        self.database.execute(f"UPDATE users SET ... WHERE id = {user_id}")
        
        # Invalidate cache
        cache_key = f"user:{user_id}"
        self.cache.delete(cache_key)
        
        return True

# Write-Through Implementation
class WriteThrough:
    """
    Write-Through Pattern
    
    Write to both cache and database simultaneously
    """
    
    def __init__(self, cache, database):
        self.cache = cache
        self.database = database
    
    def save_user(self, user_id, data):
        # Write to database
        self.database.execute(f"INSERT INTO users ...")
        
        # Write to cache
        cache_key = f"user:{user_id}"
        self.cache.setex(cache_key, 3600, data)
        
        return True
    
    def get_user(self, user_id):
        # Always check cache first
        cache_key = f"user:{user_id}"
        return self.cache.get(cache_key)

# ============================================================
# 4. CACHE INVALIDATION
# ============================================================

"""
Cache Invalidation Strategies:

1. Time-based (TTL)
   - Data expires after set time
   - Simple but may serve stale data

2. Event-based
   - Invalidate on data change
   - More accurate but complex

3. Version-based
   - Include version in cache key
   - user:123:v2

Common Patterns:
- Invalidate on write
- Publish-Subscribe for distributed systems
- Write-through invalidation
"""

class CacheInvalidation:
    """Different cache invalidation approaches"""
    
    def __init__(self, cache):
        self.cache = cache
    
    # Time-based invalidation
    def cache_with_ttl(self, key, value, ttl_seconds=3600):
        """Cache with automatic expiration"""
        self.cache.setex(key, ttl_seconds, value)
    
    # Event-based invalidation
    def invalidate_on_update(self, user_id):
        """Invalidate cache when data changes"""
        # Delete user cache
        self.cache.delete(f"user:{user_id}")
        
        # Delete related caches
        self.cache.delete(f"user:{user_id}:orders")
        self.cache.delete(f"user:{user_id}:profile")
        
        # Delete list caches that might contain this user
        self.cache.delete("users:list")
    
    # Version-based invalidation
    def cache_with_version(self, user_id, data, version):
        """Cache with version in key"""
        key = f"user:{user_id}:v{version}"
        self.cache.set(key, data)
        
        # Store current version
        self.cache.set(f"user:{user_id}:version", version)
    
    def get_with_version(self, user_id):
        """Get data with version check"""
        version = self.cache.get(f"user:{user_id}:version")
        if version:
            key = f"user:{user_id}:v{version}"
            return self.cache.get(key)
        return None

# ============================================================
# 5. REDIS CACHING EXAMPLE
# ============================================================

"""
Redis Caching Commands:

SET key value               - Set string value
GET key                     - Get string value
SETEX key seconds value     - Set with expiration
DEL key                     - Delete key
EXISTS key                  - Check if key exists
EXPIRE key seconds          - Set expiration
TTL key                     - Get remaining time
KEYS pattern                - Find keys matching pattern
HSET key field value        - Set hash field
HGET key field              - Get hash field
HGETALL key                 - Get all hash fields
LPUSH key value             - Push to list
LRANGE key start stop       - Get list range
SADD key member             - Add to set
SMEMBERS key                - Get all set members
"""

# Python Redis Example
redis_example = '''
import redis
import json
from datetime import timedelta

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class RedisCache:
    def __init__(self):
        self.redis = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
    
    # String caching
    def cache_string(self, key, value, ttl=3600):
        """Cache a simple string value"""
        self.redis.setex(key, ttl, value)
    
    def get_string(self, key):
        """Get cached string"""
        return self.redis.get(key)
    
    # Object caching (JSON)
    def cache_object(self, key, obj, ttl=3600):
        """Cache a Python object as JSON"""
        self.redis.setex(key, ttl, json.dumps(obj))
    
    def get_object(self, key):
        """Get cached object"""
        data = self.redis.get(key)
        return json.loads(data) if data else None
    
    # Hash caching (for objects with fields)
    def cache_user(self, user_id, user_data):
        """Cache user data as hash"""
        key = f"user:{user_id}"
        self.redis.hset(key, mapping=user_data)
        self.redis.expire(key, 3600)
    
    def get_user(self, user_id):
        """Get cached user hash"""
        key = f"user:{user_id}"
        return self.redis.hgetall(key)
    
    # List caching
    def cache_recent_items(self, key, items, max_items=100):
        """Cache a list of recent items"""
        pipe = self.redis.pipeline()
        for item in items:
            pipe.lpush(key, json.dumps(item))
        pipe.ltrim(key, 0, max_items - 1)
        pipe.expire(key, 3600)
        pipe.execute()
    
    def get_recent_items(self, key, count=10):
        """Get recent items from list"""
        items = self.redis.lrange(key, 0, count - 1)
        return [json.loads(item) for item in items]
    
    # Cache decorator
    def cached(self, ttl=3600):
        """Decorator to cache function results"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Create cache key from function name and arguments
                key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
                
                # Check cache
                cached = self.redis.get(key)
                if cached:
                    return json.loads(cached)
                
                # Call function
                result = func(*args, **kwargs)
                
                # Cache result
                self.redis.setex(key, ttl, json.dumps(result))
                
                return result
            return wrapper
        return decorator

# Usage Example
cache = RedisCache()

@cache.cached(ttl=300)
def get_expensive_data(user_id):
    """This result will be cached for 5 minutes"""
    # Expensive database query or computation
    return {"user_id": user_id, "data": "expensive result"}
'''

# ============================================================
# 6. HTTP CACHING
# ============================================================

"""
HTTP Caching Headers:

1. Cache-Control
   - max-age=3600: Cache for 1 hour
   - no-cache: Validate before use
   - no-store: Don't cache at all
   - private: Only browser can cache
   - public: Anyone can cache (CDN)

2. ETag
   - Unique identifier for resource version
   - Used for conditional requests

3. Last-Modified
   - When resource was last changed
   - Used with If-Modified-Since

4. Expires
   - Specific expiration date/time
   - Legacy, prefer Cache-Control
"""

http_cache_headers = {
    # Cache for 1 hour, allow CDN caching
    "public_resource": {
        "Cache-Control": "public, max-age=3600",
        "ETag": '"abc123"'
    },
    
    # Private data, cache for 5 minutes
    "private_resource": {
        "Cache-Control": "private, max-age=300",
        "ETag": '"user-specific-123"'
    },
    
    # Don't cache at all
    "no_cache": {
        "Cache-Control": "no-store, no-cache, must-revalidate"
    },
    
    # Validate every time
    "must_validate": {
        "Cache-Control": "no-cache",
        "ETag": '"version-456"'
    }
}

# FastAPI Caching Example
fastapi_caching = '''
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/products")
async def get_products(response: Response):
    products = fetch_products()  # Get from DB
    
    # Set cache headers
    response.headers["Cache-Control"] = "public, max-age=3600"
    response.headers["ETag"] = generate_etag(products)
    
    return products

@app.get("/user/profile")
async def get_profile(response: Response):
    profile = fetch_user_profile()
    
    # Private cache only
    response.headers["Cache-Control"] = "private, max-age=300"
    
    return profile

@app.get("/auth/session")
async def get_session(response: Response):
    # Never cache authentication data
    response.headers["Cache-Control"] = "no-store"
    
    return {"session": "data"}
'''

# ============================================================
# 7. CACHING BEST PRACTICES
# ============================================================

"""
Caching Best Practices:

1. Cache the Right Data
   - Frequently accessed
   - Expensive to compute
   - Rarely changes

2. Choose Appropriate TTL
   - Balance freshness vs performance
   - Critical data: shorter TTL
   - Static data: longer TTL

3. Handle Cache Failures Gracefully
   - Don't fail if cache is down
   - Fall back to database

4. Monitor Cache Performance
   - Hit rate (should be >90%)
   - Miss rate
   - Memory usage
   - Latency

5. Prevent Cache Stampede
   - Use locks for expensive computations
   - Stagger TTL with jitter

6. Use Appropriate Key Names
   - Namespace keys (user:123:profile)
   - Include version if needed
   - Keep keys readable

7. Don't Cache Everything
   - Personalized data might not cache well
   - Real-time data shouldn't be cached
   - Small, fast queries might not benefit
"""

# Cache Stampede Prevention
class CacheStampede:
    """Prevent cache stampede with locking"""
    
    def __init__(self, cache):
        self.cache = cache
        self.lock_timeout = 10  # seconds
    
    def get_with_lock(self, key, compute_func, ttl=3600):
        """Get data with lock to prevent stampede"""
        
        # Try to get from cache
        data = self.cache.get(key)
        if data:
            return data
        
        # Try to acquire lock
        lock_key = f"{key}:lock"
        if self.cache.set(lock_key, "locked", nx=True, ex=self.lock_timeout):
            try:
                # We have the lock, compute and cache
                data = compute_func()
                self.cache.setex(key, ttl, data)
                return data
            finally:
                # Release lock
                self.cache.delete(lock_key)
        else:
            # Someone else is computing, wait and retry
            import time
            time.sleep(0.1)
            return self.get_with_lock(key, compute_func, ttl)

# TTL with Jitter
import random

def ttl_with_jitter(base_ttl, jitter_percent=10):
    """Add random jitter to TTL to prevent synchronized expiration"""
    jitter = base_ttl * (jitter_percent / 100)
    return base_ttl + random.uniform(-jitter, jitter)

# Example: base_ttl=3600, could return 3240-3960

# ============================================================
# 8. CACHING PATTERNS
# ============================================================

"""
Common Caching Patterns:

1. Memoization
   - Cache function results
   - Same inputs = same output

2. Object Cache
   - Cache entire objects
   - user:123 -> {name, email, ...}

3. Query Cache
   - Cache query results
   - products:category:electronics

4. Fragment Cache
   - Cache parts of pages
   - Sidebar, navigation, etc.

5. Session Cache
   - Store user sessions
   - Faster than database

6. Rate Limiting Cache
   - Track request counts
   - user:123:requests:minute
"""

# Memoization Pattern
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    """Memoized fibonacci - results cached in memory"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Query Cache Pattern
class QueryCache:
    """Cache database query results"""
    
    def __init__(self, cache, db):
        self.cache = cache
        self.db = db
    
    def get_products_by_category(self, category, page=1, per_page=20):
        # Create cache key
        cache_key = f"products:category:{category}:page:{page}:size:{per_page}"
        
        # Check cache
        cached = self.cache.get(cache_key)
        if cached:
            return cached
        
        # Query database
        products = self.db.query("""
            SELECT * FROM products 
            WHERE category = %s 
            LIMIT %s OFFSET %s
        """, (category, per_page, (page-1) * per_page))
        
        # Cache with shorter TTL for list queries
        self.cache.setex(cache_key, 300, products)  # 5 minutes
        
        return products
    
    def invalidate_category(self, category):
        """Invalidate all cached pages for a category"""
        pattern = f"products:category:{category}:*"
        keys = self.cache.keys(pattern)
        if keys:
            self.cache.delete(*keys)

# ============================================================
# 9. DISTRIBUTED CACHING
# ============================================================

"""
Distributed Caching Considerations:

1. Consistent Hashing
   - Distribute keys across nodes
   - Minimize redistribution on node changes

2. Replication
   - Master-slave for read scaling
   - Master-master for write scaling

3. Cluster Mode
   - Redis Cluster
   - Automatic sharding

4. Cache Coherence
   - Keep all caches in sync
   - Use pub/sub for invalidation
"""

# Redis Cluster Example
redis_cluster_example = '''
from redis.cluster import RedisCluster

# Connect to Redis Cluster
rc = RedisCluster(
    startup_nodes=[
        {"host": "127.0.0.1", "port": 7000},
        {"host": "127.0.0.1", "port": 7001},
        {"host": "127.0.0.1", "port": 7002}
    ],
    decode_responses=True
)

# Use like regular Redis
rc.set("key", "value")
rc.get("key")
'''

# Pub/Sub for Cache Invalidation
pubsub_example = '''
import redis
import threading

r = redis.Redis()

def cache_invalidation_listener():
    """Listen for cache invalidation messages"""
    pubsub = r.pubsub()
    pubsub.subscribe('cache_invalidation')
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            key = message['data']
            # Invalidate local cache
            local_cache.pop(key, None)
            print(f"Invalidated cache key: {key}")

# Start listener in background
thread = threading.Thread(target=cache_invalidation_listener)
thread.daemon = True
thread.start()

# Publish invalidation from any server
def invalidate_cache(key):
    r.delete(key)  # Delete from Redis
    r.publish('cache_invalidation', key)  # Notify all servers
'''

# ============================================================
# SUMMARY
# ============================================================

"""
Caching Summary:

1. Strategies:
   - Cache-Aside (most common)
   - Write-Through
   - Write-Behind
   - Read-Through

2. Invalidation:
   - TTL-based
   - Event-based
   - Version-based

3. Tools:
   - Redis (most popular)
   - Memcached
   - In-memory (lru_cache)

4. Best Practices:
   - Cache frequently accessed data
   - Set appropriate TTLs
   - Handle failures gracefully
   - Monitor hit rates
   - Prevent cache stampede
"""

if __name__ == "__main__":
    print("Caching Strategies")
    print("=" * 50)
    
    print("\nCaching Strategies:")
    print("1. Cache-Aside (Lazy Loading)")
    print("2. Write-Through")
    print("3. Write-Behind")
    print("4. Read-Through")
    
    print("\nCache Invalidation:")
    print("- TTL-based (automatic expiration)")
    print("- Event-based (invalidate on change)")
    print("- Version-based (include version in key)")
    
    print("\nBest Practices:")
    print("- Cache frequently accessed data")
    print("- Use appropriate TTLs")
    print("- Handle cache failures gracefully")
    print("- Monitor cache hit rates")
