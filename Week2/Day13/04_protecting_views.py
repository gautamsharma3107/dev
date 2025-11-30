"""
Day 13 - Protecting Views
=========================
Learn: How to restrict access to views using decorators and mixins

Key Concepts:
- @login_required decorator for function-based views
- LoginRequiredMixin for class-based views
- Custom permission decorators
- Redirecting unauthorized users
"""

# ========== PART 1: LOGIN_REQUIRED DECORATOR ==========
print("=" * 60)
print("PROTECTING VIEWS - @login_required")
print("=" * 60)

LOGIN_REQUIRED_CODE = '''
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Basic usage - redirects to settings.LOGIN_URL if not authenticated
@login_required
def dashboard(request):
    """Only logged-in users can access this view"""
    return render(request, 'dashboard.html')


# Custom login URL
@login_required(login_url='/accounts/login/')
def profile(request):
    """Redirect to custom login URL if not authenticated"""
    return render(request, 'profile.html')


# Custom redirect field name (default is 'next')
@login_required(redirect_field_name='redirect_to')
def settings_view(request):
    """Use custom redirect parameter name"""
    return render(request, 'settings.html')


# Using with other decorators
from django.views.decorators.http import require_http_methods

@login_required
@require_http_methods(["GET", "POST"])
def edit_profile(request):
    """Requires login AND only accepts GET/POST methods"""
    return render(request, 'edit_profile.html')
'''

print("\n1. @login_required Decorator:")
print("-" * 40)
print(LOGIN_REQUIRED_CODE)

# ========== PART 2: HOW IT WORKS ==========
print("\n" + "=" * 60)
print("HOW @login_required WORKS")
print("=" * 60)

HOW_IT_WORKS = '''
When user tries to access a protected view:

1. If user IS authenticated:
   → View executes normally

2. If user is NOT authenticated:
   → Redirected to LOGIN_URL (from settings.py)
   → 'next' parameter added: /login/?next=/dashboard/
   → After login, user redirected back to original URL


# settings.py configuration
LOGIN_URL = 'login'                 # URL name or path
LOGIN_REDIRECT_URL = 'home'         # After login (if no 'next')
LOGOUT_REDIRECT_URL = 'login'       # After logout

# The 'next' parameter flow:
# 1. User visits /dashboard/ (protected)
# 2. Redirected to /login/?next=/dashboard/
# 3. User logs in
# 4. Redirected to /dashboard/ (from 'next' param)
'''

print(HOW_IT_WORKS)

# ========== PART 3: CLASS-BASED VIEWS ==========
print("\n" + "=" * 60)
print("PROTECTING CLASS-BASED VIEWS")
print("=" * 60)

CBV_CODE = '''
# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

# Basic usage - put LoginRequiredMixin FIRST in inheritance
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


# Custom settings
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = '/accounts/login/'      # Custom login URL
    redirect_field_name = 'redirect_to'  # Custom redirect param


# With ListView
class MyPostsView(LoginRequiredMixin, ListView):
    template_name = 'my_posts.html'
    model = Post
    context_object_name = 'posts'
    
    def get_queryset(self):
        # Only show posts by current user
        return Post.objects.filter(author=self.request.user)


# With CreateView
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'create_post.html'
    
    def form_valid(self, form):
        # Set the author to current user before saving
        form.instance.author = self.request.user
        return super().form_valid(form)


# With UpdateView - only allow editing own posts
class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'edit_post.html'
    
    def get_queryset(self):
        # Only allow editing own posts
        return Post.objects.filter(author=self.request.user)
'''

print("\n2. Class-Based Views with Mixins:")
print("-" * 40)
print(CBV_CODE)

# ========== PART 4: PERMISSION REQUIRED ==========
print("\n" + "=" * 60)
print("PERMISSION-BASED PROTECTION")
print("=" * 60)

