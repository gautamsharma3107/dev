"""
Day 8 - HTTP Methods
====================
Learn: GET, POST, PUT, PATCH, DELETE and when to use them

Key Concepts:
- HTTP methods define the action to perform on a resource
- Each method has specific use cases and semantics
- CRUD operations map to HTTP methods
"""

# ========== OVERVIEW OF HTTP METHODS ==========
print("=" * 60)
print("HTTP METHODS OVERVIEW")
print("=" * 60)

print("""
📋 HTTP Methods (Verbs):

┌──────────┬──────────────┬─────────────────────────────────────┐
│  Method  │  CRUD Action │  Description                        │
├──────────┼──────────────┼─────────────────────────────────────┤
│  GET     │  Read        │  Retrieve data from server          │
│  POST    │  Create      │  Send data to create new resource   │
│  PUT     │  Update      │  Replace entire resource            │
│  PATCH   │  Update      │  Partially update resource          │
│  DELETE  │  Delete      │  Remove a resource                  │
├──────────┼──────────────┼─────────────────────────────────────┤
│  HEAD    │  Read        │  GET without response body          │
│  OPTIONS │  Read        │  Get supported methods              │
└──────────┴──────────────┴─────────────────────────────────────┘

CRUD = Create, Read, Update, Delete
""")

# ========== GET METHOD ==========
print("\n" + "=" * 60)
print("GET METHOD - Retrieve Data")
print("=" * 60)

print("""
📖 GET Request:

Purpose: Retrieve data from the server
Body: No request body
Safe: Yes (doesn't modify data)
Idempotent: Yes (same result every time)

Examples:
---------
GET /api/users              → Get all users
GET /api/users/123          → Get user with ID 123
GET /api/users?role=admin   → Get users filtered by role
GET /search?q=python        → Search with query parameter
""")

# Simulating GET request
print("📝 Example GET Request:")
print("-" * 40)
print("""
GET /api/users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
Authorization: Bearer token123
""")

print("📥 Example GET Response:")
print("-" * 40)
print("""
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
}
""")

# ========== POST METHOD ==========
print("\n" + "=" * 60)
print("POST METHOD - Create Data")
print("=" * 60)

print("""
✏️ POST Request:

Purpose: Create a new resource
Body: Contains data for new resource
Safe: No (modifies server state)
Idempotent: No (creates new resource each time)

Examples:
---------
POST /api/users             → Create new user
POST /api/login             → Submit login credentials
POST /api/upload            → Upload a file
POST /api/orders            → Create new order
""")

print("📝 Example POST Request:")
print("-" * 40)
print("""
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer token123

{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "password": "secure123"
}
""")

print("📥 Example POST Response:")
print("-" * 40)
print("""
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/users/124

{
    "id": 124,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "created_at": "2024-01-15T10:30:00Z"
}
""")

# ========== PUT METHOD ==========
print("\n" + "=" * 60)
print("PUT METHOD - Replace/Update Data")
print("=" * 60)

print("""
🔄 PUT Request:

Purpose: Replace entire resource or create if doesn't exist
Body: Complete resource data
Safe: No (modifies server state)
Idempotent: Yes (same result if repeated)

Examples:
---------
PUT /api/users/123          → Replace user 123 completely
PUT /api/settings           → Replace all settings
PUT /api/profiles/123       → Update entire profile
""")

print("📝 Example PUT Request:")
print("-" * 40)
print("""
PUT /api/users/123 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "name": "John Doe Updated",
    "email": "john.new@example.com",
    "phone": "+1-555-0123",
    "address": "123 New Street"
}
""")

print("📥 Example PUT Response:")
print("-" * 40)
print("""
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 123,
    "name": "John Doe Updated",
    "email": "john.new@example.com",
    "phone": "+1-555-0123",
    "address": "123 New Street",
    "updated_at": "2024-01-15T11:00:00Z"
}
""")

# ========== PATCH METHOD ==========
print("\n" + "=" * 60)
print("PATCH METHOD - Partial Update")
print("=" * 60)

print("""
🔧 PATCH Request:

Purpose: Partially update a resource
Body: Only fields to update
Safe: No (modifies server state)
Idempotent: Not guaranteed

Examples:
---------
PATCH /api/users/123        → Update specific fields only
PATCH /api/orders/456       → Update order status only
""")

print("📝 Example PATCH Request:")
print("-" * 40)
print("""
PATCH /api/users/123 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
    "email": "john.updated@example.com"
}
""")

print("📥 Example PATCH Response:")
print("-" * 40)
print("""
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 123,
    "name": "John Doe",
    "email": "john.updated@example.com",
    "updated_at": "2024-01-15T11:30:00Z"
}
""")

# ========== DELETE METHOD ==========
print("\n" + "=" * 60)
print("DELETE METHOD - Remove Data")
print("=" * 60)

print("""
🗑️ DELETE Request:

Purpose: Remove a resource from the server
Body: Usually no body
Safe: No (modifies server state)
Idempotent: Yes (deleting twice has same effect)

Examples:
---------
DELETE /api/users/123       → Delete user 123
DELETE /api/posts/456       → Delete post 456
DELETE /api/cache           → Clear cache
""")

print("📝 Example DELETE Request:")
print("-" * 40)
print("""
DELETE /api/users/123 HTTP/1.1
Host: api.example.com
Authorization: Bearer token123
""")

print("📥 Example DELETE Response:")
print("-" * 40)
print("""
HTTP/1.1 204 No Content

(No body returned)

OR

HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "User 123 deleted successfully"
}
""")

# ========== PUT VS PATCH ==========
print("\n" + "=" * 60)
print("PUT VS PATCH - What's the Difference?")
print("=" * 60)

