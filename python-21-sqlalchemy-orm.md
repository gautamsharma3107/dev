# SQLAlchemy ORM: Complete Guide

---

## Table of Contents
1. [Introduction to SQLAlchemy](#introduction-to-sqlalchemy)
2. [Installation and Setup](#installation-and-setup)
3. [Core vs ORM](#core-vs-orm)
4. [Models and Schemas](#models-and-schemas)
5. [Sessions and Connections](#sessions-and-connections)
6. [Queries](#queries)
7. [Relationships](#relationships)
8. [Migrations with Alembic](#migrations-with-alembic)
9. [Practical Examples](#practical-examples)
10. [Best Practices](#best-practices)
11. [Performance Tips](#performance-tips)
12. [Practice Exercises](#practice-exercises)

---

## Introduction to SQLAlchemy

### What is SQLAlchemy?

SQLAlchemy is a powerful Python SQL toolkit and Object-Relational Mapping (ORM) library.

### Two Layers

```
SQLAlchemy Architecture:

┌─────────────────────────────────────────┐
│         ORM Layer (High-level)          │  ← More Pythonic
├─────────────────────────────────────────┤
│   Declarative Base, Models, Sessions    │
├─────────────────────────────────────────┤
│         Core Layer (SQL-level)          │  ← More Control
├─────────────────────────────────────────┤
│   Connections, Engines, Raw SQL         │
├─────────────────────────────────────────┤
│      Database Drivers (psycopg2, etc)   │
├─────────────────────────────────────────┤
│      Actual Database (PostgreSQL, etc)  │
└─────────────────────────────────────────┘
```

### Why SQLAlchemy?

1. **Database Agnostic** - Switch databases without changing code
2. **Type Safety** - Models define schema clearly
3. **Relationships** - Automatic foreign key handling
4. **Query Building** - Pythonic query syntax
5. **Performance** - Lazy loading, eager loading options
6. **Migrations** - Track schema changes (with Alembic)
7. **Security** - Built-in SQL injection protection

---

## Installation and Setup

### Installing SQLAlchemy

```bash
# Basic installation
pip install sqlalchemy

# With database drivers
pip install sqlalchemy psycopg2-binary  # PostgreSQL
pip install sqlalchemy mysql-connector-python  # MySQL
pip install sqlalchemy sqlite  # SQLite (built-in)

# Full stack (ORM + migrations)
pip install sqlalchemy alembic
```

### Connection Strings

```python
from sqlalchemy import create_engine

# SQLite
engine = create_engine("sqlite:///app.db")

# SQLite (in-memory)
engine = create_engine("sqlite:///:memory:")

# PostgreSQL
engine = create_engine("postgresql://user:password@localhost:5432/dbname")
engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/dbname")

# MySQL
engine = create_engine("mysql+pymysql://user:password@localhost:3306/dbname")

# With connection pooling
engine = create_engine(
    "postgresql://user:password@localhost/dbname",
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True  # Test connections before using
)
```

---

## Core vs ORM

### SQLAlchemy Core (Low-level)

```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

engine = create_engine("sqlite:///example.db")
metadata = MetaData()

# Define table using Core
users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('email', String(100))
)

# Create tables
metadata.create_all(engine)

# Insert using Core
with engine.connect() as conn:
    insert_stmt = users_table.insert().values(
        name='Alice',
        email='alice@example.com'
    )
    conn.execute(insert_stmt)
    conn.commit()

# Query using Core
with engine.connect() as conn:
    select_stmt = select(users_table).where(users_table.c.name == 'Alice')
    result = conn.execute(select_stmt)
    for row in result:
        print(row)
```

### SQLAlchemy ORM (High-level)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("sqlite:///example.db")
Base = declarative_base()

# Define model using ORM
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

# Create tables
Base.metadata.create_all(engine)

# Insert using ORM
session = Session(engine)
user = User(name='Alice', email='alice@example.com')
session.add(user)
session.commit()

# Query using ORM
user = session.query(User).filter_by(name='Alice').first()
print(user.name, user.email)
```

### Comparison

```
Core:
✓ More control over SQL
✓ Better for complex queries
✗ More verbose
✗ Less intuitive for simple operations

ORM:
✓ Very Pythonic
✓ Less code
✓ Easier relationships
✗ Less control over generated SQL
✗ Potential performance issues if misused
```

---

## Models and Schemas

### Basic Model Definition

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
```

### Data Types

```python
from sqlalchemy import (
    Integer, String, Float, Boolean, DateTime, Date, Time,
    Text, JSON, DECIMAL, CHAR, VARCHAR, LargeBinary,
    Enum, UniqueConstraint, ForeignKey, CheckConstraint
)

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)  # Longer text
    price = Column(DECIMAL(10, 2), nullable=False)
    quantity = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    metadata = Column(JSON)  # JSON data
    status = Column(Enum('active', 'inactive', 'discontinued'), default='active')
    
    # Constraints
    __table_args__ = (
        CheckConstraint('price > 0'),
        UniqueConstraint('name', name='uq_product_name'),
    )
```

### Indexes

```python
from sqlalchemy import Index

class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Indexes
    __table_args__ = (
        Index('idx_author', 'author'),
        Index('idx_created_at', 'created_at'),
        Index('idx_author_created', 'author', 'created_at'),  # Composite
    )
```

### Validation in Models

```python
from sqlalchemy import event
from sqlalchemy.orm import validates

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    age = Column(Integer)
    
    @validates('email')
    def validate_email(self, key, value):
        if '@' not in value:
            raise ValueError("Invalid email address")
        return value
    
    @validates('age')
    def validate_age(self, key, value):
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        return value
```

---

## Sessions and Connections

### Session Basics

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///example.db")

# Create session
session = Session(engine)

# Do operations...

# Commit
session.commit()

# Rollback
session.rollback()

# Close
session.close()
```

### Context Manager Pattern (Recommended)

```python
from sqlalchemy.orm import Session

# Session closes automatically
with Session(engine) as session:
    user = User(name='Alice', email='alice@example.com')
    session.add(user)
    session.commit()
```

### Session Factory (for applications)

```python
from sqlalchemy.orm import sessionmaker, Session

# Create factory
SessionLocal = sessionmaker(bind=engine)

# Use factory
session = SessionLocal()
try:
    # Operations
    session.commit()
finally:
    session.close()

# Or with context manager
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Usage in Flask/FastAPI
@app.get("/users/")
def get_users(session: Session = Depends(get_session)):
    return session.query(User).all()
```

---

## Queries

### Basic Queries

```python
from sqlalchemy.orm import Session

session = Session(engine)

# Get all
users = session.query(User).all()

# Get one
user = session.query(User).first()

# Get by ID
user = session.query(User).get(1)

# Count
count = session.query(User).count()

# Filter
users = session.query(User).filter(User.age > 25).all()
users = session.query(User).filter_by(name='Alice').all()
```

### Where Conditions

```python
# Equal
users = session.query(User).filter(User.name == 'Alice').all()

# Not equal
users = session.query(User).filter(User.age != 25).all()

# Greater than
users = session.query(User).filter(User.age > 25).all()

# In list
users = session.query(User).filter(User.status.in_(['active', 'pending'])).all()

# Like pattern
users = session.query(User).filter(User.name.like('A%')).all()

# Is NULL
users = session.query(User).filter(User.phone == None).all()
users = session.query(User).filter(User.phone.is_(None)).all()

# Between
users = session.query(User).filter(User.age.between(20, 30)).all()
```

### Logical Operators

```python
from sqlalchemy import and_, or_, not_

# AND
users = session.query(User).filter(
    and_(User.age > 25, User.status == 'active')
).all()

# OR
users = session.query(User).filter(
    or_(User.name == 'Alice', User.name == 'Bob')
).all()

# NOT
users = session.query(User).filter(
    not_(User.status == 'inactive')
).all()

# Combined
users = session.query(User).filter(
    or_(
        and_(User.age > 25, User.status == 'active'),
        User.is_admin == True
    )
).all()
```

### Sorting and Limiting

```python
# Order by
users = session.query(User).order_by(User.name).all()
users = session.query(User).order_by(User.age.desc()).all()

# Multiple order by
users = session.query(User).order_by(User.department, User.age.desc()).all()

# Limit
users = session.query(User).limit(10).all()

# Offset (pagination)
users = session.query(User).limit(10).offset(20).all()

# Pagination helper
page = 2
per_page = 10
users = session.query(User).limit(per_page).offset((page - 1) * per_page).all()
```

### Aggregations

```python
from sqlalchemy import func

# Count
count = session.query(func.count(User.id)).scalar()

# Sum
total = session.query(func.sum(Order.amount)).scalar()

# Average
avg_age = session.query(func.avg(User.age)).scalar()

# Min/Max
min_price = session.query(func.min(Product.price)).scalar()
max_price = session.query(func.max(Product.price)).scalar()

# Group by
results = session.query(
    User.department,
    func.count(User.id).label('count'),
    func.avg(User.salary).label('avg_salary')
).group_by(User.department).all()

for dept, count, avg_salary in results:
    print(f"{dept}: {count} employees, avg salary: {avg_salary}")
```

### Distinct

```python
# Get unique values
departments = session.query(User.department).distinct().all()

# Distinct with filter
active_depts = session.query(User.department).filter(
    User.is_active == True
).distinct().all()
```

---

## Relationships

### One-to-Many

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    # Relationship
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    # Relationship
    author = relationship("Author", back_populates="books")

# Usage
session = Session(engine)
author = Author(name="J.K. Rowling")
book = Book(title="Harry Potter", author=author)
session.add(author)
session.commit()

# Query
author = session.query(Author).first()
print(author.books)  # All books by author
```

### Many-to-Many

```python
from sqlalchemy import Table

# Association table
student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    students = relationship("Student", secondary=student_course, back_populates="courses")

# Usage
session = Session(engine)
student = Student(name="Alice")
course = Course(name="Python 101")
student.courses.append(course)
session.add(student)
session.commit()

# Query
student = session.query(Student).first()
print(student.courses)  # All courses for student
```

### One-to-One

```python
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    profile = relationship("UserProfile", uselist=False, back_populates="user")

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    
    id = Column(Integer, primary_key=True)
    bio = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    
    user = relationship("User", back_populates="profile")
```

### Relationship Options

```python
# Lazy loading
relationship("Book", lazy="select")  # Default, load on access
relationship("Book", lazy="joined")  # Eager load with JOIN
relationship("Book", lazy="subquery")  # Eager load with subquery
relationship("Book", lazy="selectin")  # Separate SELECT for each parent
relationship("Book", lazy=False)  # Don't load automatically

# Cascade
relationship("Book", cascade="all, delete-orphan")
# Delete books when author is deleted

# Backref
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    books = relationship("Book", backref="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
```

---

## Migrations with Alembic

### Alembic Setup

```bash
# Install
pip install alembic

# Initialize
alembic init migrations

# This creates:
# migrations/
#   ├── alembic.ini (config)
#   ├── env.py (migration environment)
#   ├── script.py.mako (migration template)
#   └── versions/ (migration scripts)
```

### Configure Alembic

Edit `migrations/env.py`:

```python
from sqlalchemy import engine_from_config
from alembic import context
from myapp.models import Base  # Import your models

# Set target metadata
target_metadata = Base.metadata

def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = os.environ.get("DATABASE_URL")
    
    connectable = engine_from_config(
        configuration, prefix="sqlalchemy.", poolclass=pool.NullPool
    )
    
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        
        with context.begin_transaction():
            context.run_migrations()
```

### Create Migrations

```bash
# Auto-generate migration from models
alembic revision --autogenerate -m "Add users table"

# Manual migration
alembic revision -m "Custom migration"
```

### Migration File Example

```python
# migrations/versions/001_add_users_table.py

from alembic import op
import sqlalchemy as sa

revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

def downgrade() -> None:
    op.drop_table('users')
```

### Apply Migrations

```bash
# Upgrade to latest
alembic upgrade head

# Upgrade to specific version
alembic upgrade 001

# Downgrade one revision
alembic downgrade -1

# Downgrade all
alembic downgrade base

# Current version
alembic current

# History
alembic history
```

---

## Practical Examples

### Complete Blog Application

```python
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, Session, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    posts = relationship('Post', back_populates='author', cascade='all, delete-orphan')
    comments = relationship('Comment', back_populates='author', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    author = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')
    tags = relationship('Tag', secondary='post_tag', back_populates='posts')
    
    def __repr__(self):
        return f'<Post {self.title}>'

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    post = relationship('Post', back_populates='comments')
    author = relationship('User', back_populates='comments')

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    
    posts = relationship('Post', secondary='post_tag', back_populates='tags')

post_tag = Table(
    'post_tag',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

# Usage
engine = create_engine('sqlite:///blog.db')
Base.metadata.create_all(engine)

session = Session(engine)

# Create user
user = User(
    username='alice',
    email='alice@example.com',
    password_hash='hashed_password'
)

# Create post
post = Post(
    title='Python Tips',
    content='Here are some Python tips...',
    author=user
)

# Add tags
python_tag = Tag(name='python')
post.tags.append(python_tag)

# Add comment
comment = Comment(
    content='Great post!',
    post=post,
    author=user
)

session.add(user)
session.commit()

# Queries
all_posts = session.query(Post).all()
user_posts = session.query(Post).filter_by(author_id=user.id).all()
published_posts = session.query(Post).filter(Post.published == True).all()
```

---

## Best Practices

### 1. Use Context Managers

```python
# ✓ GOOD
from sqlalchemy.orm import Session

with Session(engine) as session:
    user = session.query(User).first()
    session.commit()

# Session closes automatically
```

### 2. Avoid N+1 Queries

```python
# ✗ BAD - N+1 problem
posts = session.query(Post).all()
for post in posts:
    print(post.author.name)  # Separate query for each post

# ✓ GOOD - Eager load
from sqlalchemy.orm import joinedload

posts = session.query(Post).options(
    joinedload(Post.author)
).all()
for post in posts:
    print(post.author.name)  # No additional queries
```

### 3. Use Lazy Loading Wisely

```python
# ✓ GOOD - Define lazy loading strategy
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id'))
    
    # Lazy load with 'selectin'
    author = relationship('User', lazy='selectin')
```

### 4. Session Management

```python
# ✓ GOOD - Create session factory
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
```

### 5. Error Handling

```python
from sqlalchemy.exc import IntegrityError, OperationalError

try:
    session.commit()
except IntegrityError:
    session.rollback()
    print("Duplicate data or constraint violation")
except OperationalError:
    session.rollback()
    print("Database connection error")
```

---

## Performance Tips

### 1. Use Indexes

```python
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(100), index=True)  # Index this column
    name = Column(String(100), index=True)
    
    __table_args__ = (
        Index('idx_email_name', 'email', 'name'),  # Composite index
    )
```

### 2. Connection Pooling

```python
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://user:password@localhost/db',
    pool_size=10,  # Number of connections to keep
    max_overflow=20,  # Additional connections allowed
    pool_pre_ping=True  # Test connections before use
)
```

### 3. Batch Operations

```python
# ✗ BAD - Individual inserts
for item in items:
    session.add(item)
    session.commit()

# ✓ GOOD - Batch insert
session.add_all(items)
session.commit()

# ✓ GOOD - Bulk operations
session.query(User).filter(User.age > 60).delete()
session.commit()
```

### 4. Query Optimization

```python
# ✓ GOOD - Select only needed columns
session.query(User.id, User.name).all()

# ✗ BAD - Select everything
session.query(User).all()

# ✓ GOOD - Use limit for large results
users = session.query(User).limit(100).all()
```

---

## Practice Exercises

### 1. Model Design
- Design models for e-commerce (users, products, orders, reviews)
- Define relationships properly
- Add constraints and indexes

### 2. CRUD Operations
- Create, read, update, delete with ORM
- Handle errors gracefully
- Use relationships

### 3. Complex Queries
- Multi-table queries with joins
- Aggregations with group by
- Filtering with complex conditions

### 4. Relationships
- One-to-many relationships
- Many-to-many relationships
- Query through relationships

### 5. Migrations
- Create migrations for schema changes
- Understand upgrade/downgrade
- Automate migration generation

### 6. Real-World Project
- Build complete application (blog, todo, expense tracker)
- Use all ORM features
- Implement proper error handling

---

# End of Notes
