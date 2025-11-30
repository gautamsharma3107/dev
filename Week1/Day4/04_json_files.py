"""
Day 4 - JSON Files
==================
Learn: Reading and writing JSON files

Key Concepts:
- JSON = JavaScript Object Notation
- Human-readable data format
- Maps to Python dict/list
- Use json module
"""

import json
import os

# ========== JSON BASICS ==========
print("=" * 50)
print("JSON FILE BASICS")
print("=" * 50)

print("""
Python Type  →  JSON Type
-----------     ---------
dict         →  object {}
list/tuple   →  array []
str          →  string ""
int/float    →  number
True/False   →  true/false
None         →  null
""")

# ========== PYTHON TO JSON ==========
print("=" * 50)
print("PYTHON TO JSON")
print("=" * 50)

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Python", "JavaScript"],
    "grades": {"Python": 95, "JavaScript": 88},
    "address": None
}

# json.dumps() - to string
json_string = json.dumps(person)
print("1. json.dumps() - to string:")
print(f"   {json_string}")

# Pretty print
json_pretty = json.dumps(person, indent=4)
print("\n2. Pretty formatted:")
print(json_pretty)

# ========== WRITE JSON TO FILE ==========
print("\n" + "=" * 50)
print("WRITING JSON TO FILE")
print("=" * 50)

# json.dump() - to file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)
print("✅ Created 'person.json'")

# List of objects
users = [
    {"id": 1, "name": "Alice", "active": True},
    {"id": 2, "name": "Bob", "active": False},
    {"id": 3, "name": "Charlie", "active": True}
]

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)
print("✅ Created 'users.json'")

print("\nusers.json:")
with open("users.json", "r") as file:
    print(file.read())

# ========== READ JSON ==========
print("=" * 50)
print("READING JSON")
print("=" * 50)

# json.load() - from file
print("1. json.load() - from file:")
with open("person.json", "r") as file:
    data = json.load(file)
    print(f"   Name: {data['name']}")
    print(f"   Courses: {data['courses']}")

# json.loads() - from string
print("\n2. json.loads() - from string:")
json_text = '{"product": "Laptop", "price": 999}'
parsed = json.loads(json_text)
print(f"   Product: {parsed['product']}, Price: ${parsed['price']}")

# ========== WORKING WITH JSON ==========
print("\n" + "=" * 50)
print("WORKING WITH JSON DATA")
print("=" * 50)

with open("users.json", "r") as file:
    users_data = json.load(file)

print("Active users:")
for user in users_data:
    if user["active"]:
        print(f"   - {user['name']}")

# Add new user
new_user = {"id": 4, "name": "Diana", "active": True}
users_data.append(new_user)

with open("users.json", "w") as file:
    json.dump(users_data, file, indent=4)
print("\n✅ Added new user to 'users.json'")

# ========== NESTED JSON ==========
print("\n" + "=" * 50)
print("NESTED JSON")
print("=" * 50)

company = {
    "name": "Tech Corp",
    "founded": 2010,
    "departments": {
        "engineering": {
            "head": "Alice",
            "employees": 50
        },
        "marketing": {
            "head": "Bob",
            "employees": 20
        }
    },
    "locations": ["NYC", "LA", "London"]
}

with open("company.json", "w") as file:
    json.dump(company, file, indent=4)

with open("company.json", "r") as file:
    data = json.load(file)

print(f"Company: {data['name']}")
print(f"Engineering Head: {data['departments']['engineering']['head']}")
print(f"Locations: {', '.join(data['locations'])}")

# ========== JSON ERRORS ==========
print("\n" + "=" * 50)
print("HANDLING JSON ERRORS")
print("=" * 50)

# Invalid JSON
invalid = '{"name": "John", age: 30}'  # Missing quotes

try:
    parsed = json.loads(invalid)
except json.JSONDecodeError as e:
    print(f"❌ JSON Error: {e}")

# Valid JSON
valid = '{"name": "John", "age": 30}'
try:
    parsed = json.loads(valid)
    print(f"✅ Valid: {parsed}")
except json.JSONDecodeError as e:
    print(f"❌ Error: {e}")

# ========== CUSTOM ENCODING ==========
print("\n" + "=" * 50)
print("CUSTOM JSON ENCODING")
print("=" * 50)

from datetime import datetime

# Custom encoder for datetime
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

event = {
    "name": "Meeting",
    "date": datetime.now()
}

json_output = json.dumps(event, cls=DateEncoder, indent=4)
print("Custom encoded with datetime:")
print(json_output)

# ========== PRACTICAL: CONFIG FILE ==========
print("\n" + "=" * 50)
print("PRACTICAL: Config File")
print("=" * 50)

default_config = {
    "app_name": "MyApp",
    "version": "1.0",
    "debug": False,
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "features": {
        "dark_mode": True,
        "notifications": True
    }
}

def save_config(config, filename="config.json"):
    with open(filename, "w") as file:
        json.dump(config, file, indent=4)
    print(f"✅ Config saved")

def load_config(filename="config.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return default_config

# Save and load
save_config(default_config)
config = load_config()

print(f"App: {config['app_name']} v{config['version']}")
print(f"Debug: {config['debug']}")
print(f"DB: {config['database']['host']}:{config['database']['port']}")

# Cleanup
for f in ["person.json", "users.json", "company.json", "config.json"]:
    if os.path.exists(f):
        os.remove(f)
print("\n✅ Cleaned up files")

print("\n" + "=" * 50)
print("✅ JSON Files - Complete!")
print("=" * 50)
