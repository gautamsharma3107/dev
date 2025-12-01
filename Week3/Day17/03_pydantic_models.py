"""
Day 17 - Pydantic Models in FastAPI
====================================
Learn: Pydantic models for data validation

Key Concepts:
- Pydantic models for request/response validation
- Field types and constraints
- Nested models
- Custom validators
"""

# ========== WHAT IS PYDANTIC? ==========
print("=" * 60)
print("INTRODUCTION TO PYDANTIC")
print("=" * 60)

print("""
Pydantic is a data validation library that uses Python type hints
to validate data. FastAPI uses Pydantic for:

1. Request body validation
2. Response model serialization
3. Settings management
4. Data parsing and coercion

Key Benefits:
- Automatic data validation
- Type coercion (converts data to correct types)
- Clear error messages
- JSON Schema generation
- IDE support and autocompletion
""")

# ========== BASIC PYDANTIC MODELS ==========
print("\n" + "=" * 60)
print("BASIC PYDANTIC MODELS")
print("=" * 60)

basic_example = '''
from pydantic import BaseModel
from typing import Optional

# Basic model
class User(BaseModel):
    name: str
    email: str
    age: int

# Model with optional fields
class Item(BaseModel):
    name: str
    description: Optional[str] = None  # Optional with default
    price: float
    tax: Optional[float] = None

# Model with default values
class Settings(BaseModel):
    debug: bool = False
    max_connections: int = 100
    api_key: str = "default-key"

# Using the models
user = User(name="John", email="john@example.com", age=30)
print(user.name)  # "John"
print(user.dict())  # {"name": "John", "email": "john@example.com", "age": 30}
print(user.json())  # JSON string

# Validation in action
item = Item(name="Laptop", price="999.99")  # String coerced to float
print(item.price)  # 999.99 (float)
'''

print("Basic Pydantic Models:")
print(basic_example)

# ========== FIELD VALIDATION ==========
print("\n" + "=" * 60)
print("FIELD VALIDATION")
print("=" * 60)

validation_example = '''
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Using Field for validation
class User(BaseModel):
    name: str = Field(
        ...,  # Required field
        min_length=2,
        max_length=50,
        description="User's full name"
    )
    email: EmailStr  # Special email validation
    age: int = Field(
        ...,
        ge=0,  # Greater than or equal to 0
        le=150,  # Less than or equal to 150
        description="User's age"
    )
    password: str = Field(
        ...,
        min_length=8,
        description="User's password"
    )

# Validation constraints:
# gt  - Greater than
# ge  - Greater than or equal
# lt  - Less than
# le  - Less than or equal
# min_length - Minimum string length
# max_length - Maximum string length
# regex - Regular expression pattern

class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0, description="Price must be positive")
    quantity: int = Field(default=0, ge=0)
    sku: str = Field(..., regex=r"^[A-Z]{3}-[0-9]{4}$")  # Format: ABC-1234
'''

print("Field Validation Example:")
print(validation_example)

# ========== USING MODELS IN FASTAPI ==========
print("\n" + "=" * 60)
print("USING MODELS IN FASTAPI")
print("=" * 60)

fastapi_example = '''
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

app = FastAPI()

# Request model
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

# Response model (doesn't include password)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# Create user - uses request model for validation
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    # user is automatically validated
    # If validation fails, FastAPI returns a 422 error
    
    # Simulate creating user
    new_user = {
        "id": 1,
        "name": user.name,
        "email": user.email
    }
    return new_user

# The response_model ensures only specified fields are returned
# Password is NOT in UserResponse, so it won't be leaked!
'''

print("Using Models in FastAPI:")
print(fastapi_example)

# ========== NESTED MODELS ==========
print("\n" + "=" * 60)
print("NESTED MODELS")
print("=" * 60)

nested_example = '''
from pydantic import BaseModel
from typing import Optional, List

# Address model
class Address(BaseModel):
    street: str
    city: str
    country: str
    zip_code: str

# User with nested address
class User(BaseModel):
    name: str
    email: str
    address: Address  # Nested model
    
# Multiple addresses
class UserWithAddresses(BaseModel):
    name: str
    email: str
    addresses: List[Address]  # List of nested models

# Example usage
user_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA",
        "zip_code": "10001"
    }
}
user = User(**user_data)

# In FastAPI
from fastapi import FastAPI
app = FastAPI()

@app.post("/users/")
def create_user(user: User):
    # Nested data is automatically validated
    return {
        "name": user.name,
        "city": user.address.city
    }
'''

print("Nested Models Example:")
print(nested_example)

# ========== CUSTOM VALIDATORS ==========
print("\n" + "=" * 60)
print("CUSTOM VALIDATORS")
print("=" * 60)

