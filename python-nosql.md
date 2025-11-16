# NoSQL Databases in Python: Complete Guide

---

## Table of Contents
1. [Introduction to NoSQL](#introduction-to-nosql)
2. [MongoDB Basics](#mongodb-basics)
3. [pymongo Library](#pymongo-library)
4. [MongoDB Operations](#mongodb-operations)
5. [Redis Basics](#redis-basics)
6. [redis-py Library](#redis-py-library)
7. [Redis Operations](#redis-operations)
8. [Use Cases and Comparisons](#use-cases-and-comparisons)
9. [Practical Examples](#practical-examples)
10. [Best Practices](#best-practices)
11. [Performance Tips](#performance-tips)
12. [Practice Exercises](#practice-exercises)

---

## Introduction to NoSQL

### What is NoSQL?

NoSQL databases are non-relational databases designed for specific data models.

### NoSQL vs SQL

```
SQL (Relational):
├── Structured schema
├── Tables with rows/columns
├── ACID transactions
├── Complex joins
└── Examples: PostgreSQL, MySQL, SQLite

NoSQL (Non-relational):
├── Flexible schema
├── Documents, key-value, graphs
├── Eventual consistency
├── Denormalized data
└── Examples: MongoDB, Redis, Cassandra, Neo4j
```

### NoSQL Types

```
Document Store (MongoDB):
- Stores JSON-like documents
- Flexible schema
- Good for: Content management, catalogs

Key-Value Store (Redis):
- Simple key-value pairs
- In-memory or persistent
- Good for: Caching, sessions, real-time

Graph Store (Neo4j):
- Stores relationships
- Good for: Social networks, recommendations

Column-Family (Cassandra):
- Stores data in columns
- Good for: Time-series, analytics
```

---

## MongoDB Basics

### What is MongoDB?

MongoDB is a document-oriented NoSQL database that stores data in JSON-like documents.

### Installation

```bash
# Install MongoDB (local)
# macOS
brew install mongodb-community

# Ubuntu/Debian
sudo apt-get install -y mongodb-org

# Windows
# Download from https://www.mongodb.com/try/download/community

# Start MongoDB
mongod

# In another terminal, connect
mongo
```

### Document Structure

```javascript
// Example MongoDB document
{
  "_id": ObjectId("5f9a3c3f0d1e2b3c4d5e6f7g"),
  "name": "Alice",
  "email": "alice@example.com",
  "age": 25,
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "zip": "10001"
  },
  "hobbies": ["reading", "coding", "gaming"],
  "created_at": ISODate("2023-10-27T10:30:00Z")
}
```

### Collections and Databases

```
MongoDB Architecture:

Database (myapp)
├── Collection (users)
│   ├── Document
│   ├── Document
│   └── Document
├── Collection (posts)
│   ├── Document
│   └── Document
└── Collection (comments)
    └── Document

Comparison to SQL:
MongoDB → SQL
Database → Database
Collection → Table
Document → Row
Field → Column
```

---

## pymongo Library

### Installation

```bash
pip install pymongo
```

### Connection

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Get database
db = client['myapp']

# Get collection
users_collection = db['users']

# Check connection
print(client.server_info())

# Close connection
client.close()
```

### Connection String

```python
from pymongo import MongoClient

# Local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# With credentials
client = MongoClient('mongodb://username:password@localhost:27017/')

# MongoDB Atlas (cloud)
client = MongoClient(
    'mongodb+srv://username:password@cluster.mongodb.net/myapp?retryWrites=true&w=majority'
)

# Connection options
client = MongoClient(
    'mongodb://localhost:27017/',
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=10000,
    retryWrites=True
)
```

### Context Manager Pattern

```python
from pymongo import MongoClient

# Automatic connection management
with MongoClient('mongodb://localhost:27017/') as client:
    db = client['myapp']
    collection = db['users']
    # Use collection...
# Connection closes automatically
```

---

## MongoDB Operations

### Insert Operations

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['myapp']
users = db['users']

# Insert single document
result = users.insert_one({
    'name': 'Alice',
    'email': 'alice@example.com',
    'age': 25
})
print(result.inserted_id)

# Insert multiple documents
result = users.insert_many([
    {'name': 'Bob', 'email': 'bob@example.com', 'age': 30},
    {'name': 'Charlie', 'email': 'charlie@example.com', 'age': 28},
    {'name': 'Diana', 'email': 'diana@example.com', 'age': 26}
])
print(result.inserted_ids)

# Insert with custom ID
users.insert_one({
    '_id': 1,
    'name': 'Eve',
    'email': 'eve@example.com'
})
```

### Find Operations

```python
# Find all documents
all_users = users.find()
for user in all_users:
    print(user)

# Find one document
user = users.find_one({'name': 'Alice'})
print(user)

# Find by ID
from bson.objectid import ObjectId
user = users.find_one({'_id': ObjectId('...')})

# Find with conditions
users_over_25 = users.find({'age': {'$gt': 25}})

# Find with projection (select fields)
users = db['users'].find(
    {'age': {'$gt': 25}},
    {'name': 1, 'email': 1, '_id': 0}  # Only name and email
)

# Count documents
count = users.count_documents({'age': {'$gt': 25}})

# Get all as list
users_list = list(users.find())
```

### Query Operators

```python
# Comparison operators
users.find({'age': {'$eq': 25}})        # Equal
users.find({'age': {'$ne': 25}})        # Not equal
users.find({'age': {'$gt': 25}})        # Greater than
users.find({'age': {'$gte': 25}})       # Greater than or equal
users.find({'age': {'$lt': 30}})        # Less than
users.find({'age': {'$lte': 30}})       # Less than or equal

# Between
users.find({'age': {'$gte': 25, '$lte': 35}})

# In list
users.find({'status': {'$in': ['active', 'pending']}})

# Not in list
users.find({'status': {'$nin': ['deleted', 'archived']}})

# String matching
users.find({'email': {'$regex': '^alice'}})  # Starts with 'alice'

# Array contains
users.find({'hobbies': 'coding'})  # Array contains 'coding'

# Exists
users.find({'phone': {'$exists': True}})

# Type check
users.find({'age': {'$type': 'int'}})
```

### Update Operations

```python
# Update single document
result = users.update_one(
    {'name': 'Alice'},
    {'$set': {'age': 26}}
)
print(result.modified_count)

# Update multiple documents
result = users.update_many(
    {'age': {'$lt': 25}},
    {'$set': {'status': 'junior'}}
)
print(result.modified_count)

# Update operators
users.update_one(
    {'name': 'Alice'},
    {
        '$set': {'age': 26},
        '$inc': {'login_count': 1},  # Increment
        '$push': {'hobbies': 'painting'},  # Add to array
        '$pull': {'hobbies': 'gaming'}  # Remove from array
    }
)

# Replace entire document
users.replace_one(
    {'name': 'Alice'},
    {'name': 'Alice', 'email': 'newemail@example.com', 'age': 26}
)

# Upsert (update or insert)
users.update_one(
    {'email': 'new@example.com'},
    {'$set': {'name': 'NewUser', 'age': 25}},
    upsert=True  # Insert if not found
)
```

### Delete Operations

```python
# Delete single document
result = users.delete_one({'name': 'Alice'})
print(result.deleted_count)

# Delete multiple documents
result = users.delete_many({'age': {'$lt': 18}})
print(result.deleted_count)

# Delete all (be careful!)
users.delete_many({})
```

### Sorting and Limiting

```python
# Sort ascending
users.find().sort('age', 1)

# Sort descending
users.find().sort('age', -1)

# Multiple sort
users.find().sort([('department', 1), ('age', -1)])

# Limit
users.find().limit(10)

# Skip (pagination)
users.find().skip(10).limit(10)

# Pagination helper
page = 2
per_page = 10
users.find().skip((page - 1) * per_page).limit(per_page)
```

### Aggregation

```python
# Aggregation pipeline
pipeline = [
    {'$match': {'age': {'$gt': 25}}},  # Filter
    {'$group': {
        '_id': '$department',
        'count': {'$sum': 1},
        'avg_age': {'$avg': '$age'}
    }},
    {'$sort': {'count': -1}}
]

results = users.aggregate(pipeline)
for result in results:
    print(result)

# Common aggregation stages
pipeline = [
    {'$match': {...}},           # Filter
    {'$group': {...}},           # Group
    {'$sort': {...}},            # Sort
    {'$limit': 10},              # Limit
    {'$skip': 5},                # Skip
    {'$project': {...}},         # Select fields
    {'$unwind': '$array_field'}, # Expand array
]
```

---

## Redis Basics

### What is Redis?

Redis is an in-memory data structure store used for caching, sessions, and real-time applications.

### Installation

```bash
# macOS
brew install redis

# Ubuntu/Debian
sudo apt-get install redis-server

# Start Redis
redis-server

# In another terminal, connect
redis-cli
```

### Data Structures

```
Redis supports multiple data types:

Strings:
- Simple key-value pairs
- SET key value
- GET key

Lists:
- Ordered collections
- LPUSH key value
- RPOP key

Sets:
- Unordered unique collections
- SADD key member
- SMEMBERS key

Hashes:
- Key-value within key
- HSET key field value
- HGET key field

Sorted Sets:
- Ordered by score
- ZADD key score member
- ZRANGE key 0 -1
```

### Redis Commands

```bash
# String operations
SET mykey "Hello"
GET mykey
INCR counter
APPEND mykey " World"

# Expiration
SET mykey "value" EX 3600  # Expire in 1 hour
TTL mykey  # Time to live
EXPIRE mykey 3600

# List operations
LPUSH mylist "world"
LPUSH mylist "hello"
LRANGE mylist 0 -1

# Set operations
SADD myset "hello"
SADD myset "world"
SMEMBERS myset

# Hash operations
HSET myhash field1 "Hello"
HGET myhash field1
HGETALL myhash

# Sorted set operations
ZADD myzset 1 "one"
ZADD myzset 2 "two"
ZRANGE myzset 0 -1
```

---

## redis-py Library

### Installation

```bash
pip install redis
```

### Connection

```python
import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Or using connection string
r = redis.from_url('redis://localhost:6379/0')

# Test connection
print(r.ping())  # Returns True if connected

# Close connection
r.close()
```

### Context Manager

```python
import redis

with redis.Redis(host='localhost', port=6379, db=0) as r:
    r.set('mykey', 'myvalue')
    print(r.get('mykey'))
# Connection closes automatically
```

---

## Redis Operations

### String Operations

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Set and get
r.set('name', 'Alice')
value = r.get('name')
print(value)  # b'Alice' (bytes)

# Get with decode
value = r.get('name').decode('utf-8')
print(value)  # 'Alice' (string)

# Increment
r.set('counter', 0)
r.incr('counter')
r.incr('counter', 5)  # Increment by 5
print(r.get('counter'))  # 6

# Decrement
r.decr('counter')
r.decr('counter', 2)

# Set with expiration
r.setex('temp_key', 3600, 'value')  # Expires in 1 hour
r.psetex('temp_key', 60000, 'value')  # Expires in 60 seconds

# Get and set
old_value = r.getset('key', 'new_value')

# Set multiple
r.mset({'key1': 'value1', 'key2': 'value2'})
values = r.mget(['key1', 'key2'])
```

### Key Operations

```python
# Check if key exists
exists = r.exists('mykey')

# Delete key
r.delete('key1', 'key2', 'key3')

# Delete all keys (be careful!)
r.flushdb()  # Current database
r.flushall()  # All databases

# Get all keys
all_keys = r.keys('*')
keys_matching = r.keys('user:*')

# Get key type
key_type = r.type('mykey')

# Set expiration
r.expire('mykey', 3600)  # Expire in 1 hour
r.pexpire('mykey', 60000)  # Expire in milliseconds
r.persist('mykey')  # Remove expiration

# Get TTL
ttl = r.ttl('mykey')  # Seconds
pttl = r.pttl('mykey')  # Milliseconds
```

### List Operations

```python
# Push values
r.lpush('mylist', 'world')  # Left push
r.lpush('mylist', 'hello')
r.rpush('mylist', 'foo')    # Right push

# Get range
values = r.lrange('mylist', 0, -1)

# Pop values
value = r.lpop('mylist')  # Left pop
value = r.rpop('mylist')  # Right pop

# List length
length = r.llen('mylist')

# Get by index
value = r.lindex('mylist', 0)

# Set by index
r.lset('mylist', 0, 'new_value')

# Trim list
r.ltrim('mylist', 0, 10)  # Keep only first 11 elements
```

### Set Operations

```python
# Add members
r.sadd('myset', 'Alice', 'Bob', 'Charlie')

# Get all members
members = r.smembers('myset')

# Check membership
is_member = r.sismember('myset', 'Alice')

# Remove members
r.srem('myset', 'Bob')

# Set size
size = r.scard('myset')

# Union, intersection, difference
set1_members = r.sunion('set1', 'set2')
set1_members = r.sinter('set1', 'set2')
set1_members = r.sdiff('set1', 'set2')

# Pop random member
member = r.spop('myset')
```

### Hash Operations

```python
# Set field
r.hset('user:1', 'name', 'Alice')
r.hset('user:1', mapping={
    'name': 'Alice',
    'email': 'alice@example.com',
    'age': 25
})

# Get field
name = r.hget('user:1', 'name')

# Get all fields
user = r.hgetall('user:1')

# Get all field names
fields = r.hkeys('user:1')

# Get all values
values = r.hvals('user:1')

# Delete field
r.hdel('user:1', 'age')

# Check field exists
exists = r.hexists('user:1', 'name')

# Get field count
count = r.hlen('user:1')

# Increment field
r.hincrby('user:1', 'age', 1)
```

### Sorted Set Operations

```python
# Add members with score
r.zadd('scores', {'Alice': 100, 'Bob': 90, 'Charlie': 85})

# Get range
members = r.zrange('scores', 0, -1)  # By index
members = r.zrange('scores', 0, -1, withscores=True)

# Range by score
members = r.zrangebyscore('scores', 80, 100)

# Get rank
rank = r.zrank('scores', 'Alice')

# Get score
score = r.zscore('scores', 'Alice')

# Increment score
r.zincrby('scores', 5, 'Bob')

# Remove member
r.zrem('scores', 'Charlie')

# Cardinality
count = r.zcard('scores')
```

---

## Use Cases and Comparisons

### MongoDB Use Cases

```
✓ Content management systems
✓ User profiles
✓ Product catalogs
✓ Flexible schema applications
✓ Document storage

Best for:
- Complex hierarchical data
- Flexible schema requirements
- Scalable document storage
```

### Redis Use Cases

```
✓ Caching
✓ Session storage
✓ Real-time analytics
✓ Leaderboards
✓ Rate limiting
✓ Pub/Sub messaging

Best for:
- High-speed access
- Temporary data
- Real-time applications
- In-memory analytics
```

### MongoDB vs Redis

```
MongoDB:
- Persistent data storage
- Flexible schema
- Query language (MQL)
- Larger data sets
- Transactions

Redis:
- In-memory (fast)
- Simple operations
- Key-value based
- Suitable for temporary data
- Very high throughput
```

---

## Practical Examples

### MongoDB: Blog Application

```python
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['blog']

# Create collections
users = db['users']
posts = db['posts']
comments = db['comments']

# Insert user
user = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'joined': datetime.utcnow()
}
user_id = users.insert_one(user).inserted_id

# Insert post
post = {
    'title': 'Python Tips',
    'content': 'Here are some Python tips...',
    'author_id': user_id,
    'created_at': datetime.utcnow(),
    'views': 0,
    'tags': ['python', 'programming']
}
post_id = posts.insert_one(post).inserted_id

# Add comment
comment = {
    'text': 'Great post!',
    'author_id': user_id,
    'post_id': post_id,
    'created_at': datetime.utcnow()
}
comments.insert_one(comment)

# Query: Get user's posts
user_posts = posts.find({'author_id': user_id})

# Query: Get post with comments
pipeline = [
    {'$match': {'_id': post_id}},
    {'$lookup': {
        'from': 'comments',
        'localField': '_id',
        'foreignField': 'post_id',
        'as': 'comments'
    }}
]
result = list(posts.aggregate(pipeline))

# Increment views
posts.update_one(
    {'_id': post_id},
    {'$inc': {'views': 1}}
)
```

### Redis: Caching and Sessions

```python
import redis
import json
from datetime import datetime, timedelta

r = redis.Redis(host='localhost', port=6379, db=0)

# Cache user data
user_id = 1
user_data = {
    'id': user_id,
    'name': 'Alice',
    'email': 'alice@example.com'
}

# Set with expiration (1 hour)
r.setex(
    f'user:{user_id}',
    3600,
    json.dumps(user_data)
)

# Get cached user
cached_user = r.get(f'user:{user_id}')
if cached_user:
    user_data = json.loads(cached_user)

# Session storage
session_id = 'sess_abc123'
session_data = {
    'user_id': user_id,
    'login_time': datetime.now().isoformat()
}

r.setex(
    f'session:{session_id}',
    1800,  # 30 minutes
    json.dumps(session_data)
)

# Rate limiting
ip = '192.168.1.1'
key = f'rate_limit:{ip}'

# Check rate limit
if r.incr(key) == 1:
    r.expire(key, 60)  # Reset after 60 seconds

if r.get(key) and int(r.get(key)) > 100:
    print("Rate limit exceeded")

# Leaderboard
r.zadd('leaderboard', {
    'Alice': 1000,
    'Bob': 900,
    'Charlie': 850
})

# Get top 10
top_10 = r.zrevrange('leaderboard', 0, 9, withscores=True)
for player, score in top_10:
    print(f"{player}: {score}")
```

---

## Best Practices

### MongoDB

```python
# ✓ GOOD - Use indexes
db['users'].create_index('email')

# ✓ GOOD - Connection pooling
from pymongo import MongoClient
client = MongoClient(
    'mongodb://localhost:27017/',
    maxPoolSize=50
)

# ✓ GOOD - Error handling
try:
    result = users.insert_one(document)
except Exception as e:
    print(f"Insert failed: {e}")

# ✓ GOOD - Transactions
session = client.start_session()
with session.start_transaction():
    users.insert_one(user_doc, session=session)
    posts.insert_one(post_doc, session=session)
```

### Redis

```python
# ✓ GOOD - Use keys strategically
r.set(f'user:{user_id}:name', name)
r.set(f'session:{session_id}', session_data)

# ✓ GOOD - Use expiration
r.setex('temporary_key', 3600, 'value')

# ✓ GOOD - Connection pooling
pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    max_connections=50
)
r = redis.Redis(connection_pool=pool)

# ✓ GOOD - Pipeline for multiple commands
pipe = r.pipeline()
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
pipe.execute()
```

---

## Performance Tips

### MongoDB

```python
# Use projection to reduce data transfer
users.find(
    {'age': {'$gt': 25}},
    {'name': 1, 'email': 1}  # Only these fields
)

# Use appropriate indexes
db['users'].create_index([('email', 1)])
db['users'].create_index([('age', 1), ('name', 1)])

# Batch operations
users.insert_many([doc1, doc2, doc3])  # Better than insert_one multiple times

# Use aggregation for complex queries
pipeline = [...]
users.aggregate(pipeline)
```

### Redis

```python
# Use pipeline for multiple commands
pipe = r.pipeline()
for i in range(1000):
    pipe.set(f'key:{i}', f'value:{i}')
pipe.execute()

# Use appropriate data types
# Strings for simple values
r.set('counter', 1)

# Hashes for related fields
r.hset('user:1', mapping={'name': 'Alice', 'email': 'alice@example.com'})

# Sets for unique collections
r.sadd('users_online', 'alice', 'bob')

# Sorted sets for rankings
r.zadd('leaderboard', {'alice': 100, 'bob': 90})
```

---

## Practice Exercises

### 1. MongoDB
- Create database and collections
- Insert, update, delete documents
- Complex queries with aggregation
- Indexing for performance

### 2. Redis
- String operations and caching
- List and set operations
- Hash operations for objects
- Sorted sets for rankings

### 3. Real-World Projects
- Blog with MongoDB (posts, comments, users)
- Caching layer with Redis
- Session management
- Rate limiting
- Leaderboard system

### 4. Integration
- MongoDB for persistent storage
- Redis for caching
- Combined architecture

---

# End of Notes
