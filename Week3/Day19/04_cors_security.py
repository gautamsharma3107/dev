"""
Day 19 - CORS and Security Basics
=================================
Learn: Cross-Origin Resource Sharing and web security

Key Concepts:
- What is CORS and why it exists
- Same-Origin Policy
- CORS headers and configuration
- Common security headers
- Basic security best practices
"""

print("=" * 60)
print("CORS AND SECURITY BASICS")
print("=" * 60)

# ========== WHAT IS CORS? ==========
print("\n" + "=" * 60)
print("WHAT IS CORS?")
print("=" * 60)

print("""
CORS = Cross-Origin Resource Sharing

THE PROBLEM:
Browsers have a security feature called "Same-Origin Policy"
that blocks requests from one origin to another.

Origin = Protocol + Domain + Port
https://example.com:443

SAME ORIGIN:
✅ https://example.com/page1 → https://example.com/api
   (Same protocol, domain, port)

DIFFERENT ORIGINS:
❌ https://frontend.com → https://api.backend.com
   (Different domains)
❌ http://localhost:3000 → http://localhost:8000
   (Different ports)
❌ http://example.com → https://example.com
   (Different protocols)

WHY IT EXISTS:
Prevents malicious websites from accessing your data
on other sites you're logged into.

CORS ALLOWS:
Servers can specify which origins are allowed to access
their resources by setting specific HTTP headers.
""")

# ========== HOW CORS WORKS ==========
print("\n" + "=" * 60)
print("HOW CORS WORKS")
print("=" * 60)

print("""
SIMPLE REQUESTS (GET, POST with simple headers):
================================================
Browser                          Server
   │                              │
   │──── GET /api/data ──────────>│
   │     Origin: http://app.com   │
   │                              │
   │<─── Response ────────────────│
   │     Access-Control-Allow-Origin: http://app.com
   │                              │
If origin matches → Browser allows response
If not → Browser blocks response (CORS error)


PREFLIGHT REQUESTS (PUT, DELETE, custom headers):
=================================================
Browser                          Server
   │                              │
   │──── OPTIONS /api/data ──────>│  (Preflight)
   │     Origin: http://app.com   │
   │     Access-Control-Request-Method: DELETE
   │                              │
   │<─── Response ────────────────│
   │     Access-Control-Allow-Origin: http://app.com
   │     Access-Control-Allow-Methods: GET, POST, DELETE
   │                              │
   │                              │
   │──── DELETE /api/data ───────>│  (Actual request)
   │     Origin: http://app.com   │
   │                              │
   │<─── Response ────────────────│
""")

# ========== CORS HEADERS ==========
print("\n" + "=" * 60)
print("CORS HEADERS EXPLAINED")
print("=" * 60)

print("""
RESPONSE HEADERS (Server → Browser):
====================================

Access-Control-Allow-Origin: https://app.com
   - Which origins can access the resource
   - Can be specific origin or * (any origin)
   - ⚠️ Don't use * with credentials!

Access-Control-Allow-Methods: GET, POST, PUT, DELETE
   - Which HTTP methods are allowed

Access-Control-Allow-Headers: Content-Type, Authorization
   - Which request headers are allowed

Access-Control-Allow-Credentials: true
   - Whether cookies/auth headers are allowed
   - Requires specific origin (not *)

Access-Control-Max-Age: 86400
   - How long preflight results can be cached (seconds)

Access-Control-Expose-Headers: X-Custom-Header
   - Which response headers JavaScript can access


REQUEST HEADERS (Browser → Server):
===================================

Origin: https://app.com
   - Where the request originated (browser sets this)

Access-Control-Request-Method: DELETE
   - Method to be used (in preflight)

Access-Control-Request-Headers: Authorization
   - Headers to be used (in preflight)
""")

# ========== FASTAPI CORS CONFIGURATION ==========
print("\n" + "=" * 60)
print("FASTAPI CORS CONFIGURATION")
print("=" * 60)