custom_validators_example = '''
from pydantic import BaseModel, validator, root_validator
from typing import List

class User(BaseModel):
    name: str
    email: str
    age: int
    tags: List[str] = []

    # Single field validator
    @validator("name")
    def name_must_have_space(cls, v):
        if " " not in v:
            raise ValueError("Name must contain first and last name")
        return v.title()  # Return modified value

    @validator("email")
    def email_must_be_valid(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email format")
        return v.lower()  # Normalize to lowercase

    @validator("age")
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Age cannot be negative")
        return v

    @validator("tags", each_item=True)
    def tags_must_be_lowercase(cls, v):
        return v.lower()

    # Root validator - access all fields
    @root_validator
    def check_consistency(cls, values):
        name = values.get("name", "")
        email = values.get("email", "")
        
        # Check if email contains part of name
        first_name = name.split()[0].lower() if " " in name else ""
        if first_name and first_name not in email:
            raise ValueError("Email should contain first name")
        
        return values

# Usage
user = User(
    name="john doe",
    email="john.doe@example.com",
    age=25,
    tags=["Python", "FastAPI"]
)
print(user.name)  # "John Doe" (title-cased)
print(user.email)  # "john.doe@example.com" (lowercased)
print(user.tags)  # ["python", "fastapi"] (lowercased)
'''

print("Custom Validators Example:")
print(custom_validators_example)

# ========== MODEL INHERITANCE ==========
print("\n" + "=" * 60)
print("MODEL INHERITANCE")
print("=" * 60)

inheritance_example = '''
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Base model with common fields
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Model for creating (no id, password required)
class UserCreate(UserBase):
    password: str

# Model for updating (all fields optional)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# Model for response (includes id, no password)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True  # Allows ORM objects

# Model for internal use (includes everything)
class UserInDB(UserBase):
    id: int
    hashed_password: str
    created_at: datetime

# Usage in FastAPI
from fastapi import FastAPI
app = FastAPI()

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    # Create user logic
    return {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "created_at": datetime.now()
    }

@app.patch("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    # Only update fields that are provided
    update_data = user.dict(exclude_unset=True)
    # Update logic...
    pass
'''

print("Model Inheritance Example:")
print(inheritance_example)

# ========== COMPLEX TYPES ==========
print("\n" + "=" * 60)
print("COMPLEX TYPES")
print("=" * 60)

complex_types_example = '''
from pydantic import BaseModel
from typing import Optional, List, Dict, Union
from datetime import datetime, date
from enum import Enum

# Enum for fixed choices
class Status(str, Enum):
    pending = "pending"
    active = "active"
    completed = "completed"
    cancelled = "cancelled"

class Task(BaseModel):
    title: str
    status: Status = Status.pending
    
# Using Union for multiple types
class Item(BaseModel):
    id: Union[int, str]  # Can be int or string
    
# Complex nested structures
class Order(BaseModel):
    id: int
    items: List[str]
    metadata: Dict[str, str]
    created_at: datetime
    scheduled_date: Optional[date] = None
    tags: List[str] = []

# Example
order = Order(
    id=1,
    items=["item1", "item2"],
    metadata={"source": "web", "priority": "high"},
    created_at=datetime.now(),
    tags=["urgent", "new"]
)
'''

print("Complex Types Example:")
print(complex_types_example)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: BLOG POST API")
print("=" * 60)

practical_example = '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

app = FastAPI()

# Status enum
class PostStatus(str, Enum):
    draft = "draft"
    published = "published"
    archived = "archived"

# Tag model
class Tag(BaseModel):
    name: str = Field(..., min_length=1, max_length=30)
    
    @validator("name")
    def lowercase_tag(cls, v):
        return v.lower()

# Author model
class Author(BaseModel):
    name: str
    email: str

# Base post model
class PostBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=200)
    content: str = Field(..., min_length=10)
    tags: List[Tag] = []
    status: PostStatus = PostStatus.draft

# Create post model
class PostCreate(PostBase):
    author_id: int

# Response model
class PostResponse(PostBase):
    id: int
    author: Author
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Update model (all optional)
class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5, max_length=200)
    content: Optional[str] = Field(None, min_length=10)
    tags: Optional[List[Tag]] = None
    status: Optional[PostStatus] = None

# In-memory storage
posts_db = {}
next_id = 1

@app.post("/posts/", response_model=PostResponse)
def create_post(post: PostCreate):
    global next_id
    new_post = {
        "id": next_id,
        "title": post.title,
        "content": post.content,
        "tags": [tag.dict() for tag in post.tags],
        "status": post.status,
        "author": {"name": "John", "email": "john@example.com"},
        "created_at": datetime.now(),
        "updated_at": None
    }
    posts_db[next_id] = new_post
    next_id += 1
    return new_post

@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts_db[post_id]

@app.patch("/posts/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post: PostUpdate):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    
    stored_post = posts_db[post_id]
    update_data = post.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        if field == "tags":
            stored_post["tags"] = [tag.dict() for tag in value]
        else:
            stored_post[field] = value
    
    stored_post["updated_at"] = datetime.now()
    return stored_post
'''

print("Blog Post API Example:")
print(practical_example)

print("\n" + "=" * 60)
print("✅ Pydantic Models - Complete!")
print("=" * 60)
print("""
Key Points to Remember:
1. Pydantic models validate incoming data automatically
2. Use Field() for constraints: min_length, max_length, gt, ge, lt, le
3. Nested models validate complex data structures
4. Custom validators with @validator and @root_validator
5. Model inheritance: Base, Create, Update, Response patterns
6. response_model in routes controls what data is returned
7. EmailStr, HttpUrl, and other special types available
""")
