"""
MINI PROJECT 1: LRU Cache Implementation
=========================================
Build a Least Recently Used (LRU) Cache

An LRU Cache:
- Has a fixed capacity
- Stores key-value pairs
- Evicts least recently used item when full
- get() and put() should be O(1)

This is a CLASSIC interview question!
Uses: Hash Map + Doubly Linked List
"""

print("=" * 60)
print("MINI PROJECT: LRU CACHE")
print("=" * 60)

print("""
LRU Cache Operations:
- get(key): Return value if exists, else -1
- put(key, value): Insert or update key-value
  If capacity exceeded, remove least recently used item

Example with capacity=2:
  put(1, 1)  → cache: {1: 1}
  put(2, 2)  → cache: {1: 1, 2: 2}
  get(1)     → returns 1, cache: {2: 2, 1: 1}  (1 is now most recent)
  put(3, 3)  → cache: {1: 1, 3: 3}  (2 evicted as LRU)
  get(2)     → returns -1 (not found)
""")

# ============================================================
# VERSION 1: Using OrderedDict (Simple)
# ============================================================

from collections import OrderedDict

class LRUCacheSimple:
    """LRU Cache using OrderedDict"""
    
    def __init__(self, capacity: int):
        """Initialize cache with given capacity"""
        # TODO: Initialize OrderedDict and capacity
        pass
    
    def get(self, key: int) -> int:
        """
        Get value for key. Return -1 if not found.
        Move key to end (most recent) if found.
        """
        # TODO: Implement
        pass
    
    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.
        If at capacity, remove least recently used item first.
        """
        # TODO: Implement
        pass


# ============================================================
# VERSION 2: Using Hash Map + Doubly Linked List (Advanced)
# ============================================================

class DLinkedNode:
    """Doubly linked list node"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache using Hash Map + Doubly Linked List
    This is the "real" implementation used in interviews
    """
    
    def __init__(self, capacity: int):
        """Initialize cache with given capacity"""
        # TODO: Initialize:
        # - capacity
        # - cache dict: key -> node
        # - head and tail dummy nodes for doubly linked list
        pass
    
    def _add_to_head(self, node: DLinkedNode) -> None:
        """Add node right after head (most recent position)"""
        # TODO: Implement
        pass
    
    def _remove_node(self, node: DLinkedNode) -> None:
        """Remove node from current position"""
        # TODO: Implement
        pass
    
    def _move_to_head(self, node: DLinkedNode) -> None:
        """Move existing node to head (mark as most recent)"""
        # TODO: Implement
        pass
    
    def _remove_tail(self) -> DLinkedNode:
        """Remove and return the tail node (least recent)"""
        # TODO: Implement
        pass
    
    def get(self, key: int) -> int:
        """Get value for key, return -1 if not found"""
        # TODO: Implement
        pass
    
    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair"""
        # TODO: Implement
        pass


# ============================================================
# TEST YOUR IMPLEMENTATION
# ============================================================

def test_lru_cache(CacheClass, name):
    """Test LRU cache implementation"""
    print(f"\n--- Testing {name} ---")
    
    # Test 1: Basic operations
    cache = CacheClass(2)
    cache.put(1, 1)
    cache.put(2, 2)
    result = cache.get(1)
    expected = 1
    print(f"get(1): {result} {'✅' if result == expected else '❌'}")
    
    # Test 2: Eviction
    cache.put(3, 3)  # Evicts key 2
    result = cache.get(2)
    expected = -1
    print(f"get(2) after eviction: {result} {'✅' if result == expected else '❌'}")
    
    # Test 3: Access updates recency
    result = cache.get(3)
    expected = 3
    print(f"get(3): {result} {'✅' if result == expected else '❌'}")
    
    # Test 4: Update existing key
    cache.put(4, 4)  # Evicts key 1
    result = cache.get(1)
    expected = -1
    print(f"get(1) after eviction: {result} {'✅' if result == expected else '❌'}")
    
    result = cache.get(3)
    expected = 3
    print(f"get(3): {result} {'✅' if result == expected else '❌'}")
    
    result = cache.get(4)
    expected = 4
    print(f"get(4): {result} {'✅' if result == expected else '❌'}")


# Uncomment to test your implementations:
# test_lru_cache(LRUCacheSimple, "LRUCacheSimple (OrderedDict)")
# test_lru_cache(LRUCache, "LRUCache (HashMap + DLL)")


# ============================================================
# SOLUTION (for reference)
# ============================================================

print("""

=== SOLUTION HINTS ===

OrderedDict Version:
```python
class LRUCacheSimple:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

For the advanced DLL version, implement helper methods:
1. _add_to_head: Insert node after dummy head
2. _remove_node: Update prev.next and next.prev
3. _move_to_head: _remove_node + _add_to_head
4. _remove_tail: Return and remove node before dummy tail
""")

print("\n" + "=" * 60)
print("Complete the implementation above!")
print("=" * 60)
