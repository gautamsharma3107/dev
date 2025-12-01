"""
Day 11 - Django Installation & Setup
=====================================
Learn: Installing Django, creating projects, and understanding structure

Key Concepts:
- Django is a high-level Python web framework
- "Batteries included" - comes with many features built-in
- MTV pattern (Model-Template-View)
- Project vs App organization
"""

import subprocess
import sys
import os

# ========== WHAT IS DJANGO? ==========
print("=" * 60)
print("WHAT IS DJANGO?")
print("=" * 60)

print("""
Django is a high-level Python web framework that encourages rapid 
development and clean, pragmatic design. Built by experienced developers, 
it takes care of much of the hassle of web development.

Key Features:
✅ Fast - Helps you build apps quickly
✅ Secure - Takes security seriously
✅ Scalable - Used by Instagram, Pinterest, Mozilla
✅ Batteries included - Admin, auth, ORM built-in
✅ MTV Architecture - Model-Template-View pattern

Django MTV vs MVC:
- Model = Model (Data layer)
- Template = View (Presentation layer)
- View = Controller (Business logic)
""")

# ========== INSTALLATION ==========
print("=" * 60)
print("INSTALLING DJANGO")
print("=" * 60)

print("""
Step 1: Create a virtual environment (recommended)
--------------------------------------------------
# Create virtual environment
python -m venv venv

# Activate it:
# Windows:
venv\\Scripts\\activate

# Linux/Mac:
source venv/bin/activate

Step 2: Install Django
----------------------
pip install django

# Or specific version:
pip install django==4.2

Step 3: Verify installation
---------------------------
python -m django --version
# or
django-admin --version
""")

# Check Django installation
print("\nChecking Django installation...")
try:
    import django
    print(f"✅ Django version: {django.get_version()}")
except ImportError:
    print("❌ Django not installed. Run: pip install django")
    print("\nTo continue this tutorial, please install Django first!")

# ========== CREATING A PROJECT ==========
print("\n" + "=" * 60)
print("CREATING A DJANGO PROJECT")
print("=" * 60)

print("""
Command to create a project:
----------------------------
django-admin startproject project_name

# Or create in current directory:
django-admin startproject project_name .

Example:
--------
django-admin startproject mysite
cd mysite
python manage.py runserver

Visit: http://127.0.0.1:8000/
""")

# ========== PROJECT STRUCTURE ==========
print("=" * 60)
print("PROJECT STRUCTURE")
print("=" * 60)

print("""
After running: django-admin startproject mysite

mysite/                    # Root directory (name doesn't matter)
├── manage.py              # Command-line utility
└── mysite/                # Python package (actual project)
    ├── __init__.py        # Empty - marks as Python package
    ├── settings.py        # Project settings/configuration
    ├── urls.py            # URL declarations (URL routing)
    ├── asgi.py            # Entry point for ASGI servers
    └── wsgi.py            # Entry point for WSGI servers

Key Files Explained:
--------------------

manage.py
---------
Django's command-line utility. Use it to:
- Run the development server: python manage.py runserver
- Create apps: python manage.py startapp appname
- Run migrations: python manage.py migrate
- Create superuser: python manage.py createsuperuser
- Open shell: python manage.py shell

settings.py
-----------
Central configuration file. Contains:
- DEBUG = True/False (development vs production)
- ALLOWED_HOSTS = [] (allowed domain names)
- INSTALLED_APPS = [...] (registered apps)
- DATABASES = {...} (database configuration)
- STATIC_URL = '/static/' (static files path)
- SECRET_KEY (keep this secret!)

urls.py
-------
URL routing configuration. Maps URLs to views.
""")

# ========== IMPORTANT SETTINGS ==========
print("=" * 60)
print("IMPORTANT SETTINGS.PY CONFIGURATION")
print("=" * 60)

print("""
# settings.py key configurations:

# 1. Debug mode (NEVER True in production!)
DEBUG = True

# 2. Allowed hosts (domains that can serve your app)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']

# 3. Installed apps (register your apps here)
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',       # Admin site
    'django.contrib.auth',        # Authentication
    'django.contrib.contenttypes',# Content types framework
    'django.contrib.sessions',    # Session framework
    'django.contrib.messages',    # Messaging framework
    'django.contrib.staticfiles', # Static files handling
    
    # Your apps (add here after creating)
    'myapp',
]

# 4. Database configuration (default: SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 5. Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates
        'APP_DIRS': True,  # Look for templates in app directories
        'OPTIONS': {...},
    },
]

# 6. Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# 7. Time zone
TIME_ZONE = 'UTC'  # Change to your timezone
USE_TZ = True
""")

