"""
DAY 2 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 2 ASSESSMENT - Lists, Dictionaries, Tuples, Sets")
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
Q1. What is the output of: [1, 2, 3][1:]
a) [1]
b) [2, 3]
c) [1, 2]
d) 2

Your answer: """)

print("""
Q2. Which method adds an element to the END of a list?
a) insert()
b) add()
c) append()
d) extend()

Your answer: """)

print("""
Q3. What does dict.get("key", "default") return if key doesn't exist?
a) None
b) Error
c) "default"
d) Empty string

Your answer: """)

print("""
Q4. Which data structure does NOT allow duplicates?
a) List
b) Tuple
c) Dictionary keys
d) All of the above allow duplicates

Your answer: """)

print("""
Q5. What is the output of: (1, 2, 3) + (4, 5)
a) [1, 2, 3, 4, 5]
b) (1, 2, 3, 4, 5)
c) Error
d) ((1, 2, 3), (4, 5))

Your answer: """)

print("""
Q6. What does {1, 2, 3} & {2, 3, 4} return?
a) {1, 2, 3, 4}
b) {2, 3}
c) {1, 4}
d) Error

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Use list comprehension to create a list of squares 
of even numbers from 1 to 10.
Expected: [4, 16, 36, 64, 100]
""")

# Write your code here:




print("""
Q8. (2 points) Given dictionary:
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 68}
Write code to find the student with highest score.
""")

# Write your code here:
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 68}




print("""
Q9. (2 points) Given two lists:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
Find elements that are in list1 but not in list2 using sets.
Expected: {1, 2, 3}
""")

# Write your code here:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between a list and a tuple.
When would you use each one? Give one example of when to use a tuple.

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
Q1: b) [2, 3]
Q2: c) append()
Q3: c) "default"
Q4: c) Dictionary keys
Q5: b) (1, 2, 3, 4, 5)
Q6: b) {2, 3}

Section B:
Q7: squares = [x**2 for x in range(1, 11) if x % 2 == 0]

Q8: 
top_student = max(scores, key=scores.get)
print(f"Topper: {top_student} with {scores[top_student]}")

Q9:
result = set(list1) - set(list2)
print(result)

Section C:
Q10: 
- Lists are mutable (can be changed), tuples are immutable
- Lists use [], tuples use ()
- Tuples are faster and use less memory
- Use tuple for fixed data like coordinates (x, y)
- Use list for data that needs to change
"""
