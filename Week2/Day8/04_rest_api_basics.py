"""
Day 8 - REST API Basics
=======================
Learn: REST principles, API design, endpoints

Key Concepts:
- REST = REpresentational State Transfer
- Architectural style for designing networked applications
- Uses HTTP methods to perform operations on resources
"""

# ========== WHAT IS REST? ==========
print("=" * 60)
print("WHAT IS REST?")
print("=" * 60)

print("""
🌐 REST (REpresentational State Transfer):

REST is an architectural style for designing web APIs.
It's NOT a protocol or standard - it's a set of guidelines.

Key Characteristics:
1. Client-Server Architecture
2. Stateless (each request is independent)
3. Cacheable
4. Uniform Interface
5. Layered System
6. Code on Demand (optional)
""")

# ========== REST PRINCIPLES ==========
print("\n" + "=" * 60)
print("REST PRINCIPLES")
print("=" * 60)

print("""
📋 The 6 REST Principles:

1️⃣ CLIENT-SERVER SEPARATION
   ┌────────────┐         ┌────────────┐
   │   Client   │ ◄─────► │   Server   │
   │   (UI)     │         │   (Data)   │
   └────────────┘         └────────────┘
   - Client handles UI, server handles data
   - They can evolve independently

2️⃣ STATELESS
   - Server doesn't store client state
   - Each request contains all needed info
   - No sessions stored on server (ideally)
   
   Good:  GET /users?token=abc123
   Bad:   GET /users (expecting server to remember you)

3️⃣ CACHEABLE
   - Responses can be cached
   - Improves performance
   - Headers control caching: Cache-Control, ETag

4️⃣ UNIFORM INTERFACE
   - Consistent URL patterns
   - Standard HTTP methods
   - Self-descriptive messages
   
   /users        (collection)
   /users/123    (specific resource)

5️⃣ LAYERED SYSTEM
   Client → Load Balancer → API Gateway → Server → Database
   - Client doesn't know about layers
   - Allows flexibility and scalability

6️⃣ CODE ON DEMAND (Optional)
   - Server can send executable code
   - JavaScript in browsers is an example
""")

# ========== RESOURCES AND ENDPOINTS ==========
print("\n" + "=" * 60)
print("RESOURCES AND ENDPOINTS")
print("=" * 60)

print("""
📦 RESOURCE: Any entity that can be named and addressed
   Examples: User, Post, Product, Order, Comment

🔗 ENDPOINT: URL path to access a resource
   Examples: /users, /posts/123, /products

Good REST URL Design:
───────────────────────────────────────────────────────────
✅ Use nouns (resources), not verbs (actions)
   Good: GET /users
   Bad:  GET /getUsers

✅ Use plural nouns for collections
   Good: /users, /posts, /products
   Bad:  /user, /post, /product

✅ Use hierarchical structure for relationships
   Good: /users/123/posts (posts by user 123)
   Good: /posts/456/comments (comments on post 456)

✅ Use query parameters for filtering
   Good: /users?role=admin&status=active
   Good: /products?category=electronics&sort=price
───────────────────────────────────────────────────────────
""")

# ========== CRUD OPERATIONS ==========
print("\n" + "=" * 60)
print("CRUD TO HTTP MAPPING")
print("=" * 60)

print("""
📝 CRUD Operations mapped to HTTP Methods:

┌──────────┬──────────┬───────────────────┬────────────────────┐
│  CRUD    │  HTTP    │  Endpoint         │  Description       │
├──────────┼──────────┼───────────────────┼────────────────────┤
│  Create  │  POST    │  /users           │  Create new user   │
│  Read    │  GET     │  /users           │  Get all users     │
│  Read    │  GET     │  /users/123       │  Get specific user │
│  Update  │  PUT     │  /users/123       │  Replace user      │
│  Update  │  PATCH   │  /users/123       │  Partial update    │
│  Delete  │  DELETE  │  /users/123       │  Delete user       │
└──────────┴──────────┴───────────────────┴────────────────────┘
""")

