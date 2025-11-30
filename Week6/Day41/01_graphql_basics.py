"""
Day 41 - GraphQL Basics
=======================
Learn: GraphQL concepts, queries, mutations, and Python implementation

Key Concepts:
- GraphQL is a query language for APIs
- Single endpoint vs multiple REST endpoints
- Client specifies exact data needed
- Strongly typed schema
"""

# ========== GRAPHQL OVERVIEW ==========
print("=" * 60)
print("GRAPHQL BASICS")
print("=" * 60)

"""
GraphQL vs REST:

REST (Traditional):
- GET /users           -> Get all users
- GET /users/1         -> Get user 1
- GET /users/1/posts   -> Get user 1's posts
- Multiple requests for related data

GraphQL (Modern):
- POST /graphql        -> Single endpoint for everything
- Client asks for exactly what it needs
- Get nested/related data in one request
"""

# ========== GRAPHQL QUERY STRUCTURE ==========
print("\n" + "=" * 60)
print("GRAPHQL QUERY STRUCTURE")
print("=" * 60)

# Example Query
example_query = """
# Basic Query - Get all users with specific fields
query {
    users {
        id
        name
        email
    }
}

# Query with arguments - Get specific user
query {
    user(id: "123") {
        name
        email
        posts {
            title
            content
        }
    }
}

# Query with variables
query GetUser($userId: ID!) {
    user(id: $userId) {
        name
        email
    }
}

# Multiple queries in one request
query {
    user(id: "1") {
        name
    }
    posts(limit: 5) {
        title
    }
}
"""

print("GraphQL Query Examples:")
print(example_query)

# ========== GRAPHQL MUTATIONS ==========
print("\n" + "=" * 60)
print("GRAPHQL MUTATIONS (Data Modification)")
print("=" * 60)

mutation_examples = """
# Create a new user
mutation {
    createUser(input: {
        name: "John Doe"
        email: "john@example.com"
    }) {
        id
        name
        email
    }
}

# Update a user
mutation {
    updateUser(id: "1", input: {
        name: "John Smith"
    }) {
        id
        name
    }
}

# Delete a user
mutation {
    deleteUser(id: "1") {
        success
        message
    }
}

# Mutation with variables
mutation CreatePost($input: PostInput!) {
    createPost(input: $input) {
        id
        title
        content
        author {
            name
        }
    }
}
"""

print("GraphQL Mutation Examples:")
print(mutation_examples)

# ========== PYTHON GRAPHQL WITH GRAPHENE ==========
print("\n" + "=" * 60)
print("PYTHON GRAPHQL WITH GRAPHENE")
print("=" * 60)

print("""
To use GraphQL in Python, install graphene:
    pip install graphene
""")

# Simple example without external dependencies (simulation)
class User:
    """Simple User model for demonstration"""
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

# Simulated database
users_db = [
    User("1", "Alice Johnson", "alice@example.com"),
    User("2", "Bob Smith", "bob@example.com"),
    User("3", "Charlie Brown", "charlie@example.com"),
]

def get_all_users():
    """Resolver for getting all users"""
    return users_db

def get_user_by_id(user_id):
    """Resolver for getting user by ID"""
    for user in users_db:
        if user.id == user_id:
            return user
    return None

