"""
Blog Models
============
Day 14 - Week 2 Mini Project

This file defines the database models for the blog application.
The Post model represents a blog post with title, content, and author.
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    """
    Post Model
    ----------
    Represents a blog post in the application.
    
    Fields:
        - title: The title of the post (max 200 characters)
        - content: The main body of the post
        - date_posted: When the post was created
        - date_updated: When the post was last updated
        - author: ForeignKey to the User who wrote the post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    class Meta:
        ordering = ['-date_posted']  # Newest posts first
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Return the URL to access the post detail view."""
        return reverse('post-detail', kwargs={'pk': self.pk})
