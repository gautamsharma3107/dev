"""
Day 12 - Django ORM Queries
============================
Learn: QuerySet methods - filter, get, all, create, update, delete

Key Concepts:
- ORM (Object-Relational Mapping) lets you interact with database using Python
- QuerySets are lazy - evaluated only when needed
- Chaining methods to build complex queries
"""

# ========== DJANGO ORM QUERIES ==========

print("=" * 60)
print("DJANGO ORM QUERIES")
print("=" * 60)

print("""
WHAT IS DJANGO ORM?
==================
Django's ORM (Object-Relational Mapping) allows you to interact with
your database using Python code instead of writing raw SQL.

- Models represent database tables
- QuerySets represent collections of database queries
- QuerySets are lazy (not evaluated until needed)

To practice these queries, use Django's shell:
    python manage.py shell
""")

# ========== BASIC CRUD OPERATIONS ==========

print("\n" + "=" * 60)
print("BASIC CRUD OPERATIONS")
print("=" * 60)

CRUD_EXAMPLES = '''
# ========== CREATE ==========
# Import your models
from blog.models import Post, Category, Tag
from django.contrib.auth.models import User

# Get or create a user
user = User.objects.get(username='admin')

# Create method 1: create()
post = Post.objects.create(
    title='My First Post',
    content='This is the content of my first post.',
    author=user
)

# Create method 2: instantiate and save()
post = Post(
    title='My Second Post',
    content='This is the content of my second post.',
    author=user
)
post.save()

# Create method 3: get_or_create() - won't create duplicate
post, created = Post.objects.get_or_create(
    title='Unique Post',
    defaults={
        'content': 'This post will only be created once.',
        'author': user
    }
)
# created is True if new object was created, False if it existed


# ========== READ (Retrieve) ==========

# Get all objects
all_posts = Post.objects.all()

# Get single object by primary key
post = Post.objects.get(pk=1)  # or .get(id=1)

# Get single object by field
post = Post.objects.get(title='My First Post')

# NOTE: .get() raises exceptions!
# - DoesNotExist: if no object found
# - MultipleObjectsReturned: if multiple objects found

# Safe way to get single object
try:
    post = Post.objects.get(pk=1)
except Post.DoesNotExist:
    post = None

# Or use .first() (returns None if not found)
post = Post.objects.filter(pk=1).first()


# ========== UPDATE ==========

# Update single object
post = Post.objects.get(pk=1)
post.title = 'Updated Title'
post.save()

# Update multiple objects (bulk update)
Post.objects.filter(is_published=False).update(is_published=True)

# Update with F() for database-level operations
from django.db.models import F
Post.objects.filter(pk=1).update(views=F('views') + 1)


# ========== DELETE ==========

# Delete single object
post = Post.objects.get(pk=1)
post.delete()

# Delete multiple objects
Post.objects.filter(is_published=False).delete()

# Delete all objects (DANGEROUS!)
# Post.objects.all().delete()
'''

print(CRUD_EXAMPLES)

# ========== QUERYSET METHODS ==========

print("\n" + "=" * 60)
print("QUERYSET METHODS")
print("=" * 60)

