"""
Day 13 - User Authentication
============================
Learn: Django authentication system - login, logout, registration

Key Concepts:
- Django's built-in authentication system
- User model and authentication views
- Creating login/logout functionality
- User registration with UserCreationForm
- Session management
"""

# ========== PART 1: DJANGO AUTH SYSTEM OVERVIEW ==========
print("=" * 60)
print("USER AUTHENTICATION - OVERVIEW")
print("=" * 60)

AUTH_OVERVIEW = '''
Django's authentication system handles:
1. User accounts (User model)
2. Groups and permissions
3. Passwords (hashing, validation)
4. Sessions and cookies
5. Authentication views (login, logout, password reset)

Built-in Components:
- django.contrib.auth - Core authentication framework
- django.contrib.contenttypes - Content type system
- django.contrib.sessions - Session framework

The User model has these fields:
- username (required, unique)
- password (required, hashed)
- email
- first_name
- last_name
- is_active (boolean)
- is_staff (can access admin)
- is_superuser (all permissions)
- date_joined
- last_login
'''

print(AUTH_OVERVIEW)

# ========== PART 2: SETUP AUTHENTICATION ==========
print("\n" + "=" * 60)
print("SETUP AUTHENTICATION")
print("=" * 60)

SETUP_CODE = '''
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',           # Authentication framework
    'django.contrib.contenttypes',   # Content types
    'django.contrib.sessions',       # Session framework
    'django.contrib.messages',       # Messages framework
    'django.contrib.staticfiles',
    # Your apps...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Auth middleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Authentication settings
LOGIN_REDIRECT_URL = 'home'      # Redirect after successful login
LOGOUT_REDIRECT_URL = 'login'   # Redirect after logout
LOGIN_URL = 'login'             # URL for login page
'''

print("\n1. Settings Configuration:")
print("-" * 40)
print(SETUP_CODE)

# ========== PART 3: BUILT-IN LOGIN VIEW ==========
print("\n" + "=" * 60)
print("BUILT-IN LOGIN VIEW")
print("=" * 60)

LOGIN_VIEW_CODE = '''
# Method 1: Using Django's Built-in LoginView
# urls.py (project level)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login view
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True,  # Redirect if already logged in
    ), name='login'),
    
    # Logout view
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'  # Where to redirect after logout
    ), name='logout'),
]

# Create template: templates/registration/login.html
"""
{% extends 'base.html' %}

{% block content %}
<div class="login-container">
    <h2>Login</h2>
    
    {% if form.errors %}
        <div class="alert alert-danger">
            Invalid username or password!
        </div>
    {% endif %}
    
    <form method="post">
        {% csrf_token %}
        
        <div class="form-group">
            {{ form.username.label_tag }}
            {{ form.username }}
        </div>
        
        <div class="form-group">
            {{ form.password.label_tag }}
            {{ form.password }}
        </div>
        
        <button type="submit" class="btn btn-primary">Login</button>
    </form>
    
    <p>Don't have an account? <a href="{% url 'register' %}">Register</a></p>
    <p><a href="{% url 'password_reset' %}">Forgot password?</a></p>
</div>
{% endblock %}
"""
'''

print("\n2. Built-in Login View:")
print("-" * 40)
print(LOGIN_VIEW_CODE)

# ========== PART 4: CUSTOM LOGIN VIEW ==========
print("\n" + "=" * 60)
print("CUSTOM LOGIN VIEW")
print("=" * 60)

CUSTOM_LOGIN_CODE = '''
# Method 2: Creating Custom Login View
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def custom_login_view(request):
    """Custom login view with more control"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                
                # Redirect to 'next' parameter or home
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})


def custom_logout_view(request):
    """Custom logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


# urls.py
urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
]
'''

print("\n3. Custom Login View:")
print("-" * 40)
print(CUSTOM_LOGIN_CODE)

