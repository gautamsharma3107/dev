# Django Full-Featured Framework: Complete Guide

---

## Table of Contents
1. [Introduction to Django](#introduction-to-django)
2. [Django Basics](#django-basics)
3. [Models](#models)
4. [Django ORM](#django-orm)
5. [Views](#views)
6. [URL Routing](#url-routing)
7. [Templates](#templates)
8. [Forms](#forms)
9. [Django Admin](#django-admin)
10. [Django REST Framework](#django-rest-framework)
11. [Middleware](#middleware)
12. [Signals](#signals)
13. [Practical Examples](#practical-examples)
14. [Best Practices](#best-practices)
15. [Practice Exercises](#practice-exercises)

---

## Introduction to Django

### What is Django?

Django is a high-level, full-featured Python web framework for building scalable web applications and APIs.

### Django Philosophy

```
Batteries Included:
- Admin interface built-in
- ORM for databases
- Forms with validation
- Authentication system
- Powerful template engine
- URL routing
- Middleware system

Design Principles:
- DRY (Don't Repeat Yourself)
- Explicit is better than implicit
- Rapid development
- Security-focused
- Scalable
```

### Django vs Flask vs FastAPI

```
Django:
✓ Full-featured
✓ Admin interface
✓ Built-in ORM
✓ Batteries included
✗ Heavier
✗ Steeper learning curve

Flask:
✓ Lightweight
✓ Flexible
✓ Easy to learn
✗ Minimal built-in
✗ More dependencies needed

FastAPI:
✓ Modern async
✓ Type hints
✓ Auto docs
✓ API-focused
✗ Fewer batteries
```

---

## Django Basics

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install Django
pip install django

# Check version
django-admin --version
```

### Creating a Project

```bash
# Create project
django-admin startproject myproject
cd myproject

# Create app
python manage.py startapp myapp

# Run development server
python manage.py runserver

# Run on different port
python manage.py runserver 8080
```

### Project Structure

```
myproject/
├── manage.py              # Command-line utility
├── myproject/             # Project package
│   ├── __init__.py
│   ├── settings.py        # Configuration
│   ├── urls.py            # URL routing
│   ├── asgi.py            # ASGI config
│   └── wsgi.py            # WSGI config
├── myapp/                 # Django app
│   ├── migrations/        # Database migrations
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Database models
│   ├── tests.py           # Tests
│   ├── urls.py            # App URLs
│   └── views.py           # Views
├── templates/             # HTML templates
├── static/                # CSS, JS, images
└── requirements.txt       # Dependencies
```

### Settings Configuration

```python
# settings.py

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Your app
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Secret key (use environment variable in production)
SECRET_KEY = 'your-secret-key'

# Debug mode
DEBUG = True  # False in production

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    },
]
```

### django-admin Commands

```bash
# Create project
django-admin startproject myproject

# Create app
python manage.py startapp myapp

# Migrations
python manage.py makemigrations          # Create migrations
python manage.py migrate                 # Apply migrations
python manage.py migrate myapp          # Apply specific app migrations

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Start shell
python manage.py shell

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic

# Create cache table
python manage.py createcachetable

# Check deployment
python manage.py check --deploy

# Custom commands
python manage.py help                   # List all commands
python manage.py help startapp          # Help for specific command
```

---

## Models

### Defining Models

```python
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Users"
        indexes = [
            models.Index(fields=['username']),
        ]
    
    def __str__(self):
        return self.username
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

### Field Types

```python
# String fields
CharField(max_length=100)
TextField()
SlugField(max_length=50)
URLField()
EmailField()

# Numeric fields
IntegerField()
BigIntegerField()
FloatField()
DecimalField(max_digits=10, decimal_places=2)

# Date/Time fields
DateField()
TimeField()
DateTimeField()
DurationField()

# Boolean/Choice fields
BooleanField(default=False)
NullBooleanField()
ChoiceField(choices=[('A', 'Choice A'), ('B', 'Choice B')])

# File fields
FileField(upload_to='files/')
ImageField(upload_to='images/')

# Special fields
AutoField()
UUIDField()
JSONField()

# Field options
null=True              # Allow NULL
blank=True             # Allow blank in forms
default=value          # Default value
unique=True            # Unique constraint
db_index=True          # Create database index
choices=[]             # Limited choices
help_text="Help"       # Form help text
verbose_name="Name"    # Human-readable name
validators=[]          # Custom validators
```

### Model Relationships

```python
# ForeignKey (One-to-Many)
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # Delete posts if user deleted
        related_name='posts'
    )

# Access
user = User.objects.first()
user_posts = user.posts.all()

# OneToOneField (One-to-One)
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField()

# ManyToManyField (Many-to-Many)
class Course(models.Model):
    students = models.ManyToManyField(User, related_name='courses')

# Access
course = Course.objects.first()
course_students = course.students.all()

# Add through model
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, null=True)
    
class Course(models.Model):
    students = models.ManyToManyField(User, through=Enrollment)
```

### Meta Options

```python
class Meta:
    # Ordering
    ordering = ['-created_at']  # Default ordering
    
    # Naming
    verbose_name = "User"
    verbose_name_plural = "Users"
    
    # Database
    db_table = 'custom_table_name'
    indexes = [
        models.Index(fields=['username']),
        models.Index(fields=['email', 'is_active']),
    ]
    unique_together = [['username', 'email']]
    
    # Permissions
    permissions = [
        ("can_publish", "Can publish posts"),
    ]
```

### Migrations

```bash
# Create migrations
python manage.py makemigrations

# Create specific app migrations
python manage.py makemigrations myapp

# See SQL
python manage.py sqlmigrate myapp 0001

# Apply migrations
python manage.py migrate

# Apply specific migration
python manage.py migrate myapp 0002

# Rollback to previous
python manage.py migrate myapp 0001

# Rollback all
python manage.py migrate myapp zero

# Show migration status
python manage.py showmigrations

# Create empty migration
python manage.py makemigrations --empty myapp --name custom_name
```

---

## Django ORM

### Basic Queries

```python
# All objects
all_users = User.objects.all()

# Get first
first_user = User.objects.first()

# Get last
last_user = User.objects.last()

# Get specific
user = User.objects.get(id=1)
user = User.objects.get(username='alice')

# Filter
active_users = User.objects.filter(is_active=True)

# Exclude
inactive_users = User.objects.exclude(is_active=True)

# Count
count = User.objects.count()

# Exists
exists = User.objects.filter(username='alice').exists()

# Values (return dictionaries)
users_dict = User.objects.values('username', 'email')

# Values list (return tuples)
usernames = User.objects.values_list('username', flat=True)
```

### Q Objects (Complex Queries)

```python
from django.db.models import Q

# OR query
users = User.objects.filter(
    Q(first_name='Alice') | Q(first_name='Bob')
)

# AND query
users = User.objects.filter(
    Q(first_name='Alice') & Q(is_active=True)
)

# NOT query
users = User.objects.filter(
    ~Q(is_active=False)
)

# Complex combinations
users = User.objects.filter(
    (Q(first_name='Alice') | Q(first_name='Bob')) & Q(is_active=True)
)
```

### F Expressions

```python
from django.db.models import F

# Reference field values
expensive_items = Item.objects.filter(
    price__gt=F('discount_price')
)

# Arithmetic operations
Item.objects.all().update(price=F('price') * 1.1)  # Increase by 10%

# String operations
User.objects.all().update(
    full_name=F('first_name').concat(F('last_name'), Value(' '))
)
```

### Aggregations

```python
from django.db.models import Count, Sum, Avg, Min, Max

# Count
user_count = User.objects.count()

# Sum
total_price = Item.objects.aggregate(Sum('price'))

# Average
avg_price = Item.objects.aggregate(Avg('price'))

# Min/Max
min_price = Item.objects.aggregate(Min('price'))
max_price = Item.objects.aggregate(Max('price'))

# Multiple aggregations
stats = Item.objects.aggregate(
    total=Sum('price'),
    average=Avg('price'),
    count=Count('id')
)
# Result: {'total': 1000, 'average': 50, 'count': 20}
```

### Annotations

```python
from django.db.models import Count, Avg

# Add annotation to each object
users_with_post_count = User.objects.annotate(
    post_count=Count('posts')
)

for user in users_with_post_count:
    print(f"{user.username}: {user.post_count} posts")

# Filter by annotation
active_users = User.objects.annotate(
    post_count=Count('posts')
).filter(post_count__gt=0)

# Aggregate grouped results
posts_per_user = User.objects.annotate(
    total_posts=Count('posts')
).values('username', 'total_posts')
```

### Select Related and Prefetch Related

```python
# N+1 problem
posts = Post.objects.all()
for post in posts:
    print(post.author.username)  # N+1 queries!

# Solution 1: select_related (for ForeignKey, OneToOne)
posts = Post.objects.select_related('author')
for post in posts:
    print(post.author.username)  # No additional queries

# Solution 2: prefetch_related (for ManyToMany, reverse ForeignKey)
users = User.objects.prefetch_related('posts')
for user in users:
    for post in user.posts.all():
        print(post.title)  # Efficient queries

# Combine both
posts = Post.objects.select_related('author').prefetch_related(
    'comments__author'
)
```

---

## Views

### Function-Based Views (FBV)

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

@require_http_methods(["GET", "POST"])
def user_list(request):
    if request.method == 'POST':
        # Handle POST
        username = request.POST.get('username')
        user = User.objects.create(username=username)
        return redirect('user-detail', pk=user.pk)
    
    # Handle GET
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/detail.html', {'user': user})

@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user-list')
    return render(request, 'users/delete.html', {'user': user})
```

### Class-Based Views (CBV)

```python
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Basic CBV
class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/list.html', {'users': users})
    
    def post(self, request):
        username = request.POST.get('username')
        user = User.objects.create(username=username)
        return redirect('user-detail', pk=user.pk)

# Generic ListView
class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    paginate_by = 10
    
    def get_queryset(self):
        return User.objects.filter(is_active=True)

# Generic DetailView
class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'
    context_object_name = 'user'

# Generic CreateView
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'first_name']
    template_name = 'users/form.html'
    success_url = reverse_lazy('user-list')

# Generic UpdateView
class UserUpdateView(UpdateView):
    model = User
    fields = ['email', 'first_name', 'last_name']
    template_name = 'users/form.html'
    success_url = reverse_lazy('user-list')

# Generic DeleteView
class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user-list')

# With authentication
class ProtectedListView(LoginRequiredMixin, ListView):
    model = User
    login_url = 'login'
    template_name = 'users/list.html'
```

### Mixins

```python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Custom mixin
class IsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

# Use mixin
class PostDetailView(IsOwnerMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'

# Multiple mixins
class ProtectedOwnedListView(LoginRequiredMixin, IsOwnerMixin, ListView):
    model = Post
    template_name = 'posts/list.html'
```

---

## URL Routing

### URL Patterns

```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('users/<int:pk>/edit/', views.user_edit, name='user-edit'),
]

# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]
```

### URL Parameters

```python
# String parameter
path('blog/<slug:slug>/', views.post_detail, name='post-detail')

# Integer parameter
path('posts/<int:post_id>/', views.post_detail, name='post-detail')

# UUID parameter
path('posts/<uuid:post_uuid>/', views.post_detail, name='post-detail')

# Path parameter (includes slashes)
path('files/<path:filepath>/', views.download_file, name='download')

# Optional parameters (use query string)
# URL: /search/?q=python
# View: query = request.GET.get('q')
```

### URL Namespaces

```python
# myapp/urls.py
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.user_list, name='user-list'),
]

# myproject/urls.py
urlpatterns = [
    path('app/', include('myapp.urls')),
]

# In templates
<a href="{% url 'myapp:index' %}">Home</a>
<a href="{% url 'myapp:user-list' %}">Users</a>

# In views
from django.urls import reverse
reverse('myapp:index')
```

### Reverse URL Resolution

```python
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

# In views
def my_view(request):
    return redirect(reverse('user-detail', args=[1]))

# In models
class Post(models.Model):
    title = models.CharField(max_length=200)
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk])

# In templates
{{ object.get_absolute_url }}
{% url 'post-detail' post.id %}
```

---

## Templates

### Django Template Language (DTL)

```html
<!-- Variables -->
{{ variable }}
{{ object.attribute }}
{{ list.0 }}
{{ dict.key }}

<!-- Filters -->
{{ text|upper }}
{{ text|lower }}
{{ text|title }}
{{ text|truncatewords:5 }}
{{ number|default:0 }}
{{ items|length }}
{{ price|floatformat:2 }}
{{ date|date:"Y-m-d" }}

<!-- Tags -->
{% if condition %}
  ...
{% elif condition %}
  ...
{% else %}
  ...
{% endif %}

{% for item in items %}
  {{ item }}
  {{ forloop.counter }}
{% empty %}
  No items
{% endfor %}
```

### Template Inheritance

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
  <header>
    <h1>My Site</h1>
    {% block nav %}{% endblock %}
  </header>
  
  <main>
    {% block content %}{% endblock %}
  </main>
  
  <footer>
    {% block footer %}{% endblock %}
  </footer>
</body>
</html>

<!-- child.html -->
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block nav %}
  <a href="{% url 'home' %}">Home</a>
  <a href="{% url 'about' %}">About</a>
{% endblock %}

{% block content %}
  <h2>Welcome!</h2>
{% endblock %}
```

### Custom Template Tags and Filters

```python
# myapp/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.simple_tag
def total_posts(user):
    return user.posts.count()

@register.inclusion_tag('user_card.html')
def show_user_card(user):
    return {'user': user}
```

```html
<!-- In template -->
{% load custom_tags %}

{{ price|multiply:2 }}
Total: {% total_posts user %}
{% show_user_card user %}
```

---

## Forms

### Django Forms

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already used")
        return email
```

### Model Forms

```python
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
        labels = {
            'username': 'Your Username',
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
```

### Form Validation

```python
class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')
        
        if password != confirm:
            raise forms.ValidationError("Passwords don't match")
        
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError("Too short")
        return username
```

### Formsets

```python
from django.forms import modelformset_factory

# Create formset
UserFormSet = modelformset_factory(User, form=UserForm, extra=1)

# In view
def edit_users(request):
    if request.method == 'POST':
        formset = UserFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('user-list')
    else:
        formset = UserFormSet()
    
    return render(request, 'edit_users.html', {'formset': formset})
```

---

## Django Admin

### Registering Models

```python
# myapp/admin.py
from django.contrib import admin
from .models import User, Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['username', 'email']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('username', 'email')
        }),
        ('Personal', {
            'fields': ('first_name', 'last_name', 'bio')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)
```

### Admin Actions

```python
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    actions = ['make_active', 'make_inactive']
    
    @admin.action(description='Mark as active')
    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    
    @admin.action(description='Mark as inactive')
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
```

---

## Django REST Framework

### Serializers

```python
from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
```

### Views and ViewSets

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        user = self.get_object()
        posts = user.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
```

### Routers

```python
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### Authentication and Permissions

```python
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
```

### Pagination, Filtering, Throttling

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour',
    }
}

# In viewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ['author', 'created_at']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
```

---

## Middleware

### Understanding Middleware

```
Request → Middleware 1 → Middleware 2 → View
Response ← Middleware 1 ← Middleware 2 ← View
```

### Custom Middleware

```python
# myapp/middleware.py
from django.utils.deprecation import MiddlewareMixin
import time

class RequestTimingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
    
    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            response['X-Process-Time'] = f"{duration:.2f}s"
        return response

# settings.py
MIDDLEWARE = [
    # ...
    'myapp.middleware.RequestTimingMiddleware',
]
```

---

## Signals

### Built-in Signals

```python
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User

# Receiver function
@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance.username}")
        # Send welcome email, create profile, etc.

@receiver(post_delete, sender=User)
def user_deleted(sender, instance, **kwargs):
    print(f"User deleted: {instance.username}")
```

### Custom Signals

```python
from django.dispatch import Signal

# Define signal
post_published = Signal()

# Send signal
from django.dispatch import receiver
from .signals import post_published

class Post(models.Model):
    # ...
    def publish(self):
        self.is_published = True
        self.save()
        post_published.send(sender=self.__class__, instance=self)

# Receiver
@receiver(post_published)
def handle_post_published(sender, instance, **kwargs):
    print(f"Post published: {instance.title}")
    # Send notification, update cache, etc.
```

---

## Practical Examples

### Complete Blog Application

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

# views.py
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = kwargs['post_id']
            comment.save()
            return redirect('post-detail', slug=comment.post.slug)
        return self.form_invalid(form)

# urls.py
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comment/', CommentCreateView.as_view(), name='comment-create'),
]
```

---

## Best Practices

### Code Organization

```
✓ Keep models clean
✓ Use managers for complex queries
✓ Separate serializers for different use cases
✓ Use viewsets for standard operations
✓ Custom permissions for complex logic
✓ Cache expensive queries
✓ Use signals for decoupled logic
```

### Performance

```
✓ Use select_related and prefetch_related
✓ Index frequently queried fields
✓ Use database query optimization
✓ Cache at multiple levels
✓ Use pagination
✓ Minimize database hits
```

### Security

```
✓ Use Django's built-in security features
✓ CSRF tokens in forms
✓ SQL injection prevention (ORM)
✓ XSS prevention (template escaping)
✓ Secure password hashing
✓ Validate input
✓ Use HTTPS
```

---

## Practice Exercises

### 1. Basic Models
- Create models with relationships
- Run migrations
- Query data

### 2. Views and Templates
- Create views (FBV and CBV)
- Render templates
- Pagination

### 3. Forms
- Create forms
- Validate data
- Handle submissions

### 4. Admin Interface
- Register models
- Customize display
- Add actions

### 5. REST API
- Create serializers
- Build API endpoints
- Add authentication

### 6. Complete Application
- Models, views, templates
- Forms and validation
- Admin interface
- REST API

---

# End of Notes
