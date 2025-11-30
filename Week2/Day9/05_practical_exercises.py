"""
Day 9 - Practical Git Exercises
===============================
Learn: Hands-on Git practice with real scenarios

Complete these exercises to master Git!
"""

# ========== EXERCISE OVERVIEW ==========
print("=" * 60)
print("DAY 9 - PRACTICAL GIT EXERCISES")
print("=" * 60)

overview = """
These exercises will help you practice Git commands in real scenarios.

For each exercise:
1. Read the scenario
2. Try to complete without looking at the solution
3. Check your work with the provided commands
4. Refer to solution only if stuck

Prerequisites:
- Git installed (check: git --version)
- GitHub account created
- Terminal/command line access
"""
print(overview)

# ========== EXERCISE 1 ==========
print("\n" + "=" * 60)
print("EXERCISE 1: Initialize Your First Repository")
print("=" * 60)

exercise_1 = """
SCENARIO:
You're starting a new Python project for a calculator app.
Create a new repository from scratch.

TASKS:
1. Create a new folder called 'calculator-app'
2. Initialize a Git repository
3. Create a README.md with project description
4. Create a main.py with a simple hello world
5. Stage and commit your files

TRY IT YOURSELF FIRST!

────────────────────────────────────────

SOLUTION:
$ mkdir calculator-app
$ cd calculator-app
$ git init
$ echo "# Calculator App" > README.md
$ echo "print('Hello, Calculator!')" > main.py
$ git status
$ git add .
$ git commit -m "Initial commit: Add README and main.py"
$ git log --oneline

VERIFY:
$ git status
# Should show "nothing to commit, working tree clean"
$ git log --oneline
# Should show your commit
"""
print(exercise_1)

# ========== EXERCISE 2 ==========
print("\n" + "=" * 60)
print("EXERCISE 2: Create and Merge a Feature Branch")
print("=" * 60)

exercise_2 = """
SCENARIO:
You need to add an 'add' function to your calculator.
Create a feature branch, make changes, and merge back to main.

TASKS:
1. Create a branch called 'feature/add-function'
2. Switch to the new branch
3. Add an add function to main.py
4. Commit your changes
5. Switch back to main
6. Merge the feature branch
7. Delete the feature branch

TRY IT YOURSELF FIRST!

────────────────────────────────────────

SOLUTION:
# Create and switch to feature branch
$ git checkout -b feature/add-function

# Edit main.py (add this content)
$ cat > main.py << 'EOF'
def add(a, b):
    return a + b

print("Calculator ready!")
print(f"2 + 3 = {add(2, 3)}")
EOF

# Stage and commit
$ git add main.py
$ git commit -m "Add addition function"

# Switch to main and merge
$ git checkout main
$ git merge feature/add-function

# Delete the feature branch
$ git branch -d feature/add-function

VERIFY:
$ git log --oneline
# Should show merge commit
$ cat main.py
# Should show the add function
"""
print(exercise_2)

# ========== EXERCISE 3 ==========
print("\n" + "=" * 60)
print("EXERCISE 3: Create a .gitignore")
print("=" * 60)

exercise_3 = """
SCENARIO:
Your Python project has generated some files that shouldn't
be tracked: __pycache__, .env file, and .vscode folder.

TASKS:
1. Create the files/folders that should be ignored
2. Create a .gitignore file
3. Add appropriate patterns
4. Verify the files are being ignored

TRY IT YOURSELF FIRST!

────────────────────────────────────────

SOLUTION:
# Create files that should be ignored (for demo)
$ mkdir __pycache__ .vscode
$ echo "SECRET_KEY=abc123" > .env
$ echo "temp" > __pycache__/temp.pyc
$ echo "settings" > .vscode/settings.json

# Create .gitignore
$ cat > .gitignore << 'EOF'
# Python
__pycache__/
*.pyc
*.pyo

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
EOF

# Stage and commit
$ git add .gitignore
$ git commit -m "Add .gitignore for Python project"

VERIFY:
$ git status
# Should NOT show __pycache__, .env, or .vscode as untracked
# Only .gitignore should be shown (which we committed)
"""
print(exercise_3)

