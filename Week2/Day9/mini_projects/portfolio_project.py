"""
Day 9 - Mini Project: Personal Portfolio Repository
====================================================
Build a complete Git repository from scratch!

This project combines everything you learned in Day 9.
"""

print("=" * 60)
print("MINI PROJECT: Personal Portfolio Repository")
print("=" * 60)

project_overview = """
PROJECT OVERVIEW
================

You will create a personal portfolio repository that showcases
your work as a developer. This project will help you practice:

✅ Initializing a Git repository
✅ Creating meaningful commits
✅ Using branches for features
✅ Writing a good README
✅ Creating a .gitignore
✅ Pushing to GitHub

FINAL RESULT:
A professional-looking portfolio repository on GitHub that you
can share with potential employers!
"""
print(project_overview)

# ============================================================
# STEP 1: Project Setup
# ============================================================
print("\n" + "=" * 60)
print("STEP 1: Project Setup")
print("=" * 60)

step1 = """
Create the project folder and initialize Git.

TASKS:
1. Create folder: portfolio
2. Navigate into it
3. Initialize Git
4. Create initial structure

COMMANDS:
$ mkdir portfolio
$ cd portfolio
$ git init

Create these files:
- README.md (empty for now)
- .gitignore (Python template)
- index.html (basic HTML)

SUGGESTED STRUCTURE:
portfolio/
├── .gitignore
├── README.md
├── index.html
├── css/
│   └── style.css
├── js/
│   └── main.js
└── projects/
    └── (your project descriptions)
"""
print(step1)

# ============================================================
# STEP 2: Create .gitignore
# ============================================================
print("\n" + "=" * 60)
print("STEP 2: Create .gitignore")
print("=" * 60)

step2 = """
Create a comprehensive .gitignore file.

CONTENT FOR .gitignore:

# OS files
.DS_Store
Thumbs.db

# IDE
.idea/
.vscode/
*.sublime-project
*.sublime-workspace

# Dependencies
node_modules/
venv/
__pycache__/

# Build
dist/
build/
*.egg-info/

# Environment
.env
.env.local

# Logs
*.log

# Temporary
*.tmp
*.temp
.cache/

COMMAND:
$ git add .gitignore
$ git commit -m "Add .gitignore"
"""
print(step2)

# ============================================================
# STEP 3: Create README.md
# ============================================================
print("\n" + "=" * 60)
print("STEP 3: Create Professional README")
print("=" * 60)

step3 = """
Create a professional README for your portfolio.

CONTENT FOR README.md:

# Your Name - Portfolio

## About Me
Brief introduction about yourself and your skills.

## Skills
- Python
- JavaScript
- HTML/CSS
- Git & GitHub
- (Add your skills)

## Projects

### Project 1: [Name]
- Description: Brief description
- Technologies: List technologies used
- Link: [Demo](url) | [Code](url)

### Project 2: [Name]
- Description: Brief description
- Technologies: List technologies used
- Link: [Demo](url) | [Code](url)

## Contact
- Email: your.email@example.com
- LinkedIn: [Profile](url)
- GitHub: [Profile](url)

## License
MIT License

---
⭐ Feel free to star this repo if you find it helpful!

COMMAND:
$ git add README.md
$ git commit -m "Add portfolio README"
"""
print(step3)

# ============================================================
# STEP 4: Use Branches for Features
# ============================================================
print("\n" + "=" * 60)
print("STEP 4: Use Branches for Features")
print("=" * 60)

step4 = """
Use feature branches to add content.

FEATURE 1: Add HTML structure
$ git checkout -b feature/html-structure

Create index.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>Your Name</h1>
        <nav>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>Your introduction here...</p>
        </section>
        <section id="projects">
            <h2>Projects</h2>
            <!-- Projects will go here -->
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <p>Get in touch!</p>
        </section>
    </main>
    <script src="js/main.js"></script>
</body>
</html>

$ git add index.html
$ git commit -m "Add HTML structure"
$ git checkout main
$ git merge feature/html-structure
$ git branch -d feature/html-structure
"""
print(step4)

# ============================================================
# STEP 5: Add Styling
# ============================================================
print("\n" + "=" * 60)
print("STEP 5: Add Styling (Feature Branch)")
print("=" * 60)

step5 = """
Create a feature branch for CSS.

$ git checkout -b feature/styling

Create css/style.css:
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
}

header {
    background: #2c3e50;
    color: white;
    padding: 1rem;
    text-align: center;
}

nav a {
    color: white;
    margin: 0 1rem;
    text-decoration: none;
}

main {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

section {
    margin-bottom: 3rem;
}

h2 {
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
}

$ mkdir css
$ # Create style.css with above content
$ git add css/style.css
$ git commit -m "Add CSS styling"
$ git checkout main
$ git merge feature/styling
"""
print(step5)

# ============================================================
# STEP 6: Push to GitHub
# ============================================================
print("\n" + "=" * 60)
print("STEP 6: Push to GitHub")
print("=" * 60)

step6 = """
Push your portfolio to GitHub!

1. Create repository on GitHub:
   - Name: portfolio
   - Description: My personal portfolio
   - Public
   - Do NOT initialize with README

2. Connect and push:
$ git remote add origin https://github.com/USERNAME/portfolio.git
$ git branch -M main
$ git push -u origin main

3. Enable GitHub Pages (optional):
   - Go to Settings > Pages
   - Source: main branch
   - Your portfolio will be live at:
     https://USERNAME.github.io/portfolio/

VERIFY:
- Check your GitHub profile
- Repository should be visible
- README should render nicely
"""
print(step6)

# ============================================================
# BONUS: GitHub Pages
# ============================================================
print("\n" + "=" * 60)
print("BONUS: Enable GitHub Pages")
print("=" * 60)

bonus = """
Make your portfolio live on the web!

STEPS:
1. Go to your repository on GitHub
2. Click 'Settings' tab
3. Scroll to 'Pages' section
4. Under 'Source', select 'main' branch
5. Click 'Save'
6. Wait a few minutes
7. Your site is live at: https://USERNAME.github.io/portfolio/

This gives you a free hosted website!
"""
print(bonus)

# ============================================================
# PROJECT CHECKLIST
# ============================================================
print("\n" + "=" * 60)
print("PROJECT CHECKLIST")
print("=" * 60)

checklist = """
✅ Complete these to finish the project:

[ ] Initialize Git repository
[ ] Create .gitignore (first commit)
[ ] Create README.md (second commit)
[ ] Use feature branch for HTML
[ ] Use feature branch for CSS
[ ] Merge all features to main
[ ] Connect to GitHub
[ ] Push to GitHub
[ ] (Bonus) Enable GitHub Pages

COMMIT HISTORY should look like:
- Add GitHub Pages configuration (optional)
- Merge feature/styling
- Add CSS styling
- Merge feature/html-structure  
- Add HTML structure
- Add portfolio README
- Add .gitignore
- Initial commit

Congratulations on completing the mini project! 🎉
"""
print(checklist)

print("\n" + "=" * 60)
print("✅ Mini Project Complete!")
print("=" * 60)
