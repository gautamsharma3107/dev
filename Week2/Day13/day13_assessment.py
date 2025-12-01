"""
DAY 13 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 13 ASSESSMENT - Django Forms & Authentication")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. Which method is used to validate a single field in a Django form?
a) validate_<fieldname>()
b) clean_<fieldname>()
c) check_<fieldname>()
d) verify_<fieldname>()

Your answer: """)

print("""
Q2. What must be included in the form tag for file uploads to work?
a) method="file"
b) enctype="multipart/form-data"
c) type="file"
d) encoding="file-upload"

Your answer: """)

print("""
Q3. Which setting defines where users are redirected after successful login?
a) LOGIN_URL
b) LOGIN_SUCCESS_URL
c) LOGIN_REDIRECT_URL
d) AUTH_REDIRECT_URL

Your answer: """)

print("""
Q4. What does @login_required do when an unauthenticated user tries to access a protected view?
a) Returns a 403 Forbidden error
b) Returns a 404 Not Found error
c) Redirects to LOGIN_URL with 'next' parameter
d) Throws an authentication exception

Your answer: """)

print("""
Q5. For class-based views, which mixin is used to require authentication?
a) AuthenticationMixin
b) LoginRequiredMixin
c) UserAuthMixin
d) RequireLoginMixin

Your answer: """)

print("""
Q6. What is the purpose of form.cleaned_data?
a) It removes all form data
b) It contains validated and converted form data
c) It cleans HTML tags from input
d) It sanitizes database queries

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a Django form class for a Contact form with the following fields:
    - name (CharField, max 100 characters)
    - email (EmailField)
    - message (CharField with Textarea widget)
    
    Add custom validation to ensure name is at least 2 characters long.
""")

# Write your code here:




print("""
Q8. (2 points) Write a custom login view that:
    - Checks if user is already authenticated (redirect to 'home' if so)
    - Uses AuthenticationForm
    - Shows success message after login
    - Redirects to 'dashboard' after successful login
""")

# Write your code here:




print("""
Q9. (2 points) Create a protected view using @login_required that:
    - Shows only posts created by the current user
    - Orders posts by creation date (newest first)
    - Returns a template called 'my_posts.html'
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between:
     - clean_<fieldname>() method
     - clean() method
     
     When would you use each one? Give an example scenario for each.

Your answer:
""")

# Write your explanation here as comments:
# 



print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) clean_<fieldname>()
Q2: b) enctype="multipart/form-data"
Q3: c) LOGIN_REDIRECT_URL
Q4: c) Redirects to LOGIN_URL with 'next' parameter
Q5: b) LoginRequiredMixin
Q6: b) It contains validated and converted form data

Section B:

Q7:
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters!")
        return name


Q8:
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


Q9:
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'my_posts.html', {'posts': posts})


Section C:

Q10:
clean_<fieldname>() method:
- Used to validate a SINGLE field
- Has access only to that field's data
- Example: Checking if username is unique
  
  def clean_username(self):
      username = self.cleaned_data['username']
      if User.objects.filter(username=username).exists():
          raise forms.ValidationError("Username taken!")
      return username

clean() method:
- Used for form-wide validation
- Has access to ALL cleaned fields
- Use when validation depends on MULTIPLE fields
- Example: Checking if passwords match
  
  def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get('password')
      confirm = cleaned_data.get('confirm_password')
      if password != confirm:
          raise forms.ValidationError("Passwords don't match!")
      return cleaned_data
"""
