"""
Day 5 - Queues
==============
Learn: Queue data structure implementation and use cases

Key Concepts:
- FIFO: First In, First Out
- Enqueue: Add to back
- Dequeue: Remove from front
- Peek: View front without removing
- O(1) for all core operations (with proper implementation)
"""

# ========== WHAT IS A QUEUE? ==========
print("=" * 50)
print("WHAT IS A QUEUE?")
print("=" * 50)

print("""
Queue = FIFO (First In, First Out)

Think of a line at a store:
- New people join at the BACK
- People leave from the FRONT
- First person in line is served first

  FRONT                    BACK
    ↓                       ↓
  ┌───┬───┬───┬───┬───┐
  │ 1 │ 2 │ 3 │ 4 │ 5 │  ← Newest
  └───┴───┴───┴───┴───┘
    ↑
  Oldest (first to leave)

Core Operations:
- enqueue(item): Add to back - O(1)
- dequeue(): Remove from front - O(1)*
- peek()/front(): View front - O(1)
- is_empty(): Check if empty - O(1)
- size(): Get count - O(1)

* O(1) with deque, O(n) with list
""")

# ========== QUEUE USING PYTHON LIST (INEFFICIENT) ==========
print("\n" + "=" * 50)
print("QUEUE USING LIST (Inefficient)")
print("=" * 50)

print("""
WARNING: Using list as queue is O(n) for dequeue!
- list.append() is O(1)
- list.pop(0) is O(n) - shifts all elements!

Use collections.deque instead (shown next)
""")

# Demo (not recommended for production)
queue = []
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print(f"Queue after adding 1, 2, 3: {queue}")

front = queue.pop(0)  # Dequeue - O(n)!
print(f"Dequeued: {front}, Queue now: {queue}")

# ========== QUEUE USING COLLECTIONS.DEQUE (EFFICIENT) ==========
print("\n" + "=" * 50)
print("QUEUE USING DEQUE (Efficient)")
print("=" * 50)

from collections import deque

queue = deque()

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(f"Queue after adding 1, 2, 3: {list(queue)}")

# Peek (view front)
print(f"Front element: {queue[0]}")

# Dequeue - O(1)!
front = queue.popleft()
print(f"Dequeued: {front}, Queue now: {list(queue)}")

# Check empty
print(f"Is empty? {len(queue) == 0}")
print(f"Size: {len(queue)}")

# ========== QUEUE CLASS IMPLEMENTATION ==========
print("\n" + "=" * 50)
print("QUEUE CLASS IMPLEMENTATION")
print("=" * 50)

class Queue:
    """Queue implementation using deque"""
    
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        """Add item to back - O(1)"""
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return front item - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.popleft()
    
    def peek(self):
        """Return front item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self._items)
    
    def __str__(self):
        return f"Queue([{', '.join(str(x) for x in self._items)}])"
    
    def __repr__(self):
        return self.__str__()

# Demonstrate
queue = Queue()
print("Created new queue")

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(f"After enqueue(10, 20, 30): {queue}")

print(f"Peek: {queue.peek()}")
print(f"Size: {queue.size()}")
print(f"Dequeue: {queue.dequeue()}")
print(f"After dequeue: {queue}")

# ========== USE CASE 1: BFS (BREADTH-FIRST SEARCH) ==========
print("\n" + "=" * 50)
print("USE CASE 1: BREADTH-FIRST SEARCH")
print("=" * 50)

print("""
BFS explores nodes level by level using a queue.

Graph:
    1
   / \\
  2   3
 / \\   \\
4   5   6

BFS Order: 1 → 2 → 3 → 4 → 5 → 6
(Level by level)
""")

def bfs(graph, start):
    """Breadth-First Search using queue"""
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add unvisited neighbors to queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

# Graph represented as adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

result = bfs(graph, 1)
print(f"BFS traversal starting from 1: {result}")

# ========== USE CASE 2: LEVEL ORDER TREE TRAVERSAL ==========
print("\n" + "=" * 50)
print("USE CASE 2: LEVEL ORDER TREE TRAVERSAL")
print("=" * 50)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
    """
    Return nodes level by level
    [
      [1],
      [2, 3],
      [4, 5, 6]
    ]
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Build tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Tree level order traversal:")
levels = level_order(root)
for i, level in enumerate(levels):
    print(f"  Level {i}: {level}")

# ========== USE CASE 3: TASK SCHEDULER ==========
print("\n" + "=" * 50)
print("USE CASE 3: TASK SCHEDULER")
print("=" * 50)

class TaskScheduler:
    """Simple FIFO task scheduler"""
    
    def __init__(self):
        self.tasks = deque()
    
    def add_task(self, task):
        """Add task to queue"""
        self.tasks.append(task)
        print(f"  Added: '{task}'")
    
    def process_next(self):
        """Process next task in queue"""
        if self.tasks:
            task = self.tasks.popleft()
            print(f"  Processing: '{task}'")
            return task
        print("  No tasks to process")
        return None
    
    def pending_count(self):
        return len(self.tasks)

# Demonstrate
print("Task Scheduler Demo:")
scheduler = TaskScheduler()

scheduler.add_task("Send email")
scheduler.add_task("Generate report")
scheduler.add_task("Backup database")

print(f"\nPending tasks: {scheduler.pending_count()}")

