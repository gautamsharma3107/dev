"""
Authentication Patterns
=======================
Day 37 - System Design Basics

Learn different authentication and authorization patterns for secure applications.
"""

# ============================================================
# 1. AUTHENTICATION VS AUTHORIZATION
# ============================================================

"""
Authentication (AuthN): Who are you?
- Verifying identity
- Login process
- "Prove you are who you claim to be"

Authorization (AuthZ): What can you do?
- Access control
- Permissions
- "What are you allowed to access?"

Flow:
1. User logs in (Authentication)
2. System checks permissions (Authorization)
3. User accesses resources
"""

# ============================================================
# 2. AUTHENTICATION METHODS
# ============================================================

"""
Common Authentication Methods:

1. Session-based Authentication
   - Server stores session
   - Client stores session ID in cookie
   - Stateful

2. Token-based Authentication (JWT)
   - Server generates token
   - Client stores token
   - Stateless

3. OAuth 2.0
   - Third-party authentication
   - Google, GitHub, Facebook login
   - Delegated access

4. API Keys
   - Simple authentication for APIs
   - Static, long-lived tokens

5. Multi-Factor Authentication (MFA)
   - Something you know (password)
   - Something you have (phone)
   - Something you are (biometric)
"""

# ============================================================
# 3. SESSION-BASED AUTHENTICATION
# ============================================================

"""
Session-based Authentication Flow:

1. User submits credentials
2. Server validates credentials
3. Server creates session, stores in database/memory
4. Server sends session ID in cookie
5. Client includes cookie in subsequent requests
6. Server validates session ID

Pros:
- Simple to implement
- Easy to invalidate (delete session)
- Works well with server-rendered apps

Cons:
- Requires server-side storage
- Not ideal for microservices
- Scaling challenges
"""

# Session Implementation Example
session_example = '''
from flask import Flask, session, request, redirect
import secrets
import hashlib

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# In-memory session store (use Redis in production)
sessions = {}
users_db = {
    "john@example.com": {
        "password_hash": "hashed_password_here",
        "name": "John Doe"
    }
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    user = users_db.get(email)
    if user and user['password_hash'] == hash_password(password):
        # Create session
        session_id = secrets.token_hex(32)
        sessions[session_id] = {
            'user_email': email,
            'created_at': datetime.now()
        }
        
        response = redirect('/dashboard')
        response.set_cookie('session_id', session_id, httponly=True, secure=True)
        return response
    
    return 'Invalid credentials', 401

@app.route('/logout')
def logout():
    session_id = request.cookies.get('session_id')
    if session_id:
        sessions.pop(session_id, None)
    
    response = redirect('/login')
    response.delete_cookie('session_id')
    return response

def require_auth(f):
    """Decorator to require authentication"""
    def wrapper(*args, **kwargs):
        session_id = request.cookies.get('session_id')
        if not session_id or session_id not in sessions:
            return redirect('/login')
        return f(*args, **kwargs)
    return wrapper

@app.route('/dashboard')
@require_auth
def dashboard():
    return 'Welcome to dashboard!'
'''

# ============================================================
# 4. JWT (JSON WEB TOKEN) AUTHENTICATION
# ============================================================

"""
JWT Authentication Flow:

1. User submits credentials
2. Server validates credentials
3. Server generates JWT token
4. Client stores token (localStorage, memory)
5. Client sends token in Authorization header
6. Server validates token

JWT Structure:
- Header: Algorithm, type
- Payload: Claims (user data, expiration)
- Signature: Verify integrity

Pros:
- Stateless (no server storage)
- Works across services
- Contains user info
- Good for microservices

Cons:
- Cannot be invalidated easily
- Token size larger than session ID
- Security considerations for storage
"""

