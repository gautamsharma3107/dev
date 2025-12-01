# Week 2 Quick Reference Cheat Sheet

## HTTP Methods
```
GET     - Retrieve data (read-only)
POST    - Create new resource
PUT     - Update entire resource
PATCH   - Partial update
DELETE  - Remove resource
```

## HTTP Status Codes
```
2xx - Success
    200 OK - Request successful
    201 Created - Resource created
    204 No Content - Success, no body

3xx - Redirection
    301 Moved Permanently
    302 Found (Temporary Redirect)

4xx - Client Error
    400 Bad Request
    401 Unauthorized
    403 Forbidden
    404 Not Found

5xx - Server Error
    500 Internal Server Error
    502 Bad Gateway
    503 Service Unavailable
```

## Git Commands
```bash
# Initialize
git init
git clone <url>

# Basic workflow
git status              # Check status
git add .               # Stage all changes
git add <file>          # Stage specific file
git commit -m "msg"     # Commit changes
git push                # Push to remote
git pull                # Pull from remote

# Branching
git branch              # List branches
git branch <name>       # Create branch
git checkout <name>     # Switch branch
git checkout -b <name>  # Create and switch
git merge <name>        # Merge branch

# History
git log                 # View history
git log --oneline       # Compact view
git diff                # See changes
```

## SQL Essentials
```sql
-- SELECT
SELECT * FROM users;
SELECT name, email FROM users;
SELECT * FROM users WHERE age > 18;
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users LIMIT 10;

-- INSERT
INSERT INTO users (name, email) 
VALUES ('John', 'john@example.com');

-- UPDATE
UPDATE users 
SET email = 'new@example.com' 
WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;

-- JOINS
SELECT posts.title, users.name
FROM posts
INNER JOIN users ON posts.user_id = users.id;

SELECT posts.title, users.name
FROM posts
LEFT JOIN users ON posts.user_id = users.id;
```

## Django Project Structure
```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
```

## Django Commands
```bash
# Create project
django-admin startproject myproject

# Create app
python manage.py startapp myapp

# Run server
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell
```

## Django Models
```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Field types
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    rating = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # Relationships
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title
```

## Django ORM Queries
```python
# All objects
Post.objects.all()

# Single object
Post.objects.get(id=1)

# Filter
Post.objects.filter(published=True)
Post.objects.filter(title__contains='Django')
Post.objects.filter(views__gte=100)

# Exclude
Post.objects.exclude(published=False)

# Order
Post.objects.order_by('-created')
Post.objects.order_by('title')

# First/Last
Post.objects.first()
Post.objects.last()

# Count
Post.objects.count()
Post.objects.filter(published=True).count()

# Create
Post.objects.create(title='New', content='...')

# Update
post = Post.objects.get(id=1)
post.title = 'Updated'
post.save()

# Delete
Post.objects.get(id=1).delete()
```

## Django URLs
```python
from django.urls import path
from . import views

urlpatterns = [
    # Basic path
    path('', views.home, name='home'),
    
    # With parameter
    path('post/<int:pk>/', views.detail, name='detail'),
    
    # String parameter
    path('user/<str:username>/', views.profile, name='profile'),
    
    # Multiple parameters
    path('archive/<int:year>/<int:month>/', views.archive, name='archive'),
]
```

## Django Views
```python
# Function-based view
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

# Class-based views
from django.views.generic import ListView, DetailView, CreateView

class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
```

## Django Templates
```html
<!-- Variables -->
{{ variable }}
{{ post.title }}
{{ user.username }}

<!-- Tags -->
{% if condition %}
    ...
{% elif other %}
    ...
{% else %}
    ...
{% endif %}

{% for item in list %}
    {{ item }}
{% empty %}
    No items
{% endfor %}

<!-- Extends/Block -->
{% extends "base.html" %}
{% block content %}
    ...
{% endblock %}

<!-- Include -->
{% include "partial.html" %}

<!-- URL -->
<a href="{% url 'name' %}">Link</a>
<a href="{% url 'detail' pk=post.pk %}">Post</a>

<!-- Static files -->
{% load static %}
<img src="{% static 'img/logo.png' %}">

<!-- CSRF Token (required in forms) -->
<form method="POST">
    {% csrf_token %}
    ...
</form>

<!-- Filters -->
{{ text|truncatewords:30 }}
{{ date|date:"F d, Y" }}
{{ name|lower }}
{{ html|safe }}
```

## Django Authentication
```python
# In views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def protected_view(request):
    return render(request, 'protected.html')

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    
# In settings.py
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# In templates
{% if user.is_authenticated %}
    Welcome, {{ user.username }}
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}
```

## Django Forms
```python
from django import forms
from .models import Post

# Model Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        # or exclude = ['author']

# Regular Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

---
**Keep this handy for quick reference! 🚀**
