"""
Day 9 - GitHub Workflow
=======================
Learn: Pull Requests, Code Reviews, Collaboration, GitHub Features

Key Concepts:
- GitHub is a platform for hosting Git repositories
- Pull Requests enable code review and collaboration
- Issues track bugs and feature requests
"""

# ========== WHAT IS GITHUB? ==========
print("=" * 60)
print("WHAT IS GITHUB?")
print("=" * 60)

github_overview = """
GitHub is a web-based platform for Git repository hosting.

GitHub vs Git:
- Git: Version control system (runs locally)
- GitHub: Platform to host Git repos online

Key features:
✅ Host your repositories online
✅ Collaborate with other developers
✅ Pull Requests for code review
✅ Issues for bug tracking
✅ Actions for CI/CD automation
✅ Wikis for documentation
✅ Project boards for planning

Alternatives to GitHub:
- GitLab
- Bitbucket
- Azure DevOps
"""
print(github_overview)

# ========== CREATING A REPOSITORY ON GITHUB ==========
print("\n" + "=" * 60)
print("CREATING A REPOSITORY ON GITHUB")
print("=" * 60)

creating_repo = """
Steps to create a new repository:

1. Go to github.com and log in
2. Click the '+' icon → 'New repository'
3. Fill in the details:
   - Repository name: my-awesome-project
   - Description: (optional but recommended)
   - Public or Private
   - Initialize with README: (optional)
   - Add .gitignore: (select your language)
   - Choose license: (MIT is common)
4. Click 'Create repository'

For a NEW local project:
# On GitHub: Create repo WITHOUT README

# Locally:
$ mkdir my-project
$ cd my-project
$ git init
$ git add .
$ git commit -m "Initial commit"
$ git branch -M main
$ git remote add origin https://github.com/username/my-project.git
$ git push -u origin main

For EXISTING local project:
# Same steps, just skip mkdir and git init
"""
print(creating_repo)

# ========== FORKING A REPOSITORY ==========
print("\n" + "=" * 60)
print("FORKING A REPOSITORY")
print("=" * 60)

forking = """
Forking creates a copy of someone else's repository in YOUR account.

Why fork?
✅ Contribute to open source projects
✅ Experiment without affecting original
✅ Start your own version of a project

How to fork:
1. Go to the repository you want to fork
2. Click 'Fork' button (top right)
3. Select your account
4. Done! You now have your own copy

Working with a fork:
$ git clone https://github.com/YOUR-username/forked-repo.git
$ cd forked-repo

# Add original repo as 'upstream' to get updates
$ git remote add upstream https://github.com/ORIGINAL-owner/repo.git

# Keep your fork updated
$ git fetch upstream
$ git checkout main
$ git merge upstream/main
$ git push origin main
"""
print(forking)

# ========== PULL REQUESTS (PRs) ==========
print("\n" + "=" * 60)
print("PULL REQUESTS (PRs)")
print("=" * 60)

pull_requests = """
Pull Requests are the heart of GitHub collaboration.

What is a Pull Request?
- A request to merge your changes into another branch
- Enables code review before merging
- Shows exactly what changes you made

Creating a Pull Request:
1. Push your feature branch to GitHub
   $ git push -u origin feature/my-feature

2. Go to repository on GitHub
3. Click 'Pull requests' → 'New pull request'
4. Select branches:
   - base: main (where you want to merge)
   - compare: feature/my-feature (your changes)
5. Click 'Create pull request'
6. Fill in:
   - Title: Clear, descriptive title
   - Description: What, why, how of your changes
7. Assign reviewers (if applicable)
8. Click 'Create pull request'

Good PR Description Template:
## What
Brief description of changes

## Why
Reason for the change

## How
Technical approach taken

## Testing
How you tested the changes

## Screenshots (if UI changes)
"""
print(pull_requests)

# ========== CODE REVIEW ==========
print("\n" + "=" * 60)
print("CODE REVIEW")
print("=" * 60)

code_review = """
Code review happens on Pull Requests.

As a REVIEWER:
1. Go to the Pull Request
2. Click 'Files changed' tab
3. Review each file:
   - Click + next to line numbers to comment
   - Suggest changes if needed
4. Click 'Review changes':
   - Comment: Just leave feedback
   - Approve: Changes look good
   - Request changes: Must fix before merging

Good review practices:
✅ Be constructive and helpful
✅ Explain WHY something should change
✅ Suggest alternatives when requesting changes
✅ Acknowledge good code too!
❌ Don't just say "this is wrong"
❌ Don't be condescending

As the PR AUTHOR:
1. Respond to all comments
2. Make requested changes
3. Push new commits to same branch
4. Request re-review when ready
5. Thank reviewers!
"""
print(code_review)

# ========== MERGING PULL REQUESTS ==========
print("\n" + "=" * 60)
print("MERGING PULL REQUESTS")
print("=" * 60)

