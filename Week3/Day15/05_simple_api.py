"""
Day 15 - Building a Complete Simple API
========================================
Learn: Putting it all together - a complete working API

Key Concepts:
- Full project structure
- Models, Serializers, Views, URLs
- Testing the API
- Using Browsable API
"""

# ========== PROJECT OVERVIEW ==========
print("=" * 60)
print("BUILDING A COMPLETE BOOK API")
print("=" * 60)

print("""
We'll build a complete Book Store API with:
- CRUD operations for books
- Author management
- Filtering and searching
- Custom actions

Project Structure:
bookstore_api/
├── bookstore_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Data models
│   ├── serializers.py    # Data conversion
│   ├── views.py          # API logic
│   ├── urls.py           # API routes
│   └── tests.py          # API tests
├── manage.py
└── requirements.txt
""")


# ========== STEP 1: MODELS ==========
print("\n" + "=" * 60)
print("STEP 1: MODELS (api/models.py)")
print("=" * 60)

models_code = '''
# api/models.py

from django.db import models


class Author(models.Model):
    """Author model for books."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Book(models.Model):
    """Book model for the bookstore."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name='books'
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
'''

print(models_code)


# ========== STEP 2: SERIALIZERS ==========
print("\n" + "=" * 60)
print("STEP 2: SERIALIZERS (api/serializers.py)")
print("=" * 60)

serializers_code = '''
# api/serializers.py

from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model."""
    books_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio', 'books_count', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def get_books_count(self, obj):
        return obj.books.count()


class BookListSerializer(serializers.ModelSerializer):
    """Simplified serializer for book list view."""
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'price', 'is_available']


class BookSerializer(serializers.ModelSerializer):
    """Full serializer for book detail/create/update."""
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    discounted_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_id', 'description',
            'price', 'discounted_price', 'published_date', 
            'isbn', 'pages', 'is_available', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_discounted_price(self, obj):
        """Calculate 10% discount."""
        return round(float(obj.price) * 0.9, 2)
    
    def validate_isbn(self, value):
        """Validate ISBN is 13 digits."""
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be exactly 13 characters")
        if not value.isdigit():
            raise serializers.ValidationError("ISBN must contain only digits")
        return value
    
    def validate_price(self, value):
        """Validate price is positive."""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value
    
    def validate_pages(self, value):
        """Validate pages is reasonable."""
        if value < 0:
            raise serializers.ValidationError("Pages cannot be negative")
        if value > 10000:
            raise serializers.ValidationError("Pages seems too high")
        return value
'''

print(serializers_code)


# ========== STEP 3: VIEWS ==========
print("\n" + "=" * 60)
print("STEP 3: VIEWS (api/views.py)")
print("=" * 60)

views_code = '''
# api/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Author, Book
from .serializers import (
    AuthorSerializer, 
    BookSerializer, 
    BookListSerializer
)


@api_view(['GET'])
def api_root(request):
    """API Overview - list all endpoints."""
    return Response({
        'message': 'Welcome to Bookstore API',
        'endpoints': {
            'authors': '/api/authors/',
            'books': '/api/books/',
            'available_books': '/api/books/available/',
        }
    })


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing authors.
    
    list: GET /api/authors/
    create: POST /api/authors/
    retrieve: GET /api/authors/{id}/
    update: PUT /api/authors/{id}/
    partial_update: PATCH /api/authors/{id}/
    destroy: DELETE /api/authors/{id}/
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing books.
    
    list: GET /api/books/
    create: POST /api/books/
    retrieve: GET /api/books/{id}/
    update: PUT /api/books/{id}/
    partial_update: PATCH /api/books/{id}/
    destroy: DELETE /api/books/{id}/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'author__name']
    ordering_fields = ['title', 'price', 'published_date', 'created_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Use different serializer for list vs detail."""
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer
    
    def get_queryset(self):
        """Allow filtering by query parameters."""
        queryset = Book.objects.all()
        
        # Filter by availability
        is_available = self.request.query_params.get('is_available', None)
        if is_available is not None:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')
        
        # Filter by author
        author_id = self.request.query_params.get('author', None)
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available books."""
        books = self.queryset.filter(is_available=True)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def unavailable(self, request):
        """Get all unavailable books."""
        books = self.queryset.filter(is_available=False)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def toggle_availability(self, request, pk=None):
        """Toggle book availability status."""
        book = self.get_object()
        book.is_available = not book.is_available
        book.save()
        serializer = self.get_serializer(book)
        return Response({
            'message': f"Book is now {'available' if book.is_available else 'unavailable'}",
            'book': serializer.data
        })
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get book statistics."""
        total_books = self.queryset.count()
        available_books = self.queryset.filter(is_available=True).count()
        
        from django.db.models import Avg, Min, Max
        price_stats = self.queryset.aggregate(
            avg_price=Avg('price'),
            min_price=Min('price'),
            max_price=Max('price')
        )
        
        return Response({
            'total_books': total_books,
            'available_books': available_books,
            'unavailable_books': total_books - available_books,
            'price_statistics': {
                'average': round(float(price_stats['avg_price'] or 0), 2),
                'minimum': float(price_stats['min_price'] or 0),
                'maximum': float(price_stats['max_price'] or 0),
            }
        })
'''

