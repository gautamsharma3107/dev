# Python Modules and Packages: Complete Guide

---

## Table of Contents
1. [Introduction to Modules](#introduction-to-modules)
2. [What are Modules](#what-are-modules)
3. [Importing Modules](#importing-modules)
4. [Creating Custom Modules](#creating-custom-modules)
5. [Module Organization](#module-organization)
6. [Module Search Path](#module-search-path)
7. [Packages](#packages)
8. [Relative vs Absolute Imports](#relative-vs-absolute-imports)
9. [Virtual Environments](#virtual-environments)
10. [pip and Package Management](#pip-and-package-management)
11. [Requirements.txt](#requirementstxt)
12. [Practical Examples](#practical-examples)
13. [Practice Exercises](#practice-exercises)

---

## Introduction to Modules

### What is a Module?

A module is a file containing Python code (functions, classes, variables).

### Why Use Modules?

1. **Code Organization** - Organize code into logical units
2. **Reusability** - Use code across multiple projects
3. **Namespace** - Avoid naming conflicts
4. **Maintainability** - Easier to update and debug
5. **Collaboration** - Share code with others

### Module vs Script

```python
# Script - meant to be run directly
# python my_script.py

# Module - meant to be imported
# import my_module
```

---

## What are Modules

### Built-in Modules

```python
# Using built-in modules
import math
print(math.pi)              # Output: 3.14159...

import random
print(random.randint(1, 10))  # Output: random number

import os
print(os.getcwd())          # Output: current directory
```

### Standard Library Modules

```python
# Some common standard library modules
import sys              # System operations
import os               # Operating system
import datetime         # Date and time
import json             # JSON handling
import csv              # CSV handling
import re               # Regular expressions
import collections      # Specialized containers
import itertools        # Iteration tools
import functools        # Functional tools
import pathlib          # Path operations
```

### Module Contents

```python
import math

# Get module contents
print(dir(math))        # List all attributes
print(help(math.sqrt))  # Get help on function

# Access module content
print(math.ceil(3.2))   # 4
print(math.sqrt(16))    # 4.0
```

---

## Importing Modules

### Import Statement

```python
import math

# Access using module name
result = math.sqrt(16)
print(result)  # Output: 4.0
```

### From...Import Statement

```python
from math import sqrt, pi

# Access directly without module name
result = sqrt(16)
print(result)  # Output: 4.0
print(pi)      # Output: 3.14159...
```

### Import with Alias

```python
import math as m

# Access using alias
print(m.sqrt(16))  # Output: 4.0

# Useful for long module names
from collections import Counter as Cnt
```

### Import All (Not Recommended)

```python
from math import *

# All public names imported
print(sqrt(16))    # Works
print(pi)          # Works

# Avoid this - pollutes namespace and can cause conflicts
```

### Selective Importing

```python
# Good - import what you need
from os.path import join, exists
from collections import defaultdict, Counter

# Can check if exists without importing
if exists("file.txt"):
    print("File exists")
```

### Multiple Imports

```python
# Single import statement
import sys, os, json

# Multiple from same module
from math import sqrt, sin, cos, tan

# Better style - separate lines
import sys
import os
import json
```

---

## Creating Custom Modules

### Simple Module

Create `math_helpers.py`:

```python
# math_helpers.py

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

CONSTANT = 42
```

Use the module:

```python
import math_helpers

result = math_helpers.add(5, 3)
print(result)  # Output: 8

print(math_helpers.CONSTANT)  # Output: 42
```

### Module with Classes

Create `person.py`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

Use the module:

```python
from person import Person, Employee

p = Person("Alice", 25)
print(p.greet())  # Output: Hello, I'm Alice

e = Employee("Bob", 30, "E001")
print(e.greet())  # Output: Hello, I'm Bob
```

### Module with Functions and Classes

Create `calculator.py`:

```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, x):
        self.result += x
        return self.result
    
    def clear(self):
        self.result = 0

def simple_add(a, b):
    return a + b

def simple_multiply(a, b):
    return a * b
```

Use the module:

```python
from calculator import Calculator, simple_add

# Using class
calc = Calculator()
calc.add(5)
calc.add(3)
print(calc.result)  # Output: 8

# Using function
print(simple_add(10, 5))  # Output: 15
```

---

## Module Organization

### __name__ == "__main__"

```python
# mymodule.py

def greet(name):
    print(f"Hello, {name}!")

# Code here only runs when script is executed directly
if __name__ == "__main__":
    greet("Alice")
    greet("Bob")

# When imported as module, the if block doesn't execute
```

Use the module:

```python
import mymodule

# greet() works, but __main__ block doesn't execute
mymodule.greet("Charlie")  # Works

# If you run mymodule.py directly:
# python mymodule.py
# Then __main__ block executes: Hello, Alice! Hello, Bob!
```

### Example: Tests in Module

```python
# calculator.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Run tests only when executed directly
if __name__ == "__main__":
    print("Running tests...")
    assert add(2, 3) == 5
    assert multiply(3, 4) == 12
    print("All tests passed!")
```

### Example: Main Function

```python
# script.py

def main():
    print("Running main program")
    # Your program logic here

if __name__ == "__main__":
    main()
```

---

## Module Search Path

### sys.path

```python
import sys

# Print module search path
for path in sys.path:
    print(path)

# Output example:
# /current/directory
# /usr/lib/python3.9
# /usr/local/lib/python3.9/site-packages
# ...
```

### Adding to sys.path

```python
import sys
from pathlib import Path

# Add directory to path
sys.path.insert(0, "/custom/module/path")

# Now Python will search this directory for modules
import my_custom_module

# More robust approach using pathlib
module_path = Path(__file__).parent.parent / "modules"
sys.path.insert(0, str(module_path))
```

### Module Search Order

```
1. Built-in modules (sys, os, etc.)
2. Current directory
3. PYTHONPATH environment variable
4. Installation-dependent defaults (site-packages)
```

### Finding Where Module Is

```python
import os
print(os.__file__)      # Location of os module
# Output: /usr/lib/python3.9/os.py

import math
print(math.__file__)    # Location of math module
```

---

## Packages

### What is a Package?

A package is a directory with Python modules and `__init__.py` file.

### Creating a Package

Directory structure:

```
myproject/
├── main.py
└── mypackage/
    ├── __init__.py
    ├── module1.py
    ├── module2.py
    └── subpackage/
        ├── __init__.py
        └── module3.py
```

### __init__.py

Create `mypackage/__init__.py`:

```python
# mypackage/__init__.py

# Package initialization code (optional)

# Can define package-level variables
__version__ = "1.0.0"

# Can import modules to make them accessible
from .module1 import function1
from .module2 import Class2

print("mypackage initialized")
```

Create `mypackage/module1.py`:

```python
# mypackage/module1.py

def function1():
    return "From module1"

class Class1:
    pass
```

Create `mypackage/module2.py`:

```python
# mypackage/module2.py

def function2():
    return "From module2"

class Class2:
    pass
```

### Using Packages

```python
# Import from package
from mypackage import module1
from mypackage.module1 import function1

# If __init__.py imports, can access directly
from mypackage import function1, Class2

# Import subpackage
from mypackage.subpackage import module3

# Import from subpackage
from mypackage.subpackage.module3 import function3
```

### Nested Packages

```
project/
├── main.py
└── mypackage/
    ├── __init__.py
    ├── utils/
    │   ├── __init__.py
    │   ├── string_utils.py
    │   └── math_utils.py
    └── models/
        ├── __init__.py
        ├── user.py
        └── product.py
```

Usage:

```python
from mypackage.utils.string_utils import format_string
from mypackage.models.user import User

# Or if __init__.py imports them
from mypackage.utils import format_string
from mypackage.models import User
```

---

## Relative vs Absolute Imports

### Absolute Imports

```python
# From mypackage/module1.py

# Absolute import
from mypackage.module2 import function2

# Works from any location
```

### Relative Imports

```python
# From mypackage/module1.py

# Relative import - import from same package
from . import module2
from .module2 import function2

# Import from subpackage
from .subpackage.module3 import function3

# Import from parent package
from .. import other_module
```

### Best Practices

```python
# Prefer absolute imports
from mypackage.utils import helper_function

# Relative imports for intra-package references
from .models import User
from ..utils import helper
```

---

## Virtual Environments

### Why Virtual Environments?

1. **Isolation** - Different projects need different packages
2. **Compatibility** - Control package versions per project
3. **Reproducibility** - Same environment across machines
4. **Cleanliness** - Don't pollute system Python

### Creating Virtual Environment

```bash
# Using venv (Python 3.3+, built-in)
python -m venv myenv

# Using virtualenv (third-party, older Python support)
virtualenv myenv

# Using conda
conda create --name myenv python=3.9
```

### Activating Virtual Environment

```bash
# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate

# Conda
conda activate myenv
```

### Deactivating Virtual Environment

```bash
deactivate
```

### Virtual Environment Structure

```
myenv/
├── bin/              # Executables (macOS/Linux)
│   ├── python
│   ├── pip
│   └── activate
├── Scripts/          # Executables (Windows)
│   ├── python.exe
│   ├── pip.exe
│   └── activate.bat
├── lib/              # Site-packages
│   └── python3.9/
│       └── site-packages/
└── pyvenv.cfg
```

---

## pip and Package Management

### Installing Packages

```bash
# Basic installation
pip install requests

# Specific version
pip install requests==2.28.0

# Minimum version
pip install "requests>=2.25.0"

# Latest compatible version
pip install requests~=2.28.0

# Multiple packages
pip install requests flask django

# From file
pip install -r requirements.txt
```

### Listing Installed Packages

```bash
# List installed packages
pip list

# Show specific package info
pip show requests

# Output includes:
# Name: requests
# Version: 2.28.0
# Location: /path/to/site-packages
# Requires: charset-normalizer, idna, urllib3, certifi
```

### Upgrading Packages

```bash
# Upgrade single package
pip install --upgrade requests

# Upgrade pip itself
pip install --upgrade pip
```

### Uninstalling Packages

```bash
# Remove package
pip uninstall requests

# Remove multiple
pip uninstall requests flask django

# Remove without confirmation
pip uninstall -y requests
```

### Searching for Packages

```bash
# Search on PyPI (via command line)
pip search requests  # Disabled on PyPI, use website instead

# Visit https://pypi.org/ to search
```

---

## requirements.txt

### Creating requirements.txt

```bash
# Generate from current environment
pip freeze > requirements.txt

# Manual creation - list packages needed
# requirements.txt
requests==2.28.0
flask==2.1.0
django>=4.0
numpy~=1.20.0
```

### Installing from requirements.txt

```bash
# Install all packages
pip install -r requirements.txt

# Install with specific python version
python -m pip install -r requirements.txt
```

### Example requirements.txt

```
# Web framework
flask==2.1.0
django==4.0.0

# HTTP requests
requests==2.28.0

# Data science
numpy>=1.20.0
pandas>=1.3.0

# Testing
pytest>=7.0
pytest-cov>=3.0

# Code quality
black==22.0
flake8>=4.0
```

### Using Multiple requirements Files

```
requirements/
├── base.txt          # Common dependencies
├── dev.txt           # Development dependencies
├── test.txt          # Testing dependencies
└── prod.txt          # Production dependencies
```

Content of `requirements/base.txt`:

```
flask==2.1.0
requests==2.28.0
```

Content of `requirements/dev.txt`:

```
-r base.txt
black==22.0
flake8>=4.0
```

Usage:

```bash
# Install base
pip install -r requirements/base.txt

# Install development (includes base)
pip install -r requirements/dev.txt
```

---

## Site-packages

### What is site-packages?

Directory where pip installs packages.

```python
import site
print(site.getsitepackages())
# Output: ['/usr/local/lib/python3.9/site-packages', ...]

# User-specific site-packages
print(site.getusersitepackages())
# Output: '/home/user/.local/lib/python3.9/site-packages'
```

### Locations by System

```
# macOS
/Library/Python/3.9/site-packages
~/.local/lib/python3.9/site-packages

# Linux
/usr/lib/python3/dist-packages
~/.local/lib/python3.9/site-packages

# Windows
C:\Python39\Lib\site-packages
C:\Users\User\AppData\Local\Python\Python39\site-packages
```

### Global vs Virtual Environment

```bash
# System Python - installs to system site-packages (requires sudo)
# pip install package  # May need sudo

# Virtual Environment - installs to venv site-packages (no sudo needed)
source myenv/bin/activate
pip install package  # Installs to myenv/lib/python3.9/site-packages
```

---

## Practical Examples

### Project Structure

```
myproject/
├── main.py
├── requirements.txt
├── venv/
├── myapp/
│   ├── __init__.py
│   ├── core.py
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       └── validators.py
└── tests/
    ├── __init__.py
    └── test_core.py
```

### Example: Creating a Package

Create `myapp/__init__.py`:

```python
__version__ = "1.0.0"

from .core import Application
from .utils.helpers import format_output
```

Create `myapp/core.py`:

```python
class Application:
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print(f"Running {self.name}")
```

Create `myapp/utils/__init__.py`:

```python
# Empty or minimal initialization
```

Create `myapp/utils/helpers.py`:

```python
def format_output(text):
    return f"==> {text} <=="
```

Create `main.py`:

```python
from myapp import Application, format_output

app = Application("MyApp")
app.run()
print(format_output("Application ready"))
```

### Example: Using Virtual Environment

```bash
# Create project
mkdir myproject
cd myproject

# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux

# Create requirements.txt
echo "flask==2.1.0
requests==2.28.0" > requirements.txt

# Install packages
pip install -r requirements.txt

# Work on project...

# Deactivate when done
deactivate
```

### Example: Setup.py (Package Distribution)

Create `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    description="My awesome package",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "flask>=2.0.0",
    ],
    python_requires=">=3.7",
)
```

Install locally:

```bash
pip install -e .  # Install in development mode
```

---

## Practice Exercises

### 1. Creating Modules
- Create a simple module with functions
- Create a module with classes
- Import and use the module

### 2. Packages
- Create a package structure
- Create __init__.py files
- Use relative imports

### 3. Virtual Environments
- Create virtual environment
- Install packages
- Generate requirements.txt

### 4. Package Management
- Install packages with pip
- Create requirements files
- Update packages

### 5. Module Search Path
- Check sys.path
- Add custom paths
- Understand import order

### 6. Real-World Project
- Create project structure
- Use virtual environment
- Create package with submodules
- Write requirements.txt

---

# End of Notes
