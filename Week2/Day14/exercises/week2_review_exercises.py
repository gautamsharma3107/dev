"""
Week 2 Review Exercises
=======================
Practice exercises covering all Week 2 topics

Topics:
- Web & HTTP Fundamentals
- Git Version Control
- SQL Essentials
- Django Basics
"""

print("=" * 60)
print("WEEK 2 REVIEW EXERCISES")
print("=" * 60)

# ============================================================
# Exercise 1: HTTP Methods
# ============================================================
print("\n" + "=" * 60)
print("Exercise 1: HTTP Methods")
print("=" * 60)

print("""
For each scenario, identify the correct HTTP method:

1. Viewing a user's profile page: ___________
2. Creating a new blog post: ___________
3. Updating your email address: ___________
4. Removing an item from cart: ___________
5. Fetching a list of products: ___________

Answers: (Fill in GET, POST, PUT/PATCH, or DELETE)
""")

# ============================================================
# Exercise 2: Git Commands
# ============================================================
print("\n" + "=" * 60)
print("Exercise 2: Git Commands")
print("=" * 60)

print("""
Write the Git commands for each task:

1. Check current repository status:
   Command: ___________

2. Stage all changes for commit:
   Command: ___________

3. Commit changes with message "Add user authentication":
   Command: ___________

4. Create and switch to a new branch called 'feature':
   Command: ___________

5. Merge 'feature' branch into current branch:
   Command: ___________
""")

# ============================================================
# Exercise 3: SQL Queries
# ============================================================
print("\n" + "=" * 60)
print("Exercise 3: SQL Queries")
print("=" * 60)

print("""
Write SQL queries for each task (using a 'users' table with 
columns: id, name, email, age, created_at):

1. Select all users:
   Query: ___________

2. Find users older than 25:
   Query: ___________

3. Find users whose name starts with 'J':
   Query: ___________

4. Count total number of users:
   Query: ___________

5. Select users ordered by age, newest first, limit 5:
   Query: ___________
""")

# ============================================================
# Exercise 4: Django ORM Queries
# ============================================================
print("\n" + "=" * 60)
print("Exercise 4: Django ORM Queries")
print("=" * 60)

print("""
Write Django ORM queries for each task (using Post model):

1. Get all posts:
   Query: ___________

2. Get post with id=5:
   Query: ___________

3. Get posts where author_id is 1:
   Query: ___________

4. Get posts containing 'Django' in title:
   Query: ___________

5. Count published posts:
   Query: ___________
""")

# ============================================================
# Exercise 5: Django Model Creation
# ============================================================
print("\n" + "=" * 60)
print("Exercise 5: Django Model Creation")
print("=" * 60)

print("""
Create a Django model for a 'Product' with:
- name (CharField, max 200)
- description (TextField)
- price (DecimalField, 2 decimal places)
- in_stock (BooleanField, default True)
- category (ForeignKey to Category model)
- created_at (auto-add datetime)

Write your model below:
""")

# Your model code here:
# class Product(models.Model):
#     pass

# ============================================================
# ANSWER KEY
# ============================================================

print("\n" + "=" * 60)
print("EXERCISES COMPLETE!")
print("=" * 60)
print("""
Check your answers with the solutions below.
Practice any exercises you got wrong!
""")

"""
ANSWER KEY
============================================

Exercise 1: HTTP Methods
1. GET
2. POST
3. PUT or PATCH
4. DELETE
5. GET


Exercise 2: Git Commands
1. git status
2. git add .
3. git commit -m "Add user authentication"
4. git checkout -b feature
5. git merge feature


Exercise 3: SQL Queries
1. SELECT * FROM users;
2. SELECT * FROM users WHERE age > 25;
3. SELECT * FROM users WHERE name LIKE 'J%';
4. SELECT COUNT(*) FROM users;
5. SELECT * FROM users ORDER BY age DESC LIMIT 5;


Exercise 4: Django ORM Queries
1. Post.objects.all()
2. Post.objects.get(id=5)
3. Post.objects.filter(author_id=1)
4. Post.objects.filter(title__contains='Django')
5. Post.objects.filter(published=True).count()


Exercise 5: Django Model
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
"""
