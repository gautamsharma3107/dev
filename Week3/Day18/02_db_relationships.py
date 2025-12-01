"""
Day 18 - Database Relationships
===============================
Learn: One-to-Many, Many-to-Many relationships

Key Concepts:
- Foreign keys and referential integrity
- One-to-many relationships
- Many-to-many with junction tables
- JOIN queries to retrieve related data
"""

import sqlite3
import os

# ========== RELATIONSHIP TYPES ==========
print("=" * 60)
print("DATABASE RELATIONSHIP TYPES")
print("=" * 60)

print("""
1. ONE-TO-ONE: One record relates to exactly one record
   Example: User <-> Profile

2. ONE-TO-MANY: One record relates to many records
   Example: Author <-> Books (one author, many books)

3. MANY-TO-MANY: Many records relate to many records
   Example: Students <-> Courses (students take many courses,
            courses have many students)
""")

# Setup database
db_file = "relationships.db"
conn = sqlite3.connect(db_file)
conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
cursor = conn.cursor()
print(f"✅ Connected to {db_file}")

# ========== ONE-TO-MANY RELATIONSHIP ==========
print("\n" + "=" * 60)
print("ONE-TO-MANY: Authors and Books")
print("=" * 60)

# Drop existing tables
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("DROP TABLE IF EXISTS authors")

# Create parent table (one side)
cursor.execute("""
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT
)
""")
print("✅ Created 'authors' table")

# Create child table (many side) with foreign key
cursor.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
""")
print("✅ Created 'books' table with foreign key")

print("""
Schema:
┌───────────────┐       ┌───────────────────┐
│   authors     │       │      books        │
├───────────────┤       ├───────────────────┤
│ id (PK)       │──────<│ author_id (FK)    │
│ name          │       │ id (PK)           │
│ country       │       │ title             │
└───────────────┘       │ year              │
                        └───────────────────┘
""")

# Insert authors
authors = [
    ("J.K. Rowling", "UK"),
    ("George Orwell", "UK"),
    ("Haruki Murakami", "Japan"),
]
cursor.executemany(
    "INSERT INTO authors (name, country) VALUES (?, ?)",
    authors
)
conn.commit()
print(f"✅ Inserted {len(authors)} authors")

# Insert books (referencing authors)
books = [
    ("Harry Potter and the Sorcerer's Stone", 1997, 1),
    ("Harry Potter and the Chamber of Secrets", 1998, 1),
    ("Harry Potter and the Prisoner of Azkaban", 1999, 1),
    ("1984", 1949, 2),
    ("Animal Farm", 1945, 2),
    ("Norwegian Wood", 1987, 3),
    ("Kafka on the Shore", 2002, 3),
]
cursor.executemany(
    "INSERT INTO books (title, year, author_id) VALUES (?, ?, ?)",
    books
)
conn.commit()
print(f"✅ Inserted {len(books)} books")

# ========== JOIN QUERIES ==========
print("\n" + "=" * 60)
print("JOIN QUERIES")
print("=" * 60)

# INNER JOIN - only matching records
print("\n1. INNER JOIN (matching records only):")
cursor.execute("""
    SELECT books.title, authors.name
    FROM books
    INNER JOIN authors ON books.author_id = authors.id
    ORDER BY authors.name, books.year
""")
for row in cursor.fetchall():
    print(f"   '{row[0]}' by {row[1]}")

# LEFT JOIN - all from left table + matches
print("\n2. LEFT JOIN (all authors, even without books):")
# First, add an author without books
cursor.execute(
    "INSERT INTO authors (name, country) VALUES (?, ?)",
    ("New Author", "USA")
)
conn.commit()

cursor.execute("""
    SELECT authors.name, books.title
    FROM authors
    LEFT JOIN books ON authors.id = books.author_id
""")
for row in cursor.fetchall():
    book = row[1] if row[1] else "(no books)"
    print(f"   {row[0]}: {book}")

# Count books per author
print("\n3. Aggregate with GROUP BY:")
cursor.execute("""
    SELECT authors.name, COUNT(books.id) as book_count
    FROM authors
    LEFT JOIN books ON authors.id = books.author_id
    GROUP BY authors.id
    ORDER BY book_count DESC
