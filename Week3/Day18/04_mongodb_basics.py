"""
Day 18 - MongoDB Basics
=======================
Learn: Document-oriented database fundamentals

Key Concepts:
- Documents and collections
- CRUD operations
- Query operators
- When to use MongoDB vs SQL

Note: This tutorial simulates MongoDB concepts using Python dicts.
      For real MongoDB, install: pip install pymongo
"""

import json
from datetime import datetime
from typing import Any

# ========== WHAT IS MONGODB ==========
print("=" * 60)
print("MONGODB BASICS")
print("=" * 60)

print("""
MongoDB is a NoSQL document database:

SQL (PostgreSQL)    →  MongoDB
──────────────────────────────────
Database            →  Database
Table               →  Collection
Row                 →  Document
Column              →  Field
Primary Key         →  _id (auto-generated)
Foreign Key         →  Reference (embedded or linked)
JOIN                →  Embedded documents or $lookup

Document Structure (JSON/BSON):
{
    "_id": "507f1f77bcf86cd799439011",
    "name": "Alice",
    "age": 25,
    "address": {              # Nested document
        "city": "NYC",
        "zip": "10001"
    },
    "tags": ["python", "web"]  # Array
}
""")

# ========== SIMULATED MONGODB ==========
print("\n" + "=" * 60)
print("MONGODB OPERATIONS (Simulated)")
print("=" * 60)

class SimpleCollection:
    """Simulates MongoDB collection for learning"""
    
    def __init__(self, name: str):
        self.name = name
        self.documents = []
        self._id_counter = 1
    
    def insert_one(self, document: dict) -> dict:
        """Insert a single document"""
        doc = document.copy()
        doc["_id"] = self._id_counter
        self._id_counter += 1
        doc["created_at"] = datetime.now().isoformat()
        self.documents.append(doc)
        return {"inserted_id": doc["_id"]}
    
    def insert_many(self, documents: list) -> dict:
        """Insert multiple documents"""
        ids = []
        for doc in documents:
            result = self.insert_one(doc)
            ids.append(result["inserted_id"])
        return {"inserted_ids": ids}
    
    def find_one(self, query: dict = None) -> dict | None:
        """Find first matching document"""
        for doc in self.documents:
            if self._matches(doc, query):
                return doc
        return None
    
    def find(self, query: dict = None) -> list:
        """Find all matching documents"""
        if query is None:
            return self.documents.copy()
        return [doc for doc in self.documents if self._matches(doc, query)]
    
    def update_one(self, query: dict, update: dict) -> dict:
        """Update first matching document"""
        for doc in self.documents:
            if self._matches(doc, query):
                if "$set" in update:
                    for key, value in update["$set"].items():
                        doc[key] = value
                doc["updated_at"] = datetime.now().isoformat()
                return {"modified_count": 1}
        return {"modified_count": 0}
    
    def delete_one(self, query: dict) -> dict:
        """Delete first matching document"""
        for i, doc in enumerate(self.documents):
            if self._matches(doc, query):
                self.documents.pop(i)
                return {"deleted_count": 1}
        return {"deleted_count": 0}
    
    def count_documents(self, query: dict = None) -> int:
        """Count matching documents"""
        return len(self.find(query))
    
    def _matches(self, doc: dict, query: dict | None) -> bool:
        """Check if document matches query"""
        if query is None:
            return True
        for key, value in query.items():
            if key.startswith("$"):  # Operators
                if key == "$gt":
                    continue  # Simplified
            if key not in doc:
                return False
            if isinstance(value, dict):  # Operators
                for op, val in value.items():
                    if op == "$gt" and not doc[key] > val:
                        return False
                    if op == "$lt" and not doc[key] < val:
                        return False
                    if op == "$gte" and not doc[key] >= val:
                        return False
                    if op == "$in" and doc[key] not in val:
                        return False
            elif doc[key] != value:
                return False
        return True

# Create collection
users = SimpleCollection("users")
print(f"✅ Created collection: {users.name}")

# ========== INSERT OPERATIONS ==========
print("\n" + "=" * 60)
print("INSERT OPERATIONS")
print("=" * 60)

# Insert one document
print("\n1. insert_one():")
result = users.insert_one({
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25,
    "skills": ["Python", "MongoDB", "FastAPI"],
    "address": {
        "city": "New York",
        "country": "USA"
    }
})
print(f"   Inserted with _id: {result['inserted_id']}")

