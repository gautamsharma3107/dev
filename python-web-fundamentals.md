# Web Fundamentals: Complete Guide

---

## Table of Contents
1. [Introduction to Web](#introduction-to-web)
2. [HTTP Protocol](#http-protocol)
3. [HTTP Methods](#http-methods)
4. [Status Codes](#status-codes)
5. [Headers](#headers)
6. [Cookies and Sessions](#cookies-and-sessions)
7. [Request and Response Structure](#request-and-response-structure)
8. [RESTful API Concepts](#restful-api-concepts)
9. [REST Principles](#rest-principles)
10. [API Design Best Practices](#api-design-best-practices)
11. [Data Formats](#data-formats)
12. [Practical Examples](#practical-examples)
13. [Practice Exercises](#practice-exercises)

---

## Introduction to Web

### How the Web Works

```
Client (Browser/App)
       ↓
    Request (HTTP)
       ↓
    Server
       ↓
   Response (HTTP)
       ↓
Client (Browser/App)
```

### Key Concepts

1. **Client** - User's browser or application
2. **Server** - Backend application hosting data
3. **HTTP** - Communication protocol
4. **Request** - Client asks server for something
5. **Response** - Server sends data back to client
6. **Stateless** - Each request is independent

---

## HTTP Protocol

### What is HTTP?

HTTP (HyperText Transfer Protocol) is the protocol for transferring data on the web.

### HTTP Versions

```
HTTP/1.0
- Simple but inefficient
- One connection per request

HTTP/1.1 (Standard)
- Keep-alive connections
- Better performance
- Most common

HTTP/2
- Multiplexing
- Header compression
- Better performance

HTTP/3
- QUIC protocol
- Faster, more reliable
- Latest version
```

### HTTP vs HTTPS

```
HTTP
- Plain text communication
- Insecure
- Port 80

HTTPS
- Encrypted communication (SSL/TLS)
- Secure
- Port 443
- Certificates required
- Modern standard
```

---

## HTTP Methods

### GET (Retrieve Data)

```
Purpose: Fetch data from server
Safe: Yes (doesn't modify data)
Idempotent: Yes (same result each time)
Body: Usually no
Cacheable: Yes

Example:
GET /users HTTP/1.1
Host: api.example.com
```

### POST (Create Data)

```
Purpose: Create new resource
Safe: No (modifies data)
Idempotent: No (each request creates new resource)
Body: Yes (required)
Cacheable: No

Example:
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "name": "Alice",
  "email": "alice@example.com"
}
```

### PUT (Replace Entire Resource)

```
Purpose: Replace entire resource
Safe: No (modifies data)
Idempotent: Yes (same result each time)
Body: Yes (required)
Cacheable: No

Example:
PUT /users/1 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "name": "Alice Updated",
  "email": "alice.new@example.com"
}
```

### DELETE (Remove Resource)

```
Purpose: Delete resource
Safe: No (modifies data)
Idempotent: Yes (deleting twice has same effect)
Body: Usually no
Cacheable: No

Example:
DELETE /users/1 HTTP/1.1
Host: api.example.com
```

### PATCH (Partial Update)

```
Purpose: Partially update resource
Safe: No (modifies data)
Idempotent: No (depends on implementation)
Body: Yes (partial data)
Cacheable: No

Example:
PATCH /users/1 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "email": "alice.new@example.com"
}
```

### Other Methods

```
HEAD
- Like GET but only returns headers
- No response body

OPTIONS
- Describes communication options
- Used for CORS preflight

TRACE
- Debug request journey
- Not commonly used
```

### Method Comparison

```
Method   | Safe | Idempotent | Cacheable | Use Case
---------|------|------------|-----------|------------------
GET      | Yes  | Yes        | Yes       | Retrieve data
POST     | No   | No         | No        | Create resource
PUT      | No   | Yes        | No        | Replace resource
DELETE   | No   | Yes        | No        | Delete resource
PATCH    | No   | No         | No        | Partial update
HEAD     | Yes  | Yes        | Yes       | Get headers only
OPTIONS  | Yes  | Yes        | No        | Describe options
```

---

## Status Codes

### 2xx Success

```
200 OK
- Request succeeded
- Data returned in response body

201 Created
- Resource successfully created
- Location header contains new resource URL

202 Accepted
- Request accepted for processing
- Result not ready yet

204 No Content
- Request succeeded
- No content to return (often for DELETE, PATCH)

206 Partial Content
- Only part of response body sent
- Used for resumable downloads
```

### 3xx Redirection

```
301 Moved Permanently
- Resource moved to new location
- Use new URL for future requests

302 Found
- Temporary redirect
- Use original URL in future

304 Not Modified
- Resource hasn't changed
- Client can use cached version

307 Temporary Redirect
- Similar to 302
- Preserve HTTP method
```

### 4xx Client Error

```
400 Bad Request
- Invalid request syntax
- Client's fault

401 Unauthorized
- Authentication required
- Missing or invalid credentials

403 Forbidden
- Authenticated but not authorized
- Insufficient permissions

404 Not Found
- Resource doesn't exist
- Common for invalid URLs

405 Method Not Allowed
- Valid URL but method not allowed

409 Conflict
- Request conflicts with current state
- Often used for version conflicts

422 Unprocessable Entity
- Request format correct but data invalid
- Semantic error

429 Too Many Requests
- Rate limit exceeded
- Wait before retrying
```

### 5xx Server Error

```
500 Internal Server Error
- Generic server error
- Something went wrong

501 Not Implemented
- Server doesn't support request method

502 Bad Gateway
- Gateway/proxy error
- Server behind gateway not responding

503 Service Unavailable
- Server temporarily unavailable
- Maintenance or overloaded

504 Gateway Timeout
- Gateway timeout waiting for response
```

### Status Code Categories

```
1xx (100-199) - Informational
- Request received, waiting for action

2xx (200-299) - Success
- Request succeeded

3xx (300-399) - Redirection
- Further action needed

4xx (400-499) - Client Error
- Request invalid or cannot be processed

5xx (500-599) - Server Error
- Server failed to fulfill request
```

---

## Headers

### Request Headers

```
Common Request Headers:

Host
- Domain name being requested
- Host: api.example.com

User-Agent
- Client information
- User-Agent: Mozilla/5.0

Accept
- Types of data client accepts
- Accept: application/json

Accept-Language
- Preferred languages
- Accept-Language: en-US, fr

Content-Type
- Type of data being sent
- Content-Type: application/json

Content-Length
- Size of request body
- Content-Length: 1024

Authorization
- Authentication credentials
- Authorization: Bearer token123

Cookie
- Session cookies
- Cookie: session_id=abc123
```

### Response Headers

```
Common Response Headers:

Content-Type
- Type of data in response
- Content-Type: application/json

Content-Length
- Size of response body
- Content-Length: 2048

Content-Encoding
- Encoding applied to body
- Content-Encoding: gzip

Cache-Control
- Caching instructions
- Cache-Control: max-age=3600

Expires
- When response expires
- Expires: Wed, 21 Oct 2025 07:28:00 GMT

Set-Cookie
- Set client cookies
- Set-Cookie: session_id=xyz789; Path=/; HttpOnly

Location
- URL for redirects
- Location: /users/123

Access-Control-Allow-Origin
- CORS - which origins allowed
- Access-Control-Allow-Origin: *

ETag
- Resource version
- ETag: "33a64df"

Last-Modified
- When resource last updated
- Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
```

### Custom Headers

```
X-Custom-Header
- Application-specific header
- X-API-Version: 1.0
- X-Request-ID: req123456
```

---

## Cookies and Sessions

### What are Cookies?

Cookies are small files stored on client to maintain state.

```
Cookie Structure:
Name=Value; Path=/; Domain=.example.com; Expires=...; HttpOnly; Secure
```

### Cookie Types

```
Session Cookies
- Stored in memory
- Deleted when browser closes
- No expiration date

Persistent Cookies
- Stored on disk
- Survive browser restart
- Have expiration date

First-Party Cookies
- Set by visited domain
- Usually for authentication

Third-Party Cookies
- Set by different domain
- Used for tracking/ads
```

### Cookie Attributes

```
Path=/
- Cookie only sent for paths starting with /

Domain=.example.com
- Cookie sent to all subdomains

Expires=date
- When cookie expires

Max-Age=seconds
- Seconds until expiration (overrides Expires)

HttpOnly
- Cannot be accessed by JavaScript
- Only sent over HTTP
- More secure

Secure
- Only sent over HTTPS
- Not sent over plain HTTP

SameSite=Strict|Lax|None
- Protection against CSRF
- Strict: Only same-site requests
- Lax: Top-level navigations allowed
- None: All requests (needs Secure flag)
```

### What are Sessions?

Sessions maintain state across multiple requests.

```
Session Flow:

1. Client sends credentials
   ↓
2. Server creates session
   ↓
3. Server sends session ID in cookie
   ↓
4. Client stores session cookie
   ↓
5. Client sends session ID with each request
   ↓
6. Server validates session
   ↓
7. Repeat requests 5-6 as needed
```

### Session Storage

```
Session Storage Options:

Memory
- Fast
- Lost on server restart
- Single server only

Database
- Persistent
- Slower than memory
- Shared across servers

Redis
- Fast
- Persistent
- Shared across servers
```

---

## Request and Response Structure

### HTTP Request Structure

```
Request Line (Method URL HTTP-Version)
GET /users/1 HTTP/1.1

Headers
Host: api.example.com
Accept: application/json
Authorization: Bearer token123

Blank Line

Body (optional)
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

### HTTP Response Structure

```
Status Line (HTTP-Version Status-Code Reason)
HTTP/1.1 200 OK

Headers
Content-Type: application/json
Content-Length: 256
Cache-Control: max-age=3600

Blank Line

Body
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```

### Example: POST Request

```
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: 45
Authorization: Bearer token123
X-Request-ID: req-123456

{"name": "Alice", "email": "alice@example.com"}
```

### Example: Response

```
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 78
Location: /api/users/1
X-Request-ID: req-123456

{"id": 1, "name": "Alice", "email": "alice@example.com", "created": true}
```

---

## RESTful API Concepts

### What is REST?

REST (Representational State Transfer) is architectural style for building web APIs.

### REST Principles

```
1. Client-Server Architecture
   - Clear separation between client and server
   - Independent evolution

2. Statelessness
   - Each request contains all information
   - Server doesn't store client context
   - Enables scalability

3. Uniform Interface
   - Consistent, predictable API
   - Resources identified by URIs
   - Resources manipulated via HTTP methods

4. Resource-Based URLs
   - URLs represent nouns (resources)
   - Not verbs (actions)
   - /users (resource) not /getUsers (verb)

5. Cacheable
   - Responses marked as cacheable
   - Improves performance
   - Reduces server load

6. Layered System
   - Client doesn't know if connected directly
   - Can have intermediaries (caches, proxies)
   - Transparent to client
```

### Resource-Based URLs

```
✓ GOOD (RESTful)
GET /users           → Get all users
GET /users/1         → Get user with ID 1
POST /users          → Create new user
PUT /users/1         → Replace user 1
DELETE /users/1      → Delete user 1

✗ BAD (RPC-style)
GET /getUsers        → Get all users
GET /getUser?id=1    → Get user 1
POST /createUser     → Create user
POST /updateUser     → Update user
POST /deleteUser     → Delete user
```

### CRUD Mapping to HTTP

```
CRUD Operation  | HTTP Method | URL           | Response
----------------|-------------|---------------|----------
Create          | POST        | /users        | 201 Created
Read            | GET         | /users/1      | 200 OK
Update          | PUT/PATCH   | /users/1      | 200 OK
Delete          | DELETE      | /users/1      | 204 No Content
List all        | GET         | /users        | 200 OK with array
```

### Nested Resources

```
GET /users/1/posts
- Get all posts by user 1

GET /users/1/posts/5
- Get post 5 by user 1

POST /users/1/posts
- Create post for user 1

PUT /users/1/posts/5
- Update post 5 for user 1

DELETE /users/1/posts/5
- Delete post 5 from user 1
```

---

## API Design Best Practices

### URL Design

```
✓ GOOD
/api/v1/users              → Use versioning
/api/v1/users/1            → Use IDs not names
/api/v1/users/1/posts      → Nest related resources
/api/v1/users?page=1&limit=10  → Pagination parameters

✗ BAD
/api/users/alice           → Names not IDs
/api/getUsers              → Verbs in URLs
/api/users/1/getUserPosts  → Complex nesting
/users?skip=0&take=10      → Confusing pagination
```

### Request/Response Format

```
✓ GOOD - Always return JSON
{
  "data": {
    "id": 1,
    "name": "Alice"
  },
  "status": "success"
}

✓ GOOD - Consistent error response
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User with ID 1 not found"
  },
  "status": "error"
}
```

### Pagination

```
✓ GOOD
/api/users?page=1&limit=10

Response:
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 100,
    "pages": 10
  }
}
```

### Filtering and Sorting

```
✓ GOOD
/api/users?status=active&sort=-created_at

✓ GOOD
/api/users?filter[status]=active&sort=-created_at
```

### Versioning

```
URL Versioning (Most common)
/api/v1/users
/api/v2/users

Header Versioning
Accept: application/vnd.api+json;version=1

Parameter Versioning
/api/users?version=1
```

### Error Handling

```
✓ GOOD - Consistent error responses
Status: 404
{
  "error": {
    "code": "NOT_FOUND",
    "message": "User not found"
  }
}

Status: 400
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": {
      "email": "Invalid email format"
    }
  }
}

Status: 500
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An error occurred"
  }
}
```

### Rate Limiting

```
Headers indicate rate limits:
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1609459200

Return 429 when limit exceeded:
HTTP/1.1 429 Too Many Requests
```

---

## Data Formats

### JSON (JavaScript Object Notation)

```
// Most common for APIs
{
  "name": "Alice",
  "age": 25,
  "email": "alice@example.com",
  "active": true,
  "roles": ["admin", "user"],
  "metadata": {
    "created": "2025-01-01",
    "updated": "2025-01-15"
  }
}

Data Types:
- String: "value"
- Number: 42, 3.14
- Boolean: true, false
- Array: [1, 2, 3]
- Object: {"key": "value"}
- Null: null
```

### XML (eXtensible Markup Language)

```
<!-- Older format, less common now -->
<?xml version="1.0" encoding="UTF-8"?>
<user>
  <name>Alice</name>
  <age>25</age>
  <email>alice@example.com</email>
  <active>true</active>
  <roles>
    <role>admin</role>
    <role>user</role>
  </roles>
</user>
```

### URL Encoding

```
Used in:
- Form data submissions
- Query parameters
- URL paths

Encoding rules:
Space → + or %20
Special chars: %[hex code]

Examples:
"Hello World" → Hello+World or Hello%20World
"name@email.com" → name%40email.com
"user/1" → user%2F1

Python encoding:
from urllib.parse import urlencode, quote

data = {"name": "Alice", "age": 25}
encoded = urlencode(data)
# Result: name=Alice&age=25

url_safe = quote("Hello World")
# Result: Hello%20World
```

### Multipart Form Data

```
Used for file uploads and complex form data

Format:
Content-Type: multipart/form-data; boundary=----boundary123

------boundary123
Content-Disposition: form-data; name="username"

Alice
------boundary123
Content-Disposition: form-data; name="email"

alice@example.com
------boundary123
Content-Disposition: form-data; name="avatar"; filename="avatar.jpg"
Content-Type: image/jpeg

[binary file content]
------boundary123--
```

### Content-Type Header

```
application/json
- JSON data (most common for APIs)

application/x-www-form-urlencoded
- Form data (URL encoded)

multipart/form-data
- Form with file uploads

application/xml
- XML data

text/plain
- Plain text

text/html
- HTML content

image/jpeg, image/png, image/gif
- Image files

application/pdf
- PDF files

video/mp4
- Video files
```

---

## Practical Examples

### Python HTTP Request Example

```python
import requests
import json

# GET request
response = requests.get('https://api.example.com/users/1')
print(response.status_code)  # 200
data = response.json()       # Parse JSON

# POST request
data = {'name': 'Alice', 'email': 'alice@example.com'}
response = requests.post(
    'https://api.example.com/users',
    json=data,
    headers={'Authorization': 'Bearer token123'}
)
print(response.json())

# PUT request
data = {'name': 'Alice Updated'}
response = requests.put(
    'https://api.example.com/users/1',
    json=data
)

# DELETE request
response = requests.delete('https://api.example.com/users/1')

# Error handling
try:
    response = requests.get('https://api.example.com/users/999')
    response.raise_for_status()  # Raise for 4xx/5xx
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### Session Management Example

```python
import requests

# Using sessions for multiple requests
session = requests.Session()

# Login
login_data = {'username': 'alice', 'password': 'password123'}
response = session.post(
    'https://api.example.com/login',
    json=login_data
)

# Session cookie automatically managed
# Make subsequent requests
response = session.get('https://api.example.com/profile')
print(response.json())

# Logout
session.post('https://api.example.com/logout')
```

### REST API Design Example

```
API Endpoints for Blog Application:

Users:
GET    /api/v1/users              → List all users
POST   /api/v1/users              → Create user
GET    /api/v1/users/1            → Get user 1
PUT    /api/v1/users/1            → Update user 1
DELETE /api/v1/users/1            → Delete user 1

Posts:
GET    /api/v1/users/1/posts      → Get all posts by user 1
POST   /api/v1/users/1/posts      → Create post for user 1
GET    /api/v1/posts/5            → Get post 5
PUT    /api/v1/posts/5            → Update post 5
DELETE /api/v1/posts/5            → Delete post 5

Comments:
GET    /api/v1/posts/5/comments   → Get comments on post 5
POST   /api/v1/posts/5/comments   → Add comment to post 5
DELETE /api/v1/posts/5/comments/3 → Delete comment 3
```

---

## Practice Exercises

### 1. HTTP Methods
- Understand when to use each method
- Identify correct method for operations
- Distinguish GET vs POST

### 2. Status Codes
- Know common status codes
- Identify appropriate response code for scenario
- Understand error codes

### 3. Headers
- Practice setting request headers
- Understand response headers
- Work with cookies

### 4. REST Principles
- Design RESTful URLs
- Map CRUD to HTTP methods
- Understand resource-based design

### 5. Data Formats
- Work with JSON
- Parse and create JSON
- Handle URL encoding

### 6. API Usage
- Make HTTP requests with Python
- Parse responses
- Handle errors

### 7. API Design
- Design complete REST API
- Plan endpoints
- Plan response formats

---

# End of Notes
