"""
Day 15 - Serializers in Django REST Framework
==============================================
Learn: Converting complex data to/from JSON

Key Concepts:
- Serializers convert between Python objects and JSON
- Similar to Django Forms but for API data
- Validation and data transformation
- Different types of serializers
"""

# ========== WHAT ARE SERIALIZERS? ==========
print("=" * 60)
print("WHAT ARE SERIALIZERS?")
print("=" * 60)

print("""
Serializers in DRF serve two main purposes:

1. SERIALIZATION (Python → JSON)
   - Convert Django model instances to JSON for API responses
   - Convert complex Python objects to simple, JSON-ready data
   
2. DESERIALIZATION (JSON → Python)
   - Convert incoming JSON data to Python objects
   - Validate incoming data before saving to database

Think of serializers as translators between:
- Your Django models ↔ JSON data clients understand
""")

# Visual representation
print("""
Serialization Flow:
==================

SERIALIZATION (Output/Response):
Model Instance → Serializer → Python Dict → JSON

    Book object         BookSerializer        {"title": "..."}       API Response
    ┌─────────┐         ┌────────────┐       ┌──────────────┐       ┌─────────┐
    │ title   │   →     │ serialize  │   →   │ Python dict  │   →   │  JSON   │
    │ author  │         └────────────┘       └──────────────┘       └─────────┘
    └─────────┘


DESERIALIZATION (Input/Request):
JSON → Python Dict → Serializer (Validate) → Model Instance

    API Request         Python dict          BookSerializer         Book object
    ┌─────────┐       ┌──────────────┐       ┌────────────┐       ┌─────────┐
    │  JSON   │   →   │ Python dict  │   →   │ validate   │   →   │ save()  │
    └─────────┘       └──────────────┘       └────────────┘       └─────────┘
""")


# ========== BASIC SERIALIZER ==========
print("\n" + "=" * 60)
print("BASIC SERIALIZER")
print("=" * 60)

print("""
Creating a basic serializer (without model):

# serializers.py

from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, allow_blank=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    published_date = serializers.DateField()
    isbn = serializers.CharField(max_length=13)
    is_available = serializers.BooleanField(default=True)
    
    def create(self, validated_data):
        \"\"\"Create and return a new Book instance.\"\"\"
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        \"\"\"Update and return an existing Book instance.\"\"\"
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.save()
        return instance
""")


# ========== MODEL SERIALIZER ==========
print("\n" + "=" * 60)
print("MODEL SERIALIZER (Recommended!)")
print("=" * 60)

print("""
ModelSerializer automatically generates fields based on model!

# serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields
        
# Or specify fields explicitly:
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'is_available']

# Or exclude certain fields:
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['created_at', 'updated_at']

# Read-only fields:
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
""")


# ========== SERIALIZER FIELD TYPES ==========
print("\n" + "=" * 60)
print("SERIALIZER FIELD TYPES")
print("=" * 60)

field_types = {
    "CharField": "String data",
    "IntegerField": "Integer numbers",
    "FloatField": "Floating point numbers",
    "DecimalField": "Decimal numbers (money)",
    "BooleanField": "True/False",
    "DateField": "Date (YYYY-MM-DD)",
    "DateTimeField": "DateTime",
    "TimeField": "Time",
    "EmailField": "Email with validation",
    "URLField": "URL with validation",
    "SlugField": "Slug strings",
    "UUIDField": "UUID strings",
    "IPAddressField": "IP addresses",
    "FileField": "File uploads",
    "ImageField": "Image uploads",
    "ListField": "List of items",
    "DictField": "Dictionary/JSON",
    "ChoiceField": "Predefined choices",
    "SerializerMethodField": "Custom computed field",
}

print(f"{'Field Type':<25} {'Description'}")
print("-" * 60)
for field, desc in field_types.items():
    print(f"{field:<25} {desc}")


# ========== FIELD OPTIONS ==========
print("\n" + "=" * 60)
print("COMMON FIELD OPTIONS")
print("=" * 60)

print("""
Field options control validation and behavior:

# Required vs Optional
title = serializers.CharField(required=True)      # Must provide
subtitle = serializers.CharField(required=False)  # Optional

# Default values
is_active = serializers.BooleanField(default=True)

# Allow blank/null
description = serializers.CharField(allow_blank=True)
bio = serializers.CharField(allow_null=True)

# Read-only / Write-only
id = serializers.IntegerField(read_only=True)     # Only in responses
password = serializers.CharField(write_only=True)  # Only in requests

# Validation
email = serializers.EmailField()                   # Auto-validates email
price = serializers.DecimalField(
    max_digits=6, 
    decimal_places=2,
    min_value=0,
    max_value=9999.99
)

# Help text
name = serializers.CharField(help_text="Enter book name")

# Source (rename fields)
author_name = serializers.CharField(source='author.name')
""")


# ========== USING SERIALIZERS ==========
print("\n" + "=" * 60)
print("USING SERIALIZERS IN PRACTICE")
print("=" * 60)

