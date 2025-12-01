"""
Day 10 - SQL JOINs
==================
Learn: INNER JOIN and LEFT JOIN

Key Concepts:
- INNER JOIN: Returns only matching rows from both tables
- LEFT JOIN: Returns all rows from left table, matching from right
- Table relationships and foreign keys
"""

import sqlite3

# ========== SETUP DATABASE ==========
print("=" * 60)
print("SETUP: Creating Sample Database with Related Tables")
print("=" * 60)

conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create users table
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        city TEXT
    )
""")

# Create orders table (related to users via user_id)
cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT NOT NULL,
        amount REAL,
        order_date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

# Create products table
cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price REAL
    )
""")

# Create order_items table (links orders to products)
cursor.execute("""
    CREATE TABLE order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
""")

# Insert sample users
users = [
    ('Alice Johnson', 'alice@email.com', 'New York'),
    ('Bob Smith', 'bob@email.com', 'Los Angeles'),
    ('Charlie Brown', 'charlie@email.com', 'Chicago'),
    ('Diana Ross', 'diana@email.com', 'Houston'),
    ('Eve Wilson', 'eve@email.com', 'Phoenix'),
    ('Frank Miller', 'frank@email.com', 'Miami'),
]

cursor.executemany(
    "INSERT INTO users (name, email, city) VALUES (?, ?, ?)",
    users
)

# Insert sample orders (some users have orders, some don't)
orders = [
    (1, 'Laptop', 999.99, '2024-01-15'),      # Alice
    (1, 'Headphones', 149.99, '2024-01-20'),  # Alice
    (2, 'Smartphone', 699.99, '2024-02-01'),  # Bob
    (3, 'Tablet', 449.99, '2024-02-10'),      # Charlie
    (3, 'Keyboard', 79.99, '2024-02-15'),     # Charlie
    (3, 'Mouse', 29.99, '2024-02-15'),        # Charlie
    (4, 'Monitor', 299.99, '2024-03-01'),     # Diana
]

cursor.executemany(
    "INSERT INTO orders (user_id, product, amount, order_date) VALUES (?, ?, ?, ?)",
    orders
)

# Insert products
products = [
    ('Laptop', 'Electronics', 999.99),
    ('Smartphone', 'Electronics', 699.99),
    ('Headphones', 'Electronics', 149.99),
    ('Tablet', 'Electronics', 449.99),
    ('Monitor', 'Electronics', 299.99),
    ('Keyboard', 'Accessories', 79.99),
    ('Mouse', 'Accessories', 29.99),
    ('USB Cable', 'Accessories', 9.99),
]

cursor.executemany(
    "INSERT INTO products (name, category, price) VALUES (?, ?, ?)",
    products
)

conn.commit()

print("✅ Created tables: users, orders, products, order_items")
print(f"   - {len(users)} users")
print(f"   - {len(orders)} orders")
print(f"   - {len(products)} products")

# ========== UNDERSTANDING RELATIONSHIPS ==========
print("\n" + "=" * 60)
print("UNDERSTANDING TABLE RELATIONSHIPS")
print("=" * 60)

print("""
Our Database Schema:
-------------------

users (id, name, email, city)
  |
  | (one-to-many: one user can have many orders)
  v
orders (id, user_id, product, amount, order_date)
        ↑
        Foreign Key links to users.id

This means:
- users table is the "parent"
- orders table is the "child"
- user_id in orders references id in users
""")

# Show current data
print("\n📊 Users Table:")
print("-" * 40)
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(f"   {row['id']}. {row['name']} ({row['city']})")

print("\n📊 Orders Table:")
print("-" * 40)
cursor.execute("SELECT * FROM orders")
for row in cursor.fetchall():
    print(f"   Order {row['id']}: User {row['user_id']} - {row['product']} (${row['amount']:.2f})")

# ========== INNER JOIN ==========
print("\n" + "=" * 60)
print("INNER JOIN")
print("=" * 60)

print("""
INNER JOIN returns only rows that have matching values in BOTH tables.

    users            orders
    +----+          +----+--------+
    | id |          | id | user_id|
    +----+          +----+--------+
    | 1  |<-------->| 1  |   1    | ← Match!
    | 2  |<-------->| 3  |   2    | ← Match!
    | 3  |<-------->| 4  |   3    | ← Match!
    | 4  |<-------->| 7  |   4    | ← Match!
    | 5  |          +----+--------+
    | 6  |          
    +----+          No orders for users 5 and 6
    
    Result: Only users 1, 2, 3, 4 (who have orders)
""")

