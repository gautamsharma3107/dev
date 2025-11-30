"""
Day 2 - List Comprehensions
============================
Learn: List comprehensions, dict comprehensions, set comprehensions

Key Concepts:
- Concise way to create lists
- More readable and often faster
- Can include conditions
- Works with dictionaries and sets too
"""

# ========== BASIC LIST COMPREHENSION ==========
print("=" * 50)
print("BASIC LIST COMPREHENSION")
print("=" * 50)

# Traditional way
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x ** 2)
print(f"Traditional: {squares_traditional}")

# List comprehension way
squares = [x ** 2 for x in range(1, 6)]
print(f"Comprehension: {squares}")

# Syntax: [expression for item in iterable]

# More examples
doubles = [x * 2 for x in range(1, 6)]
print(f"\nDoubles: {doubles}")

cubes = [x ** 3 for x in range(1, 6)]
print(f"Cubes: {cubes}")

# ========== WITH CONDITION (FILTER) ==========
print("\n" + "=" * 50)
print("WITH CONDITION (if)")
print("=" * 50)

# Even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional way
evens_traditional = []
for n in numbers:
    if n % 2 == 0:
        evens_traditional.append(n)
print(f"Traditional evens: {evens_traditional}")

# Comprehension way
evens = [n for n in numbers if n % 2 == 0]
print(f"Comprehension evens: {evens}")

# Syntax: [expression for item in iterable if condition]

# More examples
odds = [n for n in numbers if n % 2 != 0]
print(f"\nOdds: {odds}")

# Greater than 5
greater = [n for n in numbers if n > 5]
print(f"Greater than 5: {greater}")

# Divisible by 3
div_by_3 = [n for n in range(1, 31) if n % 3 == 0]
print(f"Divisible by 3 (1-30): {div_by_3}")

# ========== WITH IF-ELSE ==========
print("\n" + "=" * 50)
print("WITH IF-ELSE")
print("=" * 50)

# Label even/odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(f"Numbers: {numbers}")
print(f"Labels: {labels}")

# Syntax: [expr_if_true if condition else expr_if_false for item in iterable]

# Replace negatives with 0
nums = [-5, 3, -2, 8, -1, 0, 7]
positive = [n if n > 0 else 0 for n in nums]
print(f"\nOriginal: {nums}")
print(f"Negatives replaced: {positive}")

# Pass/Fail
scores = [85, 42, 91, 68, 55, 78]
results = ["Pass" if s >= 60 else "Fail" for s in scores]
print(f"\nScores: {scores}")
print(f"Results: {results}")

# ========== NESTED LOOPS ==========
print("\n" + "=" * 50)
print("NESTED LOOPS IN COMPREHENSION")
print("=" * 50)

# Traditional nested loop
pairs_traditional = []
for x in [1, 2, 3]:
    for y in ['a', 'b']:
        pairs_traditional.append((x, y))
print(f"Traditional: {pairs_traditional}")

# Comprehension way
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(f"Comprehension: {pairs}")

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for sublist in nested for num in sublist]
print(f"\nNested: {nested}")
print(f"Flattened: {flat}")

# Multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nMultiplication table:")
for row in table:
    print(f"  {row}")

# ========== WITH STRINGS ==========
print("\n" + "=" * 50)
print("WITH STRINGS")
print("=" * 50)

# Uppercase letters
word = "hello"
upper = [char.upper() for char in word]
print(f"Original: {word}")
print(f"Uppercase list: {upper}")
print(f"Joined: {''.join(upper)}")

# Extract vowels
sentence = "Hello World Python Programming"
vowels = [char for char in sentence.lower() if char in 'aeiou']
print(f"\nSentence: {sentence}")
print(f"Vowels: {vowels}")

# Words longer than 5 characters
words = ["apple", "cat", "banana", "dog", "elephant"]
long_words = [w for w in words if len(w) > 5]
print(f"\nWords: {words}")
print(f"Long words (>5): {long_words}")

# First letter of each word
sentence = "Python Is Really Fun"
initials = [word[0] for word in sentence.split()]
print(f"\nSentence: {sentence}")
print(f"Initials: {''.join(initials)}")

# ========== DICTIONARY COMPREHENSION ==========
print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION")
print("=" * 50)

# Basic dict comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# From two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grade_book = {name: score for name, score in zip(names, scores)}
print(f"\nGrade book: {grade_book}")

# With condition
passing = {name: score for name, score in grade_book.items() if score >= 80}
print(f"Passing students: {passing}")

# Transform keys/values
original = {"a": 1, "b": 2, "c": 3}
upper_keys = {k.upper(): v * 10 for k, v in original.items()}
print(f"\nOriginal: {original}")
print(f"Transformed: {upper_keys}")

# Swap keys and values
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# ========== SET COMPREHENSION ==========
print("\n" + "=" * 50)
print("SET COMPREHENSION")
print("=" * 50)

# Basic set comprehension
squares_set = {x**2 for x in range(-3, 4)}
print(f"Squares set (-3 to 3): {squares_set}")

# Unique first letters
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
first_letters = {w[0] for w in words}
print(f"\nWords: {words}")
print(f"Unique first letters: {first_letters}")

# ========== GENERATOR EXPRESSIONS ==========
print("\n" + "=" * 50)
print("GENERATOR EXPRESSIONS (Bonus)")
print("=" * 50)

# Generator expression (uses parentheses)
# More memory efficient for large data

# List comprehension (creates list in memory)
sum_squares_list = sum([x**2 for x in range(1000000)])

# Generator expression (doesn't create list)
sum_squares_gen = sum(x**2 for x in range(1000000))

print(f"Sum of squares (0-999999): {sum_squares_gen}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Filter and transform
print("1. Filter and transform:")
prices = [100, 250, 50, 400, 150]
discounted = [p * 0.9 for p in prices if p >= 100]
print(f"   Original prices: {prices}")
print(f"   Discounted (>=100): {discounted}")

# Example 2: Parse data
print("\n2. Parse CSV-like data:")
data = "Alice:85,Bob:92,Charlie:78"
parsed = {item.split(":")[0]: int(item.split(":")[1]) for item in data.split(",")}
print(f"   Raw: {data}")
print(f"   Parsed: {parsed}")

# Example 3: Matrix operations
print("\n3. Matrix transpose:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"   Original:")
for row in matrix:
    print(f"     {row}")
print(f"   Transposed:")
for row in transposed:
    print(f"     {row}")

# Example 4: Word lengths
print("\n4. Word lengths:")
sentence = "Python list comprehensions are powerful"
word_lengths = {word: len(word) for word in sentence.split()}
print(f"   Sentence: {sentence}")
print(f"   Word lengths: {word_lengths}")

# Example 5: Filter dictionary
print("\n5. Filter products by price:")
products = {"iPhone": 999, "AirPods": 199, "MacBook": 1999, "iPad": 799}
affordable = {k: v for k, v in products.items() if v < 1000}
print(f"   All products: {products}")
print(f"   Under $1000: {affordable}")

# Example 6: Combine comprehensions
print("\n6. Complex example - Grade analysis:")
students = {
    "Alice": [85, 90, 88],
    "Bob": [70, 75, 72],
    "Charlie": [95, 92, 98]
}

# Calculate average and determine if honors (avg >= 90)
honors = {
    name: sum(scores)/len(scores) 
    for name, scores in students.items() 
    if sum(scores)/len(scores) >= 90
}
print(f"   Students: {students}")
print(f"   Honors students (avg >= 90): {honors}")

print("\n" + "=" * 50)
print("✅ List Comprehensions - Complete!")
print("=" * 50)
