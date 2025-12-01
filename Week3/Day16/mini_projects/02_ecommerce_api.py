"""
MINI PROJECT 2: E-Commerce Product API
========================================
Create a REST API for an e-commerce product catalog

Requirements:
1. Token authentication for admin operations
2. Public access to product listing and details
3. Only admin users can create/edit/delete products
4. Advanced filtering (price range, category, availability)
5. Full-text search across products
6. Multiple ordering options
7. Cursor pagination for performance
8. Comprehensive API documentation

Models:
-------
- Category: name, description
- Product: name, description, price, category, stock, is_active, created_at

API Endpoints:
--------------
- GET /api/categories/         - List categories (public)
- POST /api/categories/        - Create category (admin only)
- GET /api/products/           - List products (public, with advanced filtering)
- POST /api/products/          - Create product (admin only)
- GET /api/products/{id}/      - Get product detail (public)
- PUT /api/products/{id}/      - Update product (admin only)
- DELETE /api/products/{id}/   - Delete product (admin only)
- GET /api/products/featured/  - Get featured products (public)
- POST /api/products/{id}/toggle-featured/ - Toggle featured (admin only)

Filtering Options:
------------------
- ?category=electronics
- ?min_price=100&max_price=500
- ?in_stock=true
- ?search=laptop
- ?ordering=price,-created_at

Documentation:
--------------
- /api/docs/ - Swagger UI with examples
- /api/redoc/ - ReDoc documentation
"""

# Your code here

print("=" * 50)
print("E-COMMERCE PRODUCT API")
print("=" * 50)
print("""
Implement the e-commerce API with:
1. Category and Product models
2. Admin-only write operations
3. Advanced filtering and search
4. Cursor pagination
5. Complete API documentation

Start by creating:
1. models.py - Category and Product models
2. serializers.py - Serializers with nested category
3. permissions.py - Admin permission checks
4. filters.py - Advanced product filters
5. pagination.py - Cursor pagination
6. views.py - ViewSets with custom actions
7. urls.py - URL routing

Good luck! 🚀
""")

# TODO: Implement the e-commerce API
