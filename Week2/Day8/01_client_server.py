"""
Day 8 - Client-Server Architecture
===================================
Learn: How the web works, request-response cycle

Key Concepts:
- Client: Browser or application that requests resources
- Server: Computer that hosts resources and responds to requests
- Request-Response cycle: Client sends request, server sends response
- URL: Uniform Resource Locator - address of a resource
- DNS: Domain Name System - translates domain names to IP addresses
"""

# ========== HOW THE WEB WORKS ==========
print("=" * 60)
print("HOW THE WEB WORKS")
print("=" * 60)

print("""
🌐 The Web Architecture:

    ┌─────────┐         REQUEST          ┌─────────┐
    │  CLIENT │  ──────────────────────► │  SERVER │
    │ Browser │                          │   Web   │
    │   App   │  ◄────────────────────── │  Server │
    └─────────┘         RESPONSE         └─────────┘

1. CLIENT (You)
   - Web browser (Chrome, Firefox, Safari)
   - Mobile apps
   - API clients (Postman, curl)
   
2. SERVER (Host)
   - Stores websites/applications
   - Processes requests
   - Returns responses
   
3. INTERNET (Highway)
   - Network connecting clients and servers
   - Uses protocols (HTTP, HTTPS, TCP/IP)
""")

# ========== URL STRUCTURE ==========
print("\n" + "=" * 60)
print("URL STRUCTURE")
print("=" * 60)

print("""
📍 URL (Uniform Resource Locator) Structure:

    https://www.example.com:443/path/page?query=value#section
    ──────  ───────────────  ─── ─────────  ───────────── ───────
      │           │           │      │          │           │
   Protocol    Domain       Port   Path      Query       Fragment
                                           Parameters

Parts Explained:
- Protocol: https:// (secure) or http:// (not secure)
- Domain: www.example.com (human-readable address)
- Port: :443 (optional, default 443 for HTTPS, 80 for HTTP)
- Path: /path/page (location on server)
- Query: ?query=value (parameters to send)
- Fragment: #section (specific part of page)
""")

# Let's parse URLs in Python
from urllib.parse import urlparse, parse_qs

example_urls = [
    "https://www.google.com/search?q=python+tutorial",
    "http://localhost:8000/api/users/123",
    "https://github.com/user/repo/blob/main/file.py"
]

print("\n🔍 Parsing URLs in Python:")
print("-" * 50)

for url in example_urls:
    parsed = urlparse(url)
    print(f"\nURL: {url}")
    print(f"  Scheme: {parsed.scheme}")
    print(f"  Domain: {parsed.netloc}")
    print(f"  Path: {parsed.path}")
    print(f"  Query: {parsed.query}")
    
# ========== REQUEST-RESPONSE CYCLE ==========
print("\n" + "=" * 60)
print("REQUEST-RESPONSE CYCLE")
print("=" * 60)

print("""
🔄 What happens when you visit a website?

1️⃣  You type URL: www.example.com
    ↓
2️⃣  DNS Lookup: Domain → IP Address (192.168.1.1)
    ↓
3️⃣  TCP Connection: Client connects to server
    ↓
4️⃣  HTTP Request: Client sends request
    ↓
5️⃣  Server Processing: Server processes request
    ↓
6️⃣  HTTP Response: Server sends back data
    ↓
7️⃣  Rendering: Browser displays the page
""")

# ========== HTTP REQUEST STRUCTURE ==========
print("\n" + "=" * 60)
print("HTTP REQUEST STRUCTURE")
print("=" * 60)

print("""
📤 HTTP Request Components:

┌──────────────────────────────────────────┐
│  GET /api/users HTTP/1.1                 │ ← Request Line
│  Host: api.example.com                   │ ← Headers
│  Content-Type: application/json          │
│  Authorization: Bearer token123          │
│                                          │
│  { "name": "John", "age": 25 }           │ ← Body (optional)
└──────────────────────────────────────────┘

Parts:
1. Request Line: METHOD + PATH + HTTP Version
2. Headers: Metadata about the request
3. Body: Data sent to server (for POST, PUT, etc.)
""")

# ========== HTTP RESPONSE STRUCTURE ==========
print("\n" + "=" * 60)
print("HTTP RESPONSE STRUCTURE")
print("=" * 60)

