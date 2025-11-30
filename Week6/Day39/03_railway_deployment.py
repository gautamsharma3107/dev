"""
Day 39 - Railway Deployment
============================
Learn: Deploying Python apps to Railway

Key Concepts:
- Railway platform overview
- GitHub integration
- Environment variables
- Database provisioning
"""

# ========== WHAT IS RAILWAY? ==========
print("=" * 60)
print("WHAT IS RAILWAY?")
print("=" * 60)

print("""
Railway = Modern Platform as a Service (PaaS)

Features:
- Modern, clean UI
- Automatic deploys from GitHub
- Built-in database provisioning
- Simple environment configuration
- Generous free tier
- Docker support

Why Railway:
- Simpler than Heroku for modern apps
- Great developer experience
- Fast deployments
- Good free tier for learning
""")

# ========== RAILWAY VS HEROKU ==========
print("=" * 60)
print("RAILWAY VS HEROKU")
print("=" * 60)

print("""
┌─────────────────┬─────────────────────┬─────────────────────┐
│ Feature         │ Railway             │ Heroku              │
├─────────────────┼─────────────────────┼─────────────────────┤
│ Free Tier       │ $5/month credit     │ Eco ($5/month)      │
│ Sleep Mode      │ No                  │ Yes (Eco)           │
│ Deployment      │ GitHub push         │ Git push/GitHub     │
│ Database        │ Built-in            │ Add-on              │
│ UI              │ Modern              │ Classic             │
│ CLI             │ Available           │ Available           │
│ Dockerfile      │ Supported           │ Supported           │
│ Nixpacks        │ Yes (auto-detect)   │ Buildpacks          │
│ Learning Curve  │ Easy                │ Easy                │
└─────────────────┴─────────────────────┴─────────────────────┘
""")

# ========== RAILWAY SETUP ==========
print("=" * 60)
print("RAILWAY SETUP")
print("=" * 60)

print("""
Step 1: Create Railway Account
──────────────────────────────
1. Go to https://railway.app/
2. Click "Login" or "Start a New Project"
3. Sign up with GitHub (recommended)
4. Verify your account

Step 2: Install Railway CLI (Optional)
──────────────────────────────────────
# macOS (using Homebrew)
brew install railway

# npm (cross-platform)
npm install -g @railway/cli

# Shell script
bash <(curl -fsSL cli.new)

Step 3: Login to CLI
────────────────────
railway login

# Opens browser for authentication
""")

# ========== DEPLOYING TO RAILWAY ==========
print("=" * 60)
print("DEPLOYING TO RAILWAY")
print("=" * 60)

print("""
Method 1: GitHub Integration (Recommended)
──────────────────────────────────────────

1. Push your code to GitHub
2. Go to https://railway.app/dashboard
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway auto-detects Python and deploys!

What Railway Detects:
- requirements.txt → Python project
- package.json → Node.js project
- Dockerfile → Docker build
- Uses Nixpacks for auto-detection

Method 2: Railway CLI
─────────────────────
# In your project directory
cd my_python_app

# Login (if not already)
railway login

# Create new project
railway init

# Deploy
railway up

# Open in browser
railway open
""")

# ========== RAILWAY PROJECT STRUCTURE ==========
print("=" * 60)
print("RAILWAY PROJECT STRUCTURE")
print("=" * 60)

print("""
Basic Python Flask App for Railway:
───────────────────────────────────

my_railway_app/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .gitignore         # Ignore files
└── README.md          # Documentation

NOTE: Railway doesn't require Procfile!
      It auto-detects how to run your app.

But if needed, create railway.json or Procfile:
───────────────────────────────────────────────
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn app:app"
  }
}
""")

# ========== SAMPLE APP FOR RAILWAY ==========
print("=" * 60)
print("SAMPLE APP FOR RAILWAY")
print("=" * 60)

app_code = '''
# app.py - Flask App for Railway
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Railway!",
        "platform": "Railway",
        "status": "running"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "my-railway-app"
    })

@app.route("/api/info")
def info():
    return jsonify({
        "python_version": os.popen("python --version").read().strip(),
        "environment": os.getenv("RAILWAY_ENVIRONMENT", "development")
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
'''

print("app.py:")
print(app_code)

requirements = '''
# requirements.txt
flask==2.3.0
gunicorn==21.2.0
python-dotenv==1.0.0
'''

print("\nrequirements.txt:")
print(requirements)

gitignore = '''
# .gitignore
venv/
__pycache__/
*.pyc
.env
.DS_Store
*.log
'''

print("\n.gitignore:")
print(gitignore)

# ========== ENVIRONMENT VARIABLES ==========
print("=" * 60)
print("ENVIRONMENT VARIABLES ON RAILWAY")
print("=" * 60)

print("""
Method 1: Railway Dashboard
───────────────────────────
1. Go to your project
2. Click on your service
3. Go to "Variables" tab
4. Add key-value pairs
5. Click "Add"
6. Deploy triggers automatically

Method 2: Railway CLI
─────────────────────
# Set a variable
railway variables set SECRET_KEY=my-secret

# List all variables
railway variables

# Remove a variable
railway variables unset SECRET_KEY

Built-in Railway Variables:
───────────────────────────
RAILWAY_ENVIRONMENT   # Environment name
RAILWAY_PROJECT_ID    # Project ID
RAILWAY_SERVICE_ID    # Service ID
PORT                  # Assigned port (auto)

Using in Python:
────────────────
import os

# Get environment variables
secret = os.getenv('SECRET_KEY')
env = os.getenv('RAILWAY_ENVIRONMENT', 'production')
port = int(os.getenv('PORT', 5000))
""")

