"""
Day 18 - Query Optimization
===========================
Learn: EXPLAIN, Indexing, N+1 Problem, Pagination

Key Concepts:
- Analyzing queries with EXPLAIN
- Creating and using indexes
- Understanding the N+1 problem
- Efficient pagination strategies
"""

import sqlite3
import os
import time
import random
import string

# ========== INTRODUCTION ==========
print("=" * 60)
print("QUERY OPTIMIZATION BASICS")
print("=" * 60)

print("""
Why Query Optimization Matters:
- Slow queries = Poor user experience
- Inefficient queries = High server costs
- Bad design = Database bottlenecks

Key Optimization Techniques:
1. Use EXPLAIN to analyze queries
2. Add indexes for frequently queried columns
3. Avoid N+1 query patterns
4. Use efficient pagination
5. Select only needed columns
""")

# Setup database with sample data
db_file = "optimization.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
print(f"✅ Connected to {db_file}")

# ========== CREATE TEST DATA ==========
print("\n" + "=" * 60)
print("CREATING TEST DATA")
print("=" * 60)

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS customers")

# Create tables
cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT
)
""")

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    order_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

# Generate sample data
print("Generating sample data...")

# Generate customers
customers = []
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
for i in range(1000):
    name = f"Customer_{i}"
    email = f"customer{i}@example.com"
    city = random.choice(cities)
    customers.append((name, email, city))

cursor.executemany(
    "INSERT INTO customers (name, email, city) VALUES (?, ?, ?)",
    customers
)

# Generate products
products = []
categories = ["Electronics", "Clothing", "Books", "Home", "Sports"]
for i in range(500):
    name = f"Product_{i}"
    price = round(random.uniform(10, 500), 2)
    category = random.choice(categories)
    products.append((name, price, category))

cursor.executemany(
    "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
    products
)

# Generate orders
orders = []
for i in range(5000):
    customer_id = random.randint(1, 1000)
    product_id = random.randint(1, 500)
    quantity = random.randint(1, 5)
    orders.append((customer_id, product_id, quantity))

cursor.executemany(
    "INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)",
    orders
)

conn.commit()
print(f"✅ Created 1000 customers, 500 products, 5000 orders")

# ========== EXPLAIN QUERY PLAN ==========
print("\n" + "=" * 60)
print("EXPLAIN QUERY PLAN")
print("=" * 60)

print("""
EXPLAIN shows how SQLite will execute your query:
- SCAN: Full table scan (slow for large tables)
- SEARCH: Using index (fast)
- USING INDEX: Which index is being used
""")

# Simple query without index
print("\n1. Query WITHOUT index:")
query = "SELECT * FROM customers WHERE city = 'New York'"
cursor.execute(f"EXPLAIN QUERY PLAN {query}")
for row in cursor.fetchall():
    print(f"   {row}")

# After adding index
print("\n2. Creating index on 'city' column...")
cursor.execute("CREATE INDEX idx_customers_city ON customers(city)")
conn.commit()
print("   ✅ Index created")

print("\n3. Same query WITH index:")
cursor.execute(f"EXPLAIN QUERY PLAN {query}")
for row in cursor.fetchall():
    print(f"   {row}")

# ========== QUERY PERFORMANCE COMPARISON ==========
print("\n" + "=" * 60)
print("PERFORMANCE COMPARISON")
print("=" * 60)

def time_query(cursor, query, params=None, runs=100):
    """Measure query execution time"""
    start = time.time()
    for _ in range(runs):
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        cursor.fetchall()
    elapsed = (time.time() - start) / runs * 1000
    return elapsed

# Query on indexed column
print("\n1. Query on indexed column (city):")
query_indexed = "SELECT * FROM customers WHERE city = ?"
time_indexed = time_query(cursor, query_indexed, ("New York",))
print(f"   Average time: {time_indexed:.3f} ms")

# Query on non-indexed column (name)
print("\n2. Query on non-indexed column (name):")
query_not_indexed = "SELECT * FROM customers WHERE name = ?"
time_not_indexed = time_query(cursor, query_not_indexed, ("Customer_500",))
print(f"   Average time: {time_not_indexed:.3f} ms")

# ========== INDEX TYPES ==========
print("\n" + "=" * 60)
print("INDEX TYPES AND STRATEGIES")
print("=" * 60)

print("""
Common Index Types:
1. Single Column Index: For filtering by one column
2. Composite Index: For multi-column queries
3. Unique Index: For columns that must be unique
4. Covering Index: Includes all columns needed by query
""")

# Single column index
print("\n1. Single Column Index:")
print("   CREATE INDEX idx_products_category ON products(category)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_products_category ON products(category)")

# Composite index
print("\n2. Composite Index (multiple columns):")
print("   CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_customer_date ON orders(customer_id, order_date)")

# Unique index
print("\n3. Unique Index:")
print("   CREATE UNIQUE INDEX idx_customers_email ON customers(email)")
cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_customers_email ON customers(email)")

conn.commit()
print("\n✅ All indexes created")

# Show all indexes
print("\nAll indexes on database:")
cursor.execute("""
    SELECT name, tbl_name 
    FROM sqlite_master 
    WHERE type = 'index' AND name NOT LIKE 'sqlite_%'
