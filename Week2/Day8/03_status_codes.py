"""
Day 8 - HTTP Status Codes
=========================
Learn: Status codes and their meanings (200, 404, 500, etc.)

Key Concepts:
- Status codes indicate the result of an HTTP request
- Three-digit codes grouped by category
- Important for error handling and debugging
"""

# ========== STATUS CODE CATEGORIES ==========
print("=" * 60)
print("HTTP STATUS CODES OVERVIEW")
print("=" * 60)

print("""
📊 Status Code Categories:

┌───────────┬────────────────────────────────────────────┐
│   Range   │  Category                                  │
├───────────┼────────────────────────────────────────────┤
│  1xx      │  Informational - Request received          │
│  2xx      │  Success - Request successful              │
│  3xx      │  Redirection - Further action needed       │
│  4xx      │  Client Error - Problem with request       │
│  5xx      │  Server Error - Server failed              │
└───────────┴────────────────────────────────────────────┘
""")

# ========== 2XX SUCCESS CODES ==========
print("\n" + "=" * 60)
print("2XX - SUCCESS CODES")
print("=" * 60)

print("""
✅ 2XX Success Codes - Request was successful!

┌───────┬───────────────────┬────────────────────────────────────┐
│ Code  │ Status            │ Description                        │
├───────┼───────────────────┼────────────────────────────────────┤
│ 200   │ OK                │ Standard success response          │
│       │                   │ Used for: GET, PUT, PATCH          │
├───────┼───────────────────┼────────────────────────────────────┤
│ 201   │ Created           │ Resource created successfully      │
│       │                   │ Used for: POST                     │
├───────┼───────────────────┼────────────────────────────────────┤
│ 202   │ Accepted          │ Request accepted for processing    │
│       │                   │ Used for: Async operations         │
├───────┼───────────────────┼────────────────────────────────────┤
│ 204   │ No Content        │ Success but no body to return      │
│       │                   │ Used for: DELETE, some PUT         │
└───────┴───────────────────┴────────────────────────────────────┘
""")

# Python examples
print("📝 Python Code Patterns:")
print("-" * 50)

# Handling 200 OK
print("""
# Handling 200 OK
response = requests.get('/api/users')
if response.status_code == 200:
    users = response.json()
    print(f"Found {len(users)} users")
""")

# Handling 201 Created
print("""
# Handling 201 Created
response = requests.post('/api/users', json=user_data)
if response.status_code == 201:
    new_user = response.json()
    print(f"Created user with ID: {new_user['id']}")
""")

# Handling 204 No Content
print("""
# Handling 204 No Content
response = requests.delete('/api/users/123')
if response.status_code == 204:
    print("User deleted successfully")
""")

# ========== 3XX REDIRECTION CODES ==========
print("\n" + "=" * 60)
print("3XX - REDIRECTION CODES")
print("=" * 60)

print("""
↪️ 3XX Redirection Codes - Resource has moved!

┌───────┬────────────────────────┬─────────────────────────────────┐
│ Code  │ Status                 │ Description                     │
├───────┼────────────────────────┼─────────────────────────────────┤
│ 301   │ Moved Permanently      │ Resource permanently moved      │
│       │                        │ URL changed forever             │
├───────┼────────────────────────┼─────────────────────────────────┤
│ 302   │ Found (Temporary)      │ Temporarily at different URL    │
│       │                        │ Original URL may work later     │
├───────┼────────────────────────┼─────────────────────────────────┤
│ 304   │ Not Modified           │ Resource unchanged since cache  │
│       │                        │ Use cached version              │
├───────┼────────────────────────┼─────────────────────────────────┤
│ 307   │ Temporary Redirect     │ Similar to 302                  │
│       │                        │ Preserves HTTP method           │
├───────┼────────────────────────┼─────────────────────────────────┤
│ 308   │ Permanent Redirect     │ Similar to 301                  │
│       │                        │ Preserves HTTP method           │
└───────┴────────────────────────┴─────────────────────────────────┘
""")

print("""
📝 Redirection Headers:

HTTP/1.1 301 Moved Permanently
Location: https://new-url.com/page    ← Follow this URL

Browsers automatically follow redirects (up to a limit)
""")

# ========== 4XX CLIENT ERROR CODES ==========
print("\n" + "=" * 60)
print("4XX - CLIENT ERROR CODES")
print("=" * 60)