# Simulate GraphQL-like query execution
def execute_query(query_type, **kwargs):
    """Simulate GraphQL query execution"""
    if query_type == "users":
        users = get_all_users()
        return [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    elif query_type == "user":
        user = get_user_by_id(kwargs.get("id"))
        if user:
            return {"id": user.id, "name": user.name, "email": user.email}
        return None
    return None

# Execute simulated queries
print("\n--- Simulated GraphQL Query Results ---")

print("\n1. Query: Get all users")
result = execute_query("users")
for user in result:
    print(f"   - {user['name']} ({user['email']})")

print("\n2. Query: Get user by ID")
result = execute_query("user", id="2")
print(f"   - Found: {result['name']} ({result['email']})")

# ========== GRAPHENE SCHEMA EXAMPLE ==========
print("\n" + "=" * 60)
print("GRAPHENE SCHEMA EXAMPLE (Code Reference)")
print("=" * 60)

graphene_example = '''
import graphene

# Define GraphQL types
class UserType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    posts = graphene.List(lambda: PostType)
    
    def resolve_posts(self, info):
        # Fetch posts for this user
        return get_posts_by_user_id(self.id)

class PostType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    content = graphene.String()
    author = graphene.Field(UserType)

# Define Query class
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID(required=True))
    
    def resolve_users(self, info):
        return get_all_users()
    
    def resolve_user(self, info, id):
        return get_user_by_id(id)

# Define Mutation class
class CreateUserInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)

class CreateUser(graphene.Mutation):
    class Arguments:
        input = CreateUserInput(required=True)
    
    user = graphene.Field(UserType)
    
    def mutate(self, info, input):
        user = create_user(input.name, input.email)
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)

# Execute queries
result = schema.execute("""
    query {
        users {
            id
            name
            email
        }
    }
""")
print(result.data)
'''

print("Graphene Schema Example:")
print(graphene_example)

# ========== GRAPHQL WITH FASTAPI ==========
print("\n" + "=" * 60)
print("GRAPHQL WITH FASTAPI (Strawberry)")
print("=" * 60)

strawberry_example = '''
# Install: pip install strawberry-graphql[fastapi]

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class User:
    id: str
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: str) -> User:
        # Fetch user from database
        return User(id=id, name="John", email="john@example.com")
    
    @strawberry.field
    def users(self) -> list[User]:
        return [
            User(id="1", name="Alice", email="alice@example.com"),
            User(id="2", name="Bob", email="bob@example.com"),
        ]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        # Create user in database
        return User(id="new-id", name=name, email=email)

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# Access GraphQL playground at: http://localhost:8000/graphql
'''

print("Strawberry GraphQL with FastAPI:")
print(strawberry_example)

# ========== GRAPHQL BENEFITS AND USE CASES ==========
print("\n" + "=" * 60)
print("GRAPHQL BENEFITS AND USE CASES")
print("=" * 60)

benefits = """
✅ BENEFITS:
- No over-fetching: Get exactly what you need
- No under-fetching: Get all needed data in one request
- Strong typing: Schema defines available data
- Self-documenting: Schema serves as documentation
- Efficient: Reduces number of API calls
- Flexible: Client controls data shape

❌ CHALLENGES:
- Learning curve for teams used to REST
- Caching is more complex
- File uploads need special handling
- Rate limiting is trickier
- N+1 query problem (use DataLoader)

🎯 USE CASES:
- Mobile apps with limited bandwidth
- Complex nested data requirements
- Multiple client types (web, mobile, desktop)
- Rapid frontend development
- Public APIs with diverse clients

🚫 WHEN NOT TO USE:
- Simple CRUD with fixed data structure
- Heavy file uploads
- Real-time needs (use WebSockets)
- Small projects with tight deadlines
"""

print(benefits)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Building a Simple GraphQL API")
print("=" * 60)

practical_example = '''
# Complete GraphQL API example with Flask

from flask import Flask
from flask_graphql import GraphQLView
import graphene

# Models
class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Book:
    def __init__(self, id, title, author_id):
        self.id = id
        self.title = title
        self.author_id = author_id

# Sample data
authors = [
    Author("1", "J.K. Rowling"),
    Author("2", "George R.R. Martin"),
]

books = [
    Book("1", "Harry Potter", "1"),
    Book("2", "Game of Thrones", "2"),
    Book("3", "The Casual Vacancy", "1"),
]

# GraphQL Types
class AuthorType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    books = graphene.List(lambda: BookType)
    
    def resolve_books(self, info):
        return [b for b in books if b.author_id == self.id]

class BookType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.Field(AuthorType)
    
    def resolve_author(self, info):
        return next((a for a in authors if a.id == self.author_id), None)

# Query
class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID(required=True))
    authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.ID(required=True))
    
    def resolve_books(self, info):
        return books
    
    def resolve_book(self, info, id):
        return next((b for b in books if b.id == id), None)
    
    def resolve_authors(self, info):
        return authors
    
    def resolve_author(self, info, id):
        return next((a for a in authors if a.id == id), None)

# Create schema and app
schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)

# Example queries to try:
# 
# query {
#     books {
#         title
#         author {
#             name
#         }
#     }
# }
#
# query {
#     author(id: "1") {
#         name
#         books {
#             title
#         }
#     }
# }
'''

print("Complete GraphQL Flask Example:")
print(practical_example)

print("\n" + "=" * 60)
print("✅ GraphQL Basics - Complete!")
print("=" * 60)
