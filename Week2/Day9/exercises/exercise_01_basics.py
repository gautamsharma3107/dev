"""
Day 9 - Exercise 1: Git Basics Practice
========================================
Practice basic Git commands
"""

print("=" * 60)
print("EXERCISE 1: Git Basics Practice")
print("=" * 60)

# ============================================================
# EXERCISE 1.1: Initialize and First Commit
# ============================================================
print("""
EXERCISE 1.1: Initialize and First Commit

TASK:
Create a new project called 'hello-git' and make your first commit.

STEPS:
1. Create a folder called 'hello-git'
2. Navigate into it
3. Initialize a Git repository
4. Create a file called 'hello.py' with: print("Hello, Git!")
5. Check the status
6. Add the file to staging
7. Commit with message "Add hello.py"

COMMANDS TO USE:
- mkdir
- cd
- git init
- echo or text editor
- git status
- git add
- git commit

Try it yourself, then check the solution below!
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

$ mkdir hello-git
$ cd hello-git
$ git init
$ echo "print('Hello, Git!')" > hello.py
$ git status
$ git add hello.py
$ git commit -m "Add hello.py"

VERIFY:
$ git log --oneline
# Should show: [hash] Add hello.py
$ git status
# Should show: nothing to commit, working tree clean
""")

# ============================================================
# EXERCISE 1.2: Make Multiple Commits
# ============================================================
print("\n" + "=" * 60)
print("""
EXERCISE 1.2: Make Multiple Commits

TASK:
Add more files and make multiple commits.

STEPS:
1. Create README.md with "# Hello Git Project"
2. Commit with message "Add README"
3. Create goodbye.py with: print("Goodbye!")
4. Commit with message "Add goodbye.py"
5. View the commit history

COMMANDS TO USE:
- echo or text editor
- git add
- git commit
- git log --oneline
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

$ echo "# Hello Git Project" > README.md
$ git add README.md
$ git commit -m "Add README"

$ echo "print('Goodbye!')" > goodbye.py
$ git add goodbye.py
$ git commit -m "Add goodbye.py"

$ git log --oneline
# Should show 3 commits

VERIFY:
$ ls
# Should show: hello.py  README.md  goodbye.py
$ git log --oneline
# Should show all three commits
""")

# ============================================================
# EXERCISE 1.3: View Changes with git diff
# ============================================================
print("\n" + "=" * 60)
print("""
EXERCISE 1.3: View Changes with git diff

TASK:
Modify a file and see the changes before committing.

STEPS:
1. Edit hello.py to add a second line: print("Welcome to Git!")
2. Use git diff to see what changed
3. Stage the changes
4. Use git diff --staged to see staged changes
5. Commit with message "Add welcome message"

COMMANDS TO USE:
- Text editor or echo >>
- git diff
- git add
- git diff --staged
- git commit
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

# Add new line to hello.py
$ echo "print('Welcome to Git!')" >> hello.py

# See unstaged changes
$ git diff
# Shows the added line in green

# Stage changes
$ git add hello.py

# See staged changes
$ git diff --staged
# Shows the same change

# Commit
$ git commit -m "Add welcome message"

VERIFY:
$ cat hello.py
# Should show both print statements
$ git log --oneline
# Should show 4 commits
""")

print("\n" + "=" * 60)
print("✅ Exercise 1 Complete!")
print("=" * 60)
print("Move on to exercise_02_branching.py")
