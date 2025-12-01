# Day 10 Quick Reference Cheat Sheet - SQL Essentials

## Database Basics
```sql
-- Database: Organized collection of data
-- Table: Collection of rows and columns
-- Row (Record): Single data entry
-- Column (Field): Attribute of data
-- Primary Key: Unique identifier for each row
-- Foreign Key: Links tables together
```

## Creating Tables
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## SELECT Queries
```sql
-- Basic SELECT
SELECT * FROM users;                    -- All columns
SELECT name, email FROM users;          -- Specific columns
SELECT DISTINCT city FROM users;        -- Unique values

-- Column aliases
SELECT name AS full_name FROM users;
```

## WHERE Clause (Filtering)
```sql
-- Comparison operators
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE name = 'John';
SELECT * FROM users WHERE age >= 18;
SELECT * FROM users WHERE age <> 25;    -- Not equal

-- Logical operators
SELECT * FROM users WHERE age > 25 AND city = 'NYC';
SELECT * FROM users WHERE age < 18 OR age > 65;
SELECT * FROM users WHERE NOT active;

-- BETWEEN
SELECT * FROM products WHERE price BETWEEN 10 AND 50;

-- IN
SELECT * FROM users WHERE city IN ('NYC', 'LA', 'Chicago');

-- LIKE (Pattern matching)
SELECT * FROM users WHERE name LIKE 'J%';      -- Starts with J
SELECT * FROM users WHERE name LIKE '%son';    -- Ends with son
SELECT * FROM users WHERE name LIKE '%a%';     -- Contains a
SELECT * FROM users WHERE name LIKE '_ohn';    -- Second char onwards 'ohn'

-- NULL checks
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

## ORDER BY (Sorting)
```sql
SELECT * FROM users ORDER BY name;            -- Ascending (default)
SELECT * FROM users ORDER BY age DESC;        -- Descending
SELECT * FROM users ORDER BY city, name;      -- Multiple columns
SELECT * FROM users ORDER BY age DESC, name ASC;
```

## LIMIT (Pagination)
```sql
SELECT * FROM users LIMIT 10;                 -- First 10 rows
SELECT * FROM users LIMIT 5 OFFSET 10;        -- 5 rows, skip first 10
SELECT * FROM users ORDER BY age DESC LIMIT 5; -- Top 5 oldest
```

## INSERT (Adding Data)
```sql
-- Single row
INSERT INTO users (name, email, age)
VALUES ('John', 'john@email.com', 25);

-- Multiple rows
INSERT INTO users (name, email, age)
VALUES 
    ('Alice', 'alice@email.com', 30),
    ('Bob', 'bob@email.com', 28);

-- All columns (if providing all values)
INSERT INTO users VALUES (1, 'John', 'john@email.com', 25);
```

## UPDATE (Modifying Data)
```sql
-- Update single column
UPDATE users SET age = 26 WHERE name = 'John';

-- Update multiple columns
UPDATE users SET age = 27, city = 'NYC' WHERE id = 1;

-- Update with calculation
UPDATE products SET price = price * 1.1;  -- 10% increase

-- IMPORTANT: Always use WHERE clause!
UPDATE users SET active = 0 WHERE last_login < '2023-01-01';
```

## DELETE (Removing Data)
```sql
-- Delete specific rows
DELETE FROM users WHERE age < 18;

-- Delete with multiple conditions
DELETE FROM users WHERE status = 'inactive' AND created_at < '2022-01-01';

-- IMPORTANT: Always use WHERE clause!
-- DELETE FROM users;  -- This deletes ALL rows!
```

## INNER JOIN
```sql
-- Returns only matching rows from both tables
SELECT users.name, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- With aliases
SELECT u.name, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- Multiple joins
SELECT u.name, o.amount, p.name AS product
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN products p ON o.product_id = p.id;
```

## LEFT JOIN
```sql
-- Returns all rows from left table, matching from right
-- Non-matching rows have NULL values
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- Find users with no orders
SELECT users.name
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.id IS NULL;
```

## Aggregate Functions
```sql
SELECT COUNT(*) FROM users;                    -- Count rows
SELECT COUNT(DISTINCT city) FROM users;        -- Count unique
SELECT SUM(amount) FROM orders;                -- Sum
SELECT AVG(age) FROM users;                    -- Average
SELECT MAX(price) FROM products;               -- Maximum
SELECT MIN(price) FROM products;               -- Minimum

-- GROUP BY
SELECT city, COUNT(*) FROM users GROUP BY city;
SELECT city, AVG(age) FROM users GROUP BY city;

-- HAVING (filter after GROUP BY)
SELECT city, COUNT(*) as count
FROM users
GROUP BY city
HAVING count > 5;
```

## Common Patterns
```sql
-- Get top N items
SELECT * FROM products ORDER BY price DESC LIMIT 5;

-- Get second highest
SELECT * FROM products ORDER BY price DESC LIMIT 1 OFFSET 1;

-- Count per category
SELECT category, COUNT(*) FROM products GROUP BY category;

-- Find duplicates
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;

-- Search with multiple conditions
SELECT * FROM products
WHERE price < 100 AND category = 'Electronics'
ORDER BY name;
```

## Python SQLite3 Quick Reference
```python
import sqlite3

# Connect to database
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Execute with parameters (SAFE from SQL injection)
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
user = cursor.fetchone()

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
               ('John', 'john@email.com'))
conn.commit()

# Close connection
conn.close()
```

---
**Keep this handy for quick reference!** 🚀
