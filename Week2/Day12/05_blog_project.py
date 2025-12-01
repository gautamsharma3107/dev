"""
Day 12 - Blog Project with Django Models & ORM
===============================================
A complete mini-project demonstrating Django models and ORM.

This file provides the complete code for a blog application.
Follow the setup instructions below to get started.
"""

print("=" * 60)
print("BLOG PROJECT: Django Models & ORM")
print("=" * 60)

# ========== PROJECT SETUP ==========

SETUP_INSTRUCTIONS = """
PROJECT SETUP INSTRUCTIONS
==========================

1. Create a new Django project:
   django-admin startproject myblog
   cd myblog

2. Create the blog app:
   python manage.py startapp blog

3. Add 'blog' to INSTALLED_APPS in myblog/settings.py:
   INSTALLED_APPS = [
       ...
       'blog',
   ]

4. Create the models (copy code below to blog/models.py)

5. Create and apply migrations:
   python manage.py makemigrations
   python manage.py migrate

6. Create superuser:
   python manage.py createsuperuser

7. Register models in admin (copy code below to blog/admin.py)

8. Run server:
   python manage.py runserver

9. Access admin at: http://127.0.0.1:8000/admin/

10. Practice ORM queries:
    python manage.py shell
"""

print(SETUP_INSTRUCTIONS)

# ========== MODELS CODE ==========

print("\n" + "=" * 60)
print("MODELS CODE (blog/models.py)")
print("=" * 60)

MODELS_CODE = '''
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    """Blog post category"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_posts', kwargs={'slug': self.slug})


class Tag(models.Model):
    """Tag for blog posts"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    """Custom manager for published posts only"""
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    """Blog post model"""
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    # Basic fields
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    
    # Relationships
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts'
    )
    
    # Content
    excerpt = models.TextField(max_length=500, blank=True, 
                               help_text='Short summary for previews')
    content = models.TextField()
    featured_image = models.URLField(blank=True, 
                                     help_text='URL of featured image')
    
    # Publishing info
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    published_date = models.DateTimeField(null=True, blank=True)
    
    # Metadata
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Managers
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager
    
    class Meta:
        ordering = ['-published_date', '-created_at']
        indexes = [
            models.Index(fields=['-published_date']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    def publish(self):
        """Publish the post"""
        self.status = 'published'
        self.published_date = timezone.now()
        self.save()
    
    def unpublish(self):
        """Unpublish the post"""
        self.status = 'draft'
        self.published_date = None
        self.save()
    
    def increment_views(self):
        """Increment view count"""
        self.views += 1
        self.save(update_fields=['views'])


class Comment(models.Model):
    """Comment on a blog post"""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.author_name} on {self.post.title}'
'''

print(MODELS_CODE)

# ========== ADMIN CODE ==========

print("\n" + "=" * 60)
print("ADMIN CODE (blog/admin.py)")
print("=" * 60)

ADMIN_CODE = '''
from django.contrib import admin
from .models import Post, Category, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'post_count']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Posts'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ['created_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 
                    'views', 'published_date']
    list_filter = ['status', 'created_at', 'category', 'author']
    list_editable = ['status']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    filter_horizontal = ['tags']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    readonly_fields = ['views', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Post', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
        ('Publishing', {
            'fields': ('status', 'published_date')
        }),
        ('Stats', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [CommentInline]
    
    actions = ['make_published', 'make_draft']
    
    @admin.action(description='Publish selected posts')
    def make_published(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='published', published_date=timezone.now())
    
    @admin.action(description='Make selected posts drafts')
    def make_draft(self, request, queryset):
        queryset.update(status='draft', published_date=None)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'post', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    list_editable = ['is_active']
    search_fields = ['author_name', 'author_email', 'content']


# Customize admin site
admin.site.site_header = "Blog Administration"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Welcome to the Blog Admin Panel"
'''

print(ADMIN_CODE)

# ========== ORM PRACTICE ==========

print("\n" + "=" * 60)
print("ORM PRACTICE QUERIES (Django Shell)")
print("=" * 60)

