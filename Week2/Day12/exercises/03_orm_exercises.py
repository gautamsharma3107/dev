"""
EXERCISES: Django ORM Queries
==============================
Complete all exercises below to practice ORM queries.

Note: These exercises assume you have a blog app with the following models:
- Post (title, content, author, category, status, views, created_at)
- Category (name, slug)
- Tag (name, slug) - ManyToMany with Post
- Comment (post, author_name, content, is_approved, created_at)
"""

# Exercise 1: Basic CRUD Operations
# TODO: Write the ORM queries for each operation

print("Exercise 1: Basic CRUD Operations")
print("-" * 40)

print("""
Write the Django ORM code for each operation:

1. Create a new category with name='News' and slug='news':
   Your code: _______________________

2. Get a single post with id=5:
   Your code: _______________________

3. Get all posts (returns QuerySet):
   Your code: _______________________

4. Update the title of post with id=5 to 'Updated Title':
   Your code: _______________________

5. Delete all comments that are not approved:
   Your code: _______________________
""")


# Exercise 2: Filtering Queries
# TODO: Write filter queries

print("\n\nExercise 2: Filtering Queries")
print("-" * 40)

print("""
Write the ORM queries:

1. Get all published posts:
   Your code: _______________________

2. Get posts with more than 100 views:
   Your code: _______________________

3. Get posts containing 'python' in the title (case-insensitive):
   Your code: _______________________

4. Get posts created in 2024:
   Your code: _______________________

5. Get posts in either 'Technology' or 'Science' categories:
   Your code: _______________________

6. Get posts that have no category assigned:
   Your code: _______________________
""")


# Exercise 3: Complex Queries with Q Objects
# TODO: Write queries using Q objects

print("\n\nExercise 3: Complex Queries with Q Objects")
print("-" * 40)

print("""
Write the ORM queries using Q objects:

1. Get posts that are either published OR have more than 50 views:
   Your code: _______________________

2. Get posts that contain 'django' in title OR content:
   Your code: _______________________

3. Get posts that are NOT drafts:
   Your code: _______________________

4. Get posts that are published AND (have > 100 views OR have > 5 comments):
   Your code: _______________________
""")


# Exercise 4: Ordering and Limiting
# TODO: Write ordering queries

print("\n\nExercise 4: Ordering and Limiting")
print("-" * 40)

print("""
Write the ORM queries:

1. Get all posts ordered by creation date (newest first):
   Your code: _______________________

2. Get the 10 most viewed posts:
   Your code: _______________________

3. Get the first published post:
   Your code: _______________________

4. Get posts 11-20 (pagination):
   Your code: _______________________
""")


# Exercise 5: Aggregation and Annotation
# TODO: Write aggregation queries

print("\n\nExercise 5: Aggregation and Annotation")
print("-" * 40)

print("""
Write the ORM queries:

1. Count total number of posts:
   Your code: _______________________

2. Get average views across all posts:
   Your code: _______________________

3. Get each post with its comment count:
   Your code: _______________________

4. Get total views per category:
   Your code: _______________________
""")


# Exercise 6: Related Object Queries
# TODO: Write queries involving relationships

print("\n\nExercise 6: Related Object Queries")
print("-" * 40)

print("""
Write the ORM queries:

1. Get all posts by user with username 'admin':
   Your code: _______________________

2. Get all posts in 'Technology' category:
   Your code: _______________________

3. Get all posts with tag 'python':
   Your code: _______________________

4. Get all approved comments for a specific post:
   Your code: _______________________

5. Get all categories that have at least one published post:
   Your code: _______________________
""")


# Exercise 7: Optimization
# TODO: Optimize the given queries

print("\n\nExercise 7: Query Optimization")
print("-" * 40)

print("""
Optimize these queries to reduce database hits:

1. Original (causes N+1 problem):
   posts = Post.objects.all()
   for post in posts:
       print(post.author.username)
   
   Optimized: _______________________

2. Original (multiple queries for ManyToMany):
   posts = Post.objects.all()
   for post in posts:
       print([t.name for t in post.tags.all()])
   
   Optimized: _______________________

3. Get posts with their authors and categories efficiently:
   Your code: _______________________
""")


# ========== ANSWERS ==========

print("\n\n" + "=" * 60)
print("ANSWERS (Check after attempting)")
print("=" * 60)

ANSWERS = """
Exercise 1:
1. Category.objects.create(name='News', slug='news')
2. Post.objects.get(pk=5)
3. Post.objects.all()
4. post = Post.objects.get(pk=5); post.title = 'Updated Title'; post.save()
   OR: Post.objects.filter(pk=5).update(title='Updated Title')
5. Comment.objects.filter(is_approved=False).delete()

Exercise 2:
1. Post.objects.filter(status='published')
2. Post.objects.filter(views__gt=100)
3. Post.objects.filter(title__icontains='python')
4. Post.objects.filter(created_at__year=2024)
5. Post.objects.filter(category__name__in=['Technology', 'Science'])
6. Post.objects.filter(category__isnull=True)

Exercise 3:
1. Post.objects.filter(Q(status='published') | Q(views__gt=50))
2. Post.objects.filter(Q(title__icontains='django') | Q(content__icontains='django'))
3. Post.objects.filter(~Q(status='draft'))
4. Post.objects.filter(Q(status='published') & (Q(views__gt=100) | Q(comment_count__gt=5)))

Exercise 4:
1. Post.objects.order_by('-created_at')
2. Post.objects.order_by('-views')[:10]
3. Post.objects.filter(status='published').first()
4. Post.objects.all()[10:20]

Exercise 5:
1. Post.objects.count()
2. Post.objects.aggregate(avg_views=Avg('views'))
3. Post.objects.annotate(comment_count=Count('comments'))
4. Category.objects.annotate(total_views=Sum('posts__views'))

Exercise 6:
1. Post.objects.filter(author__username='admin')
2. Post.objects.filter(category__name='Technology')
   OR: Category.objects.get(name='Technology').posts.all()
3. Post.objects.filter(tags__name='python')
4. post.comments.filter(is_approved=True)
5. Category.objects.filter(posts__status='published').distinct()

Exercise 7:
1. Post.objects.select_related('author')
2. Post.objects.prefetch_related('tags')
3. Post.objects.select_related('author', 'category').prefetch_related('tags')
"""

print(ANSWERS)
