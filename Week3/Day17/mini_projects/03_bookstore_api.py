"""
MINI PROJECT 3: Book Store API (Complete Solution)
===================================================
A complete Book Store API demonstrating all FastAPI concepts from Day 17.

This is a fully implemented example that you can study and learn from.

Features:
- Complete CRUD operations
- Pydantic models with validation
- Custom validators
- Error handling
- Pagination and filtering
- Response models
- Proper status codes
- API documentation

Run with: uvicorn 03_bookstore_api:app --reload
Test at: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, status, Query, Path
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

# ========== ENUMS ==========

class Genre(str, Enum):
    fiction = "fiction"
    non_fiction = "non-fiction"
    science = "science"
    technology = "technology"
    history = "history"
    biography = "biography"
    other = "other"


# ========== MODELS ==========

class BookBase(BaseModel):
    """Base book model with common fields."""
    title: str = Field(..., min_length=1, max_length=200, description="Book title")
    author: str = Field(..., min_length=1, max_length=100, description="Author name")
    genre: Genre = Field(default=Genre.other, description="Book genre")
    price: float = Field(..., gt=0, description="Book price")
    isbn: Optional[str] = Field(None, regex=r"^\d{10}(\d{3})?$", description="ISBN-10 or ISBN-13")
    description: Optional[str] = Field(None, max_length=1000)
    
    @validator('title', 'author')
    def strip_and_title_case(cls, v):
        return v.strip().title()


class BookCreate(BookBase):
    """Model for creating a new book."""
    stock: int = Field(default=0, ge=0, description="Initial stock quantity")


class BookUpdate(BaseModel):
    """Model for updating a book (all fields optional)."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    genre: Optional[Genre] = None
    price: Optional[float] = Field(None, gt=0)
    isbn: Optional[str] = Field(None, regex=r"^\d{10}(\d{3})?$")
    description: Optional[str] = Field(None, max_length=1000)
    stock: Optional[int] = Field(None, ge=0)


class BookResponse(BookBase):
    """Response model for a book."""
    id: int
    stock: int
    in_stock: bool
    created_at: datetime
    updated_at: Optional[datetime]


class PaginatedResponse(BaseModel):
    """Paginated response wrapper."""
    total: int
    page: int
    per_page: int
    books: List[BookResponse]


# ========== APP SETUP ==========

app = FastAPI(
    title="Book Store API",
    description="""
    A complete Book Store API built with FastAPI.
    
    ## Features
    - 📚 Full CRUD operations for books
    - 🔍 Search and filter books
    - 📄 Pagination support
    - ✅ Input validation with Pydantic
    - 📖 Automatic API documentation
    """,
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@bookstore.example.com"
    }
)

# In-memory database
books_db = {}
next_id = 1


# ========== SEED DATA ==========

def seed_data():
    """Add some sample books to the database."""
    global next_id
    sample_books = [
        {
            "title": "The Python Guide",
            "author": "John Smith",
            "genre": Genre.technology,
            "price": 39.99,
            "isbn": "1234567890",
            "description": "A comprehensive guide to Python programming",
            "stock": 50
        },
        {
            "title": "FastAPI Mastery",
            "author": "Jane Doe",
            "genre": Genre.technology,
            "price": 44.99,
            "isbn": "0987654321",
            "description": "Master FastAPI framework",
            "stock": 30
        },
        {
            "title": "The Great Novel",
            "author": "Famous Writer",
            "genre": Genre.fiction,
            "price": 14.99,
            "isbn": "1111111111",
            "description": "A captivating story",
            "stock": 0
        }
    ]
    
    for book_data in sample_books:
        books_db[next_id] = {
            "id": next_id,
            **book_data,
            "in_stock": book_data["stock"] > 0,
            "created_at": datetime.utcnow(),
            "updated_at": None
        }
        next_id += 1

seed_data()


# ========== HELPER FUNCTIONS ==========

def get_book_or_404(book_id: int) -> dict:
    """Get a book by ID or raise 404."""
    if book_id not in books_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return books_db[book_id]


# ========== ENDPOINTS ==========

@app.get("/", tags=["root"])
def root():
    """Welcome endpoint with API information."""
    return {
        "message": "Welcome to Book Store API",
        "version": "1.0.0",
        "documentation": "/docs",
        "endpoints": {
            "books": "/books/",
            "search": "/books/search/"
        }
    }


