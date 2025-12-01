# Day 12 Quick Reference Cheat Sheet

## Django Models

### Basic Model Structure
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
```

### Common Field Types
```python
# String fields
CharField(max_length=100)     # Short text
TextField()                    # Long text
SlugField(unique=True)        # URL-friendly

# Numeric fields
IntegerField()
FloatField()
DecimalField(max_digits=10, decimal_places=2)
PositiveIntegerField()

# Boolean
BooleanField(default=False)

# Date/Time
DateField()
DateTimeField(auto_now_add=True)  # Set on create
DateTimeField(auto_now=True)       # Set on every save

# File fields
ImageField(upload_to='images/')
FileField(upload_to='files/')

# Other
EmailField()
URLField()
```

### Field Options
```python
null=True       # Database allows NULL
blank=True      # Form allows empty
default=value   # Default value
unique=True     # Unique constraint
choices=LIST    # Predefined choices
verbose_name    # Human-readable name
```

### Relationships
```python
# ForeignKey (Many-to-One)
author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='posts'
)

# ManyToManyField
tags = models.ManyToManyField(Tag, blank=True)

# OneToOneField
profile = models.OneToOneField(User, on_delete=models.CASCADE)
```

### on_delete Options
```python
CASCADE     # Delete related objects
PROTECT     # Prevent deletion
SET_NULL    # Set to NULL (requires null=True)
SET_DEFAULT # Set to default value
DO_NOTHING  # Do nothing
```

## Migrations

### Essential Commands
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Show SQL for migration
python manage.py sqlmigrate app_name 0001

# Rollback migration
python manage.py migrate app_name 0001
```

## ORM Queries

### CRUD Operations
```python
# CREATE
Post.objects.create(title='New', content='...')
post = Post(title='New')
post.save()

# READ
Post.objects.all()
Post.objects.get(pk=1)
Post.objects.filter(status='published')
Post.objects.exclude(status='draft')

# UPDATE
post = Post.objects.get(pk=1)
post.title = 'Updated'
post.save()
Post.objects.filter(pk=1).update(title='Updated')

# DELETE
post.delete()
Post.objects.filter(status='draft').delete()
```

### Field Lookups
```python
__exact        # Exact match
__iexact       # Case-insensitive exact
__contains     # Contains substring
__icontains    # Case-insensitive contains
__startswith   # Starts with
__endswith     # Ends with
__in           # In list
__gt, __gte    # Greater than (or equal)
__lt, __lte    # Less than (or equal)
__range        # Range
__isnull       # Is null
__year, __month, __day  # Date parts
```

### Query Examples
```python
# Filter by field
Post.objects.filter(title__contains='python')
Post.objects.filter(views__gt=100)
Post.objects.filter(created_at__year=2024)

# Multiple conditions (AND)
Post.objects.filter(status='published', views__gt=100)

# OR conditions
from django.db.models import Q
Post.objects.filter(Q(status='published') | Q(author=user))

# Ordering
Post.objects.order_by('-created_at')
Post.objects.order_by('?')  # Random

# Limiting
Post.objects.all()[:10]
Post.objects.first()
Post.objects.last()

# Values
Post.objects.values('title', 'views')
Post.objects.values_list('title', flat=True)

# Distinct
Post.objects.values('category').distinct()
```

### Aggregation
```python
from django.db.models import Count, Sum, Avg, Max, Min

Post.objects.count()
Post.objects.aggregate(avg_views=Avg('views'))
Post.objects.aggregate(total=Sum('views'))

# Per-object annotation
Post.objects.annotate(comment_count=Count('comments'))
```

### Related Objects
```python
# Forward relation
post.author
post.category.name

# Reverse relation
user.blog_posts.all()
category.posts.all()

# Optimization
Post.objects.select_related('author', 'category')
Post.objects.prefetch_related('tags', 'comments')
```

## Django Admin

### Basic Registration
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)

# Or with decorator
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
```

### Common ModelAdmin Options
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # List view
    list_display = ['title', 'author', 'status']
    list_filter = ['status', 'created_at']
    list_editable = ['status']
    search_fields = ['title', 'content']
    ordering = ['-created_at']
    list_per_page = 25
    date_hierarchy = 'created_at'
    
    # Edit view
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    filter_horizontal = ['tags']
    readonly_fields = ['views', 'created_at']
    
    fieldsets = (
        ('Basic', {'fields': ('title', 'slug')}),
        ('Content', {'fields': ('content',)}),
    )
    
    # Actions
    actions = ['make_published']
    
    @admin.action(description='Publish selected')
    def make_published(self, request, queryset):
        queryset.update(status='published')
```

### Inline Admin
```python
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
```

### Admin Commands
```bash
# Create superuser
python manage.py createsuperuser

# Change password
python manage.py changepassword username

# Shell for testing
python manage.py shell
```

## Quick Setup Checklist

```bash
# 1. Create project
django-admin startproject myproject
cd myproject

# 2. Create app
python manage.py startapp myapp

# 3. Add to INSTALLED_APPS in settings.py
# 4. Define models in models.py

# 5. Make migrations
python manage.py makemigrations

# 6. Apply migrations
python manage.py migrate

# 7. Register in admin.py

# 8. Create superuser
python manage.py createsuperuser

# 9. Run server
python manage.py runserver

# 10. Access admin: http://127.0.0.1:8000/admin/
```

---
**Keep this handy for quick reference!** 🚀
