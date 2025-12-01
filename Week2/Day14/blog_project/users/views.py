"""
Users Views
============
Day 14 - Week 2 Mini Project

This file contains views for user authentication:
- register: User registration view
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """
    User Registration View
    
    Handles both GET (display form) and POST (process registration) requests.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})
