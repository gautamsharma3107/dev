"""
Day 15 - API Views and Viewsets
===============================
Learn: Different ways to create API endpoints

Key Concepts:
- Function-based views with @api_view decorator
- Class-based APIView
- Generic views for common patterns
- ViewSets for maximum automation
"""

# ========== OVERVIEW OF VIEW TYPES ==========
print("=" * 60)
print("OVERVIEW OF API VIEW TYPES")
print("=" * 60)

print("""
DRF provides multiple ways to create API views:

1. @api_view decorator - Simple, function-based
2. APIView class - Full control, class-based
3. Generic Views - Common patterns made easy
4. ViewSets - Maximum automation with routers

Complexity vs Control:
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  @api_view    →   APIView    →   Generics   →  ViewSet  │
│                                                         │
│  Most Control                          Least Code       │
│  Most Code                             Most Automation  │
│                                                         │
└─────────────────────────────────────────────────────────┘
""")


# ========== FUNCTION-BASED VIEWS ==========
print("\n" + "=" * 60)
print("1. FUNCTION-BASED VIEWS (@api_view)")
print("=" * 60)

print("""
Simplest way to create API endpoints:

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


@api_view(['GET', 'POST'])
def book_list(request):
    \"\"\"
    GET: List all books
    POST: Create a new book
    \"\"\"
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    \"\"\"
    GET: Retrieve a book
    PUT: Update a book
    DELETE: Delete a book
    \"\"\"
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
]
""")


# ========== CLASS-BASED APIVIEW ==========
print("\n" + "=" * 60)
print("2. CLASS-BASED APIView")
print("=" * 60)

print("""
More structured, better for complex logic:

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookListAPIView(APIView):
    \"\"\"
    List all books or create a new book.
    \"\"\"
    
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    \"\"\"
    Retrieve, update or delete a book.
    \"\"\"
    
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None
    
    def get(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# urls.py
urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
""")


# ========== GENERIC VIEWS ==========
print("\n" + "=" * 60)
print("3. GENERIC VIEWS")
print("=" * 60)

print("""
Pre-built views for common patterns - much less code!

Available Generic Views:
┌────────────────────────┬────────────────────────────────────┐
│ Generic View           │ HTTP Methods                       │
├────────────────────────┼────────────────────────────────────┤
│ ListAPIView            │ GET (list)                         │
│ CreateAPIView          │ POST (create)                      │
│ RetrieveAPIView        │ GET (single object)                │
│ UpdateAPIView          │ PUT, PATCH                         │
│ DestroyAPIView         │ DELETE                             │
│ ListCreateAPIView      │ GET (list), POST                   │
│ RetrieveUpdateAPIView  │ GET (single), PUT, PATCH           │
│ RetrieveDestroyAPIView │ GET (single), DELETE               │
│ RetrieveUpdateDestroy  │ GET (single), PUT, PATCH, DELETE   │
└────────────────────────┴────────────────────────────────────┘

# views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookListCreate(generics.ListCreateAPIView):
    \"\"\"GET: List all books, POST: Create a book\"\"\"
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    \"\"\"GET: Single book, PUT/PATCH: Update, DELETE: Remove\"\"\"
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# That's it! All CRUD operations in just 8 lines!

# urls.py
urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
""")


# ========== CUSTOMIZING GENERIC VIEWS ==========
print("\n" + "=" * 60)
print("CUSTOMIZING GENERIC VIEWS")
print("=" * 60)

print("""
Override methods to customize behavior:

class BookListCreate(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    
    # Custom queryset
    def get_queryset(self):
        queryset = Book.objects.filter(is_available=True)
        
        # Filter by author from query params
        author = self.request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author__icontains=author)
        
        return queryset
    
    # Custom serializer based on action
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer
        return BookListSerializer
    
    # Custom create logic
    def perform_create(self, serializer):
        # Add extra data before saving
        serializer.save(created_by=self.request.user)
    
    # Custom response on list
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'count': len(response.data),
            'books': response.data
        }
        return response
""")


# ========== VIEWSETS ==========
print("\n" + "=" * 60)
print("4. VIEWSETS (Recommended for Full CRUD)")
print("=" * 60)

print("""
ViewSets combine all operations in ONE class + automatic URL routing!

# views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    \"\"\"
    A viewset that provides default CRUD actions:
    - list: GET /books/
    - create: POST /books/
    - retrieve: GET /books/{id}/
    - update: PUT /books/{id}/
    - partial_update: PATCH /books/{id}/
    - destroy: DELETE /books/{id}/
    \"\"\"
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# That's it! Complete CRUD API in 3 lines!


# Using Routers for automatic URL generation:
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# This creates all these URLs automatically:
# GET    /books/         → list all books
# POST   /books/         → create a book
# GET    /books/{id}/    → retrieve a book
# PUT    /books/{id}/    → update a book
# PATCH  /books/{id}/    → partial update
# DELETE /books/{id}/    → delete a book
""")


