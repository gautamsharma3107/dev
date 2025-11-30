"""
Day 5 - Stacks
==============
Learn: Stack data structure implementation and use cases

Key Concepts:
- LIFO: Last In, First Out
- Push: Add to top
- Pop: Remove from top
- Peek: View top without removing
- O(1) for all core operations
"""

# ========== WHAT IS A STACK? ==========
print("=" * 50)
print("WHAT IS A STACK?")
print("=" * 50)

print("""
Stack = LIFO (Last In, First Out)

Think of a stack of plates:
- Add plate on TOP
- Remove plate from TOP
- Can only see the TOP plate

        ┌─────┐
        │  3  │  ← TOP (most recent)
        ├─────┤
        │  2  │
        ├─────┤
        │  1  │  ← BOTTOM (first added)
        └─────┘

Core Operations:
- push(item): Add to top - O(1)
- pop(): Remove from top - O(1)
- peek()/top(): View top - O(1)
- is_empty(): Check if empty - O(1)
- size(): Get count - O(1)
""")

# ========== STACK USING PYTHON LIST ==========
print("\n" + "=" * 50)
print("SIMPLE STACK (Using Python List)")
print("=" * 50)

# Python list works perfectly as a stack!
stack = []

# Push operations
stack.append(1)
stack.append(2)
stack.append(3)
print(f"After pushing 1, 2, 3: {stack}")

# Peek (view top)
top = stack[-1]
print(f"Top element (peek): {top}")

# Pop operations
removed = stack.pop()
print(f"Popped: {removed}, Stack now: {stack}")

# Check empty
is_empty = len(stack) == 0
print(f"Is empty? {is_empty}")

# ========== STACK CLASS IMPLEMENTATION ==========
print("\n" + "=" * 50)
print("STACK CLASS IMPLEMENTATION")
print("=" * 50)

class Stack:
    """Stack implementation using list"""
    
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Add item to top - O(1)"""
        self._items.append(item)
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self._items)
    
    def __str__(self):
        return f"Stack({self._items})"
    
    def __repr__(self):
        return self.__str__()

# Demonstrate
stack = Stack()
print("Created new stack")

stack.push(10)
stack.push(20)
stack.push(30)
print(f"After push(10, 20, 30): {stack}")

print(f"Peek: {stack.peek()}")
print(f"Size: {stack.size()}")
print(f"Pop: {stack.pop()}")
print(f"After pop: {stack}")

# ========== USE CASE 1: REVERSE A STRING ==========
print("\n" + "=" * 50)
print("USE CASE 1: REVERSE A STRING")
print("=" * 50)

def reverse_string(s):
    """Reverse string using stack"""
    stack = []
    
    # Push all characters
    for char in s:
        stack.append(char)
    
    # Pop all characters
    result = ""
    while stack:
        result += stack.pop()
    
    return result

test = "Hello World"
print(f"Original: '{test}'")
print(f"Reversed: '{reverse_string(test)}'")

# ========== USE CASE 2: BALANCED PARENTHESES ==========
print("\n" + "=" * 50)
print("USE CASE 2: BALANCED PARENTHESES")
print("=" * 50)

def is_balanced(expression):
    """
    Check if parentheses/brackets are balanced
    Classic stack problem!
    """
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {")": "(", "}": "{", "]": "["}
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Test cases
test_cases = [
    "()",          # Balanced
    "([])",        # Balanced
    "([)]",        # Not balanced
    "((()))",      # Balanced
    "(()",         # Not balanced
    "{[()]}",      # Balanced
    "",            # Balanced (empty)
]

print("Checking balanced parentheses:")
for expr in test_cases:
    result = "✅ Balanced" if is_balanced(expr) else "❌ Not balanced"
    display = expr if expr else "(empty)"
    print(f"  '{display}': {result}")

# ========== USE CASE 3: EVALUATE POSTFIX EXPRESSION ==========
print("\n" + "=" * 50)
print("USE CASE 3: POSTFIX EXPRESSION EVALUATION")
print("=" * 50)

print("""
Postfix notation: Operators come AFTER operands
- Infix:   2 + 3
- Postfix: 2 3 +

