# Day 9 Quick Reference Cheat Sheet - Git Version Control

## Git Configuration
```bash
# Set username and email (first time setup)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# View configuration
git config --list

# Set default editor
git config --global core.editor "code --wait"
```

## Repository Setup
```bash
# Initialize new repository
git init

# Clone existing repository
git clone <url>
git clone <url> <folder-name>
```

## Basic Commands
```bash
# Check status
git status

# Stage files
git add <file>           # Single file
git add .                # All changes
git add -A               # All changes in repo
git add *.py             # Pattern matching

# Commit changes
git commit -m "message"
git commit -am "message"  # Add + commit (tracked files)

# View history
git log                  # Full log
git log --oneline        # Compact
git log -n 5             # Last 5 commits
git log --graph          # Visual graph
```

## Remote Operations
```bash
# Add remote
git remote add origin <url>

# View remotes
git remote -v

# Push to remote
git push -u origin main   # First time (set upstream)
git push                  # After upstream is set

# Pull from remote
git pull origin main
git pull

# Fetch (download without merge)
git fetch origin
```

## Branching
```bash
# List branches
git branch               # Local only
git branch -a            # All (including remote)
git branch -r            # Remote only

# Create branch
git branch <name>
git checkout -b <name>   # Create + switch
git switch -c <name>     # Create + switch (new syntax)

# Switch branch
git checkout <name>
git switch <name>        # New syntax
git checkout -           # Previous branch

# Delete branch
git branch -d <name>     # Safe delete (merged only)
git branch -D <name>     # Force delete
```

## Merging
```bash
# Merge branch into current branch
git merge <branch-name>

# Abort merge (if conflicts)
git merge --abort

# After resolving conflicts
git add <resolved-files>
git commit -m "Resolve merge conflict"
```

## Stashing
```bash
# Stash current changes
git stash
git stash save "message"

# List stashes
git stash list

# Apply stash
git stash pop            # Apply and remove
git stash apply          # Apply and keep

# Delete stash
git stash drop
git stash clear          # Clear all
```

## Viewing Changes
```bash
# View unstaged changes
git diff

# View staged changes
git diff --staged

# View specific commit
git show <commit-hash>

# View file at specific commit
git show <hash>:<file>

# See who changed what
git blame <file>
```

## Undoing Changes
```bash
# Unstage file
git restore --staged <file>
git reset HEAD <file>    # Old syntax

# Discard local changes
git restore <file>
git checkout -- <file>   # Old syntax

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert commit (creates new commit)
git revert <commit-hash>
```

## .gitignore Patterns
```bash
# Common patterns
*.log                    # All .log files
!important.log           # Exception (track this file)
/build                   # build folder in root only
build/                   # All build folders
**/logs                  # logs folder anywhere
*.py[cod]                # .pyc, .pyo, .pyd files
__pycache__/             # Python cache
node_modules/            # Node dependencies
.env                     # Environment file
.vscode/                 # VS Code settings
```

## Commit Message Best Practices
```bash
# Good commit messages
git commit -m "Add user authentication feature"
git commit -m "Fix login button not responding"
git commit -m "Update README with installation steps"

# Bad commit messages
git commit -m "fix"
git commit -m "changes"
git commit -m "asdfgh"
```

## Complete Workflow Example
```bash
# Starting a new feature
git checkout main
git pull origin main
git checkout -b feature/new-feature

# Working on feature
# ... make changes ...
git add .
git commit -m "Add new feature"

# Push to remote
git push -u origin feature/new-feature

# After PR is merged
git checkout main
git pull origin main
git branch -d feature/new-feature
```

## GitHub Workflow
```bash
# Fork workflow (contributing to others' repos)
git clone <your-fork-url>
git remote add upstream <original-repo-url>

# Keep fork updated
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## Useful Aliases
```bash
# Add to git config
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"

# Usage
git st           # Instead of git status
git co main      # Instead of git checkout main
```

## Emergency Commands
```bash
# Recover deleted branch
git reflog
git checkout -b <branch-name> <hash>

# Fix last commit message
git commit --amend -m "New message"

# Remove file from all history (DANGEROUS)
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch <file>' HEAD
```

## Quick Tips
- Always `git pull` before starting work
- Commit often with meaningful messages
- Use branches for new features
- Never commit sensitive data
- Use `.gitignore` from the start
- Review changes before committing: `git diff`

---
**Keep this handy for quick reference!** 🚀
