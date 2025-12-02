"""
Database Schema Design
======================
Day 37 - System Design Basics

Learn how to design efficient, scalable database schemas.
"""

# ============================================================
# 1. DATABASE DESIGN FUNDAMENTALS
# ============================================================

"""
Key Concepts in Database Design:

1. Tables (Entities)
   - Represent real-world objects
   - Users, Products, Orders, etc.

2. Columns (Attributes)
   - Properties of entities
   - id, name, email, created_at

3. Rows (Records)
   - Individual instances
   - Each row is one user, one product

4. Primary Key
   - Unique identifier for each row
   - Usually 'id' or 'uuid'

5. Foreign Key
   - Links to another table
   - Establishes relationships

6. Indexes
   - Speed up queries
   - Trade-off: faster reads, slower writes
"""

# ============================================================
# 2. NORMALIZATION
# ============================================================

"""
Database Normalization Levels:

1NF (First Normal Form):
- No repeating groups
- Each cell contains single value
- Each column has unique name

2NF (Second Normal Form):
- Is in 1NF
- No partial dependencies
- Non-key columns depend on entire primary key

3NF (Third Normal Form):
- Is in 2NF
- No transitive dependencies
- Non-key columns depend only on primary key

Example: Before Normalization
+------------------------------------------+
| order_id | customer | product | category |
+------------------------------------------+
| 1        | John     | Laptop  | Electronics |
| 2        | John     | Phone   | Electronics |
+------------------------------------------+

After Normalization (3NF):

Customers Table:
+----+------+
| id | name |
+----+------+
| 1  | John |
+----+------+

Categories Table:
+----+-------------+
| id | name        |
+----+-------------+
| 1  | Electronics |
+----+-------------+

Products Table:
+----+--------+-------------+
| id | name   | category_id |
+----+--------+-------------+
| 1  | Laptop | 1           |
| 2  | Phone  | 1           |
+----+--------+-------------+

Orders Table:
+----+-------------+------------+
| id | customer_id | product_id |
+----+-------------+------------+
| 1  | 1           | 1          |
| 2  | 1           | 2          |
+----+-------------+------------+
"""

# ============================================================
# 3. RELATIONSHIPS
# ============================================================

"""
Types of Relationships:

1. One-to-One (1:1)
   - User has one Profile
   - Country has one Capital
   
   users             profiles
   +----+           +----+---------+
   | id |---1:1---| id | user_id |
   +----+           +----+---------+

2. One-to-Many (1:N)
   - User has many Orders
   - Category has many Products
   
   users             orders
   +----+           +----+---------+
   | id |---1:N---| id | user_id |
   +----+           +----+---------+

3. Many-to-Many (M:N)
   - Users have many Roles
   - Products have many Tags
   - Requires junction/pivot table
   
   users      user_roles      roles
   +----+    +---------+     +----+
   | id |----| user_id |-----| id |
   +----+    | role_id |     +----+
             +---------+
"""

# SQL Schema Examples
schema_examples = {
    "one_to_one": """
-- One-to-One: User has one Profile
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    full_name VARCHAR(255),
    bio TEXT,
    avatar_url VARCHAR(500)
);
""",

    "one_to_many": """
-- One-to-Many: User has many Orders
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    total_amount DECIMAL(10, 2),
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index for faster queries
CREATE INDEX idx_orders_user_id ON orders(user_id);
""",

    "many_to_many": """
-- Many-to-Many: Products have many Tags
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- Junction/Pivot table
CREATE TABLE product_tags (
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (product_id, tag_id)
);
"""
}

# ============================================================
# 4. COMMON SCHEMA PATTERNS
# ============================================================

"""
E-Commerce Schema Pattern:
"""

ecommerce_schema = """
-- Users and Authentication
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    parent_id INTEGER REFERENCES categories(id),
    slug VARCHAR(255) UNIQUE
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER DEFAULT 0,
    category_id INTEGER REFERENCES categories(id),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    status VARCHAR(50) DEFAULT 'pending',
    total_amount DECIMAL(10, 2),
    shipping_address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL
);

-- Reviews
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    product_id INTEGER REFERENCES products(id),
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, product_id)
);
"""

