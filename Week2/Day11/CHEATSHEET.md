# Day 11 Quick Reference Cheat Sheet

## Django Installation
```bash
# Install Django
pip install django

# Check version
python -m django --version

# Create project
django-admin startproject project_name

# Create app
python manage.py startapp app_name

# Run server
python manage.py runserver
python manage.py runserver 8080  # Custom port
```

## Project Structure
```
project_name/
├── manage.py              # CLI utility
├── project_name/
│   ├── __init__.py       # Package marker
│   ├── settings.py       # Configuration
│   ├── urls.py           # URL routing
│   ├── asgi.py           # ASGI config
│   └── wsgi.py           # WSGI config
```

## App Structure
```
app_name/
├── __init__.py
├── admin.py              # Admin config
├── apps.py               # App config
├── models.py             # Database models
├── views.py              # View functions
├── tests.py              # Tests
├── urls.py               # App URLs (create this)
└── templates/            # Templates (create this)
```

## Register App in settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... other apps
    'myapp',  # Add your app here
]
```

## URL Routing

### Main urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```

### App urls.py
```python
from django.urls import path
from . import views

app_name = 'myapp'  # Namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user/<int:id>/', views.user_detail, name='user_detail'),
    path('post/<slug:slug>/', views.post, name='post'),
]
```

### Path Converters
```python
<int:id>        # Integer: 123
<str:name>      # String (default): hello
<slug:slug>     # Slug: my-post-title
<uuid:id>       # UUID: 075194d3-6885-417e-a8a8-6c931e272f00
<path:subpath>  # Path with slashes: path/to/file
```

## Views

### Basic Function View
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")
```

### View with Template
```python
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Welcome',
        'items': ['a', 'b', 'c']
    }
    return render(request, 'home.html', context)
```

### View with URL Parameters
```python
def user_detail(request, id):
    return HttpResponse(f"User ID: {id}")
```

### Redirects
```python
from django.shortcuts import redirect

def old_page(request):
    return redirect('myapp:home')  # Named URL
```

## Templates

### Template Location
```
myapp/
└── templates/
    └── myapp/
        ├── base.html
        └── home.html
```

### Basic Template (home.html)
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>Welcome to Django!</p>
</body>
</html>
```

### Template Variables
```html
{{ variable }}
{{ user.name }}
{{ list.0 }}
{{ dict.key }}
```

### Template Tags
```html
{% if condition %}
    <p>True</p>
{% elif other %}
    <p>Other</p>
{% else %}
    <p>False</p>
{% endif %}

{% for item in items %}
    <p>{{ forloop.counter }}. {{ item }}</p>
{% empty %}
    <p>No items</p>
{% endfor %}

{% url 'myapp:home' %}
{% url 'myapp:user_detail' id=5 %}
```

### Template Filters
```html
{{ name|lower }}
{{ name|upper }}
{{ text|truncatewords:30 }}
{{ date|date:"Y-m-d" }}
{{ value|default:"N/A" }}
{{ list|length }}
{{ number|floatformat:2 }}
```

### Template Inheritance

**base.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Site{% endblock %}</title>
</head>
<body>
    <nav>Navigation</nav>
    {% block content %}{% endblock %}
    <footer>Footer</footer>
</body>
</html>
```

**child.html:**
```html
{% extends 'myapp/base.html' %}

{% block title %}Home - {{ block.super }}{% endblock %}

{% block content %}
    <h1>Home Page</h1>
{% endblock %}
```

## Common HttpResponse Types
```python
from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseRedirect,
    Http404,
)

# Plain text
return HttpResponse("Hello")

# JSON
return JsonResponse({'key': 'value'})

# Redirect
return HttpResponseRedirect('/new-url/')

# 404 Error
from django.shortcuts import get_object_or_404
raise Http404("Page not found")
```

## Useful Shortcuts
```python
from django.shortcuts import render, redirect, get_object_or_404

# Render template
render(request, 'template.html', context)

# Redirect
redirect('view_name')
redirect('/absolute/url/')
redirect('https://example.com')

# Get or 404
get_object_or_404(Model, pk=id)
```

## Request Object
```python
def view(request):
    request.method      # 'GET', 'POST'
    request.GET         # Query params dict
    request.POST        # POST data dict
    request.path        # '/current/path/'
    request.user        # Current user
    request.session     # Session dict
```

---
**Keep this handy for Day 11 topics!** 🚀