""")
for row in cursor.fetchall():
    print(f"   {row[0]} on {row[1]}")

# ========== N+1 QUERY PROBLEM ==========
print("\n" + "=" * 60)
print("THE N+1 QUERY PROBLEM")
print("=" * 60)

print("""
N+1 Problem: Making N additional queries in a loop

Example: Display all orders with customer names
- 1 query to get all orders
- N queries to get each customer's name (one per order!)

This is VERY inefficient!
""")

# BAD: N+1 pattern
print("\n❌ BAD: N+1 Query Pattern")
print("   (Simulated - not actually running N+1 queries)")
print("""
   orders = cursor.execute("SELECT * FROM orders LIMIT 100")
   for order in orders:
       # This runs 100 additional queries!
       customer = cursor.execute(
           "SELECT name FROM customers WHERE id = ?",
           (order['customer_id'],)
       )
""")

# Count queries for demonstration
def demonstrate_n_plus_1():
    queries = 1  # Initial orders query
    cursor.execute("SELECT * FROM orders LIMIT 100")
    orders = cursor.fetchall()
    
    for order in orders:
        queries += 1  # One query per order
        cursor.execute(
            "SELECT name FROM customers WHERE id = ?",
            (order[1],)
        )
    return queries

query_count = demonstrate_n_plus_1()
print(f"\n   Total queries executed: {query_count} (1 + 100)")

# GOOD: Single JOIN query
print("\n✅ GOOD: Single JOIN Query")
print("""
   SELECT orders.*, customers.name
   FROM orders
   JOIN customers ON orders.customer_id = customers.id
   LIMIT 100
""")

cursor.execute("""
    SELECT o.id, o.quantity, o.order_date, c.name as customer_name
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    LIMIT 100
""")
results = cursor.fetchall()
print(f"   Total queries executed: 1")
print(f"   Results fetched: {len(results)}")

# Performance comparison
print("\n⏱️ Performance Comparison:")

# N+1 approach
start = time.time()
cursor.execute("SELECT * FROM orders LIMIT 100")
orders = cursor.fetchall()
for order in orders:
    cursor.execute("SELECT name FROM customers WHERE id = ?", (order[1],))
    cursor.fetchone()
n_plus_1_time = time.time() - start

# JOIN approach
start = time.time()
cursor.execute("""
    SELECT o.*, c.name 
    FROM orders o 
    JOIN customers c ON o.customer_id = c.id 
    LIMIT 100
""")
cursor.fetchall()
join_time = time.time() - start

print(f"   N+1 approach: {n_plus_1_time*1000:.2f} ms")
print(f"   JOIN approach: {join_time*1000:.2f} ms")
print(f"   JOIN is {n_plus_1_time/join_time:.1f}x faster!")

# ========== PAGINATION ==========
print("\n" + "=" * 60)
print("EFFICIENT PAGINATION")
print("=" * 60)

print("""
Two main pagination approaches:

