"""
Day 39 - Cloud Platforms Overview
==================================
Learn: Understanding cloud computing and major platforms

Key Concepts:
- What is cloud computing?
- Types of cloud services (IaaS, PaaS, SaaS)
- Major cloud providers comparison
- Developer-friendly deployment platforms
"""

# ========== WHAT IS CLOUD COMPUTING? ==========
print("=" * 60)
print("WHAT IS CLOUD COMPUTING?")
print("=" * 60)

print("""
Cloud Computing = Delivery of computing services over the internet

Instead of:
  - Buying your own servers
  - Managing data centers
  - Handling hardware maintenance

You get:
  - On-demand resources
  - Pay-as-you-go pricing
  - Scalability
  - Global availability
""")

# ========== TYPES OF CLOUD SERVICES ==========
print("=" * 60)
print("TYPES OF CLOUD SERVICES")
print("=" * 60)

print("""
┌─────────────────────────────────────────────────────────────┐
│                    Cloud Service Models                      │
├─────────────────┬──────────────────┬─────────────────────────┤
│      IaaS       │       PaaS       │          SaaS           │
│ Infrastructure  │     Platform     │        Software         │
│   as a Service  │   as a Service   │      as a Service       │
├─────────────────┼──────────────────┼─────────────────────────┤
│ You manage:     │ You manage:      │ You manage:             │
│ - Applications  │ - Applications   │ - Nothing (just use it) │
│ - Data          │ - Data           │                         │
│ - Runtime       │                  │                         │
│ - Middleware    │                  │                         │
│ - OS            │                  │                         │
├─────────────────┼──────────────────┼─────────────────────────┤
│ Provider:       │ Provider:        │ Provider:               │
│ - Virtualization│ - Runtime        │ - Everything            │
│ - Servers       │ - OS             │                         │
│ - Storage       │ - Virtualization │                         │
│ - Networking    │ - Servers        │                         │
│                 │ - Storage        │                         │
├─────────────────┼──────────────────┼─────────────────────────┤
│ Examples:       │ Examples:        │ Examples:               │
│ - AWS EC2       │ - Heroku         │ - Gmail                 │
│ - Azure VMs     │ - Railway        │ - Salesforce            │
│ - GCP Compute   │ - Render         │ - Dropbox               │
│                 │ - Google App Eng │ - Slack                 │
└─────────────────┴──────────────────┴─────────────────────────┘
""")

# ========== MAJOR CLOUD PROVIDERS ==========
print("=" * 60)
print("MAJOR CLOUD PROVIDERS")
print("=" * 60)

print("""
1. AMAZON WEB SERVICES (AWS)
   ──────────────────────────
   ✅ Largest market share (~32%)
   ✅ Most services (200+)
   ✅ Mature and reliable
   ❌ Complex pricing
   ❌ Steep learning curve
   
   Key Services:
   - EC2 (Virtual Servers)
   - S3 (Object Storage)
   - Lambda (Serverless)
   - RDS (Managed Database)
   - ECS/EKS (Containers)

2. GOOGLE CLOUD PLATFORM (GCP)
   ───────────────────────────
   ✅ Best for data/ML
   ✅ Strong Kubernetes support
   ✅ Competitive pricing
   ❌ Smaller service catalog
   ❌ Less enterprise adoption
   
   Key Services:
   - Compute Engine (VMs)
   - Cloud Storage
   - Cloud Functions
   - BigQuery (Analytics)
   - Kubernetes Engine

3. MICROSOFT AZURE
   ────────────────
   ✅ Best for enterprises
   ✅ Great .NET integration
   ✅ Hybrid cloud leader
   ❌ Complex portal
   ❌ Inconsistent UX
   
   Key Services:
   - Virtual Machines
   - Blob Storage
   - Azure Functions
   - Azure SQL
   - AKS (Kubernetes)
""")

# ========== DEVELOPER-FRIENDLY PLATFORMS ==========
print("=" * 60)
print("DEVELOPER-FRIENDLY PLATFORMS (PaaS)")
print("=" * 60)

print("""
For beginners and small projects, use PaaS platforms:

1. HEROKU
   ───────
   ✅ Simple deployment (git push)
   ✅ Good free tier (limited)
   ✅ Easy scaling
   ✅ Great for prototypes
   ❌ Can get expensive at scale
   ❌ Free tier has sleep mode
   
   Best for: Quick deployments, prototypes, learning

2. RAILWAY
   ────────
   ✅ Modern UI/UX
   ✅ Simple setup
   ✅ GitHub integration
   ✅ Free tier available
   ✅ Database provisioning
   ❌ Relatively new
   
   Best for: Modern projects, full-stack apps

3. RENDER
   ───────
   ✅ Free tier for static sites
   ✅ Auto-deploy from Git
   ✅ Built-in SSL
   ✅ Background workers
   ❌ Limited free compute
   
   Best for: Static sites, web services

4. VERCEL
   ───────
   ✅ Best for frontend/Next.js
   ✅ Excellent DX
   ✅ Edge functions
   ✅ Generous free tier
   ❌ Backend limitations
   
   Best for: Frontend, JAMstack, serverless

5. FLY.IO
   ───────
   ✅ Edge deployment
   ✅ Docker-based
   ✅ Good free tier
   ✅ Distributed apps
   ❌ Learning curve
   
   Best for: Global apps, Docker deployments
""")