PERMISSION_CODE = '''
# Function-based views
from django.contrib.auth.decorators import permission_required

# Requires specific permission
@permission_required('blog.add_post')
def create_post(request):
    """Only users with 'add_post' permission can access"""
    return render(request, 'create_post.html')


# Multiple permissions (all required)
@permission_required(['blog.add_post', 'blog.change_post'])
def manage_posts(request):
    """Requires both permissions"""
    return render(request, 'manage_posts.html')


# Custom behavior if no permission (raise 403 instead of redirect)
@permission_required('blog.delete_post', raise_exception=True)
def delete_post(request, pk):
    """Returns 403 Forbidden if user lacks permission"""
    # Delete post logic
    pass


# Class-based views
from django.contrib.auth.mixins import PermissionRequiredMixin

class CreatePostView(PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
    # Or multiple: permission_required = ['blog.add_post', 'blog.change_post']
    model = Post
    fields = ['title', 'content']


# Checking permissions in views
def some_view(request):
    if request.user.has_perm('blog.add_post'):
        # User has permission
        pass
    
    # Check multiple permissions
    if request.user.has_perms(['blog.add_post', 'blog.change_post']):
        # User has all permissions
        pass
'''

print("\n3. Permission-Based Protection:")
print("-" * 40)
print(PERMISSION_CODE)

# ========== PART 5: USER PASSES TEST ==========
print("\n" + "=" * 60)
print("CUSTOM TESTS - user_passes_test")
print("=" * 60)

USER_PASSES_TEST_CODE = '''
# Function-based views with custom tests
from django.contrib.auth.decorators import user_passes_test

# Check if user is staff
def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def staff_dashboard(request):
    """Only staff members can access"""
    return render(request, 'staff_dashboard.html')


# Check if user is superuser
def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def admin_panel(request):
    """Only superusers can access"""
    return render(request, 'admin_panel.html')


# Custom check - email verified
def is_email_verified(user):
    return user.is_authenticated and user.profile.email_verified

@user_passes_test(is_email_verified)
def premium_content(request):
    """Only users with verified email can access"""
    return render(request, 'premium.html')


# Custom check - is premium user
def is_premium_user(user):
    return user.is_authenticated and hasattr(user, 'subscription') and user.subscription.is_active

@user_passes_test(is_premium_user, login_url='/upgrade/')
def premium_features(request):
    """Only premium subscribers can access"""
    return render(request, 'premium_features.html')


# Class-based views
from django.contrib.auth.mixins import UserPassesTestMixin

class StaffDashboardView(UserPassesTestMixin, TemplateView):
    template_name = 'staff_dashboard.html'
    
    def test_func(self):
        return self.request.user.is_staff


class PremiumContentView(UserPassesTestMixin, TemplateView):
    template_name = 'premium_content.html'
    
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.profile.is_premium
    
    def handle_no_permission(self):
        # Custom handling when test fails
        from django.shortcuts import redirect
        return redirect('upgrade')
'''

print("\n4. Custom Tests with user_passes_test:")
print("-" * 40)
print(USER_PASSES_TEST_CODE)

# ========== PART 6: CHECKING IN TEMPLATES ==========
print("\n" + "=" * 60)
print("CHECKING PERMISSIONS IN TEMPLATES")
print("=" * 60)

TEMPLATE_PERMISSIONS_CODE = '''
<!-- Check authentication -->
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Logout</a>
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}


<!-- Check staff status -->
{% if user.is_staff %}
    <a href="{% url 'admin:index' %}">Admin Panel</a>
{% endif %}


<!-- Check superuser status -->
{% if user.is_superuser %}
    <a href="{% url 'system_settings' %}">System Settings</a>
{% endif %}


<!-- Check specific permission -->
{% if perms.blog.add_post %}
    <a href="{% url 'create_post' %}">Create New Post</a>
{% endif %}

{% if perms.blog.delete_post %}
    <button class="delete-btn">Delete Post</button>
{% endif %}


<!-- Check multiple permissions -->
{% if perms.blog.add_post and perms.blog.change_post %}
    <a href="{% url 'manage_posts' %}">Manage Posts</a>
{% endif %}


<!-- Show different content based on auth status -->
{% if user.is_authenticated %}
    {% if user.profile.is_premium %}
        <div class="premium-content">
            <!-- Premium content here -->
        </div>
    {% else %}
        <div class="upgrade-banner">
            <a href="{% url 'upgrade' %}">Upgrade to Premium</a>
        </div>
    {% endif %}
{% else %}
    <div class="login-prompt">
        <a href="{% url 'login' %}">Login to see more</a>
    </div>
{% endif %}
'''

