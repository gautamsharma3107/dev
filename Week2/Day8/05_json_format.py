"""
Day 8 - JSON Format
==================
Learn: JSON structure, parsing, creating, and manipulating JSON data

Key Concepts:
- JSON = JavaScript Object Notation
- Language-independent data format
- Human-readable and machine-parseable
- Most common format for API communication
"""

import json

# ========== WHAT IS JSON? ==========
print("=" * 60)
print("WHAT IS JSON?")
print("=" * 60)

print("""
📄 JSON (JavaScript Object Notation):

- Lightweight data-interchange format
- Easy for humans to read and write
- Easy for machines to parse and generate
- Language independent
- Most popular format for APIs

Why JSON?
✅ Human-readable
✅ Compact
✅ Language independent
✅ Native to JavaScript/Web
✅ Supported by all programming languages
""")

# ========== JSON DATA TYPES ==========
print("\n" + "=" * 60)
print("JSON DATA TYPES")
print("=" * 60)

print("""
📋 JSON supports these data types:

┌─────────────┬──────────────────┬──────────────────────────┐
│  JSON Type  │  Python Type     │  Example                 │
├─────────────┼──────────────────┼──────────────────────────┤
│  string     │  str             │  "hello"                 │
│  number     │  int/float       │  42, 3.14                │
│  boolean    │  bool            │  true, false             │
│  null       │  None            │  null                    │
│  array      │  list            │  [1, 2, 3]               │
│  object     │  dict            │  {"key": "value"}        │
└─────────────┴──────────────────┴──────────────────────────┘

⚠️ Important Differences:
- JSON uses double quotes only: "text" ✅  'text' ❌
- JSON booleans are lowercase: true/false (not True/False)
- JSON null, not None
- No trailing commas allowed
- No comments allowed in JSON
""")

# ========== JSON STRUCTURE ==========
print("\n" + "=" * 60)
print("JSON STRUCTURE")
print("=" * 60)

print("""
📝 JSON Object (like Python dict):

{
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "is_active": true,
    "score": null
}

📝 JSON Array (like Python list):

[
    "apple",
    "banana",
    "cherry"
]

📝 Nested Structure:

{
    "user": {
        "name": "John",
        "contacts": {
            "email": "john@example.com",
            "phone": "123-456-7890"
        }
    },
    "orders": [
        {"id": 1, "total": 99.99},
        {"id": 2, "total": 49.99}
    ]
}
""")

# ========== WORKING WITH JSON IN PYTHON ==========
print("\n" + "=" * 60)
print("WORKING WITH JSON IN PYTHON")
print("=" * 60)

# Python dict
user = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "is_active": True,
    "hobbies": ["coding", "gaming", "reading"],
    "address": {
        "city": "New York",
        "country": "USA"
    }
}

print("📝 Original Python Dictionary:")
print(user)
print(f"\nType: {type(user)}")

# ========== CONVERTING PYTHON TO JSON ==========
print("\n" + "-" * 50)
print("Converting Python to JSON (json.dumps)")
print("-" * 50)

# Convert to JSON string
json_string = json.dumps(user)
print(f"\nJSON String:")
print(json_string)
print(f"\nType: {type(json_string)}")

# Pretty print with indentation
print("\n📝 Pretty Formatted JSON:")
json_pretty = json.dumps(user, indent=4)
print(json_pretty)

# With sorting keys
print("\n📝 Sorted Keys:")
json_sorted = json.dumps(user, indent=4, sort_keys=True)
print(json_sorted)

# ========== CONVERTING JSON TO PYTHON ==========
print("\n" + "-" * 50)
print("Converting JSON to Python (json.loads)")
print("-" * 50)

# JSON string
json_data = '''
{
    "name": "Jane Smith",
    "age": 25,
    "skills": ["Python", "JavaScript", "SQL"],
    "employed": true,
    "salary": null
}
'''

print(f"JSON String:\n{json_data}")

# Parse JSON
python_obj = json.loads(json_data)
print(f"\nParsed to Python dict:")
print(python_obj)
print(f"\nType: {type(python_obj)}")

# Access data
print(f"\nAccessing data:")
print(f"  Name: {python_obj['name']}")
print(f"  Age: {python_obj['age']}")
print(f"  Skills: {python_obj['skills']}")
print(f"  First skill: {python_obj['skills'][0]}")

# ========== READING JSON FROM FILES ==========
print("\n" + "=" * 60)
print("READING AND WRITING JSON FILES")
print("=" * 60)

# Sample data
users_data = {
    "users": [
        {"id": 1, "name": "John", "role": "admin"},
        {"id": 2, "name": "Jane", "role": "user"},
        {"id": 3, "name": "Bob", "role": "user"}
    ],
    "total": 3,
    "page": 1
}

# Write to file
print("\n📝 Writing JSON to file:")
print("-" * 40)

# Using a temporary in-memory approach for demonstration
import io

# Simulating file operations
json_output = json.dumps(users_data, indent=4)
print(f"Writing to users.json:\n{json_output}")

# For actual file operations:
print("""
# Write to file
with open('users.json', 'w') as f:
    json.dump(users_data, f, indent=4)

# Read from file
with open('users.json', 'r') as f:
    data = json.load(f)
    print(data)
""")

# ========== HANDLING API RESPONSES ==========
print("\n" + "=" * 60)
print("HANDLING API RESPONSES")
print("=" * 60)

