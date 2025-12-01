"""
MINI PROJECT 2: Database Caching Layer
=======================================
A caching layer for database operations

Features:
1. Cache-aside pattern implementation
2. TTL (Time To Live) support
3. Cache invalidation strategies
4. Performance metrics

Run this to see a complete caching implementation!
"""

import sqlite3
import os
import time
import json
from datetime import datetime, timedelta
from typing import Any, Callable
import random

print("=" * 60)
print("DATABASE CACHING LAYER")
print("=" * 60)

# ========== CACHE IMPLEMENTATION ==========
class Cache:
    """In-memory cache with TTL support"""
    
    def __init__(self):
        self._data = {}
        self._expires = {}
        self._stats = {
            "hits": 0,
            "misses": 0,
            "sets": 0,
            "deletes": 0
        }
    
    def get(self, key: str) -> Any | None:
        """Get value, return None if expired or missing"""
        self._cleanup_expired(key)
        
        if key in self._data:
            self._stats["hits"] += 1
            return self._data[key]
        
        self._stats["misses"] += 1
        return None
    
    def set(self, key: str, value: Any, ttl: int = 300) -> None:
        """Set value with TTL (default 5 minutes)"""
        self._data[key] = value
        self._expires[key] = datetime.now() + timedelta(seconds=ttl)
        self._stats["sets"] += 1
    
    def delete(self, key: str) -> bool:
        """Delete a key"""
        if key in self._data:
            del self._data[key]
            if key in self._expires:
                del self._expires[key]
            self._stats["deletes"] += 1
            return True
        return False
    
    def delete_pattern(self, pattern: str) -> int:
        """Delete all keys matching pattern (simple wildcard)"""
        prefix = pattern.rstrip("*")
        keys_to_delete = [k for k in self._data if k.startswith(prefix)]
        for key in keys_to_delete:
            self.delete(key)
        return len(keys_to_delete)
    
    def clear(self) -> None:
        """Clear all cached data"""
        self._data.clear()
        self._expires.clear()
    
    def _cleanup_expired(self, key: str) -> None:
        """Remove key if expired"""
        if key in self._expires:
            if datetime.now() > self._expires[key]:
                del self._data[key]
                del self._expires[key]
    
    @property
    def stats(self) -> dict:
        """Get cache statistics"""
        total = self._stats["hits"] + self._stats["misses"]
        hit_rate = (self._stats["hits"] / total * 100) if total > 0 else 0
        return {
            **self._stats,
            "hit_rate": f"{hit_rate:.1f}%",
            "size": len(self._data)
        }

