"""
Day 20 - API Testing
====================
Learn: Testing REST APIs with pytest, mocking HTTP requests

Key Concepts:
- Testing API endpoints
- Using test clients
- Mocking external API calls
- Testing authentication
"""

import pytest
import json
from unittest.mock import Mock, patch, MagicMock
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from datetime import datetime

# Note: 'requests' is imported inside WeatherService methods to demonstrate
# mocking patterns. In production code, imports should be at the top of the file.

# ========== INTRODUCTION TO API TESTING ==========
print("=" * 60)
print("API TESTING INTRODUCTION")
print("=" * 60)

"""
Types of API Tests:
1. Unit Tests - Test individual functions/methods
2. Integration Tests - Test API endpoints with database
3. Contract Tests - Verify API follows its specification
4. End-to-End Tests - Test complete workflows

Tools for API Testing:
- pytest + requests: Simple and flexible
- FastAPI TestClient: Built-in testing support
- httpx: Modern async HTTP client
- responses: Mock responses library
"""

# ========== SIMULATED API FRAMEWORK ==========
print("\n" + "=" * 60)
print("SIMPLE API IMPLEMENTATION")
print("=" * 60)


@dataclass
class Book:
    """Book model."""
    id: int
    title: str
    author: str
    isbn: str
    published_year: int
    available: bool = True


class BookStore:
    """Simple in-memory bookstore API simulation."""
    
    def __init__(self):
        self.books: Dict[int, Book] = {}
        self.next_id = 1
    
    def get_all_books(self) -> List[Book]:
        """Get all books."""
        return list(self.books.values())
    
    def get_book(self, book_id: int) -> Optional[Book]:
        """Get book by ID."""
        return self.books.get(book_id)
    
    def search_books(self, query: str) -> List[Book]:
        """Search books by title or author."""
        query_lower = query.lower()
        return [
            book for book in self.books.values()
            if query_lower in book.title.lower() or query_lower in book.author.lower()
        ]
    
    def add_book(self, title: str, author: str, isbn: str, published_year: int) -> Book:
        """Add a new book."""
        if not title or not author:
            raise ValueError("Title and author are required")
        if not isbn or len(isbn) < 10:
            raise ValueError("Valid ISBN is required")
        
        # Check for duplicate ISBN
        for book in self.books.values():
            if book.isbn == isbn:
                raise ValueError(f"Book with ISBN {isbn} already exists")
        
        book = Book(
            id=self.next_id,
            title=title,
            author=author,
            isbn=isbn,
            published_year=published_year
        )
        self.books[self.next_id] = book
        self.next_id += 1
        return book
    
    def update_book(self, book_id: int, **kwargs) -> Optional[Book]:
        """Update book details."""
        book = self.books.get(book_id)
        if not book:
            return None
        
        for key, value in kwargs.items():
            if hasattr(book, key) and value is not None:
                setattr(book, key, value)
        return book
    
    def delete_book(self, book_id: int) -> bool:
        """Delete a book."""
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
    
    def checkout_book(self, book_id: int) -> bool:
        """Mark book as checked out."""
        book = self.books.get(book_id)
        if book and book.available:
            book.available = False
            return True
        return False
    
    def return_book(self, book_id: int) -> bool:
        """Mark book as returned."""
        book = self.books.get(book_id)
        if book and not book.available:
            book.available = True
            return True
        return False


# ========== TESTING THE API ==========
print("\n" + "=" * 60)
print("COMPREHENSIVE API TESTS")
print("=" * 60)


