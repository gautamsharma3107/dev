"""
MINI PROJECT 2: Blog with Full Authentication
==============================================
Build a complete blog application with user authentication.

This is the main project for Day 13 combining all concepts learned:
- Django Forms
- Form Validation
- User Authentication
- Protected Views

Requirements:
1. User registration, login, logout
2. Create, read, update, delete blog posts
3. Only authenticated users can create posts
4. Only post authors can edit/delete their posts
5. Comments on posts (authenticated users only)
6. User profile with their posts
"""

print("=" * 60)
print("MINI PROJECT: BLOG WITH FULL AUTHENTICATION")
print("=" * 60)

PROJECT_STRUCTURE = '''
blog_project/
├── blog_project/
│   ├── settings.py
│   └── urls.py
├── blog/
│   ├── models.py     # Post, Comment models
│   ├── forms.py      # PostForm, CommentForm
│   ├── views.py      # All blog views
│   ├── urls.py       # Blog URL patterns
│   └── templates/
│       └── blog/
│           ├── post_list.html
│           ├── post_detail.html
│           ├── post_form.html
│           ├── post_confirm_delete.html
│           └── my_posts.html
├── accounts/
│   ├── forms.py      # CustomUserCreationForm
│   ├── views.py      # Auth views
│   ├── urls.py       # Auth URLs
│   └── templates/
│       └── registration/
│           ├── login.html
│           └── register.html
└── templates/
    └── base.html
'''

print(PROJECT_STRUCTURE)

print("\n" + "=" * 60)
print("MODEL DEFINITIONS")
print("=" * 60)

MODELS_CODE = '''
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
'''

print(MODELS_CODE)

print("\n" + "=" * 60)
print("FEATURES TO IMPLEMENT")
print("=" * 60)

print("""
1. AUTHENTICATION:
   - User registration with validation
   - Login/Logout functionality
   - Protected views

2. BLOG POSTS:
   - List all published posts (public)
   - View single post with comments (public)
   - Create new post (authenticated)
   - Edit post (author only)
   - Delete post (author only)
   - View my posts (authenticated)

3. COMMENTS:
   - Add comment to post (authenticated)
   - Display comments on post detail

4. FORMS:
   - PostForm with validation
   - CommentForm with validation
   - Custom registration form

5. TEMPLATES:
   - Base template with navigation
   - Conditional display based on auth status
   - Messages for user feedback
""")

print("\n" + "=" * 60)
print("BONUS CHALLENGES")
print("=" * 60)

print("""
1. Add post categories/tags
2. Add search functionality
3. Add pagination
4. Add rich text editor for posts
5. Add image upload for posts
6. Add like/dislike functionality
7. Add user avatars
""")

print("\n" + "=" * 60)
print("GRADING CRITERIA")
print("=" * 60)

print("""
- Functionality (40 points)
  - All CRUD operations work correctly
  - Authentication works properly
  - Views are properly protected

- Code Quality (20 points)
  - Clean, readable code
  - Proper naming conventions
  - DRY principles followed

- Best Practices (20 points)
  - Form validation implemented
  - Messages used for feedback
  - Proper error handling

- Documentation (10 points)
  - README file
  - Code comments where needed

- Deployment Ready (10 points)
  - Settings configured properly
  - Static files configured
  - Debug mode considerations

Total: 100 points (70% = 70 points to pass)
""")

print("\n" + "=" * 60)
print("START CODING BELOW")
print("=" * 60)

# TODO: Implement your blog application here
# Refer to 05_user_auth_project.py for complete implementation