# ========== ADDING A DATABASE ==========
print("=" * 60)
print("ADDING A DATABASE ON RAILWAY")
print("=" * 60)

print("""
Step 1: Add Database Service
────────────────────────────
1. In your project, click "New"
2. Select "Database"
3. Choose: PostgreSQL, MySQL, MongoDB, or Redis
4. Click to provision

Step 2: Connect to Database
───────────────────────────
Railway automatically provides connection variables:
- DATABASE_URL (full connection string)
- PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE (PostgreSQL)
- MYSQL_URL, MYSQL_HOST, etc. (MySQL)
- MONGO_URL (MongoDB)
- REDIS_URL (Redis)

Step 3: Use in Python
─────────────────────
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get database URL from environment
database_url = os.getenv('DATABASE_URL')

# Railway uses postgresql:// which SQLAlchemy supports directly
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)

# Create tables
with app.app_context():
    db.create_all()
""")

# ========== COMPLETE DEPLOYMENT FLOW ==========
print("=" * 60)
print("COMPLETE RAILWAY DEPLOYMENT FLOW")
print("=" * 60)

print("""
Step-by-Step Deployment:
────────────────────────

1. Create and test locally
   mkdir my_railway_app
   cd my_railway_app
   python -m venv venv
   source venv/bin/activate
   pip install flask gunicorn python-dotenv
   
   # Create app.py
   # Test: python app.py
   # Visit: http://localhost:5000

2. Create requirements.txt
   pip freeze > requirements.txt

3. Initialize Git and push to GitHub
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/you/my-railway-app.git
   git push -u origin main

4. Deploy on Railway
   - Go to https://railway.app/dashboard
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Wait for deployment (usually < 2 minutes)

5. Access your app
   - Click on the deployment
   - Go to "Settings" → "Domains"
   - Click "Generate Domain"
   - Your app is live at: https://xxx.up.railway.app

6. Add environment variables (if needed)
   - Go to "Variables" tab
   - Add your secrets
   - Deployment auto-triggers
""")

# ========== RAILWAY CLI COMMANDS ==========
print("=" * 60)
print("RAILWAY CLI COMMANDS")
print("=" * 60)

print("""
Project Management:
───────────────────
railway login           # Login to Railway
railway logout          # Logout
railway init            # Initialize new project
railway link            # Link to existing project

Deployment:
───────────
railway up              # Deploy current directory
railway up --detach     # Deploy without logs
railway status          # Show deployment status

Environment:
────────────
railway variables       # List all variables
railway variables set KEY=value
railway variables unset KEY

Logs:
─────
railway logs            # Show logs
railway logs --follow   # Stream logs

Database:
─────────
railway connect postgres    # Connect to PostgreSQL
railway connect mysql       # Connect to MySQL
railway connect redis       # Connect to Redis

Other:
──────
railway open            # Open project in browser
railway run <command>   # Run command in project context
railway shell           # Open shell with env vars
""")

# ========== RAILWAY PRICING ==========
print("=" * 60)
print("RAILWAY PRICING")
print("=" * 60)

print("""
Railway Pricing (as of 2024):
─────────────────────────────

Free Tier (Hobby Plan):
- $5 credit per month
- No credit card required
- Great for learning/prototypes
- ~500 hours of compute
- Execution limit: 500 hours/month

Pro Plan ($20/month):
- $20 included usage
- No execution limits
- Team features
- Priority support

Usage-Based Pricing:
───────────────────
RAM: $0.000231/GB/minute
CPU: $0.000463/vCPU/minute
Network: $0.10/GB

Database:
PostgreSQL, MySQL: Included in usage
Redis, MongoDB: Included in usage

Typical Monthly Costs:
─────────────────────
Small Flask app: ~$5/month
Flask + PostgreSQL: ~$7-10/month
Full-stack app: ~$10-15/month
""")

# ========== COMMON ISSUES & SOLUTIONS ==========
print("=" * 60)
print("COMMON RAILWAY ISSUES")
print("=" * 60)

print("""
1. "Build Failed"
   ───────────────
   Problem: Deployment fails during build
   Solution: 
   - Check requirements.txt is correct
   - View build logs for specific errors
   - Ensure compatible Python version

2. "App Not Starting"
   ───────────────────
   Problem: Build succeeds but app doesn't start
   Solution:
   - Check that PORT is used correctly
   - Use: port = int(os.getenv('PORT', 5000))
   - Check logs for startup errors

3. "No Domains Available"
   ───────────────────────
   Problem: Can't access app
   Solution:
   - Go to Service Settings
   - Click "Generate Domain"
   - Or add custom domain

4. "Database Connection Failed"
   ────────────────────────────
   Problem: Can't connect to database
   Solution:
   - Check DATABASE_URL is set
   - Verify database service is running
   - Check connection string format

5. "Environment Variable Not Found"
   ─────────────────────────────────
   Problem: os.getenv() returns None
   Solution:
   - Variables set in dashboard after deploy
   - Re-deploy after adding variables
   - Check variable names (case-sensitive)
""")

# ========== BEST PRACTICES ==========
print("=" * 60)
print("RAILWAY BEST PRACTICES")
print("=" * 60)

print("""
1. Use environment variables for secrets
2. Enable automatic deployments from main branch
3. Use health check endpoints
4. Monitor usage to stay within free tier
5. Set up proper .gitignore
6. Use gunicorn for production
7. Add proper logging
8. Use separate environments (dev/prod)
""")

print("\n" + "=" * 60)
print("✅ Railway Deployment - Complete!")
print("=" * 60)
