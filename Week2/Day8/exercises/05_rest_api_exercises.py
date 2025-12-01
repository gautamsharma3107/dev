"""
Day 8 - Exercise 5: REST API Exercises
======================================
Practice designing and working with REST APIs
"""

print("=" * 60)
print("Exercise 5: REST API Design")
print("=" * 60)

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# ============================================================
# Exercise 5.1: Design a REST API
# ============================================================

print("\n📝 Exercise 5.1: Design a Blog API")
print("-" * 50)
print("""
Design RESTful endpoints for a Blog API with the following resources:
- Posts (title, content, author_id, category, created_at)
- Authors (name, email, bio)
- Comments (post_id, author_name, content, created_at)
- Categories (name, description)

List all the endpoints you would create with:
- HTTP Method
- URL Path
- Description
- Example Request/Response (for at least 3 endpoints)
""")

# TODO: Write your API design below as comments:

# POSTS:
# 

# AUTHORS:
# 

# COMMENTS:
# 

# CATEGORIES:
# 

# Example Request/Response:
# 

# ============================================================
# Exercise 5.2: Build a Simple API Client
# ============================================================

print("\n📝 Exercise 5.2: Build API Client Class")
print("-" * 50)
print("""
Create a reusable API client class that can:
- Set a base URL
- Set default headers (like Authorization)
- Make GET, POST, PUT, PATCH, DELETE requests
- Handle errors gracefully
- Return parsed JSON responses
""")

class APIClient:
    """
    A reusable REST API client.
    """
    
    def __init__(self, base_url, default_headers=None):
        """Initialize the API client with base URL and optional headers"""
        # TODO: Implement initialization
        pass
    
    def set_auth_token(self, token):
        """Set Bearer token for authentication"""
        # TODO: Implement
        pass
    
    def get(self, endpoint, params=None):
        """Make GET request"""
        # TODO: Implement
        pass
    
    def post(self, endpoint, data):
        """Make POST request with JSON body"""
        # TODO: Implement
        pass
    
    def put(self, endpoint, data):
        """Make PUT request with JSON body"""
        # TODO: Implement
        pass
    
    def patch(self, endpoint, data):
        """Make PATCH request with JSON body"""
        # TODO: Implement
        pass
    
    def delete(self, endpoint):
        """Make DELETE request"""
        # TODO: Implement
        pass

# Test your client:
# client = APIClient("https://httpbin.org")
# print(client.get("/get"))
# print(client.post("/post", {"name": "John"}))

# ============================================================
# Exercise 5.3: API Response Handling
# ============================================================

print("\n📝 Exercise 5.3: Handle Different Response Types")
print("-" * 50)
print("""
Create a function that handles various API response formats and
normalizes them to a consistent structure.

Your function should handle:
1. Successful responses with data
2. Empty successful responses (204 No Content)
3. Error responses with different formats
4. Paginated responses
""")

def normalize_response(status_code, response_body):
    """
    Normalize API response to a consistent format.
    
    Returns:
        {
            "success": bool,
            "status": int,
            "data": any or None,
            "error": str or None,
            "pagination": dict or None
        }
    """
    # TODO: Implement normalization
    pass

# Test cases:
# test_responses = [
#     (200, {"user": {"id": 1, "name": "John"}}),
#     (201, {"id": 5, "message": "Created"}),
#     (204, None),
#     (400, {"error": "Invalid email"}),
#     (404, {"message": "Not found"}),
#     (200, {"data": [1,2,3], "page": 1, "total": 10}),
# ]
# 
# for status, body in test_responses:
#     result = normalize_response(status, body)
#     print(f"Status {status}: {result}")

# ============================================================
# Exercise 5.4: Query Parameter Builder
# ============================================================

print("\n📝 Exercise 5.4: Build Query Parameters")
print("-" * 50)
print("""
Create a function that builds query parameters for API requests.

Features:
- Handle None values (exclude them)
- Handle lists (convert to comma-separated or multiple params)
- Handle boolean values (convert to "true"/"false")
- URL encode special characters
""")

