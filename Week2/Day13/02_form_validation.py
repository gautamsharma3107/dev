"""
Day 13 - Form Validation
========================
Learn: Django form validation techniques

Key Concepts:
- Built-in field validators
- Custom field validation (clean_<fieldname>)
- Form-wide validation (clean method)
- Error handling and display
"""

# ========== PART 1: BUILT-IN VALIDATORS ==========
print("=" * 60)
print("FORM VALIDATION - BUILT-IN VALIDATORS")
print("=" * 60)

BUILTIN_VALIDATORS_CODE = '''
# forms.py
from django import forms
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
    EmailValidator,
    URLValidator,
)

class UserForm(forms.Form):
    # Field-level validation arguments
    username = forms.CharField(
        min_length=3,           # Minimum length
        max_length=20,          # Maximum length
    )
    
    age = forms.IntegerField(
        min_value=13,           # Minimum value
        max_value=120,          # Maximum value
    )
    
    email = forms.EmailField()  # Built-in email validation
    
    website = forms.URLField(required=False)  # Built-in URL validation
    
    # Using validators parameter
    phone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\\+?1?\\d{9,15}$',
                message='Enter a valid phone number'
            )
        ]
    )
    
    # Multiple validators
    password = forms.CharField(
        validators=[
            MinLengthValidator(8, message='Password must be at least 8 characters'),
        ],
        widget=forms.PasswordInput
    )
'''

print("\n1. Built-in Validators:")
print("-" * 40)
print(BUILTIN_VALIDATORS_CODE)

# ========== PART 2: CUSTOM FIELD VALIDATION ==========
print("\n" + "=" * 60)
print("CUSTOM FIELD VALIDATION (clean_<fieldname>)")
print("=" * 60)

CUSTOM_FIELD_VALIDATION_CODE = '''
# forms.py
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    # Custom validation for username field
    def clean_username(self):
        """
        clean_<fieldname> method validates a single field
        Called automatically when form.is_valid() is called
        """
        username = self.cleaned_data['username']
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken!")
        
        # Check for invalid characters
        if not username.isalnum():
            raise forms.ValidationError("Username can only contain letters and numbers!")
        
        # Check if username is reserved
        reserved = ['admin', 'root', 'superuser', 'administrator']
        if username.lower() in reserved:
            raise forms.ValidationError("This username is reserved!")
        
        # Always return the cleaned data
        return username
    
    # Custom validation for email field
    def clean_email(self):
        email = self.cleaned_data['email']
        
        # Check for disposable email domains
        disposable_domains = ['tempmail.com', 'throwaway.com', 'mailinator.com']
        domain = email.split('@')[-1]
        
        if domain in disposable_domains:
            raise forms.ValidationError("Disposable email addresses are not allowed!")
        
        # Check if email already registered
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists!")
        
        return email
    
    # Custom validation for password
    def clean_password(self):
        password = self.cleaned_data['password']
        
        # Check length
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long!")
        
        # Check for at least one uppercase
        if not any(c.isupper() for c in password):
            raise forms.ValidationError("Password must contain at least one uppercase letter!")
        
        # Check for at least one digit
        if not any(c.isdigit() for c in password):
            raise forms.ValidationError("Password must contain at least one number!")
        
        # Check for at least one special character
        special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        if not any(c in special_chars for c in password):
            raise forms.ValidationError("Password must contain at least one special character!")
        
        return password
'''

print("\n2. Custom Field Validation:")
print("-" * 40)
print(CUSTOM_FIELD_VALIDATION_CODE)

# ========== PART 3: FORM-WIDE VALIDATION ==========
print("\n" + "=" * 60)
print("FORM-WIDE VALIDATION (clean method)")
print("=" * 60)