# ========== PART 5: USER REGISTRATION ==========
print("\n" + "=" * 60)
print("USER REGISTRATION")
print("=" * 60)

REGISTRATION_CODE = '''
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    """Extended registration form with email"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes to password fields
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
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        if commit:
            user.save()
        return user


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, 'Registration successful! Welcome!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


# urls.py
urlpatterns = [
    path('register/', register_view, name='register'),
]
'''

print("\n4. User Registration:")
print("-" * 40)
print(REGISTRATION_CODE)

# ========== PART 6: REGISTRATION TEMPLATE ==========
print("\n" + "=" * 60)
print("REGISTRATION TEMPLATE")
print("=" * 60)

REGISTER_TEMPLATE_CODE = '''
<!-- templates/registration/register.html -->
{% extends 'base.html' %}

{% block content %}
<div class="register-container">
    <h2>Create Account</h2>
    
    <form method="post">
        {% csrf_token %}
        
        {% if form.non_field_errors %}
            <div class="alert alert-danger">
                {% for error in form.non_field_errors %}
                    <p>{{ error }}</p>
                {% endfor %}
            </div>
        {% endif %}
        
        <div class="form-group">
            <label for="{{ form.username.id_for_label }}">Username</label>
            {{ form.username }}
            {% if form.username.errors %}
                <small class="text-danger">{{ form.username.errors }}</small>
            {% endif %}
        </div>
        
        <div class="form-group">
            <label for="{{ form.email.id_for_label }}">Email</label>
            {{ form.email }}
            {% if form.email.errors %}
                <small class="text-danger">{{ form.email.errors }}</small>
            {% endif %}
        </div>
        
        <div class="form-row">
            <div class="form-group col-md-6">
                <label for="{{ form.first_name.id_for_label }}">First Name</label>
                {{ form.first_name }}
            </div>
            <div class="form-group col-md-6">
                <label for="{{ form.last_name.id_for_label }}">Last Name</label>
                {{ form.last_name }}
            </div>
        </div>
        
        <div class="form-group">
            <label for="{{ form.password1.id_for_label }}">Password</label>
            {{ form.password1 }}
            {% if form.password1.errors %}
                <small class="text-danger">{{ form.password1.errors }}</small>
            {% endif %}
            <small class="form-text text-muted">
                {{ form.password1.help_text }}
            </small>
        </div>
        
        <div class="form-group">
            <label for="{{ form.password2.id_for_label }}">Confirm Password</label>
            {{ form.password2 }}
            {% if form.password2.errors %}
                <small class="text-danger">{{ form.password2.errors }}</small>
            {% endif %}
        </div>
        
        <button type="submit" class="btn btn-primary btn-block">Register</button>
    </form>
    
    <p class="mt-3">Already have an account? <a href="{% url 'login' %}">Login</a></p>
</div>
{% endblock %}
'''

print("\n5. Registration Template:")
print("-" * 40)
print(REGISTER_TEMPLATE_CODE)

# ========== PART 7: PASSWORD RESET ==========
print("\n" + "=" * 60)
print("PASSWORD RESET FUNCTIONALITY")
print("=" * 60)

PASSWORD_RESET_CODE = '''
# urls.py - Add password reset URLs
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Password reset request
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html',
             email_template_name='registration/password_reset_email.html',
             subject_template_name='registration/password_reset_subject.txt',
         ), name='password_reset'),
    
    # Password reset email sent confirmation
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), name='password_reset_done'),
    
    # Password reset confirm (link from email)
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ), name='password_reset_confirm'),
    
    # Password reset complete
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), name='password_reset_complete'),
]

# settings.py - Email configuration for password reset
# For development, use console email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For production, configure actual email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your@email.com'
# EMAIL_HOST_PASSWORD = 'your-app-password'


# Templates for password reset:
"""
<!-- password_reset.html -->
<h2>Reset Your Password</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Reset Password</button>
</form>

<!-- password_reset_done.html -->
<h2>Password Reset Email Sent</h2>
<p>Check your email for instructions to reset your password.</p>

<!-- password_reset_confirm.html -->
<h2>Set New Password</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Set Password</button>
</form>

<!-- password_reset_complete.html -->
<h2>Password Reset Complete</h2>
<p>Your password has been reset. <a href="{% url 'login' %}">Login now</a></p>
"""
'''