def build_query_params(params):
    """
    Build URL query string from parameters dictionary.
    
    Args:
        params: dict of parameter names and values
        
    Returns:
        str: Query string (without leading ?)
    """
    # TODO: Implement
    pass

# Test cases:
# print(build_query_params({"page": 1, "limit": 10}))
# # Expected: "page=1&limit=10"

# print(build_query_params({"search": "hello world", "active": True}))
# # Expected: "search=hello%20world&active=true"

# print(build_query_params({"name": "John", "empty": None, "tags": ["python", "api"]}))
# # Expected: "name=John&tags=python,api"

# ============================================================
# Exercise 5.5: Pagination Handler
# ============================================================

print("\n📝 Exercise 5.5: Implement Pagination")
print("-" * 50)
print("""
Create a class that handles API pagination.

Features:
- Track current page and total pages
- Generate next/previous page URLs
- Check if more pages exist
- Calculate offset for database queries
""")

class Paginator:
    """Handle API pagination."""
    
    def __init__(self, base_url, page=1, per_page=20, total_items=0):
        """Initialize paginator"""
        # TODO: Implement
        pass
    
    @property
    def total_pages(self):
        """Calculate total number of pages"""
        # TODO: Implement
        pass
    
    @property
    def has_next(self):
        """Check if there's a next page"""
        # TODO: Implement
        pass
    
    @property
    def has_prev(self):
        """Check if there's a previous page"""
        # TODO: Implement
        pass
    
    @property
    def offset(self):
        """Calculate offset for database queries"""
        # TODO: Implement
        pass
    
    def next_url(self):
        """Get URL for next page"""
        # TODO: Implement
        pass
    
    def prev_url(self):
        """Get URL for previous page"""
        # TODO: Implement
        pass
    
    def to_dict(self):
        """Return pagination info as dictionary"""
        # TODO: Implement
        pass

# Test:
# paginator = Paginator("/api/users", page=2, per_page=10, total_items=45)
# print(f"Total pages: {paginator.total_pages}")
# print(f"Has next: {paginator.has_next}")
# print(f"Has prev: {paginator.has_prev}")
# print(f"Offset: {paginator.offset}")
# print(f"Next URL: {paginator.next_url()}")
# print(f"Prev URL: {paginator.prev_url()}")
# print(f"Info: {paginator.to_dict()}")

# ============================================================
# Exercise 5.6: Real API Integration
# ============================================================

print("\n📝 Exercise 5.6: Real API Integration")
print("-" * 50)
print("""
Use a real public API to fetch and display data.
Use the JSONPlaceholder API (https://jsonplaceholder.typicode.com)

Tasks:
1. Fetch all users
2. Fetch posts by a specific user
3. Fetch comments on a post
4. Display the data in a formatted way
""")

def fetch_users():
    """Fetch all users from JSONPlaceholder API"""
    # TODO: Implement
    pass

def fetch_user_posts(user_id):
    """Fetch posts by a specific user"""
    # TODO: Implement
    pass

def fetch_post_comments(post_id):
    """Fetch comments on a specific post"""
    # TODO: Implement
    pass

def display_user_summary():
    """
    Display a summary:
    - List all users (name, email)
    - For the first user, show their posts
    - For the first post, show its comments
    """
    # TODO: Implement
    pass

# Run:
# display_user_summary()

print("\n" + "=" * 60)
print("✅ Complete the exercises above!")
print("=" * 60)

