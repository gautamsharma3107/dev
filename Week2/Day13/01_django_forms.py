"""
Day 13 - Django Forms Basics
============================
Learn: Django forms, ModelForms, widgets, and form handling

Key Concepts:
- Forms are Python classes that handle user input
- ModelForms auto-generate forms from models
- Widgets customize how form fields are rendered
- Always validate form data before processing

IMPORTANT: This is a tutorial file. Run it as Django views.
"""

# ========== PART 1: BASIC FORMS ==========
print("=" * 60)
print("DJANGO FORMS - BASICS")
print("=" * 60)

# --------------------------------------
# STEP 1: Create a Basic Form
# --------------------------------------
# In your app, create forms.py file

BASIC_FORM_CODE = '''
# myapp/forms.py
from django import forms

class ContactForm(forms.Form):
    """A simple contact form"""
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        help_text="Enter your full name"
    )
    email = forms.EmailField(
        label="Email Address"
    )
    subject = forms.CharField(
        max_length=200,
        label="Subject"
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label="Your Message"
    )
'''

print("\n1. Basic Form Definition:")
print("-" * 40)
print(BASIC_FORM_CODE)

# --------------------------------------
# STEP 2: Common Field Types
# --------------------------------------

FIELD_TYPES_CODE = '''
# Common Django Form Field Types
from django import forms

class AllFieldTypesForm(forms.Form):
    # Text fields
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    
    # Numeric fields
    age = forms.IntegerField(min_value=0, max_value=150)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    rating = forms.FloatField()
    
    # Choice fields
    CHOICES = [('a', 'Option A'), ('b', 'Option B'), ('c', 'Option C')]
    option = forms.ChoiceField(choices=CHOICES)
    multiple = forms.MultipleChoiceField(choices=CHOICES)
    
    # Boolean field
    agree = forms.BooleanField(required=True)
    
    # Date/Time fields
    birth_date = forms.DateField()
    appointment = forms.DateTimeField()
    start_time = forms.TimeField()
    
    # Email and URL
    email = forms.EmailField()
    website = forms.URLField(required=False)
    
    # File fields
    document = forms.FileField(required=False)
    photo = forms.ImageField(required=False)
    
    # Hidden field
    user_id = forms.CharField(widget=forms.HiddenInput)
'''

print("\n2. Common Field Types:")
print("-" * 40)
print(FIELD_TYPES_CODE)

# --------------------------------------
# STEP 3: Widgets (Customize Rendering)
# --------------------------------------

WIDGETS_CODE = '''
# Widgets customize how fields are rendered in HTML
from django import forms

class StyledForm(forms.Form):
    # Add CSS classes and attributes
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'id': 'name-field'
        })
    )
    
    # Password field
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )
    
    # Textarea with custom size
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'cols': 40
        })
    )
    
    # Radio buttons instead of dropdown
    GENDER_CHOICES = [('m', 'Male'), ('f', 'Female'), ('o', 'Other')]
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )
    
    # Checkboxes for multiple selection
    HOBBY_CHOICES = [('r', 'Reading'), ('s', 'Sports'), ('m', 'Music')]
    hobbies = forms.MultipleChoiceField(
        choices=HOBBY_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    
    # Date picker
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
'''

print("\n3. Custom Widgets:")
print("-" * 40)
print(WIDGETS_CODE)

# ========== PART 2: MODEL FORMS ==========
print("\n" + "=" * 60)
print("DJANGO MODEL FORMS")
print("=" * 60)

MODEL_FORM_CODE = '''
# ModelForm automatically creates form from a model
# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published']
        # OR exclude = ['author', 'created_at']
        # OR fields = '__all__'
        
        # Customize labels
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }
        
        # Add help text
        help_texts = {
            'title': 'Enter a catchy title',
        }
        
        # Customize widgets
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
'''

print("\n4. ModelForm Definition:")
print("-" * 40)
print(MODEL_FORM_CODE)

# ========== PART 3: USING FORMS IN VIEWS ==========
print("\n" + "=" * 60)
print("USING FORMS IN VIEWS")
print("=" * 60)