FORM_WIDE_VALIDATION_CODE = '''
# forms.py
from django import forms

class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, user, *args, **kwargs):
        """Store the user for validation"""
        self.user = user
        super().__init__(*args, **kwargs)
    
    def clean_current_password(self):
        """Verify current password is correct"""
        current_password = self.cleaned_data['current_password']
        if not self.user.check_password(current_password):
            raise forms.ValidationError("Current password is incorrect!")
        return current_password
    
    def clean(self):
        """
        Form-wide validation using clean() method
        Use this when validation depends on multiple fields
        """
        cleaned_data = super().clean()
        
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        current_password = cleaned_data.get('current_password')
        
        # Check if passwords match
        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("New passwords don't match!")
        
        # Check new password is different from current
        if new_password and current_password:
            if new_password == current_password:
                raise forms.ValidationError("New password must be different from current password!")
        
        return cleaned_data


class EventForm(forms.Form):
    """Example: Validate start/end dates"""
    title = forms.CharField(max_length=200)
    start_date = forms.DateField()
    end_date = forms.DateField()
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date must be after start date!")
            
            # Check event duration
            duration = (end_date - start_date).days
            if duration > 30:
                raise forms.ValidationError("Event cannot be longer than 30 days!")
        
        return cleaned_data
'''

print("\n3. Form-wide Validation:")
print("-" * 40)
print(FORM_WIDE_VALIDATION_CODE)

# ========== PART 4: ADDING ERRORS MANUALLY ==========
print("\n" + "=" * 60)
print("ADDING ERRORS MANUALLY")
print("=" * 60)

MANUAL_ERRORS_CODE = '''
# forms.py
from django import forms

class BookingForm(forms.Form):
    room = forms.CharField()
    date = forms.DateField()
    guests = forms.IntegerField(min_value=1)
    
    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        date = cleaned_data.get('date')
        guests = cleaned_data.get('guests')
        
        # Add error to specific field
        if room and not self.is_room_available(room, date):
            self.add_error('room', 'This room is not available on the selected date.')
        
        # Add error to specific field
        if guests and guests > self.get_room_capacity(room):
            self.add_error('guests', f'This room has a maximum capacity of {self.get_room_capacity(room)} guests.')
        
        # Add non-field error (general form error)
        if room and date and self.is_blackout_date(date):
            self.add_error(None, 'Bookings are not available on this date.')
        
        return cleaned_data
    
    def is_room_available(self, room, date):
        # Check room availability in database
        return True
    
    def get_room_capacity(self, room):
        return 4
    
    def is_blackout_date(self, date):
        return False
'''

print("\n4. Adding Errors Manually:")
print("-" * 40)
print(MANUAL_ERRORS_CODE)

# ========== PART 5: DISPLAYING ERRORS IN TEMPLATES ==========
print("\n" + "=" * 60)
print("DISPLAYING ERRORS IN TEMPLATES")
print("=" * 60)

TEMPLATE_ERRORS_CODE = '''
<!-- templates/form.html -->

<form method="post">
    {% csrf_token %}
    
    <!-- Display non-field errors (form-wide errors) -->
    {% if form.non_field_errors %}
        <div class="alert alert-danger">
            {% for error in form.non_field_errors %}
                <p>{{ error }}</p>
            {% endfor %}
        </div>
    {% endif %}
    
    <!-- Display all errors at top -->
    {% if form.errors %}
        <div class="alert alert-danger">
            <h4>Please correct the following errors:</h4>
            <ul>
                {% for field in form %}
                    {% for error in field.errors %}
                        <li><strong>{{ field.label }}:</strong> {{ error }}</li>
                    {% endfor %}
                {% endfor %}
                {% for error in form.non_field_errors %}
                    <li>{{ error }}</li>
                {% endfor %}
            </ul>
        </div>
    {% endif %}
    
    <!-- Render fields with inline errors -->
    {% for field in form %}
        <div class="form-group {% if field.errors %}has-error{% endif %}">
            {{ field.label_tag }}
            {{ field }}
            
            {% if field.errors %}
                <ul class="error-list">
                    {% for error in field.errors %}
                        <li class="text-danger">{{ error }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
            
            {% if field.help_text %}
                <small class="help-text">{{ field.help_text }}</small>
            {% endif %}
        </div>
    {% endfor %}
    
    <button type="submit">Submit</button>
</form>
'''

