"""
MINI PROJECT 1: Secure Blog API
================================
Create a secure REST API for a blog platform

Requirements:
1. Token-based authentication for all write operations
2. Public read access for articles
3. Only article owners can edit/delete their articles
4. Admin can moderate (edit/delete) any article
5. Filtering by category, status, and date range
6. Search in title and content
7. Pagination with configurable page size
8. API documentation with Swagger

Models:
-------
- Article: title, content, category, status, author, created_at, updated_at

API Endpoints:
--------------
- POST /api/register/      - User registration (returns token)
- POST /api/login/         - User login (returns token)
- POST /api/logout/        - User logout (deletes token)
- GET /api/articles/       - List articles (public, with filtering)
- POST /api/articles/      - Create article (authenticated)
- GET /api/articles/{id}/  - Get article detail (public)
- PUT /api/articles/{id}/  - Update article (owner/admin only)
- DELETE /api/articles/{id}/ - Delete article (owner/admin only)
- POST /api/articles/{id}/publish/ - Publish article (owner only)

Documentation:
--------------
- /api/docs/ - Swagger UI
- /api/redoc/ - ReDoc
"""

# Your code here

print("=" * 50)
print("SECURE BLOG API")
print("=" * 50)
print("""
Implement the secure blog API with:
1. Token authentication
2. Owner/Admin permissions
3. Filtering and pagination
4. API documentation

Start by creating:
1. models.py - Article model
2. serializers.py - Article serializers
3. permissions.py - Custom permissions
4. filters.py - Article filters
5. pagination.py - Custom pagination
6. views.py - ViewSets and views
7. urls.py - URL routing

Good luck! 🚀
""")

# TODO: Implement the blog API