class TestBookStoreAPI:
    """Tests for the BookStore API."""
    
    @pytest.fixture
    def store(self):
        """Create a fresh BookStore instance."""
        return BookStore()
    
    @pytest.fixture
    def store_with_books(self):
        """Create a BookStore with sample books."""
        store = BookStore()
        store.add_book("Python Basics", "John Smith", "1234567890", 2020)
        store.add_book("Advanced Python", "Jane Doe", "0987654321", 2021)
        store.add_book("Web Development", "Bob Wilson", "1111111111", 2022)
        return store
    
    # GET /books - List all books
    def test_get_all_books_empty_store(self, store):
        """GET /books should return empty list for new store."""
        books = store.get_all_books()
        assert books == []
    
    def test_get_all_books_with_data(self, store_with_books):
        """GET /books should return all books."""
        books = store_with_books.get_all_books()
        assert len(books) == 3
    
    # GET /books/{id} - Get specific book
    def test_get_book_existing(self, store_with_books):
        """GET /books/1 should return the book."""
        book = store_with_books.get_book(1)
        assert book is not None
        assert book.title == "Python Basics"
        assert book.author == "John Smith"
    
    def test_get_book_not_found(self, store):
        """GET /books/999 should return None."""
        book = store.get_book(999)
        assert book is None
    
    # GET /books/search - Search books
    def test_search_books_by_title(self, store_with_books):
        """Search should find books by title."""
        results = store_with_books.search_books("Python")
        assert len(results) == 2
    
    def test_search_books_by_author(self, store_with_books):
        """Search should find books by author."""
        results = store_with_books.search_books("Jane")
        assert len(results) == 1
        assert results[0].author == "Jane Doe"
    
    def test_search_books_no_results(self, store_with_books):
        """Search with no matches should return empty list."""
        results = store_with_books.search_books("Nonexistent")
        assert results == []
    
    def test_search_case_insensitive(self, store_with_books):
        """Search should be case insensitive."""
        results = store_with_books.search_books("python")
        assert len(results) == 2
    
    # POST /books - Add new book
    def test_add_book_success(self, store):
        """POST /books should create a new book."""
        book = store.add_book(
            title="New Book",
            author="Author Name",
            isbn="5555555555",
            published_year=2023
        )
        assert book.id == 1
        assert book.title == "New Book"
        assert book.available == True
    
    def test_add_book_without_title_fails(self, store):
        """POST /books without title should fail."""
        with pytest.raises(ValueError) as excinfo:
            store.add_book("", "Author", "1234567890", 2023)
        assert "required" in str(excinfo.value)
    
    def test_add_book_invalid_isbn_fails(self, store):
        """POST /books with invalid ISBN should fail."""
        with pytest.raises(ValueError) as excinfo:
            store.add_book("Title", "Author", "123", 2023)
        assert "ISBN" in str(excinfo.value)
    
    def test_add_book_duplicate_isbn_fails(self, store_with_books):
        """POST /books with duplicate ISBN should fail."""
        with pytest.raises(ValueError) as excinfo:
            store_with_books.add_book("Duplicate", "Author", "1234567890", 2023)
        assert "already exists" in str(excinfo.value)
    
    # PUT /books/{id} - Update book
    def test_update_book_success(self, store_with_books):
        """PUT /books/1 should update the book."""
        updated = store_with_books.update_book(1, title="Updated Title")
        assert updated is not None
        assert updated.title == "Updated Title"
        # Other fields should remain unchanged
        assert updated.author == "John Smith"
    
    def test_update_book_not_found(self, store):
        """PUT /books/999 should return None."""
        result = store.update_book(999, title="Test")
        assert result is None
    
    def test_update_multiple_fields(self, store_with_books):
        """PUT /books/1 should update multiple fields."""
        updated = store_with_books.update_book(
            1,
            title="New Title",
            author="New Author"
        )
        assert updated.title == "New Title"
        assert updated.author == "New Author"
    
    # DELETE /books/{id} - Delete book
    def test_delete_book_success(self, store_with_books):
        """DELETE /books/1 should remove the book."""
        result = store_with_books.delete_book(1)
        assert result == True
        assert store_with_books.get_book(1) is None
    
    def test_delete_book_not_found(self, store):
        """DELETE /books/999 should return False."""
        result = store.delete_book(999)
        assert result == False
    
    # POST /books/{id}/checkout - Checkout book
    def test_checkout_book_success(self, store_with_books):
        """Checkout available book should succeed."""
        result = store_with_books.checkout_book(1)
        assert result == True
        book = store_with_books.get_book(1)
        assert book.available == False
    
    def test_checkout_unavailable_book_fails(self, store_with_books):
        """Checkout already checked out book should fail."""
        store_with_books.checkout_book(1)
        result = store_with_books.checkout_book(1)
        assert result == False
    
    def test_checkout_nonexistent_book_fails(self, store):
        """Checkout nonexistent book should fail."""
        result = store.checkout_book(999)
        assert result == False
    
    # POST /books/{id}/return - Return book
    def test_return_book_success(self, store_with_books):
        """Return checked out book should succeed."""
        store_with_books.checkout_book(1)
        result = store_with_books.return_book(1)
        assert result == True
        book = store_with_books.get_book(1)
        assert book.available == True
    
    def test_return_available_book_fails(self, store_with_books):
        """Return already available book should fail."""
        result = store_with_books.return_book(1)
        assert result == False


# ========== MOCKING HTTP REQUESTS ==========
print("\n" + "=" * 60)
print("MOCKING EXTERNAL API CALLS")
print("=" * 60)

"""
When testing code that calls external APIs, you should mock
the HTTP requests to:
1. Make tests fast (no network calls)
2. Make tests reliable (no external dependencies)
3. Test error handling
4. Control response data
"""