# ========== CHOOSING A PLATFORM ==========
print("=" * 60)
print("CHOOSING A PLATFORM")
print("=" * 60)

print("""
Decision Framework:

┌─────────────────────────────────────────────────────────────┐
│           What Are You Building?                            │
├─────────────────────────────────────────────────────────────┤
│ Learning/Prototype    → Heroku, Railway, Render             │
│ Frontend/Static       → Vercel, Netlify, GitHub Pages       │
│ Full-Stack App        → Railway, Render, Heroku             │
│ ML/AI Project         → AWS SageMaker, GCP AI, Railway      │
│ Enterprise App        → AWS, Azure, GCP                     │
│ Global/Edge App       → Fly.io, Cloudflare Workers          │
└─────────────────────────────────────────────────────────────┘

For This Course (Beginners):
1. Start with Heroku or Railway
2. Both have free tiers
3. Simple git-based deployment
4. Good documentation
""")

# ========== DEPLOYMENT WORKFLOW ==========
print("=" * 60)
print("TYPICAL DEPLOYMENT WORKFLOW")
print("=" * 60)

print("""
Local Development → Version Control → Cloud Platform

Step-by-Step:
─────────────
1. DEVELOP LOCALLY
   - Write your code
   - Test locally
   - Create requirements.txt

2. VERSION CONTROL
   - Initialize git repository
   - Commit your changes
   - Push to GitHub

3. CONFIGURE PLATFORM
   - Create account
   - Create new app
   - Configure environment variables

4. DEPLOY
   - Connect GitHub repo
   - Push to deploy
   - Or use CLI to deploy

5. MONITOR
   - Check logs
   - Monitor performance
   - Debug issues
""")

# ========== DEPLOYMENT REQUIREMENTS ==========
print("=" * 60)
print("DEPLOYMENT REQUIREMENTS")
print("=" * 60)

print("""
Essential Files for Python Deployment:

1. requirements.txt
   ─────────────────
   Lists all Python dependencies
   
   Example:
   flask==2.0.1
   gunicorn==20.1.0
   python-dotenv==0.19.0

2. Procfile (for Heroku)
   ──────────────────────
   Tells Heroku how to run your app
   
   Example:
   web: gunicorn app:app

3. runtime.txt (optional)
   ───────────────────────
   Specifies Python version
   
   Example:
   python-3.10.0

4. .env (local only)
   ──────────────────
   Environment variables (DO NOT commit!)
   
   Example:
   DATABASE_URL=postgres://...
   SECRET_KEY=your-secret-key

5. .gitignore
   ───────────
   Files to exclude from git
   
   Example:
   .env
   __pycache__/
   *.pyc
   venv/
""")

# ========== SAMPLE PROJECT STRUCTURE ==========
print("=" * 60)
print("SAMPLE PROJECT STRUCTURE FOR DEPLOYMENT")
print("=" * 60)

print("""
my_flask_app/
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── Procfile              # Heroku process file
├── runtime.txt           # Python version (optional)
├── .env                  # Local environment vars (NOT committed)
├── .gitignore            # Files to ignore
├── static/               # Static files
│   ├── css/
│   └── js/
├── templates/            # HTML templates
│   └── index.html
└── README.md             # Documentation
""")

# ========== SIMPLE FLASK APP FOR DEPLOYMENT ==========
print("=" * 60)
print("SIMPLE FLASK APP FOR DEPLOYMENT")
print("=" * 60)

flask_app_code = '''
# app.py - Simple Flask App Ready for Deployment
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from the Cloud!",
        "status": "running",
        "environment": os.getenv("FLASK_ENV", "production")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
'''

print("Example Flask App (app.py):")
print(flask_app_code)

requirements_content = '''
# requirements.txt
flask==2.3.0
gunicorn==21.2.0
python-dotenv==1.0.0
'''

print("\nrequirements.txt:")
print(requirements_content)

procfile_content = '''
# Procfile (no extension)
web: gunicorn app:app
'''

print("\nProcfile:")
print(procfile_content)

# ========== SUMMARY ==========
print("=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ Cloud computing provides on-demand resources
✅ IaaS, PaaS, SaaS are the main service models
✅ For beginners: Use Heroku or Railway
✅ Essential files: requirements.txt, Procfile
✅ Never commit secrets/environment variables
✅ Use Git for version control and deployment

Next Steps:
1. Create accounts on Heroku and Railway
2. Set up a simple Flask app
3. Practice deployment workflow
""")

print("\n" + "=" * 60)
print("✅ Cloud Platforms Overview - Complete!")
print("=" * 60)
