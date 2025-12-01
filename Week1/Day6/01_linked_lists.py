"""
Day 6 - Linked Lists Basics
===========================
Learn: Singly linked list implementation and operations

Key Concepts:
- Linked list is a linear data structure
- Each element (node) contains data and reference to next node
- Head points to the first node
- Last node points to None
"""

# ========== NODE CLASS ==========
print("=" * 50)
print("NODE CLASS")
print("=" * 50)

class Node:
    """
    A node in a singly linked list.
    Each node contains:
    - data: the value stored
    - next: reference to the next node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"

# Create some nodes
print("\nCreating nodes:")
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

print(f"node1: {node1}, data={node1.data}, next={node1.next}")
print(f"node2: {node2}, data={node2.data}, next={node2.next}")
print(f"node3: {node3}, data={node3.data}, next={node3.next}")

# Link nodes manually
node1.next = node2
node2.next = node3

print("\nAfter linking:")
print(f"node1.next = {node1.next}")
print(f"node2.next = {node2.next}")
print(f"node3.next = {node3.next}")

# ========== LINKED LIST CLASS ==========
print("\n" + "=" * 50)
print("LINKED LIST CLASS")
print("=" * 50)

class LinkedList:
    """
    Singly Linked List implementation with common operations.
    """
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None
    
    def __len__(self):
        """Return size of list - O(1)"""
        return self.size
    
    def __repr__(self):
        """String representation"""
        if not self.head:
            return "LinkedList: Empty"
        
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "LinkedList: " + " -> ".join(nodes) + " -> None"

# Create an empty linked list
ll = LinkedList()
print(f"\nEmpty list: {ll}")
print(f"Is empty? {ll.is_empty()}")
print(f"Size: {len(ll)}")

# ========== INSERT OPERATIONS ==========
print("\n" + "=" * 50)
print("INSERT OPERATIONS")
print("=" * 50)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        if not self.head:
            return "LinkedList: Empty"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "LinkedList: " + " -> ".join(nodes) + " -> None"
    
    def insert_at_head(self, data):
        """
        Insert at beginning - O(1)
        New node becomes the head
        """
        new_node = Node(data)
        new_node.next = self.head  # Point to current head
        self.head = new_node       # Update head
        self.size += 1
    
    def insert_at_tail(self, data):
        """
        Insert at end - O(n)
        Must traverse to find the last node
        """
        new_node = Node(data)
        
        # If list is empty, new node is head
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        self.size += 1
    
    def insert_at_index(self, index, data):
        """
        Insert at specific position - O(n)
        Index 0 means insert at head
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.insert_at_head(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        # Move to node before insertion point
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1

# Demo insert operations
print("\nInsert at head:")
ll = LinkedList()
ll.insert_at_head(30)
print(f"After inserting 30 at head: {ll}")
ll.insert_at_head(20)
print(f"After inserting 20 at head: {ll}")
ll.insert_at_head(10)
print(f"After inserting 10 at head: {ll}")

print("\nInsert at tail:")
ll2 = LinkedList()
ll2.insert_at_tail(10)
print(f"After inserting 10 at tail: {ll2}")
ll2.insert_at_tail(20)
print(f"After inserting 20 at tail: {ll2}")
ll2.insert_at_tail(30)
print(f"After inserting 30 at tail: {ll2}")

print("\nInsert at index:")
ll3 = LinkedList()
ll3.insert_at_tail(10)
ll3.insert_at_tail(30)
print(f"Initial list: {ll3}")
ll3.insert_at_index(1, 20)  # Insert 20 at index 1
print(f"After inserting 20 at index 1: {ll3}")
ll3.insert_at_index(0, 5)   # Insert 5 at index 0
print(f"After inserting 5 at index 0: {ll3}")

# ========== DELETE OPERATIONS ==========
print("\n" + "=" * 50)
print("DELETE OPERATIONS")
print("=" * 50)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        if not self.head:
            return "LinkedList: Empty"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "LinkedList: " + " -> ".join(nodes) + " -> None"
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1
    
    def delete_at_head(self):
        """
        Delete first node - O(1)
        """
        if not self.head:
            raise IndexError("List is empty")
        
        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data
    
    def delete_at_tail(self):
        """
        Delete last node - O(n)
        Must traverse to second-to-last node
        """
        if not self.head:
            raise IndexError("List is empty")
        
        # If only one node
        if not self.head.next:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        # Traverse to second-to-last node
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        self.size -= 1
        return deleted_data
    
    def delete_by_value(self, value):
        """
        Delete first occurrence of value - O(n)
        """
        if not self.head:
            raise ValueError("List is empty")
        
        # If head contains the value
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return True
        
        # Search for value
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False  # Value not found
    
    def delete_at_index(self, index):
        """
        Delete node at specific index - O(n)
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            return self.delete_at_head()
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data

# Demo delete operations
print("\nDelete operations:")
ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert_at_tail(i)
print(f"Initial list: {ll}")

deleted = ll.delete_at_head()
print(f"Deleted at head ({deleted}): {ll}")

deleted = ll.delete_at_tail()
print(f"Deleted at tail ({deleted}): {ll}")

ll.delete_by_value(30)
print(f"Deleted value 30: {ll}")

deleted = ll.delete_at_index(0)
print(f"Deleted at index 0 ({deleted}): {ll}")

# ========== SEARCH OPERATIONS ==========
print("\n" + "=" * 50)
print("SEARCH OPERATIONS")
print("=" * 50)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1
    
    def __repr__(self):
        if not self.head:
            return "LinkedList: Empty"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "LinkedList: " + " -> ".join(nodes) + " -> None"
    
    def search(self, value):
        """
        Search for value - O(n)
        Returns True if found, False otherwise
        """
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def get_index(self, value):
        """
        Get index of first occurrence - O(n)
        Returns -1 if not found
        """
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def get_at_index(self, index):
        """
        Get value at index - O(n)
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

# Demo search operations
print("\nSearch operations:")
ll = LinkedList()
for i in [10, 20, 30, 40, 50]:
    ll.insert_at_tail(i)
print(f"List: {ll}")

print(f"\nSearch for 30: {ll.search(30)}")
print(f"Search for 100: {ll.search(100)}")
print(f"Index of 30: {ll.get_index(30)}")
print(f"Index of 100: {ll.get_index(100)}")
print(f"Value at index 2: {ll.get_at_index(2)}")

# ========== TRAVERSAL AND UTILITY ==========
print("\n" + "=" * 50)
print("TRAVERSAL AND UTILITY")
print("=" * 50)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1
    
    def __repr__(self):
        if not self.head:
            return "LinkedList: Empty"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "LinkedList: " + " -> ".join(nodes) + " -> None"
    
    def traverse(self):
        """
        Print all elements - O(n)
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def to_list(self):
        """
        Convert to Python list - O(n)
        """
        return self.traverse()
    
    def from_list(self, python_list):
        """
        Create linked list from Python list - O(n)
        """
        self.head = None
        self.size = 0
        for item in python_list:
            self.insert_at_tail(item)
    
    def reverse(self):
        """
        Reverse the linked list in place - O(n)
        Uses three pointers: prev, current, next
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next  # Store next
            current.next = prev       # Reverse link
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        
        self.head = prev
    
    def get_middle(self):
        """
        Find middle element using slow/fast pointer - O(n)
        """
        if not self.head:
            return None
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data

# Demo traversal and utility
print("\nTraversal and utility:")
ll = LinkedList()
ll.from_list([10, 20, 30, 40, 50])
print(f"List from Python list: {ll}")
print(f"To Python list: {ll.to_list()}")
print(f"Middle element: {ll.get_middle()}")

ll.reverse()
print(f"Reversed: {ll}")

ll.reverse()  # Reverse back
print(f"Reversed back: {ll}")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: Task Queue")
print("=" * 50)

class TaskQueue:
    """
    A simple task queue using linked list
    Tasks are processed in FIFO order
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_task(self, task):
        """Add task to end of queue"""
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"✅ Added task: '{task}'")
    
    def process_next(self):
        """Process and remove first task"""
        if not self.head:
            print("❌ No tasks in queue!")
            return None
        
        task = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        print(f"⚙️  Processing: '{task}'")
        return task
    
    def view_queue(self):
        """View all pending tasks"""
        if not self.head:
            print("Queue is empty")
            return
        
        print(f"\nPending tasks ({self.size}):")
        current = self.head
        position = 1
        while current:
            print(f"  {position}. {current.data}")
            current = current.next
            position += 1
    
    def is_empty(self):
        return self.size == 0

# Demo task queue
print("\nTask Queue Demo:")
queue = TaskQueue()

queue.add_task("Send email to client")
queue.add_task("Update database")
queue.add_task("Generate report")
queue.add_task("Backup files")

queue.view_queue()

print("\nProcessing tasks:")
queue.process_next()
queue.process_next()

queue.view_queue()

# ========== LINKED LIST VS ARRAY ==========
print("\n" + "=" * 50)
print("LINKED LIST VS ARRAY COMPARISON")
print("=" * 50)

print("""
| Operation           | Array      | Linked List |
|---------------------|------------|-------------|
| Access by index     | O(1)       | O(n)        |
| Search              | O(n)       | O(n)        |
| Insert at beginning | O(n)       | O(1)        |
| Insert at end       | O(1)*      | O(n)**      |
| Insert at middle    | O(n)       | O(n)        |
| Delete at beginning | O(n)       | O(1)        |
| Delete at end       | O(1)       | O(n)**      |
| Delete at middle    | O(n)       | O(n)        |
| Memory              | Contiguous | Scattered   |
| Memory overhead     | Less       | More (next) |

* O(1) amortized for dynamic arrays
** Can be O(1) if we maintain tail pointer

When to use Linked List:
- Frequent insertions/deletions at beginning
- Unknown or varying size
- Don't need random access
- Implementing stacks, queues

When to use Array:
- Need random access by index
- Memory efficiency is important
- Cache performance matters
- Simple iteration
""")

print("\n" + "=" * 50)
print("✅ Linked Lists Basics - Complete!")
print("=" * 50)
