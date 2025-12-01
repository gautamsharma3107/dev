"""
DAY 9 ASSESSMENT - ANSWER KEY
==============================
For instructor use only.
Review this file AFTER completing the assessment test.
"""

print("=" * 60)
print("DAY 9 ASSESSMENT - ANSWER KEY")
print("=" * 60)
print("⚠️  WARNING: Review this ONLY after completing the assessment!")
print("=" * 60)

# ============================================================
# SECTION A ANSWERS: Multiple Choice (6 points)
# ============================================================

print("""
SECTION A ANSWERS (MCQ - 6 points):
───────────────────────────────────

Q1: b) Initializes a new Git repository
    Explanation: 'git init' creates a new .git folder and 
    initializes version control in the current directory.

Q2: c) git add .
    Explanation: The dot (.) means "all changes in current 
    directory". git commit -a only works for tracked files.

Q3: b) To specify files that should not be tracked by Git
    Explanation: .gitignore contains patterns for files Git 
    should ignore (not track or commit).

Q4: c) git checkout -b new-branch
    Explanation: The -b flag creates a new branch AND 
    switches to it in one command.

Q5: c) add → commit → push
    Explanation: First stage changes (add), then save locally 
    (commit), then upload to remote (push).

Q6: b) Downloads changes from remote and merges them
    Explanation: git pull = git fetch + git merge. It gets 
    remote changes and integrates them.
""")

# ============================================================
# SECTION B ANSWERS: Coding Challenges (6 points)
# ============================================================

print("""
SECTION B ANSWERS (Coding - 6 points):
──────────────────────────────────────

Q7 (2 points) - Initialize repository:
    git init
    git add .
    git commit -m "Initial commit"
    
    Alternative: git add -A (adds all, including deletions)

Q8 (2 points) - Branch operations:
    git checkout -b feature/login    # Create and switch
    git checkout main                # Switch to main
    git merge feature/login          # Merge feature into main
    git branch -d feature/login      # Delete merged branch
    
    Alternative for step 1:
    git branch feature/login
    git checkout feature/login

Q9 (2 points) - Python .gitignore:
    Any 5 of these patterns are correct:
    
    __pycache__/
    *.py[cod]
    *.pyo
    *.pyc
    *.so
    .env
    .env.local
    venv/
    .venv/
    env/
    ENV/
    *.egg-info/
    dist/
    build/
    .pytest_cache/
    .coverage
    htmlcov/
    *.log
    .idea/
    .vscode/
""")

# ============================================================
# SECTION C ANSWERS: Conceptual Question (2 points)
# ============================================================

print("""
SECTION C ANSWER (Conceptual - 2 points):
─────────────────────────────────────────

Q10: Difference between git merge and git rebase

MERGE:
• Combines two branches by creating a merge commit
• Preserves the full history of both branches
• Non-destructive - original branches remain unchanged
• Creates a "merge commit" that has two parents
• History shows all commits from both branches

REBASE:
• Moves commits from one branch onto another
• Creates a linear history (no merge commits)
• Rewrites commit history (new commit hashes)
• Makes the commit history cleaner

WHEN TO USE:

Use MERGE when:
• Working on shared/public branches
• You want to preserve complete history
• Merging a feature branch into main (standard workflow)
• Team collaboration where history matters

Use REBASE when:
• Cleaning up local commits before sharing
• Keeping feature branch updated with main
• You want a linear, clean history
• Working alone on a feature branch

⚠️ IMPORTANT:
Never rebase commits that have been pushed to a shared remote!
This rewrites history and causes problems for collaborators.
""")

# ============================================================
# SCORING GUIDE
# ============================================================

print("""
════════════════════════════════════════════════════════════
SCORING GUIDE
════════════════════════════════════════════════════════════

Section A: 6 points (1 point each question)
Section B: 6 points (2 points each question)
Section C: 2 points

TOTAL POSSIBLE: 14 points
PASSING SCORE: 10 points (70%)

PARTIAL CREDIT (Section B & C):
• Full understanding + correct syntax: Full points
• Minor syntax errors but correct concept: 1.5 points
• Partial understanding: 1 point
• Incorrect: 0 points

════════════════════════════════════════════════════════════
REVIEW RECOMMENDATIONS
════════════════════════════════════════════════════════════

If student struggles with:

Q1-Q2: Review 01_git_basics.py (init, add, status)
Q3, Q9: Review 04_gitignore.py (.gitignore patterns)
Q4, Q8: Review 02_branching_merging.py (branches)
Q5, Q7: Review 01_git_basics.py (workflow)
Q6:     Review 01_git_basics.py (push/pull)
Q10:    Review 02_branching_merging.py (merge vs rebase)

Practice exercises are in the exercises/ folder.
""")

print("=" * 60)
print("End of Answer Key")
print("=" * 60)
