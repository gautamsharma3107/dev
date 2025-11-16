# Python Project Ideas: Complete Implementation Guide

---

## Table of Contents
1. [Introduction](#introduction)
2. [Project 1: Library Management System](#project-1-library-management-system)
3. [Project 2: Custom Logging Framework](#project-2-custom-logging-framework)
4. [Project 3: Data Parser (CSV to JSON)](#project-3-data-parser-csv-to-json)
5. [Project 4: Decorator-Based Caching System](#project-4-decorator-based-caching-system)
6. [Project 5: Command-Line Tool with argparse](#project-5-command-line-tool-with-argparse)
7. [Testing and Debugging](#testing-and-debugging)
8. [Deployment Tips](#deployment-tips)

---

## Introduction

### Project-Based Learning

These projects consolidate knowledge from all previous guides:
- Data structures (lists, dicts, OOP)
- Exception handling
- File I/O
- Decorators and advanced concepts
- Standard library modules
- Functional programming

### Learning Outcomes

Each project teaches:
- Real-world problem solving
- Code organization
- Testing practices
- User interaction
- Error handling

---

## Project 1: Library Management System

### Overview

Build a complete library management system using OOP principles.

### Requirements

1. Manage books (add, remove, search)
2. Manage members (register, remove)
3. Track borrowing/returning books
4. Store data persistently (JSON)
5. Generate reports

### Project Structure

```
library_system/
├── main.py
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   └── library.py
├── utils/
│   ├── __init__.py
│   └── storage.py
├── data/
│   └── library_data.json
└── requirements.txt
```

### Implementation

#### models/book.py

```python
from datetime import datetime, timedelta
from enum import Enum

class BookStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"

class Book:
    def __init__(self, book_id, title, author, isbn, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.available_copies = copies
        self.status = BookStatus.AVAILABLE
    
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self.available_copies < self.copies:
            self.available_copies += 1
            return True
        return False
    
    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "copies": self.copies,
            "available_copies": self.available_copies
        }
    
    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["isbn"],
            data["copies"]
        )
        book.available_copies = data.get("available_copies", data["copies"])
        return book
```

#### models/member.py

```python
from datetime import datetime

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
        self.registration_date = datetime.now()
    
    def borrow_book(self, book_id):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            return True
        return False
    
    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": self.borrowed_books,
            "registration_date": self.registration_date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        member = cls(data["member_id"], data["name"], data["email"])
        member.borrowed_books = data.get("borrowed_books", [])
        return member
```

#### models/library.py

```python
import json
from typing import List, Optional
from .book import Book
from .member import Member

class Library:
    def __init__(self):
        self.books: dict = {}
        self.members: dict = {}
    
    # Book management
    def add_book(self, book: Book):
        if book.book_id in self.books:
            raise ValueError(f"Book {book.book_id} already exists")
        self.books[book.book_id] = book
    
    def remove_book(self, book_id):
        if book_id not in self.books:
            raise ValueError(f"Book {book_id} not found")
        del self.books[book_id]
    
    def search_books(self, query: str) -> List[Book]:
        query = query.lower()
        results = []
        for book in self.books.values():
            if (query in book.title.lower() or 
                query in book.author.lower() or 
                query in book.isbn):
                results.append(book)
        return results
    
    def get_book(self, book_id) -> Optional[Book]:
        return self.books.get(book_id)
    
    # Member management
    def register_member(self, member: Member):
        if member.member_id in self.members:
            raise ValueError(f"Member {member.member_id} already exists")
        self.members[member.member_id] = member
    
    def remove_member(self, member_id):
        member = self.members.get(member_id)
        if not member:
            raise ValueError(f"Member {member_id} not found")
        if member.borrowed_books:
            raise ValueError(f"Member has {len(member.borrowed_books)} borrowed books")
        del self.members[member_id]
    
    def get_member(self, member_id) -> Optional[Member]:
        return self.members.get(member_id)
    
    # Borrowing
    def borrow_book(self, member_id: str, book_id: str) -> bool:
        member = self.get_member(member_id)
        book = self.get_book(book_id)
        
        if not member:
            raise ValueError(f"Member {member_id} not found")
        if not book:
            raise ValueError(f"Book {book_id} not found")
        
        if book.borrow():
            member.borrow_book(book_id)
            return True
        return False
    
    def return_book(self, member_id: str, book_id: str) -> bool:
        member = self.get_member(member_id)
        book = self.get_book(book_id)
        
        if not member:
            raise ValueError(f"Member {member_id} not found")
        if not book:
            raise ValueError(f"Book {book_id} not found")
        
        if book.return_book():
            member.return_book(book_id)
            return True
        return False
    
    # Reports
    def get_available_books(self) -> List[Book]:
        return [book for book in self.books.values() if book.available_copies > 0]
    
    def get_member_borrowed_books(self, member_id: str) -> List[Book]:
        member = self.get_member(member_id)
        if not member:
            raise ValueError(f"Member {member_id} not found")
        
        return [self.books[book_id] for book_id in member.borrowed_books]
    
    def get_library_stats(self) -> dict:
        return {
            "total_books": len(self.books),
            "total_members": len(self.members),
            "available_books": len(self.get_available_books()),
            "borrowed_books": sum(
                book.copies - book.available_copies 
                for book in self.books.values()
            )
        }
```

#### utils/storage.py

```python
import json
from pathlib import Path
from ..models.book import Book
from ..models.member import Member

class LibraryStorage:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
    
    def save(self, library):
        data = {
            "books": {bid: book.to_dict() for bid, book in library.books.items()},
            "members": {mid: member.to_dict() for mid, member in library.members.items()}
        }
        
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)
    
    def load(self, library):
        if not self.filepath.exists():
            return
        
        with open(self.filepath, "r") as f:
            data = json.load(f)
        
        for book_data in data.get("books", {}).values():
            book = Book.from_dict(book_data)
            library.books[book.book_id] = book
        
        for member_data in data.get("members", {}).values():
            member = Member.from_dict(member_data)
            library.members[member.member_id] = member
```

#### main.py

```python
from models.library import Library
from models.book import Book
from models.member import Member
from utils.storage import LibraryStorage

def main():
    # Initialize
    library = Library()
    storage = LibraryStorage("data/library_data.json")
    storage.load(library)
    
    # Add sample books
    if not library.books:
        books = [
            Book("1", "Python Mastery", "John Smith", "978-1234567890"),
            Book("2", "Data Science 101", "Jane Doe", "978-0987654321", 2),
            Book("3", "Web Development", "Bob Johnson", "978-1122334455")
        ]
        for book in books:
            library.add_book(book)
    
    # Add sample members
    if not library.members:
        members = [
            Member("M1", "Alice", "alice@example.com"),
            Member("M2", "Bob", "bob@example.com")
        ]
        for member in members:
            library.register_member(member)
    
    # Operations
    print("=== Library Management System ===\n")
    
    # Search
    print("Searching for 'Python':")
    results = library.search_books("Python")
    for book in results:
        print(f"  - {book.title} by {book.author}")
    
    # Borrow
    print("\nBorrowing book...")
    library.borrow_book("M1", "1")
    print("✓ Book borrowed successfully")
    
    # View stats
    print("\nLibrary Statistics:")
    stats = library.get_library_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Save
    storage.save(library)
    print("\n✓ Data saved")

if __name__ == "__main__":
    main()
```

---

## Project 2: Custom Logging Framework

### Overview

Build a flexible, reusable logging framework with multiple outputs.

### Features

1. Multiple log levels
2. File and console output
3. Rotating file handlers
4. Custom formatting
5. Singleton pattern

### Implementation

```python
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import os
from enum import Enum

class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.logger = logging.getLogger("CustomLogger")
        self.logger.setLevel(logging.DEBUG)
        
        # Ensure log directory exists
        os.makedirs("logs", exist_ok=True)
        
        # Format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler with rotation
        file_handler = RotatingFileHandler(
            "logs/app.log",
            maxBytes=1000000,  # 1MB
            backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
        self._initialized = True
    
    def debug(self, message):
        self.logger.debug(message)
    
    def info(self, message):
        self.logger.info(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def critical(self, message):
        self.logger.critical(message)

# Usage
logger = Logger()
logger.info("Application started")
logger.debug("Debug information")
logger.error("An error occurred")
```

---

## Project 3: Data Parser (CSV to JSON)

### Overview

Convert CSV files to JSON format with data validation and transformation.

### Features

1. Read CSV files
2. Validate data
3. Transform types
4. Write JSON output
5. Error handling

### Implementation

```python
import csv
import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

class DataParser:
    def __init__(self):
        self.data = []
    
    def read_csv(self, filepath: str) -> List[Dict]:
        """Read CSV file and return list of dictionaries"""
        self.data = []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.data.append(row)
        
        return self.data
    
    def validate_data(self, schema: Dict[str, type]) -> bool:
        """Validate data against schema"""
        for record in self.data:
            for field, field_type in schema.items():
                if field not in record:
                    raise ValueError(f"Missing field: {field}")
                
                value = record[field]
                if not self._validate_type(value, field_type):
                    raise ValueError(
                        f"Invalid type for {field}: expected {field_type.__name__}"
                    )
        return True
    
    def _validate_type(self, value: str, field_type: type) -> bool:
        """Validate value against type"""
        try:
            if field_type == int:
                int(value)
            elif field_type == float:
                float(value)
            elif field_type == bool:
                value.lower() in ['true', 'false', '1', '0', 'yes', 'no']
            return True
        except (ValueError, AttributeError):
            return False
    
    def transform_data(self, transformations: Dict[str, callable]):
        """Apply transformations to data"""
        for record in self.data:
            for field, transform_func in transformations.items():
                if field in record:
                    try:
                        record[field] = transform_func(record[field])
                    except Exception as e:
                        print(f"Error transforming {field}: {e}")
    
    def to_json(self, output_filepath: str, indent: int = 2):
        """Write data to JSON file"""
        with open(output_filepath, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=indent)
    
    def filter_data(self, condition: callable) -> List[Dict]:
        """Filter data based on condition"""
        return [record for record in self.data if condition(record)]

# Usage
parser = DataParser()
parser.read_csv("data/input.csv")

# Define schema
schema = {
    "name": str,
    "age": int,
    "salary": float
}

# Validate
parser.validate_data(schema)

# Transform
transformations = {
    "name": str.upper,
    "age": int,
    "salary": float
}
parser.transform_data(transformations)

# Write output
parser.to_json("data/output.json")
```

---

## Project 4: Decorator-Based Caching System

### Overview

Implement a flexible caching system using decorators.

### Features

1. LRU cache
2. TTL (time-to-live)
3. Manual cache invalidation
4. Cache statistics

### Implementation

```python
from functools import wraps
from collections import OrderedDict
from datetime import datetime, timedelta
import time

class Cache:
    def __init__(self, max_size: int = 128):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.hits = 0
        self.misses = 0
    
    def get(self, key):
        if key in self.cache:
            self.hits += 1
            value, timestamp = self.cache[key]
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return value
        self.misses += 1
        return None
    
    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = (value, datetime.now())
        
        # Remove oldest if over capacity
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)
    
    def clear(self):
        self.cache.clear()
        self.hits = 0
        self.misses = 0
    
    def stats(self):
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": f"{hit_rate:.2f}%",
            "size": len(self.cache)
        }

# Decorator with TTL
def cached(ttl: int = None):
    """Decorator for caching function results"""
    cache = {}
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            
            if key in cache:
                value, timestamp = cache[key]
                
                # Check TTL
                if ttl is None or (datetime.now() - timestamp).seconds < ttl:
                    return value
            
            result = func(*args, **kwargs)
            cache[key] = (result, datetime.now())
            return result
        
        wrapper.cache = cache
        wrapper.clear_cache = lambda: cache.clear()
        return wrapper
    return decorator

# Usage
@cached(ttl=60)
def expensive_computation(n):
    time.sleep(1)
    return n ** n

print(expensive_computation(5))  # Computed (1 second)
print(expensive_computation(5))  # Cached (instant)

expensive_computation.clear_cache()  # Manual clear
```

---

## Project 5: Command-Line Tool with argparse

### Overview

Build a multi-purpose CLI tool with subcommands.

### Features

1. Multiple subcommands
2. Argument validation
3. Help documentation
4. Error handling

### Implementation

```python
import argparse
import json
from pathlib import Path
from typing import List

class ConfigManager:
    """Manage application configuration"""
    
    def __init__(self, config_file: str = "config.json"):
        self.config_file = Path(config_file)
        self.config = {}
        self.load()
    
    def load(self):
        if self.config_file.exists():
            with open(self.config_file) as f:
                self.config = json.load(f)
    
    def save(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def set(self, key: str, value):
        self.config[key] = value
        self.save()
    
    def get(self, key: str, default=None):
        return self.config.get(key, default)

def cmd_config(args, config: ConfigManager):
    """Handle config commands"""
    if args.action == "set":
        config.set(args.key, args.value)
        print(f"✓ Set {args.key} = {args.value}")
    elif args.action == "get":
        value = config.get(args.key)
        if value:
            print(f"{args.key} = {value}")
        else:
            print(f"Key {args.key} not found")
    elif args.action == "list":
        for key, value in config.config.items():
            print(f"  {key}: {value}")

def cmd_files(args):
    """Handle file commands"""
    if args.action == "list":
        path = Path(args.directory or ".")
        files = list(path.glob(args.pattern or "*"))
        for f in sorted(files):
            print(f"  {f}")
    elif args.action == "count":
        path = Path(args.directory or ".")
        count = len(list(path.glob("**/*")))
        print(f"Total items: {count}")

def main():
    parser = argparse.ArgumentParser(
        description="Multi-purpose CLI tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Config command
    config_parser = subparsers.add_parser("config", help="Manage configuration")
    config_parser.add_argument(
        "action",
        choices=["get", "set", "list"],
        help="Config action"
    )
    config_parser.add_argument("key", nargs="?", help="Configuration key")
    config_parser.add_argument("value", nargs="?", help="Configuration value")
    
    # Files command
    files_parser = subparsers.add_parser("files", help="Manage files")
    files_parser.add_argument(
        "action",
        choices=["list", "count"],
        help="File action"
    )
    files_parser.add_argument(
        "-d", "--directory",
        help="Target directory"
    )
    files_parser.add_argument(
        "-p", "--pattern",
        help="File pattern"
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    config = ConfigManager()
    
    if args.command == "config":
        cmd_config(args, config)
    elif args.command == "files":
        cmd_files(args)

if __name__ == "__main__":
    main()
```

---

## Testing and Debugging

### Unit Testing

```python
import unittest
from library_system.models.book import Book
from library_system.models.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("1", "Test Book", "Author", "123")
    
    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertIn("1", self.library.books)
    
    def test_borrow_book(self):
        self.library.add_book(self.book)
        available_before = self.book.available_copies
        self.book.borrow()
        self.assertEqual(self.book.available_copies, available_before - 1)

if __name__ == "__main__":
    unittest.main()
```

---

## Deployment Tips

### Requirements.txt

```
requests==2.28.0
python-dotenv==0.20.0
pytest==7.0.0
pytest-cov==3.0.0
```

### Running Projects

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run project
python main.py

# Run CLI tool
python main.py config list
python main.py files list
```

---

## Learning Outcomes

After completing these projects, you'll understand:

✅ OOP design patterns
✅ Real-world application architecture
✅ Error handling and logging
✅ Data validation and transformation
✅ Caching strategies
✅ CLI development
✅ Testing and debugging
✅ Project organization

---

# End of Notes
