"""
Day 18 - Relationship Exercises
===============================
Practice: Foreign keys, JOINs, and data relationships

Complete each exercise to practice database relationships.
Solutions are provided at the bottom - try solving first!
"""

import sqlite3
import os

print("=" * 60)
print("DAY 18 EXERCISES: Database Relationships")
print("=" * 60)

# Setup database
db_file = "exercises.db"
conn = sqlite3.connect(db_file)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# ============================================================
# SETUP: Create tables for exercises
# ============================================================

# Drop existing tables
for table in ["order_items", "orders", "products", "categories", "customers"]:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Create tables
cursor.execute("""
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
""")

cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    total REAL DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)
""")

cursor.execute("""
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

# Insert sample data
categories = [("Electronics",), ("Books",), ("Clothing",), ("Home",)]
cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)

products = [
    ("Laptop", 999.99, 1), ("Mouse", 29.99, 1), ("Keyboard", 79.99, 1),
    ("Python Book", 49.99, 2), ("SQL Guide", 39.99, 2),
    ("T-Shirt", 19.99, 3), ("Jeans", 59.99, 3),
    ("Lamp", 34.99, 4), ("Chair", 149.99, 4),
]
cursor.executemany("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", products)

customers = [
    ("Alice Johnson", "alice@email.com", "New York"),
    ("Bob Smith", "bob@email.com", "Los Angeles"),
    ("Charlie Brown", "charlie@email.com", "Chicago"),
]
cursor.executemany("INSERT INTO customers (name, email, city) VALUES (?, ?, ?)", customers)

orders = [
    (1, "2024-01-15", 1079.97),  # Alice's order
    (1, "2024-02-01", 49.99),    # Alice's second order
    (2, "2024-01-20", 79.98),    # Bob's order
]
cursor.executemany("INSERT INTO orders (customer_id, order_date, total) VALUES (?, ?, ?)", orders)

order_items = [
    (1, 1, 1, 999.99),  # Laptop in order 1
    (1, 2, 1, 29.99),   # Mouse in order 1
    (1, 4, 1, 49.99),   # Python Book in order 1
    (2, 4, 1, 49.99),   # Python Book in order 2
    (3, 6, 2, 19.99),   # 2 T-Shirts in order 3
    (3, 5, 1, 39.99),   # SQL Guide in order 3
]
cursor.executemany("INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)", order_items)

conn.commit()
print("✅ Database setup complete\n")

# ============================================================
# EXERCISE 1: Basic JOIN
# ============================================================

print("=" * 60)
print("EXERCISE 1: List all products with their category names")
print("=" * 60)
print("Expected: Each product row should include category name")
print("Tables: products, categories")
print()

# TODO: Write your query here
# query = """
#     SELECT ...
# """

print("Your solution:")
print("(Write your query above and uncomment)")
print()

# ============================================================
# EXERCISE 2: LEFT JOIN
# ============================================================

print("=" * 60)
print("EXERCISE 2: List all categories with product count")
print("=" * 60)
print("Expected: Show all categories, even those without products")
print("Tables: categories, products")
print()

# TODO: Write your query here
# query = """
#     SELECT ...
# """

print("Your solution:")
print("(Write your query above and uncomment)")
print()

# ============================================================
# EXERCISE 3: Multiple JOINs
# ============================================================

print("=" * 60)
print("EXERCISE 3: List all order items with customer and product names")
print("=" * 60)
print("Expected: customer_name, product_name, quantity, price")
print("Tables: order_items, orders, customers, products")
print()

# TODO: Write your query here
# query = """
#     SELECT ...
# """

print("Your solution:")
print("(Write your query above and uncomment)")
print()

# ============================================================
# EXERCISE 4: Aggregate with JOIN
# ============================================================

print("=" * 60)
print("EXERCISE 4: Find total spending per customer")
print("=" * 60)
print("Expected: customer_name, total_spent (sum of all orders)")
print("Tables: customers, orders")
print()

# TODO: Write your query here
# query = """
#     SELECT ...
# """

print("Your solution:")
print("(Write your query above and uncomment)")
print()

# ============================================================
# EXERCISE 5: Complex Query
# ============================================================

print("=" * 60)
print("EXERCISE 5: Find top-selling products by quantity")
print("=" * 60)
print("Expected: product_name, total_quantity_sold, revenue")
print("Tables: products, order_items")
print("Hint: Use SUM() and GROUP BY")
print()

# TODO: Write your query here
# query = """
#     SELECT ...
# """

print("Your solution:")
print("(Write your query above and uncomment)")
print()

# ============================================================
# SOLUTIONS
# ============================================================

print("\n" + "=" * 60)
print("SOLUTIONS (scroll down to see)")
print("=" * 60)
print()
print()
print()

# SOLUTION 1
print("SOLUTION 1:")
cursor.execute("""
    SELECT p.name as product, p.price, c.name as category
    FROM products p
    INNER JOIN categories c ON p.category_id = c.id
    ORDER BY c.name, p.name
""")
for row in cursor.fetchall():
    print(f"  {row[0]:<15} ${row[1]:<8} ({row[2]})")
print()

# SOLUTION 2
print("SOLUTION 2:")
cursor.execute("""
    SELECT c.name as category, COUNT(p.id) as product_count
    FROM categories c
    LEFT JOIN products p ON c.id = p.category_id
    GROUP BY c.id
    ORDER BY product_count DESC
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} products")
print()

# SOLUTION 3
print("SOLUTION 3:")
cursor.execute("""
    SELECT 
        cu.name as customer,
        pr.name as product,
        oi.quantity,
        oi.price
    FROM order_items oi
    JOIN orders o ON oi.order_id = o.id
    JOIN customers cu ON o.customer_id = cu.id
    JOIN products pr ON oi.product_id = pr.id
""")
for row in cursor.fetchall():
    print(f"  {row[0]:<15} bought {row[2]}x {row[1]:<12} @ ${row[3]}")
print()

# SOLUTION 4
print("SOLUTION 4:")
cursor.execute("""
    SELECT c.name, SUM(o.total) as total_spent
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id
    ORDER BY total_spent DESC
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: ${row[1]:.2f}")
print()

# SOLUTION 5
print("SOLUTION 5:")
cursor.execute("""
    SELECT 
        p.name as product,
        SUM(oi.quantity) as total_qty,
        SUM(oi.quantity * oi.price) as revenue
    FROM products p
    JOIN order_items oi ON p.id = oi.product_id
    GROUP BY p.id
    ORDER BY total_qty DESC
""")
for row in cursor.fetchall():
    print(f"  {row[0]:<15} qty: {row[1]}, revenue: ${row[2]:.2f}")
print()

# Cleanup
conn.close()
if os.path.exists(db_file):
    os.remove(db_file)
print("\n✅ Exercises complete! Database cleaned up.")
