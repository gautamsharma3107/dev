"""
Hello World Django - Setup Instructions
========================================
Follow these step-by-step instructions to build your first Django app!
"""

print("=" * 60)
print("HELLO WORLD DJANGO - SETUP GUIDE")
print("=" * 60)

# ============================================================
# STEP 1: Create Virtual Environment
# ============================================================
print("""
STEP 1: Create Virtual Environment
==================================

Open your terminal and run:

# Create virtual environment
python -m venv venv

# Activate it:
# On Windows:
venv\\Scripts\\activate

# On Mac/Linux:
source venv/bin/activate

You should see (venv) at the start of your command line.
""")

# ============================================================
# STEP 2: Install Django
# ============================================================
print("""
STEP 2: Install Django
======================

pip install django

# Verify installation:
python -m django --version
""")

# ============================================================
# STEP 3: Create Project
# ============================================================
print("""
STEP 3: Create Django Project
=============================

django-admin startproject helloproject
cd helloproject

Your folder structure:
helloproject/
├── manage.py
└── helloproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
""")

# ============================================================
# STEP 4: Create App
# ============================================================
print("""
STEP 4: Create Hello App
========================

python manage.py startapp hello

Your folder structure now:
helloproject/
├── manage.py
├── helloproject/
│   └── ...
└── hello/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
""")

# ============================================================
# STEP 5: Register App
# ============================================================
print("""
STEP 5: Register App in settings.py
===================================

Open helloproject/settings.py and add 'hello' to INSTALLED_APPS:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',  # Add this line!
]
""")

# ============================================================
# STEP 6: Create Views
# ============================================================
print("""
STEP 6: Create Views
====================

Open hello/views.py and replace with:

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    context = {
        'title': 'Hello, Django!',
        'message': 'Welcome to your first Django application!',
        'current_time': datetime.now(),
        'features': [
            'URL Routing',
            'Function-Based Views',
            'Template Inheritance',
            'Context Data',
        ]
    }
    return render(request, 'hello/home.html', context)

def about(request):
    context = {
        'title': 'About',
        'description': 'This is a simple Hello World Django app.',
        'author': 'Your Name'
    }
    return render(request, 'hello/about.html', context)

def greet(request, name):
    return HttpResponse(f'Hello, {name}!')
""")

# ============================================================
# STEP 7: Create App URLs
# ============================================================
print("""
STEP 7: Create App URLs
=======================

Create a new file hello/urls.py:

from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('greet/<str:name>/', views.greet, name='greet'),
]
""")

# ============================================================
# STEP 8: Include App URLs
# ============================================================
print("""
STEP 8: Include App URLs in Main urls.py
========================================

Open helloproject/urls.py and modify:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
]
""")

# ============================================================
# STEP 9: Create Templates
# ============================================================
print("""
STEP 9: Create Templates
========================

Create the templates folder structure:
hello/
└── templates/
    └── hello/
        ├── base.html
        ├── home.html
        └── about.html

base.html:
----------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Hello Django{% endblock %}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        header {
            background-color: #092e20;
            color: white;
            padding: 20px;
            margin-bottom: 20px;
        }
        nav a {
            color: white;
            margin-right: 15px;
            text-decoration: none;
        }
        nav a:hover {
            text-decoration: underline;
        }
        main {
            background: white;
            padding: 20px;
            border-radius: 5px;
        }
        footer {
            margin-top: 20px;
            text-align: center;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>🎉 Hello Django!</h1>
        <nav>
            <a href="{% url 'hello:home' %}">Home</a>
            <a href="{% url 'hello:about' %}">About</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>Built with Django - Day 11 Mini Project</p>
    </footer>
</body>
</html>

home.html:
----------
{% extends 'hello/base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h2>{{ title }}</h2>
<p>{{ message }}</p>

<p><strong>Current Time:</strong> {{ current_time|date:"F j, Y, g:i a" }}</p>

<h3>What you've learned:</h3>
<ul>
{% for feature in features %}
    <li>{{ feature }}</li>
{% endfor %}
</ul>

<p>Try visiting: <a href="{% url 'hello:greet' name='YourName' %}">/greet/YourName/</a></p>
{% endblock %}

about.html:
-----------
{% extends 'hello/base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h2>{{ title }}</h2>
<p>{{ description }}</p>
<p><strong>Author:</strong> {{ author }}</p>
<p><a href="{% url 'hello:home' %}">← Back to Home</a></p>
{% endblock %}
""")

# ============================================================
# STEP 10: Run Server
# ============================================================
print("""
STEP 10: Run the Development Server
===================================

python manage.py runserver

Visit these URLs:
- http://127.0.0.1:8000/          (Home page)
- http://127.0.0.1:8000/about/    (About page)
- http://127.0.0.1:8000/greet/Django/  (Greeting page)

🎉 Congratulations! You've built your first Django app!
""")

# ============================================================
# COMPLETE PROJECT STRUCTURE
# ============================================================
print("""
COMPLETE PROJECT STRUCTURE
==========================

helloproject/
├── manage.py
├── helloproject/
│   ├── __init__.py
│   ├── settings.py      # Added 'hello' to INSTALLED_APPS
│   ├── urls.py          # Added include('hello.urls')
│   ├── asgi.py
│   └── wsgi.py
└── hello/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py         # Your views
    ├── urls.py          # Your URL patterns (created)
    └── templates/
        └── hello/
            ├── base.html
            ├── home.html
            └── about.html
""")

print("\n" + "=" * 60)
print("✅ Setup Guide Complete!")
print("=" * 60)