print(views_code)


# ========== STEP 4: URLS ==========
print("\n" + "=" * 60)
print("STEP 4: URLS (api/urls.py)")
print("=" * 60)

urls_code = '''
# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create router and register viewsets
router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('', include(router.urls)),
]


# bookstore_api/urls.py (main project urls)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),  # For browsable API login
]
'''

print(urls_code)


# ========== STEP 5: ADMIN ==========
print("\n" + "=" * 60)
print("STEP 5: ADMIN (api/admin.py)")
print("=" * 60)

admin_code = '''
# api/admin.py

from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']
    ordering = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'is_available', 'created_at']
    list_filter = ['is_available', 'author', 'published_date']
    search_fields = ['title', 'isbn', 'description']
    ordering = ['-created_at']
    raw_id_fields = ['author']
'''

print(admin_code)


# ========== STEP 6: TESTING THE API ==========
print("\n" + "=" * 60)
print("STEP 6: TESTING THE API")
print("=" * 60)

print("""
Using curl to test the API:

# 1. Get all books
curl http://127.0.0.1:8000/api/books/

# 2. Get a single book
curl http://127.0.0.1:8000/api/books/1/

# 3. Create a new author
curl -X POST http://127.0.0.1:8000/api/authors/ \\
  -H "Content-Type: application/json" \\
  -d '{"name": "John Doe", "email": "john@example.com", "bio": "A great author"}'

# 4. Create a new book
curl -X POST http://127.0.0.1:8000/api/books/ \\
  -H "Content-Type: application/json" \\
  -d '{
    "title": "Django for Beginners",
    "author_id": 1,
    "description": "Learn Django from scratch",
    "price": "29.99",
    "published_date": "2024-01-15",
    "isbn": "1234567890123",
    "pages": 350
  }'

# 5. Update a book
curl -X PUT http://127.0.0.1:8000/api/books/1/ \\
  -H "Content-Type: application/json" \\
  -d '{
    "title": "Django for Beginners - Updated",
    "author_id": 1,
    "description": "Learn Django from scratch - 2nd Edition",
    "price": "34.99",
    "published_date": "2024-06-01",
    "isbn": "1234567890123",
    "pages": 400
  }'

# 6. Partial update (PATCH)
curl -X PATCH http://127.0.0.1:8000/api/books/1/ \\
  -H "Content-Type: application/json" \\
  -d '{"price": "39.99"}'

# 7. Delete a book
curl -X DELETE http://127.0.0.1:8000/api/books/1/

# 8. Search books
curl "http://127.0.0.1:8000/api/books/?search=django"

# 9. Filter by availability
curl "http://127.0.0.1:8000/api/books/?is_available=true"

# 10. Order by price
curl "http://127.0.0.1:8000/api/books/?ordering=price"

# 11. Get available books
curl http://127.0.0.1:8000/api/books/available/

# 12. Get statistics
curl http://127.0.0.1:8000/api/books/statistics/

# 13. Toggle availability
curl -X POST http://127.0.0.1:8000/api/books/1/toggle_availability/
""")


# ========== STEP 7: BROWSABLE API ==========
print("\n" + "=" * 60)
print("STEP 7: USING THE BROWSABLE API")
print("=" * 60)

print("""
DRF provides a beautiful web interface!

1. Start the server:
   $ python manage.py runserver

2. Open browser and go to:
   http://127.0.0.1:8000/api/

3. You'll see:
   - List of all endpoints
   - Forms to create/update data
   - Response data in nice format
   - Authentication controls

Features:
✅ Navigate between endpoints
✅ Test GET, POST, PUT, PATCH, DELETE
✅ See response data formatted
✅ Use forms for data entry
✅ Login/logout for authentication
✅ See raw JSON or HTML view
""")


# ========== PYTHON TEST SCRIPT ==========
print("\n" + "=" * 60)
print("PYTHON TEST SCRIPT")
print("=" * 60)

