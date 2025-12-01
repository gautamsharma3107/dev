"""
DAY 12 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 12 ASSESSMENT TEST - Django Models & ORM")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. Which Django field type would you use for storing a blog post body?
a) CharField
b) TextField
c) ContentField
d) LongTextField

Your answer: """)

print("""
Q2. What does auto_now_add=True do for a DateTimeField?
a) Updates the field every time the model is saved
b) Sets the field only when the object is first created
c) Requires the field to be provided
d) Makes the field optional

Your answer: """)

print("""
Q3. Which on_delete option prevents parent deletion if children exist?
a) CASCADE
b) SET_NULL
c) PROTECT
d) DO_NOTHING

Your answer: """)

print("""
Q4. What command applies pending migrations to the database?
a) python manage.py makemigrations
b) python manage.py migrate
c) python manage.py runmigrations
d) python manage.py syncdb

Your answer: """)

print("""
Q5. Which QuerySet method returns a single object and raises an exception if not found?
a) filter()
b) first()
c) get()
d) find()

Your answer: """)

print("""
Q6. What is the purpose of select_related() in Django ORM?
a) Select specific fields from the model
b) Optimize queries for ForeignKey relationships
c) Filter related objects
d) Create relationships between models

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a Django model for a 'Product' with:
- name (max 200 chars)
- price (decimal, 10 digits, 2 decimal places)
- is_available (boolean, default True)
- created_at (auto-set on creation)

Include the __str__ method returning the product name.
""")

# Write your code here:
print("# Your model code:")


print("""
Q8. (2 points) Write Django ORM queries to:
a) Get all products with price greater than 50
b) Get products ordered by price (highest first)
c) Update all unavailable products to available
""")

# Write your queries here:
print("# Your query code:")


print("""
Q9. (2 points) Write the admin.py code to register a Post model with:
- list_display showing: title, author, status, created_at
- list_filter for: status, created_at
- search_fields for: title, content
""")

# Write your admin code here:
print("# Your admin code:")


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between ForeignKey and ManyToManyField.
Give an example use case for each.

Your answer:
""")

# Write your explanation here:


# ============================================================
# TEST COMPLETE
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers below.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

# ============================================================
# ANSWER KEY
# ============================================================

print("\n" + "=" * 60)
print("ANSWER KEY (Don't look until you're done!)")
print("=" * 60)

ANSWERS = """
SECTION A (MCQ) - 1 point each:
-------------------------------
Q1: b) TextField
    (CharField has max_length limit, TextField is for unlimited text)

Q2: b) Sets the field only when the object is first created
    (auto_now=True updates every save, auto_now_add only on creation)

Q3: c) PROTECT
    (CASCADE deletes children, SET_NULL sets to NULL, PROTECT prevents deletion)

Q4: b) python manage.py migrate
    (makemigrations creates migration files, migrate applies them)

Q5: c) get()
    (filter returns QuerySet, first returns None if not found, get raises DoesNotExist)

Q6: b) Optimize queries for ForeignKey relationships
    (Uses JOIN to fetch related objects in single query)


SECTION B (Coding) - 2 points each:
-----------------------------------
Q7: Product Model

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


Q8: ORM Queries

# a) Products with price > 50
Product.objects.filter(price__gt=50)

# b) Products ordered by price (highest first)
Product.objects.order_by('-price')

# c) Update unavailable to available
Product.objects.filter(is_available=False).update(is_available=True)


Q9: Admin Registration

from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'content']


SECTION C (Conceptual) - 2 points:
----------------------------------
Q10: ForeignKey vs ManyToManyField

ForeignKey (Many-to-One):
- One object relates to ONE other object
- Example: A blog Post has ONE Author
- The post table has an author_id column
- Usage: Post.author (returns single User)

ManyToManyField (Many-to-Many):
- One object relates to MANY other objects, and vice versa
- Example: A Post can have MANY Tags, a Tag can be on MANY Posts
- Django creates an intermediate table to store relationships
- Usage: post.tags.all() (returns QuerySet of Tags)


SCORING:
--------
Section A: 6 points (1 each)
Section B: 6 points (2 each)
Section C: 2 points

Total: 14 points
Passing: 10 points (70%)
"""

print(ANSWERS)