# Basic INNER JOIN
print("\n1. Basic INNER JOIN:")
print("-" * 50)
cursor.execute("""
    SELECT users.name, orders.product, orders.amount
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
""")

for row in cursor.fetchall():
    print(f"   {row['name']} ordered {row['product']} (${row['amount']:.2f})")

# INNER JOIN with aliases
print("\n2. INNER JOIN with table aliases:")
print("-" * 50)
cursor.execute("""
    SELECT u.name, u.city, o.product, o.amount, o.order_date
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    ORDER BY o.order_date DESC
""")

print("   Recent orders (with user info):")
for row in cursor.fetchall():
    print(f"   {row['order_date']}: {row['name']} ({row['city']}) - {row['product']}")

# INNER JOIN with conditions
print("\n3. INNER JOIN with WHERE clause:")
print("-" * 50)
cursor.execute("""
    SELECT u.name, o.product, o.amount
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    WHERE o.amount > 200
    ORDER BY o.amount DESC
""")

print("   Orders over $200:")
for row in cursor.fetchall():
    print(f"   {row['name']}: {row['product']} - ${row['amount']:.2f}")

# INNER JOIN with aggregate
print("\n4. INNER JOIN with aggregation:")
print("-" * 50)
cursor.execute("""
    SELECT u.name, 
           COUNT(o.id) as total_orders,
           SUM(o.amount) as total_spent,
           AVG(o.amount) as avg_order
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    GROUP BY u.id
    ORDER BY total_spent DESC
""")

print("   User purchase summary:")
for row in cursor.fetchall():
    print(f"   {row['name']}: {row['total_orders']} orders, "
          f"${row['total_spent']:.2f} total (avg: ${row['avg_order']:.2f})")

# ========== LEFT JOIN ==========
print("\n" + "=" * 60)
print("LEFT JOIN (LEFT OUTER JOIN)")
print("=" * 60)

print("""
LEFT JOIN returns ALL rows from the left table, and matching rows 
from the right table. Non-matching rows have NULL values.

    users            orders
    +----+          +----+--------+
    | id |          | id | user_id|
    +----+          +----+--------+
    | 1  |--------->| 1  |   1    | ← Match!
    | 2  |--------->| 3  |   2    | ← Match!
    | 3  |--------->| 4  |   3    | ← Match!
    | 4  |--------->| 7  |   4    | ← Match!
    | 5  |--------->|    | NULL   | ← No match, but included
    | 6  |--------->|    | NULL   | ← No match, but included
    +----+          +----+--------+
    
    Result: ALL users (1-6), but orders will be NULL for 5 and 6
""")

# Basic LEFT JOIN
print("\n1. Basic LEFT JOIN:")
print("-" * 50)
cursor.execute("""
    SELECT users.name, orders.product, orders.amount
    FROM users
    LEFT JOIN orders ON users.id = orders.user_id
    ORDER BY users.id
""")

for row in cursor.fetchall():
    product = row['product'] if row['product'] else "No orders"
    amount = f"${row['amount']:.2f}" if row['amount'] else "-"
    print(f"   {row['name']}: {product} ({amount})")

# Find users with NO orders
print("\n2. Find users with NO orders (LEFT JOIN + IS NULL):")
print("-" * 50)
cursor.execute("""
    SELECT u.name, u.email
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE o.id IS NULL
""")

print("   Users who haven't ordered anything:")
for row in cursor.fetchall():
    print(f"   - {row['name']} ({row['email']})")

# LEFT JOIN with COALESCE (handle NULLs)
print("\n3. LEFT JOIN with COALESCE (replace NULL with default):")
print("-" * 50)
cursor.execute("""
    SELECT u.name, 
           COALESCE(COUNT(o.id), 0) as order_count,
           COALESCE(SUM(o.amount), 0) as total_spent
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    GROUP BY u.id
    ORDER BY total_spent DESC
""")

print("   All users purchase summary:")
for row in cursor.fetchall():
    print(f"   {row['name']}: {row['order_count']} orders, ${row['total_spent']:.2f}")

