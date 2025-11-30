"""
Day 1 - If-Else Statements
===========================
Learn: Conditional statements, decision making, control flow

Key Concepts:
- if, elif, else statements
- Comparison and logical operators in conditions
- Nested conditions
- Ternary operator
"""

# ========== BASIC IF STATEMENT ==========
print("=" * 50)
print("BASIC IF STATEMENT")
print("=" * 50)

age = 20

if age >= 18:
    print(f"Age {age}: You are an adult!")

# If statement that doesn't execute
score = 45

if score >= 50:
    print("You passed!")  # This won't print

print("Program continues...")

# ========== IF-ELSE STATEMENT ==========
print("\n" + "=" * 50)
print("IF-ELSE STATEMENT")
print("=" * 50)

number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Another example
temperature = 15

if temperature > 25:
    print("It's hot outside!")
else:
    print("It's cool outside!")

# ========== IF-ELIF-ELSE STATEMENT ==========
print("\n" + "=" * 50)
print("IF-ELIF-ELSE STATEMENT")
print("=" * 50)

marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks}, Grade: {grade}")

# ========== NESTED IF STATEMENTS ==========
print("\n" + "=" * 50)
print("NESTED IF STATEMENTS")
print("=" * 50)

age = 25
has_license = True

if age >= 18:
    print("Age requirement met.")
    if has_license:
        print("You can drive!")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")

# ========== LOGICAL OPERATORS IN CONDITIONS ==========
print("\n" + "=" * 50)
print("LOGICAL OPERATORS IN CONDITIONS")
print("=" * 50)

# AND operator
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials!")

# OR operator
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print(f"{day}: It's weekend!")
else:
    print(f"{day}: It's a weekday.")

# NOT operator
is_raining = False

if not is_raining:
    print("You can go outside!")
else:
    print("Take an umbrella!")

# ========== MULTIPLE CONDITIONS ==========
print("\n" + "=" * 50)
print("MULTIPLE CONDITIONS")
print("=" * 50)

age = 25
income = 50000
credit_score = 720

# Loan approval example
if age >= 21 and income >= 30000 and credit_score >= 650:
    print("Loan approved!")
else:
    print("Loan denied.")
    if age < 21:
        print("Reason: Age requirement not met")
    elif income < 30000:
        print("Reason: Insufficient income")
    elif credit_score < 650:
        print("Reason: Low credit score")

# ========== TERNARY OPERATOR ==========
print("\n" + "=" * 50)
print("TERNARY OPERATOR (One-line if-else)")
print("=" * 50)

age = 20

# Regular if-else
if age >= 18:
    status = "adult"
else:
    status = "minor"
print(f"Regular: {status}")

# Ternary operator (shorter)
status = "adult" if age >= 18 else "minor"
print(f"Ternary: {status}")

# More examples
number = -5
result = "positive" if number > 0 else "negative or zero"
print(f"{number} is {result}")

score = 75
result = "Pass" if score >= 50 else "Fail"
print(f"Score {score}: {result}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 1: Login System")
print("=" * 50)

correct_username = "gautam"
correct_password = "python123"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("✅ Login successful! Welcome!")
else:
    print("❌ Invalid credentials!")

# ========== PRACTICAL EXAMPLE 2 ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 2: Grade Calculator")
print("=" * 50)

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter between 0-100.")
elif marks >= 90:
    print(f"Marks: {marks} | Grade: A+ | Excellent!")
elif marks >= 80:
    print(f"Marks: {marks} | Grade: A | Very Good!")
elif marks >= 70:
    print(f"Marks: {marks} | Grade: B | Good!")
elif marks >= 60:
    print(f"Marks: {marks} | Grade: C | Average")
elif marks >= 50:
    print(f"Marks: {marks} | Grade: D | Pass")
else:
    print(f"Marks: {marks} | Grade: F | Fail")

# ========== PRACTICAL EXAMPLE 3 ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 3: Ticket Price Calculator")
print("=" * 50)

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

base_price = 100

if age < 5:
    price = 0
    print("Free entry for children under 5!")
elif age < 18:
    price = base_price * 0.5
    print(f"Child ticket: 50% discount")
elif age >= 65:
    price = base_price * 0.6
    print(f"Senior citizen: 40% discount")
elif is_student:
    price = base_price * 0.7
    print(f"Student discount: 30% off")
else:
    price = base_price
    print("Regular ticket")

print(f"Ticket Price: ${price:.2f}")

# ========== PRACTICAL EXAMPLE 4 ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 4: BMI Calculator")
print("=" * 50)

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print(f"\nYour BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print("\n" + "=" * 50)
print("✅ If-Else Statements - Complete!")
print("=" * 50)
