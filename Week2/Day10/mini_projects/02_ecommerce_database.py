"""
Day 10 - Mini Project 2: E-Commerce Database
=============================================
Build a simple e-commerce database with customers, products, and orders.

Features:
- Customer management
- Product inventory
- Order processing
- Sales reports
"""

import sqlite3
from datetime import datetime

print("=" * 60)
print("E-COMMERCE DATABASE - Mini Project")
print("=" * 60)

# Create database
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# ========== STEP 1: CREATE SCHEMA ==========
print("\n📋 Step 1: Creating database schema...")
print("-" * 40)

# Customers table
cursor.execute("""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        city TEXT,
        registered_date TEXT,
        vip INTEGER DEFAULT 0
    )
""")

# Products table
cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price REAL,
        stock INTEGER DEFAULT 0,
        active INTEGER DEFAULT 1
    )
""")

# Orders table
cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        order_date TEXT,
        status TEXT DEFAULT 'pending',
        total_amount REAL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
""")

# Order items table
cursor.execute("""
    CREATE TABLE order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        unit_price REAL,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
""")

print("   ✅ Created tables: customers, products, orders, order_items")

# ========== STEP 2: INSERT DATA ==========
print("\n📋 Step 2: Populating with sample data...")
print("-" * 40)

# Insert customers
customers = [
    ('Alice Johnson', 'alice@email.com', 'New York', '2023-01-15', 1),
    ('Bob Smith', 'bob@email.com', 'Los Angeles', '2023-02-20', 0),
    ('Charlie Brown', 'charlie@email.com', 'Chicago', '2023-03-10', 1),
    ('Diana Ross', 'diana@email.com', 'Houston', '2023-04-05', 0),
    ('Eve Wilson', 'eve@email.com', 'Phoenix', '2023-05-18', 0),
    ('Frank Miller', 'frank@email.com', 'New York', '2023-06-22', 1),
]

cursor.executemany("""
    INSERT INTO customers (name, email, city, registered_date, vip)
    VALUES (?, ?, ?, ?, ?)
""", customers)

# Insert products
products = [
    ('Laptop Pro', 'Electronics', 1299.99, 50),
    ('Smartphone X', 'Electronics', 899.99, 100),
    ('Wireless Earbuds', 'Electronics', 149.99, 200),
    ('Smart Watch', 'Electronics', 299.99, 75),
    ('USB-C Hub', 'Accessories', 49.99, 150),
    ('Laptop Bag', 'Accessories', 79.99, 80),
    ('Mouse Pad XL', 'Accessories', 24.99, 200),
    ('Webcam HD', 'Electronics', 89.99, 60),
]

cursor.executemany("""
    INSERT INTO products (name, category, price, stock)
    VALUES (?, ?, ?, ?)
""", products)

# Insert orders
orders = [
    (1, '2024-01-15', 'completed', 1449.98),
    (1, '2024-02-10', 'completed', 149.99),
    (2, '2024-01-20', 'completed', 899.99),
    (3, '2024-02-05', 'completed', 1649.97),
    (3, '2024-03-01', 'shipped', 379.98),
    (4, '2024-02-15', 'completed', 449.98),
    (5, '2024-03-10', 'processing', 1299.99),
    (6, '2024-03-12', 'pending', 349.98),
]

cursor.executemany("""
    INSERT INTO orders (customer_id, order_date, status, total_amount)
    VALUES (?, ?, ?, ?)
""", orders)

# Insert order items
order_items = [
    (1, 1, 1, 1299.99),    # Order 1: 1 Laptop
    (1, 3, 1, 149.99),     # Order 1: 1 Earbuds
    (2, 3, 1, 149.99),     # Order 2: 1 Earbuds
    (3, 2, 1, 899.99),     # Order 3: 1 Smartphone
    (4, 1, 1, 1299.99),    # Order 4: 1 Laptop
    (4, 4, 1, 299.99),     # Order 4: 1 Smart Watch
    (4, 5, 1, 49.99),      # Order 4: 1 USB Hub
    (5, 4, 1, 299.99),     # Order 5: 1 Smart Watch
    (5, 6, 1, 79.99),      # Order 5: 1 Laptop Bag
    (6, 4, 1, 299.99),     # Order 6: 1 Smart Watch
    (6, 3, 1, 149.99),     # Order 6: 1 Earbuds
    (7, 1, 1, 1299.99),    # Order 7: 1 Laptop
    (8, 4, 1, 299.99),     # Order 8: 1 Smart Watch
    (8, 5, 1, 49.99),      # Order 8: 1 USB Hub
]

cursor.executemany("""
    INSERT INTO order_items (order_id, product_id, quantity, unit_price)
    VALUES (?, ?, ?, ?)
""", order_items)

conn.commit()
print(f"   ✅ Added {len(customers)} customers, {len(products)} products, {len(orders)} orders")

# ========== STEP 3: BUSINESS REPORTS ==========
print("\n📋 Step 3: Generating Business Reports...")

# Report 1: Customer Summary
print("\n" + "=" * 60)
print("📊 Report 1: Customer Summary")
print("-" * 60)
cursor.execute("""
    SELECT c.name, c.city, 
           CASE WHEN c.vip = 1 THEN '⭐ VIP' ELSE '' END as status,
           COUNT(o.id) as orders,
           COALESCE(SUM(o.total_amount), 0) as total_spent
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id
    ORDER BY total_spent DESC
""")
for row in cursor.fetchall():
    print(f"   {row['name']:<20} {row['city']:<15} {row['status']:<6} "
          f"Orders: {row['orders']} | Total: ${row['total_spent']:,.2f}")