# Insert multiple documents
print("\n2. insert_many():")
new_users = [
    {
        "name": "Bob",
        "email": "bob@example.com",
        "age": 30,
        "skills": ["JavaScript", "React", "Node.js"],
        "address": {"city": "San Francisco", "country": "USA"}
    },
    {
        "name": "Charlie",
        "email": "charlie@example.com",
        "age": 22,
        "skills": ["Python", "Django", "PostgreSQL"],
        "address": {"city": "London", "country": "UK"}
    },
    {
        "name": "Diana",
        "email": "diana@example.com",
        "age": 28,
        "skills": ["Python", "FastAPI", "MongoDB"],
        "address": {"city": "Berlin", "country": "Germany"}
    }
]
result = users.insert_many(new_users)
print(f"   Inserted {len(result['inserted_ids'])} documents")

# ========== FIND OPERATIONS ==========
print("\n" + "=" * 60)
print("FIND OPERATIONS")
print("=" * 60)

# Find one
print("\n1. find_one() - Single document:")
user = users.find_one({"name": "Alice"})
if user:
    print(f"   Found: {user['name']} ({user['email']})")
    print(f"   Skills: {user['skills']}")
    print(f"   City: {user['address']['city']}")

# Find all
print("\n2. find() - All documents:")
all_users = users.find()
print(f"   Total users: {len(all_users)}")
for u in all_users:
    print(f"   - {u['name']} (age: {u['age']})")

# Find with query
print("\n3. find() with query - Age > 25:")
older_users = users.find({"age": {"$gt": 25}})
print(f"   Found {len(older_users)} users over 25:")
for u in older_users:
    print(f"   - {u['name']} (age: {u['age']})")

# ========== UPDATE OPERATIONS ==========
print("\n" + "=" * 60)
print("UPDATE OPERATIONS")
print("=" * 60)

print("\n1. update_one() with $set:")
result = users.update_one(
    {"name": "Alice"},
    {"$set": {"age": 26, "role": "Senior Developer"}}
)
print(f"   Modified {result['modified_count']} document(s)")

# Verify update
user = users.find_one({"name": "Alice"})
print(f"   Alice's new age: {user['age']}")
print(f"   Alice's new role: {user.get('role', 'N/A')}")

# ========== DELETE OPERATIONS ==========
print("\n" + "=" * 60)
print("DELETE OPERATIONS")
print("=" * 60)

print(f"\nBefore delete: {users.count_documents()} documents")

result = users.delete_one({"name": "Charlie"})
print(f"Deleted {result['deleted_count']} document(s)")

print(f"After delete: {users.count_documents()} documents")

# ========== MONGODB QUERY OPERATORS ==========
print("\n" + "=" * 60)
print("MONGODB QUERY OPERATORS (Reference)")
print("=" * 60)

print("""
COMPARISON OPERATORS:
$eq   - Equal                 {"age": {"$eq": 25}}
$ne   - Not equal             {"status": {"$ne": "inactive"}}
$gt   - Greater than          {"age": {"$gt": 18}}
$gte  - Greater or equal      {"age": {"$gte": 18}}
$lt   - Less than             {"age": {"$lt": 65}}
$lte  - Less or equal         {"age": {"$lte": 65}}
$in   - In array              {"city": {"$in": ["NYC", "LA"]}}
$nin  - Not in array          {"status": {"$nin": ["banned"]}}

LOGICAL OPERATORS:
$and  - All conditions        {"$and": [{...}, {...}]}
$or   - Any condition         {"$or": [{...}, {...}]}
$not  - Negation              {"age": {"$not": {"$gt": 25}}}
$nor  - None of conditions    {"$nor": [{...}, {...}]}

ELEMENT OPERATORS:
$exists - Field exists        {"email": {"$exists": true}}
$type   - Field type          {"age": {"$type": "int"}}

ARRAY OPERATORS:
$all      - All elements      {"tags": {"$all": ["a", "b"]}}
$elemMatch - Match element    {"results": {"$elemMatch": {...}}}
$size     - Array size        {"tags": {"$size": 3}}

REAL MONGODB EXAMPLE:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
users = db["users"]

# Find users in NYC or LA, age >= 21, sorted by name
users.find({
    "$and": [
        {"city": {"$in": ["NYC", "LA"]}},
        {"age": {"$gte": 21}}
    ]
}).sort("name", 1).limit(10)
""")