# ========== EXERCISE 4 ==========
print("\n" + "=" * 60)
print("EXERCISE 4: Connect to GitHub and Push")
print("=" * 60)

exercise_4 = """
SCENARIO:
You want to backup your calculator project to GitHub.

TASKS:
1. Create a new repository on GitHub (in browser)
   - Name: calculator-app
   - Do NOT initialize with README (you already have files)
2. Connect your local repo to GitHub
3. Push your code to GitHub
4. Verify it appears on GitHub

TRY IT YOURSELF FIRST!

────────────────────────────────────────

SOLUTION:
# After creating repo on GitHub:

# Add remote
$ git remote add origin https://github.com/YOUR-USERNAME/calculator-app.git

# Verify remote is added
$ git remote -v

# Push to GitHub (first time)
$ git branch -M main
$ git push -u origin main

# For subsequent pushes
$ git push

VERIFY:
- Go to GitHub
- Navigate to your calculator-app repo
- You should see all your files!
"""
print(exercise_4)

# ========== EXERCISE 5 ==========
print("\n" + "=" * 60)
print("EXERCISE 5: Simulate Collaboration")
print("=" * 60)

exercise_5 = """
SCENARIO:
Simulate what happens when a colleague makes changes.
You'll edit directly on GitHub, then pull the changes locally.

TASKS:
1. On GitHub, edit README.md (add some description)
2. Commit the change directly on GitHub
3. Locally, check if you're behind
4. Pull the changes
5. View the updated README locally

TRY IT YOURSELF FIRST!

────────────────────────────────────────

SOLUTION:
# ON GITHUB:
# 1. Go to your repository
# 2. Click on README.md
# 3. Click pencil icon (edit)
# 4. Add: "A simple calculator app built with Python"
# 5. Commit changes

# LOCALLY:
# Fetch to see if there are changes
$ git fetch
$ git status
# Should show "Your branch is behind..."

# Pull the changes
$ git pull origin main

# Verify
$ cat README.md
# Should show your new description

VERIFY:
$ git log --oneline
# Should show the commit from GitHub
"""
print(exercise_5)

# ========== EXERCISE 6 ==========
print("\n" + "=" * 60)
print("EXERCISE 6: Handle Multiple Branches")
print("=" * 60)

exercise_6 = """
SCENARIO:
You're working on two features simultaneously:
- subtract function
- multiply function

TASKS:
1. Create branch 'feature/subtract'
2. Add subtract function, commit
3. Switch to main, create 'feature/multiply'
4. Add multiply function, commit
5. Merge both branches into main
6. Clean up by deleting feature branches

TRY IT YOURSELF FIRST!

────────────────────────────────────────

SOLUTION:
# Feature 1: Subtract
$ git checkout -b feature/subtract
$ cat >> main.py << 'EOF'

def subtract(a, b):
    return a - b
EOF
$ git add main.py
$ git commit -m "Add subtract function"

# Switch to main, create feature 2
$ git checkout main
$ git checkout -b feature/multiply
$ cat >> main.py << 'EOF'

def multiply(a, b):
    return a * b
EOF
$ git add main.py
$ git commit -m "Add multiply function"

# Merge both into main
$ git checkout main
$ git merge feature/subtract
$ git merge feature/multiply
# Note: Second merge might cause conflict - resolve if needed

# Clean up
$ git branch -d feature/subtract
$ git branch -d feature/multiply

VERIFY:
$ cat main.py
# Should have add, subtract, and multiply functions
$ git branch
# Should only show main
"""
print(exercise_6)

# ========== EXERCISE 7 ==========
print("\n" + "=" * 60)
print("EXERCISE 7: Use Git Stash")
print("=" * 60)