merging_prs = """
Once approved, PRs can be merged.

Merge options on GitHub:

1. Create a merge commit (default)
   - Preserves all commits
   - Creates a merge commit
   - Shows full history

2. Squash and merge
   - Combines all commits into ONE
   - Cleaner history
   - Good for feature branches with many small commits

3. Rebase and merge
   - Moves commits to tip of base branch
   - Linear history
   - No merge commit

Steps to merge:
1. Ensure PR is approved
2. Ensure all checks pass (CI/CD)
3. Click 'Merge pull request'
4. Choose merge type
5. Confirm merge
6. Delete branch (optional but recommended)

After merging, locally:
$ git checkout main
$ git pull origin main
$ git branch -d feature/my-feature
"""
print(merging_prs)

# ========== GITHUB ISSUES ==========
print("\n" + "=" * 60)
print("GITHUB ISSUES")
print("=" * 60)

issues = """
Issues track bugs, features, and tasks.

Creating an Issue:
1. Go to 'Issues' tab
2. Click 'New issue'
3. Fill in title and description
4. Add labels (bug, enhancement, etc.)
5. Assign to someone (optional)
6. Add to project (optional)

Good Issue Template:
## Bug Report

**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What should happen.

**Screenshots**
If applicable.

**Environment**
- OS: [e.g., Windows 10]
- Browser: [e.g., Chrome 120]
- Version: [e.g., 1.0.0]

Linking Issues to PRs:
- In PR description: "Fixes #123" or "Closes #123"
- Issue will auto-close when PR merges
"""
print(issues)

# ========== GITHUB ACTIONS (CI/CD) ==========
print("\n" + "=" * 60)
print("GITHUB ACTIONS (CI/CD)")
print("=" * 60)

actions = """
GitHub Actions automate workflows.

Common uses:
✅ Run tests on every push
✅ Lint code automatically
✅ Deploy to production
✅ Build and publish packages

Basic workflow file (.github/workflows/test.yml):

name: Run Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: python -m pytest

This runs tests on every push and PR to main!

💡 Tip: Start simple and add more automation as needed.
"""
print(actions)

# ========== GITHUB BEST PRACTICES ==========
print("\n" + "=" * 60)
print("GITHUB BEST PRACTICES")
print("=" * 60)

best_practices = """
Repository Best Practices:

1. README.md
   - Project description
   - Installation instructions
   - Usage examples
   - Contributing guidelines

2. LICENSE
   - Choose appropriate license (MIT, Apache, GPL)
   - Protects your work legally

3. .gitignore
   - Exclude unnecessary files
   - Use templates for your language

4. Contributing Guidelines (CONTRIBUTING.md)
   - How to contribute
   - Code style requirements
   - PR process

5. Branch Protection Rules
   - Require PR reviews
   - Require status checks
   - Prevent force push to main

Collaboration Best Practices:
✅ Use descriptive branch names
✅ Write clear commit messages
✅ Create small, focused PRs
✅ Review code promptly
✅ Use labels and milestones
✅ Keep discussions in Issues/PRs
"""
print(best_practices)

# ========== COMPLETE GITHUB WORKFLOW ==========
print("\n" + "=" * 60)
print("COMPLETE GITHUB WORKFLOW")
print("=" * 60)

complete_workflow = """
Real-World Collaboration Workflow:

1. SETUP (once)
   - Fork or clone the repository
   - Set up upstream remote if forked

2. START FEATURE
   $ git checkout main
   $ git pull origin main
   $ git checkout -b feature/add-search

3. DEVELOP
   - Write code
   - Commit often with clear messages
   $ git add .
   $ git commit -m "Add search bar component"

4. PUSH TO GITHUB
   $ git push -u origin feature/add-search

5. CREATE PULL REQUEST
   - Go to GitHub
   - Create PR from feature/add-search → main
   - Write clear description
   - Request reviewers

6. CODE REVIEW
   - Address feedback
   - Push fixes to same branch
   - Discuss in PR comments

7. MERGE
   - Once approved, merge PR
   - Delete feature branch on GitHub

8. CLEANUP LOCALLY
   $ git checkout main
   $ git pull origin main
   $ git branch -d feature/add-search

9. REPEAT for next feature!
"""
print(complete_workflow)

# ========== USEFUL GITHUB FEATURES ==========
print("\n" + "=" * 60)
print("USEFUL GITHUB FEATURES")
print("=" * 60)

features = """
Additional GitHub Features:

1. GitHub Pages
   - Free hosting for static websites
   - Great for documentation or portfolios

2. Releases
   - Version your software (v1.0.0, v1.1.0)
   - Attach binaries and changelogs

3. Projects
   - Kanban-style project management
   - Integrate with Issues and PRs

4. Discussions
   - Q&A and conversations
   - Community engagement

5. Security
   - Dependabot for dependency updates
   - Code scanning for vulnerabilities
   - Secret scanning

6. Codespaces
   - Cloud-based development environments
   - Code from anywhere

Keyboard Shortcuts (on GitHub):
- ? : Show all shortcuts
- t : File finder
- w : Branch selector
- l : Jump to line
- b : Blame view
"""
print(features)

print("\n" + "=" * 60)
print("✅ GitHub Workflow - Complete!")
print("=" * 60)
print("Next: Learn about .gitignore in 04_gitignore.py")
