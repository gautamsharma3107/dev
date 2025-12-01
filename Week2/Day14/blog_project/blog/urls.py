"""
Blog URL Configuration
======================
Day 14 - Week 2 Mini Project

URL patterns for the blog application:
- '' : Home page (list of all posts)
- 'post/<pk>/' : Detail view for a single post
- 'post/new/' : Create a new post
- 'post/<pk>/update/' : Update an existing post
- 'post/<pk>/delete/' : Delete a post
- 'about/' : About page
"""

from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
