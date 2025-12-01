"""
Day 21 - Authentication
=======================
Learn: Token-based authentication with JWT

Key Concepts:
- Password hashing with bcrypt
- JWT (JSON Web Tokens)
- OAuth2 with Password flow
- Protected routes
"""

# ========== AUTHENTICATION OVERVIEW ==========
print("=" * 60)
print("AUTHENTICATION")
print("=" * 60)

auth_overview = """
Authentication Flow:
1. User registers with username/password
2. Password is hashed and stored
3. User logs in with credentials
4. Server validates credentials
5. Server returns JWT token
6. Client includes token in requests
7. Server validates token for protected routes
"""
print(auth_overview)

# ========== PASSWORD HASHING ==========
print("\n1. PASSWORD HASHING")
print("-" * 40)

hashing_code = '''
from passlib.context import CryptContext

# Create password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)

# Example usage:
# hashed = hash_password("mysecretpassword")
# is_valid = verify_password("mysecretpassword", hashed)  # True
'''
print(hashing_code)

# ========== JWT TOKENS ==========
print("\n2. JWT TOKENS")
print("-" * 40)

jwt_code = '''
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# Configuration
# ⚠️ SECURITY WARNING: Never use this secret key in production!
# Generate a secure key with: openssl rand -hex 32
SECRET_KEY = "your-secret-key-change-in-production"  # CHANGE THIS IN PRODUCTION!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT access token"""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> dict:
    """Decode and validate a JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

# Example usage:
# token = create_access_token({"sub": "user@example.com"})
# payload = decode_token(token)  # {"sub": "user@example.com", "exp": ...}
'''
print(jwt_code)

# ========== USER SCHEMAS ==========
print("\n3. USER SCHEMAS")
print("-" * 40)

user_schemas = '''
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool = True
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None
'''
print(user_schemas)

# ========== USER MODEL ==========
print("\n4. USER MODEL")
print("-" * 40)

user_model = '''
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
'''
print(user_model)

# ========== OAUTH2 SETUP ==========
print("\n5. OAUTH2 SETUP")
print("-" * 40)

oauth2_code = '''
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# OAuth2 scheme - tells FastAPI where to get the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """Get current user from JWT token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = decode_token(token)
    if payload is None:
        raise credentials_exception
    
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    
    return user

async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """Ensure user is active"""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user
'''
print(oauth2_code)

# ========== AUTH ROUTES ==========
print("\n6. AUTH ROUTES")
print("-" * 40)

auth_routes = '''
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["authentication"])

# REGISTER
@router.post("/register", response_model=UserResponse, status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    # Check if user exists
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )
    
    # Create user
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# LOGIN
@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Login and get access token"""
    # Find user
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# GET CURRENT USER
@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_active_user)):
    """Get current logged in user"""
    return current_user
'''
print(auth_routes)

# ========== PROTECTED ROUTES ==========
print("\n7. PROTECTED ROUTES")
print("-" * 40)

protected_routes = '''
from fastapi import APIRouter, Depends
from typing import List

router = APIRouter(prefix="/items", tags=["items"])

# Public route - no auth required
@router.get("/public", response_model=List[ItemResponse])
def get_public_items(db: Session = Depends(get_db)):
    """Get items (public)"""
    return db.query(Item).all()

# Protected route - auth required
@router.get("/", response_model=List[ItemResponse])
def get_items(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)  # Auth required!
):
    """Get items (authenticated users only)"""
    return db.query(Item).filter(Item.owner_id == current_user.id).all()

# Protected route - admin only
@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Delete item (owner only)"""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}
'''
print(protected_routes)

# ========== COMPLETE EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE WORKING EXAMPLE")
print("=" * 60)

complete_example = '''
# auth_example.py - Run: uvicorn auth_example:app --reload

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

# App setup
app = FastAPI(title="Auth API")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Fake database
users_db = {}

# Schemas
class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Helper functions
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in users_db:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return users_db[username]

# Routes
@app.post("/register")
def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User exists")
    users_db[user.username] = User(
        username=user.username,
        hashed_password=hash_password(user.password)
    )
    return {"message": "User created"}

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username}

@app.get("/protected")
def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}!"}
'''
print(complete_example)

print("\n" + "=" * 60)
print("✅ Authentication - Complete!")
print("=" * 60)
print("\nNext: Learn about database relationships in 04_relationships.py")
