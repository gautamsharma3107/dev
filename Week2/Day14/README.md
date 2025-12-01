# Day 14: Week 2 Mini-Project + Review

## 🎯 Today's Goals
- Build a complete Blog or To-Do Web Application
- Implement CRUD operations (Create, Read, Update, Delete)
- Add user authentication (login, logout, register)
- Work with database models and relationships
- Deploy and test locally
- Complete Week 2 comprehensive assessment

## 📚 Week 2 Recap Topics
1. Web & HTTP Fundamentals (Day 8)
2. Git Version Control (Day 9)
3. SQL Essentials (Day 10)
4. Django Basics - Setup & URLs & Views (Day 11)
5. Django Models & ORM (Day 12)
6. Django Forms & Authentication (Day 13)

## 🏗️ Mini-Project: Simple Blog Web App

### Features Required
- User Registration and Login
- Create, Read, Update, Delete Blog Posts
- Post listing with pagination
- User-specific posts (authors can only edit/delete their own posts)
- Clean templates with navigation

### Project Structure
```
blog_project/
├── manage.py
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── blog/
│           ├── base.html
│           ├── home.html
│           ├── post_detail.html
│           ├── post_form.html
│           └── post_confirm_delete.html
└── users/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── users/
            ├── login.html
            ├── logout.html
            └── register.html
```

## 📂 Files in This Folder
- `README.md` - This file with project overview
- `blog_project/` - Complete Django blog application
- `exercises/` - Week 2 review exercises
- `day14_assessment.py` - Comprehensive Week 2 assessment
- `CHEATSHEET.md` - Week 2 quick reference guide

## ✅ Daily Checklist
- [ ] Review all Week 2 concepts
- [ ] Set up Django project structure
- [ ] Create blog models (Post model)
- [ ] Implement CRUD views for posts
- [ ] Create user registration and login
- [ ] Add templates with proper navigation
- [ ] Test all functionality locally
- [ ] Take Week 2 comprehensive assessment
- [ ] Score 70%+ to proceed to Week 3

## 🚀 Getting Started

### 1. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django
```

### 2. Navigate to Project
```bash
cd blog_project
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

### 6. Access the App
- Blog Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/users/login/
- Register: http://127.0.0.1:8000/users/register/

## 📋 Assessment Breakdown

### Weekly Project Assessment (100 points)
- Functionality (40 points)
- Code quality (20 points)
- Best practices (20 points)
- Documentation (10 points)
- Deployment (10 points)

**Pass Requirement: 70+ points**

### Written Assessment (14 points)
- 6 MCQs/True-False (6 points)
- 3 Short coding challenges (6 points)
- 1 Conceptual question (2 points)

**Pass Requirement: 10+ points (70%)**

## 💡 Key Concepts to Remember
- Django follows MTV (Model-Template-View) pattern
- Use `@login_required` decorator for protected views
- Always use `{% csrf_token %}` in forms
- URL namespacing helps organize routes
- ORM queries: `Model.objects.all()`, `.filter()`, `.get()`

---
**Week 2 Complete! Great job learning Django basics! 🎉**