# Simulated API response
api_response = '''
{
    "status": "success",
    "data": {
        "users": [
            {
                "id": 1,
                "name": "John Doe",
                "email": "john@example.com",
                "posts": [
                    {"id": 101, "title": "First Post"},
                    {"id": 102, "title": "Second Post"}
                ]
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "jane@example.com",
                "posts": []
            }
        ]
    },
    "pagination": {
        "page": 1,
        "per_page": 10,
        "total": 2
    }
}
'''

print("📥 API Response:")
response = json.loads(api_response)
print(json.dumps(response, indent=2))

print("\n📝 Extracting Data:")
print("-" * 40)

# Navigate nested JSON
if response['status'] == 'success':
    users = response['data']['users']
    print(f"Total users: {len(users)}")
    
    for user in users:
        print(f"\n  User: {user['name']}")
        print(f"  Email: {user['email']}")
        print(f"  Posts: {len(user['posts'])}")
        
        for post in user['posts']:
            print(f"    - {post['title']}")

# ========== COMMON JSON OPERATIONS ==========
print("\n" + "=" * 60)
print("COMMON JSON OPERATIONS")
print("=" * 60)

# Working with complex JSON
print("\n1️⃣ Safe Key Access (avoid KeyError):")
print("-" * 40)

data = {"name": "John", "age": 30}

# Using get() for safe access
print(f"Name: {data.get('name', 'Unknown')}")
print(f"Email: {data.get('email', 'Not provided')}")  # Key doesn't exist

print("\n2️⃣ Nested Safe Access:")
print("-" * 40)

nested = {
    "user": {
        "profile": {
            "name": "John"
        }
    }
}

# Safe nested access
def safe_get(data, *keys, default=None):
    """Safely get nested values"""
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default
        if current is None:
            return default
    return current

print(f"Name: {safe_get(nested, 'user', 'profile', 'name')}")
print(f"Email: {safe_get(nested, 'user', 'profile', 'email', default='N/A')}")

print("\n3️⃣ Modifying JSON Data:")
print("-" * 40)

# Add/update fields
user = {"name": "John", "age": 30}
print(f"Original: {user}")

user['email'] = "john@example.com"  # Add new field
user['age'] = 31  # Update existing field
print(f"Modified: {user}")

# Remove fields
del user['age']
print(f"After deletion: {user}")

print("\n4️⃣ Merging JSON Objects:")
print("-" * 40)

defaults = {"theme": "light", "language": "en", "notifications": True}
user_prefs = {"theme": "dark", "language": "en"}

# Merge (Python 3.9+)
merged = defaults | user_prefs
print(f"Defaults: {defaults}")
print(f"User prefs: {user_prefs}")
print(f"Merged: {merged}")

# Alternative for older Python
merged_alt = {**defaults, **user_prefs}
print(f"Merged (alt): {merged_alt}")

# ========== JSON VALIDATION ==========
print("\n" + "=" * 60)
print("JSON VALIDATION")
print("=" * 60)

def validate_json(json_string):
    """Check if a string is valid JSON"""
    try:
        json.loads(json_string)
        return True, "Valid JSON"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"

test_cases = [
    '{"name": "John", "age": 30}',  # Valid
    "{'name': 'John'}",              # Invalid (single quotes)
    '{"name": "John",}',             # Invalid (trailing comma)
    '{"name": "John"',               # Invalid (missing brace)
    '[1, 2, 3]',                     # Valid
]

print("Testing JSON validation:")
for test in test_cases:
    is_valid, message = validate_json(test)
    status = "✅" if is_valid else "❌"
    print(f"{status} {test[:30]:30} → {message}")

# ========== REAL-WORLD EXAMPLE ==========
print("\n" + "=" * 60)
print("REAL-WORLD EXAMPLE - API Data Processing")
print("=" * 60)

# Simulating fetching data from an API
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def fetch_json(url):
    """Fetch JSON from a URL"""
    try:
        req = Request(url)
        req.add_header('Accept', 'application/json')
        
        with urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except (HTTPError, URLError, json.JSONDecodeError) as e:
        return {"error": str(e)}

print("\n🌐 Fetching JSON from API:")
print("-" * 40)

# Using httpbin for testing
result = fetch_json("https://httpbin.org/json")

if "error" not in result:
    print("✅ Successfully fetched JSON!")
    print(f"\nData structure:")
    print(json.dumps(result, indent=2))
else:
    print(f"❌ Error: {result['error']}")

# ========== COMMON PITFALLS ==========
print("\n" + "=" * 60)
print("COMMON JSON PITFALLS")
print("=" * 60)

print("""
⚠️ Common Mistakes to Avoid:

1. Using single quotes
   ❌ {'name': 'John'}
   ✅ {"name": "John"}

2. Trailing commas
   ❌ {"a": 1, "b": 2,}
   ✅ {"a": 1, "b": 2}

3. Using Python-specific values
   ❌ {"active": True, "data": None}
   ✅ {"active": true, "data": null}
   (json.dumps handles this automatically)

4. Comments in JSON
   ❌ {"name": "John"} // this is a comment
   ✅ JSON doesn't support comments

5. Unquoted keys
   ❌ {name: "John"}
   ✅ {"name": "John"}

6. NaN or Infinity
   ❌ {"value": NaN}
   ✅ Use null or a string instead

7. Forgetting to handle encoding
   Always use .encode()/.decode() with proper encoding
""")

print("\n" + "=" * 60)
print("✅ JSON Format - Complete!")
print("=" * 60)