print("""
⚠️ 4XX Client Errors - Something wrong with the request!

┌───────┬─────────────────────┬───────────────────────────────────┐
│ Code  │ Status              │ Description & Common Cause        │
├───────┼─────────────────────┼───────────────────────────────────┤
│ 400   │ Bad Request         │ Invalid request syntax            │
│       │                     │ Missing required field            │
│       │                     │ Invalid data format               │
├───────┼─────────────────────┼───────────────────────────────────┤
│ 401   │ Unauthorized        │ Authentication required           │
│       │                     │ Invalid/expired token             │
│       │                     │ Missing credentials               │
├───────┼─────────────────────┼───────────────────────────────────┤
│ 403   │ Forbidden           │ Access denied (even if logged in) │
│       │                     │ No permission for resource        │
│       │                     │ Admin-only endpoint               │
├───────┼─────────────────────┼───────────────────────────────────┤
│ 404   │ Not Found           │ Resource doesn't exist            │
│       │                     │ Wrong URL                         │
│       │                     │ Deleted resource                  │
├───────┼─────────────────────┼───────────────────────────────────┤
│ 405   │ Method Not Allowed  │ HTTP method not supported         │
│       │                     │ POST to GET-only endpoint         │
├───────┼─────────────────────┼───────────────────────────────────┤
│ 409   │ Conflict            │ Resource state conflict           │
│       │                     │ Duplicate entry                   │
│       │                     │ Version conflict                  │
├───────┼─────────────────────┼───────────────────────────────────┤
│ 422   │ Unprocessable       │ Valid syntax but semantic error   │
│       │ Entity              │ Failed validation rules           │
├───────┼─────────────────────┼───────────────────────────────────┤
│ 429   │ Too Many Requests   │ Rate limit exceeded               │
│       │                     │ Too many API calls                │
└───────┴─────────────────────┴───────────────────────────────────┘
""")

# 401 vs 403 difference
print("🔐 401 vs 403 - What's the difference?")
print("-" * 50)
print("""
401 Unauthorized:
  - "Who are you? Please identify yourself."
  - Missing or invalid authentication
  - Solution: Log in or provide valid token

403 Forbidden:
  - "I know who you are, but you can't access this."
  - Authenticated but not authorized
  - Solution: Request higher permissions
""")

# ========== 5XX SERVER ERROR CODES ==========
print("\n" + "=" * 60)
print("5XX - SERVER ERROR CODES")
print("=" * 60)

print("""
💥 5XX Server Errors - Server failed to handle request!

┌───────┬───────────────────────┬─────────────────────────────────┐
│ Code  │ Status                │ Description                     │
├───────┼───────────────────────┼─────────────────────────────────┤
│ 500   │ Internal Server Error │ Generic server error            │
│       │                       │ Unhandled exception             │
│       │                       │ Bug in server code              │
├───────┼───────────────────────┼─────────────────────────────────┤
│ 501   │ Not Implemented       │ Server doesn't support method   │
│       │                       │ Feature not built yet           │
├───────┼───────────────────────┼─────────────────────────────────┤
│ 502   │ Bad Gateway           │ Invalid response from upstream  │
│       │                       │ Proxy/load balancer issue       │
├───────┼───────────────────────┼─────────────────────────────────┤
│ 503   │ Service Unavailable   │ Server temporarily unavailable  │
│       │                       │ Maintenance mode                │
│       │                       │ Server overloaded               │
├───────┼───────────────────────┼─────────────────────────────────┤
│ 504   │ Gateway Timeout       │ Upstream server took too long   │
│       │                       │ Request timed out               │
└───────┴───────────────────────┴─────────────────────────────────┘
""")

print("""
🚨 Important for Server Errors:
- Usually not the client's fault
- Retry after some time (with backoff)
- Check server logs for details
- May need server-side fix
""")

# ========== PRACTICAL ERROR HANDLING ==========
print("\n" + "=" * 60)
print("PRACTICAL ERROR HANDLING")
print("=" * 60)

# Demonstration of status code handling
def handle_response(status_code, response_body=None):
    """
    Handle different HTTP status codes appropriately
    """
    handlers = {
        # Success codes
        200: lambda: print("✅ Success! Data retrieved."),
        201: lambda: print("✅ Resource created successfully!"),
        204: lambda: print("✅ Success! No content to return."),
        
        # Redirection
        301: lambda: print("↪️ Resource moved permanently. Update your bookmark."),
        302: lambda: print("↪️ Resource temporarily moved."),
        304: lambda: print("📦 Using cached version."),
        
        # Client errors
        400: lambda: print("❌ Bad Request - Check your data format."),
        401: lambda: print("🔐 Unauthorized - Please log in."),
        403: lambda: print("🚫 Forbidden - You don't have permission."),
        404: lambda: print("🔍 Not Found - Resource doesn't exist."),
        405: lambda: print("❌ Method Not Allowed - Use different HTTP method."),
        409: lambda: print("⚠️ Conflict - Resource already exists."),
        422: lambda: print("❌ Validation Error - Check required fields."),
        429: lambda: print("⏱️ Too Many Requests - Slow down!"),
        
        # Server errors
        500: lambda: print("💥 Server Error - Not your fault, try again later."),
        502: lambda: print("🌐 Bad Gateway - Server communication issue."),
        503: lambda: print("🔧 Service Unavailable - Under maintenance."),
        504: lambda: print("⏰ Gateway Timeout - Server took too long."),
    }
    
    handler = handlers.get(status_code, lambda: print(f"Unknown status: {status_code}"))
    handler()
    return status_code // 100  # Return category (2, 3, 4, or 5)