# ========== EMBEDDING VS REFERENCING ==========
print("\n" + "=" * 60)
print("EMBEDDING VS REFERENCING")
print("=" * 60)

print("""
Two approaches for relationships in MongoDB:

1. EMBEDDING (Denormalization)
   - Store related data together
   - Best for: One-to-few, data read together
   
   {
       "name": "Alice",
       "orders": [                    # Embedded
           {"product": "Book", "price": 15},
           {"product": "Pen", "price": 2}
       ]
   }

2. REFERENCING (Normalization)
   - Store references to other documents
   - Best for: One-to-many, many-to-many
   
   // users collection
   {"_id": 1, "name": "Alice"}
   
   // orders collection
   {"_id": 101, "user_id": 1, "product": "Book"}

WHEN TO USE EACH:

EMBED when:
✓ Data is accessed together
✓ Data has 1:1 or 1:few relationship
✓ Data doesn't change frequently
✓ Document size stays under 16MB

REFERENCE when:
✓ Data is accessed independently
✓ Data has 1:many or many:many relationship
✓ Data changes frequently
✓ Need to query related data separately
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Blog with Comments")
print("=" * 60)

posts = SimpleCollection("posts")

# Example blog post with embedded comments
blog_post = {
    "title": "Introduction to MongoDB",
    "author": {
        "name": "Alice",
        "email": "alice@blog.com"
    },
    "content": "MongoDB is a document database...",
    "tags": ["mongodb", "database", "nosql", "tutorial"],
    "comments": [
        {
            "author": "Bob",
            "text": "Great article!",
            "date": "2024-01-15"
        },
        {
            "author": "Charlie",
            "text": "Very helpful, thanks!",
            "date": "2024-01-16"
        }
    ],
    "views": 150,
    "likes": 42
}

posts.insert_one(blog_post)
print("✅ Created blog post with embedded comments")

# Query the post
post = posts.find_one({"title": "Introduction to MongoDB"})
print(f"\nBlog Post: {post['title']}")
print(f"Author: {post['author']['name']}")
print(f"Tags: {', '.join(post['tags'])}")
print(f"Comments ({len(post['comments'])}):")
for comment in post['comments']:
    print(f"  - {comment['author']}: {comment['text']}")

# ========== SQL VS MONGODB COMPARISON ==========
print("\n" + "=" * 60)
print("SQL VS MONGODB: WHEN TO USE")
print("=" * 60)

print("""
USE SQL (PostgreSQL/SQLite) WHEN:
✓ Data has clear, stable structure
✓ Complex relationships with JOINs
✓ Need ACID transactions
✓ Data integrity is critical
✓ Complex aggregations and reporting

Examples: Banking, inventory, CRM

USE MONGODB WHEN:
✓ Schema may evolve frequently
✓ Data is document-like (JSON)
✓ Need horizontal scaling
✓ Rapid development/prototyping
✓ Real-time analytics on diverse data

Examples: Content management, IoT, catalogs

HYBRID APPROACH:
Many modern applications use BOTH:
- SQL for critical transactional data
- MongoDB for flexible content/logs
- Redis for caching (Day 18 topic!)
""")

# ========== REAL MONGODB CONNECTION ==========
print("\n" + "=" * 60)
print("REAL MONGODB CONNECTION (Reference)")
print("=" * 60)

print("""
# Install pymongo
pip install pymongo

# Connect to MongoDB
from pymongo import MongoClient

# Local connection
client = MongoClient("mongodb://localhost:27017/")

# Remote connection with credentials
client = MongoClient(
    "mongodb://username:password@host:27017/dbname"
)

# Get database and collection
db = client["mydb"]
users = db["users"]

# CRUD operations
users.insert_one({"name": "Alice", "age": 25})
users.find_one({"name": "Alice"})
users.update_one({"name": "Alice"}, {"$set": {"age": 26}})
users.delete_one({"name": "Alice"})

# Always close connection
client.close()
""")

print("\n" + "=" * 60)
print("✅ MongoDB Basics - Complete!")
print("=" * 60)
