"""
DAY 1 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 1 ASSESSMENT TEST - Python Crash Course Part 1")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What is the output of: print(type(10))
a) <class 'float'>
b) <class 'int'>
c) <class 'str'>
d) 10

Your answer: """)

print("""
Q2. What does the modulus operator (%) return?
a) Quotient
b) Remainder
c) Exponent
d) Floor division

Your answer: """)

print("""
Q3. Which of the following is NOT a valid variable name in Python?
a) my_var
b) _myvar
c) 2myvar
d) myVar2

Your answer: """)

print("""
Q4. What is the result of: bool("")  (empty string)
a) True
b) False
c) Error
d) None

Your answer: """)

print("""
Q5. What does the following code print: "Python"[::-1]
a) Python
b) nohtyP
c) P
n) Error

Your answer: """)

print("""
Q6. Which operator is used for exponentiation in Python?
a) ^
b) **
c) pow
d) exp

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to swap two variables without using a third variable.
Given: a = 10, b = 20
Expected output: a = 20, b = 10
""")

# Write your code here:
a = 10
b = 20

# Your swapping code:



print(f"After swap: a = {a}, b = {b}")

print("""
Q8. (2 points) Write code to check if a number is even or odd.
Ask user for input and print "Even" or "Odd"
""")

# Write your code here:




print("""
Q9. (2 points) Write code to print all numbers from 1 to 20, but skip numbers divisible by 3.
Use a loop and continue statement.
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between '==' and 'is' operators in Python.
Give an example where they give different results.

Your answer:
""")

# Write your explanation here as comments:
# 




# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: b) <class 'int'>
Q2: b) Remainder
Q3: c) 2myvar (cannot start with number)
Q4: b) False (empty string is falsy)
Q5: b) nohtyP (reverses the string)
Q6: b) **

Section B (Coding):
Q7: a, b = b, a  (or a = a + b; b = a - b; a = a - b)

Q8: 
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

Q9:
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

Section C:
Q10: 
- '==' checks if values are equal
- 'is' checks if objects are same in memory
Example:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True (same values)
print(list1 is list2)  # False (different objects)
"""
