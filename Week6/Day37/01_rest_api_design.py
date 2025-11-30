"""
REST API Design Principles
==========================
Day 37 - System Design Basics

Learn best practices for designing clean, scalable REST APIs.
"""

# ============================================================
# 1. REST API FUNDAMENTALS
# ============================================================

"""
REST (Representational State Transfer) Principles:

1. Client-Server Architecture
   - Separation of concerns
   - Client handles UI, Server handles data

2. Statelessness
   - Each request contains all info needed
   - No session state on server

3. Cacheability
   - Responses must define if cacheable
   - Improves performance

4. Uniform Interface
   - Consistent, predictable endpoints
   - Resource-based URLs

5. Layered System
   - Client doesn't know if connected directly to server
   - Allows for load balancers, proxies, etc.

6. Code on Demand (Optional)
   - Server can send executable code to client
"""

# ============================================================
# 2. URL/ENDPOINT DESIGN
# ============================================================

"""
Best Practices for URL Design:

✅ Good Examples:
- GET /users              - Get all users
- GET /users/123          - Get user by ID
- POST /users             - Create new user
- PUT /users/123          - Update entire user
- PATCH /users/123        - Partial update
- DELETE /users/123       - Delete user

❌ Bad Examples:
- GET /getUsers           - Don't use verbs
- GET /user/all           - Use plural nouns
- POST /users/create      - Redundant
- GET /users/delete/123   - Wrong method

Nested Resources:
- GET /users/123/orders           - User's orders
- GET /users/123/orders/456       - Specific order
- POST /users/123/orders          - Create order for user
"""

# Example: RESTful API Structure
api_endpoints = {
    "users": {
        "GET /users": "List all users",
        "GET /users/{id}": "Get single user",
        "POST /users": "Create user",
        "PUT /users/{id}": "Update user",
        "DELETE /users/{id}": "Delete user",
    },
    "products": {
        "GET /products": "List all products",
        "GET /products/{id}": "Get single product",
        "GET /products?category=electronics": "Filter by category",
        "GET /products?sort=price&order=asc": "Sort products",
    },
    "orders": {
        "GET /users/{user_id}/orders": "Get user's orders",
        "POST /users/{user_id}/orders": "Create order for user",
        "GET /orders/{id}": "Get order details",
    }
}

# ============================================================
# 3. HTTP METHODS
# ============================================================

"""
HTTP Methods and Their Usage:

| Method  | Action    | Idempotent | Safe | Body |
|---------|-----------|------------|------|------|
| GET     | Read      | Yes        | Yes  | No   |
| POST    | Create    | No         | No   | Yes  |
| PUT     | Replace   | Yes        | No   | Yes  |
| PATCH   | Partial   | No         | No   | Yes  |
| DELETE  | Delete    | Yes        | No   | No   |

Idempotent: Multiple identical requests = same result
Safe: Doesn't modify resource
"""

# ============================================================
# 4. HTTP STATUS CODES
# ============================================================

status_codes = {
    # Success (2xx)
    200: "OK - Request succeeded",
    201: "Created - Resource created successfully",
    204: "No Content - Success with no response body",
    
    # Redirection (3xx)
    301: "Moved Permanently",
    304: "Not Modified - Use cached version",
    
    # Client Errors (4xx)
    400: "Bad Request - Invalid syntax",
    401: "Unauthorized - Authentication required",
    403: "Forbidden - Not allowed to access",
    404: "Not Found - Resource doesn't exist",
    405: "Method Not Allowed",
    409: "Conflict - Resource conflict",
    422: "Unprocessable Entity - Validation error",
    429: "Too Many Requests - Rate limited",
    
    # Server Errors (5xx)
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
}

