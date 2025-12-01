"""
Day 9 - Branching and Merging
=============================
Learn: Create branches, switch branches, merge branches, resolve conflicts

Key Concepts:
- Branches let you work on different features simultaneously
- main/master is the default branch
- Merging combines changes from different branches
"""

# ========== WHAT ARE BRANCHES? ==========
print("=" * 60)
print("WHAT ARE BRANCHES?")
print("=" * 60)

branches_overview = """
Branches are parallel versions of your code.

Think of it like this:
                    ┌── feature-1 branch
                   /
main ────●────●────●────●────● (main continues)
                   \\
                    └── feature-2 branch

Why use branches?
✅ Work on new features without breaking main code
✅ Multiple team members can work simultaneously
✅ Test experimental changes safely
✅ Easy to discard changes if they don't work
✅ Keep main/master branch always stable

Common branch types:
- main/master: Production-ready code
- develop: Integration branch for features
- feature/*: New features (e.g., feature/login)
- bugfix/*: Bug fixes (e.g., bugfix/login-error)
- hotfix/*: Urgent production fixes
"""
print(branches_overview)

# ========== CREATING BRANCHES ==========
print("\n" + "=" * 60)
print("CREATING BRANCHES")
print("=" * 60)

creating_branches = """
Commands for creating branches:

$ git branch                       # List all local branches
$ git branch <branch-name>         # Create new branch
$ git checkout -b <branch-name>    # Create AND switch to new branch
$ git switch -c <branch-name>      # Create AND switch (newer syntax)

Example - Create a feature branch:
$ git branch feature/login
$ git branch
* main
  feature/login

The * indicates your current branch.

💡 Tip: Use descriptive branch names!
   Good: feature/user-authentication, bugfix/payment-error
   Bad: branch1, new-stuff, my-branch
"""
print(creating_branches)

# ========== SWITCHING BRANCHES ==========
print("\n" + "=" * 60)
print("SWITCHING BRANCHES")
print("=" * 60)

switching_branches = """
Commands for switching branches:

$ git checkout <branch-name>       # Switch to existing branch
$ git switch <branch-name>         # Switch (newer syntax)
$ git checkout -                   # Switch to previous branch

Example:
$ git checkout feature/login
Switched to branch 'feature/login'

$ git branch
  main
* feature/login

# Make changes on feature branch
$ echo "def login():" > login.py
$ git add .
$ git commit -m "Add login function"

# Switch back to main
$ git checkout main
Switched to branch 'main'

💡 Tip: Commit or stash changes before switching branches!
   Uncommitted changes will follow you to the new branch.
"""
print(switching_branches)

# ========== VIEWING BRANCHES ==========
print("\n" + "=" * 60)
print("VIEWING BRANCHES")
print("=" * 60)

viewing_branches = """
Commands for viewing branches:

$ git branch                # List local branches
$ git branch -a             # List all branches (including remote)
$ git branch -r             # List remote branches only
$ git branch -v             # List branches with last commit
$ git branch --merged       # Show branches merged into current
$ git branch --no-merged    # Show unmerged branches

Example:
$ git branch -a
* main
  feature/login
  bugfix/header
  remotes/origin/main
  remotes/origin/develop

$ git branch -v
* main           abc1234 Latest commit on main
  feature/login  def5678 Add login function
  bugfix/header  ghi9012 Fix header styling
"""
print(viewing_branches)

# ========== MERGING BRANCHES ==========
print("\n" + "=" * 60)
print("MERGING BRANCHES")
print("=" * 60)

merging_branches = """
Merging combines changes from one branch into another.

Steps to merge:
1. Switch to the branch you want to merge INTO
2. Run git merge <branch-name>

Example - Merge feature into main:
$ git checkout main              # Switch to main
$ git merge feature/login        # Merge feature/login into main

Fast-forward merge (simple case):
$ git merge feature/login
Updating abc1234..def5678
Fast-forward
 login.py | 15 +++++++++++++++
 1 file changed, 15 insertions(+)

Three-way merge (when branches diverged):
$ git merge feature/login
Merge made by the 'ort' strategy.
 login.py | 15 +++++++++++++++
 1 file changed, 15 insertions(+)

💡 Tip: Always merge the latest main into your feature branch before
   creating a pull request!
"""
print(merging_branches)

# ========== MERGE CONFLICTS ==========
print("\n" + "=" * 60)
print("MERGE CONFLICTS")
print("=" * 60)

merge_conflicts = """
Conflicts happen when the same lines are changed in both branches.

When conflict occurs:
$ git merge feature/login
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.

What a conflict looks like in the file:
<<<<<<< HEAD
def greet():
    return "Hello from main"
=======
def greet():
    return "Hello from feature"
>>>>>>> feature/login

How to resolve:
1. Open the conflicted file
2. Choose which version to keep (or combine them)
3. Remove the conflict markers (<<<, ===, >>>)
4. Save the file
5. Stage and commit

After fixing:
def greet():
    return "Hello from main and feature"  # Combined version

$ git add app.py
$ git commit -m "Resolve merge conflict in app.py"

💡 Tip: Communication with your team prevents most conflicts!
"""
print(merge_conflicts)