"""
SOLUTIONS:

Exercise 5.1:
# POSTS:
# GET    /api/posts                  List all posts
# GET    /api/posts/{id}             Get a specific post
# POST   /api/posts                  Create a new post
# PUT    /api/posts/{id}             Update a post
# PATCH  /api/posts/{id}             Partially update a post
# DELETE /api/posts/{id}             Delete a post
# GET    /api/posts?category=tech    Filter by category
# GET    /api/posts?author_id=5      Filter by author

# AUTHORS:
# GET    /api/authors                List all authors
# GET    /api/authors/{id}           Get an author
# GET    /api/authors/{id}/posts     Get posts by author
# POST   /api/authors                Create author
# PUT    /api/authors/{id}           Update author
# DELETE /api/authors/{id}           Delete author

# COMMENTS:
# GET    /api/posts/{id}/comments    Get comments on a post
# POST   /api/posts/{id}/comments    Add comment to post
# DELETE /api/comments/{id}          Delete a comment

# CATEGORIES:
# GET    /api/categories             List categories
# POST   /api/categories             Create category
# GET    /api/categories/{id}/posts  Get posts in category

Exercise 5.2:
class APIClient:
    def __init__(self, base_url, default_headers=None):
        self.base_url = base_url.rstrip('/')
        self.headers = default_headers or {'Content-Type': 'application/json'}
    
    def set_auth_token(self, token):
        self.headers['Authorization'] = f'Bearer {token}'
    
    def _request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        req_data = json.dumps(data).encode() if data else None
        req = Request(url, data=req_data, headers=self.headers, method=method)
        try:
            with urlopen(req, timeout=10) as response:
                return {"status": response.status, "data": json.loads(response.read().decode())}
        except HTTPError as e:
            return {"status": e.code, "error": e.reason}
        except URLError as e:
            return {"error": str(e)}
    
    def get(self, endpoint, params=None):
        if params:
            endpoint += "?" + "&".join(f"{k}={v}" for k, v in params.items())
        return self._request('GET', endpoint)
    
    def post(self, endpoint, data):
        return self._request('POST', endpoint, data)
    
    def put(self, endpoint, data):
        return self._request('PUT', endpoint, data)
    
    def patch(self, endpoint, data):
        return self._request('PATCH', endpoint, data)
    
    def delete(self, endpoint):
        return self._request('DELETE', endpoint)

Exercise 5.4:
from urllib.parse import urlencode, quote

def build_query_params(params):
    clean_params = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, bool):
            clean_params[key] = str(value).lower()
        elif isinstance(value, list):
            clean_params[key] = ",".join(str(v) for v in value)
        else:
            clean_params[key] = value
    return urlencode(clean_params)

Exercise 5.5:
import math

class Paginator:
    def __init__(self, base_url, page=1, per_page=20, total_items=0):
        self.base_url = base_url
        self.page = page
        self.per_page = per_page
        self.total_items = total_items
    
    @property
    def total_pages(self):
        return math.ceil(self.total_items / self.per_page)
    
    @property
    def has_next(self):
        return self.page < self.total_pages
    
    @property
    def has_prev(self):
        return self.page > 1
    
    @property
    def offset(self):
        return (self.page - 1) * self.per_page
    
    def next_url(self):
        return f"{self.base_url}?page={self.page + 1}&per_page={self.per_page}" if self.has_next else None
    
    def prev_url(self):
        return f"{self.base_url}?page={self.page - 1}&per_page={self.per_page}" if self.has_prev else None
    
    def to_dict(self):
        return {
            "page": self.page,
            "per_page": self.per_page,
            "total": self.total_items,
            "total_pages": self.total_pages,
            "next": self.next_url(),
            "prev": self.prev_url()
        }

Exercise 5.6:
def fetch_users():
    req = Request("https://jsonplaceholder.typicode.com/users")
    with urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode())

def fetch_user_posts(user_id):
    req = Request(f"https://jsonplaceholder.typicode.com/users/{user_id}/posts")
    with urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode())

def fetch_post_comments(post_id):
    req = Request(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    with urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode())

def display_user_summary():
    users = fetch_users()
    print("Users:")
    for user in users[:5]:
        print(f"  - {user['name']} ({user['email']})")
    
    if users:
        posts = fetch_user_posts(users[0]['id'])
        print(f"\\nPosts by {users[0]['name']}:")
        for post in posts[:3]:
            print(f"  - {post['title']}")
        
        if posts:
            comments = fetch_post_comments(posts[0]['id'])
            print(f"\\nComments on '{posts[0]['title']}':")
            for comment in comments[:2]:
                print(f"  - {comment['name']}: {comment['body'][:50]}...")
"""
