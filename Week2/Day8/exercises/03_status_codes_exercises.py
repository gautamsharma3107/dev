"""
Day 8 - Exercise 3: Status Codes Exercises
==========================================
Practice understanding and handling HTTP status codes
"""

print("=" * 60)
print("Exercise 3: HTTP Status Codes")
print("=" * 60)

# ============================================================
# Exercise 3.1: Identify Status Codes
# ============================================================

print("\n📝 Exercise 3.1: Identify Status Codes")
print("-" * 50)
print("""
Match each scenario with the appropriate HTTP status code:

Scenarios:
1. User successfully logged in
2. New blog post was created
3. Page not found
4. User tried to access admin page without permission
5. Server crashed due to a bug
6. User submitted invalid form data
7. Resource was deleted successfully (no content returned)
8. API rate limit exceeded
9. User needs to authenticate first
10. Request successful, redirecting to new URL

Write the correct status code for each:
""")

# TODO: Write the status codes
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# 6. 
# 7. 
# 8. 
# 9. 
# 10. 

# ============================================================
# Exercise 3.2: Status Code Handler
# ============================================================

print("\n📝 Exercise 3.2: Build a Status Code Handler")
print("-" * 50)
print("""
Create a function that takes an HTTP status code and returns:
- The status category (Success, Redirect, Client Error, Server Error)
- A user-friendly message explaining what happened
- Whether the request should be retried

Example output:
handle_status(200) -> {
    "category": "Success",
    "message": "Request successful",
    "retry": False
}
""")

def handle_status(status_code):
    """
    Handle HTTP status code and return appropriate information.
    
    Returns:
        dict with 'category', 'message', and 'retry' keys
    """
    # TODO: Implement this function
    # Consider these status codes: 200, 201, 204, 301, 302, 400, 401, 403, 404, 
    # 409, 429, 500, 502, 503
    pass

# Test your function:
test_codes = [200, 201, 204, 301, 400, 401, 403, 404, 429, 500, 503]
# for code in test_codes:
#     result = handle_status(code)
#     print(f"{code}: {result}")

# ============================================================
# Exercise 3.3: Error Response Parser
# ============================================================

print("\n📝 Exercise 3.3: Parse Error Responses")
print("-" * 50)
print("""
Create a function that parses API error responses and extracts
useful information for debugging.

Sample error responses to handle:

1. {"error": "Invalid email format", "field": "email"}
2. {"message": "Not found", "status": 404}
3. {"errors": [{"field": "name", "message": "Required"}, {"field": "email", "message": "Invalid"}]}
4. {"detail": "Authentication credentials were not provided."}
5. Plain text: "Internal Server Error"
""")

def parse_error_response(response, status_code):
    """
    Parse various error response formats.
    
    Returns:
        dict with 'status', 'main_message', and 'details' keys
    """
    # TODO: Implement this function
    # Handle different response formats (dict, list of errors, plain text)
    pass

# Test cases:
# test_responses = [
#     ({"error": "Invalid email format", "field": "email"}, 400),
#     ({"message": "Not found", "status": 404}, 404),
#     ({"errors": [{"field": "name", "message": "Required"}]}, 422),
#     ({"detail": "Authentication required"}, 401),
#     ("Internal Server Error", 500)
# ]
# 
# for response, code in test_responses:
#     result = parse_error_response(response, code)
#     print(f"Status {code}: {result}")

# ============================================================
# Exercise 3.4: Retry Logic
# ============================================================

print("\n📝 Exercise 3.4: Implement Retry Logic")
print("-" * 50)
print("""
Create a function that makes an HTTP request with retry logic.
- Retry on 5xx errors (server errors) up to 3 times
- Retry on 429 (rate limit) after waiting
- Don't retry on 4xx errors (client errors)
- Use exponential backoff between retries
""")

import time

def make_request_with_retry(url, max_retries=3):
    """
    Make HTTP request with intelligent retry logic.
    
    Args:
        url: URL to request
        max_retries: Maximum number of retry attempts
        
    Returns:
        Response data or error information
    """
    # TODO: Implement retry logic
    # Use time.sleep() for delays between retries
    # Implement exponential backoff (1s, 2s, 4s)
    pass