""")
for row in cursor.fetchall():
    print(f"   {row[0]}: {row[1]} book(s)")

# ========== MANY-TO-MANY RELATIONSHIP ==========
print("\n" + "=" * 60)
print("MANY-TO-MANY: Students and Courses")
print("=" * 60)

# Drop existing tables
cursor.execute("DROP TABLE IF EXISTS enrollments")
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS courses")

# Create students table
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
)
""")

# Create courses table
cursor.execute("""
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    instructor TEXT
)
""")

# Create junction/bridge table for many-to-many
cursor.execute("""
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrolled_date DATE DEFAULT CURRENT_DATE,
    grade TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
)
""")
conn.commit()
print("✅ Created students, courses, and enrollments tables")

print("""
Schema:
┌────────────────┐       ┌─────────────────┐       ┌────────────────┐
│   students     │       │  enrollments    │       │    courses     │
├────────────────┤       ├─────────────────┤       ├────────────────┤
│ id (PK)        │──────<│ student_id (FK) │       │ id (PK)        │
│ name           │       │ course_id (FK)  │>──────│ name           │
│ email          │       │ enrolled_date   │       │ instructor     │
└────────────────┘       │ grade           │       └────────────────┘
                         └─────────────────┘
""")

# Insert students
students = [
    ("Alice Johnson", "alice@university.edu"),
    ("Bob Smith", "bob@university.edu"),
    ("Charlie Brown", "charlie@university.edu"),
]
cursor.executemany(
    "INSERT INTO students (name, email) VALUES (?, ?)",
    students
)

# Insert courses
courses = [
    ("Python Programming", "Dr. Smith"),
    ("Data Science", "Dr. Johnson"),
    ("Web Development", "Dr. Williams"),
]
cursor.executemany(
    "INSERT INTO courses (name, instructor) VALUES (?, ?)",
    courses
)

# Create enrollments (many-to-many relationships)
enrollments = [
    (1, 1, "2024-01-15", "A"),   # Alice in Python
    (1, 2, "2024-01-15", "B+"),  # Alice in Data Science
    (2, 1, "2024-01-16", "A-"),  # Bob in Python
    (2, 3, "2024-01-16", "B"),   # Bob in Web Dev
    (3, 1, "2024-01-17", "B+"),  # Charlie in Python
    (3, 2, "2024-01-17", "A"),   # Charlie in Data Science
    (3, 3, "2024-01-17", "A-"),  # Charlie in Web Dev
]
cursor.executemany(
    "INSERT INTO enrollments (student_id, course_id, enrolled_date, grade) VALUES (?, ?, ?, ?)",
    enrollments
)
conn.commit()
print(f"✅ Inserted students, courses, and enrollments")

# ========== MANY-TO-MANY QUERIES ==========
print("\n" + "=" * 60)
print("MANY-TO-MANY QUERIES")
print("=" * 60)

# Get all enrollments with details
print("\n1. All enrollments with student and course names:")
cursor.execute("""
    SELECT s.name, c.name, e.grade
    FROM enrollments e
    JOIN students s ON e.student_id = s.id
    JOIN courses c ON e.course_id = c.id
    ORDER BY s.name, c.name
""")
for row in cursor.fetchall():
    print(f"   {row[0]} - {row[1]}: {row[2]}")

# Courses for a specific student
print("\n2. Courses for 'Alice Johnson':")
cursor.execute("""
    SELECT c.name, c.instructor, e.grade
    FROM courses c
    JOIN enrollments e ON c.id = e.course_id
    JOIN students s ON e.student_id = s.id
    WHERE s.name = 'Alice Johnson'
""")
for row in cursor.fetchall():
    print(f"   {row[0]} (Instructor: {row[1]}) - Grade: {row[2]}")

# Students in a specific course
print("\n3. Students in 'Python Programming':")
cursor.execute("""
    SELECT s.name, s.email, e.grade
    FROM students s
    JOIN enrollments e ON s.id = e.student_id
    JOIN courses c ON e.course_id = c.id
    WHERE c.name = 'Python Programming'
""")
for row in cursor.fetchall():
    print(f"   {row[0]} ({row[1]}) - Grade: {row[2]}")

# Count students per course
print("\n4. Student count per course:")
cursor.execute("""
    SELECT c.name, COUNT(e.student_id) as student_count
    FROM courses c
    LEFT JOIN enrollments e ON c.id = e.course_id
    GROUP BY c.id
    ORDER BY student_count DESC
""")
for row in cursor.fetchall():
    print(f"   {row[0]}: {row[1]} students")

