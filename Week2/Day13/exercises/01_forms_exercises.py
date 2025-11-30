"""
EXERCISES: Django Forms
========================
Complete all exercises below
"""

# Exercise 1: Create a basic registration form
# TODO: Create a form with username, email, password, and confirm_password fields
# Add appropriate widgets and CSS classes

print("Exercise 1: Registration Form")
print("-" * 40)

# Your code here - create RegistrationForm class




# Exercise 2: Add field validation
# TODO: Modify the form to validate:
# - Username is alphanumeric only
# - Email domain is not from a disposable email provider
# - Password is at least 8 characters

print("\n\nExercise 2: Field Validation")
print("-" * 40)

# Your code here - add clean_<fieldname> methods




# Exercise 3: Add form-wide validation
# TODO: Add clean() method to check:
# - Password and confirm_password match
# - Password doesn't contain the username

print("\n\nExercise 3: Form-wide Validation")
print("-" * 40)

# Your code here - add clean() method




# Exercise 4: Create a ModelForm
# TODO: Create a ModelForm for a Product model with fields:
# - name, description, price, quantity
# Add custom validation for price (must be positive)

print("\n\nExercise 4: ModelForm Creation")
print("-" * 40)

# Your code here - create ProductForm class




# Exercise 5: Create a form view
# TODO: Write a view function that:
# - Shows the ProductForm on GET request
# - Validates and saves the form on POST
# - Displays success/error messages
# - Redirects to product list after success

print("\n\nExercise 5: Form View")
print("-" * 40)

# Your code here - create product_create_view function
