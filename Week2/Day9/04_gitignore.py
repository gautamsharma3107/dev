"""
Day 9 - .gitignore Files
========================
Learn: Creating and using .gitignore to exclude files from Git

Key Concepts:
- .gitignore tells Git which files to ignore
- Prevents sensitive data and unnecessary files from being committed
- Uses pattern matching for flexibility
"""

# ========== WHAT IS .GITIGNORE? ==========
print("=" * 60)
print("WHAT IS .GITIGNORE?")
print("=" * 60)

gitignore_overview = """
.gitignore is a special file that tells Git which files to ignore.

Why use .gitignore?
✅ Exclude sensitive files (passwords, API keys)
✅ Exclude build artifacts and compiled files
✅ Exclude dependencies (node_modules, venv)
✅ Exclude system files (.DS_Store, Thumbs.db)
✅ Exclude IDE/editor files
✅ Keep repository clean and small

Where to place .gitignore:
- Root of your repository (most common)
- Can also be in subdirectories

When to create:
- Create BEFORE you start committing files
- If you already committed, files must be untracked first
"""
print(gitignore_overview)

# ========== BASIC SYNTAX ==========
print("\n" + "=" * 60)
print(".GITIGNORE SYNTAX")
print("=" * 60)

syntax = """
.gitignore Pattern Syntax:

# This is a comment
*.log           # Ignore all .log files
!important.log  # But NOT important.log (exception)
/build          # Ignore build folder in root only
build/          # Ignore all build folders anywhere
doc/*.txt       # Ignore .txt files in doc folder
**/logs         # Ignore logs folder anywhere
temp?.txt       # Ignore temp1.txt, temp2.txt, etc.

Rules:
1. Blank lines are ignored
2. Lines starting with # are comments
3. / at the beginning means root directory
4. / at the end means directory
5. ! negates a pattern (exception)
6. * matches anything except /
7. ** matches directories recursively
8. ? matches any single character
"""
print(syntax)

# ========== COMMON PATTERNS ==========
print("\n" + "=" * 60)
print("COMMON .GITIGNORE PATTERNS")
print("=" * 60)

common_patterns = """
PYTHON PROJECTS:
# Byte-compiled files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
.env/
.venv/
env/

# Distribution / packaging
dist/
build/
*.egg-info/
.eggs/

# Environment variables
.env
.env.local
*.env

# Jupyter Notebooks
.ipynb_checkpoints/

JAVASCRIPT/NODE PROJECTS:
# Dependencies
node_modules/

# Build outputs
dist/
build/
.next/

# Logs
npm-debug.log*
yarn-error.log*

# Environment
.env
.env.local
.env.production

# Cache
.cache/
.parcel-cache/

GENERAL (All Projects):
# Operating system
.DS_Store
Thumbs.db
*.swp

# IDE/Editors
.idea/
.vscode/
*.sublime-project
*.sublime-workspace
.project
.settings/

# Logs
*.log
logs/

# Temporary files
tmp/
temp/
*.tmp
*.temp

# Secrets (IMPORTANT!)
secrets/
*.pem
*.key
credentials.json
"""
print(common_patterns)

# ========== CREATING .GITIGNORE ==========
print("\n" + "=" * 60)
print("CREATING A .GITIGNORE FILE")
print("=" * 60)

creating_gitignore = """
Method 1: Create manually
$ touch .gitignore
# Then edit with your patterns

Method 2: Use GitHub template when creating repo
- Select language template when creating repo

Method 3: Use gitignore.io
- Visit gitignore.io
- Enter your tech stack (Python, Node, VSCode, etc.)
- Generate and copy the content

Method 4: Copy from existing projects
- Look at popular repos in your language
- Copy and adapt their .gitignore

Example: Creating a Python .gitignore
$ cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.so
.Python
env/
venv/
.venv/

# Environment variables
.env
.env.local

# IDE
.idea/
.vscode/
*.swp

# Testing
.pytest_cache/
.coverage
htmlcov/

# Build
dist/
build/
*.egg-info/
EOF
"""
print(creating_gitignore)

# ========== IGNORING ALREADY TRACKED FILES ==========
print("\n" + "=" * 60)
print("IGNORING ALREADY TRACKED FILES")
print("=" * 60)

already_tracked = """
Problem: You committed a file, then added it to .gitignore.
Result: Git still tracks it!

Solution: Remove from Git's tracking (but keep the file):

# Remove single file from tracking
$ git rm --cached filename.txt

# Remove directory from tracking
$ git rm -r --cached foldername/

# After removing, commit the change
$ git commit -m "Remove tracked file that should be ignored"

Example: Accidentally committed node_modules
$ git rm -r --cached node_modules
$ git commit -m "Remove node_modules from tracking"
$ git push

Now node_modules is ignored but still exists locally!

💡 Tip: Always set up .gitignore before first commit!
"""
print(already_tracked)

# ========== GLOBAL .GITIGNORE ==========
print("\n" + "=" * 60)
print("GLOBAL .GITIGNORE")
print("=" * 60)