print("\nProcessing tasks:")
while scheduler.pending_count() > 0:
    scheduler.process_next()

# ========== USE CASE 4: SLIDING WINDOW MAXIMUM ==========
print("\n" + "=" * 50)
print("USE CASE 4: SLIDING WINDOW MAXIMUM")
print("=" * 50)

print("""
Find maximum in each window of size k.
Input:  [1, 3, -1, -3, 5, 3, 6, 7], k=3
Output: [3, 3, 5, 5, 6, 7]

Window positions:
[1  3  -1] -3  5  3  6  7  → max = 3
 1 [3  -1  -3] 5  3  6  7  → max = 3
 1  3 [-1  -3  5] 3  6  7  → max = 5
 ...
""")

def sliding_window_max(nums, k):
    """
    Find max in each window using deque
    Deque stores indices, keeps elements in decreasing order
    """
    result = []
    dq = deque()  # Store indices
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements (they can never be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Start recording results when window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window_max(nums, k)
print(f"Array: {nums}")
print(f"Window size: {k}")
print(f"Max in each window: {result}")

# ========== USE CASE 5: PRINT QUEUE ==========
print("\n" + "=" * 50)
print("USE CASE 5: PRINT QUEUE SIMULATION")
print("=" * 50)

class PrintJob:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
    
    def __str__(self):
        return f"{self.name} ({self.pages} pages)"

class PrintQueue:
    def __init__(self):
        self.queue = deque()
    
    def add_job(self, job):
        self.queue.append(job)
        print(f"  Added job: {job}")
    
    def process_job(self):
        if self.queue:
            job = self.queue.popleft()
            print(f"  Printing: {job}")
            return job
        print("  Print queue is empty")
        return None
    
    def show_queue(self):
        print(f"  Queue: [{', '.join(str(j) for j in self.queue)}]")

# Demonstrate
print("Print Queue Demo:")
printer = PrintQueue()

printer.add_job(PrintJob("Report", 10))
printer.add_job(PrintJob("Resume", 2))
printer.add_job(PrintJob("Thesis", 100))

print("\nProcessing print queue:")
printer.show_queue()
printer.process_job()
printer.show_queue()
printer.process_job()
printer.show_queue()

# ========== CIRCULAR QUEUE ==========
print("\n" + "=" * 50)
print("CIRCULAR QUEUE (Fixed Size)")
print("=" * 50)

print("""
Circular queue: Fixed size, reuses space efficiently
When tail reaches end, it wraps to beginning.

Used in:
- CPU scheduling
- Traffic management
- Memory buffers
""")

class CircularQueue:
    """Fixed-size circular queue"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def enqueue(self, item):
        if self.is_full():
            return False
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def __str__(self):
        items = []
        idx = self.head
        for _ in range(self.size):
            items.append(self.queue[idx])
            idx = (idx + 1) % self.capacity
        return f"CircularQueue({items})"

# Demonstrate
cq = CircularQueue(3)
print(f"Created circular queue with capacity 3")

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(f"After enqueue 1, 2, 3: {cq}")

print(f"Is full? {cq.is_full()}")
print(f"Enqueue 4 (should fail): {cq.enqueue(4)}")

cq.dequeue()
print(f"After dequeue: {cq}")

cq.enqueue(4)
print(f"After enqueue 4: {cq}")

# ========== PRIORITY QUEUE (BONUS) ==========
print("\n" + "=" * 50)
print("PRIORITY QUEUE (Preview)")
print("=" * 50)

print("""
Priority Queue: Elements dequeued by priority, not order.
Higher priority elements are served first.

Python uses heapq module or queue.PriorityQueue
""")

import heapq

# heapq implements a min-heap
heap = []
heapq.heappush(heap, (3, "Low priority"))
heapq.heappush(heap, (1, "High priority"))
heapq.heappush(heap, (2, "Medium priority"))

print("Priority Queue (min-heap):")
while heap:
    priority, task = heapq.heappop(heap)
    print(f"  Processing: {task} (priority {priority})")

# ========== WHEN TO USE QUEUES ==========
print("\n" + "=" * 50)
print("WHEN TO USE QUEUES")
print("=" * 50)

print("""
Use a Queue when:
✅ FIFO order is needed
✅ Breadth-First Search (BFS)
✅ Level-order tree traversal
✅ Task scheduling
✅ Print queues
✅ Message queues
✅ Buffer management

Stack vs Queue:
- Stack (LIFO): Undo, DFS, backtracking
- Queue (FIFO): BFS, scheduling, buffers
""")

# ========== COMPARISON TABLE ==========
print("\n" + "=" * 50)
print("STACK VS QUEUE COMPARISON")
print("=" * 50)

print("""
| Feature     | Stack (LIFO)      | Queue (FIFO)      |
|-------------|-------------------|-------------------|
| Add         | push() to TOP     | enqueue() to BACK |
| Remove      | pop() from TOP    | dequeue() from FRONT |
| View        | peek() at TOP     | peek() at FRONT   |
| Use case    | Undo, DFS         | BFS, scheduling   |
| Memory      | Last in, first out| First in, first out|
""")

print("\n" + "=" * 50)
print("✅ Queues - Complete!")
print("=" * 50)
print("\nNext: Let's learn about Hash Maps! 🚀")
