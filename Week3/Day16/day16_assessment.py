"""
DAY 16 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 16 ASSESSMENT TEST - DRF Advanced")
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
Q1. What is the correct HTTP header format for Token authentication in DRF?
a) Bearer: <token>
b) Authorization: Token <token>
c) X-Auth-Token: <token>
d) Token: <token>

Your answer: """)

print("""
Q2. Which permission class allows anyone to read but only authenticated users to write?
a) IsAuthenticated
b) AllowAny
c) IsAuthenticatedOrReadOnly
d) DjangoModelPermissions

Your answer: """)

print("""
Q3. Which filter backend is used for text search across multiple fields?
a) DjangoFilterBackend
b) SearchFilter
c) OrderingFilter
d) TextSearchBackend

Your answer: """)

print("""
Q4. What is the main advantage of CursorPagination over PageNumberPagination?
a) It allows jumping to any page
b) It's more efficient for large datasets and consistent during data changes
c) It returns more data per request
d) It doesn't require an ordered queryset

Your answer: """)

print("""
Q5. In a custom permission class, which method checks access to a specific object?
a) has_permission()
b) has_object_permission()
c) check_permissions()
d) validate_object()

Your answer: """)

print("""
Q6. Which package is recommended for API documentation in DRF?
a) drf-yasg
b) drf-spectacular
c) swagger-codegen
d) rest-framework-docs

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a custom permission class called 'IsOwnerOrReadOnly' that:
- Allows read access (GET, HEAD, OPTIONS) to anyone
- Allows write access only if obj.owner == request.user
""")

# Write your code here:




print("""
Q8. (2 points) Configure a ViewSet with:
- DjangoFilterBackend, SearchFilter, and OrderingFilter
- filterset_fields: ['category', 'status']
- search_fields: ['title', 'content']
- ordering_fields: ['created_at', 'views']
- Default ordering: '-created_at'
""")

# Write your code here:




print("""
Q9. (2 points) Create a custom PageNumberPagination class that:
- Has page_size of 20
- Allows page_size query param with max 50
- Use it in a ViewSet
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between has_permission() and 
has_object_permission() in DRF permissions. When is each method called?

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
When done, check your answers with your professor.
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
Q1: b) Authorization: Token <token>
Q2: c) IsAuthenticatedOrReadOnly
Q3: b) SearchFilter
Q4: b) It's more efficient for large datasets and consistent during data changes
Q5: b) has_object_permission()
Q6: b) drf-spectacular

Section B (Coding):

Q7:
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


Q8:
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'status']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'views']
    ordering = ['-created_at']


Q9:
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50

class MyViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination


Section C:
Q10:
- has_permission() is called for every request before the view runs.
  It checks if the request should be permitted at the view level.
  Used for list and create operations.

- has_object_permission() is called when accessing a specific object.
  It's called after has_permission() passes, for detail views.
  Used for retrieve, update, and destroy operations on a specific object.
  
Example: For a GET /api/articles/5/ request:
1. First has_permission() is called
2. If it returns True, the object is retrieved
3. Then has_object_permission() is called with that object
"""
