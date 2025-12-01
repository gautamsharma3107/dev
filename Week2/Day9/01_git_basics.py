"""
Day 9 - Git Basics
==================
Learn: init, add, commit, push, pull - The fundamental Git commands

Key Concepts:
- Git is a distributed version control system
- Tracks changes in your code over time
- Enables collaboration with other developers
- Every Git command starts with 'git'
"""

# ========== WHAT IS GIT? ==========
print("=" * 60)
print("WHAT IS GIT?")
print("=" * 60)

git_overview = """
Git is a FREE, open-source distributed version control system.

Why use Git?
✅ Track changes in your code
✅ Revert to previous versions if something breaks
✅ Collaborate with other developers
✅ Work on multiple features simultaneously (branching)
✅ Keep a history of all changes
✅ Industry standard - used by almost every company
"""
print(git_overview)

# ========== GIT WORKFLOW OVERVIEW ==========
print("\n" + "=" * 60)
print("GIT WORKFLOW OVERVIEW")
print("=" * 60)

workflow = """
The basic Git workflow:

    Working Directory → Staging Area → Local Repository → Remote Repository
           ↓                 ↓               ↓                  ↓
      (your files)      (git add)       (git commit)       (git push)
      
1. Working Directory: Where you edit your files
2. Staging Area: Files ready to be committed
3. Local Repository: Your local Git database
4. Remote Repository: GitHub, GitLab, etc.
"""
print(workflow)

# ========== GIT INIT ==========
print("\n" + "=" * 60)
print("GIT INIT - Initialize a Repository")
print("=" * 60)

git_init = """
'git init' creates a new Git repository in your current directory.

Command:
$ git init

What happens:
- Creates a hidden .git folder
- This folder contains all Git tracking information
- Your project is now a Git repository!

Example:
$ mkdir my-project
$ cd my-project
$ git init
Initialized empty Git repository in /path/to/my-project/.git/

💡 Tip: Only run 'git init' once per project!
"""
print(git_init)

# ========== GIT STATUS ==========
print("\n" + "=" * 60)
print("GIT STATUS - Check Repository Status")
print("=" * 60)

git_status = """
'git status' shows the current state of your repository.

Command:
$ git status

What it shows:
- Which branch you're on
- Untracked files (new files Git doesn't know about)
- Modified files (changed but not staged)
- Staged files (ready to be committed)

Example output:
$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py
        README.md

💡 Tip: Use 'git status' frequently to see what's going on!
"""
print(git_status)

# ========== GIT ADD ==========
print("\n" + "=" * 60)
print("GIT ADD - Stage Changes")
print("=" * 60)

git_add = """
'git add' moves files from Working Directory to Staging Area.

Commands:
$ git add <filename>       # Add specific file
$ git add .                # Add ALL changes in current directory
$ git add -A               # Add ALL changes in entire repository
$ git add *.py             # Add all Python files
$ git add folder/          # Add entire folder

Example:
$ git add app.py
$ git add README.md
# OR add everything at once:
$ git add .

After adding:
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   app.py
        new file:   README.md

💡 Tip: Use 'git add .' for convenience, but be careful not to add unwanted files!
"""
print(git_add)

# ========== GIT COMMIT ==========
print("\n" + "=" * 60)
print("GIT COMMIT - Save Changes")
print("=" * 60)

git_commit = """
'git commit' saves staged changes to your local repository.

Commands:
$ git commit -m "Your message"         # Commit with inline message
$ git commit                           # Opens editor for message
$ git commit -am "message"             # Add + commit (only for tracked files)

Good commit message guidelines:
✅ Be specific: "Add user login functionality"
✅ Use present tense: "Add feature" not "Added feature"
✅ Keep it short: 50 characters or less for subject
❌ Avoid vague: "Fix stuff", "Update code", "Changes"

Example:
$ git commit -m "Add user authentication feature"
[main abc1234] Add user authentication feature
 2 files changed, 45 insertions(+)
 create mode 100644 auth.py
 create mode 100644 tests/test_auth.py

💡 Tip: Commit often! Small, focused commits are better than large ones.
"""
print(git_commit)

# ========== GIT LOG ==========
print("\n" + "=" * 60)
print("GIT LOG - View Commit History")
print("=" * 60)

git_log = """
'git log' shows the history of commits.

Commands:
$ git log                    # Full log with details
$ git log --oneline          # Compact one-line format
$ git log -n 5               # Show last 5 commits
$ git log --graph            # Visual branch graph
$ git log --author="Name"    # Filter by author

Example:
$ git log --oneline
abc1234 Add user authentication
def5678 Create homepage template
ghi9012 Initial commit

$ git log
commit abc1234567890abcdef (HEAD -> main)
Author: Your Name <email@example.com>
Date:   Mon Nov 30 2024 10:00:00

    Add user authentication feature

💡 Tip: Press 'q' to exit git log!
"""
print(git_log)

# ========== GIT REMOTE ==========
print("\n" + "=" * 60)
print("GIT REMOTE - Connect to GitHub")
print("=" * 60)

