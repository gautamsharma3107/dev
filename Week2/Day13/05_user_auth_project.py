"""
Day 13 - Quick Project: Blog with User Authentication
=====================================================
Complete project combining all Day 13 concepts:
- Django forms
- Form validation
- User authentication (login, logout, register)
- Protected views

This file shows the complete code for a blog application with user auth.
"""

print("=" * 60)
print("QUICK PROJECT: BLOG WITH USER AUTHENTICATION")
print("=" * 60)
print("""
This project demonstrates:
1. User registration with custom form
2. Login/Logout functionality
3. Protected views for creating/editing posts
4. Only post authors can edit/delete their posts
5. Form validation

Follow the code sections below to build your blog!
""")

# ========== STEP 1: PROJECT SETUP ==========
print("\n" + "=" * 60)
print("STEP 1: PROJECT SETUP")
print("=" * 60)

PROJECT_SETUP = '''
# Terminal commands to set up project:

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install Django
pip install django

# Create project
django-admin startproject blog_project
cd blog_project

# Create apps
python manage.py startapp blog
python manage.py startapp accounts

# Project structure:
blog_project/
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
├── accounts/
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
├── templates/
│   ├── base.html
│   └── registration/
└── manage.py
'''

print(PROJECT_SETUP)

# ========== STEP 2: SETTINGS.PY ==========
print("\n" + "=" * 60)
print("STEP 2: SETTINGS CONFIGURATION")
print("=" * 60)

SETTINGS_CODE = '''
# blog_project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom apps
    'blog',
    'accounts',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Authentication settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'post_list'
LOGOUT_REDIRECT_URL = 'login'

# Messages framework (for alerts)
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
'''

print(SETTINGS_CODE)

# ========== STEP 3: MODELS ==========
print("\n" + "=" * 60)
print("STEP 3: BLOG MODELS")
print("=" * 60)

MODELS_CODE = '''
# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'


# Run migrations:
# python manage.py makemigrations
# python manage.py migrate
'''

print(MODELS_CODE)

# ========== STEP 4: FORMS ==========
print("\n" + "=" * 60)
print("STEP 4: FORMS")
print("=" * 60)

FORMS_CODE = '''
# blog/forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post content here...'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long!")
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write a comment...'
            })
        }


# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
'''

print(FORMS_CODE)

# ========== STEP 5: VIEWS ==========
print("\n" + "=" * 60)
print("STEP 5: VIEWS")
print("=" * 60)

VIEWS_CODE = '''
# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    """Public view - shows all published posts"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(published=True)


class PostDetailView(DetailView):
    """Public view - shows single post with comments"""
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """Protected view - create new post"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Protected view - only author can edit"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        messages.error(self.request, 'You can only edit your own posts!')
        return redirect('post_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Protected view - only author can delete"""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self):
        messages.error(self.request, 'You can only delete your own posts!')
        return redirect('post_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def my_posts(request):
    """Show current user's posts (including unpublished)"""
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})


@login_required
def add_comment(request, pk):
    """Add comment to a post"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added!')
    return redirect('post_detail', pk=pk)


# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome!')
            return redirect('post_list')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')
'''

print(VIEWS_CODE)

# ========== STEP 6: URLS ==========
print("\n" + "=" * 60)
print("STEP 6: URL CONFIGURATION")
print("=" * 60)

URLS_CODE = '''
# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
]


# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('my-posts/', views.my_posts, name='my_posts'),
]


# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
'''

print(URLS_CODE)

# ========== STEP 7: TEMPLATES ==========
print("\n" + "=" * 60)
print("STEP 7: TEMPLATES")
print("=" * 60)

