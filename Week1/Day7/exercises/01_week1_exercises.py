"""
WEEK 1 REVIEW EXERCISES
=======================
Complete these exercises to reinforce all Week 1 concepts

Topics covered:
- Variables and data types
- Lists and dictionaries
- Functions
- File handling
- Exception handling
- Basic DSA patterns
"""

print("=" * 60)
print("WEEK 1 REVIEW EXERCISES")
print("=" * 60)

# ============================================================
# EXERCISE 1: Data Processing Pipeline
# ============================================================

print("\n" + "-" * 60)
print("Exercise 1: Data Processing Pipeline")
print("-" * 60)

"""
TODO: Create a data processing pipeline that:
1. Takes a list of raw user data (strings like "name,age,city")
2. Parses each entry into a dictionary
3. Filters users older than 25
4. Returns a sorted list by age

Example input:
    ["Alice,30,NYC", "Bob,22,LA", "Charlie,28,Chicago"]
    
Expected output:
    [{"name": "Charlie", "age": 28, "city": "Chicago"},
     {"name": "Alice", "age": 30, "city": "NYC"}]
"""

def process_user_data(raw_data):
    """
    Process raw user data strings into filtered, sorted dictionaries.
    
    Args:
        raw_data: List of strings in format "name,age,city"
    
    Returns:
        List of dictionaries for users older than 25, sorted by age
    """
    # TODO: Implement this function
    pass

# Test data
test_data = [
    "Alice,30,NYC",
    "Bob,22,LA",
    "Charlie,28,Chicago",
    "Diana,35,Seattle",
    "Eve,24,Boston"
]

# Uncomment to test:
# result = process_user_data(test_data)
# print(f"Filtered users: {result}")


# ============================================================
# EXERCISE 2: Inventory Manager
# ============================================================

print("\n" + "-" * 60)
print("Exercise 2: Inventory Manager")
print("-" * 60)

"""
TODO: Create an inventory management class that:
1. Stores products with name, quantity, and price
2. Allows adding and removing products
3. Calculates total inventory value
4. Finds products low in stock (< threshold)
5. Saves/loads inventory from JSON file
"""

class InventoryManager:
    def __init__(self):
        self.products = {}  # {name: {"quantity": int, "price": float}}
    
    def add_product(self, name, quantity, price):
        """Add or update a product"""
        # TODO: Implement
        pass
    
    def remove_product(self, name, quantity):
        """Remove quantity from product. Return False if not enough stock."""
        # TODO: Implement
        pass
    
    def total_value(self):
        """Calculate total inventory value"""
        # TODO: Implement
        pass
    
    def low_stock(self, threshold=10):
        """Return list of products with quantity below threshold"""
        # TODO: Implement
        pass
    
    def save_to_file(self, filename):
        """Save inventory to JSON file"""
        # TODO: Implement
        pass
    
    def load_from_file(self, filename):
        """Load inventory from JSON file"""
        # TODO: Implement
        pass

# Test the inventory manager
# inventory = InventoryManager()
# inventory.add_product("Laptop", 50, 999.99)
# inventory.add_product("Mouse", 200, 29.99)
# print(f"Total value: ${inventory.total_value():.2f}")


# ============================================================
# EXERCISE 3: Text Analyzer
# ============================================================

print("\n" + "-" * 60)
print("Exercise 3: Text Analyzer")
print("-" * 60)

"""
TODO: Create functions that analyze text and return:
1. Word count
2. Character count (with and without spaces)
3. Sentence count
4. Most common words (top 5)
5. Average word length
"""

def analyze_text(text):
    """
    Analyze text and return comprehensive statistics.
    
    Returns:
        Dictionary with word_count, char_count, char_count_no_spaces,
        sentence_count, most_common_words, avg_word_length
    """
    # TODO: Implement
    pass

sample_text = """
Python is an amazing programming language. It is easy to learn and very powerful.
Many developers use Python for web development, data science, and automation.
Python has a great community and excellent documentation.
"""

# Uncomment to test:
# stats = analyze_text(sample_text)
# for key, value in stats.items():
#     print(f"{key}: {value}")


# ============================================================
# EXERCISE 4: Stack-Based Expression Validator
# ============================================================

print("\n" + "-" * 60)
print("Exercise 4: Expression Validator")
print("-" * 60)

"""
TODO: Create a function that validates if brackets are balanced
using a stack. Support (), [], {}

Valid: "(())", "([{}])", "({[]})"
Invalid: "(]", "([)]", "((("
"""

def is_balanced(expression):
    """
    Check if brackets in expression are balanced.
    
    Args:
        expression: String containing brackets
    
    Returns:
        True if balanced, False otherwise
    """
    # TODO: Implement using a stack
    pass

# Test cases
test_expressions = [
    "(())",      # True
    "([{}])",    # True
    "({[]})",    # True
    "(]",        # False
    "([)]",      # False
    "(((",       # False
    "{}[]()([{()}])",  # True
]

# Uncomment to test:
# for expr in test_expressions:
#     print(f"{expr}: {is_balanced(expr)}")


# ============================================================
# EXERCISE 5: Two-Pointer Problems
# ============================================================

print("\n" + "-" * 60)
print("Exercise 5: Two-Pointer Problems")
print("-" * 60)

"""
TODO: Implement these two-pointer solutions:
1. Remove duplicates from sorted array (in-place)
2. Find pair with given sum in sorted array
3. Reverse words in a string
"""

def remove_duplicates(arr):
    """
    Remove duplicates from sorted array in-place.
    Return new length (don't resize array).
    """
    # TODO: Implement
    pass

