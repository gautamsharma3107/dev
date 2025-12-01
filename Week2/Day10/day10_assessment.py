"""
DAY 10 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

This assessment tests your SQL knowledge with 10 queries to write.
Answer all questions. Good luck!
"""

import sqlite3

print("=" * 60)
print("DAY 10 ASSESSMENT TEST - SQL Essentials")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# Setup database for the test
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary REAL,
        hire_date TEXT,
        manager_id INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY,
        name TEXT,
        budget REAL,
        location TEXT
    )
""")

cursor.execute("""
    CREATE TABLE projects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department_id INTEGER,
        start_date TEXT,
        status TEXT
    )
""")

# Insert sample data
employees = [
    (1, 'Alice Johnson', 'Engineering', 95000, '2020-01-15', None),
    (2, 'Bob Smith', 'Engineering', 85000, '2021-03-20', 1),
    (3, 'Charlie Brown', 'Marketing', 72000, '2020-06-10', 4),
    (4, 'Diana Ross', 'Marketing', 88000, '2019-02-01', None),
    (5, 'Eve Wilson', 'Engineering', 78000, '2022-07-15', 1),
    (6, 'Frank Miller', 'Sales', 82000, '2021-01-10', 7),
    (7, 'Grace Lee', 'Sales', 92000, '2018-09-05', None),
    (8, 'Henry Davis', 'Engineering', 98000, '2017-11-20', 1),
    (9, 'Ivy Chen', 'Marketing', 65000, '2023-04-15', 4),
    (10, 'Jack Brown', 'HR', 68000, '2022-08-01', None),
]

departments = [
    (1, 'Engineering', 500000, 'Building A'),
    (2, 'Marketing', 200000, 'Building B'),
    (3, 'Sales', 300000, 'Building B'),
    (4, 'HR', 100000, 'Building C'),
    (5, 'Finance', 150000, 'Building A'),  # No employees
]

projects = [
    (1, 'Website Redesign', 1, '2024-01-01', 'active'),
    (2, 'Mobile App', 1, '2024-02-15', 'active'),
    (3, 'Marketing Campaign', 2, '2024-01-10', 'completed'),
    (4, 'Sales Portal', 3, '2024-03-01', 'active'),
    (5, 'HR System', 4, '2024-02-01', 'on_hold'),
]

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)", employees)
cursor.executemany("INSERT INTO departments VALUES (?, ?, ?, ?)", departments)
cursor.executemany("INSERT INTO projects VALUES (?, ?, ?, ?, ?)", projects)
conn.commit()

print("\n📊 Database Setup Complete!")
print("Tables: employees, departments, projects")
print("-" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What SQL keyword is used to retrieve data from a database?
a) GET
b) FETCH
c) SELECT
d) RETRIEVE

Your answer: """)

print("""
Q2. Which JOIN returns ALL rows from the left table and matching rows from the right?
a) INNER JOIN
b) RIGHT JOIN
c) LEFT JOIN
d) FULL JOIN

Your answer: """)

print("""
Q3. What does the WHERE clause do?
a) Sorts the results
b) Filters rows based on conditions
c) Groups rows together
d) Limits the number of rows

Your answer: """)

print("""
Q4. Which statement is used to modify existing data?
a) MODIFY
b) CHANGE
c) UPDATE
d) ALTER

Your answer: """)

print("""
Q5. What is the correct order of SQL clauses?
a) SELECT, FROM, ORDER BY, WHERE
b) SELECT, WHERE, FROM, ORDER BY
c) SELECT, FROM, WHERE, ORDER BY
d) FROM, SELECT, WHERE, ORDER BY

Your answer: """)

print("""
Q6. Which operator is used for pattern matching in SQL?
a) MATCH
b) LIKE
c) PATTERN
d) SIMILAR

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each - Write SQL queries
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

# Q7
print("""
Q7. (2 points) Write a query to select all employees from Engineering 
    department with salary > $80,000, ordered by salary descending.
""")

# YOUR QUERY HERE:
query7 = """
SELECT name, salary 
FROM employees 
WHERE department = 'Engineering' AND salary > 80000 
ORDER BY salary DESC
"""

print("Your query:")
print(f"   {query7.strip()}")
cursor.execute(query7)
results = cursor.fetchall()
print("\nExpected Result:")
for row in results:
    print(f"   {row['name']}: ${row['salary']:,.0f}")

# Q8
print("""
Q8. (2 points) Write a query using LEFT JOIN to show ALL departments 
    and count of employees in each (including departments with 0 employees).
""")

# YOUR QUERY HERE:
query8 = """
SELECT d.name as department, COUNT(e.id) as employee_count
FROM departments d
LEFT JOIN employees e ON d.name = e.department
GROUP BY d.id
ORDER BY employee_count DESC
"""

print("Your query:")
print(f"   {query8.strip()}")
cursor.execute(query8)
results = cursor.fetchall()
print("\nExpected Result:")
for row in results:
    print(f"   {row['department']}: {row['employee_count']} employees")

# Q9
print("""
Q9. (2 points) Write a query to find the department with the highest 
    average salary.
""")

# YOUR QUERY HERE:
query9 = """
SELECT department, ROUND(AVG(salary), 2) as avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1
"""

print("Your query:")
print(f"   {query9.strip()}")
cursor.execute(query9)
row = cursor.fetchone()
print("\nExpected Result:")
print(f"   {row['department']}: ${row['avg_salary']:,.2f}")

# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between INNER JOIN and LEFT JOIN.
     Give an example scenario for when you would use each.

Your answer:
""")

