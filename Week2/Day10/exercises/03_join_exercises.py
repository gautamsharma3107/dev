"""
Day 10 - SQL Exercise 3: JOIN Queries
=====================================
Practice: INNER JOIN and LEFT JOIN

Complete each exercise by writing the SQL query.
"""

import sqlite3

# Setup database
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        city TEXT
    )
""")

cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product TEXT,
        amount REAL,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
""")

cursor.execute("""
    CREATE TABLE categories (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")

cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category_id INTEGER,
        price REAL,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
""")

# Insert sample data
customers = [
    (1, 'Alice Johnson', 'alice@email.com', 'New York'),
    (2, 'Bob Smith', 'bob@email.com', 'Los Angeles'),
    (3, 'Charlie Brown', 'charlie@email.com', 'Chicago'),
    (4, 'Diana Ross', 'diana@email.com', 'Houston'),
    (5, 'Eve Wilson', 'eve@email.com', 'Phoenix'),  # No orders
    (6, 'Frank Miller', 'frank@email.com', 'Miami'),  # No orders
]

orders = [
    (1, 1, 'Laptop', 999.99, '2024-01-15'),
    (2, 1, 'Mouse', 29.99, '2024-01-20'),
    (3, 2, 'Keyboard', 79.99, '2024-02-01'),
    (4, 3, 'Monitor', 299.99, '2024-02-10'),
    (5, 3, 'Headphones', 149.99, '2024-02-15'),
    (6, 4, 'Tablet', 449.99, '2024-03-01'),
    (7, 4, 'Charger', 19.99, '2024-03-05'),
    (8, 4, 'Case', 29.99, '2024-03-05'),
]

categories = [
    (1, 'Electronics'),
    (2, 'Accessories'),
    (3, 'Software'),  # No products
]

products = [
    (1, 'Laptop', 1, 999.99),
    (2, 'Smartphone', 1, 699.99),
    (3, 'Mouse', 2, 29.99),
    (4, 'Keyboard', 2, 79.99),
    (5, 'Monitor', 1, 299.99),
]

cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customers)
cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", orders)
cursor.executemany("INSERT INTO categories VALUES (?, ?)", categories)
cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", products)
conn.commit()

print("=" * 60)
print("SQL EXERCISE 3: JOIN Queries")
print("=" * 60)
print("\nTables: customers, orders, categories, products")
print("-" * 60)

# Show table structure
print("\n📊 Customers (6 total, 2 without orders):")
cursor.execute("SELECT id, name FROM customers")
for row in cursor.fetchall():
    print(f"   {row['id']}. {row['name']}")

print("\n📊 Orders (8 total):")
cursor.execute("SELECT id, customer_id, product FROM orders")
for row in cursor.fetchall():
    print(f"   Order {row['id']}: Customer {row['customer_id']} - {row['product']}")

# ============================================================
# EXERCISE 1: Basic INNER JOIN
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 1: INNER JOIN - Show customer names with their orders")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.name, o.product, o.amount
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
""")

for row in cursor.fetchall():
    print(f"   {row['name']} ordered {row['product']} (${row['amount']:.2f})")

# ============================================================
# EXERCISE 2: LEFT JOIN to find ALL customers
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 2: LEFT JOIN - Show ALL customers and their orders")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.name, COALESCE(o.product, 'No orders') as product
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
""")

for row in cursor.fetchall():
    print(f"   {row['name']}: {row['product']}")

# ============================================================
# EXERCISE 3: Find customers with NO orders
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 3: Find customers who haven't placed any orders")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.name, c.email
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    WHERE o.id IS NULL
""")

for row in cursor.fetchall():
    print(f"   {row['name']} ({row['email']})")

# ============================================================
# EXERCISE 4: INNER JOIN with aggregation
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 4: Total spending per customer")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.name, COUNT(o.id) as order_count, SUM(o.amount) as total_spent
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id
    ORDER BY total_spent DESC
""")

for row in cursor.fetchall():
    print(f"   {row['name']}: {row['order_count']} orders, ${row['total_spent']:.2f}")

# ============================================================
# EXERCISE 5: LEFT JOIN with aggregation (all customers)
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 5: ALL customers with their order summary")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.name, 
           COUNT(o.id) as order_count, 
           COALESCE(SUM(o.amount), 0) as total_spent
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id
    ORDER BY total_spent DESC
""")

for row in cursor.fetchall():
    print(f"   {row['name']}: {row['order_count']} orders, ${row['total_spent']:.2f}")

# ============================================================
# EXERCISE 6: JOIN with multiple conditions
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 6: Orders over $100 with customer info")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.name, c.city, o.product, o.amount
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.amount > 100
    ORDER BY o.amount DESC
""")

for row in cursor.fetchall():
    print(f"   {row['name']} ({row['city']}): {row['product']} - ${row['amount']:.2f}")

# ============================================================
# EXERCISE 7: JOIN products with categories
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 7: Products with their category names")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT p.name as product, c.name as category, p.price
    FROM products p
    INNER JOIN categories c ON p.category_id = c.id
    ORDER BY c.name, p.name
""")

for row in cursor.fetchall():
    print(f"   {row['category']}: {row['product']} - ${row['price']:.2f}")

# ============================================================
# EXERCISE 8: Find categories with no products
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 8: Categories with no products")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.name as category
    FROM categories c
    LEFT JOIN products p ON c.id = p.category_id
    WHERE p.id IS NULL
""")

for row in cursor.fetchall():
    print(f"   - {row['category']} (empty category)")

# ============================================================
# EXERCISE 9: Orders by city
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 9: Total orders and revenue by city")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.city, COUNT(o.id) as orders, SUM(o.amount) as revenue
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    GROUP BY c.city
    ORDER BY revenue DESC
""")

for row in cursor.fetchall():
    print(f"   {row['city']}: {row['orders']} orders, ${row['revenue']:.2f}")

# ============================================================
# EXERCISE 10: Top customers by order count
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 10: Top 3 customers by number of orders")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    SELECT c.name, COUNT(o.id) as order_count
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id
    ORDER BY order_count DESC
    LIMIT 3
""")

for i, row in enumerate(cursor.fetchall(), 1):
    print(f"   #{i} {row['name']}: {row['order_count']} orders")

conn.close()

print("\n" + "=" * 60)
print("✅ Exercise 3 Complete!")
print("=" * 60)
print("""
Practice Tips:
- Use INNER JOIN when you only want matching rows
- Use LEFT JOIN when you want ALL rows from the left table
- Use WHERE ... IS NULL to find non-matching rows
- Always consider which table should be "left" in LEFT JOIN
""")
