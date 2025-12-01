"""
Day 21 - CRUD Operations
========================
Learn: Create, Read, Update, Delete operations in FastAPI

Key Concepts:
- HTTP methods (POST, GET, PUT, DELETE)
- Request/Response models with Pydantic
- Path parameters and query parameters
- Error handling
"""

# ========== CRUD OVERVIEW ==========
print("=" * 60)
print("CRUD OPERATIONS")
print("=" * 60)

crud_overview = """
CRUD Operations Map to HTTP Methods:
- CREATE → POST   (Add new resource)
- READ   → GET    (Retrieve resource(s))
- UPDATE → PUT    (Update entire resource)
         → PATCH  (Update partial resource)
- DELETE → DELETE (Remove resource)
"""
print(crud_overview)

# ========== PYDANTIC SCHEMAS ==========
print("\n1. PYDANTIC SCHEMAS (schemas.py)")
print("-" * 40)

schemas_code = '''
# schemas.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

# Base schema - shared attributes
class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    in_stock: bool = True

# Create schema - for creating new items
class ItemCreate(ItemBase):
    pass

# Update schema - all fields optional
class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    in_stock: Optional[bool] = None

# Response schema - includes id and timestamps
class ItemResponse(ItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True  # Enable ORM mode
'''
print(schemas_code)

# ========== CREATE OPERATION ==========
print("\n2. CREATE OPERATION (POST)")
print("-" * 40)

create_code = '''
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

app = FastAPI()

# CREATE - Add new item
@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """Create a new item"""
    # Check if item already exists
    existing = db.query(Item).filter(Item.name == item.name).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Item with this name already exists"
        )
    
    # Create new item
    db_item = Item(
        **item.dict(),
        created_at=datetime.utcnow()
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Bulk create - Add multiple items
@app.post("/items/bulk", response_model=List[ItemResponse])
def create_items_bulk(items: List[ItemCreate], db: Session = Depends(get_db)):
    """Create multiple items at once"""
    db_items = []
    for item in items:
        db_item = Item(**item.dict(), created_at=datetime.utcnow())
        db.add(db_item)
        db_items.append(db_item)
    db.commit()
    for db_item in db_items:
        db.refresh(db_item)
    return db_items
'''
print(create_code)

# ========== READ OPERATIONS ==========
print("\n3. READ OPERATIONS (GET)")
print("-" * 40)

read_code = '''
# READ - Get all items with pagination
@app.get("/items/", response_model=List[ItemResponse])
def get_items(
    skip: int = 0,
    limit: int = 10,
    in_stock: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    """Get all items with optional filtering"""
    query = db.query(Item)
    
    # Apply filter if provided
    if in_stock is not None:
        query = query.filter(Item.in_stock == in_stock)
    
    # Apply pagination
    items = query.offset(skip).limit(limit).all()
    return items

# READ - Get single item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific item by ID"""
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return item

# READ - Search items
@app.get("/items/search/", response_model=List[ItemResponse])
def search_items(
    q: str,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    db: Session = Depends(get_db)
):
    """Search items by name"""
    query = db.query(Item).filter(Item.name.contains(q))
    
    if min_price:
        query = query.filter(Item.price >= min_price)
    if max_price:
        query = query.filter(Item.price <= max_price)
    
    return query.all()
'''
print(read_code)

# ========== UPDATE OPERATIONS ==========
print("\n4. UPDATE OPERATIONS (PUT/PATCH)")
print("-" * 40)

update_code = '''
# UPDATE - Full update (PUT)
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    item: ItemCreate,
    db: Session = Depends(get_db)
):
    """Update an item (full update)"""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    
    # Update all fields
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    
    db_item.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_item)
    return db_item

# UPDATE - Partial update (PATCH)
@app.patch("/items/{item_id}", response_model=ItemResponse)
def patch_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db)
):
    """Partially update an item"""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    
    # Update only provided fields
    update_data = item.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    db_item.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_item)
    return db_item
'''
print(update_code)

# ========== DELETE OPERATION ==========
print("\n5. DELETE OPERATION (DELETE)")
print("-" * 40)

delete_code = '''
# DELETE - Remove single item
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an item"""
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    
    db.delete(db_item)
    db.commit()
    return None  # 204 No Content

# DELETE - Remove multiple items
@app.delete("/items/", status_code=status.HTTP_200_OK)
def delete_items(item_ids: List[int], db: Session = Depends(get_db)):
    """Delete multiple items"""
    deleted_count = db.query(Item).filter(Item.id.in_(item_ids)).delete()
    db.commit()
    return {"deleted": deleted_count}
'''
print(delete_code)

# ========== COMPLETE EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE WORKING EXAMPLE")
print("=" * 60)

complete_example = '''
# Save as main.py and run: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

app = FastAPI(title="CRUD API", version="1.0.0")

# In-memory database
items_db = {}
counter = 0

# Schemas
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    in_stock: bool = True

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None

class Item(ItemCreate):
    id: int
    created_at: datetime

# CREATE
@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    global counter
    counter += 1
    new_item = Item(
        id=counter,
        created_at=datetime.utcnow(),
        **item.dict()
    )
    items_db[counter] = new_item
    return new_item

# READ all
@app.get("/items/", response_model=List[Item])
def get_items(skip: int = 0, limit: int = 10):
    items = list(items_db.values())
    return items[skip:skip + limit]

# READ one
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# UPDATE (full)
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(
        id=item_id,
        created_at=items_db[item_id].created_at,
        **item.dict()
    )
    items_db[item_id] = updated
    return updated

# UPDATE (partial)
@app.patch("/items/{item_id}", response_model=Item)
def patch_item(item_id: int, item: ItemUpdate):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    stored = items_db[item_id]
    update_data = item.dict(exclude_unset=True)
    updated = stored.copy(update=update_data)
    items_db[item_id] = updated
    return updated

# DELETE
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return None
'''
print(complete_example)

print("\n" + "=" * 60)
print("✅ CRUD Operations - Complete!")
print("=" * 60)
print("\nNext: Learn about authentication in 03_authentication.py")
