"""
Day 9 - Exercise 2: Branching Practice
========================================
Practice creating and managing branches
"""

print("=" * 60)
print("EXERCISE 2: Branching Practice")
print("=" * 60)

# ============================================================
# EXERCISE 2.1: Create and Switch Branches
# ============================================================
print("""
EXERCISE 2.1: Create and Switch Branches

TASK:
Create a feature branch and make changes on it.

STEPS:
1. Check which branch you're on
2. Create a branch called 'feature/greeting'
3. Switch to the new branch
4. Verify you're on the feature branch
5. Add a new file greet.py with: def greet(name): return f"Hello, {name}!"
6. Commit the change

COMMANDS TO USE:
- git branch
- git checkout -b OR git branch + git checkout
- git add
- git commit
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

# Check current branch
$ git branch
# * main

# Create and switch to feature branch
$ git checkout -b feature/greeting
# Switched to a new branch 'feature/greeting'

# Verify
$ git branch
#   main
# * feature/greeting

# Create new file
$ cat > greet.py << 'EOF'
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
EOF

# Commit
$ git add greet.py
$ git commit -m "Add greeting function"

VERIFY:
$ git log --oneline
# Shows commit on feature branch
$ git branch
# Shows * next to feature/greeting
""")

# ============================================================
# EXERCISE 2.2: Merge a Branch
# ============================================================
print("\n" + "=" * 60)
print("""
EXERCISE 2.2: Merge a Branch

TASK:
Merge your feature branch back into main.

STEPS:
1. Switch back to main branch
2. Verify greet.py doesn't exist on main (it was made on feature)
3. Merge feature/greeting into main
4. Verify greet.py now exists on main
5. Delete the feature branch

COMMANDS TO USE:
- git checkout
- ls
- git merge
- git branch -d
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

# Switch to main
$ git checkout main
# Switched to branch 'main'

# Check - greet.py shouldn't be here yet
$ ls
# hello.py  README.md  goodbye.py (no greet.py)

# Merge feature branch
$ git merge feature/greeting
# Fast-forward merge

# Verify
$ ls
# hello.py  README.md  goodbye.py  greet.py

# Delete feature branch
$ git branch -d feature/greeting
# Deleted branch feature/greeting

VERIFY:
$ git branch
# Only shows main
$ git log --oneline
# Shows merge commit
$ cat greet.py
# Shows the greeting function
""")

# ============================================================
# EXERCISE 2.3: Work with Multiple Branches
# ============================================================
print("\n" + "=" * 60)
print("""
EXERCISE 2.3: Work with Multiple Branches

TASK:
Create two feature branches and merge them both.

STEPS:
1. Create branch 'feature/calculator' and add calculator.py (add function)
2. Switch back to main
3. Create branch 'feature/utils' and add utils.py (helper functions)
4. Switch back to main
5. Merge both branches into main
6. View the branch graph

COMMANDS TO USE:
- git checkout -b
- git add
- git commit
- git checkout main
- git merge
- git log --oneline --graph --all
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

# First feature branch
$ git checkout -b feature/calculator
$ cat > calculator.py << 'EOF'
def add(a, b):
    return a + b
EOF
$ git add calculator.py
$ git commit -m "Add calculator with add function"

# Switch to main, create second feature
$ git checkout main
$ git checkout -b feature/utils
$ cat > utils.py << 'EOF'
def format_result(result):
    return f"Result: {result}"
EOF
$ git add utils.py
$ git commit -m "Add utils with format function"

# Merge both into main
$ git checkout main
$ git merge feature/calculator
$ git merge feature/utils

# View graph
$ git log --oneline --graph --all

# Clean up
$ git branch -d feature/calculator
$ git branch -d feature/utils

VERIFY:
$ ls
# Should have all files including calculator.py and utils.py
$ git log --oneline
# Shows all merges
""")

print("\n" + "=" * 60)
print("✅ Exercise 2 Complete!")
print("=" * 60)
print("Move on to exercise_03_remote.py")