QUERYSET_METHODS = '''
# ========== FILTERING ==========

# filter() - returns QuerySet of matching objects
published_posts = Post.objects.filter(is_published=True)

# Multiple conditions (AND)
recent_published = Post.objects.filter(
    is_published=True,
    created_at__year=2024
)

# Chaining filters (same as above)
recent_published = Post.objects.filter(is_published=True).filter(created_at__year=2024)

# exclude() - returns QuerySet excluding matches
not_draft = Post.objects.exclude(status='draft')


# ========== FIELD LOOKUPS ==========

# Exact match (default)
Post.objects.filter(title='Hello')
Post.objects.filter(title__exact='Hello')

# Case-insensitive exact
Post.objects.filter(title__iexact='hello')

# Contains
Post.objects.filter(title__contains='python')
Post.objects.filter(title__icontains='python')  # Case-insensitive

# Starts with / Ends with
Post.objects.filter(title__startswith='How')
Post.objects.filter(title__endswith='?')

# In list
Post.objects.filter(status__in=['published', 'featured'])

# Range
Post.objects.filter(views__range=(10, 100))

# Greater than / Less than
Post.objects.filter(views__gt=100)     # Greater than
Post.objects.filter(views__gte=100)    # Greater than or equal
Post.objects.filter(views__lt=50)      # Less than
Post.objects.filter(views__lte=50)     # Less than or equal

# Date/Time lookups
Post.objects.filter(created_at__year=2024)
Post.objects.filter(created_at__month=6)
Post.objects.filter(created_at__day=15)
Post.objects.filter(created_at__date='2024-06-15')

# Null check
Post.objects.filter(published_date__isnull=True)


# ========== ORDERING ==========

# Order by field (ascending)
Post.objects.order_by('created_at')

# Order by field (descending)
Post.objects.order_by('-created_at')

# Multiple ordering
Post.objects.order_by('-is_published', '-created_at')

# Random ordering
Post.objects.order_by('?')  # Note: Can be slow on large tables


# ========== LIMITING RESULTS ==========

# Slicing (like Python lists)
Post.objects.all()[:5]      # First 5
Post.objects.all()[5:10]    # 5 to 10
Post.objects.all()[:1]      # Single item as QuerySet

# first() and last()
Post.objects.first()
Post.objects.last()
Post.objects.filter(is_published=True).first()


# ========== DISTINCT ==========

# Remove duplicates
Category.objects.values('name').distinct()


# ========== VALUES AND VALUES_LIST ==========

# Get dictionaries instead of model instances
Post.objects.values('title', 'created_at')
# [{'title': 'Post 1', 'created_at': datetime}, ...]

# Get tuples
Post.objects.values_list('title', 'created_at')
# [('Post 1', datetime), ...]

# Get flat list (single field only)
Post.objects.values_list('title', flat=True)
# ['Post 1', 'Post 2', ...]
'''

print(QUERYSET_METHODS)

# ========== COMPLEX QUERIES ==========

print("\n" + "=" * 60)
print("COMPLEX QUERIES")
print("=" * 60)

COMPLEX_QUERIES = '''
# ========== Q OBJECTS (OR queries) ==========
from django.db.models import Q

# OR condition
Post.objects.filter(Q(title__contains='python') | Q(title__contains='django'))

# AND condition (same as multiple filter)
Post.objects.filter(Q(is_published=True) & Q(views__gt=100))

# NOT condition
Post.objects.filter(~Q(status='draft'))

# Complex combination
Post.objects.filter(
    Q(is_published=True) | Q(author__username='admin'),
    created_at__year=2024  # This is AND with the Q expression
)


# ========== F OBJECTS (Field comparisons) ==========
from django.db.models import F

# Compare two fields
Post.objects.filter(views__gt=F('comments_count'))

# Math with F objects
Post.objects.annotate(total=F('views') + F('shares'))

# Update with F (atomic operation)
Post.objects.filter(pk=1).update(views=F('views') + 1)


# ========== AGGREGATION ==========
from django.db.models import Count, Sum, Avg, Max, Min

# Single aggregate value
Post.objects.aggregate(total_views=Sum('views'))
# {'total_views': 1234}

Post.objects.aggregate(
    total=Count('id'),
    avg_views=Avg('views'),
    max_views=Max('views'),
    min_views=Min('views')
)


# ========== ANNOTATION (per-object) ==========

# Add computed field to each object
posts = Post.objects.annotate(comment_count=Count('comments'))
for post in posts:
    print(f"{post.title}: {post.comment_count} comments")

# Group by with annotation
from django.db.models.functions import TruncMonth
Post.objects.annotate(
    month=TruncMonth('created_at')
).values('month').annotate(
    count=Count('id')
).order_by('month')


# ========== RELATED OBJECTS ==========

# Forward relation (ForeignKey)
post = Post.objects.get(pk=1)
post.author  # Get the related User
post.category.name  # Get related Category

# Reverse relation (related_name)
user = User.objects.get(username='admin')
user.blog_posts.all()  # All posts by this user

category = Category.objects.get(slug='tech')
category.posts.all()  # All posts in this category

# ManyToMany
post.tags.all()  # All tags for this post
tag.posts.all()  # All posts with this tag

# Spanning relationships in queries
Post.objects.filter(author__username='admin')
Post.objects.filter(category__name='Technology')
Post.objects.filter(tags__name='python')


# ========== SELECT_RELATED & PREFETCH_RELATED ==========

# Optimize queries for ForeignKey (JOIN)
posts = Post.objects.select_related('author', 'category')
for post in posts:
    print(post.author.username)  # No additional query!

# Optimize queries for ManyToMany (separate query)
posts = Post.objects.prefetch_related('tags')
for post in posts:
    print([tag.name for tag in post.tags.all()])  # No additional query!

# Combine both
posts = Post.objects.select_related('author').prefetch_related('tags', 'comments')
'''

