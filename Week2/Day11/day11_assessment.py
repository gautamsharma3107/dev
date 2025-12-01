"""
DAY 11 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 11 ASSESSMENT - Django Part 1: Setup & Basics")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. Which command creates a new Django project?
a) python manage.py startproject myproject
b) django-admin startproject myproject
c) pip install django myproject
d) django create myproject

Your answer: """)

print("""
Q2. What file contains the Django project settings?
a) urls.py
b) config.py
c) settings.py
d) manage.py

Your answer: """)

print("""
Q3. Which command creates a new Django app inside a project?
a) django-admin startapp myapp
b) python manage.py startapp myapp
c) python manage.py createapp myapp
d) django-admin createapp myapp

Your answer: """)

print("""
Q4. What is the correct syntax to display a variable in a Django template?
a) {% variable %}
b) {{ variable }}
c) {$ variable $}
d) <% variable %>

Your answer: """)

print("""
Q5. Which of these is the correct URL pattern to capture an integer ID?
a) path('post/<id>/', views.post)
b) path('post/<int:id>/', views.post)
c) path('post/{id}/', views.post)
d) path('post/[int:id]/', views.post)

Your answer: """)

print("""
Q6. What does {% csrf_token %} do in a Django form template?
a) Validates form fields
b) Provides security against Cross-Site Request Forgery attacks
c) Creates a unique form ID
d) Encrypts form data

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a simple Django view function called 'about' that:
    - Takes a request parameter
    - Returns an HttpResponse with the text "About Page"
""")

# Write your code here:




print("""
Q8. (2 points) Write a Django URL pattern for the following:
    - URL: 'article/<slug:slug>/'
    - View: views.article_detail
    - Name: 'article_detail'
    Use the path() function.
""")

# Write your code here:




print("""
Q9. (2 points) Complete the Django template code to:
    - Loop through a list called 'posts'
    - Display each post's title
    - Show "No posts yet" if the list is empty
    
    Use the {% for %} tag with {% empty %}.
""")

# Write your template code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between a Django project
     and a Django app. Give an example of how they relate.

Your answer:
""")

# Write your explanation here as comments:
# 



print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) django-admin startproject myproject
Q2: c) settings.py
Q3: b) python manage.py startapp myapp
Q4: b) {{ variable }}
Q5: b) path('post/<int:id>/', views.post)
Q6: b) Provides security against Cross-Site Request Forgery attacks

Section B:
Q7:
from django.http import HttpResponse

def about(request):
    return HttpResponse("About Page")


Q8:
from django.urls import path
from . import views

urlpatterns = [
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]


Q9:
{% for post in posts %}
    <h2>{{ post.title }}</h2>
{% empty %}
    <p>No posts yet</p>
{% endfor %}


Section C:
Q10:
A Django PROJECT is the entire web application, containing:
- Project-wide settings (settings.py)
- Main URL configuration
- Can contain multiple apps
- Example: An e-commerce website project

A Django APP is a modular component within the project that handles a specific feature:
- Has its own models, views, templates
- Designed to be reusable
- Example: 'products', 'cart', 'users' apps within the e-commerce project

Relationship Example:
- Project: "myshop" (e-commerce website)
- Apps within myshop:
  - "products" app - handles product catalog
  - "orders" app - handles order processing
  - "users" app - handles user authentication
  
Each app is independent and could potentially be reused in another project.
"""
