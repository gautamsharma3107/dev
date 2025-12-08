"""
Day 39 - Heroku Deployment
==========================
Learn: Deploying Python apps to Heroku

Key Concepts:
- Heroku account setup
- Heroku CLI installation
- App creation and deployment
- Scaling and management
"""

# ========== WHAT IS HEROKU? ==========
print("=" * 60)
print("WHAT IS HEROKU?")
print("=" * 60)

print("""
Heroku = Platform as a Service (PaaS)

Features:
- Simple git-based deployment
- Automatic scaling
- Add-ons marketplace (databases, caching, etc.)
- Free tier available (with limitations)
- Supports Python, Node.js, Ruby, Java, Go, and more

Why Heroku for Beginners:
- No server management required
- Deploy with 'git push'
- Easy environment configuration
- Great documentation
""")

# ========== HEROKU SETUP ==========
print("=" * 60)
print("HEROKU SETUP")
print("=" * 60)

print("""
Step 1: Create Heroku Account
─────────────────────────────
1. Go to https://signup.heroku.com/
2. Create free account
3. Verify email address

Step 2: Install Heroku CLI
──────────────────────────
# macOS (using Homebrew)
brew tap heroku/brew && brew install heroku

# Ubuntu/Debian
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Windows (download installer)
https://devcenter.heroku.com/articles/heroku-cli

Step 3: Login to Heroku CLI
───────────────────────────
heroku login

# This opens a browser for authentication
# Or use: heroku login -i (for terminal-based login)
""")

# ========== PREPARING YOUR APP ==========
print("=" * 60)
print("PREPARING YOUR APP FOR HEROKU")
print("=" * 60)

print("""
Required Files:
───────────────

1. requirements.txt
   ─────────────────
   pip freeze > requirements.txt
   
   Or create manually:
   flask==2.3.0
   gunicorn==21.2.0
   python-dotenv==1.0.0

2. Procfile (NO extension!)
   ────────────────────────
   web: gunicorn app:app
   
   Format: <process type>: <command>
   - 'web' is for HTTP traffic
   - 'gunicorn app:app' means:
     - Use gunicorn web server
     - 'app' is the Python file (app.py)
     - ':app' is the Flask application instance

3. runtime.txt (optional)
   ───────────────────────
   python-3.10.12
   
   Specifies exact Python version
   Check supported versions: 
   https://devcenter.heroku.com/articles/python-support
""")

# ========== CREATING A HEROKU APP ==========
print("=" * 60)
print("CREATING A HEROKU APP")
print("=" * 60)

print("""
Method 1: Using Heroku CLI
──────────────────────────

# Navigate to your project
cd my_flask_app

# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit"

# Create Heroku app
heroku create my-app-name

# This creates:
# - A new Heroku app
# - A git remote named 'heroku'

# If name is taken, use:
heroku create  # (generates random name)

Method 2: Using Heroku Dashboard
────────────────────────────────
1. Go to https://dashboard.heroku.com/
2. Click "New" → "Create new app"
3. Enter app name
4. Choose region
5. Click "Create app"
""")

# ========== DEPLOYING TO HEROKU ==========
print("=" * 60)
print("DEPLOYING TO HEROKU")
print("=" * 60)

print("""
Method 1: Git Push (Most Common)
────────────────────────────────

# Make sure you have Heroku remote
git remote -v
# Should show: heroku  https://git.heroku.com/my-app-name.git

# Deploy!
git push heroku main

# Or if your branch is 'master'
git push heroku master

# What happens:
# 1. Heroku receives your code
# 2. Detects Python (by requirements.txt)
# 3. Installs dependencies
# 4. Runs your Procfile command
# 5. App is live!

Method 2: GitHub Integration
────────────────────────────
1. Go to Heroku Dashboard
2. Select your app
3. Go to "Deploy" tab
4. Connect to GitHub
5. Select repository
6. Enable "Automatic Deploys" (optional)
7. Click "Deploy Branch"
""")

# ========== SAMPLE DEPLOYMENT FLOW ==========
print("=" * 60)
print("COMPLETE DEPLOYMENT FLOW")
print("=" * 60)

print("""
# Step-by-step Heroku deployment

# 1. Create project structure
mkdir my_heroku_app
cd my_heroku_app

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate  # Windows

# 3. Install dependencies
pip install flask gunicorn python-dotenv

# 4. Create app.py
cat > app.py << 'EOF'
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Heroku!",
        "version": "1.0.0"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
EOF

# 5. Create requirements.txt
pip freeze > requirements.txt

# 6. Create Procfile
echo "web: gunicorn app:app" > Procfile

# 7. Create .gitignore
cat > .gitignore << 'EOF'
venv/
__pycache__/
*.pyc
.env
.DS_Store
EOF

# 8. Initialize git and commit
git init
git add .
git commit -m "Initial commit"

# 9. Create Heroku app and deploy
heroku login
heroku create my-unique-app-name
git push heroku main

# 10. Open your app!
heroku open
""")

