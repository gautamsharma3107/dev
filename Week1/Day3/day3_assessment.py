"""
DAY 3 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 3 ASSESSMENT - Functions")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What does this function return: def foo(): pass
a) None
b) 0
c) Error
d) Empty string

Your answer: """)

print("""
Q2. What is the output of: (lambda x: x * 2)(5)
a) Error
b) 10
c) lambda x: x * 2
d) 5

Your answer: """)

print("""
Q3. What does *args allow in a function?
a) Only string arguments
b) Variable number of positional arguments
c) Only keyword arguments
d) Exactly two arguments

Your answer: """)

print("""
Q4. What does filter(lambda x: x > 0, [-1, 0, 1, 2]) return?
a) [-1, 0, 1, 2]
b) [1, 2]
c) [True, False, True, True]
d) Error

Your answer: """)

print("""
Q5. Which statement about lambda functions is FALSE?
a) They can have multiple expressions
b) They are anonymous functions
c) They can have multiple arguments
d) They are defined with 'lambda' keyword

Your answer: """)

print("""
Q6. What does zip(['a','b'], [1,2]) produce (as list)?
a) [('a',1), ('b',2)]
b) {'a':1, 'b':2}
c) ['a1', 'b2']
d) [['a','b'], [1,2]]

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write a function 'multiply_all' that takes any 
number of arguments and returns their product.
Example: multiply_all(2, 3, 4) -> 24
""")

# Write your code here:




print("""
Q8. (2 points) Use map and lambda to convert this list of 
temperatures from Celsius to Fahrenheit.
celsius = [0, 10, 20, 30, 40]
Formula: F = C * 9/5 + 32
Expected: [32.0, 50.0, 68.0, 86.0, 104.0]
""")

# Write your code here:
celsius = [0, 10, 20, 30, 40]




print("""
Q9. (2 points) Write a function that takes a list of numbers 
and returns two lists: one with even numbers, one with odd.
Use tuple unpacking when calling.
Example: evens, odds = separate_numbers([1,2,3,4,5,6])
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) What is the difference between map() and filter()?
Explain with a simple example.

Your answer:
""")

# Write your explanation here as comments:
# 




print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: a) None
Q2: b) 10
Q3: b) Variable number of positional arguments
Q4: b) [1, 2]
Q5: a) They can have multiple expressions (FALSE - only one expression)
Q6: a) [('a',1), ('b',2)]

Section B:
Q7:
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Or using reduce:
from functools import reduce
def multiply_all(*args):
    return reduce(lambda a, b: a * b, args, 1)

Q8:
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

Q9:
def separate_numbers(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 != 0]
    return evens, odds

# Or using filter:
def separate_numbers(numbers):
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 != 0, numbers))
    return evens, odds

Section C:
Q10:
- map() applies a function to each element and returns transformed values
  Example: map(lambda x: x*2, [1,2,3]) -> [2,4,6]
  
- filter() applies a function to each element and keeps only those where 
  the function returns True
  Example: filter(lambda x: x>2, [1,2,3,4]) -> [3,4]
"""
