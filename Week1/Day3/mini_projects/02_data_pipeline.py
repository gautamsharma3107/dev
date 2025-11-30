"""
MINI PROJECT 2: Data Processing Pipeline
==========================================
Create functions to process and analyze data

Requirements:
1. Load data (simulate with a list of dictionaries)
2. Filter data based on criteria
3. Transform data (apply calculations)
4. Aggregate data (sum, average, count)
5. Generate report

Sample data: List of sales records
[{"product": "A", "quantity": 5, "price": 100, "date": "2024-01-15"}, ...]
"""

print("=" * 50)
print("DATA PROCESSING PIPELINE")
print("=" * 50)

# Sample data
sales_data = [
    {"product": "Laptop", "quantity": 5, "price": 999, "category": "Electronics"},
    {"product": "Phone", "quantity": 10, "price": 699, "category": "Electronics"},
    {"product": "Desk", "quantity": 3, "price": 299, "category": "Furniture"},
    {"product": "Chair", "quantity": 8, "price": 149, "category": "Furniture"},
    {"product": "Monitor", "quantity": 6, "price": 399, "category": "Electronics"},
    {"product": "Keyboard", "quantity": 15, "price": 79, "category": "Electronics"},
    {"product": "Bookshelf", "quantity": 2, "price": 199, "category": "Furniture"},
]

# TODO: Implement these functions:

def filter_by_category(data, category):
    """Filter data by category."""
    pass

def calculate_revenue(data):
    """Add revenue field (quantity * price) to each item."""
    pass

def get_total_revenue(data):
    """Calculate total revenue."""
    pass

def get_category_summary(data):
    """Get summary by category: count, total revenue, average price."""
    pass

def get_top_products(data, n=3):
    """Get top n products by revenue."""
    pass

def generate_report(data):
    """Generate a formatted report."""
    pass

# Run the pipeline
# ----------------
