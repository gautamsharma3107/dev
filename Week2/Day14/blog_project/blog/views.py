"""
Blog Views
===========
Day 14 - Week 2 Mini Project

This file contains all views for the blog application:
- PostListView: Display all posts with pagination
- PostDetailView: Display a single post
- PostCreateView: Create a new post
- PostUpdateView: Update an existing post
- PostDeleteView: Delete a post
"""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


class PostListView(ListView):
    """
    Display a list of all blog posts.
    
    - Uses pagination (5 posts per page)
    - Orders posts by date (newest first)
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetailView(DetailView):
    """
    Display a single blog post.
    """
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new blog post.
    
    - Requires user to be logged in
    - Automatically sets the author to the current user
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        """Set the author to the current user before saving."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Update an existing blog post.
    
    - Requires user to be logged in
    - Only allows the author to update their own post
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    
    def test_func(self):
        """Check if the current user is the author of the post."""
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a blog post.
    
    - Requires user to be logged in
    - Only allows the author to delete their own post
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'
    
    def test_func(self):
        """Check if the current user is the author of the post."""
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    """Display the about page."""
    return render(request, 'blog/about.html', {'title': 'About'})
