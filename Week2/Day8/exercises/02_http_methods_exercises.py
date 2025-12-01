"""
Day 8 - Exercise 2: HTTP Methods Exercises
==========================================
Practice using different HTTP methods
"""

print("=" * 60)
print("Exercise 2: HTTP Methods")
print("=" * 60)

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# ============================================================
# Exercise 2.1: Identify the Correct Method
# ============================================================

print("\n📝 Exercise 2.1: Identify the Correct HTTP Method")
print("-" * 50)
print("""
For each scenario, identify which HTTP method should be used:

1. Fetching a user's profile information
2. Creating a new blog post
3. Updating a user's email address only
4. Replacing an entire product listing
5. Removing a comment from a post
6. Getting a list of all products
7. Submitting a login form
8. Changing the password of a user

Write your answers below as comments:
""")

# TODO: Write the correct HTTP method for each:
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# 6. 
# 7. 
# 8. 

# ============================================================
# Exercise 2.2: Design API Endpoints
# ============================================================

print("\n📝 Exercise 2.2: Design RESTful API Endpoints")
print("-" * 50)
print("""
Design RESTful endpoints for a Book Library API.
Define the method and URL path for each operation:

Operations needed:
1. Get all books
2. Get a specific book by ID
3. Add a new book
4. Update a book's information completely
5. Update only the book's availability status
6. Delete a book
7. Get all books by a specific author
8. Get all reviews for a specific book
9. Add a review to a book

Write your endpoint designs below:
""")

# TODO: Design the endpoints
# Example format: METHOD /path

# 1. Get all books:           
# 2. Get specific book:       
# 3. Add new book:           
# 4. Update entire book:     
# 5. Update availability:    
# 6. Delete book:            
# 7. Books by author:        
# 8. Reviews for book:       
# 9. Add review:             

# ============================================================
# Exercise 2.3: Make HTTP Requests
# ============================================================

print("\n📝 Exercise 2.3: Make HTTP Requests")
print("-" * 50)
print("""
Complete the functions below to make HTTP requests to httpbin.org
(a free HTTP testing service).
""")

def make_get_request(url):
    """
    Make a GET request and return the response data.
    Handle errors gracefully.
    """
    # TODO: Implement GET request
    pass

def make_post_request(url, data):
    """
    Make a POST request with JSON data and return the response.
    Handle errors gracefully.
    """
    # TODO: Implement POST request
    pass

def make_put_request(url, data):
    """
    Make a PUT request with JSON data and return the response.
    Handle errors gracefully.
    """
    # TODO: Implement PUT request
    pass

def make_delete_request(url):
    """
    Make a DELETE request and return the status.
    Handle errors gracefully.
    """
    # TODO: Implement DELETE request
    pass

# Test your functions:
# print("GET:", make_get_request("https://httpbin.org/get"))
# print("POST:", make_post_request("https://httpbin.org/post", {"name": "John"}))
# print("PUT:", make_put_request("https://httpbin.org/put", {"name": "John Updated"}))
# print("DELETE:", make_delete_request("https://httpbin.org/delete"))

# ============================================================
# Exercise 2.4: Request Headers
# ============================================================

print("\n📝 Exercise 2.4: Custom Request Headers")
print("-" * 50)
print("""
Create a function that makes a request with custom headers.
The function should:
1. Accept a URL, method, and headers dictionary
2. Make the request with those headers
3. Return the response including the headers the server received

Test by sending these headers:
- User-Agent: MyApp/1.0
- X-Custom-Header: my-value
- Accept-Language: en-US
""")

def make_request_with_headers(url, method='GET', headers=None, data=None):
    """
    Make an HTTP request with custom headers.
    Returns the response data including what headers the server received.
    """
    # TODO: Implement this function
    pass

# Test your function:
# custom_headers = {
#     'User-Agent': 'MyApp/1.0',
#     'X-Custom-Header': 'my-value',
#     'Accept-Language': 'en-US'
# }
# result = make_request_with_headers("https://httpbin.org/headers", headers=custom_headers)
# print(result)

# ============================================================
# Exercise 2.5: CRUD Operations Simulation
# ============================================================

print("\n📝 Exercise 2.5: CRUD Operations Simulation")
print("-" * 50)
print("""
Simulate a complete CRUD workflow for a "Task" resource using httpbin.org.
1. Create a new task (POST)
2. Read the task (GET)
3. Update the task (PUT)
4. Partially update the task (PATCH)
5. Delete the task (DELETE)

Print the status and result of each operation.
""")

def simulate_crud_workflow():
    """
    Simulate complete CRUD operations for a Task resource.
    """
    base_url = "https://httpbin.org"
    
    # TODO: Implement CRUD workflow
    # 1. CREATE (POST)
    print("Creating task...")
    
    # 2. READ (GET)
    print("Reading task...")
    
    # 3. UPDATE (PUT)
    print("Updating task...")
    
    # 4. PARTIAL UPDATE (PATCH)
    print("Partially updating task...")
    
    # 5. DELETE
    print("Deleting task...")

# Run the simulation:
# simulate_crud_workflow()

print("\n" + "=" * 60)
print("✅ Complete the exercises above!")
print("=" * 60)

"""
SOLUTIONS:

Exercise 2.1:
1. GET
2. POST
3. PATCH
4. PUT
5. DELETE
6. GET
7. POST
8. PATCH (or PUT if changing entire credentials)

Exercise 2.2:
1. GET /books
2. GET /books/{id}
3. POST /books
4. PUT /books/{id}
5. PATCH /books/{id}
6. DELETE /books/{id}
7. GET /books?author={author_name} or GET /authors/{id}/books
8. GET /books/{id}/reviews
9. POST /books/{id}/reviews

Exercise 2.3:
def make_get_request(url):
    try:
        req = Request(url)
        with urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except (HTTPError, URLError) as e:
        return {"error": str(e)}

def make_post_request(url, data):
    try:
        req = Request(url, data=json.dumps(data).encode(), 
                     headers={'Content-Type': 'application/json'}, method='POST')
        with urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except (HTTPError, URLError) as e:
        return {"error": str(e)}

# Similar implementations for PUT and DELETE...

Exercise 2.4:
def make_request_with_headers(url, method='GET', headers=None, data=None):
    try:
        req_data = json.dumps(data).encode() if data else None
        req = Request(url, data=req_data, method=method)
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)
        with urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except (HTTPError, URLError) as e:
        return {"error": str(e)}

Exercise 2.5:
def simulate_crud_workflow():
    base_url = "https://httpbin.org"
    
    # CREATE
    task = {"title": "Learn HTTP", "done": False}
    result = make_post_request(f"{base_url}/post", task)
    print(f"Created: {result.get('json', {})}")
    
    # READ
    result = make_get_request(f"{base_url}/get")
    print(f"Read successful: {result.get('url', '')}")
    
    # UPDATE
    updated_task = {"title": "Learn HTTP Methods", "done": True}
    result = make_put_request(f"{base_url}/put", updated_task)
    print(f"Updated: {result.get('json', {})}")
    
    # DELETE
    result = make_delete_request(f"{base_url}/delete")
    print(f"Deleted successfully")
"""
