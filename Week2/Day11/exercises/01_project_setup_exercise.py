"""
Day 11 - Exercise 1: Django Project Setup
==========================================
Practice: Setting up Django projects and apps

Instructions:
- Complete each exercise
- Test your code by running the scripts
- Check the solutions at the bottom (try first!)
"""

print("=" * 60)
print("EXERCISE 1: Django Project Setup")
print("=" * 60)

# ============================================================
# Exercise 1.1: Installation Check
# ============================================================
print("\n--- Exercise 1.1: Installation Check ---")
print("""
Task: Write code to check if Django is installed and print the version.
Hint: Import django and use django.get_version()
""")

# Your code here:




# ============================================================
# Exercise 1.2: Project Structure Quiz
# ============================================================
print("\n--- Exercise 1.2: Project Structure Quiz ---")
print("""
Task: Answer these questions about Django project structure:

1. Which file do you run to start the development server?
   Your answer: 

2. Which file contains database configuration?
   Your answer: 

3. Which file defines the main URL patterns?
   Your answer: 

4. What command creates a new app called 'blog'?
   Your answer: 

5. Where do you add your app name after creating it?
   Your answer: 
""")

# ============================================================
# Exercise 1.3: Settings Configuration
# ============================================================
print("\n--- Exercise 1.3: Settings Configuration ---")
print("""
Task: Write the INSTALLED_APPS list that includes:
- All default Django apps (admin, auth, contenttypes, sessions, messages, staticfiles)
- A custom app called 'blog'
- A custom app called 'users'
""")

# Your code here:
# INSTALLED_APPS = [
#     ...
# ]




# ============================================================
# Exercise 1.4: App Registration
# ============================================================
print("\n--- Exercise 1.4: App Registration ---")
print("""
Task: Given this apps.py file content:

from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

Write TWO ways to register this app in INSTALLED_APPS:
1. Short form: 
2. Long form: 
""")

# Your answers here:




# ============================================================
# Exercise 1.5: Command Practice
# ============================================================
print("\n--- Exercise 1.5: Command Practice ---")
print("""
Task: Write the correct manage.py command for each task:

1. Run the development server on port 8080:
   Command: 

2. Create database tables from migrations:
   Command: 

3. Create a superuser for admin access:
   Command: 

4. Open an interactive Python shell with Django:
   Command: 

5. Check for project issues without making changes:
   Command: 
""")




print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("""
Exercise 1.1 Solution:
----------------------
import django
print(f"Django version: {django.get_version()}")
# Or: python -m django --version


Exercise 1.2 Solutions:
-----------------------
1. manage.py (python manage.py runserver)
2. settings.py (in the DATABASES setting)
3. urls.py (main project urls.py)
4. python manage.py startapp blog
5. INSTALLED_APPS list in settings.py


Exercise 1.3 Solution:
----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom apps
    'blog',
    'users',
]


Exercise 1.4 Solution:
----------------------
1. Short form: 'products'
2. Long form: 'products.apps.ProductsConfig'


Exercise 1.5 Solutions:
-----------------------
1. python manage.py runserver 8080
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py shell
5. python manage.py check
""")

print("\n✅ Exercise 1 Complete! Move on to Exercise 2.")