# ========== API DESIGN EXAMPLE ==========
print("\n" + "=" * 60)
print("REST API DESIGN EXAMPLE")
print("=" * 60)

print("""
🏪 Example: E-Commerce API Design

USERS RESOURCE:
───────────────────────────────────────────────────────────
GET    /api/users              List all users
GET    /api/users/123          Get user 123
POST   /api/users              Create new user
PUT    /api/users/123          Replace user 123
PATCH  /api/users/123          Update user 123 partially
DELETE /api/users/123          Delete user 123

PRODUCTS RESOURCE:
───────────────────────────────────────────────────────────
GET    /api/products           List all products
GET    /api/products/456       Get product 456
POST   /api/products           Create new product
PUT    /api/products/456       Replace product 456
PATCH  /api/products/456       Update product 456
DELETE /api/products/456       Delete product 456

ORDERS RESOURCE (Nested):
───────────────────────────────────────────────────────────
GET    /api/users/123/orders        User 123's orders
GET    /api/orders/789              Get specific order
POST   /api/orders                  Create new order
PATCH  /api/orders/789              Update order status
DELETE /api/orders/789              Cancel order

FILTERING & PAGINATION:
───────────────────────────────────────────────────────────
GET /api/products?category=electronics
GET /api/products?price_min=100&price_max=500
GET /api/products?sort=price&order=asc
GET /api/products?page=2&limit=20
GET /api/users?role=admin&status=active
""")

# ========== REQUEST & RESPONSE FORMATS ==========
print("\n" + "=" * 60)
print("REQUEST & RESPONSE FORMATS")
print("=" * 60)

print("""
📤 REQUEST Example (Creating a user):

POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer <token>

{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "secure123",
    "role": "customer"
}

───────────────────────────────────────────────────────────

📥 RESPONSE Example (User created):

HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/users/124

{
    "id": 124,
    "name": "John Doe",
    "email": "john@example.com",
    "role": "customer",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
}
""")

# ========== COMMON API RESPONSE PATTERNS ==========
print("\n" + "=" * 60)
print("COMMON API RESPONSE PATTERNS")
print("=" * 60)