print("""
# In Django shell or views:

# 1. SERIALIZE - Model to JSON (for response)
>>> from api.models import Book
>>> from api.serializers import BookSerializer

>>> book = Book.objects.first()
>>> serializer = BookSerializer(book)
>>> serializer.data
{'id': 1, 'title': 'Django for Beginners', 'author': 'John Doe', ...}

# Serialize multiple objects (many=True)
>>> books = Book.objects.all()
>>> serializer = BookSerializer(books, many=True)
>>> serializer.data
[{'id': 1, 'title': 'Django for Beginners', ...}, {'id': 2, ...}]


# 2. DESERIALIZE - JSON to Model (for creating/updating)
>>> data = {
...     'title': 'New Book',
...     'author': 'Jane Smith',
...     'price': '29.99',
...     'published_date': '2024-01-15',
...     'isbn': '1234567890123'
... }

>>> serializer = BookSerializer(data=data)
>>> serializer.is_valid()  # Always call this first!
True
>>> serializer.validated_data  # Cleaned data
{'title': 'New Book', 'author': 'Jane Smith', ...}
>>> serializer.save()  # Create the object
<Book: New Book by Jane Smith>

# With validation errors:
>>> serializer.is_valid()
False
>>> serializer.errors
{'title': ['This field is required.']}
""")


# ========== NESTED SERIALIZERS ==========
print("\n" + "=" * 60)
print("NESTED SERIALIZERS")
print("=" * 60)

print("""
For related objects (ForeignKey, Many-to-Many):

# models.py
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


# serializers.py
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    # Nested serializer
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id']


# Response will look like:
{
    "id": 1,
    "title": "Django for Beginners",
    "author": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }
}
""")


# ========== CUSTOM VALIDATION ==========
print("\n" + "=" * 60)
print("CUSTOM VALIDATION")
print("=" * 60)

print("""
# Field-level validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    # Validate single field
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        if value > 1000:
            raise serializers.ValidationError("Price is too high")
        return value
    
    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters")
        if not value.isdigit():
            raise serializers.ValidationError("ISBN must contain only digits")
        return value
    
    # Object-level validation (validate multiple fields)
    def validate(self, data):
        if data.get('title', '').lower() == 'test':
            raise serializers.ValidationError("Title cannot be 'test'")
        return data
""")


# ========== SERIALIZER METHOD FIELD ==========
print("\n" + "=" * 60)
print("SERIALIZER METHOD FIELD")
print("=" * 60)

print("""
Add computed/custom fields:

class BookSerializer(serializers.ModelSerializer):
    # Custom computed fields
    discounted_price = serializers.SerializerMethodField()
    time_since_published = serializers.SerializerMethodField()
    full_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'discounted_price', 
                  'published_date', 'time_since_published', 'full_info']
    
    def get_discounted_price(self, obj):
        \"\"\"Calculate 10% discount\"\"\"
        return float(obj.price) * 0.9
    
    def get_time_since_published(self, obj):
        \"\"\"Calculate days since published\"\"\"
        from datetime import date
        delta = date.today() - obj.published_date
        return f"{delta.days} days ago"
    
    def get_full_info(self, obj):
        \"\"\"Combine multiple fields\"\"\"
        return f"{obj.title} by {obj.author} - ${obj.price}"


# Response will include:
{
    "id": 1,
    "title": "Django for Beginners",
    "price": "29.99",
    "discounted_price": 26.99,
    "published_date": "2024-01-15",
    "time_since_published": "45 days ago",
    "full_info": "Django for Beginners by John Doe - $29.99"
}
""")


# ========== COMPLETE SERIALIZER EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE SERIALIZER EXAMPLE")
print("=" * 60)

complete_serializer = '''
# api/serializers.py

from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author model."""
    books_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio', 'books_count']
        read_only_fields = ['id']
    
    def get_books_count(self, obj):
        return obj.books.count()


class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book model."""
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    discounted_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_id', 'description',
            'price', 'discounted_price', 'published_date', 
            'isbn', 'is_available', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_discounted_price(self, obj):
        """Calculate 10% discount."""
        return round(float(obj.price) * 0.9, 2)
    
    def validate_isbn(self, value):
        """Validate ISBN is 13 digits."""
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters")
        if not value.isdigit():
            raise serializers.ValidationError("ISBN must contain only digits")
        return value
    
    def validate_price(self, value):
        """Validate price is positive."""
        if value <= 0:
            raise serializers.ValidationError("Price must be positive")
        return value


class BookListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list view."""
    author_name = serializers.CharField(source='author.name')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'price', 'is_available']
'''

print(complete_serializer)


print("\n" + "=" * 60)
print("✅ Serializers - Complete!")
print("=" * 60)
print("""
Summary:
- Serializers convert between Python objects and JSON
- ModelSerializer auto-generates fields from models
- Use field options for validation and behavior
- Add custom validation with validate_<field> methods
- Use SerializerMethodField for computed fields
- Nest serializers for related objects

Next: Let's learn about API Views and Viewsets!
""")
