"""
Day 16 - Filtering and Pagination in Django REST Framework
==========================================================
Learn: DjangoFilterBackend, SearchFilter, OrderingFilter, Pagination classes

Key Concepts:
- Filtering allows clients to narrow down results
- Pagination prevents sending too much data at once
- DRF provides flexible, configurable filtering and pagination
"""

# ========== SETUP FILTERING ==========
print("=" * 60)
print("FILTERING SETUP")
print("=" * 60)

print("""
Install django-filter:
----------------------
pip install django-filter

Configure in settings.py:
-------------------------
""")

filter_settings_code = '''
# settings.py

INSTALLED_APPS = [
    # ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
'''

print(filter_settings_code)

# ========== BASIC FILTERING ==========
print("\n" + "=" * 60)
print("BASIC FILTERING WITH DjangoFilterBackend")
print("=" * 60)

basic_filter_code = '''
# models.py

from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']


# views.py

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'status', 'author', 'is_featured']
    
    # Now you can filter:
    # GET /api/articles/?category=tech
    # GET /api/articles/?status=published
    # GET /api/articles/?author=1
    # GET /api/articles/?is_featured=true
    # GET /api/articles/?category=tech&status=published
'''

print(basic_filter_code)

# ========== CUSTOM FILTERSETS ==========
print("\n" + "=" * 60)
print("CUSTOM FILTERSETS")
print("=" * 60)

custom_filterset_code = '''
# filters.py

import django_filters
from .models import Article


class ArticleFilter(django_filters.FilterSet):
    """
    Custom filter set for advanced filtering options.
    """
    # Exact match (default)
    category = django_filters.CharFilter(field_name='category')
    
    # Case-insensitive contains
    title = django_filters.CharFilter(
        field_name='title', 
        lookup_expr='icontains'
    )
    
    # Date range filters
    created_after = django_filters.DateTimeFilter(
        field_name='created_at', 
        lookup_expr='gte'
    )
    created_before = django_filters.DateTimeFilter(
        field_name='created_at', 
        lookup_expr='lte'
    )
    
    # Number range filters
    min_views = django_filters.NumberFilter(
        field_name='views', 
        lookup_expr='gte'
    )
    max_views = django_filters.NumberFilter(
        field_name='views', 
        lookup_expr='lte'
    )
    
    # Multiple choice filter
    status = django_filters.MultipleChoiceFilter(
        choices=Article._meta.get_field('status').choices
    )
    
    # Boolean filter
    is_featured = django_filters.BooleanFilter(field_name='is_featured')
    
    # Related field filter
    author_username = django_filters.CharFilter(
        field_name='author__username',
        lookup_expr='icontains'
    )
    
    class Meta:
        model = Article
        fields = [
            'category', 'title', 'status', 'is_featured',
            'created_after', 'created_before',
            'min_views', 'max_views', 'author_username'
        ]


# views.py

from django_filters.rest_framework import DjangoFilterBackend
from .filters import ArticleFilter


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter
    
    # Example queries:
    # GET /api/articles/?title=django
    # GET /api/articles/?created_after=2024-01-01
    # GET /api/articles/?min_views=100&max_views=1000
    # GET /api/articles/?status=draft&status=published  (multiple values)
    # GET /api/articles/?author_username=john
'''

print(custom_filterset_code)

# ========== SEARCH FILTER ==========
print("\n" + "=" * 60)
print("SEARCH FILTER")
print("=" * 60)

search_filter_code = '''
# views.py

from rest_framework import viewsets
from rest_framework.filters import SearchFilter


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter]
    
    # Search across multiple fields
    search_fields = ['title', 'content', 'author__username', 'category']
    
    # Now you can search:
    # GET /api/articles/?search=django
    # This searches in title, content, author username, and category


# Advanced search options:

class AdvancedSearchViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter]
    
    search_fields = [
        'title',              # Exact field search
        '^title',             # Starts with search
        '=status',            # Exact match only
        '@content',           # Full-text search (PostgreSQL)
        'author__username',   # Related field search
        'author__email',      # Another related field
    ]
    
    # Search operators:
    # ^  - istartswith
    # =  - iexact
    # @  - Full-text search (requires PostgreSQL)
    # $  - regex search
'''

print(search_filter_code)

# ========== ORDERING FILTER ==========
print("\n" + "=" * 60)
print("ORDERING FILTER")
print("=" * 60)