@app.get("/books/", response_model=PaginatedResponse, tags=["books"])
def get_books(
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(10, ge=1, le=50, description="Items per page"),
    genre: Optional[Genre] = Query(None, description="Filter by genre"),
    in_stock: Optional[bool] = Query(None, description="Filter by stock availability"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price")
):
    """
    Get all books with filtering and pagination.
    
    - **page**: Page number (starts from 1)
    - **per_page**: Number of items per page (1-50)
    - **genre**: Filter by book genre
    - **in_stock**: Filter by stock availability
    - **min_price**: Minimum price filter
    - **max_price**: Maximum price filter
    """
    books = list(books_db.values())
    
    # Apply filters
    if genre:
        books = [b for b in books if b["genre"] == genre]
    
    if in_stock is not None:
        books = [b for b in books if b["in_stock"] == in_stock]
    
    if min_price is not None:
        books = [b for b in books if b["price"] >= min_price]
    
    if max_price is not None:
        books = [b for b in books if b["price"] <= max_price]
    
    # Calculate pagination
    total = len(books)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = books[start:end]
    
    return {
        "total": total,
        "page": page,
        "per_page": per_page,
        "books": paginated_books
    }


@app.get("/books/search/", response_model=List[BookResponse], tags=["books"])
def search_books(
    q: str = Query(..., min_length=2, description="Search query"),
    limit: int = Query(10, ge=1, le=50, description="Maximum results")
):
    """
    Search books by title or author.
    
    - **q**: Search query (min 2 characters)
    - **limit**: Maximum number of results
    """
    query = q.lower()
    results = [
        book for book in books_db.values()
        if query in book["title"].lower() or query in book["author"].lower()
    ]
    return results[:limit]


@app.post("/books/", response_model=BookResponse, status_code=status.HTTP_201_CREATED, tags=["books"])
def create_book(book: BookCreate):
    """
    Add a new book to the store.
    
    - **title**: Book title (required)
    - **author**: Author name (required)
    - **genre**: Book genre
    - **price**: Book price (must be positive)
    - **isbn**: ISBN number (optional)
    - **description**: Book description (optional)
    - **stock**: Initial stock quantity
    """
    global next_id
    
    new_book = {
        "id": next_id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "price": book.price,
        "isbn": book.isbn,
        "description": book.description,
        "stock": book.stock,
        "in_stock": book.stock > 0,
        "created_at": datetime.utcnow(),
        "updated_at": None
    }
    
    books_db[next_id] = new_book
    next_id += 1
    
    return new_book


@app.get("/books/{book_id}", response_model=BookResponse, tags=["books"])
def get_book(book_id: int = Path(..., gt=0, description="Book ID")):
    """
    Get a specific book by ID.
    
    - **book_id**: The ID of the book to retrieve
    """
    return get_book_or_404(book_id)


@app.put("/books/{book_id}", response_model=BookResponse, tags=["books"])
def update_book(
    book_id: int = Path(..., gt=0),
    book: BookCreate = ...
):
    """
    Update a book completely.
    
    - **book_id**: The ID of the book to update
    """
    get_book_or_404(book_id)
    
    updated_book = {
        "id": book_id,
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "price": book.price,
        "isbn": book.isbn,
        "description": book.description,
        "stock": book.stock,
        "in_stock": book.stock > 0,
        "created_at": books_db[book_id]["created_at"],
        "updated_at": datetime.utcnow()
    }
    
    books_db[book_id] = updated_book
    return updated_book


@app.patch("/books/{book_id}", response_model=BookResponse, tags=["books"])
def partial_update_book(
    book_id: int = Path(..., gt=0),
    book: BookUpdate = ...
):
    """
    Partially update a book.
    
    - **book_id**: The ID of the book to update
    """
    stored_book = get_book_or_404(book_id)
    
    update_data = book.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        stored_book[field] = value
    
    # Update in_stock based on stock
    if "stock" in update_data:
        stored_book["in_stock"] = stored_book["stock"] > 0
    
    stored_book["updated_at"] = datetime.utcnow()
    
    return stored_book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["books"])
def delete_book(book_id: int = Path(..., gt=0)):
    """
    Delete a book from the store.
    
    - **book_id**: The ID of the book to delete
    """
    get_book_or_404(book_id)
    del books_db[book_id]
    return None


@app.post("/books/{book_id}/restock", response_model=BookResponse, tags=["books"])
def restock_book(
    book_id: int = Path(..., gt=0),
    quantity: int = Query(..., gt=0, description="Quantity to add")
):
    """
    Add stock to a book.
    
    - **book_id**: The ID of the book to restock
    - **quantity**: Number of copies to add
    """
    book = get_book_or_404(book_id)
    book["stock"] += quantity
    book["in_stock"] = True
    book["updated_at"] = datetime.utcnow()
    return book


@app.get("/books/stats/summary", tags=["stats"])
def get_stats():
    """Get book store statistics."""
    books = list(books_db.values())
    
    if not books:
        return {"message": "No books in the store"}
    
    total_books = len(books)
    total_stock = sum(b["stock"] for b in books)
    in_stock_count = sum(1 for b in books if b["in_stock"])
    avg_price = sum(b["price"] for b in books) / total_books
    
    genre_counts = {}
    for book in books:
        genre = book["genre"]
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    
    return {
        "total_books": total_books,
        "total_stock": total_stock,
        "in_stock_count": in_stock_count,
        "out_of_stock_count": total_books - in_stock_count,
        "average_price": round(avg_price, 2),
        "books_by_genre": genre_counts
    }


# Run with: uvicorn 03_bookstore_api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