# ========== FOREIGN KEY CONSTRAINTS ==========
print("\n" + "=" * 60)
print("FOREIGN KEY CONSTRAINTS")
print("=" * 60)

print("""
ON DELETE options:
- CASCADE: Delete related records automatically
- SET NULL: Set foreign key to NULL
- RESTRICT: Prevent deletion if references exist
- NO ACTION: Similar to RESTRICT (default)

ON UPDATE options:
- CASCADE: Update foreign key automatically
- SET NULL: Set foreign key to NULL
- RESTRICT: Prevent update if references exist
""")

# Demonstrate CASCADE delete
print("\nDemonstrating CASCADE delete:")
cursor.execute("SELECT COUNT(*) FROM enrollments WHERE student_id = 1")
before = cursor.fetchone()[0]
print(f"   Enrollments for student 1 before delete: {before}")

cursor.execute("DELETE FROM students WHERE id = 1")
conn.commit()

cursor.execute("SELECT COUNT(*) FROM enrollments WHERE student_id = 1")
after = cursor.fetchone()[0]
print(f"   Enrollments for student 1 after delete: {after}")
print("   ✅ Related enrollments were automatically deleted!")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Blog Database")
print("=" * 60)

# Drop existing tables
for table in ["comments", "post_tags", "tags", "posts", "users_blog"]:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Users table
cursor.execute("""
CREATE TABLE users_blog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

# Posts table (one-to-many with users)
cursor.execute("""
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    author_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users_blog(id) ON DELETE CASCADE
)
""")

# Tags table
cursor.execute("""
CREATE TABLE tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
""")

# Post-Tags junction table (many-to-many)
cursor.execute("""
CREATE TABLE post_tags (
    post_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
)
""")

# Comments table (one-to-many with posts)
cursor.execute("""
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES users_blog(id) ON DELETE CASCADE
)
""")
conn.commit()
print("✅ Created blog database schema")

# Insert sample data
cursor.executemany(
    "INSERT INTO users_blog (username, email) VALUES (?, ?)",
    [("john_doe", "john@blog.com"), ("jane_smith", "jane@blog.com")]
)
cursor.executemany(
    "INSERT INTO tags (name) VALUES (?)",
    [("Python",), ("Web",), ("Database",), ("Tutorial",)]
)
cursor.executemany(
    "INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)",
    [
        ("Learning Python", "Python is great...", 1),
        ("SQL Basics", "Understanding databases...", 1),
        ("Web Development", "Building modern apps...", 2),
    ]
)
cursor.executemany(
    "INSERT INTO post_tags (post_id, tag_id) VALUES (?, ?)",
    [(1, 1), (1, 4), (2, 3), (2, 4), (3, 2), (3, 1)]
)
cursor.executemany(
    "INSERT INTO comments (post_id, author_id, content) VALUES (?, ?, ?)",
    [
        (1, 2, "Great article!"),
        (1, 2, "Very helpful, thanks!"),
        (2, 2, "Nice explanation"),
    ]
)
conn.commit()

# Complex query: Posts with author, tags, and comment count
print("\nBlog posts with details:")
cursor.execute("""
    SELECT 
        p.title,
        u.username as author,
        GROUP_CONCAT(DISTINCT t.name) as tags,
        COUNT(DISTINCT c.id) as comment_count
    FROM posts p
    JOIN users_blog u ON p.author_id = u.id
    LEFT JOIN post_tags pt ON p.id = pt.post_id
    LEFT JOIN tags t ON pt.tag_id = t.id
    LEFT JOIN comments c ON p.id = c.post_id
    GROUP BY p.id
""")
print(f"{'Title':<20} {'Author':<12} {'Tags':<25} {'Comments'}")
print("-" * 65)
for row in cursor.fetchall():
    print(f"{row[0]:<20} {row[1]:<12} {row[2] or 'None':<25} {row[3]}")

# ========== CLEANUP ==========
print("\n" + "=" * 60)
print("CLEANUP")
print("=" * 60)

conn.close()
if os.path.exists(db_file):
    os.remove(db_file)
print("✅ Database closed and removed")

print("\n" + "=" * 60)
print("✅ Database Relationships - Complete!")
print("=" * 60)