class WeatherService:
    """Service that fetches weather data from external API."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.weather.example.com"
    
    def get_weather(self, city: str) -> Dict[str, Any]:
        """Get weather for a city."""
        import requests
        
        response = requests.get(
            f"{self.base_url}/weather",
            params={"city": city, "key": self.api_key}
        )
        
        if response.status_code == 404:
            raise ValueError(f"City '{city}' not found")
        if response.status_code != 200:
            raise RuntimeError("Weather service unavailable")
        
        return response.json()
    
    def get_forecast(self, city: str, days: int = 5) -> List[Dict]:
        """Get weather forecast for a city."""
        import requests
        
        response = requests.get(
            f"{self.base_url}/forecast",
            params={"city": city, "days": days, "key": self.api_key}
        )
        
        if response.status_code != 200:
            raise RuntimeError("Forecast service unavailable")
        
        return response.json()["forecast"]


class TestWeatherServiceWithMocking:
    """Tests for WeatherService using mocking."""
    
    @pytest.fixture
    def weather_service(self):
        """Create WeatherService instance."""
        return WeatherService(api_key="test-api-key")
    
    @patch('requests.get')
    def test_get_weather_success(self, mock_get, weather_service):
        """Test successful weather fetch."""
        # ARRANGE
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "city": "London",
            "temperature": 15,
            "humidity": 80,
            "condition": "Cloudy"
        }
        mock_get.return_value = mock_response
        
        # ACT
        result = weather_service.get_weather("London")
        
        # ASSERT
        assert result["city"] == "London"
        assert result["temperature"] == 15
        mock_get.assert_called_once()
    
    @patch('requests.get')
    def test_get_weather_city_not_found(self, mock_get, weather_service):
        """Test weather fetch for unknown city."""
        # ARRANGE
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        # ACT & ASSERT
        with pytest.raises(ValueError) as excinfo:
            weather_service.get_weather("UnknownCity")
        assert "not found" in str(excinfo.value)
    
    @patch('requests.get')
    def test_get_weather_service_error(self, mock_get, weather_service):
        """Test weather service unavailable."""
        # ARRANGE
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        # ACT & ASSERT
        with pytest.raises(RuntimeError) as excinfo:
            weather_service.get_weather("London")
        assert "unavailable" in str(excinfo.value)
    
    @patch('requests.get')
    def test_get_forecast_success(self, mock_get, weather_service):
        """Test successful forecast fetch."""
        # ARRANGE
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "city": "Paris",
            "forecast": [
                {"day": "Monday", "temp": 20},
                {"day": "Tuesday", "temp": 22},
                {"day": "Wednesday", "temp": 19}
            ]
        }
        mock_get.return_value = mock_response
        
        # ACT
        result = weather_service.get_forecast("Paris", days=3)
        
        # ASSERT
        assert len(result) == 3
        assert result[0]["day"] == "Monday"


# ========== TESTING WITH FASTAPI ==========
print("\n" + "=" * 60)
print("FASTAPI TESTING EXAMPLE")
print("=" * 60)

"""
FastAPI provides TestClient for easy testing:

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
"""

# Simulated FastAPI-style testing
class APIClient:
    """Simulated API test client."""
    
    def __init__(self, store: BookStore):
        self.store = store
    
    def get(self, path: str) -> Dict:
        """Simulate GET request."""
        if path == "/books":
            books = self.store.get_all_books()
            return {
                "status_code": 200,
                "json": [{"id": b.id, "title": b.title} for b in books]
            }
        elif path.startswith("/books/"):
            book_id = int(path.split("/")[-1])
            book = self.store.get_book(book_id)
            if book:
                return {"status_code": 200, "json": {"id": book.id, "title": book.title}}
            return {"status_code": 404, "json": {"error": "Not found"}}
        return {"status_code": 404, "json": {"error": "Not found"}}
    
    def post(self, path: str, json: Dict) -> Dict:
        """Simulate POST request."""
        if path == "/books":
            try:
                book = self.store.add_book(
                    title=json.get("title", ""),
                    author=json.get("author", ""),
                    isbn=json.get("isbn", ""),
                    published_year=json.get("published_year", 2023)
                )
                return {
                    "status_code": 201,
                    "json": {"id": book.id, "title": book.title}
                }
            except ValueError as e:
                return {"status_code": 400, "json": {"error": str(e)}}
        return {"status_code": 404, "json": {"error": "Not found"}}
    
    def delete(self, path: str) -> Dict:
        """Simulate DELETE request."""
        if path.startswith("/books/"):
            book_id = int(path.split("/")[-1])
            if self.store.delete_book(book_id):
                return {"status_code": 204, "json": None}
            return {"status_code": 404, "json": {"error": "Not found"}}
        return {"status_code": 404, "json": {"error": "Not found"}}


class TestAPIClientStyle:
    """Tests using API client style (like FastAPI TestClient)."""
    
    @pytest.fixture
    def client(self):
        """Create API client with fresh store."""
        store = BookStore()
        return APIClient(store)
    
    @pytest.fixture
    def client_with_data(self):
        """Create API client with sample data."""
        store = BookStore()
        store.add_book("Test Book", "Test Author", "1234567890", 2023)
        return APIClient(store)
    
    def test_get_books_empty(self, client):
        """GET /books returns empty list."""
        response = client.get("/books")
        assert response["status_code"] == 200
        assert response["json"] == []
    
    def test_get_books_with_data(self, client_with_data):
        """GET /books returns book list."""
        response = client_with_data.get("/books")
        assert response["status_code"] == 200
        assert len(response["json"]) == 1
    
    def test_get_book_by_id(self, client_with_data):
        """GET /books/1 returns book."""
        response = client_with_data.get("/books/1")
        assert response["status_code"] == 200
        assert response["json"]["title"] == "Test Book"
    
    def test_get_book_not_found(self, client):
        """GET /books/999 returns 404."""
        response = client.get("/books/999")
        assert response["status_code"] == 404
    
    def test_create_book(self, client):
        """POST /books creates new book."""
        response = client.post("/books", {
            "title": "New Book",
            "author": "Author",
            "isbn": "9999999999",
            "published_year": 2023
        })
        assert response["status_code"] == 201
        assert response["json"]["title"] == "New Book"
    
    def test_create_book_validation_error(self, client):
        """POST /books with invalid data returns 400."""
        response = client.post("/books", {
            "title": "",
            "author": "Author",
            "isbn": "1234567890",
            "published_year": 2023
        })
        assert response["status_code"] == 400
        assert "error" in response["json"]
    
    def test_delete_book(self, client_with_data):
        """DELETE /books/1 removes book."""
        response = client_with_data.delete("/books/1")
        assert response["status_code"] == 204
        
        # Verify book is deleted
        get_response = client_with_data.get("/books/1")
        assert get_response["status_code"] == 404
    
    def test_delete_book_not_found(self, client):
        """DELETE /books/999 returns 404."""
        response = client.delete("/books/999")
        assert response["status_code"] == 404


# ========== TESTING AUTHENTICATION ==========
print("\n" + "=" * 60)
print("TESTING AUTHENTICATION")
print("=" * 60)


class AuthenticatedAPI:
    """API with authentication."""
    
    def __init__(self):
        self.tokens = {}  # token -> user_id
        self.users = {}   # user_id -> user_data
    
    def login(self, username: str, password: str) -> Optional[str]:
        """Authenticate user and return token."""
        # Simplified authentication
        if username == "admin" and password == "admin123":
            token = f"token_{username}_{datetime.now().timestamp()}"
            self.tokens[token] = username
            return token
        return None
    
    def verify_token(self, token: str) -> Optional[str]:
        """Verify token and return username."""
        return self.tokens.get(token)
    
    def get_protected_resource(self, token: str) -> Dict:
        """Access protected resource."""
        username = self.verify_token(token)
        if not username:
            raise PermissionError("Invalid or missing token")
        return {"message": f"Hello, {username}!", "data": "secret"}


class TestAuthentication:
    """Tests for authentication."""
    
    @pytest.fixture
    def api(self):
        """Create API instance."""
        return AuthenticatedAPI()
    
    def test_login_success(self, api):
        """Valid credentials should return token."""
        token = api.login("admin", "admin123")
        assert token is not None
        assert token.startswith("token_")
    
    def test_login_invalid_credentials(self, api):
        """Invalid credentials should return None."""
        token = api.login("admin", "wrongpassword")
        assert token is None
    
    def test_access_protected_with_valid_token(self, api):
        """Valid token should allow access."""
        token = api.login("admin", "admin123")
        result = api.get_protected_resource(token)
        assert result["message"] == "Hello, admin!"
    
    def test_access_protected_with_invalid_token(self, api):
        """Invalid token should raise error."""
        with pytest.raises(PermissionError):
            api.get_protected_resource("invalid_token")
    
    def test_access_protected_without_token(self, api):
        """Missing token should raise error."""
        with pytest.raises(PermissionError):
            api.get_protected_resource("")


print("\n" + "=" * 60)
print("✅ API Testing - Complete!")
print("=" * 60)
print("\nRun: pytest 03_api_testing.py -v")
