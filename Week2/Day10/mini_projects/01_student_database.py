"""
Day 10 - Mini Project 1: Student Database
==========================================
Build a simple student management system using SQL.

Features:
- Create students and courses tables
- Add students and assign them to courses
- Query students by course, GPA, etc.
- Generate simple reports
"""

import sqlite3

print("=" * 60)
print("STUDENT DATABASE - Mini Project")
print("=" * 60)

# Create database
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# ========== STEP 1: CREATE TABLES ==========
print("\n📋 Step 1: Creating database schema...")
print("-" * 40)

# Students table
cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER,
        gpa REAL,
        enrollment_date TEXT
    )
""")
print("   ✅ Created 'students' table")

# Courses table
cursor.execute("""
    CREATE TABLE courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        code TEXT UNIQUE,
        credits INTEGER,
        instructor TEXT
    )
""")
print("   ✅ Created 'courses' table")

# Enrollments table (links students to courses)
cursor.execute("""
    CREATE TABLE enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        grade TEXT,
        enrolled_date TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
""")
print("   ✅ Created 'enrollments' table")

# ========== STEP 2: INSERT DATA ==========
print("\n📋 Step 2: Populating with sample data...")
print("-" * 40)

# Insert students
students = [
    ('Alice Johnson', 'alice@university.edu', 20, 3.8, '2022-09-01'),
    ('Bob Smith', 'bob@university.edu', 21, 3.5, '2021-09-01'),
    ('Charlie Brown', 'charlie@university.edu', 19, 3.9, '2023-09-01'),
    ('Diana Ross', 'diana@university.edu', 22, 3.2, '2020-09-01'),
    ('Eve Wilson', 'eve@university.edu', 20, 3.7, '2022-09-01'),
    ('Frank Miller', 'frank@university.edu', 21, 2.9, '2021-09-01'),
    ('Grace Lee', 'grace@university.edu', 19, 4.0, '2023-09-01'),
    ('Henry Davis', 'henry@university.edu', 23, 3.4, '2019-09-01'),
]

cursor.executemany("""
    INSERT INTO students (name, email, age, gpa, enrollment_date)
    VALUES (?, ?, ?, ?, ?)
""", students)
print(f"   ✅ Added {len(students)} students")

# Insert courses
courses = [
    ('Introduction to Python', 'CS101', 3, 'Dr. Smith'),
    ('Data Structures', 'CS201', 4, 'Dr. Johnson'),
    ('Database Systems', 'CS301', 3, 'Dr. Williams'),
    ('Web Development', 'CS202', 3, 'Prof. Brown'),
    ('Machine Learning', 'CS401', 4, 'Dr. Davis'),
]

cursor.executemany("""
    INSERT INTO courses (name, code, credits, instructor)
    VALUES (?, ?, ?, ?)
""", courses)
print(f"   ✅ Added {len(courses)} courses")

# Insert enrollments
enrollments = [
    (1, 1, 'A', '2024-01-15'),   # Alice - Python
    (1, 2, 'A-', '2024-01-15'),  # Alice - Data Structures
    (2, 1, 'B+', '2024-01-15'),  # Bob - Python
    (2, 3, 'B', '2024-01-15'),   # Bob - Database
    (3, 1, 'A+', '2024-01-15'),  # Charlie - Python
    (3, 2, 'A', '2024-01-15'),   # Charlie - Data Structures
    (3, 4, 'A', '2024-01-15'),   # Charlie - Web Dev
    (4, 3, 'B-', '2024-01-15'),  # Diana - Database
    (5, 1, 'A', '2024-01-15'),   # Eve - Python
    (5, 5, 'A-', '2024-01-15'),  # Eve - ML
    (6, 1, 'C+', '2024-01-15'),  # Frank - Python
    (7, 1, 'A+', '2024-01-15'),  # Grace - Python
    (7, 2, 'A+', '2024-01-15'),  # Grace - Data Structures
    (7, 5, 'A', '2024-01-15'),   # Grace - ML
]

cursor.executemany("""
    INSERT INTO enrollments (student_id, course_id, grade, enrolled_date)
    VALUES (?, ?, ?, ?)
""", enrollments)
print(f"   ✅ Added {len(enrollments)} enrollments")

conn.commit()

# ========== STEP 3: RUN QUERIES ==========
print("\n📋 Step 3: Running queries...")

# Query 1: All students
print("\n" + "=" * 60)
print("📊 Query 1: All Students")
print("-" * 60)
cursor.execute("SELECT * FROM students ORDER BY name")
for row in cursor.fetchall():
    print(f"   {row['name']:<20} GPA: {row['gpa']:.2f} | Age: {row['age']}")

# Query 2: Students with GPA above 3.5
print("\n" + "=" * 60)
print("📊 Query 2: Honor Roll (GPA > 3.5)")
print("-" * 60)
cursor.execute("SELECT name, gpa FROM students WHERE gpa > 3.5 ORDER BY gpa DESC")
for row in cursor.fetchall():
    print(f"   🌟 {row['name']}: {row['gpa']:.2f}")

# Query 3: Students enrolled in Python (INNER JOIN)
print("\n" + "=" * 60)
print("📊 Query 3: Students in 'Introduction to Python'")
print("-" * 60)
cursor.execute("""
    SELECT s.name, e.grade
    FROM students s
    INNER JOIN enrollments e ON s.id = e.student_id
    INNER JOIN courses c ON e.course_id = c.id
    WHERE c.code = 'CS101'
    ORDER BY e.grade