ORM_PRACTICE = '''
# Start Django shell
# python manage.py shell

# Import models
from blog.models import Post, Category, Tag, Comment
from django.contrib.auth.models import User

# ========== CREATE DATA ==========

# Create a user (if none exists)
user, created = User.objects.get_or_create(
    username='blogger',
    defaults={'email': 'blogger@example.com'}
)
if created:
    user.set_password('testpass123')
    user.save()

# Create categories
tech = Category.objects.create(name='Technology', slug='technology')
life = Category.objects.create(name='Lifestyle', slug='lifestyle')
code = Category.objects.create(name='Coding', slug='coding')

# Create tags
python_tag = Tag.objects.create(name='Python', slug='python')
django_tag = Tag.objects.create(name='Django', slug='django')
web_tag = Tag.objects.create(name='Web Development', slug='web-dev')

# Create posts
post1 = Post.objects.create(
    title='Getting Started with Django',
    slug='getting-started-django',
    author=user,
    category=tech,
    excerpt='Learn Django basics in this comprehensive guide.',
    content='Full tutorial content here...',
    status='published'
)
post1.tags.add(python_tag, django_tag)

post2 = Post.objects.create(
    title='Python Tips and Tricks',
    slug='python-tips-tricks',
    author=user,
    category=code,
    excerpt='Useful Python tips for beginners.',
    content='Content about Python tips...',
    status='draft'
)
post2.tags.add(python_tag)

# Create comments
Comment.objects.create(
    post=post1,
    author_name='Reader1',
    author_email='reader1@example.com',
    content='Great article!'
)

# ========== READ DATA ==========

# Get all posts
Post.objects.all()

# Get published posts only (using custom manager)
Post.published.all()

# Get single post
post = Post.objects.get(slug='getting-started-django')

# Filter posts
Post.objects.filter(status='published')
Post.objects.filter(author__username='blogger')
Post.objects.filter(category__name='Technology')
Post.objects.filter(tags__name='Python')

# Search in title and content
from django.db.models import Q
Post.objects.filter(Q(title__icontains='django') | Q(content__icontains='django'))

# Get posts with comment count
from django.db.models import Count
Post.objects.annotate(num_comments=Count('comments'))

# ========== UPDATE DATA ==========

# Update single post
post = Post.objects.get(slug='python-tips-tricks')
post.status = 'published'
post.save()

# Bulk update
Post.objects.filter(status='draft').update(status='published')

# ========== DELETE DATA ==========

# Delete single post
# post = Post.objects.get(slug='old-post')
# post.delete()

# Delete multiple posts
# Post.objects.filter(views=0).delete()

# ========== RELATIONSHIPS ==========

# Get post's author
post = Post.objects.get(pk=1)
post.author.username

# Get post's category
post.category.name

# Get post's tags
post.tags.all()

# Get posts by category (reverse relation)
tech = Category.objects.get(slug='technology')
tech.posts.all()

# Get posts by tag
tag = Tag.objects.get(slug='python')
tag.posts.all()

# Get comments on a post
post.comments.all()
post.comments.filter(is_active=True)

# ========== OPTIMIZATION ==========

# Use select_related for ForeignKey
posts = Post.objects.select_related('author', 'category').all()

# Use prefetch_related for ManyToMany
posts = Post.objects.prefetch_related('tags', 'comments').all()

# Combined
posts = Post.objects.select_related('author', 'category').prefetch_related('tags', 'comments').all()
'''

print(ORM_PRACTICE)

# ========== QUICK TASKS ==========

print("\n" + "=" * 60)
print("PRACTICE TASKS")
print("=" * 60)

print("""
Complete these tasks to practice:

1. Create 3 more categories and 5 more tags
2. Create 5 new posts across different categories
3. Add multiple tags to each post
4. Create comments on different posts
5. Practice filtering:
   - Get all published posts in 'Technology' category
   - Get posts that have more than 100 views
   - Get posts created in the last 7 days
   - Get posts with 'Python' tag
6. Practice aggregation:
   - Count total posts per category
   - Get average views per post
   - Find the post with most comments
7. Practice relationships:
   - Get all comments by a specific author name
   - Get all posts that have no comments
   - Get all categories that have at least 3 posts
""")

print("\n" + "=" * 60)
print("✅ Blog Project Setup - Complete!")
print("=" * 60)