print("📝 Testing Status Code Handler:")
print("-" * 50)

test_codes = [200, 201, 301, 400, 401, 403, 404, 500, 503]
for code in test_codes:
    print(f"\nStatus {code}:", end=" ")
    handle_response(code)

# ========== REAL-WORLD ERROR HANDLING ==========
print("\n" + "=" * 60)
print("REAL-WORLD ERROR HANDLING PATTERN")
print("=" * 60)

print("""
📝 Recommended Error Handling Pattern:

```python
import requests

def make_api_request(url, method='GET', data=None):
    try:
        if method == 'GET':
            response = requests.get(url, timeout=10)
        elif method == 'POST':
            response = requests.post(url, json=data, timeout=10)
        
        # Check for successful response
        if response.status_code >= 200 and response.status_code < 300:
            return {'success': True, 'data': response.json()}
        
        # Handle client errors
        elif response.status_code >= 400 and response.status_code < 500:
            error_messages = {
                400: 'Invalid request data',
                401: 'Please log in again',
                403: 'Access denied',
                404: 'Resource not found',
                422: 'Validation failed',
                429: 'Too many requests, wait and retry'
            }
            msg = error_messages.get(response.status_code, 'Client error')
            return {'success': False, 'error': msg, 'code': response.status_code}
        
        # Handle server errors
        elif response.status_code >= 500:
            return {'success': False, 'error': 'Server error, try again later',
                    'code': response.status_code}
    
    except requests.exceptions.Timeout:
        return {'success': False, 'error': 'Request timed out'}
    except requests.exceptions.ConnectionError:
        return {'success': False, 'error': 'Could not connect to server'}
    except Exception as e:
        return {'success': False, 'error': str(e)}
```
""")

# ========== COMMON STATUS CODE CHEAT SHEET ==========
print("\n" + "=" * 60)
print("QUICK REFERENCE CHEAT SHEET")
print("=" * 60)

print("""
🎯 Most Important Status Codes to Remember:

SUCCESS:
  200 OK              → Everything worked
  201 Created         → New resource created (POST)
  204 No Content      → Success, nothing to return (DELETE)

CLIENT ERRORS:
  400 Bad Request     → You sent bad data
  401 Unauthorized    → Need to log in
  403 Forbidden       → No permission
  404 Not Found       → Resource doesn't exist
  422 Unprocessable   → Validation failed
  429 Too Many        → Rate limited

SERVER ERRORS:
  500 Internal Error  → Server broke
  502 Bad Gateway     → Upstream issue
  503 Unavailable     → Server down/maintenance
  504 Timeout         → Server too slow

PRO TIP: 
- 2xx = 😊 Success
- 4xx = 🤔 You did something wrong
- 5xx = 😱 Server did something wrong
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - Testing Status Codes")
print("=" * 60)

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# Using httpbin.org to test different status codes
test_endpoints = [
    ("https://httpbin.org/status/200", "200 OK"),
    ("https://httpbin.org/status/201", "201 Created"),
    ("https://httpbin.org/status/400", "400 Bad Request"),
    ("https://httpbin.org/status/404", "404 Not Found"),
    ("https://httpbin.org/status/500", "500 Server Error"),
]

print("🧪 Testing different status codes with httpbin.org:\n")

for url, description in test_endpoints:
    try:
        req = Request(url)
        with urlopen(req, timeout=5) as response:
            print(f"✅ {description}: Received status {response.status}")
    except HTTPError as e:
        print(f"⚠️ {description}: Received status {e.code}")
    except URLError as e:
        print(f"❌ {description}: Connection error - {e.reason}")
    except Exception as e:
        print(f"❌ {description}: Error - {e}")

print("\n" + "=" * 60)
print("✅ HTTP Status Codes - Complete!")
print("=" * 60)
