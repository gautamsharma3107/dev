"""
Day 15 - Why APIs?
==================
Learn: Understanding REST APIs and their importance

Key Concepts:
- APIs allow different applications to communicate
- REST (Representational State Transfer) is an architectural style
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- JSON is the standard data format for APIs
"""

# ========== WHAT IS AN API? ==========
print("=" * 60)
print("WHAT IS AN API?")
print("=" * 60)

"""
API = Application Programming Interface

Think of an API as a waiter in a restaurant:
- You (the client) want to order food
- The kitchen (the server) can prepare food
- The waiter (the API) takes your order and brings back food

APIs allow different software applications to communicate with each other.
"""

print("""
🍔 Restaurant Analogy:

CLIENT (You)  <----->  WAITER (API)  <----->  KITCHEN (Server/Database)

You don't go into the kitchen yourself!
The waiter handles all communication.

Similarly in web development:
FRONTEND APP  <----->  API  <----->  BACKEND/DATABASE
""")


# ========== WHY DO WE NEED APIs? ==========
print("\n" + "=" * 60)
print("WHY DO WE NEED APIs?")
print("=" * 60)

print("""
1. 📱 MULTIPLE CLIENTS
   - Same API can serve mobile apps, web apps, desktop apps
   - One backend, many frontends
   
2. 🔄 SEPARATION OF CONCERNS
   - Frontend developers focus on UI
   - Backend developers focus on business logic
   - They communicate via API
   
3. 🌐 THIRD-PARTY INTEGRATION
   - Your app can use Google Maps, Payment gateways, etc.
   - Other apps can use your data/services
   
4. 📈 SCALABILITY
   - Frontend and backend can scale independently
   - Easier to maintain and update
   
5. 🔒 SECURITY
   - API controls what data is exposed
   - Authentication and authorization
""")


# ========== REST API PRINCIPLES ==========
print("\n" + "=" * 60)
print("REST API PRINCIPLES")
print("=" * 60)

print("""
REST = REpresentational State Transfer

Key Principles:
1. STATELESS - Each request contains all needed information
2. CLIENT-SERVER - Separation between client and server
3. UNIFORM INTERFACE - Standard HTTP methods
4. CACHEABLE - Responses can be cached
5. LAYERED SYSTEM - Client doesn't know if connected directly to server
""")


# ========== HTTP METHODS ==========
print("\n" + "=" * 60)
print("HTTP METHODS")
print("=" * 60)

http_methods = {
    "GET": ("Read/Retrieve data", "/api/books/", "Get all books"),
    "POST": ("Create new data", "/api/books/", "Create a new book"),
    "PUT": ("Update entire resource", "/api/books/1/", "Update book with ID 1"),
    "PATCH": ("Update part of resource", "/api/books/1/", "Update specific fields"),
    "DELETE": ("Delete resource", "/api/books/1/", "Delete book with ID 1"),
}

print(f"{'Method':<10} {'Purpose':<25} {'Example URL':<20} {'Action'}")
print("-" * 80)
for method, (purpose, url, action) in http_methods.items():
    print(f"{method:<10} {purpose:<25} {url:<20} {action}")


# ========== HTTP STATUS CODES ==========
print("\n" + "=" * 60)
print("HTTP STATUS CODES")
print("=" * 60)

status_codes = {
    "2xx - Success": [
        ("200", "OK", "Request successful"),
        ("201", "Created", "Resource created successfully"),
        ("204", "No Content", "Success but no content to return"),
    ],
    "4xx - Client Error": [
        ("400", "Bad Request", "Invalid request data"),
        ("401", "Unauthorized", "Authentication required"),
        ("403", "Forbidden", "Not allowed to access"),
        ("404", "Not Found", "Resource doesn't exist"),
    ],
    "5xx - Server Error": [
        ("500", "Internal Server Error", "Server-side error"),
        ("502", "Bad Gateway", "Invalid response from server"),
        ("503", "Service Unavailable", "Server temporarily down"),
    ],
}

for category, codes in status_codes.items():
    print(f"\n{category}:")
    print("-" * 60)
    for code, name, description in codes:
        print(f"  {code} - {name}: {description}")


# ========== JSON FORMAT ==========
print("\n" + "=" * 60)
print("JSON FORMAT")
print("=" * 60)

import json

# Example book data in JSON format
book_data = {
    "id": 1,
    "title": "Learning Django REST Framework",
    "author": "John Doe",
    "price": 29.99,
    "is_available": True,
    "tags": ["python", "django", "api"],
    "publisher": {
        "name": "Tech Books",
        "location": "New York"
    }
}

print("JSON is the standard format for API data exchange:\n")
print(json.dumps(book_data, indent=2))

print("""
JSON Data Types:
- String: "text"
- Number: 42, 3.14
- Boolean: true, false
- Array: [1, 2, 3]
- Object: {"key": "value"}
- Null: null
""")


# ========== API REQUEST/RESPONSE EXAMPLE ==========
print("\n" + "=" * 60)
print("API REQUEST/RESPONSE EXAMPLE")
print("=" * 60)

print("""
📤 REQUEST (Client → Server)
---------------------------
GET /api/books/1/ HTTP/1.1
Host: example.com
Authorization: Bearer token123
Content-Type: application/json


📥 RESPONSE (Server → Client)
----------------------------
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "title": "Learning Django REST Framework",
    "author": "John Doe",
    "price": 29.99
}
""")


# ========== REAL-WORLD API EXAMPLES ==========
print("\n" + "=" * 60)
print("REAL-WORLD API EXAMPLES")
print("=" * 60)

print("""
🌍 Popular APIs You've Probably Used:

1. 🐦 Twitter API
   - Post tweets, get user data, search tweets
   
2. 📍 Google Maps API
   - Get directions, search places, display maps
   
3. 💳 Stripe API
   - Process payments, manage subscriptions
   
4. 🌤️ OpenWeather API
   - Get weather data for any location
   
5. 📸 Instagram API
   - Post photos, get user media, manage comments
   
6. 🎵 Spotify API
   - Search music, control playback, get playlists
""")


# ========== DJANGO REST FRAMEWORK OVERVIEW ==========
print("\n" + "=" * 60)
print("DJANGO REST FRAMEWORK (DRF)")
print("=" * 60)

print("""
Django REST Framework is the most popular toolkit for building 
Web APIs in Django.

Why DRF?
✅ Built on top of Django - use what you already know
✅ Serialization - easy data conversion
✅ Browsable API - test APIs in browser
✅ Authentication - multiple auth methods built-in
✅ Permissions - fine-grained access control
✅ Viewsets & Routers - less code, more power
✅ Documentation - excellent docs and community

Without DRF:
- Manual JSON conversion
- Custom authentication
- Manual URL routing for APIs
- No browsable interface

With DRF:
- Automatic serialization
- Built-in authentication classes
- Automatic URL routing with Routers
- Beautiful browsable API interface
""")


print("\n" + "=" * 60)
print("✅ Why APIs? - Complete!")
print("=" * 60)
print("""
Summary:
- APIs enable communication between applications
- REST is the standard architectural style
- HTTP methods define CRUD operations
- Status codes indicate request results
- JSON is the standard data format
- DRF makes building APIs in Django easy!

Next: Let's install and set up Django REST Framework!
""")