# ========== VIEWSET TYPES ==========
print("\n" + "=" * 60)
print("TYPES OF VIEWSETS")
print("=" * 60)

print("""
┌──────────────────────┬──────────────────────────────────────────┐
│ ViewSet Type         │ Description                              │
├──────────────────────┼──────────────────────────────────────────┤
│ ViewSet              │ Basic, no model operations built-in      │
│ GenericViewSet       │ With generic view mixins support         │
│ ModelViewSet         │ Full CRUD - list, create, retrieve,      │
│                      │ update, partial_update, destroy          │
│ ReadOnlyModelViewSet │ Only list and retrieve (read-only)       │
└──────────────────────┴──────────────────────────────────────────┘

# ReadOnlyModelViewSet (only GET operations)
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only allows: list and retrieve


# Custom ViewSet with specific actions
from rest_framework import viewsets, mixins

class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only allows: list and create
""")


# ========== CUSTOM VIEWSET ACTIONS ==========
print("\n" + "=" * 60)
print("CUSTOM VIEWSET ACTIONS")
print("=" * 60)

print("""
Add custom endpoints to your ViewSet:

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Custom action: GET /books/available/
    @action(detail=False, methods=['get'])
    def available(self, request):
        \"\"\"Get all available books.\"\"\"
        available_books = Book.objects.filter(is_available=True)
        serializer = self.get_serializer(available_books, many=True)
        return Response(serializer.data)
    
    # Custom action: POST /books/{id}/mark_unavailable/
    @action(detail=True, methods=['post'])
    def mark_unavailable(self, request, pk=None):
        \"\"\"Mark a specific book as unavailable.\"\"\"
        book = self.get_object()
        book.is_available = False
        book.save()
        return Response({'status': 'book marked unavailable'})
    
    # Custom action with different serializer
    @action(detail=True, methods=['get'], serializer_class=BookDetailSerializer)
    def full_details(self, request, pk=None):
        \"\"\"Get full details of a book.\"\"\"
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response(serializer.data)


# URLs generated:
# GET  /books/available/           → custom list action
# POST /books/{id}/mark_unavailable/  → custom detail action
# GET  /books/{id}/full_details/   → custom detail action
""")


# ========== FILTERING AND SEARCHING ==========
print("\n" + "=" * 60)
print("FILTERING AND SEARCHING")
print("=" * 60)

print("""
Add filtering capabilities to views:

# Install django-filter
# pip install django-filter

# settings.py
INSTALLED_APPS = [
    ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
}

# views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Filtering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author', 'is_available', 'published_date']
    
    # Searching
    search_fields = ['title', 'description', 'author']
    
    # Ordering
    ordering_fields = ['title', 'price', 'published_date']
    ordering = ['-created_at']  # Default ordering


# Usage:
# GET /books/?author=John           → Filter by author
# GET /books/?is_available=true     → Filter by availability
# GET /books/?search=django         → Search in title, description, author
# GET /books/?ordering=price        → Order by price (ascending)
# GET /books/?ordering=-price       → Order by price (descending)
""")


# ========== COMPLETE VIEWS EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE VIEWS EXAMPLE")
print("=" * 60)

complete_views = '''
# api/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, BookListSerializer


# ViewSet - Recommended for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for books.
    
    list: GET /api/books/
    create: POST /api/books/
    retrieve: GET /api/books/{id}/
    update: PUT /api/books/{id}/
    partial_update: PATCH /api/books/{id}/
    destroy: DELETE /api/books/{id}/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Filtering and searching
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author', 'is_available']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'price', 'created_at']
    ordering = ['-created_at']
    
    # Different serializer for list vs detail
    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer
    
    # Custom action: Get available books
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available books."""
        books = self.queryset.filter(is_available=True)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
    
    # Custom action: Mark book as unavailable
    @action(detail=True, methods=['post'])
    def mark_unavailable(self, request, pk=None):
        """Mark a book as unavailable."""
        book = self.get_object()
        book.is_available = False
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    """API endpoint for authors."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Simple function-based view example
@api_view(['GET'])
def api_overview(request):
    """Overview of available API endpoints."""
    api_urls = {
        'Books': '/api/books/',
        'Authors': '/api/authors/',
        'Available Books': '/api/books/available/',
    }
    return Response(api_urls)


# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('', include(router.urls)),
]
'''

print(complete_views)


print("\n" + "=" * 60)
print("✅ API Views and Viewsets - Complete!")
print("=" * 60)
print("""
Summary:
- @api_view for simple function-based views
- APIView for class-based views with full control
- Generic views for common patterns
- ViewSets for maximum automation
- Routers auto-generate URLs for ViewSets
- Use @action for custom endpoints
- Add filtering, searching, and ordering

Next: Let's build a complete simple API!
""")