# ========== DELETING BRANCHES ==========
print("\n" + "=" * 60)
print("DELETING BRANCHES")
print("=" * 60)

deleting_branches = """
After merging, you often want to delete the feature branch.

Commands:
$ git branch -d <branch-name>    # Delete merged branch (safe)
$ git branch -D <branch-name>    # Force delete (even if not merged)
$ git push origin --delete <branch>  # Delete remote branch

Example:
# After merging feature/login into main
$ git branch -d feature/login
Deleted branch feature/login (was def5678).

# If branch has unmerged changes
$ git branch -d unfinished-feature
error: The branch 'unfinished-feature' is not fully merged.
If you are sure you want to delete it, run 'git branch -D unfinished-feature'.

# Force delete if sure
$ git branch -D unfinished-feature
Deleted branch unfinished-feature (was abc1234).

💡 Tip: Delete branches after merging to keep your repo clean!
"""
print(deleting_branches)

# ========== REBASING (Advanced) ==========
print("\n" + "=" * 60)
print("REBASING (Advanced Concept)")
print("=" * 60)

rebasing = """
Rebase is an alternative to merge - it rewrites commit history.

Merge vs Rebase:

MERGE (preserves history):
main:    A──B──C──────M  (merge commit)
feature:    └──D──E──/

REBASE (linear history):
main:    A──B──C──D'──E'  (commits moved to end)

Basic rebase:
$ git checkout feature/login
$ git rebase main
# Now feature/login is based on latest main

⚠️ IMPORTANT RULES:
1. Never rebase public/shared branches
2. Only rebase your own feature branches
3. If in doubt, use merge instead

When to use rebase:
✅ Updating your feature branch with latest main
✅ Cleaning up local commits before pushing
❌ Never on main branch
❌ Never on branches others are working on

💡 For beginners: Stick with merge until you're comfortable with Git!
"""
print(rebasing)

# ========== GIT STASH ==========
print("\n" + "=" * 60)
print("GIT STASH - Save Work Temporarily")
print("=" * 60)

git_stash = """
Stash temporarily saves your uncommitted changes.

Use case: Need to switch branches but not ready to commit.

Commands:
$ git stash                    # Stash changes
$ git stash list               # List all stashes
$ git stash pop                # Apply latest stash and remove it
$ git stash apply              # Apply latest stash but keep it
$ git stash drop               # Delete latest stash
$ git stash clear              # Delete all stashes

Example workflow:
# Working on feature, but need to fix bug on main
$ git stash
Saved working directory and index state WIP on feature: abc1234 message

$ git checkout main
$ # fix the bug
$ git commit -m "Fix critical bug"

$ git checkout feature
$ git stash pop
# Your changes are back!

💡 Tip: Use stash messages for clarity:
   $ git stash save "work in progress on login form"
"""
print(git_stash)

# ========== COMPLETE BRANCHING WORKFLOW ==========
print("\n" + "=" * 60)
print("COMPLETE BRANCHING WORKFLOW")
print("=" * 60)

workflow = """
Feature Development Workflow:

# 1. Start from updated main
$ git checkout main
$ git pull origin main

# 2. Create feature branch
$ git checkout -b feature/user-profile

# 3. Make changes and commit often
$ # code, code, code...
$ git add .
$ git commit -m "Add profile page template"
$ # more coding...
$ git add .
$ git commit -m "Add profile update API"

# 4. Keep branch updated with main (optional but recommended)
$ git checkout main
$ git pull origin main
$ git checkout feature/user-profile
$ git merge main
# Resolve any conflicts if needed

# 5. Push feature branch to GitHub
$ git push -u origin feature/user-profile

# 6. Create Pull Request on GitHub (next lesson)

# 7. After PR is approved and merged, clean up
$ git checkout main
$ git pull origin main
$ git branch -d feature/user-profile
"""
print(workflow)

# ========== QUICK REFERENCE ==========
print("\n" + "=" * 60)
print("QUICK REFERENCE - Branch Commands")
print("=" * 60)

quick_ref = """
COMMAND                             PURPOSE
────────────────────────────────────────────────────────────
git branch                          List local branches
git branch -a                       List all branches
git branch <name>                   Create new branch
git checkout <name>                 Switch to branch
git checkout -b <name>              Create + switch to branch
git switch <name>                   Switch (newer syntax)
git switch -c <name>                Create + switch (newer)
git merge <branch>                  Merge branch into current
git branch -d <name>                Delete merged branch
git branch -D <name>                Force delete branch
git stash                           Stash changes
git stash pop                       Apply stashed changes
git rebase <branch>                 Rebase onto branch
────────────────────────────────────────────────────────────
"""
print(quick_ref)

print("\n" + "=" * 60)
print("✅ Branching and Merging - Complete!")
print("=" * 60)
print("Next: Learn about GitHub workflow in 03_github_workflow.py")