# JWT Implementation Example
jwt_example = '''
import jwt
import datetime
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)
SECRET_KEY = "your-secret-key-keep-it-safe"

def generate_token(user_id, email, role="user"):
    """Generate JWT token"""
    payload = {
        'user_id': user_id,
        'email': email,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token):
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

def require_token(f):
    """Decorator to require valid JWT"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Get token from header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Missing token'}), 401
        
        token = auth_header.split(' ')[1]
        payload = verify_token(token)
        
        if not payload:
            return jsonify({'error': 'Invalid or expired token'}), 401
        
        # Add user info to request
        request.user = payload
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Validate credentials (simplified)
    user = authenticate_user(email, password)
    if user:
        token = generate_token(user['id'], user['email'], user['role'])
        return jsonify({
            'token': token,
            'user': {'id': user['id'], 'email': user['email']}
        })
    
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/protected')
@require_token
def protected():
    return jsonify({
        'message': 'Access granted',
        'user': request.user
    })

# Refresh Token Pattern
def generate_tokens(user_id, email):
    """Generate access and refresh tokens"""
    access_token = jwt.encode({
        'user_id': user_id,
        'email': email,
        'type': 'access',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    }, SECRET_KEY, algorithm='HS256')
    
    refresh_token = jwt.encode({
        'user_id': user_id,
        'type': 'refresh',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }, SECRET_KEY, algorithm='HS256')
    
    return access_token, refresh_token

@app.route('/refresh', methods=['POST'])
def refresh():
    """Get new access token using refresh token"""
    refresh_token = request.json.get('refresh_token')
    payload = verify_token(refresh_token)
    
    if payload and payload.get('type') == 'refresh':
        user = get_user(payload['user_id'])
        access_token, _ = generate_tokens(user['id'], user['email'])
        return jsonify({'access_token': access_token})
    
    return jsonify({'error': 'Invalid refresh token'}), 401
'''

# ============================================================
# 5. OAUTH 2.0
# ============================================================

"""
OAuth 2.0 Flow (Authorization Code):

1. User clicks "Login with Google"
2. Redirect to Google authorization page
3. User grants permission
4. Google redirects back with authorization code
5. Server exchanges code for access token
6. Server uses token to get user info
7. Server creates session/JWT for user

Roles:
- Resource Owner: User
- Client: Your application
- Authorization Server: Google, GitHub, etc.
- Resource Server: API with user data

Grant Types:
- Authorization Code: Most secure, for web apps
- Implicit: For SPAs (deprecated)
- Client Credentials: For machine-to-machine
- Password: For trusted apps (not recommended)
"""

# OAuth 2.0 Implementation Example
oauth_example = '''
from flask import Flask, redirect, request, session
import requests
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# Google OAuth Configuration
GOOGLE_CLIENT_ID = "your-client-id"
GOOGLE_CLIENT_SECRET = "your-client-secret"
GOOGLE_REDIRECT_URI = "http://localhost:5000/callback"

@app.route('/login/google')
def google_login():
    """Redirect to Google authorization page"""
    state = secrets.token_hex(16)
    session['oauth_state'] = state
    
    auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={GOOGLE_CLIENT_ID}&"
        f"redirect_uri={GOOGLE_REDIRECT_URI}&"
        "response_type=code&"
        "scope=openid%20email%20profile&"
        f"state={state}"
    )
    
    return redirect(auth_url)

@app.route('/callback')
def google_callback():
    """Handle Google OAuth callback"""
    # Verify state
    if request.args.get('state') != session.get('oauth_state'):
        return 'Invalid state', 400
    
    # Exchange code for token
    code = request.args.get('code')
    token_response = requests.post(
        'https://oauth2.googleapis.com/token',
        data={
            'client_id': GOOGLE_CLIENT_ID,
            'client_secret': GOOGLE_CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': GOOGLE_REDIRECT_URI
        }
    )
    
    tokens = token_response.json()
    access_token = tokens['access_token']
    
    # Get user info
    user_info = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        headers={'Authorization': f'Bearer {access_token}'}
    ).json()
    
    # Create or update user in database
    user = create_or_update_user(
        email=user_info['email'],
        name=user_info['name'],
        google_id=user_info['id']
    )
    
    # Create session or JWT
    session['user_id'] = user['id']
    
    return redirect('/dashboard')
'''

# ============================================================
# 6. API KEY AUTHENTICATION
# ============================================================

"""
API Key Authentication:

- Simple authentication for APIs
- Key sent in header or query parameter
- Best for server-to-server communication

Security Considerations:
- Use HTTPS
- Rotate keys regularly
- Limit key permissions
- Monitor usage
"""

