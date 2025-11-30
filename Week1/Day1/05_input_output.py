"""
Day 1 - Input and Output
=========================
Learn: Taking user input, displaying output, formatting

Key Concepts:
- input() function for user input
- print() function for output
- Type conversion for input
- String formatting for better output
"""

# ========== BASIC OUTPUT ==========
print("=" * 50)
print("BASIC OUTPUT")
print("=" * 50)

# Simple print
print("Hello, World!")

# Multiple arguments
print("Hello", "World", "from", "Python")

# Custom separator
print("Apple", "Banana", "Cherry", sep=" | ")

# Custom ending (default is newline)
print("Loading", end="...")
print("Done!")

# Print multiple lines
print("\nMultiple\nLines\nWith\nNewline")

# ========== PRINT FORMATTING ==========
print("\n" + "=" * 50)
print("PRINT FORMATTING")
print("=" * 50)

name = "Gautam"
age = 25
height = 5.9

# f-strings
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.1f} feet")

# Multiple variables
print(f"{name} is {age} years old and {height} feet tall.")

# Expressions in f-strings
print(f"Next year, {name} will be {age + 1} years old.")

# ========== BASIC INPUT ==========
print("\n" + "=" * 50)
print("BASIC INPUT")
print("=" * 50)

print("Let's get to know you!")
print("-" * 30)

# Taking string input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Taking integer input
age_str = input("Enter your age: ")
age = int(age_str)
print(f"You are {age} years old.")
print(f"Next year, you will be {age + 1}!")

# Taking float input
height_str = input("Enter your height in feet: ")
height = float(height_str)
print(f"Your height is {height} feet ({height * 30.48:.2f} cm).")

# ========== INPUT TYPE CONVERSION ==========
print("\n" + "=" * 50)
print("INPUT TYPE CONVERSION")
print("=" * 50)

# Method 1: Convert after input
num1_str = input("Enter first number: ")
num1 = int(num1_str)

# Method 2: Convert during input (more common)
num2 = int(input("Enter second number: "))

result = num1 + num2
print(f"\n{num1} + {num2} = {result}")

# ========== MULTIPLE INPUTS ==========
print("\n" + "=" * 50)
print("MULTIPLE INPUTS")
print("=" * 50)

# Taking multiple values in one line
print("Enter three numbers separated by space:")
numbers = input().split()
print(f"You entered: {numbers}")

# Convert to integers
num_list = [int(x) for x in numbers]
print(f"As integers: {num_list}")
print(f"Sum: {sum(num_list)}")

# Using map for conversion (shorter way)
print("\nEnter three numbers separated by space:")
a, b, c = map(int, input().split())
print(f"Numbers: {a}, {b}, {c}")
print(f"Product: {a * b * c}")

# ========== PRACTICAL EXAMPLES ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 1: Calculator")
print("=" * 50)

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"\nResult: {num1} {operator} {num2} = {result}")

# ========== PRACTICAL EXAMPLE 2 ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 2: User Profile")
print("=" * 50)

print("Create Your Profile")
print("-" * 30)

name = input("Full Name: ")
age = int(input("Age: "))
city = input("City: ")
hobby = input("Favorite Hobby: ")

print("\n" + "=" * 50)
print("YOUR PROFILE")
print("=" * 50)
print(f"Name:  {name}")
print(f"Age:   {age}")
print(f"City:  {city}")
print(f"Hobby: {hobby}")
print("=" * 50)

# ========== PRACTICAL EXAMPLE 3 ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE 3: Shopping Bill")
print("=" * 50)

item1 = input("Item 1 name: ")
price1 = float(input("Item 1 price: $"))

item2 = input("Item 2 name: ")
price2 = float(input("Item 2 price: $"))

item3 = input("Item 3 name: ")
price3 = float(input("Item 3 price: $"))

subtotal = price1 + price2 + price3
tax = subtotal * 0.08  # 8% tax
total = subtotal + tax

print("\n" + "=" * 50)
print("SHOPPING BILL")
print("=" * 50)
print(f"{item1:<20} ${price1:>8.2f}")
print(f"{item2:<20} ${price2:>8.2f}")
print(f"{item3:<20} ${price3:>8.2f}")
print("-" * 30)
print(f"{'Subtotal':<20} ${subtotal:>8.2f}")
print(f"{'Tax (8%)':<20} ${tax:>8.2f}")
print("=" * 30)
print(f"{'TOTAL':<20} ${total:>8.2f}")
print("=" * 50)

# ========== TIPS ==========
print("\n" + "=" * 50)
print("TIPS FOR INPUT/OUTPUT")
print("=" * 50)
print("""
1. Always convert input() to appropriate type (int, float, etc.)
2. Use f-strings for formatting (cleaner and faster)
3. Handle invalid input with try-except (we'll learn later)
4. Use descriptive prompts for user input
5. Format output for better readability
""")

print("=" * 50)
print("✅ Input and Output - Complete!")
print("=" * 50)