# ============================================================
# 5. DATA TYPES BEST PRACTICES
# ============================================================

data_type_recommendations = """
Common Data Types and When to Use:

INTEGERS:
- SERIAL/BIGSERIAL: Auto-incrementing IDs
- INTEGER: Counts, quantities
- BIGINT: Large numbers, timestamps in milliseconds

STRINGS:
- VARCHAR(n): Variable-length with max (emails, names)
- TEXT: Long text without limit (descriptions, comments)
- CHAR(n): Fixed-length (country codes, status codes)

NUMBERS:
- DECIMAL(10,2): Money (avoids floating-point errors)
- FLOAT/DOUBLE: Scientific calculations
- NUMERIC: High-precision calculations

DATES/TIMES:
- TIMESTAMP: Date and time (with timezone preferred)
- DATE: Just the date
- TIME: Just the time
- INTERVAL: Duration

BOOLEAN:
- BOOLEAN: True/False flags

JSON:
- JSON/JSONB: Flexible schema data (JSONB for querying)

UUID:
- UUID: Distributed unique IDs
"""

# ============================================================
# 6. INDEXING STRATEGIES
# ============================================================

"""
Indexing Best Practices:

1. Primary Key Index (Automatic)
   - Created automatically on primary key

2. Foreign Key Index (Manual)
   - Always index foreign keys for JOIN performance

3. Unique Index
   - For columns that must be unique (email)

4. Composite Index
   - For queries on multiple columns
   - Order matters: (user_id, created_at)

5. Partial Index
   - Index only specific rows
   - WHERE clause in index

6. Full-Text Index
   - For text search
"""

indexing_examples = """
-- Foreign Key Index (Important!)
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_products_category_id ON products(category_id);

-- Unique Index
CREATE UNIQUE INDEX idx_users_email ON users(email);

-- Composite Index (order matters!)
-- Useful for: WHERE user_id = 1 ORDER BY created_at DESC
CREATE INDEX idx_orders_user_created ON orders(user_id, created_at DESC);

-- Partial Index
-- Index only active products
CREATE INDEX idx_active_products ON products(name) WHERE is_active = TRUE;

-- Full-text search index
CREATE INDEX idx_products_search ON products USING gin(to_tsvector('english', name || ' ' || description));
"""

# ============================================================
# 7. QUERY OPTIMIZATION
# ============================================================

"""
Query Optimization Tips:

1. Use EXPLAIN ANALYZE to understand query plans
2. Select only needed columns (avoid SELECT *)
3. Use appropriate indexes
4. Avoid N+1 queries (use JOINs or eager loading)
5. Use LIMIT for pagination
6. Cache frequently accessed data
"""

# N+1 Problem Example
n_plus_one_problem = """
-- BAD: N+1 queries
-- 1 query to get users
SELECT * FROM users;
-- N queries to get orders for each user
SELECT * FROM orders WHERE user_id = 1;
SELECT * FROM orders WHERE user_id = 2;
...

-- GOOD: Single query with JOIN
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
ORDER BY u.id;

-- Or in ORM, use eager loading:
# Django: User.objects.prefetch_related('orders')
# SQLAlchemy: session.query(User).options(joinedload(User.orders))
"""

# ============================================================
# 8. SOFT DELETE PATTERN
# ============================================================

"""
Soft Delete vs Hard Delete:

Hard Delete: Actually removes the row
Soft Delete: Marks row as deleted, keeps data

Benefits of Soft Delete:
- Data recovery
- Audit trail
- Referential integrity maintained
"""

soft_delete_schema = """
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    is_deleted BOOLEAN DEFAULT FALSE,  -- Soft delete flag
    deleted_at TIMESTAMP,               -- When deleted
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Always filter out deleted records
CREATE VIEW active_users AS
SELECT * FROM users WHERE is_deleted = FALSE;

-- Soft delete query
UPDATE users SET is_deleted = TRUE, deleted_at = NOW() WHERE id = 1;

-- Restore deleted record
UPDATE users SET is_deleted = FALSE, deleted_at = NULL WHERE id = 1;
"""

# ============================================================
# 9. AUDIT LOGGING PATTERN
# ============================================================