# API Key Implementation
api_key_example = '''
from flask import Flask, request, jsonify
from functools import wraps
import secrets
import hashlib

app = Flask(__name__)

# API Keys storage (use database in production)
api_keys = {
    "hashed_key_1": {
        "name": "Production App",
        "permissions": ["read", "write"],
        "rate_limit": 1000
    },
    "hashed_key_2": {
        "name": "Analytics Service",
        "permissions": ["read"],
        "rate_limit": 5000
    }
}

def hash_api_key(key):
    return hashlib.sha256(key.encode()).hexdigest()

def generate_api_key():
    """Generate new API key"""
    return f"sk_{secrets.token_hex(32)}"

def require_api_key(permissions=None):
    """Decorator to require valid API key"""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Get API key from header
            api_key = request.headers.get('X-API-Key')
            if not api_key:
                api_key = request.args.get('api_key')
            
            if not api_key:
                return jsonify({'error': 'Missing API key'}), 401
            
            # Look up key
            key_hash = hash_api_key(api_key)
            key_data = api_keys.get(key_hash)
            
            if not key_data:
                return jsonify({'error': 'Invalid API key'}), 401
            
            # Check permissions
            if permissions:
                if not all(p in key_data['permissions'] for p in permissions):
                    return jsonify({'error': 'Insufficient permissions'}), 403
            
            request.api_key_data = key_data
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/data')
@require_api_key(permissions=['read'])
def get_data():
    return jsonify({'data': 'some data'})

@app.route('/api/data', methods=['POST'])
@require_api_key(permissions=['write'])
def create_data():
    return jsonify({'created': True})
'''

# ============================================================
# 7. AUTHORIZATION PATTERNS
# ============================================================

"""
Authorization Patterns:

1. Role-Based Access Control (RBAC)
   - Users have roles
   - Roles have permissions
   - Simple and common

2. Attribute-Based Access Control (ABAC)
   - Based on attributes
   - User, resource, environment
   - More flexible, more complex

3. Permission-Based
   - Direct permission assignment
   - Fine-grained control
"""

# RBAC Implementation
class RBAC:
    """Role-Based Access Control"""
    
    def __init__(self):
        # Define roles and their permissions
        self.roles = {
            'admin': ['create', 'read', 'update', 'delete', 'manage_users'],
            'editor': ['create', 'read', 'update'],
            'viewer': ['read'],
            'moderator': ['read', 'update', 'delete']
        }
        
        # User role assignments
        self.user_roles = {
            'user_1': ['admin'],
            'user_2': ['editor'],
            'user_3': ['viewer', 'moderator']  # Multiple roles
        }
    
    def get_user_permissions(self, user_id):
        """Get all permissions for a user"""
        permissions = set()
        user_roles = self.user_roles.get(user_id, [])
        
        for role in user_roles:
            role_permissions = self.roles.get(role, [])
            permissions.update(role_permissions)
        
        return permissions
    
    def has_permission(self, user_id, permission):
        """Check if user has specific permission"""
        permissions = self.get_user_permissions(user_id)
        return permission in permissions
    
    def has_role(self, user_id, role):
        """Check if user has specific role"""
        user_roles = self.user_roles.get(user_id, [])
        return role in user_roles

# RBAC Decorator
def require_permission(permission):
    """Decorator to require specific permission"""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            rbac = RBAC()
            user_id = get_current_user_id()  # From session/JWT
            
            if not rbac.has_permission(user_id, permission):
                return jsonify({'error': 'Permission denied'}), 403
            
            return f(*args, **kwargs)
        return wrapper
    return decorator

def require_role(role):
    """Decorator to require specific role"""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            rbac = RBAC()
            user_id = get_current_user_id()
            
            if not rbac.has_role(user_id, role):
                return jsonify({'error': 'Role required: ' + role}), 403
            
            return f(*args, **kwargs)
        return wrapper
    return decorator

# ============================================================
# 8. PASSWORD SECURITY
# ============================================================

"""
Password Security Best Practices:

1. Never store plain text passwords
2. Use strong hashing algorithms (bcrypt, Argon2)
3. Use unique salt for each password
4. Enforce password complexity
5. Rate limit login attempts
6. Implement account lockout
"""