print("\n6. Password Reset:")
print("-" * 40)
print(PASSWORD_RESET_CODE)

# ========== PART 8: CHECKING USER IN TEMPLATES ==========
print("\n" + "=" * 60)
print("USER IN TEMPLATES AND VIEWS")
print("=" * 60)

USER_ACCESS_CODE = '''
# Accessing user in views
# views.py
from django.shortcuts import render

def profile_view(request):
    if request.user.is_authenticated:
        # User is logged in
        username = request.user.username
        email = request.user.email
        # Get user's posts, orders, etc.
        user_data = {
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'date_joined': request.user.date_joined,
        }
        return render(request, 'profile.html', {'user_data': user_data})
    else:
        # User is not logged in
        return redirect('login')


# templates/base.html - Navigation with auth check
"""
<nav>
    <a href="{% url 'home' %}">Home</a>
    
    {% if user.is_authenticated %}
        <span>Welcome, {{ user.username }}!</span>
        <a href="{% url 'profile' %}">Profile</a>
        <a href="{% url 'logout' %}">Logout</a>
        
        {% if user.is_staff %}
            <a href="{% url 'admin:index' %}">Admin</a>
        {% endif %}
    {% else %}
        <a href="{% url 'login' %}">Login</a>
        <a href="{% url 'register' %}">Register</a>
    {% endif %}
</nav>
"""

# templates/profile.html
"""
{% extends 'base.html' %}

{% block content %}
<div class="profile-container">
    <h2>{{ user.username }}'s Profile</h2>
    
    <div class="profile-info">
        <p><strong>Username:</strong> {{ user.username }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Name:</strong> {{ user.get_full_name }}</p>
        <p><strong>Member since:</strong> {{ user.date_joined|date:"F d, Y" }}</p>
        <p><strong>Last login:</strong> {{ user.last_login|date:"F d, Y H:i" }}</p>
    </div>
    
    <a href="{% url 'edit_profile' %}" class="btn">Edit Profile</a>
    <a href="{% url 'change_password' %}" class="btn">Change Password</a>
</div>
{% endblock %}
"""
'''

print("\n7. Accessing User:")
print("-" * 40)
print(USER_ACCESS_CODE)

# ========== PART 9: COMPLETE AUTH SETUP ==========
print("\n" + "=" * 60)
print("COMPLETE AUTHENTICATION SETUP")
print("=" * 60)

COMPLETE_SETUP_CODE = '''
# Complete auth setup in one place

# 1. accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login/Logout
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    
    # Registration
    path('register/', views.register_view, name='register'),
    
    # Profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    
    # Password change (for logged-in users)
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change.html',
        success_url='/accounts/password-change/done/'
    ), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'
    ), name='password_change_done'),
    
    # Password reset (forgot password)
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]

# 2. project/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # ... other app urls
]

# 3. settings.py
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

# 4. Create templates directory structure:
"""
templates/
├── base.html
└── registration/
    ├── login.html
    ├── register.html
    ├── password_change.html
    ├── password_change_done.html
    ├── password_reset.html
    ├── password_reset_done.html
    ├── password_reset_confirm.html
    └── password_reset_complete.html
"""
'''

print("\n8. Complete Auth Setup:")
print("-" * 40)
print(COMPLETE_SETUP_CODE)

print("\n" + "=" * 60)
print("✅ User Authentication - Complete!")
print("=" * 60)
print("\nNext: 04_protecting_views.py - Learn to protect views with @login_required")
