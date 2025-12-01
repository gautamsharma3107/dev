"""
DAY 18 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 18 ASSESSMENT - Database Advanced Topics")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What type of relationship requires a junction/bridge table?
a) One-to-One
b) One-to-Many
c) Many-to-Many
d) Self-referencing

Your answer: """)

print("""
Q2. Which SQL keyword is used to analyze query execution plans?
a) ANALYZE
b) EXPLAIN
c) DEBUG
d) PROFILE

Your answer: """)

print("""
Q3. What is the main purpose of database indexes?
a) Store backup copies of data
b) Speed up data retrieval
c) Encrypt sensitive data
d) Compress table size

Your answer: """)

print("""
Q4. In MongoDB, what is a "document"?
a) A text file
b) A JSON-like record (similar to a row in SQL)
c) A database schema
d) An index configuration

Your answer: """)

print("""
Q5. What does TTL stand for in Redis caching?
a) Time To Load
b) Time To Live
c) Total Transfer Length
d) Temporary Table Lock

Your answer: """)

print("""
Q6. What is the N+1 query problem?
a) Having N+1 tables in a database
b) Making 1 initial query plus N additional queries in a loop
c) Having N+1 indexes on a table
d) A database with more than N+1 connections

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write SQL to create a "comments" table with a 
    foreign key to "posts" table (one-to-many relationship).
    Include CASCADE on delete.
""")

# Write your SQL here:



print("""
Q8. (2 points) Write a SQL query using JOIN to get all posts 
    with their author's name, sorted by post date descending.
    Tables: posts(id, title, author_id, created_at), 
            authors(id, name)
""")

# Write your SQL here:



print("""
Q9. (2 points) Write Python code to implement the cache-aside 
    pattern. Function should:
    1. Check cache first
    2. If miss, fetch from database
    3. Store result in cache with TTL
""")

# Write your code here:
# def get_user_cached(user_id):
#     ...



# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) When would you choose MongoDB over PostgreSQL?
     Give two specific scenarios with brief explanations.

Your answer:
""")

# Write your explanation here as comments:
#



print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: c) Many-to-Many
    - Junction tables store the relationships between two tables
    
Q2: b) EXPLAIN
    - EXPLAIN QUERY PLAN shows how the database executes a query
    
Q3: b) Speed up data retrieval
    - Indexes create data structures for faster lookups
    
Q4: b) A JSON-like record (similar to a row in SQL)
    - MongoDB documents are BSON (binary JSON) objects
    
Q5: b) Time To Live
    - TTL defines how long a cached value remains valid
    
Q6: b) Making 1 initial query plus N additional queries in a loop
    - This happens when fetching related data in a loop

Section B:

Q7:
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

Q8:
SELECT posts.title, posts.created_at, authors.name
FROM posts
JOIN authors ON posts.author_id = authors.id
ORDER BY posts.created_at DESC;

-- Or with aliases:
SELECT p.title, p.created_at, a.name as author_name
FROM posts p
INNER JOIN authors a ON p.author_id = a.id
ORDER BY p.created_at DESC;

Q9:
def get_user_cached(user_id):
    cache_key = f"user:{user_id}"
    
    # Check cache first
    cached = redis.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Cache miss - fetch from database
    user = db.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()
    
    if user:
        # Store in cache with TTL (e.g., 5 minutes)
        redis.set(cache_key, json.dumps(user), ex=300)
    
    return user

Section C:

Q10: Choose MongoDB over PostgreSQL when:

1. Flexible/Evolving Schema:
   - When your data structure changes frequently
   - Example: Content management systems where each document
     type may have different fields
   - MongoDB doesn't require migrations for schema changes

2. Document-Centric Data:
   - When data is naturally hierarchical/nested (JSON-like)
   - Example: Product catalogs with varying attributes per category
   - MongoDB stores nested data in single documents efficiently

Other valid scenarios:
- Rapid prototyping (no schema design upfront)
- Horizontal scaling requirements
- Real-time analytics on diverse data
- IoT data with varying sensor types
"""