# Password Hashing Example
password_example = '''
import bcrypt
import re

class PasswordManager:
    """Secure password handling"""
    
    def __init__(self, rounds=12):
        self.rounds = rounds  # bcrypt work factor
    
    def hash_password(self, password):
        """Hash password with bcrypt"""
        salt = bcrypt.gensalt(rounds=self.rounds)
        return bcrypt.hashpw(password.encode(), salt).decode()
    
    def verify_password(self, password, hashed):
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode(), hashed.encode())
    
    def validate_password_strength(self, password):
        """Check password meets requirements"""
        errors = []
        
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")
        if not re.search(r'[A-Z]', password):
            errors.append("Password must contain uppercase letter")
        if not re.search(r'[a-z]', password):
            errors.append("Password must contain lowercase letter")
        if not re.search(r'[0-9]', password):
            errors.append("Password must contain number")
        if not re.search(r'[!@#$%^&*]', password):
            errors.append("Password must contain special character")
        
        return len(errors) == 0, errors

# Usage
pm = PasswordManager()
hashed = pm.hash_password("SecureP@ss123")
is_valid = pm.verify_password("SecureP@ss123", hashed)
'''

# Rate Limiting for Login
login_rate_limit = '''
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Track login attempts (use Redis in production)
login_attempts = {}

def check_rate_limit(email):
    """Check if user is rate limited"""
    now = time.time()
    key = f"login:{email}"
    
    if key not in login_attempts:
        login_attempts[key] = {'count': 0, 'reset_at': now + 3600}
    
    attempts = login_attempts[key]
    
    # Reset if window passed
    if now > attempts['reset_at']:
        attempts['count'] = 0
        attempts['reset_at'] = now + 3600
    
    # Check limit
    if attempts['count'] >= 5:
        return False, attempts['reset_at'] - now
    
    return True, 0

def record_failed_attempt(email):
    """Record failed login attempt"""
    key = f"login:{email}"
    if key in login_attempts:
        login_attempts[key]['count'] += 1

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    
    # Check rate limit
    allowed, wait_time = check_rate_limit(email)
    if not allowed:
        return jsonify({
            'error': 'Too many attempts',
            'retry_after': int(wait_time)
        }), 429
    
    # Authenticate
    user = authenticate(email, password)
    if user:
        return jsonify({'token': generate_token(user)})
    
    # Record failed attempt
    record_failed_attempt(email)
    return jsonify({'error': 'Invalid credentials'}), 401
'''

# ============================================================
# 9. SECURITY BEST PRACTICES
# ============================================================

"""
Authentication Security Best Practices:

1. Use HTTPS everywhere
2. Store tokens securely (httpOnly cookies, no localStorage)
3. Implement CSRF protection
4. Use secure cookie settings
5. Validate and sanitize all inputs
6. Log authentication events
7. Implement proper logout
8. Use short-lived access tokens
9. Rotate refresh tokens
10. Monitor for suspicious activity
"""

security_headers = {
    # Prevent XSS
    'X-XSS-Protection': '1; mode=block',
    'X-Content-Type-Options': 'nosniff',
    
    # Prevent clickjacking
    'X-Frame-Options': 'DENY',
    
    # Content Security Policy
    'Content-Security-Policy': "default-src 'self'",
    
    # HTTPS only
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
}

# Secure Cookie Settings
secure_cookie_settings = {
    'httpOnly': True,     # Not accessible via JavaScript
    'secure': True,       # HTTPS only
    'sameSite': 'Strict', # CSRF protection
    'path': '/',
    'max_age': 3600       # 1 hour
}

# ============================================================
# 10. COMPLETE AUTH SYSTEM EXAMPLE
# ============================================================

