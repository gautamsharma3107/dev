"""
DAY 9 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 9 ASSESSMENT TEST - Git Version Control")
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
Q1. What does 'git init' do?
a) Creates a copy of a remote repository
b) Initializes a new Git repository
c) Adds files to staging area
d) Commits changes to the repository

Your answer: """)

print("""
Q2. Which command stages ALL changes in the current directory?
a) git commit -a
b) git stage .
c) git add .
d) git push

Your answer: """)

print("""
Q3. What is the purpose of a .gitignore file?
a) To ignore Git commands
b) To specify files that should not be tracked by Git
c) To delete files from the repository
d) To create new branches

Your answer: """)

print("""
Q4. Which command creates a new branch AND switches to it?
a) git branch new-branch
b) git switch new-branch
c) git checkout -b new-branch
d) git merge new-branch

Your answer: """)

print("""
Q5. What is the correct order of Git operations for making changes?
a) commit → add → push
b) push → add → commit
c) add → commit → push
d) add → push → commit

Your answer: """)

print("""
Q6. What does 'git pull' do?
a) Uploads local commits to remote
b) Downloads changes from remote and merges them
c) Creates a new branch
d) Shows the commit history

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write the Git commands to:
    1. Create a new repository
    2. Add all files
    3. Make the first commit with message "Initial commit"
    
Write the commands:
""")

# Write your commands here:
# 
# 
# 


print("""
Q8. (2 points) Write the Git commands to:
    1. Create a branch called "feature/login"
    2. Switch to main branch
    3. Merge the feature/login branch into main
    4. Delete the feature/login branch

Write the commands:
""")

# Write your commands here:
# 
# 
# 
# 


print("""
Q9. (2 points) Create a basic .gitignore content for a Python project.
    Include at least 5 patterns for common Python files/folders to ignore.

Write the .gitignore content:
""")

# Write your .gitignore content here:
# 
# 
# 
# 
# 


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between 'git merge' and 'git rebase'.
     When would you use each one?

Your answer:
""")

# Write your explanation here as comments:
# 
# 
# 


# ============================================================
# TEST COMPLETE
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with the answer key below.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice the commands hands-on
- Git proficiency comes with practice!

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ - 6 points):
Q1: b) Initializes a new Git repository
Q2: c) git add .
Q3: b) To specify files that should not be tracked by Git
Q4: c) git checkout -b new-branch
Q5: c) add → commit → push
Q6: b) Downloads changes from remote and merges them

Section B (Coding - 6 points):

Q7 (2 points): 
git init
git add .
git commit -m "Initial commit"

Q8 (2 points):
git checkout -b feature/login   (or git branch feature/login; git checkout feature/login)
git checkout main
git merge feature/login
git branch -d feature/login

Q9 (2 points - any 5 valid patterns):
# Python .gitignore
__pycache__/
*.py[cod]
*.so
.env
venv/
.venv/
env/
*.egg-info/
dist/
build/
.pytest_cache/
.coverage
*.log
.idea/
.vscode/

Section C (Conceptual - 2 points):

Q10:
git merge:
- Combines two branches by creating a merge commit
- Preserves the full history of both branches
- Non-destructive - original branches remain unchanged
- Use when: working on shared branches, want to preserve history

git rebase:
- Moves commits from one branch onto another
- Creates a linear history (no merge commits)
- Rewrites commit history
- Use when: cleaning up local commits before sharing,
  keeping feature branch updated with main
- Never use on public/shared branches

Example when to use each:
- Merge: When merging a feature branch into main (standard workflow)
- Rebase: When updating your local feature branch with latest main changes

SCORING:
Section A: 6 points (1 point each)
Section B: 6 points (2 points each)
Section C: 2 points

Total: 14 points
Passing: 10 points (70%)

If you scored below 70%, review:
- Basic commands (if Q1, Q2, Q5 wrong)
- .gitignore (if Q3, Q9 wrong)
- Branching (if Q4, Q8 wrong)
- Remote operations (if Q6 wrong)
- Git workflow (if Q7 wrong)
- Advanced concepts (if Q10 wrong)
"""