print("""
🔄 PUT vs 🔧 PATCH:

┌────────────────┬─────────────────────┬─────────────────────┐
│    Feature     │        PUT          │       PATCH         │
├────────────────┼─────────────────────┼─────────────────────┤
│ Purpose        │ Replace entire      │ Update partial      │
│                │ resource            │ resource            │
├────────────────┼─────────────────────┼─────────────────────┤
│ Body Content   │ Complete resource   │ Only changed fields │
├────────────────┼─────────────────────┼─────────────────────┤
│ Missing Fields │ Set to null/default │ Unchanged           │
├────────────────┼─────────────────────┼─────────────────────┤
│ Idempotent     │ Yes                 │ Not guaranteed      │
└────────────────┴─────────────────────┴─────────────────────┘

Example - User has: name, email, phone
-----------------------------------------
PUT (must send all):          PATCH (send only changes):
{                             {
    "name": "John",               "phone": "555-0123"
    "email": "j@test.com",    }
    "phone": "555-0123"
}

If you use PUT without phone, phone becomes null!
""")

# ========== SAFE AND IDEMPOTENT METHODS ==========
print("\n" + "=" * 60)
print("SAFE AND IDEMPOTENT METHODS")
print("=" * 60)

print("""
🔒 Safe Methods: Don't modify server state
   GET, HEAD, OPTIONS

🔄 Idempotent Methods: Same result when repeated
   GET, HEAD, OPTIONS, PUT, DELETE

┌──────────┬────────┬─────────────┐
│  Method  │  Safe  │  Idempotent │
├──────────┼────────┼─────────────┤
│  GET     │   ✅   │      ✅     │
│  HEAD    │   ✅   │      ✅     │
│  OPTIONS │   ✅   │      ✅     │
│  POST    │   ❌   │      ❌     │
│  PUT     │   ❌   │      ✅     │
│  PATCH   │   ❌   │      ❌     │
│  DELETE  │   ❌   │      ✅     │
└──────────┴────────┴─────────────┘

Why does it matter?
- Safe methods can be cached
- Idempotent methods can be retried safely on failure
""")

# ========== PRACTICAL PYTHON EXAMPLES ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES WITH PYTHON")
print("=" * 60)

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def make_request(method, url, data=None, headers=None):
    """Helper function to make HTTP requests"""
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    
    request_data = json.dumps(data).encode() if data else None
    
    req = Request(url, data=request_data, headers=headers, method=method)
    
    try:
        with urlopen(req, timeout=10) as response:
            return {
                'status': response.status,
                'headers': dict(response.headers),
                'body': json.loads(response.read().decode())
            }
    except HTTPError as e:
        return {'error': f"HTTP {e.code}: {e.reason}"}
    except URLError as e:
        return {'error': f"URL Error: {e.reason}"}
    except Exception as e:
        return {'error': str(e)}

# Using httpbin.org for testing
base_url = "https://httpbin.org"

print("\n🧪 Testing HTTP Methods with httpbin.org:")
print("-" * 50)

# Test GET
print("\n1️⃣ GET Request:")
result = make_request('GET', f"{base_url}/get")
if 'error' not in result:
    print(f"   Status: {result['status']}")
    print(f"   Origin: {result['body'].get('origin', 'N/A')}")
else:
    print(f"   {result['error']}")

# Test POST
print("\n2️⃣ POST Request:")
post_data = {"name": "John", "email": "john@example.com"}
result = make_request('POST', f"{base_url}/post", data=post_data)
if 'error' not in result:
    print(f"   Status: {result['status']}")
    print(f"   Sent Data: {result['body'].get('json', {})}")
else:
    print(f"   {result['error']}")

# Test PUT
print("\n3️⃣ PUT Request:")
put_data = {"name": "John Updated", "email": "john.new@example.com"}
result = make_request('PUT', f"{base_url}/put", data=put_data)
if 'error' not in result:
    print(f"   Status: {result['status']}")
    print(f"   Sent Data: {result['body'].get('json', {})}")
else:
    print(f"   {result['error']}")

# Test PATCH
print("\n4️⃣ PATCH Request:")
patch_data = {"email": "patched@example.com"}
result = make_request('PATCH', f"{base_url}/patch", data=patch_data)
if 'error' not in result:
    print(f"   Status: {result['status']}")
    print(f"   Sent Data: {result['body'].get('json', {})}")
else:
    print(f"   {result['error']}")

# Test DELETE
print("\n5️⃣ DELETE Request:")
result = make_request('DELETE', f"{base_url}/delete")
if 'error' not in result:
    print(f"   Status: {result['status']}")
else:
    print(f"   {result['error']}")

# ========== COMMON USE CASES ==========
print("\n" + "=" * 60)
print("COMMON USE CASES")
print("=" * 60)

print("""
📱 Real-World API Examples:

User Management:
  GET    /users         → List all users
  GET    /users/123     → Get specific user
  POST   /users         → Create new user
  PUT    /users/123     → Update entire user profile
  PATCH  /users/123     → Update user's email only
  DELETE /users/123     → Delete user

Blog Posts:
  GET    /posts         → List all posts
  GET    /posts/456     → Get specific post
  POST   /posts         → Create new post
  PUT    /posts/456     → Update entire post
  PATCH  /posts/456     → Update post title only
  DELETE /posts/456     → Delete post

E-commerce:
  GET    /products      → List products
  POST   /cart          → Add item to cart
  PATCH  /cart/items/1  → Update quantity
  DELETE /cart/items/1  → Remove from cart
  POST   /orders        → Create order
""")

print("\n" + "=" * 60)
print("✅ HTTP Methods - Complete!")
print("=" * 60)