def find_pair_with_sum(arr, target):
    """
    Find two numbers in sorted array that add to target.
    Return their indices or [-1, -1] if not found.
    """
    # TODO: Implement
    pass

def reverse_words(s):
    """
    Reverse words in string. "Hello World" -> "World Hello"
    """
    # TODO: Implement
    pass

# Uncomment to test:
# arr = [1, 1, 2, 2, 3, 4, 4, 5]
# print(f"Remove duplicates new length: {remove_duplicates(arr)}")
# 
# arr2 = [1, 2, 4, 6, 8, 10]
# print(f"Find pair with sum 10: {find_pair_with_sum(arr2, 10)}")
# 
# print(f"Reverse words: {reverse_words('Hello World')}")


# ============================================================
# EXERCISE 6: File-Based Logger with Rotation
# ============================================================

print("\n" + "-" * 60)
print("Exercise 6: File-Based Logger")
print("-" * 60)

"""
TODO: Create a Logger class that:
1. Writes log messages to a file with timestamps
2. Supports log levels: DEBUG, INFO, WARNING, ERROR
3. Rotates log file when it exceeds max_lines
4. Can read and filter logs by level
"""

class Logger:
    def __init__(self, filename, max_lines=100):
        self.filename = filename
        self.max_lines = max_lines
    
    def _get_timestamp(self):
        """Return current timestamp string"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def log(self, level, message):
        """Write log entry to file"""
        # TODO: Implement
        pass
    
    def debug(self, message):
        self.log("DEBUG", message)
    
    def info(self, message):
        self.log("INFO", message)
    
    def warning(self, message):
        self.log("WARNING", message)
    
    def error(self, message):
        self.log("ERROR", message)
    
    def read_logs(self, level=None):
        """Read logs, optionally filtered by level"""
        # TODO: Implement
        pass
    
    def _rotate_if_needed(self):
        """Rotate log file if it exceeds max_lines"""
        # TODO: Implement
        pass

# Uncomment to test:
# logger = Logger("app.log")
# logger.info("Application started")
# logger.debug("Loading configuration")
# logger.warning("Config file not found, using defaults")
# logger.error("Failed to connect to database")
# 
# print("All logs:")
# for log in logger.read_logs():
#     print(log)
# 
# print("\nErrors only:")
# for log in logger.read_logs("ERROR"):
#     print(log)


# ============================================================
# EXERCISE 7: Sliding Window Problems
# ============================================================

print("\n" + "-" * 60)
print("Exercise 7: Sliding Window Problems")
print("-" * 60)

"""
TODO: Implement these sliding window solutions:
1. Maximum sum subarray of size k
2. Longest substring without repeating characters
3. Minimum window substring
"""

def max_sum_subarray(arr, k):
    """
    Find maximum sum of any contiguous subarray of size k.
    """
    # TODO: Implement
    pass

def longest_unique_substring(s):
    """
    Find length of longest substring without repeating characters.
    "abcabcbb" -> 3 ("abc")
    """
    # TODO: Implement
    pass

def contains_all_chars(s, pattern):
    """
    Check if string s contains all characters of pattern.
    "adobecodebanc", "abc" -> True (contains a, b, c)
    """
    # TODO: Implement
    pass

# Uncomment to test:
# arr = [2, 1, 5, 1, 3, 2]
# print(f"Max sum of size 3: {max_sum_subarray(arr, 3)}")  # 9
# 
# print(f"Longest unique: {longest_unique_substring('abcabcbb')}")  # 3
# 
# print(f"Contains all: {contains_all_chars('adobecodebanc', 'abc')}")  # True


# ============================================================
# EXERCISE 8: Complete Application - Contact Manager
# ============================================================

print("\n" + "-" * 60)
print("Exercise 8: Contact Manager Application")
print("-" * 60)

"""
TODO: Build a complete contact manager that combines all Week 1 skills:
- Store contacts with name, phone, email, category
- CRUD operations
- Search contacts by name or category
- Import/export from CSV
- Validation and error handling
"""

class ContactManager:
    def __init__(self, data_file="contacts.json"):
        self.data_file = data_file
        self.contacts = []
        self.load()
    
    def load(self):
        """Load contacts from file"""
        # TODO: Implement with error handling
        pass
    
    def save(self):
        """Save contacts to file"""
        # TODO: Implement
        pass
    
    def add_contact(self, name, phone, email, category="personal"):
        """Add new contact with validation"""
        # TODO: Implement with validation
        pass
    
    def find_contact(self, name):
        """Find contact by name (case-insensitive)"""
        # TODO: Implement
        pass
    
    def update_contact(self, name, **kwargs):
        """Update contact fields"""
        # TODO: Implement
        pass
    
    def delete_contact(self, name):
        """Delete contact by name"""
        # TODO: Implement
        pass
    
    def search(self, query):
        """Search contacts by name or category"""
        # TODO: Implement
        pass
    
    def list_by_category(self, category):
        """List all contacts in a category"""
        # TODO: Implement
        pass
    
    def export_csv(self, filename):
        """Export contacts to CSV"""
        # TODO: Implement
        pass
    
    def import_csv(self, filename):
        """Import contacts from CSV"""
        # TODO: Implement
        pass

# Test the contact manager
# cm = ContactManager()
# cm.add_contact("Alice", "555-1234", "alice@email.com", "work")
# cm.add_contact("Bob", "555-5678", "bob@email.com", "personal")
# print(f"All contacts: {cm.contacts}")
# print(f"Found: {cm.find_contact('alice')}")


print("\n" + "=" * 60)
print("Complete all exercises to reinforce Week 1 concepts!")
print("=" * 60)
