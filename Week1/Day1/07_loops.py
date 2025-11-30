"""
Day 1 - Loops
=============
Learn: for loops, while loops, loop control (break, continue)

Key Concepts:
- For loops for iterating over sequences
- While loops for condition-based iteration
- range() function
- break, continue, and pass statements
- Nested loops
"""

# ========== FOR LOOP BASICS ==========
print("=" * 50)
print("FOR LOOP BASICS")
print("=" * 50)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop through a string
word = "Python"
print("\nLetters in 'Python':")
for letter in word:
    print(letter, end=" ")
print()

# ========== RANGE FUNCTION ==========
print("\n" + "=" * 50)
print("RANGE FUNCTION")
print("=" * 50)

# range(stop) - from 0 to stop-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop) - from start to stop-1
print("\nrange(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step)
print("\nrange(0, 10, 2) - even numbers:")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

print("\nrange(10, 0, -1) - countdown:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# ========== FOR LOOP EXAMPLES ==========
print("\n" + "=" * 50)
print("FOR LOOP EXAMPLES")
print("=" * 50)

# Sum of numbers
total = 0
for num in range(1, 11):
    total += num
print(f"Sum of 1 to 10: {total}")

# Multiplication table
number = 5
print(f"\nMultiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# ========== WHILE LOOP BASICS ==========
print("\n" + "=" * 50)
print("WHILE LOOP BASICS")
print("=" * 50)

# Basic while loop
count = 1
print("Count from 1 to 5:")
while count <= 5:
    print(count, end=" ")
    count += 1
print()

# While loop with condition
number = 1
print("\nPowers of 2 less than 100:")
while number < 100:
    print(number, end=" ")
    number *= 2
print()

# ========== BREAK STATEMENT ==========
print("\n" + "=" * 50)
print("BREAK STATEMENT (Exit loop)")
print("=" * 50)

# Find first number divisible by 7
for num in range(1, 50):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break

# Search in list
names = ["Alice", "Bob", "Charlie", "David"]
search = "Charlie"

for name in names:
    if name == search:
        print(f"\n{search} found!")
        break
else:
    print(f"{search} not found!")  # Executes if loop completes without break

# ========== CONTINUE STATEMENT ==========
print("\n" + "=" * 50)
print("CONTINUE STATEMENT (Skip iteration)")
print("=" * 50)

# Print odd numbers only
print("Odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print()

# Skip specific values
print("\nNumbers except 3 and 7:")
for num in range(1, 11):
    if num == 3 or num == 7:
        continue
    print(num, end=" ")
print()

# ========== NESTED LOOPS ==========
print("\n" + "=" * 50)
print("NESTED LOOPS")
print("=" * 50)

# Multiplication table
print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3d}", end=" ")
    print()

# Pattern printing
print("\nPattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# ========== LOOP WITH ELSE ==========
print("\n" + "=" * 50)
print("LOOP WITH ELSE")
print("=" * 50)

# Check if number is prime
num = 17
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    else:
        is_prime = True

print(f"{num} is {'prime' if is_prime else 'not prime'}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 1: Factorial")
print("=" * 50)

n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")

# ========== PRACTICAL EXAMPLE 2 ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 2: Guess the Number")
print("=" * 50)

import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("I'm thinking of a number between 1 and 10.")
print(f"You have {max_attempts} attempts.")

while attempts < max_attempts:
    guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"\n😞 Game over! The number was {secret_number}")

# ========== PRACTICAL EXAMPLE 3 ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 3: Menu System")
print("=" * 50)

while True:
    print("\n=== MENU ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "5":
        print("Goodbye!")
        break
    
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        continue
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == "4":
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Cannot divide by zero!")

# ========== PRACTICAL EXAMPLE 4 ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 4: Pattern Printing")
print("=" * 50)

rows = int(input("Enter number of rows: "))

print("\nPattern 1: Right triangle")
for i in range(1, rows + 1):
    print("* " * i)

print("\nPattern 2: Pyramid")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print("\nPattern 3: Numbers")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + "=" * 50)
print("✅ Loops - Complete!")
print("=" * 50)