print("""
📥 HTTP Response Components:

┌──────────────────────────────────────────┐
│  HTTP/1.1 200 OK                         │ ← Status Line
│  Content-Type: application/json          │ ← Headers
│  Content-Length: 123                     │
│  Date: Mon, 01 Jan 2024 12:00:00 GMT     │
│                                          │
│  {                                       │ ← Body
│    "users": [                            │
│      {"id": 1, "name": "John"}           │
│    ]                                     │
│  }                                       │
└──────────────────────────────────────────┘

Parts:
1. Status Line: HTTP Version + Status Code + Status Text
2. Headers: Metadata about the response
3. Body: Data returned by server
""")

# ========== DNS - DOMAIN NAME SYSTEM ==========
print("\n" + "=" * 60)
print("DNS - DOMAIN NAME SYSTEM")
print("=" * 60)

print("""
🔤 DNS - Translates domain names to IP addresses

    www.google.com  ───DNS───►  142.250.190.68
    (Easy to remember)          (Actual address)

DNS Lookup Process:
1. Browser checks local cache
2. OS checks its cache
3. Query DNS resolver (ISP)
4. Root nameservers → TLD servers → Authoritative servers
5. IP address returned
""")

# Get IP address of a domain (demonstration)
import socket

domains = ["google.com", "github.com", "python.org"]

print("\n🌐 Looking up IP addresses:")
print("-" * 40)

for domain in domains:
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain:20} → {ip}")
    except socket.gaierror:
        print(f"{domain:20} → Could not resolve")

# ========== PROTOCOLS ==========
print("\n" + "=" * 60)
print("WEB PROTOCOLS")
print("=" * 60)

print("""
📡 Common Protocols:

┌───────────┬────────────────────────────────────────┐
│ Protocol  │ Description                            │
├───────────┼────────────────────────────────────────┤
│ HTTP      │ HyperText Transfer Protocol            │
│           │ - Foundation of web communication      │
│           │ - Stateless protocol                   │
│           │ - Port 80 (default)                    │
├───────────┼────────────────────────────────────────┤
│ HTTPS     │ HTTP Secure (HTTP + SSL/TLS)           │
│           │ - Encrypted communication              │
│           │ - Port 443 (default)                   │
│           │ - Always use for sensitive data!       │
├───────────┼────────────────────────────────────────┤
│ TCP/IP    │ Transmission Control Protocol          │
│           │ - Reliable data transmission           │
│           │ - Error checking and ordering          │
├───────────┼────────────────────────────────────────┤
│ WebSocket │ Full-duplex communication              │
│           │ - Real-time, bidirectional             │
│           │ - Chat apps, live updates              │
└───────────┴────────────────────────────────────────┘
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - Making a Web Request")
print("=" * 60)

# Using the built-in urllib library
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
import json

print("""
📝 Making HTTP Requests with Python:

Python has built-in libraries for HTTP:
- urllib (built-in)
- http.client (built-in)
- requests (third-party, easier to use)
""")

# Example: Fetching data from a public API
print("\n🌐 Fetching data from a public API:")
print("-" * 50)

try:
    # Create a request to a public API
    url = "https://httpbin.org/get"
    req = Request(url)
    req.add_header('User-Agent', 'Python-Learning/1.0')
    
    print(f"Sending GET request to: {url}")
    
    with urlopen(req, timeout=5) as response:
        print(f"Status Code: {response.status}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        # Read and parse response
        data = json.loads(response.read().decode())
        print(f"Response received successfully!")
        print(f"Origin IP: {data.get('origin', 'N/A')}")
        
except HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except URLError as e:
    print(f"URL Error: {e.reason}")
except Exception as e:
    print(f"Error: {e}")

# ========== KEY TERMS SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TERMS SUMMARY")
print("=" * 60)

terms = {
    "Client": "Device/software that requests resources (browser, app)",
    "Server": "Computer that hosts and serves resources",
    "URL": "Address of a resource on the web",
    "DNS": "System that translates domain names to IP addresses",
    "HTTP": "Protocol for transferring hypertext (web pages)",
    "HTTPS": "Secure version of HTTP (encrypted)",
    "Request": "Message sent from client to server",
    "Response": "Message sent from server to client",
    "Header": "Metadata about request/response",
    "Body": "Main content/data in request/response",
    "Port": "Virtual endpoint for network communication",
    "Protocol": "Set of rules for data communication"
}

for term, definition in terms.items():
    print(f"• {term}: {definition}")

print("\n" + "=" * 60)
print("✅ Client-Server Architecture - Complete!")
print("=" * 60)