# Test with httpbin status endpoints:
# print(make_request_with_retry("https://httpbin.org/status/200"))
# print(make_request_with_retry("https://httpbin.org/status/500"))
# print(make_request_with_retry("https://httpbin.org/status/404"))

# ============================================================
# Exercise 3.5: Status Code Quiz
# ============================================================

print("\n📝 Exercise 3.5: Status Code Quiz")
print("-" * 50)
print("""
Answer these questions:

1. What's the difference between 401 and 403?

2. When would you use 201 instead of 200?

3. Why is 204 commonly used with DELETE?

4. What does the Retry-After header mean with 429?

5. When might you see a 502 Bad Gateway error?

Write your answers as comments below:
""")

# TODO: Write your answers
# 1. 401 vs 403:
#
# 2. 201 vs 200:
#
# 3. 204 with DELETE:
#
# 4. Retry-After with 429:
#
# 5. 502 Bad Gateway:
#

print("\n" + "=" * 60)
print("✅ Complete the exercises above!")
print("=" * 60)

"""
SOLUTIONS:

Exercise 3.1:
1. 200 OK
2. 201 Created
3. 404 Not Found
4. 403 Forbidden
5. 500 Internal Server Error
6. 400 Bad Request
7. 204 No Content
8. 429 Too Many Requests
9. 401 Unauthorized
10. 301 or 302 (Redirect)

Exercise 3.2:
def handle_status(status_code):
    handlers = {
        200: {"category": "Success", "message": "Request successful", "retry": False},
        201: {"category": "Success", "message": "Resource created", "retry": False},
        204: {"category": "Success", "message": "No content", "retry": False},
        301: {"category": "Redirect", "message": "Permanently moved", "retry": False},
        400: {"category": "Client Error", "message": "Bad request data", "retry": False},
        401: {"category": "Client Error", "message": "Authentication required", "retry": False},
        403: {"category": "Client Error", "message": "Access forbidden", "retry": False},
        404: {"category": "Client Error", "message": "Resource not found", "retry": False},
        429: {"category": "Client Error", "message": "Rate limit exceeded", "retry": True},
        500: {"category": "Server Error", "message": "Server error", "retry": True},
        503: {"category": "Server Error", "message": "Service unavailable", "retry": True}
    }
    return handlers.get(status_code, {"category": "Unknown", "message": "Unknown status", "retry": False})

Exercise 3.3:
def parse_error_response(response, status_code):
    result = {"status": status_code, "main_message": "", "details": []}
    
    if isinstance(response, str):
        result["main_message"] = response
    elif isinstance(response, dict):
        if "error" in response:
            result["main_message"] = response["error"]
            if "field" in response:
                result["details"].append(f"Field: {response['field']}")
        elif "message" in response:
            result["main_message"] = response["message"]
        elif "detail" in response:
            result["main_message"] = response["detail"]
        elif "errors" in response:
            result["main_message"] = "Multiple errors"
            result["details"] = [f"{e['field']}: {e['message']}" for e in response["errors"]]
    
    return result

Exercise 3.4:
def make_request_with_retry(url, max_retries=3):
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError
    
    for attempt in range(max_retries + 1):
        try:
            req = Request(url)
            with urlopen(req, timeout=10) as response:
                return {"status": response.status, "success": True}
        except HTTPError as e:
            if e.code >= 500 or e.code == 429:
                if attempt < max_retries:
                    delay = 2 ** attempt  # Exponential backoff
                    time.sleep(delay)
                    continue
            return {"status": e.code, "success": False, "retry_attempted": attempt}
        except URLError as e:
            return {"error": str(e), "success": False}
    
    return {"error": "Max retries exceeded", "success": False}

Exercise 3.5:
1. 401 = Not authenticated (who are you?), 403 = Not authorized (you can't do this)
2. 201 when a new resource is created (POST), 200 for general success (GET, PUT)
3. 204 = success but nothing to return; DELETE usually doesn't need to return the deleted data
4. Retry-After tells the client how long to wait before making another request
5. 502 occurs when a proxy/load balancer can't get a valid response from the upstream server
"""