complete_auth_example = '''
"""
Complete Authentication System with:
- Registration
- Login (JWT)
- Password reset
- Email verification
- Role-based access
"""

from flask import Flask, request, jsonify
from functools import wraps
import jwt
import bcrypt
import secrets
from datetime import datetime, timedelta

app = Flask(__name__)
SECRET_KEY = secrets.token_hex(32)

# Database models (simplified)
users = {}
reset_tokens = {}

class AuthSystem:
    @staticmethod
    def register(email, password, name):
        """Register new user"""
        if email in users:
            return None, "Email already exists"
        
        # Hash password
        password_hash = bcrypt.hashpw(
            password.encode(), 
            bcrypt.gensalt()
        ).decode()
        
        # Create user
        user_id = str(len(users) + 1)
        users[email] = {
            'id': user_id,
            'email': email,
            'password_hash': password_hash,
            'name': name,
            'role': 'user',
            'is_verified': False,
            'created_at': datetime.utcnow()
        }
        
        return users[email], None
    
    @staticmethod
    def login(email, password):
        """Authenticate user and return tokens"""
        user = users.get(email)
        if not user:
            return None, "Invalid credentials"
        
        if not bcrypt.checkpw(password.encode(), user['password_hash'].encode()):
            return None, "Invalid credentials"
        
        # Generate tokens
        access_token = jwt.encode({
            'user_id': user['id'],
            'email': user['email'],
            'role': user['role'],
            'exp': datetime.utcnow() + timedelta(minutes=15)
        }, SECRET_KEY, algorithm='HS256')
        
        refresh_token = jwt.encode({
            'user_id': user['id'],
            'type': 'refresh',
            'exp': datetime.utcnow() + timedelta(days=7)
        }, SECRET_KEY, algorithm='HS256')
        
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': {
                'id': user['id'],
                'email': user['email'],
                'name': user['name']
            }
        }, None
    
    @staticmethod
    def request_password_reset(email):
        """Generate password reset token"""
        if email not in users:
            return True  # Don't reveal if email exists
        
        token = secrets.token_urlsafe(32)
        reset_tokens[token] = {
            'email': email,
            'expires': datetime.utcnow() + timedelta(hours=1)
        }
        
        # Send email (simplified)
        print(f"Password reset link: /reset-password?token={token}")
        return True
    
    @staticmethod
    def reset_password(token, new_password):
        """Reset password using token"""
        reset_data = reset_tokens.get(token)
        if not reset_data:
            return False, "Invalid token"
        
        if datetime.utcnow() > reset_data['expires']:
            del reset_tokens[token]
            return False, "Token expired"
        
        # Update password
        email = reset_data['email']
        users[email]['password_hash'] = bcrypt.hashpw(
            new_password.encode(),
            bcrypt.gensalt()
        ).decode()
        
        del reset_tokens[token]
        return True, None

# Decorators
def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Missing token'}), 401
        
        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user = payload
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        
        return f(*args, **kwargs)
    return wrapper

def require_role(role):
    def decorator(f):
        @wraps(f)
        @require_auth
        def wrapper(*args, **kwargs):
            if request.user.get('role') != role:
                return jsonify({'error': 'Insufficient permissions'}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user, error = AuthSystem.register(
        data['email'],
        data['password'],
        data['name']
    )
    if error:
        return jsonify({'error': error}), 400
    return jsonify({'user': {'id': user['id'], 'email': user['email']}}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    result, error = AuthSystem.login(data['email'], data['password'])
    if error:
        return jsonify({'error': error}), 401
    return jsonify(result)

@app.route('/me')
@require_auth
def get_me():
    return jsonify({'user': request.user})

@app.route('/admin')
@require_role('admin')
def admin_only():
    return jsonify({'message': 'Admin access granted'})
'''

# ============================================================
# SUMMARY
# ============================================================

"""
Authentication Patterns Summary:

1. Session-based: Simple, server-stored sessions
2. JWT: Stateless tokens, good for APIs
3. OAuth 2.0: Third-party authentication
4. API Keys: Simple API authentication

Authorization:
- RBAC: Role-based access control
- ABAC: Attribute-based access control

Security Best Practices:
- Use HTTPS
- Hash passwords (bcrypt)
- Rate limit login attempts
- Use secure cookie settings
- Implement proper token refresh
"""

if __name__ == "__main__":
    print("Authentication Patterns")
    print("=" * 50)
    
    print("\nAuthentication Methods:")
    print("1. Session-based")
    print("2. JWT (JSON Web Tokens)")
    print("3. OAuth 2.0")
    print("4. API Keys")
    
    print("\nAuthorization Patterns:")
    print("- RBAC (Role-Based Access Control)")
    print("- ABAC (Attribute-Based Access Control)")
    
    # Demo RBAC
    rbac = RBAC()
    print("\nRBAC Demo:")
    print(f"User 1 permissions: {rbac.get_user_permissions('user_1')}")
    print(f"User 2 has 'delete' permission: {rbac.has_permission('user_2', 'delete')}")
    print(f"User 3 has 'moderator' role: {rbac.has_role('user_3', 'moderator')}")
