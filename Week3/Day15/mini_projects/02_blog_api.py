"""
MINI PROJECT 2: Blog API
========================
Build a REST API for a simple blog

Requirements:
- Post model with: title, content, author, is_published, views_count, created_at
- Comment model related to Post
- Tag model with many-to-many relationship
- Full CRUD for posts
- Nested comments in post detail
- Filter posts by author, is_published
- Search posts by title and content
- Custom action: increment views
"""

print("=" * 60)
print("MINI PROJECT: Blog API")
print("=" * 60)

# ========== MODELS ==========
print("""
MODELS (models.py)
------------------

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='posts'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    is_published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"
""")


# ========== SERIALIZERS ==========
print("""
SERIALIZERS (serializers.py)
----------------------------

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag, Post, Comment


class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'posts_count']
    
    def get_posts_count(self, obj):
        return obj.posts.filter(is_published=True).count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'author_name', 'author_email',
            'content', 'is_approved', 'created_at'
        ]
        read_only_fields = ['id', 'is_approved', 'created_at']
        extra_kwargs = {
            'post': {'write_only': True}
        }


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostListSerializer(serializers.ModelSerializer):
    \"\"\"Simplified serializer for list view.\"\"\"
    author = serializers.CharField(source='author.username')
    tags = TagSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'author', 'tags',
            'is_published', 'views_count', 'comments_count',
            'created_at'
        ]
    
    def get_comments_count(self, obj):
        return obj.comments.filter(is_approved=True).count()


class PostDetailSerializer(serializers.ModelSerializer):
    \"\"\"Full serializer with nested comments.\"\"\"
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    comments = serializers.SerializerMethodField()
    reading_time = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 
            'author', 'author_id',
            'tags', 'tag_ids',
            'is_published', 'views_count',
            'comments', 'reading_time',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'views_count', 'created_at', 'updated_at']
    
    def get_comments(self, obj):
        approved_comments = obj.comments.filter(is_approved=True)
        return CommentSerializer(approved_comments, many=True).data
    
    def get_reading_time(self, obj):
        \"\"\"Estimate reading time (200 words per minute).\"\"\"
        word_count = len(obj.content.split())
        minutes = max(1, word_count // 200)
        return f"{minutes} min read"
    
    def create(self, validated_data):
        tag_ids = validated_data.pop('tag_ids', [])
        post = Post.objects.create(**validated_data)
        post.tags.set(tag_ids)
        return post
    
    def update(self, instance, validated_data):
        tag_ids = validated_data.pop('tag_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if tag_ids is not None:
            instance.tags.set(tag_ids)
        return instance
""")


# ========== VIEWS ==========
print("""
VIEWS (views.py)
----------------

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Tag, Post, Comment
from .serializers import (
    TagSerializer, PostListSerializer, PostDetailSerializer,
    CommentSerializer
)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'views_count', 'title']
    ordering = ['-created_at']
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer
    
    def get_queryset(self):
        queryset = Post.objects.all()
        
        # Only show published posts to non-staff
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_published=True)
        
        # Filter by author
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author__username=author)
        
        # Filter by tag
        tag = self.request.query_params.get('tag')
        if tag:
            queryset = queryset.filter(tags__slug=tag)
        
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        \"\"\"Increment view count on retrieve.\"\"\"
        instance = self.get_object()
        instance.views_count += 1
        instance.save(update_fields=['views_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def published(self, request):
        \"\"\"Get all published posts.\"\"\"
        posts = self.queryset.filter(is_published=True)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def popular(self, request):
        \"\"\"Get top 10 most viewed posts.\"\"\"
        posts = self.queryset.filter(is_published=True).order_by('-views_count')[:10]
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def publish(self, request, slug=None):
        \"\"\"Publish a post.\"\"\"
        post = self.get_object()
        post.is_published = True
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def unpublish(self, request, slug=None):
        \"\"\"Unpublish a post.\"\"\"
        post = self.get_object()
        post.is_published = False
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get', 'post'])
    def comments(self, request, slug=None):
        \"\"\"Get or add comments for a post.\"\"\"
        post = self.get_object()
        
        if request.method == 'GET':
            comments = post.comments.filter(is_approved=True)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            data = request.data.copy()
            data['post'] = post.id
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        
        # Filter by post
        post_slug = self.request.query_params.get('post')
        if post_slug:
            queryset = queryset.filter(post__slug=post_slug)
        
        # Only show approved comments to non-staff
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_approved=True)
        
        return queryset
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        \"\"\"Approve a comment.\"\"\"
        comment = self.get_object()
        comment.is_approved = True
        comment.save()
        serializer = self.get_serializer(comment)
        return Response(serializer.data)
""")


# ========== URLS ==========
print("""
URLS (urls.py)
--------------

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Endpoints:
# Tags:
#   GET    /api/tags/
#   POST   /api/tags/
#   GET    /api/tags/{slug}/
#   PUT    /api/tags/{slug}/
#   DELETE /api/tags/{slug}/
#
# Posts:
#   GET    /api/posts/
#   POST   /api/posts/
#   GET    /api/posts/{slug}/
#   PUT    /api/posts/{slug}/
#   DELETE /api/posts/{slug}/
#   GET    /api/posts/published/
#   GET    /api/posts/popular/
#   POST   /api/posts/{slug}/publish/
#   POST   /api/posts/{slug}/unpublish/
#   GET    /api/posts/{slug}/comments/
#   POST   /api/posts/{slug}/comments/
#
# Comments:
#   GET    /api/comments/
#   POST   /api/comments/
#   GET    /api/comments/{id}/
#   DELETE /api/comments/{id}/
#   POST   /api/comments/{id}/approve/
""")


print("\n" + "=" * 60)
print("✅ Blog API Mini Project Complete!")
print("=" * 60)
print("""
What you've learned:
- Multiple related models
- Many-to-many relationships
- Nested serializers
- Custom lookup fields (slug)
- View count increment
- Comment moderation
- Filtering by relationships

Challenge: Add a 'like' feature for posts!
""")