TEMPLATES_CODE = '''
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Blog{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'post_list' %}">My Blog</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'post_list' %}">Home</a>
                    </li>
                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'post_create' %}">New Post</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'my_posts' %}">My Posts</a>
                        </li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <span class="nav-link">Hello, {{ user.username }}</span>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'login' %}">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'register' %}">Register</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}
        
        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>


<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h4>Login</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    {% if form.errors %}
                        <div class="alert alert-danger">Invalid username or password!</div>
                    {% endif %}
                    <div class="mb-3">
                        <label class="form-label">Username</label>
                        {{ form.username }}
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Password</label>
                        {{ form.password }}
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
                <p class="mt-3 text-center">
                    Don't have an account? <a href="{% url 'register' %}">Register</a>
                </p>
            </div>
        </div>
    </div>
</div>
{% endblock %}


<!-- templates/registration/register.html -->
{% extends 'base.html' %}

{% block title %}Register{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h4>Create Account</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    {% for field in form %}
                        <div class="mb-3">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}
                                <small class="text-danger">{{ field.errors }}</small>
                            {% endif %}
                            {% if field.help_text %}
                                <small class="form-text text-muted">{{ field.help_text }}</small>
                            {% endif %}
                        </div>
                    {% endfor %}
                    <button type="submit" class="btn btn-primary w-100">Register</button>
                </form>
                <p class="mt-3 text-center">
                    Already have an account? <a href="{% url 'login' %}">Login</a>
                </p>
            </div>
        </div>
    </div>
</div>
{% endblock %}


<!-- templates/blog/post_list.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Latest Posts</h2>
{% for post in posts %}
    <div class="card mb-3">
        <div class="card-body">
            <h5 class="card-title">
                <a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a>
            </h5>
            <p class="card-text text-muted">
                By {{ post.author.username }} | {{ post.created_at|date:"M d, Y" }}
            </p>
            <p class="card-text">{{ post.content|truncatewords:50 }}</p>
            <a href="{% url 'post_detail' post.pk %}" class="btn btn-sm btn-outline-primary">Read More</a>
        </div>
    </div>
{% empty %}
    <p>No posts yet.</p>
{% endfor %}
{% endblock %}


<!-- templates/blog/post_detail.html -->
{% extends 'base.html' %}

{% block content %}
<article>
    <h1>{{ post.title }}</h1>
    <p class="text-muted">
        By {{ post.author.username }} | {{ post.created_at|date:"F d, Y H:i" }}
        {% if user == post.author %}
            | <a href="{% url 'post_update' post.pk %}">Edit</a>
            | <a href="{% url 'post_delete' post.pk %}" class="text-danger">Delete</a>
        {% endif %}
    </p>
    <hr>
    <div>{{ post.content|linebreaks }}</div>
</article>

<hr>
<h4>Comments ({{ post.comments.count }})</h4>

{% if user.is_authenticated %}
    <form method="post" action="{% url 'add_comment' post.pk %}" class="mb-4">
        {% csrf_token %}
        {{ comment_form.content }}
        <button type="submit" class="btn btn-primary mt-2">Add Comment</button>
    </form>
{% else %}
    <p><a href="{% url 'login' %}">Login</a> to add a comment.</p>
{% endif %}

{% for comment in post.comments.all %}
    <div class="card mb-2">
        <div class="card-body">
            <p class="mb-1">{{ comment.content }}</p>
            <small class="text-muted">By {{ comment.author.username }} | {{ comment.created_at|date:"M d, Y H:i" }}</small>
        </div>
    </div>
{% empty %}
    <p>No comments yet.</p>
{% endfor %}
{% endblock %}


<!-- templates/blog/post_form.html -->
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <h2>{% if form.instance.pk %}Edit Post{% else %}Create New Post{% endif %}</h2>
        <form method="post">
            {% csrf_token %}
            {% for field in form %}
                <div class="mb-3">
                    <label class="form-label">{{ field.label }}</label>
                    {{ field }}
                    {% if field.errors %}
                        <small class="text-danger">{{ field.errors }}</small>
                    {% endif %}
                </div>
            {% endfor %}
            <button type="submit" class="btn btn-primary">Save</button>
            <a href="{% url 'post_list' %}" class="btn btn-secondary">Cancel</a>
        </form>
    </div>
</div>
{% endblock %}


<!-- templates/blog/post_confirm_delete.html -->
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card">
            <div class="card-body">
                <h4>Delete Post</h4>
                <p>Are you sure you want to delete "{{ post.title }}"?</p>
                <form method="post">
                    {% csrf_token %}
                    <button type="submit" class="btn btn-danger">Yes, Delete</button>
                    <a href="{% url 'post_detail' post.pk %}" class="btn btn-secondary">Cancel</a>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}


<!-- templates/blog/my_posts.html -->
{% extends 'base.html' %}

{% block content %}
<h2>My Posts</h2>
<a href="{% url 'post_create' %}" class="btn btn-primary mb-3">Create New Post</a>

{% for post in posts %}
    <div class="card mb-3">
        <div class="card-body">
            <h5 class="card-title">
                <a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a>
                {% if not post.published %}
                    <span class="badge bg-warning">Draft</span>
                {% endif %}
            </h5>
            <p class="card-text text-muted">{{ post.created_at|date:"M d, Y" }}</p>
            <a href="{% url 'post_update' post.pk %}" class="btn btn-sm btn-outline-secondary">Edit</a>
            <a href="{% url 'post_delete' post.pk %}" class="btn btn-sm btn-outline-danger">Delete</a>
        </div>
    </div>
{% empty %}
    <p>You haven't created any posts yet.</p>
{% endfor %}
{% endblock %}
'''

print(TEMPLATES_CODE)

# ========== STEP 8: RUNNING THE PROJECT ==========
print("\n" + "=" * 60)
print("STEP 8: RUNNING THE PROJECT")
print("=" * 60)

RUN_PROJECT = '''
# Terminal commands to run the project:

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Visit http://127.0.0.1:8000/ in your browser

# Test the application:
1. Register a new account
2. Login with your credentials
3. Create a new post
4. View and edit your posts
5. Add comments to posts
6. Try to edit someone else's post (should fail)
7. Logout and try to access protected views
'''

print(RUN_PROJECT)

print("\n" + "=" * 60)
print("✅ Quick Project: Blog with User Authentication - Complete!")
print("=" * 60)
print("""
Congratulations! You've learned:
✓ Django forms and ModelForms
✓ Form validation techniques
✓ User authentication (login, logout, register)
✓ Protected views with @login_required
✓ Owner-only access with UserPassesTestMixin
✓ Building a complete blog application

Now take the Day 13 Assessment to test your knowledge!
""")
