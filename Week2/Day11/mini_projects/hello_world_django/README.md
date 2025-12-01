# Hello World Django Mini-Project

## 📝 Overview
This is your Day 11 mini-project: Build a simple "Hello World" Django application.

## 🎯 Project Goals
- Create a Django project from scratch
- Set up URL routing
- Create function-based views
- Use Django templates with inheritance
- Pass data from views to templates

## 📁 Project Structure
```
hello_world_django/
├── README.md           # This file
├── setup_instructions.py  # Step-by-step setup guide
├── views.py            # Example views
├── urls.py             # Example URL patterns
└── templates/
    └── hello/
        ├── base.html
        ├── home.html
        └── about.html
```

## 🚀 Quick Start

### Step 1: Create a new Django project
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install Django
pip install django

# Create project
django-admin startproject helloproject
cd helloproject
```

### Step 2: Create the hello app
```bash
python manage.py startapp hello
```

### Step 3: Register the app
Add `'hello'` to `INSTALLED_APPS` in `settings.py`

### Step 4: Copy the example files
Copy the views.py, urls.py, and templates from this folder to your app.

### Step 5: Configure URLs
Add `path('', include('hello.urls'))` to main urls.py

### Step 6: Run the server
```bash
python manage.py runserver
```

### Step 7: Test it!
Visit http://127.0.0.1:8000/

## 🎓 Learning Objectives Met
After completing this project, you will have:
- [x] Created a Django project
- [x] Created and registered a Django app
- [x] Set up URL routing
- [x] Created function-based views
- [x] Used template inheritance
- [x] Passed context data to templates

## 💡 Extension Ideas
1. Add a contact page with a form
2. Add more dynamic content (current time, visitor counter)
3. Add static files (CSS styling)
4. Add a navigation menu to all pages
5. Create a simple blog page listing posts

Good luck! 🍀