print("""
📋 Standard Response Patterns:

SINGLE RESOURCE:
{
    "id": 123,
    "name": "John",
    "email": "john@example.com"
}

COLLECTION (List):
{
    "data": [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ],
    "total": 100,
    "page": 1,
    "limit": 20
}

WITH PAGINATION:
{
    "data": [...],
    "pagination": {
        "total": 100,
        "page": 1,
        "per_page": 20,
        "total_pages": 5,
        "next": "/api/users?page=2",
        "prev": null
    }
}

ERROR RESPONSE:
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Email is required",
        "details": [
            {"field": "email", "message": "This field is required"}
        ]
    }
}
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - Simple REST Client")
print("=" * 60)

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

class SimpleRESTClient:
    """
    A simple REST client demonstrating API interactions
    """
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def _make_request(self, method, endpoint, data=None):
        """Make HTTP request and return response"""
        url = f"{self.base_url}{endpoint}"
        
        request_data = json.dumps(data).encode() if data else None
        req = Request(url, data=request_data, headers=self.headers, method=method)
        
        try:
            with urlopen(req, timeout=10) as response:
                body = response.read().decode()
                return {
                    'status': response.status,
                    'data': json.loads(body) if body else None,
                    'success': True
                }
        except HTTPError as e:
            return {
                'status': e.code,
                'error': e.reason,
                'success': False
            }
        except (URLError, Exception) as e:
            return {
                'status': None,
                'error': str(e),
                'success': False
            }
    
    def get(self, endpoint):
        """GET request"""
        return self._make_request('GET', endpoint)
    
    def post(self, endpoint, data):
        """POST request"""
        return self._make_request('POST', endpoint, data)
    
    def put(self, endpoint, data):
        """PUT request"""
        return self._make_request('PUT', endpoint, data)
    
    def patch(self, endpoint, data):
        """PATCH request"""
        return self._make_request('PATCH', endpoint, data)
    
    def delete(self, endpoint):
        """DELETE request"""
        return self._make_request('DELETE', endpoint)

# Demo with httpbin.org (echo API for testing)
print("\n🧪 Testing REST Client with httpbin.org:")
print("-" * 50)

client = SimpleRESTClient("https://httpbin.org")

# Test GET
print("\n1️⃣ GET Request:")
result = client.get("/get")
if result['success']:
    print(f"   Status: {result['status']}")
    print(f"   Response received successfully!")
else:
    print(f"   Error: {result.get('error', 'Unknown error')}")

# Test POST
print("\n2️⃣ POST Request:")
user_data = {"name": "John", "email": "john@example.com"}
result = client.post("/post", user_data)
if result['success']:
    print(f"   Status: {result['status']}")
    print(f"   Sent: {user_data}")
    print(f"   Server received: {result['data'].get('json', {})}")
else:
    print(f"   Error: {result.get('error', 'Unknown error')}")

# Test PUT
print("\n3️⃣ PUT Request:")
update_data = {"name": "John Updated", "email": "john.new@example.com"}
result = client.put("/put", update_data)
if result['success']:
    print(f"   Status: {result['status']}")
    print(f"   Updated data sent successfully!")
else:
    print(f"   Error: {result.get('error', 'Unknown error')}")

# Test DELETE
print("\n4️⃣ DELETE Request:")
result = client.delete("/delete")
if result['success']:
    print(f"   Status: {result['status']}")
    print(f"   Delete request successful!")
else:
    print(f"   Error: {result.get('error', 'Unknown error')}")

# ========== REST VS GRAPHQL ==========
print("\n" + "=" * 60)
print("REST VS GRAPHQL (Quick Comparison)")
print("=" * 60)

print("""
📊 REST vs GraphQL:

┌─────────────────┬──────────────────┬──────────────────────┐
│    Feature      │      REST        │      GraphQL         │
├─────────────────┼──────────────────┼──────────────────────┤
│ Data Fetching   │ Multiple         │ Single endpoint      │
│                 │ endpoints        │ /graphql             │
├─────────────────┼──────────────────┼──────────────────────┤
│ Over-fetching   │ Common           │ Request only what    │
│                 │                  │ you need             │
├─────────────────┼──────────────────┼──────────────────────┤
│ Learning Curve  │ Easier           │ Steeper              │
├─────────────────┼──────────────────┼──────────────────────┤
│ Caching         │ HTTP caching     │ More complex         │
├─────────────────┼──────────────────┼──────────────────────┤
│ Best For        │ Simple CRUD      │ Complex nested       │
│                 │ operations       │ data needs           │
└─────────────────┴──────────────────┴──────────────────────┘

Both are widely used! REST is more common for simple APIs.
""")

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("REST API BEST PRACTICES")
print("=" * 60)

print("""
✅ REST API Best Practices:

1. USE PROPER HTTP METHODS
   - GET for reading
   - POST for creating
   - PUT/PATCH for updating
   - DELETE for deleting

2. USE PROPER STATUS CODES
   - 200/201 for success
   - 400 for bad request
   - 401/403 for auth issues
   - 404 for not found
   - 500 for server errors

3. VERSION YOUR API
   - /api/v1/users
   - /api/v2/users
   
4. USE PAGINATION
   - /api/users?page=1&limit=20
   - Return total count in response

5. HANDLE ERRORS GRACEFULLY
   - Return meaningful error messages
   - Use consistent error format

6. SECURE YOUR API
   - Use HTTPS always
   - Implement authentication (JWT, OAuth)
   - Rate limiting
   - Input validation

7. DOCUMENT YOUR API
   - Use OpenAPI/Swagger
   - Provide examples
   - Keep it updated
""")

print("\n" + "=" * 60)
print("✅ REST API Basics - Complete!")
print("=" * 60)