# Write your explanation here as comments:
# INNER JOIN: 
# 
# LEFT JOIN:
# 
# Example scenario:
#

# ============================================================
# BONUS CHALLENGE (Not graded)
# ============================================================

print("\n" + "=" * 60)
print("BONUS CHALLENGE (Optional)")
print("=" * 60)

print("""
Write the 10 SQL queries from Day 10's curriculum:
(These are just for practice - solutions provided below)
""")

print("\n1. SELECT all data from employees")
cursor.execute("SELECT * FROM employees")
print(f"   Result: {len(cursor.fetchall())} rows")

print("\n2. SELECT with WHERE (salary > 75000)")
cursor.execute("SELECT name, salary FROM employees WHERE salary > 75000")
print(f"   Result: {len(cursor.fetchall())} rows")

print("\n3. SELECT with ORDER BY (by hire_date)")
cursor.execute("SELECT name, hire_date FROM employees ORDER BY hire_date")
print(f"   Result: Ordered by hire date")

print("\n4. SELECT with LIMIT (top 3 salaries)")
cursor.execute("SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 3")
results = cursor.fetchall()
for row in results:
    print(f"      - {row['name']}: ${row['salary']:,.0f}")

print("\n5. INSERT new employee")
cursor.execute("""
    INSERT INTO employees (id, name, department, salary, hire_date)
    VALUES (11, 'Kate Williams', 'Engineering', 75000, '2024-01-01')
""")
print("   Result: 1 row inserted")

print("\n6. UPDATE salary")
cursor.execute("UPDATE employees SET salary = 80000 WHERE id = 11")
print("   Result: Salary updated")

print("\n7. DELETE employee")
cursor.execute("DELETE FROM employees WHERE id = 11")
print("   Result: 1 row deleted")

print("\n8. INNER JOIN employees and projects")
cursor.execute("""
    SELECT e.name, p.name as project
    FROM employees e
    INNER JOIN projects p ON e.department = (
        SELECT d.name FROM departments d WHERE d.id = p.department_id
    )
    LIMIT 5
""")
print(f"   Result: {len(cursor.fetchall())} matching rows")

print("\n9. LEFT JOIN all departments")
cursor.execute("""
    SELECT d.name, COUNT(e.id) as emp_count
    FROM departments d
    LEFT JOIN employees e ON d.name = e.department
    GROUP BY d.id
""")
results = cursor.fetchall()
for row in results:
    print(f"      - {row['name']}: {row['emp_count']}")

print("\n10. Aggregate query - AVG salary by department")
cursor.execute("""
    SELECT department, ROUND(AVG(salary), 2) as avg_sal
    FROM employees
    GROUP BY department
    ORDER BY avg_sal DESC
""")
results = cursor.fetchall()
for row in results:
    print(f"      - {row['department']}: ${row['avg_sal']:,.2f}")

conn.close()

# ============================================================
# ANSWER KEY
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: c) SELECT
Q2: c) LEFT JOIN
Q3: b) Filters rows based on conditions
Q4: c) UPDATE
Q5: c) SELECT, FROM, WHERE, ORDER BY
Q6: b) LIKE

Section B (Coding):
Q7: SELECT name, salary FROM employees 
    WHERE department = 'Engineering' AND salary > 80000 
    ORDER BY salary DESC

Q8: SELECT d.name, COUNT(e.id) as employee_count
    FROM departments d
    LEFT JOIN employees e ON d.name = e.department
    GROUP BY d.id

Q9: SELECT department, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
    ORDER BY avg_salary DESC
    LIMIT 1

Section C:
Q10: 
- INNER JOIN returns only rows that have matching values in BOTH tables.
  Use when you only want records that have a relationship.
  Example: Show only customers who have placed orders.

- LEFT JOIN returns ALL rows from the left table, and matching rows from 
  the right table. Non-matching rows have NULL values.
  Use when you want all records from one table, even without matches.
  Example: Show all customers, including those who haven't ordered.
"""