# Report 2: Top Products
print("\n" + "=" * 60)
print("📊 Report 2: Top Selling Products")
print("-" * 60)
cursor.execute("""
    SELECT p.name, p.category, 
           COUNT(oi.id) as times_ordered,
           SUM(oi.quantity) as total_qty,
           SUM(oi.quantity * oi.unit_price) as revenue
    FROM products p
    LEFT JOIN order_items oi ON p.id = oi.product_id
    GROUP BY p.id
    ORDER BY revenue DESC
""")
for row in cursor.fetchall():
    revenue = row['revenue'] or 0
    qty = row['total_qty'] or 0
    print(f"   {row['name']:<20} {row['category']:<12} "
          f"Qty Sold: {qty:<5} Revenue: ${revenue:,.2f}")

# Report 3: Sales by Category
print("\n" + "=" * 60)
print("📊 Report 3: Sales by Category")
print("-" * 60)
cursor.execute("""
    SELECT p.category, 
           COUNT(DISTINCT oi.order_id) as orders,
           SUM(oi.quantity) as items_sold,
           SUM(oi.quantity * oi.unit_price) as revenue
    FROM products p
    INNER JOIN order_items oi ON p.id = oi.product_id
    GROUP BY p.category
    ORDER BY revenue DESC
""")
for row in cursor.fetchall():
    print(f"   {row['category']:<15} Orders: {row['orders']:<5} "
          f"Items: {row['items_sold']:<5} Revenue: ${row['revenue']:,.2f}")

# Report 4: Order Status
print("\n" + "=" * 60)
print("📊 Report 4: Orders by Status")
print("-" * 60)
cursor.execute("""
    SELECT status, COUNT(*) as count, SUM(total_amount) as total
    FROM orders
    GROUP BY status
    ORDER BY count DESC
""")
for row in cursor.fetchall():
    status_icon = {'completed': '✅', 'shipped': '📦', 'processing': '⏳', 'pending': '🕐'}
    icon = status_icon.get(row['status'], '❓')
    print(f"   {icon} {row['status']:<12} {row['count']} orders | ${row['total']:,.2f}")

# Report 5: City Performance
print("\n" + "=" * 60)
print("📊 Report 5: Sales by City")
print("-" * 60)
cursor.execute("""
    SELECT c.city, 
           COUNT(DISTINCT c.id) as customers,
           COUNT(o.id) as orders,
           SUM(o.total_amount) as revenue
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    GROUP BY c.city
    ORDER BY revenue DESC
""")
for row in cursor.fetchall():
    revenue = row['revenue'] or 0
    print(f"   {row['city']:<15} Customers: {row['customers']:<5} "
          f"Orders: {row['orders']:<5} Revenue: ${revenue:,.2f}")

# Report 6: VIP vs Regular Customers
print("\n" + "=" * 60)
print("📊 Report 6: VIP vs Regular Customer Comparison")
print("-" * 60)
cursor.execute("""
    SELECT CASE WHEN c.vip = 1 THEN 'VIP' ELSE 'Regular' END as type,
           COUNT(DISTINCT c.id) as customers,
           COUNT(o.id) as total_orders,
           SUM(o.total_amount) as total_revenue,
           ROUND(AVG(o.total_amount), 2) as avg_order
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    GROUP BY c.vip
""")
for row in cursor.fetchall():
    revenue = row['total_revenue'] or 0
    avg = row['avg_order'] or 0
    print(f"   {row['type']:<10} Customers: {row['customers']:<5} "
          f"Orders: {row['total_orders']:<5} Total: ${revenue:,.2f} (Avg: ${avg:,.2f})")

# Report 7: Products Never Ordered
print("\n" + "=" * 60)
print("📊 Report 7: Products Never Ordered")
print("-" * 60)
cursor.execute("""
    SELECT p.name, p.category, p.price, p.stock
    FROM products p
    LEFT JOIN order_items oi ON p.id = oi.product_id
    WHERE oi.id IS NULL
""")
results = cursor.fetchall()
if results:
    for row in results:
        print(f"   ⚠️ {row['name']} ({row['category']}) - ${row['price']} (Stock: {row['stock']})")
else:
    print("   ✅ All products have been ordered at least once!")

# Report 8: Recent Orders Detail
print("\n" + "=" * 60)
print("📊 Report 8: Recent Orders (Last 3)")
print("-" * 60)
cursor.execute("""
    SELECT o.id, c.name, o.order_date, o.status, o.total_amount
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.id
    ORDER BY o.order_date DESC
    LIMIT 3
""")
for row in cursor.fetchall():
    print(f"\n   Order #{row['id']} - {row['order_date']} [{row['status']}]")
    print(f"   Customer: {row['name']} | Total: ${row['total_amount']:,.2f}")
    
    # Get items for this order
    cursor.execute("""
        SELECT p.name, oi.quantity, oi.unit_price
        FROM order_items oi
        INNER JOIN products p ON oi.product_id = p.id
        WHERE oi.order_id = ?
    """, (row['id'],))
    items = cursor.fetchall()
    for item in items:
        print(f"      - {item['name']} x{item['quantity']} @ ${item['unit_price']:.2f}")

conn.close()

print("\n" + "=" * 60)
print("✅ Mini Project Complete!")
print("=" * 60)
print("""
What you practiced:
- Complex schema with multiple related tables
- Multi-table JOINs (3+ tables)
- Aggregations with GROUP BY
- CASE statements for conditional logic
- Business analytics queries
- LEFT JOIN to find missing data
""")
