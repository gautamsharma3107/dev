"""
Day 12 - Django Models Basics
==============================
Learn: Creating models, model fields, field options

Key Concepts:
- Models are Python classes that represent database tables
- Each model attribute represents a database field
- Django handles table creation through migrations
"""

# ========== DJANGO MODEL BASICS ==========

"""
IMPORTANT: This file shows Django model code examples.
To run Django code, you need a Django project setup.
See the blog_project in mini_projects/ for a complete working example.

First, make sure Django is installed:
    pip install django

Create a new project:
    django-admin startproject myproject
    cd myproject
    python manage.py startapp blog
"""

# ========== BASIC MODEL STRUCTURE ==========

# Example model code (place in blog/models.py):

EXAMPLE_MODEL = '''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# ========== SIMPLE MODEL ==========
class Post(models.Model):
    """
    A basic blog post model.
    Each class attribute becomes a database column.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String representation shown in admin and shell"""
        return self.title
    
    class Meta:
        """Model metadata options"""
        ordering = ['-created_at']  # Newest first
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'


# ========== COMMON FIELD TYPES ==========
class Product(models.Model):
    """
    Example model showcasing different field types.
    """
    # String fields
    name = models.CharField(max_length=100)  # Short text
    description = models.TextField()          # Long text
    slug = models.SlugField(unique=True)      # URL-friendly string
    
    # Numeric fields
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    rating = models.FloatField(null=True, blank=True)
    
    # Boolean field
    is_available = models.BooleanField(default=True)
    
    # Date/Time fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    release_date = models.DateField(null=True, blank=True)
    
    # File fields
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    document = models.FileField(upload_to='docs/', null=True, blank=True)
    
    # Email and URL
    support_email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name


# ========== FIELD OPTIONS ==========
"""
Common field options:
- null=True       : Database allows NULL values
- blank=True      : Form validation allows empty values
- default=value   : Default value if not specified
- unique=True     : Unique constraint
- choices=list    : Limit to predefined choices
- verbose_name    : Human-readable field name
- help_text       : Help text for forms
"""

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(
        max_length=200,
        verbose_name='Article Title',
        help_text='Enter the article title (max 200 characters)'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title


# ========== MODEL WITH RELATIONSHIPS ==========
class Category(models.Model):
    """Category for blog posts"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    """Tag for blog posts"""
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """
    Blog post with relationships.
    """
    # ForeignKey: Many-to-One relationship
    # One category can have many posts
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # Delete posts when category is deleted
        related_name='posts'
    )
    
    # ForeignKey to User
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    
    # ManyToManyField: Many-to-Many relationship
    # A post can have multiple tags, a tag can be on multiple posts
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)
    
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def publish(self):
        """Custom method to publish the post"""
        self.is_published = True
        self.published_date = timezone.now()
        self.save()


# ========== ON_DELETE OPTIONS ==========
"""
on_delete options for ForeignKey:
- CASCADE      : Delete related objects when parent is deleted
- PROTECT      : Prevent deletion of parent if children exist
- SET_NULL     : Set to NULL (requires null=True)
- SET_DEFAULT  : Set to default value
- DO_NOTHING   : Do nothing (may cause integrity errors)
"""

class Comment(models.Model):
    """Comment on a blog post"""
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,  # Delete comments when post is deleted
        related_name='comments'
    )
    author_name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.author_name} on {self.post.title}'
'''

print("=" * 60)
print("DJANGO MODELS BASICS")
print("=" * 60)

print("""
Django models are Python classes that represent database tables.
Each model maps to a single database table.

KEY CONCEPTS:
1. Model Class = Database Table
2. Model Attribute = Database Column
3. Model Instance = Database Row

COMMON FIELD TYPES:
- CharField      : Short text with max_length
- TextField      : Unlimited text
- IntegerField   : Integer numbers
- FloatField     : Floating point numbers
- DecimalField   : Precise decimal numbers
- BooleanField   : True/False values
- DateField      : Date only
- DateTimeField  : Date and time
- EmailField     : Email validation
- URLField       : URL validation
- SlugField      : URL-friendly string
- ImageField     : Image upload
- FileField      : File upload

RELATIONSHIP FIELDS:
- ForeignKey           : Many-to-One relationship
- ManyToManyField      : Many-to-Many relationship
- OneToOneField        : One-to-One relationship

FIELD OPTIONS:
- null=True       : Database allows NULL
- blank=True      : Form allows empty
- default=value   : Default value
- unique=True     : Unique constraint
- choices=list    : Predefined choices
- verbose_name    : Human-readable name
""")

print("\n" + "=" * 60)
print("EXAMPLE MODEL CODE")
print("=" * 60)
print(EXAMPLE_MODEL)

print("\n" + "=" * 60)
print("✅ Django Models Basics - Complete!")
print("=" * 60)