# ========== CACHED DATABASE ==========
class CachedDatabase:
    """Database with caching layer"""
    
    def __init__(self, db_path: str, cache: Cache):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cache = cache
        self._db_calls = 0
    
    def setup_schema(self):
        """Create tables"""
        self.cursor.execute("DROP TABLE IF EXISTS products")
        self.cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT,
            stock INTEGER DEFAULT 0
        )
        """)
        self.conn.commit()
    
    def insert_product(self, name: str, price: float, category: str, stock: int) -> int:
        """Insert product (no caching for writes)"""
        self.cursor.execute(
            "INSERT INTO products (name, price, category, stock) VALUES (?, ?, ?, ?)",
            (name, price, category, stock)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_product(self, product_id: int, use_cache: bool = True) -> dict | None:
        """Get product by ID with caching"""
        cache_key = f"product:{product_id}"
        
        if use_cache:
            cached = self.cache.get(cache_key)
            if cached is not None:
                return cached
        
        # Cache miss - fetch from database
        self._db_calls += 1
        self.cursor.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,)
        )
        row = self.cursor.fetchone()
        
        if row:
            product = {
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "category": row[3],
                "stock": row[4]
            }
            if use_cache:
                self.cache.set(cache_key, product, ttl=300)
            return product
        return None
    
    def update_product(self, product_id: int, **updates) -> bool:
        """Update product and invalidate cache"""
        set_clause = ", ".join(f"{k} = ?" for k in updates.keys())
        self.cursor.execute(
            f"UPDATE products SET {set_clause} WHERE id = ?",
            (*updates.values(), product_id)
        )
        self.conn.commit()
        
        # Invalidate cache
        self.cache.delete(f"product:{product_id}")
        
        return self.cursor.rowcount > 0
    
    def get_products_by_category(self, category: str, use_cache: bool = True) -> list:
        """Get products by category with caching"""
        cache_key = f"products:category:{category}"
        
        if use_cache:
            cached = self.cache.get(cache_key)
            if cached is not None:
                return cached
        
        self._db_calls += 1
        self.cursor.execute(
            "SELECT * FROM products WHERE category = ?",
            (category,)
        )
        
        products = []
        for row in self.cursor.fetchall():
            products.append({
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "category": row[3],
                "stock": row[4]
            })
        
        if use_cache and products:
            self.cache.set(cache_key, products, ttl=60)  # Shorter TTL for lists
        
        return products
    
    def delete_product(self, product_id: int) -> bool:
        """Delete product and invalidate cache"""
        # Get category before delete for cache invalidation
        product = self.get_product(product_id, use_cache=False)
        
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()
        
        if self.cursor.rowcount > 0:
            # Invalidate both product and category cache
            self.cache.delete(f"product:{product_id}")
            if product:
                self.cache.delete(f"products:category:{product['category']}")
            return True
        return False
    
    @property
    def db_calls(self) -> int:
        return self._db_calls
    
    def close(self):
        self.conn.close()

# ========== DEMO ==========
print("\n📦 Setting up database and cache...")

db_file = "cached_products.db"
cache = Cache()
db = CachedDatabase(db_file, cache)
db.setup_schema()

# Insert sample products
categories = ["Electronics", "Clothing", "Books", "Home"]
products_data = [
    ("Laptop", 999.99, "Electronics", 50),
    ("Mouse", 29.99, "Electronics", 200),
    ("Keyboard", 79.99, "Electronics", 150),
    ("T-Shirt", 19.99, "Clothing", 500),
    ("Jeans", 49.99, "Clothing", 300),
    ("Python Book", 39.99, "Books", 100),
    ("SQL Guide", 34.99, "Books", 75),
    ("Desk Lamp", 24.99, "Home", 80),
]

product_ids = []
for name, price, category, stock in products_data:
    product_ids.append(db.insert_product(name, price, category, stock))
print(f"✅ Created {len(products_data)} products")

# ========== DEMONSTRATE CACHING ==========
print("\n" + "=" * 60)
print("CACHING DEMONSTRATION")
print("=" * 60)

# Reset stats
db._db_calls = 0

print("\n📊 Test 1: Repeated single product lookup")
print("-" * 40)

# First call - cache miss
start = time.time()
product = db.get_product(1)
first_time = (time.time() - start) * 1000
print(f"Call 1 (MISS): {product['name']} - {first_time:.3f}ms")

# Second call - cache hit
start = time.time()
product = db.get_product(1)
second_time = (time.time() - start) * 1000
print(f"Call 2 (HIT):  {product['name']} - {second_time:.3f}ms")

# Third call - cache hit
start = time.time()
product = db.get_product(1)
third_time = (time.time() - start) * 1000
print(f"Call 3 (HIT):  {product['name']} - {third_time:.3f}ms")

print(f"\nDatabase calls: {db.db_calls}")
print(f"Cache stats: {cache.stats}")

print("\n📊 Test 2: Multiple product lookups")
print("-" * 40)

# Simulate multiple requests
db._db_calls = 0
cache.clear()

for _ in range(100):
    product_id = random.choice(product_ids)
    db.get_product(product_id)

print(f"100 random lookups:")
print(f"Database calls: {db.db_calls}")
print(f"Cache stats: {cache.stats}")

print("\n📊 Test 3: Category lookups")
print("-" * 40)

db._db_calls = 0

# First call - cache miss
products = db.get_products_by_category("Electronics")
print(f"Electronics (MISS): {len(products)} products")

# Second call - cache hit
products = db.get_products_by_category("Electronics")
print(f"Electronics (HIT):  {len(products)} products")

print(f"Database calls: {db.db_calls}")

print("\n📊 Test 4: Cache invalidation on update")
print("-" * 40)

# Get product (caches it)
product = db.get_product(1)
print(f"Before update: {product['name']} = ${product['price']}")

# Update (invalidates cache)
db.update_product(1, price=899.99)
print("Updated price to $899.99 (cache invalidated)")

# Get again (fetches fresh from DB)
product = db.get_product(1)
print(f"After update:  {product['name']} = ${product['price']}")

print("\n📊 Test 5: Performance comparison")
print("-" * 40)

db._db_calls = 0
cache.clear()

# Without cache
start = time.time()
for _ in range(1000):
    db.get_product(random.randint(1, 8), use_cache=False)
no_cache_time = time.time() - start
no_cache_calls = db.db_calls

# Reset
db._db_calls = 0
cache.clear()

# With cache
start = time.time()
for _ in range(1000):
    db.get_product(random.randint(1, 8), use_cache=True)
with_cache_time = time.time() - start
with_cache_calls = db.db_calls

print(f"1000 random lookups:")
print(f"Without cache: {no_cache_time*1000:.1f}ms, {no_cache_calls} DB calls")
print(f"With cache:    {with_cache_time*1000:.1f}ms, {with_cache_calls} DB calls")
print(f"Speedup:       {no_cache_time/with_cache_time:.1f}x faster")
print(f"DB call reduction: {(1 - with_cache_calls/no_cache_calls)*100:.1f}%")

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("CACHING BEST PRACTICES")
print("=" * 60)

print("""
1. CHOOSE WHAT TO CACHE
   ✓ Frequently accessed data
   ✓ Expensive queries
   ✓ Relatively static data
   ✗ User-specific data (careful with multi-tenant)
   ✗ Rapidly changing data

2. SET APPROPRIATE TTL
   - Short (30-60s): Frequently changing data
   - Medium (5-15min): Product listings, search results
   - Long (1hr+): Configuration, reference data

3. INVALIDATION STRATEGIES
   - Update/Delete: Always invalidate related keys
   - Pattern matching: Delete all related keys
   - Version keys: Append version number

4. HANDLE CACHE FAILURES
   - Fail gracefully (fall back to database)
   - Don't let cache failures break your app
   - Monitor cache health

5. MONITOR AND OPTIMIZE
   - Track hit/miss rates
   - Adjust TTL based on usage patterns
   - Watch for cache stampede (many misses at once)
""")

# ========== CLEANUP ==========
print("=" * 60)
db.close()
if os.path.exists(db_file):
    os.remove(db_file)
print("✅ Caching demo complete! Database cleaned up.")
