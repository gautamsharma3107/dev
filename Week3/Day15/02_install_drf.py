"""
Day 15 - Installing Django REST Framework
==========================================
Learn: How to install and configure DRF in your Django project

Key Concepts:
- Installing DRF with pip
- Adding to INSTALLED_APPS
- Basic configuration settings
- Project structure for APIs
"""

# ========== INSTALLATION ==========
print("=" * 60)
print("INSTALLING DJANGO REST FRAMEWORK")
print("=" * 60)

print("""
Step 1: Install DRF using pip
-----------------------------
$ pip install djangorestframework

Optional packages you might want:
$ pip install django-filter         # For filtering querysets
$ pip install markdown              # For browsable API markdown support
$ pip install djangorestframework-simplejwt  # For JWT authentication
""")


# ========== PROJECT SETUP ==========
print("\n" + "=" * 60)
print("PROJECT SETUP")
print("=" * 60)

print("""
Step 2: Create Django Project (if you don't have one)
-----------------------------------------------------
$ django-admin startproject api_project
$ cd api_project
$ python manage.py startapp api

Project Structure:
api_project/
├── api_project/
│   ├── __init__.py
│   ├── settings.py      # Configuration
│   ├── urls.py          # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
├── api/                 # Our API app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # Database models
│   ├── serializers.py   # NEW: Data serialization
│   ├── views.py         # API views
│   ├── urls.py          # API URL routing
│   └── tests.py
├── manage.py
└── requirements.txt
""")


# ========== SETTINGS CONFIGURATION ==========
print("\n" + "=" * 60)
print("SETTINGS CONFIGURATION")
print("=" * 60)

print("""
Step 3: Update settings.py
--------------------------

# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',           # Add this!
    
    # Local apps
    'api',                      # Your API app
]

# DRF Configuration (add at the end of settings.py)
REST_FRAMEWORK = {
    # Default permission class
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    
    # Default authentication classes
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    
    # Date/time format
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    
    # Filtering
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
""")


# ========== URL CONFIGURATION ==========
print("\n" + "=" * 60)
print("URL CONFIGURATION")
print("=" * 60)

print("""
Step 4: Configure URLs
----------------------

# api_project/urls.py (main project urls)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),           # API endpoints
    path('api-auth/', include('rest_framework.urls')),  # Login for browsable API
]


# api/urls.py (app urls - create this file)

from django.urls import path
from . import views

urlpatterns = [
    # We'll add API endpoints here
]
""")


# ========== CREATING A MODEL ==========
print("\n" + "=" * 60)
print("CREATING A MODEL")
print("=" * 60)

print("""
Step 5: Create a Model for our API
----------------------------------

# api/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} by {self.author}"


# Run migrations
$ python manage.py makemigrations
$ python manage.py migrate
""")


# ========== ADMIN CONFIGURATION ==========
print("\n" + "=" * 60)
print("ADMIN CONFIGURATION")
print("=" * 60)

print("""
Step 6: Register Model in Admin
-------------------------------

# api/admin.py

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'is_available', 'created_at']
    list_filter = ['is_available', 'published_date']
    search_fields = ['title', 'author', 'isbn']
    ordering = ['-created_at']


# Create superuser to access admin
$ python manage.py createsuperuser
""")


# ========== VERIFYING INSTALLATION ==========
print("\n" + "=" * 60)
print("VERIFYING INSTALLATION")
print("=" * 60)

print("""
Step 7: Verify Everything Works
-------------------------------

# Check installed packages
$ pip freeze | grep djangorestframework

# Start development server
$ python manage.py runserver

# Visit these URLs:
- Admin: http://127.0.0.1:8000/admin/
- API Auth: http://127.0.0.1:8000/api-auth/login/

You should see:
✅ Admin panel working
✅ DRF login page at /api-auth/login/
✅ No errors in terminal
""")


# ========== EXAMPLE: Complete settings.py ==========
print("\n" + "=" * 60)
print("COMPLETE SETTINGS EXAMPLE")
print("=" * 60)

complete_settings = '''
# settings.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key-here'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party
    'rest_framework',
    
    # Local
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
'''

print(complete_settings)


print("\n" + "=" * 60)
print("✅ DRF Installation - Complete!")
print("=" * 60)
print("""
Summary:
- Install DRF with pip
- Add 'rest_framework' to INSTALLED_APPS
- Configure REST_FRAMEWORK settings
- Set up URL routing
- Create models for your API
- Register models in admin

Next: Let's learn about Serializers!
""")
