"""
Day 9 - Exercise 3: Remote Repository Practice
================================================
Practice working with GitHub/remote repositories
"""

print("=" * 60)
print("EXERCISE 3: Remote Repository Practice")
print("=" * 60)

# ============================================================
# EXERCISE 3.1: Connect to GitHub
# ============================================================
print("""
EXERCISE 3.1: Connect to GitHub

TASK:
Push your local repository to GitHub.

PREREQUISITES:
- GitHub account
- Repository created on GitHub (empty - no README)

STEPS:
1. Create a new repository on GitHub called 'hello-git'
   (Do NOT initialize with README)
2. Add the remote origin
3. Verify remote is added
4. Push to GitHub
5. Check GitHub to see your code

COMMANDS TO USE:
- git remote add
- git remote -v
- git branch -M main
- git push -u origin main
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

# Add remote (replace USERNAME with your GitHub username)
$ git remote add origin https://github.com/USERNAME/hello-git.git

# Verify
$ git remote -v
# origin  https://github.com/USERNAME/hello-git.git (fetch)
# origin  https://github.com/USERNAME/hello-git.git (push)

# Ensure branch is named 'main'
$ git branch -M main

# Push to GitHub
$ git push -u origin main
# Enter GitHub credentials if prompted

VERIFY:
- Go to https://github.com/USERNAME/hello-git
- You should see all your files!
""")

# ============================================================
# EXERCISE 3.2: Pull Changes
# ============================================================
print("\n" + "=" * 60)
print("""
EXERCISE 3.2: Pull Changes from Remote

TASK:
Simulate pulling changes from GitHub.

STEPS:
1. Go to GitHub and edit README.md directly
   (Add: "This is a practice repository for Git!")
2. Commit the change on GitHub
3. Locally, check if you're behind
4. Pull the changes
5. Verify the README was updated locally

COMMANDS TO USE:
- git fetch
- git status
- git pull
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

# ON GITHUB:
# 1. Click on README.md
# 2. Click pencil icon to edit
# 3. Add new line: "This is a practice repository for Git!"
# 4. Commit changes (at bottom of page)

# LOCALLY:

# Check if there are remote changes
$ git fetch origin

# Check status
$ git status
# Your branch is behind 'origin/main' by 1 commit

# Pull the changes
$ git pull origin main

# Verify
$ cat README.md
# Shows the new line you added on GitHub

VERIFY:
$ git log --oneline -3
# Should show the commit from GitHub
""")

# ============================================================
# EXERCISE 3.3: Clone a Repository
# ============================================================
print("\n" + "=" * 60)
print("""
EXERCISE 3.3: Clone a Repository

TASK:
Clone an existing repository from GitHub.

STEPS:
1. Find a public repository to clone (or use your own)
2. Clone it to a new folder
3. Explore the cloned repository
4. View its remotes
5. View its commit history

COMMANDS TO USE:
- git clone
- cd
- ls
- git remote -v
- git log --oneline
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

# Clone a repository (example using a public repo)
$ git clone https://github.com/octocat/Hello-World.git

# Navigate into it
$ cd Hello-World

# See files
$ ls

# Check remote
$ git remote -v
# Shows origin pointing to the GitHub URL

# View history
$ git log --oneline

# View branches
$ git branch -a

VERIFY:
$ ls -la
# Should show .git folder and repository files
$ git remote -v
# Should show origin URL
""")

# ============================================================
# EXERCISE 3.4: Push a Feature Branch
# ============================================================
print("\n" + "=" * 60)
print("""
EXERCISE 3.4: Push a Feature Branch to GitHub

TASK:
Create a feature branch and push it to GitHub.

STEPS:
1. Go back to your hello-git repository
2. Create a new branch 'feature/awesome'
3. Add a file awesome.py
4. Commit
5. Push the feature branch to GitHub
6. Check GitHub - you should see the new branch!

COMMANDS TO USE:
- cd
- git checkout -b
- git add
- git commit
- git push -u origin <branch>
""")

input("Press Enter to see the solution...")

print("""
SOLUTION:

# Go to your repo
$ cd ~/hello-git

# Create feature branch
$ git checkout -b feature/awesome
$ echo "print('This is awesome!')" > awesome.py
$ git add awesome.py
$ git commit -m "Add awesome feature"

# Push feature branch
$ git push -u origin feature/awesome

# Now on GitHub:
# - Click "branches" dropdown
# - You'll see feature/awesome listed!
# - You can create a Pull Request

VERIFY:
- Go to GitHub
- Check branches dropdown
- feature/awesome should be visible
""")

print("\n" + "=" * 60)
print("✅ Exercise 3 Complete!")
print("=" * 60)
print("You've practiced working with remote repositories!")