print("\n5. Checking Permissions in Templates:")
print("-" * 40)
print(TEMPLATE_PERMISSIONS_CODE)

# ========== PART 7: CUSTOM DECORATORS ==========
print("\n" + "=" * 60)
print("CREATING CUSTOM DECORATORS")
print("=" * 60)

CUSTOM_DECORATORS_CODE = '''
# decorators.py
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied

def anonymous_required(view_func):
    """Decorator that redirects authenticated users"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper


def staff_required(view_func):
    """Decorator that requires staff status"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_staff:
            raise PermissionDenied("Staff access required")
        return view_func(request, *args, **kwargs)
    return wrapper


def premium_required(view_func):
    """Decorator that requires premium subscription"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not hasattr(request.user, 'subscription') or not request.user.subscription.is_active:
            messages.warning(request, 'This feature requires a premium subscription.')
            return redirect('upgrade')
        return view_func(request, *args, **kwargs)
    return wrapper


def ajax_login_required(view_func):
    """For AJAX views - return JSON error instead of redirect"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.http import JsonResponse
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return view_func(request, *args, **kwargs)
    return wrapper


# Usage in views.py
from .decorators import anonymous_required, staff_required, premium_required

@anonymous_required
def login_view(request):
    """Only non-authenticated users can access login page"""
    pass


@staff_required
def staff_dashboard(request):
    """Only staff can access"""
    pass


@premium_required
def premium_feature(request):
    """Only premium users can access"""
    pass
'''

print("\n6. Custom Decorators:")
print("-" * 40)
print(CUSTOM_DECORATORS_CODE)

# ========== PART 8: PROTECTING API VIEWS ==========
print("\n" + "=" * 60)
print("PROTECTING API VIEWS")
print("=" * 60)

API_PROTECTION_CODE = '''
# For Django REST Framework views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_profile(request):
    """API endpoint - requires authentication"""
    return Response({'username': request.user.username})


# Class-based API views
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'username': request.user.username})


# Custom permission class
from rest_framework.permissions import BasePermission

class IsPremiumUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            hasattr(request.user, 'subscription') and 
            request.user.subscription.is_active
        )


class PremiumContentAPIView(APIView):
    permission_classes = [IsPremiumUser]
    
    def get(self, request):
        return Response({'premium_data': 'secret content'})
'''

print("\n7. Protecting API Views:")
print("-" * 40)
print(API_PROTECTION_CODE)

# ========== PART 9: COMPLETE EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE EXAMPLE: Blog with Protected Views")
print("=" * 60)

COMPLETE_EXAMPLE_CODE = '''
# views.py - Complete blog views with protection
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


# Public views - no protection
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# Protected views - require login
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)


# Protected + ownership check
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        messages.error(self.request, 'You can only edit your own posts!')
        return redirect('post_list')
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff


# Function-based protected view
@login_required
def my_posts(request):
    """Show only current user's posts"""
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # Protected
    path('post/new/', views.CreatePostView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.UpdatePostView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    path('my-posts/', views.my_posts, name='my_posts'),
]
'''

print("\nComplete Blog Example:")
print("-" * 40)
print(COMPLETE_EXAMPLE_CODE)

print("\n" + "=" * 60)
print("✅ Protecting Views - Complete!")
print("=" * 60)
print("\nNext: 05_user_auth_project.py - Build a complete blog with user authentication")