test_script = '''
# test_api.py
# Run this script to test your API

import requests

BASE_URL = "http://127.0.0.1:8000/api"

def test_api():
    print("Testing Bookstore API")
    print("=" * 50)
    
    # 1. Test API root
    print("\\n1. Testing API root...")
    response = requests.get(f"{BASE_URL}/")
    print(f"   Status: {response.status_code}")
    print(f"   Data: {response.json()}")
    
    # 2. Create an author
    print("\\n2. Creating an author...")
    author_data = {
        "name": "Test Author",
        "email": "test@example.com",
        "bio": "A test author"
    }
    response = requests.post(f"{BASE_URL}/authors/", json=author_data)
    print(f"   Status: {response.status_code}")
    author = response.json()
    print(f"   Created: {author}")
    author_id = author.get('id')
    
    # 3. Create a book
    print("\\n3. Creating a book...")
    book_data = {
        "title": "Test Book",
        "author_id": author_id,
        "description": "A test book description",
        "price": "19.99",
        "published_date": "2024-01-01",
        "isbn": "1234567890123",
        "pages": 200
    }
    response = requests.post(f"{BASE_URL}/books/", json=book_data)
    print(f"   Status: {response.status_code}")
    book = response.json()
    print(f"   Created: {book.get('title')}")
    book_id = book.get('id')
    
    # 4. Get all books
    print("\\n4. Getting all books...")
    response = requests.get(f"{BASE_URL}/books/")
    print(f"   Status: {response.status_code}")
    print(f"   Books count: {len(response.json())}")
    
    # 5. Get single book
    print(f"\\n5. Getting book {book_id}...")
    response = requests.get(f"{BASE_URL}/books/{book_id}/")
    print(f"   Status: {response.status_code}")
    print(f"   Title: {response.json().get('title')}")
    
    # 6. Update book
    print(f"\\n6. Updating book {book_id}...")
    update_data = {"price": "24.99"}
    response = requests.patch(f"{BASE_URL}/books/{book_id}/", json=update_data)
    print(f"   Status: {response.status_code}")
    print(f"   New price: {response.json().get('price')}")
    
    # 7. Get statistics
    print("\\n7. Getting statistics...")
    response = requests.get(f"{BASE_URL}/books/statistics/")
    print(f"   Status: {response.status_code}")
    print(f"   Stats: {response.json()}")
    
    # 8. Toggle availability
    print(f"\\n8. Toggling availability for book {book_id}...")
    response = requests.post(f"{BASE_URL}/books/{book_id}/toggle_availability/")
    print(f"   Status: {response.status_code}")
    print(f"   Message: {response.json().get('message')}")
    
    # 9. Delete book
    print(f"\\n9. Deleting book {book_id}...")
    response = requests.delete(f"{BASE_URL}/books/{book_id}/")
    print(f"   Status: {response.status_code}")
    
    # 10. Delete author
    print(f"\\n10. Deleting author {author_id}...")
    response = requests.delete(f"{BASE_URL}/authors/{author_id}/")
    print(f"   Status: {response.status_code}")
    
    print("\\n" + "=" * 50)
    print("API Testing Complete!")


if __name__ == "__main__":
    test_api()
'''

print(test_script)


# ========== SETUP COMMANDS ==========
print("\n" + "=" * 60)
print("SETUP COMMANDS")
print("=" * 60)

print("""
# Complete setup from scratch:

# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# 2. Install packages
pip install django djangorestframework

# 3. Create project
django-admin startproject bookstore_api
cd bookstore_api

# 4. Create app
python manage.py startapp api

# 5. Copy the code from above to respective files

# 6. Add to settings.py INSTALLED_APPS:
#    'rest_framework',
#    'api',

# 7. Run migrations
python manage.py makemigrations
python manage.py migrate

# 8. Create superuser
python manage.py createsuperuser

# 9. Run server
python manage.py runserver

# 10. Open browser: http://127.0.0.1:8000/api/
""")


print("\n" + "=" * 60)
print("✅ Complete Simple API - Built!")
print("=" * 60)
print("""
Congratulations! You've built a complete REST API with:

✅ Two models: Author and Book
✅ Serializers with validation
✅ ViewSets with full CRUD
✅ Custom actions (available, statistics, toggle)
✅ Filtering and searching
✅ Automatic URL routing
✅ Browsable API interface

API Endpoints:
- GET    /api/                     → API overview
- GET    /api/authors/             → List authors
- POST   /api/authors/             → Create author
- GET    /api/authors/{id}/        → Get author
- PUT    /api/authors/{id}/        → Update author
- DELETE /api/authors/{id}/        → Delete author
- GET    /api/books/               → List books
- POST   /api/books/               → Create book
- GET    /api/books/{id}/          → Get book
- PUT    /api/books/{id}/          → Update book
- DELETE /api/books/{id}/          → Delete book
- GET    /api/books/available/     → Available books
- GET    /api/books/statistics/    → Book statistics
- POST   /api/books/{id}/toggle_availability/  → Toggle availability

Next Step: Day 16 - DRF Advanced (Authentication, Permissions, etc.)
""")
