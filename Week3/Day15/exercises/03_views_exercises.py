"""
EXERCISES: API Views
====================
Complete all exercises below
"""

# Exercise 1: Function-Based View
# TODO: Create a function-based API view

print("Exercise 1: Function-Based View")
print("-" * 40)

print("""
Create a function-based view for listing and creating products:

Requirements:
- Handle GET request: Return all products
- Handle POST request: Create a new product
- Return proper status codes
- Use ProductSerializer

Write your view:
""")

# Your code here:
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
#
# @api_view(['GET', 'POST'])
# def product_list(request):
#     pass


# Exercise 2: Class-Based APIView
# TODO: Convert the function view to a class-based view

print("\n\nExercise 2: Class-Based APIView")
print("-" * 40)

print("""
Convert Exercise 1 to a class-based APIView:

Requirements:
- Same functionality as Exercise 1
- Use get() and post() methods
- Handle object not found for detail view

Write your class view:
""")

# Your code here:
# from rest_framework.views import APIView
#
# class ProductListAPIView(APIView):
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass


# Exercise 3: Generic Views
# TODO: Use generic views for CRUD

print("\n\nExercise 3: Generic Views")
print("-" * 40)

print("""
Create API views using generic views:

Requirements:
1. ProductListCreate: GET list, POST create
2. ProductDetail: GET single, PUT update, DELETE remove

Hint: Use ListCreateAPIView and RetrieveUpdateDestroyAPIView

Write your views:
""")

# Your code here:
# from rest_framework import generics
#
# class ProductListCreate(generics.ListCreateAPIView):
#     pass
#
# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     pass


# Exercise 4: ViewSet
# TODO: Create a ModelViewSet

print("\n\nExercise 4: ViewSet")
print("-" * 40)

print("""
Create a ProductViewSet with ModelViewSet:

Requirements:
1. Full CRUD operations
2. Add search functionality (search by name)
3. Add ordering (by price, name)
4. Custom action: get_active_products (returns only active products)

Write your viewset:
""")

# Your code here:
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.filters import SearchFilter, OrderingFilter
#
# class ProductViewSet(viewsets.ModelViewSet):
#     pass


# Exercise 5: Custom Filtering
# TODO: Add custom filtering to ViewSet

print("\n\nExercise 5: Custom Filtering")
print("-" * 40)

print("""
Enhance ProductViewSet with custom filtering:

Requirements:
1. Filter by price range (min_price, max_price)
2. Filter by is_active status
3. Filter by category_id
4. Custom action: low_stock - products with stock < 10

Override get_queryset() to add filtering logic.

Write your enhanced viewset:
""")

# Your code here:
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         queryset = Product.objects.all()
#         
#         # Add your filtering logic here
#         # min_price = self.request.query_params.get('min_price')
#         
#         return queryset
#
#     @action(detail=False, methods=['get'])
#     def low_stock(self, request):
#         pass