VIEW_CODE = '''
# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm, PostForm

# Function-based view with regular form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Access cleaned (validated) data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Process the data (send email, save to DB, etc.)
            # send_email(name, email, subject, message)
            
            return redirect('contact_success')
    else:
        # GET request - show empty form
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


# View with ModelForm - creating new post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save yet
            post.author = request.user      # Add the author
            post.save()                     # Now save
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})


# View for editing existing post
def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Bind to existing object
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)  # Pre-fill with existing data
    
    return render(request, 'edit_post.html', {'form': form})
'''

print("\n5. Views with Forms:")
print("-" * 40)
print(VIEW_CODE)

# ========== PART 4: FORM TEMPLATES ==========
print("\n" + "=" * 60)
print("FORM TEMPLATES")
print("=" * 60)

TEMPLATE_CODE = '''
<!-- templates/contact.html -->

<!-- Method 1: Quick and simple -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

<!-- Method 2: As table -->
<form method="post">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <button type="submit">Submit</button>
</form>

<!-- Method 3: As unordered list -->
<form method="post">
    {% csrf_token %}
    <ul>
        {{ form.as_ul }}
    </ul>
    <button type="submit">Submit</button>
</form>

<!-- Method 4: Manual field rendering (recommended for styling) -->
<form method="post">
    {% csrf_token %}
    
    {% for field in form %}
        <div class="form-group">
            <label for="{{ field.id_for_label }}">{{ field.label }}</label>
            {{ field }}
            {% if field.help_text %}
                <small class="help-text">{{ field.help_text }}</small>
            {% endif %}
            {% if field.errors %}
                <div class="errors">
                    {% for error in field.errors %}
                        <span class="error">{{ error }}</span>
                    {% endfor %}
                </div>
            {% endif %}
        </div>
    {% endfor %}
    
    <button type="submit">Submit</button>
</form>

<!-- Method 5: Individual field access -->
<form method="post">
    {% csrf_token %}
    
    <div class="form-group">
        {{ form.name.label_tag }}
        {{ form.name }}
        {{ form.name.errors }}
    </div>
    
    <div class="form-group">
        {{ form.email.label_tag }}
        {{ form.email }}
        {{ form.email.errors }}
    </div>
    
    <button type="submit">Submit</button>
</form>
'''

print("\n6. Template Rendering:")
print("-" * 40)
print(TEMPLATE_CODE)

# ========== PART 5: HANDLING FILE UPLOADS ==========
print("\n" + "=" * 60)
print("FILE UPLOADS")
print("=" * 60)

FILE_UPLOAD_CODE = '''
# forms.py
class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    avatar = forms.ImageField()
    resume = forms.FileField(required=False)

# views.py
def upload_profile(request):
    if request.method == 'POST':
        # IMPORTANT: Include request.FILES for file uploads
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.cleaned_data['avatar']
            # Save file or process it
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'upload.html', {'form': form})

# template - MUST include enctype for file uploads
# <form method="post" enctype="multipart/form-data">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Upload</button>
# </form>

# settings.py - Configure media files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'
'''

print("\n7. File Uploads:")
print("-" * 40)
print(FILE_UPLOAD_CODE)

# ========== PRACTICAL EXERCISE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXERCISE")
print("=" * 60)

EXERCISE_CODE = '''
# Exercise: Create a registration form with the following fields:
# 1. Username (required, 3-20 characters)
# 2. Email (required, valid email)
# 3. Password (required, password input)
# 4. Confirm Password (required, password input)
# 5. Date of Birth (optional, date field)
# 6. Bio (optional, textarea)
# 7. Agree to Terms (required, checkbox)

# Create the form in forms.py:
class RegistrationForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    agree_terms = forms.BooleanField(
        label="I agree to the terms and conditions"
    )
'''

print("\nExercise Code:")
print("-" * 40)
print(EXERCISE_CODE)

print("\n" + "=" * 60)
print("✅ Django Forms Basics - Complete!")
print("=" * 60)
print("\nNext: 02_form_validation.py - Learn form validation techniques")