Algorithm:
1. Scan left to right
2. If operand: push to stack
3. If operator: pop two operands, calculate, push result
""")

def evaluate_postfix(expression):
    """Evaluate postfix expression"""
    stack = []
    operators = {'+', '-', '*', '/'}
    
    tokens = expression.split()
    
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()  # Second operand (popped first!)
            a = stack.pop()  # First operand
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a // b  # Integer division
            
            stack.append(result)
    
    return stack.pop()

# Test
expressions = [
    ("2 3 +", "2 + 3"),           # = 5
    ("5 2 -", "5 - 2"),           # = 3
    ("3 4 *", "3 * 4"),           # = 12
    ("2 3 + 4 *", "(2 + 3) * 4"), # = 20
    ("5 1 2 + 4 * + 3 -", "5 + ((1 + 2) * 4) - 3"),  # = 14
]

print("\nEvaluating postfix expressions:")
for postfix, infix in expressions:
    result = evaluate_postfix(postfix)
    print(f"  Postfix: '{postfix}' = {result}")
    print(f"    Infix: {infix}")

# ========== USE CASE 4: UNDO FUNCTIONALITY ==========
print("\n" + "=" * 50)
print("USE CASE 4: UNDO FUNCTIONALITY")
print("=" * 50)

class TextEditor:
    """Simple text editor with undo"""
    
    def __init__(self):
        self.text = ""
        self.history = []  # Stack of previous states
    
    def write(self, new_text):
        """Add text and save state"""
        self.history.append(self.text)
        self.text += new_text
    
    def delete(self, n):
        """Delete last n characters"""
        self.history.append(self.text)
        self.text = self.text[:-n] if n <= len(self.text) else ""
    
    def undo(self):
        """Restore previous state"""
        if self.history:
            self.text = self.history.pop()
            return True
        return False
    
    def __str__(self):
        return f"'{self.text}'"

# Demonstrate
editor = TextEditor()
print("Text Editor Demo:")
print(f"Initial: {editor}")

editor.write("Hello")
print(f"After write('Hello'): {editor}")

editor.write(" World")
print(f"After write(' World'): {editor}")

editor.delete(5)
print(f"After delete(5): {editor}")

editor.undo()
print(f"After undo(): {editor}")

editor.undo()
print(f"After undo(): {editor}")

# ========== USE CASE 5: NEXT GREATER ELEMENT ==========
print("\n" + "=" * 50)
print("USE CASE 5: NEXT GREATER ELEMENT")
print("=" * 50)

print("""
For each element, find the next element that is greater.
- Input:  [4, 5, 2, 10, 8]
- Output: [5, 10, 10, -1, -1]
  (4→5, 5→10, 2→10, 10→none, 8→none)
""")

def next_greater_element(arr):
    """Find next greater element for each - O(n)"""
    n = len(arr)
    result = [-1] * n
    stack = []  # Stack of indices
    
    for i in range(n):
        # Pop elements smaller than current
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    
    return result

arr = [4, 5, 2, 10, 8]
result = next_greater_element(arr)
print(f"Input:  {arr}")
print(f"Output: {result}")

# ========== USE CASE 6: FUNCTION CALL STACK ==========
print("\n" + "=" * 50)
print("USE CASE 6: FUNCTION CALL STACK (Concept)")
print("=" * 50)

print("""
The call stack tracks function execution:

def a():
    b()  ← a calls b

def b():
    c()  ← b calls c

def c():
    pass  ← c returns

Call Stack grows/shrinks:
┌───────┐
│   c   │ ← Currently executing
├───────┤
│   b   │
├───────┤
│   a   │
├───────┤
│  main │
└───────┘

When c() returns, it's popped from stack
Then b() continues, and so on...

This is why:
- Infinite recursion → Stack Overflow!
- Debuggers show "stack trace"
""")

def demonstrate_call_stack(n):
    """Show recursion using stack"""
    print(f"  {'  ' * n}Entering level {n}")
    if n > 0:
        demonstrate_call_stack(n - 1)
    print(f"  {'  ' * n}Exiting level {n}")

print("\nRecursive call demonstration:")
demonstrate_call_stack(3)

# ========== WHEN TO USE STACKS ==========
print("\n" + "=" * 50)
print("WHEN TO USE STACKS")
print("=" * 50)

print("""
Use a Stack when:
✅ LIFO order is needed
✅ Undo/Redo functionality
✅ Parsing expressions (brackets, math)
✅ Depth-First Search (DFS)
✅ Backtracking algorithms
✅ Function call management
✅ Browser back button

Real-world examples:
- Text editor undo
- Browser back button
- Ctrl+Z in any app
- Syntax checking in compilers
- Expression evaluation
""")

# ========== STACK VS OTHER STRUCTURES ==========
print("\n" + "=" * 50)
print("STACK VS OTHER STRUCTURES")
print("=" * 50)

print("""
Structure | Order  | Use Case
----------|--------|------------------
Stack     | LIFO   | Undo, DFS, parsing
Queue     | FIFO   | BFS, task scheduling
Array     | Random | Direct index access
""")

print("\n" + "=" * 50)
print("✅ Stacks - Complete!")
print("=" * 50)
print("\nNext: Let's learn about Queues! 🚀")