"""
Audit Logging: Track all changes to important data
"""

audit_schema = """
-- Audit log table
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    table_name VARCHAR(100) NOT NULL,
    record_id INTEGER NOT NULL,
    action VARCHAR(20) NOT NULL,  -- INSERT, UPDATE, DELETE
    old_data JSONB,
    new_data JSONB,
    user_id INTEGER,
    ip_address VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger function for audit logging
CREATE OR REPLACE FUNCTION audit_trigger_function()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'DELETE' THEN
        INSERT INTO audit_logs (table_name, record_id, action, old_data)
        VALUES (TG_TABLE_NAME, OLD.id, 'DELETE', row_to_json(OLD)::jsonb);
        RETURN OLD;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO audit_logs (table_name, record_id, action, old_data, new_data)
        VALUES (TG_TABLE_NAME, NEW.id, 'UPDATE', row_to_json(OLD)::jsonb, row_to_json(NEW)::jsonb);
        RETURN NEW;
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO audit_logs (table_name, record_id, action, new_data)
        VALUES (TG_TABLE_NAME, NEW.id, 'INSERT', row_to_json(NEW)::jsonb);
        RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Apply trigger to users table
CREATE TRIGGER users_audit_trigger
AFTER INSERT OR UPDATE OR DELETE ON users
FOR EACH ROW EXECUTE FUNCTION audit_trigger_function();
"""

# ============================================================
# 10. SCHEMA MIGRATION BEST PRACTICES
# ============================================================

"""
Migration Best Practices:

1. Always use migration tools (Alembic, Django migrations)
2. Make migrations reversible (up and down)
3. Test migrations on copy of production data
4. Use transactions for safety
5. Add columns as nullable first, then backfill
6. Never drop columns directly in production
7. Use descriptive migration names
"""

migration_example = """
-- Adding a new column safely:

-- Step 1: Add nullable column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Step 2: Backfill data
UPDATE users SET phone = '' WHERE phone IS NULL;

-- Step 3: Add NOT NULL constraint (if needed)
ALTER TABLE users ALTER COLUMN phone SET NOT NULL;

-- Removing a column safely:

-- Step 1: Stop using the column in code
-- Step 2: Deploy code changes
-- Step 3: Wait for old processes to complete
-- Step 4: Drop the column
ALTER TABLE users DROP COLUMN old_column;
"""

# ============================================================
# 11. PYTHON ORM EXAMPLE (SQLAlchemy)
# ============================================================

"""
SQLAlchemy Model Example:
"""

sqlalchemy_example = '''
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    orders = relationship("Order", back_populates="user")
    profile = relationship("Profile", uselist=False, back_populates="user")

class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    full_name = Column(String(255))
    bio = Column(String)
    
    user = relationship("User", back_populates="profile")

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_amount = Column(Numeric(10, 2))
    status = Column(String(50), default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    
    order = relationship("Order", back_populates="items")
'''

# ============================================================
# SUMMARY
# ============================================================

"""
Database Schema Design Best Practices:

1. Normalize data (usually to 3NF)
2. Use appropriate data types
3. Always define primary keys
4. Create indexes for foreign keys and frequently queried columns
5. Use constraints (NOT NULL, UNIQUE, CHECK)
6. Plan for relationships (1:1, 1:N, M:N)
7. Consider soft deletes for important data
8. Implement audit logging for compliance
9. Use migrations for schema changes
10. Denormalize only when necessary for performance
"""

if __name__ == "__main__":
    print("Database Schema Design")
    print("=" * 50)
    
    print("\nRelationship Types:")
    print("1. One-to-One (1:1) - User has one Profile")
    print("2. One-to-Many (1:N) - User has many Orders")
    print("3. Many-to-Many (M:N) - Products have many Tags")
    
    print("\nNormalization Levels:")
    print("- 1NF: No repeating groups")
    print("- 2NF: No partial dependencies")
    print("- 3NF: No transitive dependencies")
    
    print("\nIndexing Tips:")
    print("- Always index foreign keys")
    print("- Use composite indexes for multi-column queries")
    print("- Consider partial indexes for filtered queries")
