# Day 8 Quick Reference Cheat Sheet

## Client-Server Architecture
```
Client (Browser) ──Request──► Server (Web Server)
                 ◄─Response──
```

### URL Structure
```
https://www.example.com:443/path/page?query=value#section
  │           │           │    │         │          │
Protocol   Domain       Port  Path    Query     Fragment
```

### DNS Lookup
- Translates domain names to IP addresses
- `google.com` → `142.250.190.68`

## HTTP Methods

| Method | CRUD   | Purpose                  | Body | Idempotent |
|--------|--------|--------------------------|------|------------|
| GET    | Read   | Retrieve data            | No   | Yes        |
| POST   | Create | Create new resource      | Yes  | No         |
| PUT    | Update | Replace entire resource  | Yes  | Yes        |
| PATCH  | Update | Partial update           | Yes  | No         |
| DELETE | Delete | Remove resource          | No   | Yes        |

```python
# Quick Examples
GET    /api/users          # List users
GET    /api/users/123      # Get user 123
POST   /api/users          # Create user
PUT    /api/users/123      # Replace user 123
PATCH  /api/users/123      # Update user 123
DELETE /api/users/123      # Delete user 123
```

## HTTP Status Codes

### Success (2xx)
- `200 OK` - Standard success
- `201 Created` - Resource created (POST)
- `204 No Content` - Success, no body (DELETE)

### Redirection (3xx)
- `301 Moved Permanently` - URL changed forever
- `302 Found` - Temporary redirect
- `304 Not Modified` - Use cache

### Client Errors (4xx)
- `400 Bad Request` - Invalid data
- `401 Unauthorized` - Need to login
- `403 Forbidden` - No permission
- `404 Not Found` - Resource doesn't exist
- `409 Conflict` - Duplicate resource
- `422 Unprocessable` - Validation failed
- `429 Too Many Requests` - Rate limited

### Server Errors (5xx)
- `500 Internal Server Error` - Server broke
- `502 Bad Gateway` - Upstream issue
- `503 Service Unavailable` - Maintenance
- `504 Gateway Timeout` - Server too slow

## REST API Design

### Good URL Patterns
```
/api/users              # Collection
/api/users/123          # Specific resource
/api/users/123/posts    # Nested resource
/api/users?role=admin   # Filtered collection
/api/users?page=2&limit=20  # Pagination
```

### API Response Patterns
```json
// Single Resource
{
    "id": 123,
    "name": "John"
}

// Collection
{
    "data": [...],
    "total": 100,
    "page": 1,
    "per_page": 20
}

// Error
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Email is required"
    }
}
```

## JSON in Python

```python
import json

# Python dict to JSON string
json_string = json.dumps(data, indent=4)

# JSON string to Python dict
python_dict = json.loads(json_string)

# Write JSON to file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read JSON from file
with open('data.json', 'r') as f:
    data = json.load(f)

# Safe access
value = data.get('key', 'default')

# Validate JSON
try:
    json.loads(json_string)
    print("Valid JSON")
except json.JSONDecodeError:
    print("Invalid JSON")
```

### JSON Data Types
| JSON | Python |
|------|--------|
| string | str |
| number | int/float |
| true/false | True/False |
| null | None |
| array | list |
| object | dict |

## HTML Basics

### Document Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Title</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

### Common Tags
```html
<!-- Headings -->
<h1>Main Title</h1>
<h2>Subtitle</h2>

<!-- Text -->
<p>Paragraph</p>
<strong>Bold</strong>
<em>Italic</em>

<!-- Links & Images -->
<a href="https://example.com">Link</a>
<img src="image.jpg" alt="Description">

<!-- Lists -->
<ul>
    <li>Bullet item</li>
</ul>
<ol>
    <li>Numbered item</li>
</ol>

<!-- Containers -->
<div>Block container</div>
<span>Inline container</span>
```

### Forms
```html
<form action="/submit" method="POST">
    <input type="text" name="username" required>
    <input type="email" name="email">
    <input type="password" name="password">
    <textarea name="message"></textarea>
    <select name="country">
        <option value="us">USA</option>
    </select>
    <input type="checkbox" name="agree">
    <button type="submit">Submit</button>
</form>
```

### Input Types
```
text, password, email, number, tel, url
date, time, checkbox, radio, file, hidden
submit, reset, button
```

## Making HTTP Requests with Python

```python
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def make_request(url, method='GET', data=None):
    headers = {'Content-Type': 'application/json'}
    req_data = json.dumps(data).encode() if data else None
    req = Request(url, data=req_data, headers=headers, method=method)
    
    try:
        with urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except URLError as e:
        print(f"URL Error: {e.reason}")

# Example usage
result = make_request("https://api.example.com/users")
result = make_request("https://api.example.com/users", "POST", {"name": "John"})
```

## HTML Escaping (Security)
```python
import html

user_input = '<script>alert("XSS")</script>'
safe_text = html.escape(user_input)
# Result: &lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;
```

---
**Keep this handy for quick reference!** 🚀
