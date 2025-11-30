# Day 18 Quick Reference Cheat Sheet

## PostgreSQL Connection
```python
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Always close
cursor.close()
conn.close()
```

## SQLite (Lightweight Alternative)
```python
import sqlite3

# Connect (creates file if not exists)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Use with context manager (auto-closes)
with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
```

## Database Relationships

### One-to-Many
```sql
-- Parent table (one)
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Child table (many)
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);
```

### Many-to-Many
```sql
-- Junction/Bridge table
CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    enrolled_date DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

## JOIN Queries
```sql
-- INNER JOIN (matching records only)
SELECT books.title, authors.name
FROM books
INNER JOIN authors ON books.author_id = authors.id;

-- LEFT JOIN (all from left + matches)
SELECT authors.name, books.title
FROM authors
LEFT JOIN books ON authors.id = books.author_id;

-- Multiple JOINs
SELECT s.name, c.course_name
FROM students s
JOIN student_courses sc ON s.id = sc.student_id
JOIN courses c ON sc.course_id = c.id;
```

## Query Optimization

### EXPLAIN Analysis
```sql
-- Show query plan
EXPLAIN QUERY PLAN
SELECT * FROM users WHERE email = 'test@example.com';

-- PostgreSQL style
EXPLAIN ANALYZE
SELECT * FROM users WHERE email = 'test@example.com';
```

### Creating Indexes
```sql
-- Single column index
CREATE INDEX idx_users_email ON users(email);

-- Composite index
CREATE INDEX idx_orders_user_date 
ON orders(user_id, order_date);

-- Unique index
CREATE UNIQUE INDEX idx_users_email_unique 
ON users(email);
```

### N+1 Problem & Solutions
```python
# ❌ BAD: N+1 queries
authors = cursor.execute("SELECT * FROM authors")
for author in authors:
    # Executes N additional queries!
    books = cursor.execute(
        "SELECT * FROM books WHERE author_id = ?", 
        (author[0],)
    )

# ✅ GOOD: Single JOIN query
query = """
    SELECT authors.*, books.title
    FROM authors
    LEFT JOIN books ON authors.id = books.author_id
"""
cursor.execute(query)
```

### Pagination
```sql
-- Offset-based (simple, slower for large offsets)
SELECT * FROM users
ORDER BY id
LIMIT 10 OFFSET 20;

-- Cursor-based (faster for large datasets)
SELECT * FROM users
WHERE id > 100  -- last seen ID
ORDER BY id
LIMIT 10;
```

## MongoDB Basics
```python
from pymongo import MongoClient

# Connect
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["users"]

# Insert
collection.insert_one({"name": "Alice", "age": 25})
collection.insert_many([{"name": "Bob"}, {"name": "Charlie"}])

# Query
user = collection.find_one({"name": "Alice"})
users = collection.find({"age": {"$gt": 18}})

# Update
collection.update_one(
    {"name": "Alice"}, 
    {"$set": {"age": 26}}
)

# Delete
collection.delete_one({"name": "Bob"})
```

## MongoDB Query Operators
```python
# Comparison
{"age": {"$gt": 18}}   # Greater than
{"age": {"$gte": 18}}  # Greater or equal
{"age": {"$lt": 65}}   # Less than
{"age": {"$in": [20, 25, 30]}}  # In list

# Logical
{"$and": [{"age": {"$gt": 18}}, {"city": "NYC"}]}
{"$or": [{"status": "active"}, {"role": "admin"}]}

# Array
{"tags": {"$all": ["python", "mongodb"]}}
{"skills": {"$size": 3}}
```

## Redis Caching
```python
import redis

# Connect
r = redis.Redis(host='localhost', port=6379, db=0)

# String operations
r.set("key", "value")
r.set("key", "value", ex=3600)  # Expires in 1 hour
value = r.get("key")

# Check existence
r.exists("key")

# Delete
r.delete("key")

# TTL (time to live)
r.ttl("key")
r.expire("key", 300)  # 5 minutes
```

## Cache-Aside Pattern
```python
def get_user(user_id):
    # Check cache first
    cached = redis.get(f"user:{user_id}")
    if cached:
        return json.loads(cached)
    
    # Miss - fetch from database
    user = db.execute(
        "SELECT * FROM users WHERE id = ?", 
        (user_id,)
    ).fetchone()
    
    # Store in cache
    redis.set(
        f"user:{user_id}", 
        json.dumps(user), 
        ex=3600
    )
    return user
```

## SQL vs NoSQL Decision Guide
```
Use SQL (PostgreSQL/SQLite) when:
✓ Data has clear relationships
✓ Need ACID transactions
✓ Complex queries with JOINs
✓ Data structure is stable

Use MongoDB when:
✓ Flexible/evolving schema
✓ Document-like data (JSON)
✓ Horizontal scaling needed
✓ Hierarchical data

Use Redis when:
✓ Caching frequently accessed data
✓ Session storage
✓ Real-time analytics
✓ Message queues
```

## Common Patterns

### Connection Pool
```python
from psycopg2 import pool

# Create pool
conn_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host="localhost",
    database="mydb"
)

# Get connection
conn = conn_pool.getconn()

# Return connection to pool
conn_pool.putconn(conn)
```

### Transaction Management
```python
try:
    cursor.execute("BEGIN")
    cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    conn.commit()
except Exception:
    conn.rollback()
    raise
```

---
**Keep this handy for Day 18 topics!** 🚀
