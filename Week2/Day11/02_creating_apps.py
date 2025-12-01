"""
Day 11 - Creating Django Apps
==============================
Learn: Creating and organizing Django apps

Key Concepts:
- Projects contain multiple apps
- Apps are reusable modules
- Each app has specific responsibility
- Apps must be registered in settings.py
"""

# ========== PROJECT VS APP ==========
print("=" * 60)
print("PROJECT VS APP")
print("=" * 60)

print("""
Django Project:
- A collection of configurations and apps
- Contains settings.py, main urls.py
- Only ONE project per website
- Think of it as your entire website

Django App:
- A web application that does something
- Can be reused across projects
- Contains models, views, templates, etc.
- Multiple apps per project

Example Structure:
------------------
ecommerce_project/          # Project
├── ecommerce/              # Project config
├── products/               # App: Product management
├── cart/                   # App: Shopping cart
├── users/                  # App: User profiles
├── orders/                 # App: Order processing
└── payments/               # App: Payment handling

Each app is a self-contained module!
""")

# ========== CREATING AN APP ==========
print("=" * 60)
print("CREATING AN APP")
print("=" * 60)

print("""
Command:
--------
python manage.py startapp app_name

Example:
--------
cd myproject
python manage.py startapp blog

This creates:
blog/
├── __init__.py      # Python package marker
├── admin.py         # Admin site configuration
├── apps.py          # App configuration
├── models.py        # Database models
├── tests.py         # Unit tests
├── views.py         # View functions/classes
└── migrations/      # Database migrations folder
    └── __init__.py

Note: You need to create these yourself:
- urls.py           # App URL routing
- templates/        # HTML templates
- static/           # CSS, JS, images
- forms.py          # Form classes
""")

# ========== APP STRUCTURE EXPLAINED ==========
print("=" * 60)
print("APP STRUCTURE EXPLAINED")
print("=" * 60)

print("""
1. __init__.py
--------------
Empty file that makes the directory a Python package.

2. admin.py
-----------
Register models to appear in Django admin.

Example:
from django.contrib import admin
from .models import Post

admin.site.register(Post)

3. apps.py
----------
App configuration class.

Example:
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

4. models.py
------------
Define database models (tables).

Example:
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

5. views.py
-----------
Handle requests and return responses.

Example:
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

6. tests.py
-----------
Write unit tests for the app.

Example:
from django.test import TestCase

class PostTestCase(TestCase):
    def test_post_creation(self):
        # Test code here
        pass

7. migrations/
--------------
Database migration files (auto-generated).
Don't edit these manually!
""")

# ========== REGISTERING AN APP ==========
print("=" * 60)
print("REGISTERING AN APP")
print("=" * 60)

print("""
After creating an app, you MUST register it in settings.py!

Step 1: Open settings.py
------------------------
myproject/settings.py

Step 2: Add to INSTALLED_APPS
-----------------------------
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps - add here!
    'blog',                  # Short form
    # OR
    'blog.apps.BlogConfig',  # Full form (recommended)
]

Why register?
- Django needs to know about your app
- Required for migrations
- Required for template discovery
- Required for admin registration
""")

# ========== CREATING APP URLS ==========
print("=" * 60)
print("CREATING APP URLs")
print("=" * 60)

print("""
Apps don't come with urls.py - create it yourself!

Step 1: Create urls.py in your app
----------------------------------
blog/urls.py

Step 2: Add URL patterns
------------------------
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'  # URL namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

Step 3: Include in main urls.py
-------------------------------
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Include app URLs
]

Result:
- /blog/           → blog.views.home
- /blog/about/     → blog.views.about
- /blog/post/1/    → blog.views.post_detail (pk=1)
""")

# ========== APP TEMPLATES ==========
print("=" * 60)
print("APP TEMPLATES")
print("=" * 60)

print("""
Create templates folder inside your app:

blog/
├── templates/
│   └── blog/           # Namespace to avoid conflicts!
│       ├── base.html
│       ├── home.html
│       └── post_detail.html
├── views.py
└── ...

Why the extra 'blog' folder?
----------------------------
Django searches ALL app templates folders.
Without namespace, 'home.html' could conflict with other apps.

Using templates in views:
-------------------------
# blog/views.py
from django.shortcuts import render

def home(request):
    # Django finds 'blog/home.html' in templates
    return render(request, 'blog/home.html', {'title': 'Home'})

Template example (blog/templates/blog/home.html):
-------------------------------------------------
{% extends 'blog/base.html' %}

{% block content %}
<h1>{{ title }}</h1>
<p>Welcome to my blog!</p>
{% endblock %}
""")