exercise_7 = """
SCENARIO:
You're working on a divide function, but suddenly need to
fix a bug in the add function. Use stash to save your work.

TASKS:
1. Start working on divide function (don't commit)
2. Stash your changes
3. Fix the bug in add function
4. Commit the fix
5. Restore your stashed work
6. Complete and commit divide function

TRY IT YOURSELF FIRST!

────────────────────────────────────────

SOLUTION:
# Start divide function (incomplete)
$ cat >> main.py << 'EOF'

def divide(a, b):
    # TODO: handle division by zero
    return a / b
EOF

# Stash changes
$ git stash save "WIP: divide function"
$ git status
# Working tree should be clean now

# Fix bug in add function (pretend there's a bug)
# Edit main.py to add input validation to add()
$ git add main.py
$ git commit -m "Fix: Add input validation to add function"

# Restore stash
$ git stash pop

# Complete divide function with error handling
# Edit main.py to complete divide function
$ git add main.py
$ git commit -m "Add divide function with zero division handling"

VERIFY:
$ git stash list
# Should be empty
$ git log --oneline -3
# Should show both commits
"""
print(exercise_7)

# ========== EXERCISE 8 ==========
print("\n" + "=" * 60)
print("EXERCISE 8: View History and Changes")
print("=" * 60)

exercise_8 = """
SCENARIO:
You need to review the project's history and see what
changed in specific commits.

TASKS:
1. View compact commit history
2. View detailed log of last 3 commits
3. See what changed in a specific commit
4. View the diff between two commits
5. See who made changes to a file (blame)

TRY IT YOURSELF FIRST!

────────────────────────────────────────

SOLUTION:
# Compact history
$ git log --oneline

# Detailed last 3
$ git log -3

# What changed in specific commit
$ git show <commit-hash>
# e.g., git show abc1234

# Diff between commits
$ git diff <older-hash> <newer-hash>
# e.g., git diff abc1234 def5678

# View who changed what
$ git blame main.py

# Show graph view
$ git log --oneline --graph --all

VERIFY:
- You can see all commits
- You understand what each commit changed
"""
print(exercise_8)

# ========== BONUS CHALLENGE ==========
print("\n" + "=" * 60)
print("BONUS CHALLENGE: Complete Calculator Project")
print("=" * 60)

bonus = """
BUILD A COMPLETE CALCULATOR:

Create a fully functional calculator project using everything
you've learned today!

Requirements:
1. Initialize new repo with proper structure
2. Create .gitignore for Python
3. Add README.md with documentation
4. Create calculator.py with:
   - add, subtract, multiply, divide functions
   - Use feature branches for each function
   - Handle edge cases (division by zero)
5. Push to GitHub
6. Create at least 5 meaningful commits

Project Structure:
calculator-project/
├── .gitignore
├── README.md
├── calculator.py
└── test_calculator.py (optional)

CHALLENGE YOURSELF:
- Use branches for each feature
- Write clear commit messages
- Create a Pull Request (even to your own repo)
- Add docstrings to functions
- Handle edge cases

This exercise combines EVERYTHING from Day 9!
Good luck! 🚀
"""
print(bonus)

# ========== QUICK REFERENCE ==========
print("\n" + "=" * 60)
print("QUICK REFERENCE FOR EXERCISES")
print("=" * 60)

quick_ref = """
COMMANDS YOU'LL USE MOST:

Setup:
  git init                    Start new repo
  git clone <url>            Copy existing repo
  git config --global ...    Configure git

Daily Workflow:
  git status                 Check what's changed
  git add .                  Stage all changes
  git commit -m "msg"        Commit changes
  git push                   Upload to remote
  git pull                   Download changes

Branching:
  git branch                 List branches
  git checkout -b <name>     Create & switch branch
  git checkout <name>        Switch branch
  git merge <branch>         Merge branch
  git branch -d <name>       Delete branch

History:
  git log --oneline          Compact history
  git show <hash>            Show commit details
  git diff                   Show changes

Other:
  git stash                  Save work temporarily
  git stash pop              Restore saved work
  git remote -v              Show remotes
"""
print(quick_ref)

print("\n" + "=" * 60)
print("✅ Practical Exercises - Complete!")
print("=" * 60)
print("Ready for the Day 9 Assessment? Take day9_assessment.py!")