# ========== COMPARISON: INNER vs LEFT JOIN ==========
print("\n" + "=" * 60)
print("COMPARISON: INNER JOIN vs LEFT JOIN")
print("=" * 60)

print("\nINNER JOIN - Only users WITH orders:")
cursor.execute("""
    SELECT DISTINCT u.name
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
""")
inner_users = [row['name'] for row in cursor.fetchall()]
print(f"   Users: {inner_users}")
print(f"   Count: {len(inner_users)}")

print("\nLEFT JOIN - ALL users (with or without orders):")
cursor.execute("""
    SELECT DISTINCT u.name
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
""")
left_users = [row['name'] for row in cursor.fetchall()]
print(f"   Users: {left_users}")
print(f"   Count: {len(left_users)}")

# ========== MULTIPLE JOINS ==========
print("\n" + "=" * 60)
print("MULTIPLE TABLE JOINS")
print("=" * 60)

# First, let's create order_items data
cursor.executemany("""
    INSERT INTO order_items (order_id, product_id, quantity)
    VALUES (?, ?, ?)
""", [
    (1, 1, 1),  # Order 1: Laptop
    (2, 3, 1),  # Order 2: Headphones
    (3, 2, 1),  # Order 3: Smartphone
    (4, 4, 1),  # Order 4: Tablet
    (5, 6, 1),  # Order 5: Keyboard
    (6, 7, 2),  # Order 6: 2x Mouse
])
conn.commit()

print("\nJoining users → orders → order_items → products:")
print("-" * 60)

cursor.execute("""
    SELECT u.name, o.order_date, p.name as product, 
           p.category, oi.quantity, p.price,
           (oi.quantity * p.price) as subtotal
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    ORDER BY o.order_date
""")

for row in cursor.fetchall():
    print(f"   {row['name']}: {row['product']} ({row['category']})")
    print(f"      Qty: {row['quantity']} x ${row['price']:.2f} = ${row['subtotal']:.2f}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 60)
print("PRACTICAL JOIN EXAMPLES")
print("=" * 60)

# Example 1: Top customers
print("\n1. Top customers by total spending:")
print("-" * 50)
cursor.execute("""
    SELECT u.name, u.city, SUM(o.amount) as total_spent
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    GROUP BY u.id
    ORDER BY total_spent DESC
    LIMIT 3
""")
for i, row in enumerate(cursor.fetchall(), 1):
    print(f"   #{i} {row['name']} ({row['city']}): ${row['total_spent']:.2f}")

# Example 2: Orders by city
print("\n2. Total orders by city:")
print("-" * 50)
cursor.execute("""
    SELECT u.city, COUNT(o.id) as order_count, SUM(o.amount) as revenue
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    GROUP BY u.city
    ORDER BY revenue DESC
""")
for row in cursor.fetchall():
    print(f"   {row['city']}: {row['order_count']} orders, ${row['revenue']:.2f}")

# Example 3: Product sales
print("\n3. Products by category (total sales):")
print("-" * 50)
cursor.execute("""
    SELECT p.category, 
           COUNT(oi.id) as times_ordered,
           SUM(oi.quantity) as total_quantity
    FROM products p
    LEFT JOIN order_items oi ON p.id = oi.product_id
    GROUP BY p.category
""")
for row in cursor.fetchall():
    print(f"   {row['category']}: ordered {row['times_ordered']} times, "
          f"total qty: {row['total_quantity'] or 0}")

# Example 4: Products never ordered
print("\n4. Products that have never been ordered:")
print("-" * 50)
cursor.execute("""
    SELECT p.name, p.category, p.price
    FROM products p
    LEFT JOIN order_items oi ON p.id = oi.product_id
    WHERE oi.id IS NULL
""")
for row in cursor.fetchall():
    print(f"   - {row['name']} ({row['category']}): ${row['price']:.2f}")

# Close connection
conn.close()

print("\n" + "=" * 60)
print("✅ SQL JOINs - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. INNER JOIN - Returns only matching rows from both tables
2. LEFT JOIN - Returns all rows from left table, matching from right
3. Use aliases (u, o) for cleaner queries
4. WHERE with NULL to find non-matching rows
5. Can join multiple tables in one query
6. Always consider which join type you need:
   - Need all records from one table? Use LEFT JOIN
   - Need only matching records? Use INNER JOIN
""")
