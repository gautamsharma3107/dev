"""
Day 10 - SQL Exercise 2: INSERT, UPDATE, DELETE
================================================
Practice: Data manipulation operations

Complete each exercise by writing the SQL query.
"""

import sqlite3

# Setup database
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create products table
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

# Insert initial data
products = [
    ('Laptop', 'Electronics', 999.99, 50),
    ('Smartphone', 'Electronics', 699.99, 100),
    ('Headphones', 'Electronics', 149.99, 200),
    ('Coffee Maker', 'Appliances', 79.99, 30),
    ('Blender', 'Appliances', 49.99, 45),
]

cursor.executemany(
    "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
    products
)
conn.commit()

print("=" * 60)
print("SQL EXERCISE 2: INSERT, UPDATE, DELETE")
print("=" * 60)
print("\nTable: products (id, name, category, price, stock, active)")
print("-" * 60)

def show_products(message="Current products:"):
    print(f"\n📊 {message}")
    cursor.execute("SELECT * FROM products ORDER BY id")
    for row in cursor.fetchall():
        status = "✅" if row['active'] else "❌"
        print(f"   {status} {row['id']}. {row['name']} ({row['category']}) - ${row['price']:.2f}, Stock: {row['stock']}")

show_products("Initial products:")

# ============================================================
# EXERCISE 1: INSERT a new product
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 1: Insert a new product 'Tablet'")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    INSERT INTO products (name, category, price, stock)
    VALUES ('Tablet', 'Electronics', 449.99, 75)
""")
conn.commit()

show_products("After INSERT:")

# ============================================================
# EXERCISE 2: INSERT multiple products
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 2: Insert multiple products")
print("-" * 40)

# YOUR QUERY HERE:
new_products = [
    ('Monitor', 'Electronics', 299.99, 40),
    ('Keyboard', 'Accessories', 79.99, 100),
    ('Mouse', 'Accessories', 29.99, 150),
]

cursor.executemany("""
    INSERT INTO products (name, category, price, stock)
    VALUES (?, ?, ?, ?)
""", new_products)
conn.commit()

show_products("After multiple INSERT:")

# ============================================================
# EXERCISE 3: UPDATE price of a single product
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 3: Increase Laptop price to $1099.99")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    UPDATE products 
    SET price = 1099.99 
    WHERE name = 'Laptop'
""")
conn.commit()

cursor.execute("SELECT name, price FROM products WHERE name = 'Laptop'")
row = cursor.fetchone()
print(f"   Laptop new price: ${row['price']:.2f}")

# ============================================================
# EXERCISE 4: UPDATE stock for multiple products
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 4: Add 50 units to all Electronics stock")
print("-" * 40)

print("   Before:")
cursor.execute("SELECT name, stock FROM products WHERE category = 'Electronics'")
for row in cursor.fetchall():
    print(f"      {row['name']}: {row['stock']}")

# YOUR QUERY HERE:
cursor.execute("""
    UPDATE products 
    SET stock = stock + 50 
    WHERE category = 'Electronics'
""")
conn.commit()

print("\n   After:")
cursor.execute("SELECT name, stock FROM products WHERE category = 'Electronics'")
for row in cursor.fetchall():
    print(f"      {row['name']}: {row['stock']}")

# ============================================================
# EXERCISE 5: UPDATE with percentage (10% price increase)
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 5: 10% price increase for Appliances")
print("-" * 40)

print("   Before:")
cursor.execute("SELECT name, price FROM products WHERE category = 'Appliances'")
for row in cursor.fetchall():
    print(f"      {row['name']}: ${row['price']:.2f}")

# YOUR QUERY HERE:
cursor.execute("""
    UPDATE products 
    SET price = price * 1.10 
    WHERE category = 'Appliances'
""")
conn.commit()

print("\n   After 10% increase:")
cursor.execute("SELECT name, price FROM products WHERE category = 'Appliances'")
for row in cursor.fetchall():
    print(f"      {row['name']}: ${row['price']:.2f}")

# ============================================================
# EXERCISE 6: SET product as inactive
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 6: Deactivate products with stock < 50")
print("-" * 40)

# YOUR QUERY HERE:
cursor.execute("""
    UPDATE products 
    SET active = 0 
    WHERE stock < 50
""")
conn.commit()

print(f"   Rows affected: {cursor.rowcount}")
show_products("After deactivation:")

# ============================================================
# EXERCISE 7: DELETE a single product
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 7: Delete the Mouse product")
print("-" * 40)

cursor.execute("SELECT COUNT(*) as count FROM products")
before = cursor.fetchone()['count']

# YOUR QUERY HERE:
cursor.execute("DELETE FROM products WHERE name = 'Mouse'")
conn.commit()

cursor.execute("SELECT COUNT(*) as count FROM products")
after = cursor.fetchone()['count']
print(f"   Before: {before} products, After: {after} products")

# ============================================================
# EXERCISE 8: DELETE inactive products
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 8: Delete all inactive products")
print("-" * 40)

# Show inactive products first
cursor.execute("SELECT name FROM products WHERE active = 0")
inactive = [row['name'] for row in cursor.fetchall()]
print(f"   Inactive products to delete: {inactive}")

# YOUR QUERY HERE:
cursor.execute("DELETE FROM products WHERE active = 0")
conn.commit()

print(f"   Deleted: {cursor.rowcount} products")
show_products("After deleting inactive:")

# ============================================================
# EXERCISE 9: Safe DELETE with condition
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 9: Delete products priced under $100")
print("-" * 40)

# Show products first
cursor.execute("SELECT name, price FROM products WHERE price < 100")
cheap = cursor.fetchall()
print(f"   Products under $100: {[row['name'] for row in cheap]}")

# YOUR QUERY HERE:
cursor.execute("DELETE FROM products WHERE price < 100")
conn.commit()

print(f"   Deleted: {cursor.rowcount} products")
show_products("After deletion:")

# ============================================================
# EXERCISE 10: Restore products (INSERT multiple)
# ============================================================
print("\n" + "=" * 60)
print("📝 Exercise 10: Restore some products")
print("-" * 40)

# YOUR QUERY HERE:
restore_products = [
    ('Gaming Mouse', 'Accessories', 59.99, 200),
    ('USB Hub', 'Accessories', 24.99, 300),
    ('Webcam', 'Electronics', 89.99, 150),
]

cursor.executemany("""
    INSERT INTO products (name, category, price, stock)
    VALUES (?, ?, ?, ?)
""", restore_products)
conn.commit()

show_products("Final product list:")

conn.close()

print("\n" + "=" * 60)
print("✅ Exercise 2 Complete!")
print("=" * 60)
print("""
Practice Tips:
- Always use WHERE with UPDATE and DELETE
- Use SELECT first to see what will be affected
- Remember to commit() after changes
- Check rowcount to see how many rows were affected
""")