print(COMPLEX_QUERIES)

# ========== PRACTICAL EXAMPLES ==========

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

PRACTICAL_EXAMPLES = '''
# ========== COMMON QUERY PATTERNS ==========

# Get latest posts
latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:10]

# Search posts
def search_posts(query):
    return Post.objects.filter(
        Q(title__icontains=query) | 
        Q(content__icontains=query)
    ).distinct()

# Posts by category with count
categories_with_counts = Category.objects.annotate(
    post_count=Count('posts')
).order_by('-post_count')

# Most viewed posts
popular_posts = Post.objects.filter(
    is_published=True
).order_by('-views')[:5]

# Posts from last 7 days
from datetime import timedelta
from django.utils import timezone

last_week = timezone.now() - timedelta(days=7)
recent_posts = Post.objects.filter(created_at__gte=last_week)

# User's draft posts
def get_user_drafts(user):
    return Post.objects.filter(
        author=user,
        is_published=False
    ).order_by('-updated_at')

# Archive by month
from django.db.models.functions import TruncMonth

archive = Post.objects.filter(
    is_published=True
).annotate(
    month=TruncMonth('published_date')
).values('month').annotate(
    count=Count('id')
).order_by('-month')

# Posts with specific tag
def posts_by_tag(tag_slug):
    return Post.objects.filter(
        tags__slug=tag_slug,
        is_published=True
    )

# Related posts (same category)
def get_related_posts(post, limit=5):
    return Post.objects.filter(
        category=post.category,
        is_published=True
    ).exclude(pk=post.pk)[:limit]
'''

print(PRACTICAL_EXAMPLES)

# ========== QUERYSET EVALUATION ==========

print("\n" + "=" * 60)
print("QUERYSET EVALUATION (IMPORTANT!)")
print("=" * 60)

print("""
QuerySets are LAZY - they don't hit the database until evaluated.

QuerySet IS EVALUATED when:
- Iteration: for post in Post.objects.all()
- Slicing with step: Post.objects.all()[::2]
- len(): len(Post.objects.all())
- list(): list(Post.objects.all())
- bool(): if Post.objects.all()
- Printing/repr()

QuerySet IS NOT EVALUATED when:
- Creating: posts = Post.objects.all()
- Chaining: posts.filter(is_published=True)
- Slicing without step: posts[:10]

CACHING:
- QuerySets cache their results after evaluation
- Reusing QuerySet variable uses cached data
- Creating new QuerySet hits database again

EXAMPLE:
    # Bad (2 database queries)
    print(Post.objects.filter(is_published=True).count())
    for post in Post.objects.filter(is_published=True):
        print(post.title)
    
    # Good (1 database query)
    posts = Post.objects.filter(is_published=True)
    print(len(posts))  # Evaluates QuerySet
    for post in posts:  # Uses cached results
        print(post.title)
""")

print("\n" + "=" * 60)
print("✅ Django ORM Queries - Complete!")
print("=" * 60)
