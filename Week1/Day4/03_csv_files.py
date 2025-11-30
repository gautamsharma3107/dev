"""
Day 4 - CSV Files
=================
Learn: Reading and writing CSV files

Key Concepts:
- CSV = Comma Separated Values
- Common for tabular data
- Use csv module for proper handling
- DictReader/DictWriter for named columns
"""

import csv
import os

# ========== CSV BASICS ==========
print("=" * 50)
print("CSV FILE BASICS")
print("=" * 50)

print("""
CSV (Comma Separated Values):
- Plain text for tabular data
- Each line = one row
- Values separated by commas
- First row often = headers
""")

# ========== CREATING CSV ==========
print("=" * 50)
print("CREATING CSV FILES")
print("=" * 50)

# Using csv.writer
data = [
    ["Name", "Age", "City", "Salary"],
    ["John", 25, "New York", 50000],
    ["Jane", 30, "Los Angeles", 65000],
    ["Bob", 22, "Chicago", 45000],
    ["Alice", 28, "Houston", 55000]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ Created 'employees.csv'")
print("\nFile contents:")
with open("employees.csv", "r") as file:
    print(file.read())

# ========== READING CSV ==========
print("=" * 50)
print("READING CSV FILES")
print("=" * 50)

# Method 1: csv.reader
print("1. Using csv.reader:")
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"   {row}")

# Method 2: Skip header
print("\n2. Skip header:")
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header
    print(f"   Header: {header}")
    for row in reader:
        print(f"   {row[0]} is {row[1]} years old")

# ========== DICTREADER & DICTWRITER ==========
print("\n" + "=" * 50)
print("DICTREADER AND DICTWRITER")
print("=" * 50)

# DictReader - rows as dictionaries
print("1. DictReader:")
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"   {row['Name']}: ${row['Salary']} in {row['City']}")

# DictWriter - write from dictionaries
print("\n2. DictWriter:")
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
    {"id": 3, "name": "Keyboard", "price": 79.99}
]

with open("products.csv", "w", newline="") as file:
    fieldnames = ["id", "name", "price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print("   ✅ Created 'products.csv'")
with open("products.csv", "r") as file:
    print(file.read())

# ========== DIFFERENT DELIMITERS ==========
print("=" * 50)
print("DIFFERENT DELIMITERS")
print("=" * 50)

# Tab-separated (TSV)
grades = [
    ["Name", "Score", "Grade"],
    ["John", 95, "A"],
    ["Jane", 87, "B"]
]

with open("grades.tsv", "w", newline="") as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(grades)

print("✅ Created 'grades.tsv' (tab-separated)")
print("\nReading TSV:")
with open("grades.tsv", "r") as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(f"   {row}")

# ========== SPECIAL CHARACTERS ==========
print("\n" + "=" * 50)
print("HANDLING SPECIAL CHARACTERS")
print("=" * 50)

# Data with commas and quotes
special = [
    ["Name", "Address", "Comment"],
    ["John", "123 Main St, Apt 4", 'Said "Hello"'],
    ["Jane", "456 Oak Ave", "Normal"]
]

with open("special.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(special)

print("✅ Created 'special.csv' with quotes")
with open("special.csv", "r") as file:
    print(file.read())

print("Reading back correctly:")
with open("special.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"   {row}")

# ========== FILTERING CSV ==========
print("\n" + "=" * 50)
print("FILTERING CSV DATA")
print("=" * 50)

print("Employees with salary > $50,000:")
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Salary"]) > 50000:
            print(f"   {row['Name']}: ${row['Salary']}")

# Statistics
print("\nSalary Statistics:")
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    salaries = [int(row["Salary"]) for row in reader]

print(f"   Count: {len(salaries)}")
print(f"   Average: ${sum(salaries)/len(salaries):,.2f}")
print(f"   Max: ${max(salaries):,}")
print(f"   Min: ${min(salaries):,}")

# ========== UPDATING CSV ==========
print("\n" + "=" * 50)
print("UPDATING CSV DATA")
print("=" * 50)

# Read, modify, write
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)
    fieldnames = reader.fieldnames

# Give 10% raise
for emp in employees:
    emp["Salary"] = int(int(emp["Salary"]) * 1.10)

with open("employees_updated.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees)

print("✅ Created 'employees_updated.csv' with 10% raise")
print("\nNew salaries:")
with open("employees_updated.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"   {row['Name']}: ${row['Salary']}")

# ========== PRACTICAL: SALES REPORT ==========
print("\n" + "=" * 50)
print("PRACTICAL: Sales Report")
print("=" * 50)

sales = [
    {"product": "Laptop", "qty": 5, "price": 999},
    {"product": "Mouse", "qty": 20, "price": 29},
    {"product": "Keyboard", "qty": 10, "price": 79},
    {"product": "Monitor", "qty": 8, "price": 299}
]

# Save
with open("sales.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["product", "qty", "price"])
    writer.writeheader()
    writer.writerows(sales)

# Generate report
print("Sales Report:")
print("-" * 40)
total = 0
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        revenue = int(row["qty"]) * int(row["price"])
        total += revenue
        print(f"   {row['product']}: {row['qty']} x ${row['price']} = ${revenue:,}")

print("-" * 40)
print(f"   TOTAL: ${total:,}")

# Cleanup
for f in ["employees.csv", "products.csv", "grades.tsv", "special.csv",
          "employees_updated.csv", "sales.csv"]:
    if os.path.exists(f):
        os.remove(f)
print("\n✅ Cleaned up files")

print("\n" + "=" * 50)
print("✅ CSV Files - Complete!")
print("=" * 50)