ordering_filter_code = '''
# views.py

from rest_framework import viewsets
from rest_framework.filters import OrderingFilter


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [OrderingFilter]
    
    # Fields that can be used for ordering
    ordering_fields = ['created_at', 'updated_at', 'views', 'title']
    
    # Default ordering (if no ordering is specified)
    ordering = ['-created_at']  # Most recent first
    
    # Now you can order:
    # GET /api/articles/?ordering=created_at        (oldest first)
    # GET /api/articles/?ordering=-created_at       (newest first)
    # GET /api/articles/?ordering=views             (lowest views first)
    # GET /api/articles/?ordering=-views            (highest views first)
    # GET /api/articles/?ordering=title,-created_at (multiple fields)


# Allow all fields for ordering (use with caution):

class AllFieldsOrderingViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = '__all__'  # Allow ordering by any field
'''

print(ordering_filter_code)

# ========== COMBINING FILTER BACKENDS ==========
print("\n" + "=" * 60)
print("COMBINING ALL FILTER BACKENDS")
print("=" * 60)

combined_code = '''
# views.py

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article
from .serializers import ArticleSerializer
from .filters import ArticleFilter


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Full-featured API endpoint with filtering, search, and ordering.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    # All three filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # DjangoFilterBackend settings
    filterset_class = ArticleFilter
    
    # SearchFilter settings
    search_fields = ['title', 'content', 'author__username']
    
    # OrderingFilter settings
    ordering_fields = ['created_at', 'updated_at', 'views', 'title']
    ordering = ['-created_at']
    
    # Combined queries:
    # GET /api/articles/?category=tech&search=python&ordering=-views
    # GET /api/articles/?status=published&min_views=100&search=django
    # GET /api/articles/?author_username=john&ordering=created_at
'''

print(combined_code)

# ========== PAGINATION SETUP ==========
print("\n" + "=" * 60)
print("PAGINATION SETUP")
print("=" * 60)

pagination_settings_code = '''
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Items per page
}
'''

print(pagination_settings_code)

# ========== PAGE NUMBER PAGINATION ==========
print("\n" + "=" * 60)
print("PAGE NUMBER PAGINATION")
print("=" * 60)

page_number_code = '''
# pagination.py

from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard pagination with configurable page size.
    """
    page_size = 10
    page_size_query_param = 'page_size'  # Allow client to set page size
    max_page_size = 100  # Maximum items per page
    
    # Custom response format (optional)
    def get_paginated_response(self, data):
        return Response({
            'pagination': {
                'count': self.page.paginator.count,
                'total_pages': self.page.paginator.num_pages,
                'current_page': self.page.number,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'results': data
        })


class LargeResultsSetPagination(PageNumberPagination):
    """
    Pagination for endpoints with more data.
    """
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500


class SmallResultsSetPagination(PageNumberPagination):
    """
    Pagination for mobile or limited bandwidth.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


# views.py

from .pagination import StandardResultsSetPagination


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination
    
    # Usage:
    # GET /api/articles/                  (page 1, 10 items)
    # GET /api/articles/?page=2           (page 2)
    # GET /api/articles/?page_size=20     (20 items per page)
    # GET /api/articles/?page=3&page_size=25


# Response format:
# {
#     "count": 153,
#     "next": "http://api.example.com/articles/?page=2",
#     "previous": null,
#     "results": [...]
# }
'''

print(page_number_code)

# ========== LIMIT OFFSET PAGINATION ==========
print("\n" + "=" * 60)
print("LIMIT OFFSET PAGINATION")
print("=" * 60)

limit_offset_code = '''
# pagination.py

from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """
    Pagination using limit and offset (like SQL).
    """
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100


# views.py

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomLimitOffsetPagination
    
    # Usage:
    # GET /api/articles/                    (first 10 items)
    # GET /api/articles/?limit=20           (first 20 items)
    # GET /api/articles/?offset=10          (skip first 10)
    # GET /api/articles/?limit=20&offset=40 (items 41-60)


# Response format:
# {
#     "count": 153,
#     "next": "http://api.example.com/articles/?limit=10&offset=10",
#     "previous": null,
#     "results": [...]
# }
'''

print(limit_offset_code)

# ========== CURSOR PAGINATION ==========
print("\n" + "=" * 60)
print("CURSOR PAGINATION (Best for large datasets)")
print("=" * 60)