# Example: Status codes in response
def example_response_codes():
    """Examples of when to use different status codes"""
    
    # 200 OK - Successful GET/PUT/PATCH
    success_response = {
        "status": 200,
        "data": {"id": 1, "name": "John Doe"}
    }
    
    # 201 Created - Successful POST
    created_response = {
        "status": 201,
        "data": {"id": 2, "name": "Jane Doe"},
        "location": "/users/2"
    }
    
    # 204 No Content - Successful DELETE
    delete_response = {
        "status": 204
    }
    
    # 400 Bad Request - Invalid input
    bad_request = {
        "status": 400,
        "error": {
            "message": "Invalid email format",
            "field": "email"
        }
    }
    
    # 404 Not Found - Resource not found
    not_found = {
        "status": 404,
        "error": {
            "message": "User not found",
            "resource": "user",
            "id": 999
        }
    }
    
    return success_response, created_response, delete_response

# ============================================================
# 5. REQUEST/RESPONSE STRUCTURE
# ============================================================

# Standard Response Format
response_format = {
    "success": True,
    "data": {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    },
    "meta": {
        "timestamp": "2024-01-15T10:30:00Z",
        "request_id": "abc123"
    }
}

# Paginated Response
paginated_response = {
    "success": True,
    "data": [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
    ],
    "pagination": {
        "page": 1,
        "per_page": 10,
        "total": 100,
        "total_pages": 10,
        "next": "/items?page=2",
        "previous": None
    }
}

# Error Response Format
error_response = {
    "success": False,
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Validation failed",
        "details": [
            {"field": "email", "message": "Invalid email format"},
            {"field": "password", "message": "Must be at least 8 characters"}
        ]
    }
}

# ============================================================
# 6. VERSIONING STRATEGIES
# ============================================================

"""
API Versioning Methods:

1. URL Path Versioning (Most Common)
   - /api/v1/users
   - /api/v2/users

2. Query Parameter
   - /api/users?version=1
   - /api/users?version=2

3. Header Versioning
   - Accept: application/vnd.api+json;version=1

4. Content Negotiation
   - Accept: application/vnd.company.api+json;version=1

Recommendation: URL Path versioning for simplicity
"""

# Example versioning structure
api_versions = {
    "v1": {
        "endpoint": "/api/v1/users",
        "fields": ["id", "name", "email"]
    },
    "v2": {
        "endpoint": "/api/v2/users",
        "fields": ["id", "name", "email", "phone", "address"]
    }
}

# ============================================================
# 7. QUERY PARAMETERS
# ============================================================

"""
Common Query Parameter Patterns:

Filtering:
- GET /products?category=electronics
- GET /products?min_price=100&max_price=500
- GET /users?status=active

Sorting:
- GET /products?sort=price
- GET /products?sort=-price (descending)
- GET /products?sort=price,name

Pagination:
- GET /products?page=2&per_page=20
- GET /products?offset=20&limit=20
- GET /products?cursor=abc123

Field Selection (Sparse Fieldsets):
- GET /users?fields=id,name,email

Search:
- GET /products?search=laptop
- GET /products?q=laptop
"""

def build_query_params():
    """Example of query parameter usage"""
    
    # Filtering
    filter_example = "/products?category=electronics&brand=apple"
    
    # Sorting (descending price, ascending name)
    sort_example = "/products?sort=-price,name"
    
    # Pagination
    pagination_example = "/products?page=2&per_page=20"
    
    # Combined
    combined_example = "/products?category=electronics&sort=-price&page=1&per_page=10"
    
    return combined_example

# ============================================================
# 8. RATE LIMITING
# ============================================================

"""
Rate Limiting Strategies:

1. Fixed Window
   - 100 requests per hour
   - Resets at the start of each hour

2. Sliding Window
   - 100 requests per rolling hour
   - More fair distribution

3. Token Bucket
   - Tokens added at fixed rate
   - Requests consume tokens

Headers to Include:
- X-RateLimit-Limit: 100
- X-RateLimit-Remaining: 95
- X-RateLimit-Reset: 1609459200 (timestamp)
- Retry-After: 3600 (seconds)
"""