fastapi_cors_code = '''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Basic CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],           # Allow all methods
    allow_headers=["*"],           # Allow all headers
)

# Production configuration
origins = [
    "https://myapp.com",
    "https://www.myapp.com",
    "https://admin.myapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    expose_headers=["X-Request-ID"],
    max_age=600,  # Cache preflight for 10 minutes
)

# Development (allow all - NOT for production!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
'''

print("FastAPI CORS configuration:")
print(fastapi_cors_code)

# ========== DJANGO CORS CONFIGURATION ==========
print("\n" + "=" * 60)
print("DJANGO CORS CONFIGURATION")
print("=" * 60)

django_cors_code = r'''
# Install: pip install django-cors-headers

# settings.py

INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Place early!
    'django.middleware.common.CommonMiddleware',
    ...
]

# Allow specific origins
CORS_ALLOWED_ORIGINS = [
    "https://myapp.com",
    "https://www.myapp.com",
]

# Or use regex patterns
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.myapp\.com$",
]

# Allow all origins (development only!)
CORS_ALLOW_ALL_ORIGINS = True

# Allow credentials (cookies, auth headers)
CORS_ALLOW_CREDENTIALS = True

# Allowed methods
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

# Allowed headers
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "origin",
    "x-csrftoken",
    "x-requested-with",
]

# Expose custom headers
CORS_EXPOSE_HEADERS = ["X-Custom-Header"]

# Preflight cache time
CORS_PREFLIGHT_MAX_AGE = 86400
'''

print("Django CORS configuration:")
print(django_cors_code)

# ========== FLASK CORS CONFIGURATION ==========
print("\n" + "=" * 60)
print("FLASK CORS CONFIGURATION")
print("=" * 60)

flask_cors_code = '''
# Install: pip install flask-cors

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Basic - allow all origins
CORS(app)

# Specific origins
CORS(app, origins=["http://localhost:3000", "https://myapp.com"])

# Full configuration
CORS(
    app,
    origins=["https://myapp.com"],
    methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    supports_credentials=True,
    max_age=600
)

# Per-route CORS
from flask_cors import cross_origin

@app.route("/api/data")
@cross_origin(origins="https://myapp.com")
def get_data():
    return {"data": "value"}

# Different settings per route
@app.route("/api/public")
@cross_origin(origins="*")  # Allow any origin
def public_data():
    return {"public": "data"}
'''

print("Flask CORS configuration:")
print(flask_cors_code)

# ========== SECURITY HEADERS ==========
print("\n" + "=" * 60)
print("IMPORTANT SECURITY HEADERS")
print("=" * 60)

print("""
1. X-Content-Type-Options: nosniff
   Prevents MIME type sniffing
   Stops browser from interpreting files as different type

2. X-Frame-Options: DENY | SAMEORIGIN
   Prevents clickjacking attacks
   DENY: Can't be embedded in any iframe
   SAMEORIGIN: Only same origin can embed

3. X-XSS-Protection: 1; mode=block
   Legacy XSS protection (modern browsers have built-in)
   Still good to include for older browsers

4. Strict-Transport-Security: max-age=31536000; includeSubDomains
   Forces HTTPS for all requests
   Browser remembers to always use HTTPS

5. Content-Security-Policy: default-src 'self'
   Controls what resources can be loaded
   Prevents XSS and data injection attacks

6. Referrer-Policy: strict-origin-when-cross-origin
   Controls what referrer info is sent
   Protects user privacy

7. Permissions-Policy: geolocation=(), camera=()
   Controls browser features available to the page
   Disables unused features for security
""")

# ========== IMPLEMENTING SECURITY HEADERS ==========
print("\n" + "=" * 60)
print("IMPLEMENTING SECURITY HEADERS")
print("=" * 60)