git_remote = """
'git remote' manages connections to remote repositories (like GitHub).

Commands:
$ git remote add origin <url>     # Add a remote repository
$ git remote -v                   # View remote URLs
$ git remote remove origin        # Remove a remote

Setting up GitHub connection:
1. Create a repository on GitHub (without README)
2. Copy the repository URL
3. Add the remote:

$ git remote add origin https://github.com/username/repo.git

Verify:
$ git remote -v
origin  https://github.com/username/repo.git (fetch)
origin  https://github.com/username/repo.git (push)

💡 Tip: 'origin' is just a name - it's the standard name for your main remote!
"""
print(git_remote)

# ========== GIT PUSH ==========
print("\n" + "=" * 60)
print("GIT PUSH - Upload to Remote")
print("=" * 60)

git_push = """
'git push' uploads your local commits to a remote repository.

Commands:
$ git push origin main              # Push to main branch
$ git push -u origin main           # Push and set upstream (first time)
$ git push                          # Push to upstream branch
$ git push --force                  # Force push (DANGEROUS!)

First time pushing:
$ git push -u origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (5/5), 500 bytes | 500.00 KiB/s, done.
To https://github.com/username/repo.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.

After -u flag is set:
$ git push                          # Will push to the same branch

💡 Tip: Always commit before pushing! Push uploads committed changes only.
"""
print(git_push)

# ========== GIT PULL ==========
print("\n" + "=" * 60)
print("GIT PULL - Download from Remote")
print("=" * 60)

git_pull = """
'git pull' downloads changes from a remote repository and merges them.

Commands:
$ git pull origin main              # Pull from main branch
$ git pull                          # Pull from upstream branch

What it does:
git pull = git fetch + git merge

Example:
$ git pull origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
From https://github.com/username/repo
   abc1234..def5678  main -> origin/main
Updating abc1234..def5678
Fast-forward
 new_file.py | 10 ++++++++++
 1 file changed, 10 insertions(+)

When to pull:
✅ Before starting new work
✅ When collaborating with others
✅ When you see "Your branch is behind..."

💡 Tip: Always pull before you push to avoid conflicts!
"""
print(git_pull)

# ========== GIT CLONE ==========
print("\n" + "=" * 60)
print("GIT CLONE - Copy a Repository")
print("=" * 60)

git_clone = """
'git clone' creates a copy of a remote repository on your computer.

Command:
$ git clone <repository-url>
$ git clone <url> <folder-name>     # Clone into specific folder

Example:
$ git clone https://github.com/username/repo.git
Cloning into 'repo'...
remote: Enumerating objects: 100, done.
remote: Total 100 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (100/100), done.

$ cd repo
$ ls
README.md  app.py  requirements.txt

What clone does:
✅ Downloads all files
✅ Downloads all commit history
✅ Sets up remote connection automatically

💡 Tip: Use clone to start working on existing projects!
"""
print(git_clone)

# ========== COMPLETE WORKFLOW EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE WORKFLOW EXAMPLE")
print("=" * 60)

complete_workflow = """
Starting a new project from scratch:

# Step 1: Create and navigate to project folder
$ mkdir my-awesome-project
$ cd my-awesome-project

# Step 2: Initialize Git
$ git init

# Step 3: Create some files
$ echo "# My Awesome Project" > README.md
$ echo "print('Hello World')" > app.py

# Step 4: Check status
$ git status

# Step 5: Stage all files
$ git add .

# Step 6: Commit
$ git commit -m "Initial commit: Add README and app.py"

# Step 7: Create repo on GitHub (do this in browser)

# Step 8: Connect to GitHub
$ git remote add origin https://github.com/username/my-awesome-project.git

# Step 9: Push to GitHub
$ git push -u origin main

🎉 Your code is now on GitHub!

Daily workflow (after initial setup):
1. git pull                    # Get latest changes
2. (make your changes)
3. git add .                   # Stage changes
4. git commit -m "message"     # Commit changes
5. git push                    # Push to GitHub
"""
print(complete_workflow)

# ========== QUICK REFERENCE ==========
print("\n" + "=" * 60)
print("QUICK REFERENCE - Essential Commands")
print("=" * 60)

quick_ref = """
COMMAND                  PURPOSE
────────────────────────────────────────────────────────────
git init                 Initialize new repository
git clone <url>          Copy existing repository
git status               Check current status
git add <file>           Stage specific file
git add .                Stage all changes
git commit -m "msg"      Commit staged changes
git push                 Upload to remote
git pull                 Download from remote
git log                  View commit history
git log --oneline        Compact commit history
git remote -v            View remote connections
git diff                 View unstaged changes
git diff --staged        View staged changes
────────────────────────────────────────────────────────────
"""
print(quick_ref)

print("\n" + "=" * 60)
print("✅ Git Basics - Complete!")
print("=" * 60)
print("Next: Learn about branching and merging in 02_branching_merging.py")
