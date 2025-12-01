"""
DAY 15 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 15 ASSESSMENT TEST - Django REST Framework Basics")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. Which HTTP method is used to create a new resource?
a) GET
b) POST
c) PUT
d) DELETE

Your answer: """)

print("""
Q2. What status code indicates that a resource was successfully created?
a) 200 OK
b) 201 Created
c) 204 No Content
d) 400 Bad Request

Your answer: """)

print("""
Q3. In DRF, which class should you use for full CRUD operations with automatic URL routing?
a) APIView
b) GenericAPIView
c) ModelViewSet
d) ListCreateAPIView

Your answer: """)

print("""
Q4. What is the purpose of a Serializer in DRF?
a) To define database tables
b) To convert between Python objects and JSON
c) To handle user authentication
d) To create URL patterns

Your answer: """)

print("""
Q5. Which attribute in ModelSerializer is used to specify which model fields to include?
a) fields
b) model
c) queryset
d) serializer_class

Your answer: """)

print("""
Q6. What does the @action decorator do in a ViewSet?
a) Creates a new model
b) Adds custom endpoints beyond standard CRUD
c) Validates incoming data
d) Handles authentication

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a basic ModelSerializer for this Product model:

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

Requirements:
- Include all fields
- Make 'id' and 'created_at' read-only
""")

# Write your code here:
print("# Your serializer code:")


print("""
Q8. (2 points) Write a function-based API view to list all products:

Requirements:
- Handle GET requests only
- Return all products using ProductSerializer
- Return proper Response
""")

# Write your code here:
print("# Your view code:")


print("""
Q9. (2 points) Write URL patterns to connect a ProductViewSet to /api/products/:

Requirements:
- Use DefaultRouter
- Register ProductViewSet
- Include router urls in urlpatterns
""")

# Write your code here:
print("# Your URL code:")


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between:
1. Function-based views (@api_view)
2. Class-based views (APIView)
3. ViewSets

When would you use each one?

Your answer:
""")

# Write your explanation here as comments:
# 


# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with the answer key below.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: b) POST - Used to create new resources
Q2: b) 201 Created - Standard code for successful creation
Q3: c) ModelViewSet - Provides full CRUD with router support
Q4: b) Convert between Python objects and JSON
Q5: a) fields - Specifies which fields to include
Q6: b) Adds custom endpoints beyond standard CRUD

Section B (Coding):

Q7: ProductSerializer
```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # or ['id', 'name', 'price', 'stock', 'created_at']
        read_only_fields = ['id', 'created_at']
```

Q8: Function-based view
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
```

Q9: URL routing
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

Section C:
Q10: 
1. @api_view (Function-based):
   - Simplest approach
   - Good for simple, one-off endpoints
   - Full control but more code
   - Use when: Simple endpoints, quick prototyping

2. APIView (Class-based):
   - More structured than functions
   - Organize code by HTTP method (get, post, etc.)
   - Better for complex logic
   - Use when: Need more organization, multiple methods

3. ViewSet:
   - Combines list/create/retrieve/update/delete
   - Works with Routers for automatic URL generation
   - Least code, most abstraction
   - Use when: Full CRUD operations, REST best practices

General recommendation:
- Use ViewSets for standard CRUD resources
- Use APIView for custom, complex logic
- Use @api_view for simple, standalone endpoints
"""
