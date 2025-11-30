"""
DAY 4 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 4 ASSESSMENT - File Handling & Exceptions")
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
Q1. Which mode opens a file for both reading and writing without 
    erasing existing content?
a) 'w+'
b) 'r+'
c) 'a+'
d) 'rw'

Your answer: """)

print("""
Q2. What does the 'with' statement do when working with files?
a) Opens the file faster
b) Automatically closes the file after the block
c) Encrypts the file contents
d) Creates a backup of the file

Your answer: """)

print("""
Q3. Which method reads all lines into a list?
a) read()
b) readline()
c) readlines()
d) readall()

Your answer: """)

print("""
Q4. What happens if you don't handle an exception?
a) Python ignores it
b) The program crashes with a traceback
c) The exception is logged automatically
d) Python automatically retries

Your answer: """)

print("""
Q5. What does the 'finally' block do?
a) Runs only if no exception occurred
b) Runs only if an exception occurred
c) Always runs regardless of exceptions
d) Runs after the program ends

Your answer: """)

print("""
Q6. What module is used to work with JSON files in Python?
a) jsonlib
b) json
c) js
d) simplejson

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to read a file and print the number 
    of lines. Handle FileNotFoundError gracefully.
""")

# Write your code here:




print("""
Q8. (2 points) Write a function safe_int(value) that converts
    a value to integer. Return 0 if conversion fails.
    Use try/except.
""")

# Write your code here:




print("""
Q9. (2 points) Write code to save this dictionary to a JSON file:
    data = {"name": "Alice", "age": 25, "city": "NYC"}
    Use proper formatting (indent=4).
""")

# Write your code here:
data = {"name": "Alice", "age": 25, "city": "NYC"}




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between:
     - except Exception as e:
     - except:
     
     Which is better practice and why?

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
Q1: b) 'r+' (read and write, file must exist)
Q2: b) Automatically closes the file after the block
Q3: c) readlines()
Q4: b) The program crashes with a traceback
Q5: c) Always runs regardless of exceptions
Q6: b) json

Section B:
Q7:
try:
    with open("filename.txt", "r") as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")
except FileNotFoundError:
    print("Error: File not found!")

Q8:
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0

Q9:
import json
data = {"name": "Alice", "age": 25, "city": "NYC"}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

Section C:
Q10:
- 'except Exception as e:' captures the exception object,
  letting you access error message and type. More specific.
  
- 'except:' catches ALL exceptions including KeyboardInterrupt
  and SystemExit, which you usually don't want to catch.
  Also doesn't give access to error details.

Best practice: Always use 'except Exception as e:' or catch
specific exception types. This gives you error details and
doesn't catch system exceptions you shouldn't handle.
"""