cursor_code = '''
# pagination.py

from rest_framework.pagination import CursorPagination


class ArticleCursorPagination(CursorPagination):
    """
    Cursor-based pagination - most efficient for large datasets.
    
    Advantages:
    - Consistent pagination even when items are added/removed
    - More efficient for large datasets
    - No duplicate items when paginating
    
    Disadvantages:
    - Can only go forward/backward (no jumping to page N)
    - Requires an ordered queryset
    """
    page_size = 10
    ordering = '-created_at'  # Must be unique or nearly unique
    cursor_query_param = 'cursor'


# views.py

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleCursorPagination
    
    # Usage:
    # GET /api/articles/                    (first page)
    # GET /api/articles/?cursor=cD0yMDI...  (next page using cursor)


# Response format:
# {
#     "next": "http://api.example.com/articles/?cursor=cD0yMDI0LTAxLTE...",
#     "previous": null,
#     "results": [...]
# }
'''

print(cursor_code)

# ========== DISABLING PAGINATION ==========
print("\n" + "=" * 60)
print("DISABLING PAGINATION FOR SPECIFIC VIEWS")
print("=" * 60)

disable_pagination_code = '''
# views.py

class SmallDatasetViewSet(viewsets.ModelViewSet):
    """
    View that returns all items without pagination.
    """
    queryset = Category.objects.all()  # Small dataset
    serializer_class = CategorySerializer
    pagination_class = None  # Disable pagination


class ConditionalPaginationViewSet(viewsets.ModelViewSet):
    """
    Pagination only when needed.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_paginate_by(self, queryset):
        """
        Return page size or None to disable pagination.
        """
        if self.request.query_params.get('all'):
            return None  # Return all results
        return 10


# Allow clients to request all results (use carefully):

class OptionalPaginationViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    @property
    def paginator(self):
        """
        Return None if 'all' query param is set.
        """
        if self.request.query_params.get('all'):
            return None
        return super().paginator
'''

print(disable_pagination_code)

# ========== FULL EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE EXAMPLE: FILTERING + PAGINATION")
print("=" * 60)

full_example_code = '''
# filters.py

import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name')
    in_stock = django_filters.BooleanFilter(field_name='stock', lookup_expr='gt', 
                                            method='filter_in_stock')
    
    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset.filter(stock=0)
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'min_price', 'max_price', 'in_stock']


# pagination.py

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ProductPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'per_page'
    max_page_size = 48
    
    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'total_count': self.page.paginator.count,
                'page': self.page.number,
                'per_page': self.get_page_size(self.request),
                'total_pages': self.page.paginator.num_pages,
            },
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'data': data
        })


# views.py

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from .pagination import ProductPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product API with filtering, search, ordering, and pagination.
    
    Filtering:
    - ?name=phone - Filter by name (case-insensitive)
    - ?min_price=100&max_price=500 - Price range
    - ?category=electronics - Filter by category
    - ?in_stock=true - Only in-stock items
    
    Search:
    - ?search=samsung - Search in name and description
    
    Ordering:
    - ?ordering=price - Sort by price (ascending)
    - ?ordering=-price - Sort by price (descending)
    - ?ordering=-created_at,price - Multiple fields
    
    Pagination:
    - ?page=2 - Page number
    - ?per_page=24 - Items per page (max 48)
    
    Combined:
    - ?category=electronics&min_price=100&search=phone&ordering=-price&page=2
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'sku']
    ordering_fields = ['price', 'name', 'created_at', 'stock']
    ordering = ['-created_at']
    pagination_class = ProductPagination
'''

print(full_example_code)

print("\n" + "=" * 60)
print("✅ Filtering and Pagination - Complete!")
print("=" * 60)

print("""
Summary:
--------
Filtering:
- DjangoFilterBackend: Field-based filtering
- SearchFilter: Text search across fields
- OrderingFilter: Sort results

Pagination Types:
- PageNumberPagination: Traditional page-based
- LimitOffsetPagination: SQL-style limit/offset
- CursorPagination: Best for large, real-time data

Best Practices:
--------------
1. Always paginate list endpoints
2. Set reasonable max page sizes
3. Use cursor pagination for large datasets
4. Combine filtering and pagination for flexibility
5. Document available filters and ordering fields

Next: Learn about API Documentation in 04_api_documentation.py
""")
