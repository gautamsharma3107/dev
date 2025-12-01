"""
MINI PROJECT: Blog API
======================
Build a complete REST API for a blog platform

Features to implement:
1. User registration and authentication
2. Posts (CRUD) - belongs to user
3. Comments (CRUD) - belongs to post and user
4. Tags (Many-to-Many with posts)
5. Like system for posts

Requirements:
- FastAPI or Django REST Framework
- SQLAlchemy for database
- JWT authentication
- At least 5 unit tests
"""

# ============================================================
# PROJECT STRUCTURE
# ============================================================

project_structure = """
blog_api/
├── main.py                 # Application entry point
├── config.py               # Configuration
├── database.py             # Database setup
├── models/
│   ├── __init__.py
│   ├── user.py            # User model
│   ├── post.py            # Post model
│   ├── comment.py         # Comment model
│   └── tag.py             # Tag model
├── schemas/
│   ├── __init__.py
│   ├── user.py            # User schemas
│   ├── post.py            # Post schemas
│   ├── comment.py         # Comment schemas
│   └── tag.py             # Tag schemas
├── routers/
│   ├── __init__.py
│   ├── auth.py            # Auth routes
│   ├── posts.py           # Post routes
│   ├── comments.py        # Comment routes
│   └── tags.py            # Tag routes
├── services/
│   ├── __init__.py
│   └── auth.py            # Auth service
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_posts.py
│   └── test_comments.py
└── requirements.txt
"""
print(project_structure)

# ============================================================
# STARTER CODE
# ============================================================

print("=" * 60)
print("STARTER CODE")
print("=" * 60)

# Database models
models_code = '''
# models/user.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    bio = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")

# models/post.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# Many-to-Many: Posts and Tags
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)

# Many-to-Many: Posts and Users (Likes)
post_likes = Table(
    "post_likes",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True)
)

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")
    liked_by = relationship("User", secondary=post_likes)

# models/comment.py
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    post_id = Column(Integer, ForeignKey("posts.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")

# models/tag.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.post import post_tags

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    # Relationships
    posts = relationship("Post", secondary=post_tags, back_populates="tags")
'''
print(models_code)

# API Endpoints to implement
print("\n" + "=" * 60)
print("ENDPOINTS TO IMPLEMENT")
print("=" * 60)

endpoints = """
Authentication:
- POST /auth/register    - Register new user
- POST /auth/login       - Login and get token
- GET  /auth/me          - Get current user

Posts:
- GET    /posts/         - List all published posts (public)
- POST   /posts/         - Create new post (auth required)
- GET    /posts/{id}     - Get post details
- PUT    /posts/{id}     - Update post (author only)
- DELETE /posts/{id}     - Delete post (author only)
- POST   /posts/{id}/like     - Like a post
- DELETE /posts/{id}/like     - Unlike a post
- GET    /posts/{id}/comments - Get post comments

Comments:
- POST   /posts/{id}/comments  - Add comment to post
- PUT    /comments/{id}        - Update comment (author only)
- DELETE /comments/{id}        - Delete comment (author only)

Tags:
- GET    /tags/          - List all tags
- POST   /tags/          - Create new tag
- GET    /tags/{id}/posts - Get posts by tag

User Profile:
- GET    /users/{username}       - Get user profile
- GET    /users/{username}/posts - Get user's posts
"""
print(endpoints)

# Tests to write
print("\n" + "=" * 60)
print("TESTS TO WRITE")
print("=" * 60)

tests = """
Required Tests (minimum 5):
1. test_create_post - Test post creation
2. test_add_comment - Test adding comment to post
3. test_like_post - Test liking a post
4. test_add_tags_to_post - Test Many-to-Many tags
5. test_get_posts_by_tag - Test filtering by tag

Bonus Tests:
- test_update_own_post
- test_cannot_update_others_post
- test_delete_post_cascades_comments
- test_unlike_post
- test_pagination
"""
print(tests)

# Grading rubric
print("\n" + "=" * 60)
print("GRADING RUBRIC")
print("=" * 60)

rubric = """
Functionality (40 points):
- User auth working (10)
- Posts CRUD working (10)
- Comments CRUD working (8)
- Tags Many-to-Many working (7)
- Like system working (5)

Code Quality (20 points):
- Clean code structure (10)
- Proper use of Pydantic (5)
- Proper use of SQLAlchemy (5)

Best Practices (20 points):
- Separation of concerns (5)
- Input validation (5)
- Proper HTTP status codes (5)
- Security best practices (5)

Testing (10 points):
- At least 5 tests (5)
- Tests cover main flows (5)

Documentation (10 points):
- API docs accessible (5)
- README with setup instructions (5)

Total: 100 points
Pass: 70 points
"""
print(rubric)

print("\n" + "=" * 60)
print("Good luck building your Blog API! 🚀")
print("=" * 60)