1. OFFSET-LIMIT (Simple but slower for large offsets)
   - Easy to implement
   - Gets slower as offset increases
   
2. KEYSET/CURSOR (Faster for large datasets)
   - Uses WHERE clause instead of OFFSET
   - Consistent performance
   - Requires ordered column
""")

# OFFSET-LIMIT Pagination
print("\n1. OFFSET-LIMIT Pagination:")
page_size = 10
page = 5  # Get page 5

cursor.execute(f"""
    SELECT * FROM customers 
    ORDER BY id 
    LIMIT {page_size} OFFSET {(page - 1) * page_size}
""")
results = cursor.fetchall()
print(f"   Page {page} (offset={(page-1)*page_size}): Got {len(results)} records")
if results:
    print(f"   First ID: {results[0][0]}, Last ID: {results[-1][0]}")

# Keyset/Cursor Pagination
print("\n2. KEYSET/CURSOR Pagination:")
last_id = 40  # ID from previous page

cursor.execute(f"""
    SELECT * FROM customers 
    WHERE id > {last_id}
    ORDER BY id 
    LIMIT {page_size}
""")
results = cursor.fetchall()
print(f"   Records after ID {last_id}: Got {len(results)} records")
if results:
    print(f"   First ID: {results[0][0]}, Last ID: {results[-1][0]}")

# Performance comparison
print("\n⏱️ Pagination Performance (large offset):")

# OFFSET approach
start = time.time()
for _ in range(100):
    cursor.execute("SELECT * FROM orders ORDER BY id LIMIT 10 OFFSET 4000")
    cursor.fetchall()
offset_time = (time.time() - start) / 100 * 1000

# Keyset approach
start = time.time()
for _ in range(100):
    cursor.execute("SELECT * FROM orders WHERE id > 4000 ORDER BY id LIMIT 10")
    cursor.fetchall()
keyset_time = (time.time() - start) / 100 * 1000

print(f"   OFFSET 4000: {offset_time:.3f} ms per query")
print(f"   Keyset (id > 4000): {keyset_time:.3f} ms per query")

# ========== QUERY OPTIMIZATION TIPS ==========
print("\n" + "=" * 60)
print("QUERY OPTIMIZATION TIPS")
print("=" * 60)

print("""
✅ DO:
1. Use indexes on columns used in WHERE, JOIN, ORDER BY
2. Select only columns you need (not SELECT *)
3. Use LIMIT to restrict results
4. Use JOINs instead of multiple queries
5. Use EXPLAIN to analyze slow queries
6. Use parameterized queries for security and performance

❌ DON'T:
1. Create indexes on every column (slows down writes)
2. Use functions in WHERE clause on indexed columns
3. Use LIKE '%text' (can't use index effectively)
4. Use SELECT * when you only need specific columns
5. Ignore slow query logs
""")

# Example: Selecting only needed columns
print("\n📝 Example: Select Only Needed Columns")

# Bad: SELECT *
start = time.time()
for _ in range(1000):
    cursor.execute("SELECT * FROM customers WHERE id = 1")
    cursor.fetchone()
bad_time = (time.time() - start) / 1000 * 1000

# Good: Select specific columns
start = time.time()
for _ in range(1000):
    cursor.execute("SELECT name, email FROM customers WHERE id = 1")
    cursor.fetchone()
good_time = (time.time() - start) / 1000 * 1000

print(f"   SELECT *: {bad_time:.4f} ms")
print(f"   SELECT name, email: {good_time:.4f} ms")

# ========== CLEANUP ==========
print("\n" + "=" * 60)
print("CLEANUP")
print("=" * 60)

conn.close()
if os.path.exists(db_file):
    os.remove(db_file)
print("✅ Database closed and removed")

print("\n" + "=" * 60)
print("✅ Query Optimization - Complete!")
print("=" * 60)
