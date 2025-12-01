"""
Users URL Configuration
=======================
Day 14 - Week 2 Mini Project

URL patterns for user authentication:
- 'register/' : User registration
- 'login/' : User login
- 'logout/' : User logout
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