# ========== APP STATIC FILES ==========
print("=" * 60)
print("APP STATIC FILES")
print("=" * 60)

print("""
Create static folder for CSS, JS, images:

blog/
├── static/
│   └── blog/           # Namespace!
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── script.js
│       └── images/
│           └── logo.png
├── templates/
└── ...

Using static files in templates:
--------------------------------
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
</head>
<body>
    <img src="{% static 'blog/images/logo.png' %}">
    <script src="{% static 'blog/js/script.js' %}"></script>
</body>
</html>
""")

# ========== PRACTICAL EXAMPLE ==========
print("=" * 60)
print("PRACTICAL: CREATE A BLOG APP")
print("=" * 60)

print("""
Let's create a complete blog app step by step:

Step 1: Create the app
----------------------
python manage.py startapp blog

Step 2: Register in settings.py
-------------------------------
INSTALLED_APPS = [
    ...
    'blog',
]

Step 3: Create blog/urls.py
---------------------------
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

Step 4: Create views
--------------------
# blog/views.py
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Blog Home',
        'posts': ['Post 1', 'Post 2', 'Post 3']
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

Step 5: Create templates
------------------------
mkdir -p blog/templates/blog

# blog/templates/blog/base.html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <nav>
        <a href="{% url 'blog:home' %}">Home</a>
        <a href="{% url 'blog:about' %}">About</a>
    </nav>
    {% block content %}{% endblock %}
</body>
</html>

# blog/templates/blog/home.html
{% extends 'blog/base.html' %}

{% block content %}
<h1>{{ title }}</h1>
{% for post in posts %}
    <p>{{ post }}</p>
{% endfor %}
{% endblock %}

Step 6: Include in main urls.py
-------------------------------
# myproject/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

Step 7: Run server
------------------
python manage.py runserver
# Visit http://127.0.0.1:8000/
""")

# ========== MULTIPLE APPS EXAMPLE ==========
print("=" * 60)
print("WORKING WITH MULTIPLE APPS")
print("=" * 60)

print("""
Real projects have multiple apps. Here's how to organize them:

Project Structure:
------------------
myshop/
├── manage.py
├── myshop/                 # Project settings
│   ├── settings.py
│   └── urls.py
├── products/               # Products app
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── cart/                   # Shopping cart app
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── users/                  # User management app
    ├── models.py
    ├── views.py
    └── urls.py

Main urls.py:
-------------
# myshop/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),      # /
    path('cart/', include('cart.urls')),     # /cart/
    path('users/', include('users.urls')),   # /users/
]

Each app handles its own routes, models, and templates!
""")

# ========== BEST PRACTICES ==========
print("=" * 60)
print("APP DESIGN BEST PRACTICES")
print("=" * 60)

print("""
1. Single Responsibility
------------------------
Each app should do ONE thing well.
❌ Bad: 'main' app that does everything
✅ Good: 'blog', 'users', 'comments' as separate apps

2. Reusability
--------------
Design apps to be pluggable.
Other projects should be able to use your app.

3. Loose Coupling
-----------------
Minimize dependencies between apps.
Use signals for cross-app communication.

4. Naming Conventions
---------------------
- Use lowercase, singular names: 'blog', not 'blogs'
- Be descriptive: 'authentication' vs 'auth'
- Avoid generic names: 'main', 'core', 'utils'

5. File Organization
--------------------
For large apps, split files:
blog/
├── models/
│   ├── __init__.py
│   ├── post.py
│   └── comment.py
├── views/
│   ├── __init__.py
│   ├── post_views.py
│   └── comment_views.py
└── ...

6. Keep apps small
------------------
If an app gets too big, split it!
'blog' → 'posts', 'comments', 'tags'
""")

print("\n" + "=" * 60)
print("✅ Creating Django Apps - Complete!")
print("=" * 60)
print("\nNext: Learn about URL routing (03_url_routing.py)")
