# Day 15 Quick Reference Cheat Sheet

## Django REST Framework Basics

### Installation
```bash
pip install djangorestframework
```

### Settings Configuration
```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

## HTTP Methods & Status Codes
```python
# HTTP Methods
GET     # Read/Retrieve data
POST    # Create new data
PUT     # Update entire resource
PATCH   # Update part of resource
DELETE  # Delete resource

# Common Status Codes
200  # OK - Success
201  # Created - Resource created
204  # No Content - Success, no content
400  # Bad Request - Invalid data
401  # Unauthorized - Auth required
403  # Forbidden - Not allowed
404  # Not Found - Resource missing
500  # Server Error
```

## Serializers
```python
from rest_framework import serializers
from .models import Book

# ModelSerializer (Recommended)
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # Or: fields = ['id', 'title', 'author', 'price']
        # Or: exclude = ['created_at']
        read_only_fields = ['id', 'created_at']

# Custom validation
def validate_price(self, value):
    if value <= 0:
        raise serializers.ValidationError("Price must be positive")
    return value

# SerializerMethodField
discounted_price = serializers.SerializerMethodField()

def get_discounted_price(self, obj):
    return float(obj.price) * 0.9
```

## Using Serializers
```python
# Serialize (Python → JSON)
serializer = BookSerializer(book)          # Single object
serializer = BookSerializer(books, many=True)  # Multiple objects
serializer.data  # Get JSON-ready dict

# Deserialize (JSON → Python)
serializer = BookSerializer(data=request.data)
serializer.is_valid()          # Always call first!
serializer.validated_data      # Cleaned data
serializer.save()              # Create object
serializer.errors              # Validation errors

# Update existing object
serializer = BookSerializer(book, data=request.data)
serializer.is_valid()
serializer.save()
```

## API Views

### Function-Based View
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

### Generic Views
```python
from rest_framework import generics

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

### ViewSet (Recommended for CRUD)
```python
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Custom action
    @action(detail=False, methods=['get'])
    def available(self, request):
        books = self.queryset.filter(is_available=True)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
```

## URL Routing

### Manual URLs
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
]
```

### Router (for ViewSets)
```python
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## Filtering & Searching
```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Built-in filters
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['price', 'title']
    ordering = ['-created_at']

# Usage:
# GET /books/?search=django
# GET /books/?ordering=price
# GET /books/?ordering=-price
```

## Common Patterns
```python
# Different serializer for list vs detail
def get_serializer_class(self):
    if self.action == 'list':
        return BookListSerializer
    return BookSerializer

# Custom queryset
def get_queryset(self):
    queryset = Book.objects.all()
    author = self.request.query_params.get('author')
    if author:
        queryset = queryset.filter(author__name=author)
    return queryset

# Add extra data on create
def perform_create(self, serializer):
    serializer.save(created_by=self.request.user)
```

## Testing API with curl
```bash
# GET all
curl http://localhost:8000/api/books/

# GET one
curl http://localhost:8000/api/books/1/

# POST create
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title": "New Book", "author_id": 1, "price": "29.99"}'

# PUT update
curl -X PUT http://localhost:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated", "author_id": 1, "price": "39.99"}'

# PATCH partial update
curl -X PATCH http://localhost:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{"price": "49.99"}'

# DELETE
curl -X DELETE http://localhost:8000/api/books/1/
```

## Project Structure
```
project/
├── project/
│   ├── settings.py    # Add 'rest_framework'
│   └── urls.py        # Include api.urls
├── api/
│   ├── models.py      # Data models
│   ├── serializers.py # Serializers
│   ├── views.py       # API views/viewsets
│   ├── urls.py        # API routes
│   └── admin.py       # Admin config
└── manage.py
```

---
**Keep this handy for quick reference!** 🚀