# ========== HEROKU COMMANDS ==========
print("=" * 60)
print("ESSENTIAL HEROKU CLI COMMANDS")
print("=" * 60)

print("""
App Management:
───────────────
heroku create <name>      # Create new app
heroku apps               # List all apps
heroku apps:info          # Show app info
heroku apps:destroy       # Delete app
heroku open               # Open app in browser

Deployment:
───────────
git push heroku main      # Deploy
heroku releases           # List releases
heroku rollback           # Roll back to previous

Logs:
─────
heroku logs               # Show recent logs
heroku logs --tail        # Stream logs in real-time
heroku logs -n 100        # Show last 100 lines

Scaling:
────────
heroku ps                 # Show dyno status
heroku ps:scale web=1     # Scale to 1 dyno
heroku ps:restart         # Restart all dynos

Environment Variables:
──────────────────────
heroku config             # List all config vars
heroku config:set KEY=val # Set a config var
heroku config:get KEY     # Get a config var
heroku config:unset KEY   # Remove a config var

Database (PostgreSQL):
──────────────────────
heroku addons:create heroku-postgresql:mini
heroku pg:info            # Database info
heroku pg:psql            # Connect to database

Running Commands:
─────────────────
heroku run bash           # Open bash shell
heroku run python         # Run Python REPL
heroku run python manage.py migrate  # Django migrations
""")

# ========== ENVIRONMENT VARIABLES ==========
print("=" * 60)
print("ENVIRONMENT VARIABLES ON HEROKU")
print("=" * 60)

print("""
Setting Config Vars:
────────────────────

# Via CLI
heroku config:set SECRET_KEY=my-secret-key
heroku config:set DEBUG=False
heroku config:set DATABASE_URL=postgres://...

# Via Dashboard
1. Go to app Settings
2. Click "Reveal Config Vars"
3. Add key-value pairs

Accessing in Python:
────────────────────
import os

secret_key = os.environ.get('SECRET_KEY')
debug = os.environ.get('DEBUG', 'False') == 'True'
database_url = os.environ.get('DATABASE_URL')

# With python-dotenv for local development
from dotenv import load_dotenv
load_dotenv()  # Loads from .env file locally
""")

# ========== HEROKU POSTGRES ==========
print("=" * 60)
print("ADDING POSTGRESQL DATABASE")
print("=" * 60)

print("""
Step 1: Add Database Add-on
───────────────────────────
heroku addons:create heroku-postgresql:mini

# This automatically sets DATABASE_URL config var

Step 2: Use in Python
─────────────────────
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# Fix for Heroku's postgres:// vs postgresql://
uri = os.environ.get('DATABASE_URL')
if uri.startswith('postgres://'):
    uri = uri.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)

Step 3: Run Migrations
──────────────────────
heroku run python
>>> from app import db
>>> db.create_all()
>>> exit()

# Or for Django:
heroku run python manage.py migrate
""")

# ========== COMMON ISSUES & SOLUTIONS ==========
print("=" * 60)
print("COMMON ISSUES & SOLUTIONS")
print("=" * 60)

print("""
1. "No web processes running"
   ───────────────────────────
   Problem: App deployed but not accessible
   Solution: Check Procfile exists and is correct
             heroku ps:scale web=1

2. "Application Error"
   ────────────────────
   Problem: App crashes on startup
   Solution: Check logs: heroku logs --tail
             Common causes:
             - Missing dependencies in requirements.txt
             - Wrong PORT usage
             - Import errors

3. "Push rejected"
   ────────────────
   Problem: Git push fails
   Solution: 
   - Ensure Heroku remote exists: git remote -v
   - Add remote: heroku git:remote -a your-app-name
   - Check you're pushing correct branch

4. "ModuleNotFoundError"
   ──────────────────────
   Problem: Missing Python package
   Solution: Add package to requirements.txt
             Re-deploy

5. "Web process failed to bind to $PORT"
   ──────────────────────────────────────
   Problem: App not using Heroku's PORT
   Solution: 
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port)
""")

# ========== HEROKU PRICING ==========
print("=" * 60)
print("HEROKU PRICING")
print("=" * 60)

print("""
Dyno Types (as of 2024):
────────────────────────

Eco ($5/month shared pool):
- 1000 dyno hours/month shared
- Sleeps after 30 min inactive
- Good for small projects

Basic ($7/month per dyno):
- Always on
- No sleep
- 512 MB RAM

Standard-1X ($25/month):
- 512 MB RAM
- Horizontal scaling
- Better for production

Standard-2X ($50/month):
- 1 GB RAM
- Better performance

Performance ($250-500/month):
- Dedicated resources
- Enterprise features

Database (PostgreSQL):
──────────────────────
Mini: Free (10K rows)
Basic: $9/month
Standard: $50+/month
""")

print("\n" + "=" * 60)
print("✅ Heroku Deployment - Complete!")
print("=" * 60)
