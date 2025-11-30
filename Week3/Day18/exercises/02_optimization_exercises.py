"""
Day 18 - Optimization Exercises
===============================
Practice: Indexes, EXPLAIN, and query optimization

Complete each exercise to practice query optimization.
"""

import sqlite3
import os
import time

print("=" * 60)
print("DAY 18 EXERCISES: Query Optimization")
print("=" * 60)

# Setup database with sample data
db_file = "optimization_exercises.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create and populate a larger table for optimization exercises
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE,
    city TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert sample data
import random
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
          "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

users = []
for i in range(10000):
    users.append((f"user_{i}", f"user{i}@email.com", random.choice(cities)))

cursor.executemany(
    "INSERT INTO users (username, email, city) VALUES (?, ?, ?)",
    users
)
conn.commit()
print(f"✅ Created 10,000 users for testing\n")

# ============================================================
# EXERCISE 1: Analyze Query Without Index
# ============================================================

print("=" * 60)
print("EXERCISE 1: Analyze query plan without index")
print("=" * 60)
print("Task: Run EXPLAIN QUERY PLAN on a city filter query")
print()

# TODO: Run EXPLAIN QUERY PLAN on this query
query = "SELECT * FROM users WHERE city = 'Chicago'"

print("Run: EXPLAIN QUERY PLAN " + query)
print("What do you see? SCAN or SEARCH?")
print()

# Your code here:
# cursor.execute("EXPLAIN QUERY PLAN " + query)
# for row in cursor.fetchall():
#     print(row)

# ============================================================
# EXERCISE 2: Create an Index
# ============================================================

print("=" * 60)
print("EXERCISE 2: Create an index on city column")
print("=" * 60)
print("Task: Create index and compare query plan")
print()

# TODO: Create index
# cursor.execute("CREATE INDEX ...")

# TODO: Run EXPLAIN again - what changed?

# ============================================================
# EXERCISE 3: Measure Performance Improvement
# ============================================================

print("=" * 60)
print("EXERCISE 3: Measure query performance")
print("=" * 60)
print("Task: Time queries before and after indexing")
print()

def time_query(cursor, query, runs=100):
    """Time a query execution"""
    start = time.time()
    for _ in range(runs):
        cursor.execute(query)
        cursor.fetchall()
    return (time.time() - start) / runs * 1000  # ms

# TODO: Time query on non-indexed column (username)
# TODO: Time query on indexed column (city)
# Compare the results!

# ============================================================
# EXERCISE 4: Composite Index
# ============================================================

print("=" * 60)
print("EXERCISE 4: Create composite index")
print("=" * 60)
print("Task: Create index for multi-column queries")
print()

# Common query pattern:
# SELECT * FROM users WHERE city = 'Chicago' ORDER BY created_at DESC

# TODO: Create composite index on (city, created_at)
# cursor.execute("CREATE INDEX ...")

# ============================================================
# EXERCISE 5: Identify N+1 Problem
# ============================================================

print("=" * 60)
print("EXERCISE 5: Fix N+1 query problem")
print("=" * 60)

# Create orders table
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount REAL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

# Insert sample orders
orders = [(random.randint(1, 1000), random.uniform(10, 100)) for _ in range(500)]
cursor.executemany("INSERT INTO orders (user_id, amount) VALUES (?, ?)", orders)
conn.commit()

print("Task: Rewrite this N+1 pattern as a single JOIN query")
print()
print("BAD (N+1):")
print('''
users = cursor.execute("SELECT id, username FROM users LIMIT 10")
for user in users:
    orders = cursor.execute(
        "SELECT * FROM orders WHERE user_id = ?", 
        (user[0],)
    )
    # Process orders...
''')
print()
print("TODO: Write a single JOIN query to get users with their orders")

# Your solution here:
# query = """
#     SELECT ...
# """

# ============================================================
# SOLUTIONS
# ============================================================

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)
print()

# SOLUTION 1
print("SOLUTION 1: Query plan without index")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM users WHERE city = 'Chicago'")
print("Before index:")
for row in cursor.fetchall():
    print(f"  {row}")
print()

# SOLUTION 2
print("SOLUTION 2: Create index and compare")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_city ON users(city)")
conn.commit()
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM users WHERE city = 'Chicago'")
print("After index:")
for row in cursor.fetchall():
    print(f"  {row}")
print()

# SOLUTION 3
print("SOLUTION 3: Performance comparison")

# Query on indexed column
time_indexed = time_query(cursor, "SELECT * FROM users WHERE city = 'Chicago'")
print(f"Query on indexed column (city): {time_indexed:.3f} ms")

# Query on non-indexed column
time_not_indexed = time_query(cursor, "SELECT * FROM users WHERE username = 'user_500'")
print(f"Query on non-indexed column (username): {time_not_indexed:.3f} ms")
print()

# SOLUTION 4
print("SOLUTION 4: Composite index")
cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_users_city_created 
    ON users(city, created_at)
""")
conn.commit()
print("Created composite index: idx_users_city_created ON (city, created_at)")
cursor.execute("""
    EXPLAIN QUERY PLAN 
    SELECT * FROM users WHERE city = 'Chicago' ORDER BY created_at DESC
""")
print("Query plan with composite index:")
for row in cursor.fetchall():
    print(f"  {row}")
print()

# SOLUTION 5
print("SOLUTION 5: Fix N+1 with JOIN")
print("Single JOIN query:")
query = """
    SELECT u.id, u.username, o.id as order_id, o.amount
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.id <= 10
    ORDER BY u.id, o.id
"""
print(query)
cursor.execute(query)
results = cursor.fetchall()
print(f"\nReturns {len(results)} rows with a single query!")
print("Sample results:")
for row in results[:5]:
    amount = row[3] if row[3] is not None else 0
    print(f"  User {row[0]} ({row[1]}): Order {row[2]} - ${amount:.2f}")

# Cleanup
conn.close()
if os.path.exists(db_file):
    os.remove(db_file)
print("\n✅ Exercises complete! Database cleaned up.")
