"""
DAY 14 ASSESSMENT TEST - WEEK 2 COMPREHENSIVE REVIEW
=====================================================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

This assessment covers all Week 2 topics:
- Web & HTTP Fundamentals (Day 8)
- Git Version Control (Day 9)
- SQL Essentials (Day 10)
- Django Basics (Days 11-13)

Answer all questions. Good luck!
"""

print("=" * 70)
print("WEEK 2 COMPREHENSIVE ASSESSMENT - Web Fundamentals & Django")
print("=" * 70)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 70)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 70)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 70)

print("""
Q1. Which HTTP method is used to retrieve data from a server?
a) POST
b) PUT
c) GET
d) DELETE

Your answer: """)

print("""
Q2. What HTTP status code indicates a successful request?
a) 404
b) 500
c) 200
d) 301

Your answer: """)

print("""
Q3. Which Git command is used to save changes to the local repository?
a) git push
b) git commit
c) git add
d) git pull

Your answer: """)

print("""
Q4. In SQL, which clause is used to filter rows?
a) ORDER BY
b) GROUP BY
c) WHERE
d) HAVING

Your answer: """)

print("""
Q5. In Django, what does the 'M' stand for in MTV pattern?
a) Method
b) Model
c) Module
d) Manager

Your answer: """)

print("""
Q6. Which Django decorator protects a view from unauthenticated users?
a) @protected
b) @auth_required
c) @login_required
d) @user_only

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 70)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 70)

print("""
Q7. (2 points) Write a Django model for a 'Book' with fields:
    - title (max 200 characters)
    - author (max 100 characters)
    - published_date (date field)
    - isbn (max 13 characters, unique)
    
Write the model class below:
""")

# Write your model here:
# from django.db import models
#
# class Book(models.Model):
#     # Your code here
#     pass


print("""
Q8. (2 points) Write a SQL query to:
    - Select all columns from the 'posts' table
    - Filter where author_id = 1
    - Order by created_at descending
    - Limit to 10 results
    
Write your SQL query:
""")

# Your SQL query:


print("""
Q9. (2 points) Write a Django URL pattern that:
    - Maps path 'post/<int:pk>/edit/' to a view called 'post_edit'
    - Names the URL 'post-edit'
    
Write the path() statement:
""")

# Your URL pattern:
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     # Your code here
# ]


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 70)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 70)

print("""
Q10. (2 points) Explain the difference between Django's ForeignKey and 
     ManyToManyField. Give an example use case for each.

Your answer:
""")

# Write your explanation here:


# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 70)
print("TEST COMPLETE!")
print("=" * 70)
print("""
When done, check your answers with the professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Great job completing Week 2! 🎉
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: c) GET
Q2: c) 200
Q3: b) git commit
Q4: c) WHERE
Q5: b) Model
Q6: c) @login_required

Section B (Coding):

Q7: Django Model
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title


Q8: SQL Query
SELECT * 
FROM posts 
WHERE author_id = 1 
ORDER BY created_at DESC 
LIMIT 10;


Q9: Django URL Pattern
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/edit/', views.post_edit, name='post-edit'),
]


Section C (Conceptual):
Q10: ForeignKey vs ManyToManyField

ForeignKey:
- Represents a one-to-many relationship
- Example: A Post belongs to one Author, but an Author can have many Posts
- Usage: author = models.ForeignKey(User, on_delete=models.CASCADE)

ManyToManyField:
- Represents a many-to-many relationship
- Example: A Post can have many Tags, and a Tag can be on many Posts
- Usage: tags = models.ManyToManyField(Tag)

The key difference is that ForeignKey links one record to exactly one 
other record (many-to-one), while ManyToManyField allows linking multiple 
records on both sides (many-to-many).
"""
