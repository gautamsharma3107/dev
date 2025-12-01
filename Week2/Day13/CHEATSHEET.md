# Day 13 Quick Reference Cheat Sheet

## Django Forms Basics
```python
# forms.py
from django import forms
from .models import Post

# Regular Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# Model Form (auto-generates from model)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        # OR exclude = ['created_at']
        # OR fields = '__all__'
```

## Form Fields
```python
# Common field types
forms.CharField(max_length=100)
forms.EmailField()
forms.IntegerField()
forms.DecimalField(max_digits=5, decimal_places=2)
forms.BooleanField()
forms.DateField()
forms.DateTimeField()
forms.ChoiceField(choices=[('a', 'Option A'), ('b', 'Option B')])
forms.FileField()
forms.ImageField()
forms.URLField()
forms.PasswordInput()
```

## Form Widgets
```python
# Customize how fields render
class MyForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        'placeholder': 'Enter message...'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput)
    
    options = forms.ChoiceField(
        choices=[('1', 'One'), ('2', 'Two')],
        widget=forms.RadioSelect
    )
```

## Form Validation
```python
# forms.py
class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    # Single field validation
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists!")
        return username
    
    # Multi-field validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm_password')
        
        if password != confirm:
            raise forms.ValidationError("Passwords don't match!")
        return cleaned_data
```

## Using Forms in Views
```python
# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Access cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Process form...
            return redirect('success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

# For ModelForm - saving to database
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Saves to database
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
```

## Form Template
```html
<!-- templates/contact.html -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

<!-- Custom rendering -->
<form method="post">
    {% csrf_token %}
    {% for field in form %}
        <div class="form-group">
            {{ field.label_tag }}
            {{ field }}
            {% if field.errors %}
                <span class="error">{{ field.errors }}</span>
            {% endif %}
        </div>
    {% endfor %}
    <button type="submit">Submit</button>
</form>

<!-- Individual fields -->
<form method="post">
    {% csrf_token %}
    {{ form.name.label_tag }}
    {{ form.name }}
    {{ form.email.label_tag }}
    {{ form.email }}
    <button type="submit">Submit</button>
</form>
```

## User Authentication Setup
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.auth',      # Already included
    'django.contrib.contenttypes',
]

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

# urls.py (project level)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),
]
```

## User Registration
```python
# forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# views.py
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
```

## Login/Logout Templates
```html
<!-- templates/registration/login.html -->
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
<p>Don't have an account? <a href="{% url 'register' %}">Register</a></p>

<!-- templates/registration/register.html -->
<h2>Register</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
```

## Protecting Views
```python
# Function-based views
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/custom-login/')
def profile(request):
    return render(request, 'profile.html')

# Class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login/'
    redirect_field_name = 'next'
```

## Accessing User in Views/Templates
```python
# In views
def my_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
    
    return render(request, 'page.html')
```

```html
<!-- In templates -->
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Logout</a>
{% else %}
    <a href="{% url 'login' %}">Login</a>
    <a href="{% url 'register' %}">Register</a>
{% endif %}
```

## Password Reset (Built-in Views)
```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'
         ), name='password_reset'),
    
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ), name='password_reset_confirm'),
    
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), name='password_reset_complete'),
]
```

## Messages Framework
```python
# views.py
from django.contrib import messages

def login_view(request):
    # After successful login
    messages.success(request, 'You have been logged in!')
    
    # Other message types
    messages.info(request, 'Info message')
    messages.warning(request, 'Warning message')
    messages.error(request, 'Error message')
```

```html
<!-- In template -->
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
```

## Common Patterns
```python
# Check permissions
from django.contrib.auth.decorators import permission_required

@permission_required('app.add_post')
def create_post(request):
    pass

# User passes test
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_view(request):
    pass

# Get current user's posts
@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'my_posts.html', {'posts': posts})
```

---
**Keep this handy for quick reference!** 🚀
