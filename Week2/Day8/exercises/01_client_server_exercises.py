"""
Day 8 - Exercise 1: Client-Server Exercises
============================================
Practice understanding client-server architecture
"""

print("=" * 60)
print("Exercise 1: Client-Server Architecture")
print("=" * 60)

# ============================================================
# Exercise 1.1: URL Parsing
# ============================================================

print("\n📝 Exercise 1.1: URL Parsing")
print("-" * 50)
print("""
Given the following URLs, identify and extract:
- Protocol
- Domain
- Port (if any)
- Path
- Query parameters

URLs to parse:
1. https://api.github.com/users/octocat
2. http://localhost:8000/api/products?category=electronics&sort=price
3. https://www.google.com:443/search?q=python+tutorial&lang=en
""")

from urllib.parse import urlparse, parse_qs

# TODO: Parse each URL and print its components
urls = [
    "https://api.github.com/users/octocat",
    "http://localhost:8000/api/products?category=electronics&sort=price",
    "https://www.google.com:443/search?q=python+tutorial&lang=en"
]

# Your code here:
for url in urls:
    # parsed = urlparse(url)
    # Print the components
    pass

# ============================================================
# Exercise 1.2: Build a URL
# ============================================================

print("\n📝 Exercise 1.2: Build a URL")
print("-" * 50)
print("""
Create a function that builds a URL from components.

Function signature:
def build_url(protocol, domain, path, params=None):
    # Returns complete URL string

Example:
build_url("https", "api.example.com", "/users", {"page": 1, "limit": 10})
# Returns: "https://api.example.com/users?page=1&limit=10"
""")

from urllib.parse import urlencode

def build_url(protocol, domain, path, params=None):
    """Build a URL from components"""
    # TODO: Implement this function
    pass

# Test your function:
# print(build_url("https", "api.example.com", "/users"))
# print(build_url("https", "api.example.com", "/users", {"page": 1, "limit": 10}))
# print(build_url("http", "localhost:8000", "/api/products", {"category": "electronics"}))

# ============================================================
# Exercise 1.3: DNS Lookup
# ============================================================

print("\n📝 Exercise 1.3: DNS Lookup")
print("-" * 50)
print("""
Create a function that performs DNS lookup for a domain.
Handle errors gracefully if the domain doesn't exist.

domains to test:
- google.com
- github.com
- nonexistent-domain-12345.com
""")

import socket

def dns_lookup(domain):
    """Perform DNS lookup and return IP address"""
    # TODO: Implement this function
    pass

# Test your function:
# for domain in ["google.com", "github.com", "nonexistent-domain-12345.com"]:
#     print(f"{domain}: {dns_lookup(domain)}")

# ============================================================
# Exercise 1.4: Request Headers Analysis
# ============================================================

print("\n📝 Exercise 1.4: Request Headers Analysis")
print("-" * 50)
print("""
Given these HTTP request headers, identify:
1. What is the request method and path?
2. What content type is being sent?
3. Is the user authenticated?
4. What browser is making the request?

Request:
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0
Accept: application/json
Content-Length: 45

{"name": "John", "email": "john@example.com"}
""")

# TODO: Write your answers as comments below:
# 1. Method and Path: 
# 2. Content Type: 
# 3. Authenticated: 
# 4. Browser: 

# ============================================================
# Exercise 1.5: Understanding the Web Flow
# ============================================================

print("\n📝 Exercise 1.5: Web Flow Sequence")
print("-" * 50)
print("""
Arrange these steps in the correct order for what happens
when you type "https://www.google.com" in your browser:

A. Browser renders the HTML page
B. DNS lookup converts domain to IP address
C. Server processes the request
D. TCP connection established
E. Browser sends HTTP GET request
F. Server sends HTTP response with HTML
G. You type the URL and press Enter
H. SSL/TLS handshake for secure connection

Write the correct order (e.g., G, B, D, ...):
""")

# TODO: Write the correct order:
# correct_order = ["G", ...]

print("\n" + "=" * 60)
print("✅ Complete the exercises above!")
print("=" * 60)

"""
SOLUTIONS:

Exercise 1.1:
for url in urls:
    parsed = urlparse(url)
    print(f"URL: {url}")
    print(f"  Protocol: {parsed.scheme}")
    print(f"  Domain: {parsed.netloc}")
    print(f"  Path: {parsed.path}")
    print(f"  Query: {parsed.query}")
    print()

Exercise 1.2:
def build_url(protocol, domain, path, params=None):
    url = f"{protocol}://{domain}{path}"
    if params:
        url += "?" + urlencode(params)
    return url

Exercise 1.3:
def dns_lookup(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "Could not resolve"

Exercise 1.4:
1. Method: POST, Path: /api/users
2. Content Type: application/json
3. Authenticated: Yes (Bearer token present)
4. Browser: Chrome 120 on Windows 10

Exercise 1.5:
Correct order: G, B, D, H, E, C, F, A
G - Type URL
B - DNS lookup
D - TCP connection
H - SSL/TLS handshake
E - Send HTTP request
C - Server processes
F - Server sends response
A - Browser renders
"""