rate_limit_headers = {
    "X-RateLimit-Limit": "100",
    "X-RateLimit-Remaining": "95",
    "X-RateLimit-Reset": "2024-01-15T11:00:00Z",
}

# When rate limited (429 response)
rate_limited_response = {
    "status": 429,
    "error": {
        "code": "RATE_LIMIT_EXCEEDED",
        "message": "Too many requests. Please try again later.",
        "retry_after": 3600
    }
}

# ============================================================
# 9. HATEOAS (Hypermedia)
# ============================================================

"""
HATEOAS: Hypermedia as the Engine of Application State

Include links in responses to guide clients to related resources.
"""

hateoas_response = {
    "data": {
        "id": 123,
        "name": "John Doe",
        "email": "john@example.com"
    },
    "links": {
        "self": "/users/123",
        "orders": "/users/123/orders",
        "profile": "/users/123/profile",
        "update": "/users/123",
        "delete": "/users/123"
    }
}

# Collection with pagination links
collection_response = {
    "data": [...],
    "links": {
        "self": "/users?page=2",
        "first": "/users?page=1",
        "prev": "/users?page=1",
        "next": "/users?page=3",
        "last": "/users?page=10"
    }
}

# ============================================================
# 10. PRACTICAL EXAMPLE: User API Design
# ============================================================

class UserAPIDesign:
    """Example of well-designed User API endpoints"""
    
    def __init__(self):
        self.base_url = "/api/v1"
    
    def get_endpoints(self):
        return {
            # User CRUD
            "list_users": f"GET {self.base_url}/users",
            "get_user": f"GET {self.base_url}/users/{{id}}",
            "create_user": f"POST {self.base_url}/users",
            "update_user": f"PUT {self.base_url}/users/{{id}}",
            "partial_update": f"PATCH {self.base_url}/users/{{id}}",
            "delete_user": f"DELETE {self.base_url}/users/{{id}}",
            
            # Related resources
            "user_orders": f"GET {self.base_url}/users/{{id}}/orders",
            "user_profile": f"GET {self.base_url}/users/{{id}}/profile",
            
            # Actions (use POST for non-CRUD operations)
            "activate_user": f"POST {self.base_url}/users/{{id}}/activate",
            "deactivate_user": f"POST {self.base_url}/users/{{id}}/deactivate",
            "reset_password": f"POST {self.base_url}/users/{{id}}/reset-password",
        }
    
    def example_request_response(self):
        """Example of request and response for creating a user"""
        
        # POST /api/v1/users
        request_body = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "securePassword123"
        }
        
        # Response: 201 Created
        response = {
            "success": True,
            "data": {
                "id": 1,
                "name": "John Doe",
                "email": "john@example.com",
                "created_at": "2024-01-15T10:30:00Z"
            },
            "links": {
                "self": "/api/v1/users/1",
                "orders": "/api/v1/users/1/orders"
            }
        }
        
        return request_body, response

# ============================================================
# SUMMARY
# ============================================================

"""
REST API Design Best Practices:

1. Use nouns for resources, not verbs
2. Use proper HTTP methods (GET, POST, PUT, DELETE)
3. Return appropriate status codes
4. Version your API
5. Support filtering, sorting, pagination
6. Use consistent response formats
7. Implement rate limiting
8. Include error details
9. Add HATEOAS links where appropriate
10. Document your API (OpenAPI/Swagger)
"""

if __name__ == "__main__":
    print("REST API Design Principles")
    print("=" * 50)
    
    api = UserAPIDesign()
    endpoints = api.get_endpoints()
    
    print("\nUser API Endpoints:")
    for name, endpoint in endpoints.items():
        print(f"  {name}: {endpoint}")
    
    print("\nExample Status Codes:")
    for code, description in list(status_codes.items())[:5]:
        print(f"  {code}: {description}")