print("\n5. Template Error Display:")
print("-" * 40)
print(TEMPLATE_ERRORS_CODE)

# ========== PART 6: CUSTOM VALIDATORS ==========
print("\n" + "=" * 60)
print("CUSTOM VALIDATORS (Reusable)")
print("=" * 60)

CUSTOM_VALIDATORS_CODE = '''
# validators.py
from django.core.exceptions import ValidationError
import re

def validate_no_profanity(value):
    """
    Custom validator to check for profanity
    Raise ValidationError if found
    """
    bad_words = ['badword1', 'badword2']  # Add actual bad words
    for word in bad_words:
        if word.lower() in value.lower():
            raise ValidationError(
                f'Your text contains inappropriate language.',
                code='profanity'
            )

def validate_strong_password(value):
    """Custom password strength validator"""
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters.')
    
    if not re.search(r'[A-Z]', value):
        raise ValidationError('Password must contain an uppercase letter.')
    
    if not re.search(r'[a-z]', value):
        raise ValidationError('Password must contain a lowercase letter.')
    
    if not re.search(r'\\d', value):
        raise ValidationError('Password must contain a number.')
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError('Password must contain a special character.')

def validate_file_size(file):
    """Validate file size (max 5MB)"""
    max_size = 5 * 1024 * 1024  # 5MB
    if file.size > max_size:
        raise ValidationError('File size must be less than 5MB.')

def validate_image_extension(file):
    """Validate image file extension"""
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    ext = file.name.lower().split('.')[-1]
    if f'.{ext}' not in valid_extensions:
        raise ValidationError('Only JPG, PNG, and GIF files are allowed.')


# Using custom validators in forms
# forms.py
from django import forms
from .validators import validate_no_profanity, validate_strong_password

class CommentForm(forms.Form):
    content = forms.CharField(
        validators=[validate_no_profanity],
        widget=forms.Textarea
    )

class SignupForm(forms.Form):
    password = forms.CharField(
        validators=[validate_strong_password],
        widget=forms.PasswordInput
    )
'''

print("\n6. Custom Reusable Validators:")
print("-" * 40)
print(CUSTOM_VALIDATORS_CODE)

# ========== PART 7: MODELFORM VALIDATION ==========
print("\n" + "=" * 60)
print("MODELFORM VALIDATION")
print("=" * 60)

MODELFORM_VALIDATION_CODE = '''
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50)

# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category']
    
    def clean_name(self):
        name = self.cleaned_data['name']
        
        # Check for duplicate names (excluding current instance for updates)
        existing = Product.objects.filter(name__iexact=name)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)
        
        if existing.exists():
            raise forms.ValidationError("A product with this name already exists!")
        
        return name
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero!")
        return price
    
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')
        
        # Business logic validation
        if price and quantity:
            total_value = price * quantity
            if total_value > 100000:
                raise forms.ValidationError(
                    "Total inventory value cannot exceed $100,000!"
                )
        
        return cleaned_data
'''

print("\n7. ModelForm Validation:")
print("-" * 40)
print(MODELFORM_VALIDATION_CODE)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Complete Registration Form")
print("=" * 60)

COMPLETE_EXAMPLE_CODE = '''
# forms.py
from django import forms
from django.contrib.auth.models import User
from datetime import date

class CompleteRegistrationForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose a username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your@email.com'
        })
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create a strong password'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    agree_terms = forms.BooleanField(
        label="I agree to the Terms of Service and Privacy Policy"
    )
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken!")
        if not username.isalnum():
            raise forms.ValidationError("Username can only contain letters and numbers!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered!")
        return email
    
    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 13:
            raise forms.ValidationError("You must be at least 13 years old to register!")
        return dob
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match!")
        
        return cleaned_data
'''

print("\nComplete Registration Form Example:")
print("-" * 40)
print(COMPLETE_EXAMPLE_CODE)

print("\n" + "=" * 60)
print("✅ Form Validation - Complete!")
print("=" * 60)
print("\nNext: 03_user_authentication.py - Learn login, logout, and registration")