# ========== MANAGE.PY COMMANDS ==========
print("=" * 60)
print("ESSENTIAL MANAGE.PY COMMANDS")
print("=" * 60)

print("""
# Run development server
python manage.py runserver
python manage.py runserver 8080      # Different port
python manage.py runserver 0.0.0.0:8000  # Allow external access

# Create database tables
python manage.py migrate

# Create new migrations
python manage.py makemigrations

# Create a new app
python manage.py startapp appname

# Create admin user
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic

# Check for issues
python manage.py check

# Show all available commands
python manage.py help
""")

# ========== DEVELOPMENT SERVER ==========
print("=" * 60)
print("DEVELOPMENT SERVER")
print("=" * 60)

print("""
Running the server:
-------------------
python manage.py runserver

Output:
-------
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 4.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Important Notes:
- Development server auto-reloads on code changes
- NEVER use in production! Use Gunicorn/uWSGI instead
- Default port: 8000
- Access at: http://127.0.0.1:8000/ or http://localhost:8000/
""")

# ========== PRACTICAL EXAMPLE ==========
print("=" * 60)
print("PRACTICAL: CREATE YOUR FIRST PROJECT")
print("=" * 60)

print("""
Follow these steps to create your first Django project:

Step 1: Open terminal
---------------------

Step 2: Create and activate virtual environment
-----------------------------------------------
python -m venv django_env
source django_env/bin/activate  # Linux/Mac
django_env\\Scripts\\activate     # Windows

Step 3: Install Django
----------------------
pip install django

Step 4: Create project
----------------------
django-admin startproject helloworld
cd helloworld

Step 5: Run migrations (creates database)
-----------------------------------------
python manage.py migrate

Step 6: Start server
--------------------
python manage.py runserver

Step 7: Open browser
--------------------
Visit: http://127.0.0.1:8000/

You should see the Django welcome page! 🎉

Step 8: Access admin (optional)
-------------------------------
python manage.py createsuperuser
# Enter username, email, password
Visit: http://127.0.0.1:8000/admin/
""")

# ========== DJANGO PROJECT LIFECYCLE ==========
print("=" * 60)
print("DJANGO PROJECT LIFECYCLE")
print("=" * 60)

print("""
1. CREATE PROJECT
   └── django-admin startproject mysite

2. CREATE APP(S)
   └── python manage.py startapp myapp

3. CONFIGURE
   └── Add app to INSTALLED_APPS
   └── Configure URLs
   └── Set up templates

4. DEVELOP
   └── Create models (database)
   └── Create views (logic)
   └── Create templates (HTML)
   └── Add URLs (routing)

5. TEST
   └── python manage.py test

6. DEPLOY
   └── Set DEBUG = False
   └── Configure production server
   └── Set up static files
""")

# ========== COMMON MISTAKES ==========
print("=" * 60)
print("COMMON MISTAKES TO AVOID")
print("=" * 60)

print("""
❌ Mistake 1: Leaving DEBUG = True in production
   ✅ Fix: Set DEBUG = False and configure ALLOWED_HOSTS

❌ Mistake 2: Committing SECRET_KEY to version control
   ✅ Fix: Use environment variables

❌ Mistake 3: Forgetting to add app to INSTALLED_APPS
   ✅ Fix: Always register your apps in settings.py

❌ Mistake 4: Using development server in production
   ✅ Fix: Use Gunicorn, uWSGI, or Daphne

❌ Mistake 5: Not running migrations after model changes
   ✅ Fix: Run makemigrations then migrate

❌ Mistake 6: Hardcoding database credentials
   ✅ Fix: Use environment variables or .env files
""")

print("\n" + "=" * 60)
print("✅ Django Installation & Setup - Complete!")
print("=" * 60)
print("\nNext: Learn how to create Django apps (02_creating_apps.py)")
