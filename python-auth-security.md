# Authentication & Web Security: Complete Guide

---

## Table of Contents
1. [Introduction to Authentication](#introduction-to-authentication)
2. [Basic Authentication](#basic-authentication)
3. [Session-Based Authentication](#session-based-authentication)
4. [Token-Based Authentication](#token-based-authentication)
5. [JWT (JSON Web Tokens)](#jwt-json-web-tokens)
6. [OAuth 2.0](#oauth-20)
7. [Web Security Threats](#web-security-threats)
8. [CORS (Cross-Origin Resource Sharing)](#cors-cross-origin-resource-sharing)
9. [CSRF (Cross-Site Request Forgery)](#csrf-cross-site-request-forgery)
10. [XSS (Cross-Site Scripting)](#xss-cross-site-scripting)
11. [SQL Injection Prevention](#sql-injection-prevention)
12. [Password Security](#password-security)
13. [HTTPS and SSL/TLS](#https-and-ssltls)
14. [Practical Examples](#practical-examples)
15. [Best Practices](#best-practices)
16. [Practice Exercises](#practice-exercises)

---

## Introduction to Authentication

### Authentication vs Authorization

```
Authentication (AuthN):
├── Who are you?
├── Verify identity
├── Login process
└── "User is Alice"

Authorization (AuthZ):
├── What can you do?
├── Verify permissions
├── Access control
└── "Alice can delete posts"
```

### Authentication Methods

```
Basic Auth
├── Username and password
├── Simplest method
└── Must use HTTPS

Session-Based
├── Server stores session
├── Client gets session ID
└── Common in traditional web apps

Token-Based
├── No server state
├── Client stores token
└── Common in APIs

OAuth 2.0
├── Third-party authentication
├── Delegated authorization
└── Google, GitHub, etc.
```

---

## Basic Authentication

### How Basic Auth Works

```
Client Request:
GET /api/users HTTP/1.1
Authorization: Basic base64(username:password)

Server Process:
1. Decode base64 string
2. Split into username and password
3. Verify credentials
4. Grant/deny access
```

### Python Implementation

```python
import base64
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI()
security = HTTPBasic()

# Valid credentials (normally from database)
USERS = {
    "alice": "password123",
    "bob": "password456"
}

@app.get("/secure")
def secure_endpoint(credentials: HTTPBasicCredentials = Depends(security)):
    # Verify username and password
    if credentials.username not in USERS:
        raise HTTPException(status_code=401, detail="Invalid username")
    
    if not secrets.compare_digest(
        credentials.password, 
        USERS[credentials.username]
    ):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return {"message": f"Hello {credentials.username}"}
```

### Encoding/Decoding

```python
import base64

# Encode credentials
credentials = "alice:password123"
encoded = base64.b64encode(credentials.encode()).decode()
print(f"Authorization: Basic {encoded}")
# Output: Authorization: Basic YWxpY2U6cGFzc3dvcmQxMjM=

# Decode credentials
header = "Basic YWxpY2U6cGFzc3dvcmQxMjM="
encoded_part = header.split(" ")[1]
decoded = base64.b64decode(encoded_part).decode()
username, password = decoded.split(":", 1)
print(username, password)  # alice password123
```

### Advantages and Disadvantages

```
Advantages:
✓ Simple to implement
✓ Built-in HTTP standard
✓ No additional setup

Disadvantages:
✗ Credentials sent with every request
✗ Base64 is encoding, not encryption
✗ MUST use HTTPS
✗ Cannot revoke without server state
✗ Password exposure risk
```

---

## Session-Based Authentication

### How Sessions Work

```
1. User logs in with credentials
   ↓
2. Server verifies credentials
   ↓
3. Server creates session object
   ↓
4. Server stores session (in database/Redis)
   ↓
5. Server sends session ID to client (via cookie)
   ↓
6. Client stores session cookie
   ↓
7. Client sends session ID with each request
   ↓
8. Server verifies session ID
   ↓
9. Grant/deny access based on session
```

### Python Implementation (Flask)

```python
from flask import Flask, session, request, redirect
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# Simulated database
USERS = {
    "alice": generate_password_hash("password123"),
    "bob": generate_password_hash("password456")
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Verify credentials
    if username not in USERS:
        return "Invalid username", 401
    
    if not check_password_hash(USERS[username], password):
        return "Invalid password", 401
    
    # Create session
    session['user_id'] = username
    session['authenticated'] = True
    
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    # Check if authenticated
    if not session.get('authenticated'):
        return redirect('/login')
    
    return f"Welcome {session['user_id']}"

@app.route('/logout')
def logout():
    # Destroy session
    session.clear()
    return redirect('/login')

# Protect routes
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
```

### Session Storage

```
Options:
1. Memory (default, Flask)
   - Fast, but lost on restart
   - Single server only

2. Database
   - Persistent
   - Shared across servers
   - Slower than memory

3. Redis
   - Fast and persistent
   - Shared across servers
   - Best practice for production

4. Filesystem
   - Simple
   - File I/O overhead
```

### Flask-Session with Redis

```python
from flask import Flask, session
from flask_session import Session
import redis

app = Flask(__name__)

# Configure Redis session
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')

Session(app)

@app.route('/login', methods=['POST'])
def login():
    session['user_id'] = 'alice'
    return "Logged in"

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return "Not authenticated", 401
    return f"User: {user_id}"
```

### Advantages and Disadvantages

```
Advantages:
✓ Server controls sessions
✓ Easy to revoke
✓ Can store user state

Disadvantages:
✗ Server-side storage required
✗ Doesn't scale easily
✗ Cookies vulnerable to CSRF
✗ Not suitable for mobile/APIs
```

---

## Token-Based Authentication

### How Token Auth Works

```
1. User sends credentials
   ↓
2. Server verifies credentials
   ↓
3. Server generates token
   ↓
4. Server sends token to client
   ↓
5. Client stores token (localStorage, sessionStorage)
   ↓
6. Client sends token in Authorization header
   ↓
7. Server validates token
   ↓
8. Grant/deny access
```

### Simple Token Implementation

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthCredentials
import secrets
import time

app = FastAPI()
security = HTTPBearer()

# Token storage (normally in database)
TOKENS = {}
USERS = {"alice": "password123"}

@app.post("/token")
def login(username: str, password: str):
    # Verify credentials
    if username not in USERS:
        raise HTTPException(status_code=401, detail="Invalid username")
    
    if USERS[username] != password:  # In production, hash passwords!
        raise HTTPException(status_code=401, detail="Invalid password")
    
    # Generate token
    token = secrets.token_urlsafe(32)
    
    # Store token with metadata
    TOKENS[token] = {
        "username": username,
        "created": time.time(),
        "expires": time.time() + 3600  # 1 hour
    }
    
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(credentials: HTTPAuthCredentials = Depends(security)):
    token = credentials.credentials
    
    # Validate token
    if token not in TOKENS:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    token_data = TOKENS[token]
    
    # Check expiration
    if time.time() > token_data["expires"]:
        del TOKENS[token]
        raise HTTPException(status_code=401, detail="Token expired")
    
    return {"message": f"Hello {token_data['username']}"}

@app.post("/logout")
def logout(credentials: HTTPAuthCredentials = Depends(security)):
    token = credentials.credentials
    if token in TOKENS:
        del TOKENS[token]
    return {"message": "Logged out"}
```

### Advantages and Disadvantages

```
Advantages:
✓ Stateless (no server storage needed)
✓ Scales easily
✓ Suitable for mobile/APIs
✓ Can revoke by changing secret

Disadvantages:
✗ Token cannot be revoked immediately
✗ Token storage on client (localStorage is vulnerable)
✗ More complex than session-based
```

---

## JWT (JSON Web Tokens)

### What is JWT?

JWT is a standard token format consisting of three parts: Header, Payload, Signature.

```
Structure:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFsaWNlIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

Header . Payload . Signature
```

### JWT Parts

```
Header:
{
  "alg": "HS256",  // Algorithm
  "typ": "JWT"     // Type
}

Payload (Claims):
{
  "sub": "alice",           // Subject (user ID)
  "name": "Alice Smith",
  "iat": 1516239022,        // Issued at
  "exp": 1516242622,        // Expiration
  "aud": "api.example.com"  // Audience
}

Signature:
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret_key
)
```

### PyJWT Implementation

```python
import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthCredentials

app = FastAPI()
security = HTTPBearer()

SECRET_KEY = "your-secret-key-keep-safe"
ALGORITHM = "HS256"

# User storage
USERS = {"alice": "password123"}

@app.post("/token")
def login(username: str, password: str):
    # Verify credentials
    if username not in USERS or USERS[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create JWT
    payload = {
        "sub": username,  # Subject
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

def verify_jwt(credentials: HTTPAuthCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/protected")
def protected_route(username: str = Depends(verify_jwt)):
    return {"message": f"Hello {username}"}
```

### JWT Claims

```python
import jwt
from datetime import datetime, timedelta

# Standard claims
payload = {
    # Registered Claims
    "iss": "myapp",                    # Issuer
    "sub": "alice",                    # Subject
    "aud": "api.example.com",          # Audience
    "exp": datetime.utcnow() + timedelta(hours=1),  # Expiration
    "nbf": datetime.utcnow(),          # Not before
    "iat": datetime.utcnow(),          # Issued at
    "jti": "unique-id",                # JWT ID
    
    # Custom claims
    "roles": ["admin", "user"],
    "email": "alice@example.com",
    "department": "engineering"
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
```

### Refresh Tokens

```python
@app.post("/token")
def login(username: str, password: str):
    # Verify credentials...
    
    # Short-lived access token (15 minutes)
    access_payload = {
        "sub": username,
        "type": "access",
        "exp": datetime.utcnow() + timedelta(minutes=15)
    }
    access_token = jwt.encode(access_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    # Long-lived refresh token (7 days)
    refresh_payload = {
        "sub": username,
        "type": "refresh",
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    refresh_token = jwt.encode(refresh_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 900  # 15 minutes
    }

@app.post("/refresh")
def refresh_access_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")
        
        # Generate new access token
        new_payload = {
            "sub": payload["sub"],
            "type": "access",
            "exp": datetime.utcnow() + timedelta(minutes=15)
        }
        new_access_token = jwt.encode(new_payload, SECRET_KEY, algorithm=ALGORITHM)
        
        return {"access_token": new_access_token, "token_type": "bearer"}
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

---

## OAuth 2.0

### What is OAuth 2.0?

OAuth 2.0 is a delegation protocol for user authorization from third-party providers.

### OAuth 2.0 Flow

```
1. User clicks "Login with Google"
   ↓
2. Client redirects to Google authorization
   ↓
3. User logs in with Google (on Google's site)
   ↓
4. User grants permission
   ↓
5. Google redirects back to client with code
   ↓
6. Client exchanges code for access token (server-to-server)
   ↓
7. Client gets user info from Google
   ↓
8. Client creates session/token
   ↓
9. User logged in
```

### OAuth 2.0 Grant Types

```
Authorization Code (Most Common)
- User goes to provider's site
- Client exchanges code for token
- Best for web apps
- Server-to-server verification

Implicit Grant (Deprecated)
- Token directly in redirect
- Less secure

Client Credentials
- Service-to-service authentication
- No user involved

Resource Owner Password
- User gives credentials to client
- Least secure

Device Code
- For devices without browser
```

### Python OAuth Implementation (Google)

```python
from fastapi import FastAPI, HTTPException
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
import os

app = FastAPI()

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key="your-secret")

# Configure OAuth
oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

@app.get("/login")
def login(request):
    redirect_uri = request.url_for('callback')
    return oauth.google.authorize_redirect(request, str(redirect_uri))

@app.get("/callback")
async def callback(request):
    token = await oauth.google.authorize_access_token(request)
    
    user_info = token.get("userinfo")
    if user_info:
        # Store user info, create session
        return {
            "user_id": user_info["sub"],
            "email": user_info["email"],
            "name": user_info["name"]
        }
    
    raise HTTPException(status_code=401, detail="Failed to authenticate")

@app.get("/logout")
def logout(request):
    request.session.clear()
    return {"message": "Logged out"}
```

---

## Web Security Threats

### Security Landscape

```
Major Web Threats:
├── CSRF (Cross-Site Request Forgery)
├── XSS (Cross-Site Scripting)
├── SQL Injection
├── Authentication Flaws
├── Sensitive Data Exposure
├── Broken Access Control
└── Security Misconfiguration
```

---

## CORS (Cross-Origin Resource Sharing)

### What is CORS?

CORS allows requests from different domains/ports.

### Same-Origin Policy

```
Same-Origin = protocol + domain + port

https://example.com:443/api/users
https://example.com:443/api/posts
→ Same origin

https://example.com vs http://example.com
→ Different origin (protocol)

https://example.com vs https://api.example.com
→ Different origin (subdomain)

https://example.com:443 vs https://example.com:8443
→ Different origin (port)
```

### CORS Headers

```
Request Headers:
Origin: https://client.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type

Response Headers:
Access-Control-Allow-Origin: https://client.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 3600
```

### FastAPI CORS Implementation

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow specific origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://client.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
    max_age=3600
)

# Allow multiple origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://client1.com",
        "https://client2.com"
    ]
)

# Allow all origins (only for development!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/data")
def get_data():
    return {"message": "Data from different origin"}
```

### Preflight Requests

```
Browser automatically makes OPTIONS request for:
- Non-simple methods (POST, PUT, DELETE)
- Custom headers
- Different origins

OPTIONS /api/users HTTP/1.1
Origin: https://client.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type

Server responds with:
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://client.com
Access-Control-Allow-Methods: POST
Access-Control-Allow-Headers: Content-Type
Access-Control-Max-Age: 3600

Browser then makes actual request.
```

---

## CSRF (Cross-Site Request Forgery)

### What is CSRF?

CSRF forces user to perform unintended actions on authenticated site.

```
Attack:
1. User logs into bank.com
2. User opens malicious-site.com (without logging out)
3. Malicious site has hidden form:
   <form action="bank.com/transfer" method="POST">
     <input name="amount" value="1000">
     <input name="to_account" value="attacker">
   </form>
4. Form auto-submits
5. User's browser sends authenticated request
6. Money transferred!
```

### CSRF Tokens

```
Protection:
1. Server generates unique token for user
2. Server sends token in form/page
3. Client includes token in request
4. Server validates token
5. Attacker cannot get token (same-origin policy)
```

### Flask CSRF Protection

```python
from flask import Flask, session, render_template, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "secret-key"
csrf = CSRFProtect(app)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
@csrf.protect  # CSRF validation
def submit():
    # Process form...
    return "Form submitted"

# In template (form.html):
# <form method="POST" action="/submit">
#   {{ csrf_token() }}
#   <input type="text" name="amount">
#   <input type="submit">
# </form>
```

### FastAPI CSRF Protection

```python
from fastapi import FastAPI, Form
from fastapi.middleware import Middleware
from starlette_csrf import CSRFMiddleware

app = FastAPI(
    middleware=[
        Middleware(CSRFMiddleware, secret="your-secret-key")
    ]
)

@app.post("/transfer")
async def transfer(amount: int = Form(...), csrf_token: str = Form(...)):
    # csrf_token validated by middleware
    return {"amount": amount, "status": "transferred"}
```

### Prevention Strategies

```
✓ Use CSRF tokens
✓ Validate Referer/Origin headers
✓ Use SameSite cookies
✓ Require authentication
✓ Use POST (not GET) for state changes
```

---

## XSS (Cross-Site Scripting)

### What is XSS?

XSS injects malicious scripts into web pages.

```
Attack:
1. Attacker posts comment: <script>alert('hacked')</script>
2. Comment stored in database
3. Other users load page
4. Script executes in their browser
5. Attacker steals cookies/tokens
```

### Types of XSS

```
Stored XSS (Most Dangerous)
- Malicious script stored in database
- Affects all users who view it

Reflected XSS
- Malicious script in URL parameter
- Affects user who clicks link

DOM-based XSS
- JavaScript vulnerability in page
- Manipulates DOM unsafely
```

### XSS Prevention

```python
from fastapi import FastAPI
from markupsafe import escape
import html

app = FastAPI()

# Escape user input
@app.get("/profile/{username}")
def profile(username: str):
    # Escape HTML characters
    safe_username = escape(username)
    return {"profile": f"Welcome {safe_username}"}

# Alternative: HTML escape
safe_username = html.escape(username)

# Never render raw user input!
# BAD:
# return f"<p>{user_comment}</p>"

# GOOD:
# return f"<p>{escape(user_comment)}</p>"
```

### Content Security Policy (CSP)

```python
# Set CSP header to prevent inline scripts
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
def home():
    response = Response("content")
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' https://trusted.com; "
        "style-src 'self' 'unsafe-inline'"
    )
    return response
```

### Template Auto-escaping

```python
# Flask auto-escapes by default
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def user(username):
    # Jinja2 auto-escapes
    return render_template('user.html', username=username)

# In template (user.html):
# <h1>Welcome {{ username }}</h1>
# If username contains HTML, it's escaped
```

---

## SQL Injection Prevention

### What is SQL Injection?

Attacker injects SQL code into queries.

```
Attack:
Input: ' OR '1'='1
Query: SELECT * FROM users WHERE username = '' OR '1'='1'
Result: Returns all users!
```

### Prevention: Parameterized Queries

```python
# SQLAlchemy (ORM)
from sqlalchemy import text

# ✓ GOOD - Parameterized
user = db.session.execute(
    text("SELECT * FROM users WHERE username = :username"),
    {"username": username}
)

# sqlite3
# ✓ GOOD
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

# MySQL
# ✓ GOOD
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```

### Prevention: ORM Usage

```python
# ✓ GOOD - Using SQLAlchemy ORM
from sqlalchemy import select

user = session.execute(
    select(User).where(User.username == username)
).first()

# Automatically parameterized
```

### Prevention: Input Validation

```python
# Validate input
import re

def validate_username(username):
    # Only allow alphanumeric and underscore
    if not re.match("^[a-zA-Z0-9_]+$", username):
        raise ValueError("Invalid username")
    return username
```

---

## Password Security

### Password Hashing

```
DO NOT store plain passwords!

Good: hash("password123") → $2b$12$K9h3Ij4Q...
Bad: password123
```

### bcrypt

```python
import bcrypt

# Hash password
password = "password123"
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
# b'$2b$12$K9h3Ij4Quw.HTLXdJ8UAmOqRNRNjq.QQVcqCkQTOBG.TsDLp2Lw5u'

# Verify password
if bcrypt.checkpw(password.encode(), hashed):
    print("Password matches!")

# In production
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash
hashed_password = pwd_context.hash("password123")

# Verify
if pwd_context.verify("password123", hashed_password):
    print("Password matches!")
```

### Argon2

```python
from argon2 import PasswordHasher

ph = PasswordHasher()

# Hash
hashed = ph.hash("password123")

# Verify
try:
    ph.verify(hashed, "password123")
    print("Password matches!")
except:
    print("Password doesn't match!")
```

### Password Best Practices

```python
import secrets
import string

def generate_strong_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# Require strong passwords
def validate_password_strength(password):
    if len(password) < 12:
        raise ValueError("Password must be at least 12 characters")
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain uppercase letter")
    if not any(c.islower() for c in password):
        raise ValueError("Password must contain lowercase letter")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain digit")
    if not any(c in string.punctuation for c in password):
        raise ValueError("Password must contain special character")
    return True
```

---

## HTTPS and SSL/TLS

### What is HTTPS?

HTTPS is HTTP with encryption (SSL/TLS).

```
HTTP (Insecure):
Client → Plain text → Server

HTTPS (Secure):
Client → Encrypted → Server
         (TLS/SSL)
```

### SSL/TLS Handshake

```
1. Client sends ClientHello
   - Supported protocols, ciphers, random

2. Server responds ServerHello
   - Chosen protocol, cipher, certificate

3. Client verifies certificate
   - Check signature, expiration, domain

4. Key Exchange
   - Client and server agree on encryption key

5. Finished
   - Both send encrypted "Finished" message

6. Encrypted Communication
   - All data encrypted with agreed key
```

### Getting SSL Certificate

```
Options:
1. Let's Encrypt (Free)
   - Automated, 90-day renewal
   - Most common

2. Commercial CA
   - Paid
   - Longer validity

3. Self-signed (Development only!)
   - No cost
   - Browser warnings
```

### Enable HTTPS in FastAPI

```python
import ssl
from fastapi import FastAPI

app = FastAPI()

# For development (self-signed cert)
if __name__ == "__main__":
    import uvicorn
    
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(
        "path/to/cert.pem",
        "path/to/key.pem"
    )
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=443,
        ssl_keyfile="path/to/key.pem",
        ssl_certfile="path/to/cert.pem"
    )

# In production, use reverse proxy (nginx)
```

### HSTS (HTTP Strict Transport Security)

```python
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    # Force HTTPS for 1 year
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains"
    )
    return response
```

---

## Practical Examples

### Complete Login System

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

app = FastAPI()

# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Models
class User(BaseModel):
    username: str
    email: str

class LoginRequest(BaseModel):
    username: str
    password: str

# Database (mock)
USERS_DB = {
    "alice": {
        "username": "alice",
        "email": "alice@example.com",
        "hashed_password": pwd_context.hash("password123")
    }
}

# Authentication
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(username, expires_delta):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + expires_delta
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/login")
async def login(request: LoginRequest):
    # Find user
    user = USERS_DB.get(request.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Verify password
    if not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        request.username,
        access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# Protected route
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401)
        return username
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401)

@app.get("/profile")
async def profile(
    token: str = Depends(lambda: "token_from_header"),
    username: str = Depends(verify_token)
):
    return {"username": username, "email": USERS_DB[username]["email"]}
```

---

## Best Practices

### Authentication

```
✓ Use HTTPS always
✓ Hash passwords with bcrypt/argon2
✓ Use secure random tokens
✓ Implement rate limiting on login
✓ Log authentication attempts
✓ Use short-lived tokens with refresh
✓ Validate input strictly
✓ Never expose sensitive info in URLs
```

### Authorization

```
✓ Principle of least privilege
✓ Separate authentication and authorization
✓ Use role-based access control (RBAC)
✓ Validate permissions on backend
✓ Log authorization failures
```

### General Security

```
✓ Keep dependencies updated
✓ Use security headers
✓ Implement rate limiting
✓ Log security events
✓ Use environment variables for secrets
✓ Run security audits regularly
✓ Follow OWASP guidelines
```

---

## Practice Exercises

### 1. Basic Auth
- Implement basic auth
- Understand base64 encoding
- Test with requests library

### 2. Session Auth
- Implement session-based login
- Store sessions in Redis
- Test logout functionality

### 3. JWT Auth
- Create JWT tokens
- Validate JWT tokens
- Implement refresh tokens

### 4. Password Security
- Hash passwords with bcrypt
- Verify passwords
- Validate password strength

### 5. CSRF Protection
- Implement CSRF tokens
- Validate tokens in requests

### 6. XSS Prevention
- Escape user input
- Use template auto-escaping
- Set CSP headers

### 7. Complete System
- Build login/logout system
- Implement protected routes
- Add password reset

---

# End of Notes
