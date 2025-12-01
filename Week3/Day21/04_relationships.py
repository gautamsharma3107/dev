"""
Day 21 - Database Relationships
===============================
Learn: One-to-Many and Many-to-Many relationships with SQLAlchemy

Key Concepts:
- One-to-Many relationships
- Many-to-Many relationships
- Foreign keys
- Back references
- Querying related data
"""

# ========== RELATIONSHIPS OVERVIEW ==========
print("=" * 60)
print("DATABASE RELATIONSHIPS")
print("=" * 60)

relationships_overview = """
Types of Relationships:
1. One-to-One   - User has one Profile
2. One-to-Many  - User has many Posts
3. Many-to-Many - Post has many Tags, Tag has many Posts

Key SQLAlchemy Concepts:
- ForeignKey: Links child to parent
- relationship(): Creates Python relationship
- back_populates: Two-way relationship
- secondary: Association table for Many-to-Many
"""
print(relationships_overview)

# ========== ONE-TO-MANY RELATIONSHIP ==========
print("\n1. ONE-TO-MANY RELATIONSHIP")
print("-" * 40)

one_to_many = '''
# One User can have Many Posts
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    # One-to-Many: One User has many Posts
    posts = relationship("Post", back_populates="author")
    
    # One-to-Many: One User has many Comments
    comments = relationship("Comment", back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign Key: Links to User
    author_id = Column(Integer, ForeignKey("users.id"))
    
    # Many-to-One: Post belongs to one User
    author = relationship("User", back_populates="posts")
    
    # One-to-Many: Post has many Comments
    comments = relationship("Comment", back_populates="post")
'''
print(one_to_many)

# ========== MANY-TO-MANY RELATIONSHIP ==========
print("\n2. MANY-TO-MANY RELATIONSHIP")
print("-" * 40)

many_to_many = '''
# Posts and Tags have Many-to-Many relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Association table for Many-to-Many
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    
    author = relationship("User", back_populates="posts")
    
    # Many-to-Many: Post has many Tags
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    # Many-to-Many: Tag has many Posts
    posts = relationship("Post", secondary=post_tags, back_populates="tags")
'''
print(many_to_many)

# ========== SCHEMAS FOR RELATIONSHIPS ==========
print("\n3. PYDANTIC SCHEMAS FOR RELATIONSHIPS")
print("-" * 40)

schemas_code = '''
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Tag Schema
class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    
    class Config:
        from_attributes = True

# User Schemas
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True

# Post Schemas
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    tag_ids: Optional[List[int]] = []

class Post(PostBase):
    id: int
    created_at: datetime
    author_id: int
    
    class Config:
        from_attributes = True

# Nested response schemas
class PostWithAuthor(Post):
    author: User
    tags: List[Tag] = []

class UserWithPosts(User):
    posts: List[Post] = []
'''
print(schemas_code)

# ========== CRUD WITH RELATIONSHIPS ==========
print("\n4. CRUD OPERATIONS WITH RELATIONSHIPS")
print("-" * 40)

crud_relationships = '''
from sqlalchemy.orm import Session, joinedload
from typing import List

# Create post with tags
def create_post_with_tags(
    db: Session,
    post: PostCreate,
    author_id: int
) -> Post:
    # Create post
    db_post = Post(
        title=post.title,
        content=post.content,
        author_id=author_id
    )
    
    # Add tags
    if post.tag_ids:
        tags = db.query(Tag).filter(Tag.id.in_(post.tag_ids)).all()
        db_post.tags = tags
    
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Get posts with author and tags (eager loading)
def get_posts_with_relations(db: Session) -> List[Post]:
    return db.query(Post).options(
        joinedload(Post.author),
        joinedload(Post.tags)
    ).all()

# Get user with all posts
def get_user_with_posts(db: Session, user_id: int) -> User:
    return db.query(User).options(
        joinedload(User.posts)
    ).filter(User.id == user_id).first()

# Add tag to post
def add_tag_to_post(db: Session, post_id: int, tag_id: int) -> Post:
    post = db.query(Post).filter(Post.id == post_id).first()
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    
    if post and tag and tag not in post.tags:
        post.tags.append(tag)
        db.commit()
        db.refresh(post)
    
    return post

# Remove tag from post
def remove_tag_from_post(db: Session, post_id: int, tag_id: int) -> Post:
    post = db.query(Post).filter(Post.id == post_id).first()
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    
    if post and tag and tag in post.tags:
        post.tags.remove(tag)
        db.commit()
        db.refresh(post)
    
    return post
'''
print(crud_relationships)

# ========== API ROUTES WITH RELATIONSHIPS ==========
print("\n5. API ROUTES WITH RELATIONSHIPS")
print("-" * 40)

api_routes = '''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

# Create post with tags
@router.post("/posts/", response_model=PostWithAuthor)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_post_with_tags(db, post, current_user.id)

# Get all posts with author and tags
@router.get("/posts/", response_model=List[PostWithAuthor])
def get_posts(db: Session = Depends(get_db)):
    return get_posts_with_relations(db)

# Get user with all their posts
@router.get("/users/{user_id}", response_model=UserWithPosts)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_with_posts(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Add tag to post
@router.post("/posts/{post_id}/tags/{tag_id}")
def add_tag(
    post_id: int,
    tag_id: int,
    db: Session = Depends(get_db)
):
    post = add_tag_to_post(db, post_id, tag_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post or tag not found")
    return {"message": "Tag added"}

# Get posts by tag
@router.get("/tags/{tag_id}/posts", response_model=List[Post])
def get_posts_by_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag.posts
'''
print(api_routes)

# ========== COMPLETE EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE WORKING EXAMPLE")
print("=" * 60)

complete_example = '''
# relationships_example.py - Run: uvicorn relationships_example:app --reload

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from typing import List, Optional

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./relationships.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Association table
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    posts = relationship("Post", secondary=post_tags, back_populates="tags")

# Create tables
Base.metadata.create_all(bind=engine)

# Schemas
class TagSchema(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class PostSchema(BaseModel):
    id: int
    title: str
    author: UserSchema
    tags: List[TagSchema] = []
    class Config:
        from_attributes = True

class PostCreate(BaseModel):
    title: str
    tag_ids: Optional[List[int]] = []

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# App
app = FastAPI(title="Relationships API")

@app.post("/users/")
def create_user(username: str, db: Session = Depends(get_db)):
    user = User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "username": user.username}

@app.post("/tags/")
def create_tag(name: str, db: Session = Depends(get_db)):
    tag = Tag(name=name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return {"id": tag.id, "name": tag.name}

@app.post("/posts/", response_model=PostSchema)
def create_post(post: PostCreate, author_id: int, db: Session = Depends(get_db)):
    db_post = Post(title=post.title, author_id=author_id)
    if post.tag_ids:
        tags = db.query(Tag).filter(Tag.id.in_(post.tag_ids)).all()
        db_post.tags = tags
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get("/posts/", response_model=List[PostSchema])
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return [{"id": p.id, "title": p.title} for p in user.posts]
'''
print(complete_example)

print("\n" + "=" * 60)
print("✅ Database Relationships - Complete!")
print("=" * 60)
print("\nNext: Learn about API testing in 05_testing_api.py")
