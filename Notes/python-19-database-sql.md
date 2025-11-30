# Database Fundamentals & SQL Basics: Complete Guide

---

## Table of Contents
1. [Introduction to Databases](#introduction-to-databases)
2. [Database Concepts](#database-concepts)
3. [SQL Syntax Basics](#sql-syntax-basics)
4. [CRUD Operations](#crud-operations)
5. [SELECT Queries and WHERE Clauses](#select-queries-and-where-clauses)
6. [Joins](#joins)
7. [Aggregation Functions](#aggregation-functions)
8. [Constraints](#constraints)
9. [Indexes and Optimization](#indexes-and-optimization)
10. [Transactions and ACID](#transactions-and-acid)
11. [Normalization](#normalization)
12. [Practical Examples](#practical-examples)
13. [Practice Exercises](#practice-exercises)

---

## Introduction to Databases

### What is a Database?

A database is an organized collection of structured data stored and accessed electronically.

### Why Databases?

1. **Persistence** - Data survives program termination
2. **Scalability** - Handle large amounts of data
3. **Efficiency** - Quick search and retrieval
4. **Integrity** - Data consistency and validation
5. **Security** - Access control and encryption
6. **Concurrency** - Multiple users simultaneously

### Database Types

```
Relational (SQL):
├── MySQL
├── PostgreSQL
├── SQL Server
├── SQLite
└── Oracle

NoSQL:
├── MongoDB (Document)
├── Redis (Key-Value)
├── Neo4j (Graph)
└── Cassandra (Column-Family)
```

---

## Database Concepts

### Tables, Rows, and Columns

```
Table: Users
┌────┬──────────┬────────┬──────────────────────┐
│ ID │ Name     │ Age    │ Email                │
├────┼──────────┼────────┼──────────────────────┤
│ 1  │ Alice    │ 25     │ alice@example.com    │  <- Row
│ 2  │ Bob      │ 30     │ bob@example.com      │
│ 3  │ Charlie  │ 28     │ charlie@example.com  │
└────┴──────────┴────────┴──────────────────────┘
 ▲      ▲        ▲        ▲
 │      │        │        │
 └─ Columns ─────────────────┘
```

### Database Schema

```
Database Name: company
├── employees (table)
│   ├── id (column)
│   ├── name (column)
│   ├── department (column)
│   └── salary (column)
├── departments (table)
│   ├── id (column)
│   ├── name (column)
│   └── budget (column)
└── projects (table)
    ├── id (column)
    ├── name (column)
    └── department_id (column)
```

### Data Types

```sql
-- Common SQL Data Types

-- Numeric
INT, INTEGER, BIGINT, SMALLINT  -- Whole numbers
FLOAT, DECIMAL, NUMERIC         -- Decimal numbers

-- Text
CHAR(n)           -- Fixed-length string
VARCHAR(n)        -- Variable-length string
TEXT              -- Large text

-- Date/Time
DATE              -- YYYY-MM-DD
TIME              -- HH:MM:SS
DATETIME          -- YYYY-MM-DD HH:MM:SS
TIMESTAMP         -- Automatic timestamp

-- Boolean
BOOLEAN, BOOL     -- TRUE or FALSE

-- Special
JSON              -- JSON data
UUID              -- Unique identifier
```

---

## SQL Syntax Basics

### Case Sensitivity

```sql
-- SQL keywords (case-insensitive, but convention is UPPERCASE)
SELECT * FROM users;
select * from users;
SeLeCt * FrOm users;
-- All three are valid, but first is preferred
```

### Comments

```sql
-- Single line comment

/* 
   Multi-line
   comment
*/

/*! MySQL-specific syntax */
```

### Statement Structure

```sql
SELECT column1, column2
FROM table_name
WHERE condition
GROUP BY column1
HAVING condition
ORDER BY column1
LIMIT 10;
```

---

## CRUD Operations

### CREATE (INSERT)

```sql
-- Insert single row
INSERT INTO users (id, name, age, email)
VALUES (1, 'Alice', 25, 'alice@example.com');

-- Insert multiple rows
INSERT INTO users (id, name, age, email)
VALUES 
  (1, 'Alice', 25, 'alice@example.com'),
  (2, 'Bob', 30, 'bob@example.com'),
  (3, 'Charlie', 28, 'charlie@example.com');

-- Insert without specifying columns (must provide all)
INSERT INTO users
VALUES (1, 'Alice', 25, 'alice@example.com');

-- Insert with default values
INSERT INTO users (id, name)
VALUES (1, 'Alice');
-- age and email will be NULL or default
```

### READ (SELECT)

```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT name, email FROM users;

-- Select with alias
SELECT name AS full_name, email FROM users;

-- Select distinct values
SELECT DISTINCT department FROM employees;

-- Count rows
SELECT COUNT(*) FROM users;
```

### UPDATE

```sql
-- Update single row
UPDATE users
SET age = 26
WHERE id = 1;

-- Update multiple columns
UPDATE users
SET age = 26, email = 'alice.new@example.com'
WHERE id = 1;

-- Update multiple rows
UPDATE users
SET age = age + 1
WHERE department = 'IT';

-- Update all rows (be careful!)
UPDATE users SET active = 1;
```

### DELETE

```sql
-- Delete specific row
DELETE FROM users
WHERE id = 1;

-- Delete multiple rows
DELETE FROM users
WHERE age > 60;

-- Delete all rows (be careful!)
DELETE FROM users;

-- Truncate (faster, but cannot rollback)
TRUNCATE TABLE users;
```

---

## SELECT Queries and WHERE Clauses

### Basic WHERE Conditions

```sql
-- Equal
SELECT * FROM users WHERE age = 25;

-- Not equal
SELECT * FROM users WHERE age != 25;
SELECT * FROM users WHERE age <> 25;

-- Greater than
SELECT * FROM users WHERE age > 25;

-- Less than or equal
SELECT * FROM users WHERE age <= 25;

-- Between
SELECT * FROM users WHERE age BETWEEN 20 AND 30;

-- In list
SELECT * FROM users WHERE department IN ('IT', 'HR', 'Sales');

-- Is NULL
SELECT * FROM users WHERE phone IS NULL;

-- Is NOT NULL
SELECT * FROM users WHERE phone IS NOT NULL;
```

### Logical Operators

```sql
-- AND
SELECT * FROM users 
WHERE age > 25 AND department = 'IT';

-- OR
SELECT * FROM users 
WHERE age > 25 OR department = 'IT';

-- NOT
SELECT * FROM users 
WHERE NOT age > 25;

-- Complex conditions
SELECT * FROM users
WHERE (age > 25 AND department = 'IT') 
   OR (age < 30 AND department = 'HR');
```

### LIKE (Pattern Matching)

```sql
-- Starts with 'A'
SELECT * FROM users WHERE name LIKE 'A%';

-- Contains 'ice'
SELECT * FROM users WHERE name LIKE '%ice%';

-- Ends with 'ce'
SELECT * FROM users WHERE name LIKE '%ce';

-- Specific pattern (A followed by 2 characters)
SELECT * FROM users WHERE name LIKE 'A__';

-- Case-insensitive pattern
SELECT * FROM users WHERE name LIKE 'alice' COLLATE NOCASE;
```

### Ordering and Limiting

```sql
-- Order ascending (default)
SELECT * FROM users ORDER BY age;
SELECT * FROM users ORDER BY age ASC;

-- Order descending
SELECT * FROM users ORDER BY age DESC;

-- Order by multiple columns
SELECT * FROM users ORDER BY department ASC, age DESC;

-- Limit results
SELECT * FROM users LIMIT 10;

-- Limit with offset
SELECT * FROM users LIMIT 10 OFFSET 5;
-- Get rows 6-15 (skip first 5)

-- Pagination (page 2, 10 items per page)
SELECT * FROM users LIMIT 10 OFFSET 10;
```

---

## Joins

### INNER JOIN

```sql
-- Syntax
SELECT users.name, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- Only returns matching rows from both tables

-- Example data:
-- users: id=1 (Alice), id=2 (Bob), id=3 (Charlie)
-- orders: user_id=1 (amount=100), user_id=2 (amount=200)

-- Result:
-- Alice, 100
-- Bob, 200
-- (Charlie has no orders, so not included)
```

### LEFT JOIN

```sql
-- Syntax
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- Returns all rows from LEFT table (users)
-- and matching rows from RIGHT table (orders)

-- Result:
-- Alice, 100
-- Bob, 200
-- Charlie, NULL (no orders)
```

### RIGHT JOIN

```sql
-- Syntax
SELECT users.name, orders.amount
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;

-- Returns all rows from RIGHT table (orders)
-- and matching rows from LEFT table (users)

-- Result:
-- Alice, 100
-- Bob, 200
```

### FULL OUTER JOIN

```sql
-- Syntax
SELECT users.name, orders.amount
FROM users
FULL OUTER JOIN orders ON users.id = orders.user_id;

-- Returns all rows from both tables
-- (not supported in MySQL, use UNION instead)

-- MySQL equivalent:
SELECT users.name, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id
UNION
SELECT users.name, orders.amount
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;
```

### Self Join

```sql
-- Find employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

### Multiple Joins

```sql
SELECT users.name, orders.amount, products.name
FROM users
INNER JOIN orders ON users.id = orders.user_id
INNER JOIN products ON orders.product_id = products.id;
```

---

## Aggregation Functions

### Basic Aggregations

```sql
-- COUNT - count rows
SELECT COUNT(*) FROM users;
SELECT COUNT(email) FROM users;  -- Counts non-NULL values

-- SUM - sum values
SELECT SUM(salary) FROM employees;

-- AVG - average
SELECT AVG(salary) FROM employees;

-- MIN - minimum
SELECT MIN(salary) FROM employees;

-- MAX - maximum
SELECT MAX(salary) FROM employees;
```

### GROUP BY

```sql
-- Group by department
SELECT department, COUNT(*) as count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;

-- Multiple grouping
SELECT department, job_title, COUNT(*), AVG(salary)
FROM employees
GROUP BY department, job_title;

-- With ORDER BY
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
```

### HAVING

```sql
-- Filter groups (WHERE filters rows, HAVING filters groups)
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- Multiple conditions
SELECT department, COUNT(*) as dept_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5 AND AVG(salary) > 40000;
```

### Advanced Aggregations

```sql
-- STRING_AGG / GROUP_CONCAT - concatenate strings
SELECT department, GROUP_CONCAT(name, ', ') as employees
FROM employees
GROUP BY department;

-- DISTINCT in aggregation
SELECT COUNT(DISTINCT department) as dept_count
FROM employees;

-- Conditional aggregation
SELECT 
  COUNT(CASE WHEN age > 30 THEN 1 END) as over_30,
  COUNT(CASE WHEN age <= 30 THEN 1 END) as under_30
FROM users;
```

---

## Constraints

### PRIMARY KEY

```sql
-- Single column primary key
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

-- Multi-column primary key
CREATE TABLE enrollments (
  student_id INT,
  course_id INT,
  PRIMARY KEY (student_id, course_id)
);

-- Add after creation
ALTER TABLE users ADD PRIMARY KEY (id);
```

### FOREIGN KEY

```sql
-- Define foreign key
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  amount DECIMAL(10, 2),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Cascading delete
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  amount DECIMAL(10, 2),
  FOREIGN KEY (user_id) REFERENCES users(id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);
```

### UNIQUE Constraint

```sql
-- Single column unique
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE
);

-- Multiple columns unique
CREATE TABLE users (
  id INT PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  UNIQUE (first_name, last_name)
);
```

### NOT NULL Constraint

```sql
CREATE TABLE users (
  id INT PRIMARY KEY NOT NULL,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100),
  age INT
);
```

### CHECK Constraint

```sql
CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  age INT CHECK (age >= 18),
  salary DECIMAL(10, 2) CHECK (salary > 0)
);
```

### DEFAULT Constraint

```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  active BOOLEAN DEFAULT TRUE
);
```

---

## Indexes and Optimization

### Creating Indexes

```sql
-- Single column index
CREATE INDEX idx_email ON users(email);

-- Multi-column index
CREATE INDEX idx_dept_salary ON employees(department, salary);

-- Unique index
CREATE UNIQUE INDEX idx_unique_email ON users(email);

-- Composite index for specific query
-- For query: SELECT * FROM users WHERE name LIKE '%alice%' AND age > 25
CREATE INDEX idx_name_age ON users(name, age);
```

### Using Indexes

```sql
-- Index speeds up this query
SELECT * FROM users WHERE email = 'alice@example.com';

-- Index helps with sorting
SELECT * FROM employees ORDER BY salary;

-- Index with range query
SELECT * FROM orders WHERE amount > 1000 AND amount < 5000;
```

### Index Types

```sql
-- BTREE (default)
CREATE INDEX idx_name ON users(name) USING BTREE;

-- HASH (faster for exact matches, not range)
CREATE INDEX idx_email ON users(email) USING HASH;

-- FULLTEXT (text searching)
CREATE FULLTEXT INDEX idx_content ON articles(content);
```

### Dropping Indexes

```sql
DROP INDEX idx_email ON users;

-- Or
DROP INDEX idx_email;
```

### Query Optimization Tips

```sql
-- ✓ Good: Use indexes
SELECT * FROM users WHERE email = 'alice@example.com';

-- ✗ Bad: Function on indexed column prevents index use
SELECT * FROM users WHERE UPPER(email) = 'ALICE@EXAMPLE.COM';

-- ✓ Good: Index-friendly WHERE clause
SELECT * FROM users WHERE age > 25 AND department = 'IT';

-- ✗ Bad: OR between unindexed conditions
SELECT * FROM users WHERE phone IS NULL OR email IS NULL;

-- ✓ Good: Specific SELECT
SELECT name, email FROM users;

-- ✗ Bad: SELECT * (unnecessary columns)
SELECT * FROM users;
```

---

## Transactions and ACID

### ACID Properties

```
Atomicity      - All or nothing (all changes committed or none)
Consistency    - Database moves from one valid state to another
Isolation      - Concurrent transactions don't interfere
Durability     - Committed data persists even after failure
```

### Transaction Control

```sql
-- Start transaction
BEGIN;
-- or
START TRANSACTION;

-- Do operations
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit (save changes)
COMMIT;

-- Or rollback (undo changes)
ROLLBACK;
```

### Example: Bank Transfer

```sql
-- Transfer $100 from account 1 to account 2
BEGIN;

-- Deduct from account 1
UPDATE accounts 
SET balance = balance - 100 
WHERE id = 1;

-- Add to account 2
UPDATE accounts 
SET balance = balance + 100 
WHERE id = 2;

-- If both succeeded, commit
COMMIT;

-- If error occurred, rollback
ROLLBACK;
```

### Isolation Levels

```sql
-- READ UNCOMMITTED (dirty reads possible)
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

-- READ COMMITTED (default for many databases)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- REPEATABLE READ
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- SERIALIZABLE (strictest)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

## Normalization

### What is Normalization?

Normalization is the process of organizing database tables to minimize data redundancy.

### Normal Forms

```
1NF (First Normal Form)
├── Eliminate repeating groups
└── Each column contains atomic (indivisible) values

2NF (Second Normal Form)
├── Must be in 1NF
└── Remove partial dependencies

3NF (Third Normal Form)
├── Must be in 2NF
└── Remove transitive dependencies

BCNF (Boyce-Codd Normal Form)
├── Must be in 3NF
└── Every determinant is a candidate key
```

### Before Normalization (Denormalized)

```
Table: Employees
┌─────┬──────────┬───────────────────────┬───────────────────┐
│ ID  │ Name     │ Departments           │ Skills            │
├─────┼──────────┼───────────────────────┼───────────────────┤
│ 1   │ Alice    │ IT, HR                │ Python, Java, SQL │
│ 2   │ Bob      │ Sales                 │ Communication     │
└─────┴──────────┴───────────────────────┴───────────────────┘

Problems:
- Repeating groups (multiple departments, skills)
- Data redundancy
- Update anomalies
```

### After Normalization (1NF)

```
Table: Employees
┌─────┬──────────┐
│ ID  │ Name     │
├─────┼──────────┤
│ 1   │ Alice    │
│ 2   │ Bob      │
└─────┴──────────┘

Table: EmployeeDepartments
┌──────────────┬──────────────┐
│ Employee_ID  │ Department   │
├──────────────┼──────────────┤
│ 1            │ IT           │
│ 1            │ HR           │
│ 2            │ Sales        │
└──────────────┴──────────────┘

Table: Skills
┌──────────────┬──────────────┐
│ Employee_ID  │ Skill        │
├──────────────┼──────────────┤
│ 1            │ Python       │
│ 1            │ Java         │
│ 1            │ SQL          │
│ 2            │ Communication
└──────────────┴──────────────┘
```

### Normalization Example (1NF to 3NF)

```sql
-- Start: Unnormalized
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  address VARCHAR(200),
  courses VARCHAR(200)  -- "Math, Physics, Chemistry"
);

-- 1NF: Eliminate repeating groups
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  address VARCHAR(200)
);

CREATE TABLE enrollments (
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  course_id INT,
  FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 2NF: Remove partial dependencies
CREATE TABLE courses (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  credits INT
);

-- 3NF: Remove transitive dependencies
-- Address contains city and zip, separate them
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  city_id INT,
  FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE cities (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  zip VARCHAR(10)
);
```

### Denormalization (Intentional)

```sql
-- Sometimes we denormalize for performance
-- Trade storage space for query speed

-- Denormalized: store total in orders
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  order_date DATE,
  total DECIMAL(10, 2)  -- Calculated/denormalized
);

-- This avoids summing all order items for reporting
-- But requires updating total whenever item is added
```

---

## Practical Examples

### Creating a Complete Database

```sql
-- Database for online store

-- Users table
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone VARCHAR(20),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  active BOOLEAN DEFAULT TRUE
);

-- Products table
CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(200) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
  stock INT DEFAULT 0,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2),
  status VARCHAR(50) DEFAULT 'pending',
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Order items table
CREATE TABLE order_items (
  id INT PRIMARY KEY AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL CHECK (quantity > 0),
  price DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id),
  UNIQUE (order_id, product_id)
);

-- Create indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
```

### Complex Queries

```sql
-- Get total spent by each user
SELECT 
  u.name,
  COUNT(o.id) as order_count,
  SUM(o.total) as total_spent,
  AVG(o.total) as avg_order
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
ORDER BY total_spent DESC;

-- Find products never ordered
SELECT p.id, p.name
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.id IS NULL;

-- Get users who spent more than $1000
SELECT u.name, SUM(o.total) as total_spent
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
HAVING SUM(o.total) > 1000
ORDER BY total_spent DESC;

-- Top 3 products by quantity sold
SELECT 
  p.name,
  SUM(oi.quantity) as total_quantity,
  SUM(oi.quantity * oi.price) as revenue
FROM products p
JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name
ORDER BY total_quantity DESC
LIMIT 3;
```

---

## Practice Exercises

### 1. Database Design
- Design a library management database
- Design an employee management system
- Design a social media database

### 2. CRUD Operations
- Insert sample data
- Update records
- Delete with conditions
- Query with multiple conditions

### 3. Joins
- Practice INNER JOIN
- Practice LEFT/RIGHT JOIN
- Practice multiple joins
- Self-join examples

### 4. Aggregations
- GROUP BY queries
- HAVING clauses
- Complex aggregations
- Window functions (if available)

### 5. Optimization
- Create appropriate indexes
- Analyze query performance
- Optimize slow queries
- Understand query plans

### 6. Normalization
- Normalize unnormalized data
- Identify normal form violations
- Design normalized schemas
- Understand trade-offs

### 7. Transactions
- Implement transaction control
- Handle rollbacks
- Ensure data consistency
- Test concurrent access

### 8. Real-World Scenarios
- Build e-commerce database
- Implement inventory system
- Create reporting queries
- Handle complex business logic

---

# End of Notes
