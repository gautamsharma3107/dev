"""
Day 11 - Exercise 2: Views and Templates
=========================================
Practice: Creating views, URL patterns, and templates

Instructions:
- Complete each exercise
- Test your code conceptually
- Check the solutions at the bottom (try first!)
"""

print("=" * 60)
print("EXERCISE 2: Views and Templates")
print("=" * 60)

# ============================================================
# Exercise 2.1: Basic Views
# ============================================================
print("\n--- Exercise 2.1: Basic Views ---")
print("""
Task: Write three view functions:

1. home_view: Returns HttpResponse with "Welcome Home!"
2. about_view: Returns HttpResponse with "About Us"
3. contact_view: Renders a template 'pages/contact.html'
""")

# Your code here:
# from django.http import HttpResponse
# from django.shortcuts import render

# def home_view(request):
#     ...

# def about_view(request):
#     ...

# def contact_view(request):
#     ...




# ============================================================
# Exercise 2.2: Views with Parameters
# ============================================================
print("\n--- Exercise 2.2: Views with Parameters ---")
print("""
Task: Write view functions that accept URL parameters:

1. user_profile(request, username): 
   Returns "Profile: {username}"

2. post_detail(request, year, month, pk):
   Returns "Post {pk} from {month}/{year}"

3. category_list(request, slug):
   Renders 'blog/category.html' with context {'category': slug}
""")

# Your code here:




# ============================================================
# Exercise 2.3: URL Patterns
# ============================================================
print("\n--- Exercise 2.3: URL Patterns ---")
print("""
Task: Write URL patterns for these routes:

1. '' (empty) -> views.home, name='home'
2. 'about/' -> views.about, name='about'
3. 'post/<int:pk>/' -> views.post_detail, name='post_detail'
4. 'user/<str:username>/' -> views.profile, name='profile'
5. 'tag/<slug:tag>/' -> views.tag_posts, name='tag_posts'

Include app_name = 'blog'
""")

# Your code here:
# from django.urls import path
# from . import views
# 
# app_name = 'blog'
# 
# urlpatterns = [
#     ...
# ]




# ============================================================
# Exercise 2.4: Template Variables
# ============================================================
print("\n--- Exercise 2.4: Template Variables ---")
print("""
Task: Given this view:

def dashboard(request):
    context = {
        'user': {'name': 'John', 'email': 'john@example.com'},
        'posts_count': 42,
        'notifications': ['New comment', 'New follower'],
        'is_premium': True
    }
    return render(request, 'dashboard.html', context)

Write the template code to display:
1. User's name
2. User's email
3. Posts count
4. First notification
5. "Premium Member" if is_premium is True
""")

# Your template code here:




# ============================================================
# Exercise 2.5: Template Tags
# ============================================================
print("\n--- Exercise 2.5: Template Tags ---")
print("""
Task: Write template code for these scenarios:

1. Loop through a list 'products' and display each product.name
   Show "No products available" if the list is empty

2. Display "Welcome back!" if user.is_authenticated, 
   else display "Please log in"

3. Create a link to the 'blog:post_detail' URL with pk=5
""")

# Your template code here:




# ============================================================
# Exercise 2.6: Template Filters
# ============================================================
print("\n--- Exercise 2.6: Template Filters ---")
print("""
Task: Apply filters to these variables:

1. {{ title }} - convert to lowercase
2. {{ description }} - truncate to 50 characters
3. {{ price }} - format as float with 2 decimal places
4. {{ created_at }} - format as "Jan 15, 2024"
5. {{ tags }} - join with commas
6. {{ bio }} - show "No bio" if empty
""")

# Your template code here:




# ============================================================
# Exercise 2.7: Template Inheritance
# ============================================================
print("\n--- Exercise 2.7: Template Inheritance ---")
print("""
Task: Create template inheritance structure:

1. Write a base.html with:
   - Title block
   - Content block
   - Extra CSS block

2. Write a child template home.html that:
   - Extends base.html
   - Sets title to "Home Page"
   - Adds content with a welcome message
""")

# Your template code here:




print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("""
Exercise 2.1 Solution:
----------------------
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return HttpResponse("Welcome Home!")

def about_view(request):
    return HttpResponse("About Us")

def contact_view(request):
    return render(request, 'pages/contact.html')


Exercise 2.2 Solution:
----------------------
def user_profile(request, username):
    return HttpResponse(f"Profile: {username}")

def post_detail(request, year, month, pk):
    return HttpResponse(f"Post {pk} from {month}/{year}")

def category_list(request, slug):
    return render(request, 'blog/category.html', {'category': slug})


Exercise 2.3 Solution:
----------------------
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('user/<str:username>/', views.profile, name='profile'),
    path('tag/<slug:tag>/', views.tag_posts, name='tag_posts'),
]


Exercise 2.4 Solution:
----------------------
<h1>{{ user.name }}</h1>
<p>Email: {{ user.email }}</p>
<p>Posts: {{ posts_count }}</p>
<p>Latest: {{ notifications.0 }}</p>
{% if is_premium %}
<span>Premium Member</span>
{% endif %}


Exercise 2.5 Solution:
----------------------
1. Product loop:
{% for product in products %}
    <p>{{ product.name }}</p>
{% empty %}
    <p>No products available</p>
{% endfor %}

2. Authentication check:
{% if user.is_authenticated %}
    <p>Welcome back!</p>
{% else %}
    <p>Please log in</p>
{% endif %}

3. URL with parameter:
<a href="{% url 'blog:post_detail' pk=5 %}">View Post</a>


Exercise 2.6 Solution:
----------------------
1. {{ title|lower }}
2. {{ description|truncatechars:50 }}
3. {{ price|floatformat:2 }}
4. {{ created_at|date:"M d, Y" }}
5. {{ tags|join:", " }}
6. {{ bio|default:"No bio" }}


Exercise 2.7 Solution:
----------------------
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

<!-- home.html -->
{% extends 'base.html' %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome to our site!</h1>
<p>We're glad you're here.</p>
{% endblock %}
""")

print("\n✅ Exercise 2 Complete! Now try the mini-project!")
