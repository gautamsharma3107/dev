"""
Hello World Django - Example Views
===================================
Copy this code to your hello/views.py file
"""

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    """Home page view"""
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
    """About page view"""
    context = {
        'title': 'About',
        'description': 'This is a simple Hello World Django app created as part of Day 11 learning.',
        'author': 'Your Name',
        'technologies': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'hello/about.html', context)


def greet(request, name):
    """Dynamic greeting view"""
    return HttpResponse(f'<h1>Hello, {name}!</h1><p><a href="/">Back to Home</a></p>')


def current_time(request):
    """Shows current server time"""
    now = datetime.now()
    context = {
        'current_time': now,
        'formatted_time': now.strftime("%B %d, %Y at %I:%M %p")
    }
    return render(request, 'hello/time.html', context)