""")
for row in cursor.fetchall():
    print(f"   {row['name']}: Grade {row['grade']}")

# Query 4: Course enrollment count
print("\n" + "=" * 60)
print("📊 Query 4: Course Enrollment Statistics")
print("-" * 60)
cursor.execute("""
    SELECT c.name, c.code, COUNT(e.id) as students_enrolled
    FROM courses c
    LEFT JOIN enrollments e ON c.id = e.course_id
    GROUP BY c.id
    ORDER BY students_enrolled DESC
""")
for row in cursor.fetchall():
    print(f"   {row['code']}: {row['name']:<25} - {row['students_enrolled']} students")

# Query 5: Student course load
print("\n" + "=" * 60)
print("📊 Query 5: Student Course Load")
print("-" * 60)
cursor.execute("""
    SELECT s.name, COUNT(e.id) as courses, SUM(c.credits) as total_credits
    FROM students s
    LEFT JOIN enrollments e ON s.id = e.student_id
    LEFT JOIN courses c ON e.course_id = c.id
    GROUP BY s.id
    ORDER BY total_credits DESC
""")
for row in cursor.fetchall():
    credits = row['total_credits'] or 0
    print(f"   {row['name']:<20} {row['courses']} courses, {credits} credits")

# Query 6: Students not enrolled in any course
print("\n" + "=" * 60)
print("📊 Query 6: Students Not Enrolled")
print("-" * 60)
cursor.execute("""
    SELECT s.name, s.email
    FROM students s
    LEFT JOIN enrollments e ON s.id = e.student_id
    WHERE e.id IS NULL
""")
results = cursor.fetchall()
if results:
    for row in results:
        print(f"   ⚠️ {row['name']} ({row['email']})")
else:
    print("   All students are enrolled in at least one course!")

# Query 7: Top performers by course
print("\n" + "=" * 60)
print("📊 Query 7: Top Students in Each Course (A or A+ grades)")
print("-" * 60)
cursor.execute("""
    SELECT c.name as course, s.name as student, e.grade
    FROM courses c
    INNER JOIN enrollments e ON c.id = e.course_id
    INNER JOIN students s ON e.student_id = s.id
    WHERE e.grade IN ('A+', 'A')
    ORDER BY c.name, e.grade
""")
for row in cursor.fetchall():
    print(f"   {row['course']}: {row['student']} ({row['grade']})")

# Query 8: Average GPA by enrollment year
print("\n" + "=" * 60)
print("📊 Query 8: Average GPA by Year")
print("-" * 60)
cursor.execute("""
    SELECT strftime('%Y', enrollment_date) as year, 
           COUNT(*) as students,
           ROUND(AVG(gpa), 2) as avg_gpa
    FROM students
    GROUP BY year
    ORDER BY year DESC
""")
for row in cursor.fetchall():
    print(f"   Class of {row['year']}: {row['students']} students, Avg GPA: {row['avg_gpa']}")

# ========== BONUS: UPDATE/DELETE ==========
print("\n📋 Bonus: Data Modification Examples")

# Update a grade
print("\n" + "-" * 40)
print("Updating Frank's Python grade from C+ to B-...")
cursor.execute("""
    UPDATE enrollments 
    SET grade = 'B-' 
    WHERE student_id = (SELECT id FROM students WHERE name = 'Frank Miller')
    AND course_id = (SELECT id FROM courses WHERE code = 'CS101')
""")
conn.commit()
print("   ✅ Grade updated!")

# Verify update
cursor.execute("""
    SELECT s.name, c.name as course, e.grade
    FROM enrollments e
    INNER JOIN students s ON e.student_id = s.id
    INNER JOIN courses c ON e.course_id = c.id
    WHERE s.name = 'Frank Miller'
""")
row = cursor.fetchone()
print(f"   Verified: {row['name']} - {row['course']}: {row['grade']}")

conn.close()

print("\n" + "=" * 60)
print("✅ Mini Project Complete!")
print("=" * 60)
print("""
What you practiced:
- Creating related tables with foreign keys
- INSERT with multiple tables
- INNER JOIN for related data
- LEFT JOIN for finding missing relations
- GROUP BY for aggregations
- UPDATE with subqueries
""")