global_gitignore = """
Global .gitignore applies to ALL your repositories.

Perfect for:
- OS-specific files (.DS_Store, Thumbs.db)
- IDE files (.idea/, .vscode/)
- Personal tools

Setup:
# Create global gitignore file
$ touch ~/.gitignore_global

# Tell Git to use it
$ git config --global core.excludesfile ~/.gitignore_global

# Edit with your patterns
$ nano ~/.gitignore_global

Recommended global patterns:

# macOS
.DS_Store
.AppleDouble
.LSOverride
._*

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini

# Linux
*~
.directory

# IDEs
.idea/
*.iml
.vscode/
*.code-workspace
*.sublime-project
*.sublime-workspace

# Vim
*.swp
*.swo
*~
"""
print(global_gitignore)

# ========== .GITIGNORE EXAMPLES ==========
print("\n" + "=" * 60)
print("COMPLETE .GITIGNORE EXAMPLES")
print("=" * 60)

examples = """
PYTHON WEB PROJECT (Django/Flask):

# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Virtual environment
venv/
.venv/
ENV/

# Environment variables
.env
.env.local
.env.*.local

# Database
*.db
*.sqlite3

# Static files (if generated)
staticfiles/

# Media uploads (often)
media/

# Logs
*.log

# IDE
.idea/
.vscode/

# Testing
.coverage
htmlcov/
.pytest_cache/

# Celery
celerybeat-schedule

-----------------------------------

NODE.JS PROJECT:

# Dependencies
node_modules/

# Build output
dist/
build/
.next/
out/

# Environment
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Cache
.cache/
.npm/
.eslintcache

# Testing
coverage/

# IDE
.idea/
.vscode/

# OS
.DS_Store
Thumbs.db
"""
print(examples)

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print(".GITIGNORE BEST PRACTICES")
print("=" * 60)

best_practices = """
.gitignore Best Practices:

1. CREATE EARLY
   - Set up .gitignore before first commit
   - Use templates for your language

2. BE SPECIFIC
   - Use specific patterns over broad ones
   - *.pyc is better than * (too broad)

3. DOCUMENT UNUSUAL ENTRIES
   - Add comments explaining non-obvious patterns
   # Ignore config file with API keys
   config.local.py

4. USE NEGATION SPARINGLY
   - ! patterns can be confusing
   - If complex, reconsider structure

5. REVIEW BEFORE COMMITTING
   $ git status
   - Check nothing sensitive is staged

6. KEEP IT ORGANIZED
   # Python
   __pycache__/
   
   # Environment
   .env
   
   # IDE
   .vscode/

7. DON'T IGNORE IMPORTANT FILES
   - Keep config templates
   - Keep .gitignore itself
   - Keep documentation

8. USE GLOBAL FOR PERSONAL FILES
   - OS files: global .gitignore
   - Project files: project .gitignore
"""
print(best_practices)

# ========== SECURITY REMINDER ==========
print("\n" + "=" * 60)
print("🚨 SECURITY: WHAT TO ALWAYS IGNORE 🚨")
print("=" * 60)

security = """
NEVER COMMIT THESE FILES:

1. Environment Files with Secrets
   .env
   .env.local
   .env.production
   *.env

2. API Keys and Credentials
   credentials.json
   service-account.json
   api_keys.py
   secrets.yaml

3. Private Keys
   *.pem
   *.key
   *.p12
   id_rsa
   id_dsa
   *.crt

4. Database Files with Real Data
   *.sql (with real data)
   *.dump

5. Configuration with Passwords
   config/local.py
   settings.local.py

What to do if you accidentally committed secrets:
1. Immediately rotate/change the secret
2. Remove from Git history (git filter-branch or BFG)
3. Force push (if allowed)
4. Consider the secret compromised even if "removed"

💡 Use environment variables instead of hardcoding secrets!
"""
print(security)

# ========== PYTHON DEMO ==========
print("\n" + "=" * 60)
print("PYTHON DEMO: WORKING WITH .GITIGNORE")
print("=" * 60)

# Here's a Python script that could generate a .gitignore
def generate_gitignore(project_type='python'):
    """Generate a .gitignore content based on project type."""
    
    common = """# Operating System
.DS_Store
Thumbs.db
*.swp
*~

# IDE
.idea/
.vscode/
*.sublime-project
*.sublime-workspace
"""
    
    templates = {
        'python': """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
.env

# Testing
.pytest_cache/
.coverage
htmlcov/

# Distribution
dist/
build/
*.egg-info/
""",
        'node': """# Node.js
node_modules/
.npm
.yarn

# Build
dist/
build/
.next/

# Environment
.env
.env.local

# Logs
npm-debug.log*
yarn-error.log*
""",
        'web': """# Web
node_modules/
dist/
.cache/
.env

# Build tools
.parcel-cache/
.sass-cache/
"""
    }
    
    return common + templates.get(project_type, templates['python'])

# Demo usage
print("Generated Python .gitignore:")
print("-" * 40)
print(generate_gitignore('python')[:500] + "...")

print("\n" + "=" * 60)
print("✅ .gitignore - Complete!")
print("=" * 60)
print("Next: Practice exercises in 05_practical_exercises.py")