security_headers_code = '''
# FastAPI Security Headers Middleware
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        
        return response

app = FastAPI()
app.add_middleware(SecurityHeadersMiddleware)


# Django Security Settings (settings.py)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True  # Force HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# Flask with Talisman
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(
    app,
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    content_security_policy={
        'default-src': "'self'",
        'script-src': "'self'",
    }
)
'''

print("Security headers implementation:")
print(security_headers_code)

# ========== COMMON SECURITY BEST PRACTICES ==========
print("\n" + "=" * 60)
print("WEB SECURITY BEST PRACTICES")
print("=" * 60)

print("""
1. AUTHENTICATION
   ✅ Use secure session management
   ✅ Implement proper password hashing (bcrypt, argon2)
   ✅ Use HTTPS for all auth requests
   ✅ Implement rate limiting on login
   ✅ Use secure token storage (HttpOnly cookies)

2. INPUT VALIDATION
   ✅ Validate all user input
   ✅ Use parameterized queries (prevent SQL injection)
   ✅ Sanitize output (prevent XSS)
   ✅ Limit input sizes

3. SENSITIVE DATA
   ✅ Never store passwords in plain text
   ✅ Encrypt sensitive data at rest
   ✅ Use HTTPS for data in transit
   ✅ Don't expose sensitive info in URLs
   ✅ Mask sensitive data in logs

4. CORS
   ✅ Be specific with allowed origins
   ✅ Don't use * with credentials
   ✅ Only allow needed methods and headers
   ✅ Set appropriate preflight cache time

5. GENERAL
   ✅ Keep dependencies updated
   ✅ Use security headers
   ✅ Implement CSRF protection
   ✅ Use Content Security Policy
   ✅ Regular security audits
""")

# ========== CORS DEBUGGING ==========
print("\n" + "=" * 60)
print("DEBUGGING CORS ISSUES")
print("=" * 60)

print("""
COMMON CORS ERRORS:
==================

Error: "has been blocked by CORS policy: No 'Access-Control-Allow-Origin'"
Fix: Add the origin to allowed origins on server

Error: "Response to preflight request doesn't pass"
Fix: Handle OPTIONS request, return proper CORS headers

Error: "Credentials flag is true, but Access-Control-Allow-Credentials is not 'true'"
Fix: Set allow_credentials=True on server

Error: "wildcard '*' cannot be used in Access-Control-Allow-Origin when credentials"
Fix: Use specific origin instead of *


DEBUGGING STEPS:
===============
1. Check browser DevTools → Network tab → Headers
2. Look for preflight OPTIONS request
3. Check response headers from server
4. Verify origin matches allowed origins
5. Check if credentials are needed

Browser Console Commands:
fetch('http://api.com/data')
  .then(r => r.json())
  .then(console.log)
  .catch(console.error)
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE EXAMPLE: SECURE API")
print("=" * 60)

secure_api_code = '''
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

# 1. CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://myapp.com",
        "http://localhost:3000",  # Dev
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=600,
)

# 2. Security Headers Middleware
class SecurityMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

app.add_middleware(SecurityMiddleware)

# 3. Rate Limiting (simple example)
request_counts = {}

@app.middleware("http")
async def rate_limit(request: Request, call_next):
    client_ip = request.client.host
    current_time = int(time.time())
    
    # Clean old entries
    request_counts[client_ip] = [
        t for t in request_counts.get(client_ip, [])
        if current_time - t < 60
    ]
    
    # Check rate limit (100 requests/minute)
    if len(request_counts.get(client_ip, [])) >= 100:
        raise HTTPException(status_code=429, detail="Too many requests")
    
    request_counts.setdefault(client_ip, []).append(current_time)
    return await call_next(request)

# 4. Your API endpoints
@app.get("/api/data")
async def get_data():
    return {"status": "secure", "data": "value"}
'''

print("Complete secure API example:")
print(secure_api_code)

print("\n" + "=" * 60)
print("✅ CORS and Security Basics - Complete!")
print("=" * 60)
