"""
Day 8 - HTML Basics
==================
Learn: HTML structure, tags, and basics needed for web templates

Key Concepts:
- HTML = HyperText Markup Language
- Structure and content of web pages
- Foundation for web templates (Django, Flask, Jinja2)
"""

# ========== WHAT IS HTML? ==========
print("=" * 60)
print("WHAT IS HTML?")
print("=" * 60)

print("""
🌐 HTML (HyperText Markup Language):

- Standard language for creating web pages
- Uses tags to structure content
- Browser interprets HTML to render pages
- Works with CSS (styling) and JavaScript (interactivity)

Why learn HTML for Python web development?
✅ Templates use HTML structure
✅ Django/Flask templates extend HTML
✅ Understanding structure helps debug
✅ API responses sometimes include HTML
""")

# ========== BASIC HTML STRUCTURE ==========
print("\n" + "=" * 60)
print("BASIC HTML STRUCTURE")
print("=" * 60)

basic_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my first web page.</p>
</body>
</html>'''

print("📄 Basic HTML Document:")
print("-" * 50)
print(basic_html)

print("""
📋 Structure Breakdown:

<!DOCTYPE html>     → Declares HTML5 document type
<html>              → Root element of HTML page
  <head>            → Contains metadata (not visible)
    <meta>          → Metadata tags
    <title>         → Page title (shown in browser tab)
  </head>
  <body>            → Contains visible page content
    <h1>            → Main heading
    <p>             → Paragraph
  </body>
</html>
""")

# ========== HTML TAGS ==========
print("\n" + "=" * 60)
print("COMMON HTML TAGS")
print("=" * 60)

print("""
📝 Tag Syntax:

<tagname attribute="value">Content</tagname>
   │         │              │          │
   │         │              │          └─ Closing tag
   │         │              └─ Content between tags
   │         └─ Attributes (optional)
   └─ Opening tag

🏷️ Common Tags:

HEADINGS (h1 is largest, h6 is smallest):
<h1>Main Title</h1>
<h2>Section Title</h2>
<h3>Subsection</h3>

TEXT:
<p>Paragraph of text</p>
<span>Inline text</span>
<strong>Bold text</strong>
<em>Italic text</em>
<br>    ← Line break (self-closing)

LINKS:
<a href="https://example.com">Click here</a>
<a href="/page">Internal link</a>

IMAGES:
<img src="image.jpg" alt="Description">

LISTS:
<ul>                    ← Unordered list (bullets)
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<ol>                    ← Ordered list (numbers)
    <li>First</li>
    <li>Second</li>
</ol>
""")

# ========== CONTAINER ELEMENTS ==========
print("\n" + "=" * 60)
print("CONTAINER ELEMENTS")
print("=" * 60)

print("""
📦 Container Tags (for grouping content):

<div>   → Generic block container
<span>  → Generic inline container
<header> → Page/section header
<nav>    → Navigation links
<main>   → Main content
<section> → Thematic section
<article> → Independent content
<aside>  → Sidebar content
<footer> → Page/section footer

Example Layout:
─────────────────────────────────
    <header>
        <nav>Navigation</nav>
    </header>
    
    <main>
        <article>
            <h1>Title</h1>
            <p>Content...</p>
        </article>
        <aside>Sidebar</aside>
    </main>
    
    <footer>
        Footer content
    </footer>
─────────────────────────────────
""")

# ========== FORMS ==========
print("\n" + "=" * 60)
print("HTML FORMS")
print("=" * 60)

print("""
📝 Forms (important for web development!):

<form action="/submit" method="POST">
    <!-- Text input -->
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <!-- Email input -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    
    <!-- Password input -->
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">
    
    <!-- Textarea -->
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="4"></textarea>
    
    <!-- Select dropdown -->
    <label for="country">Country:</label>
    <select id="country" name="country">
        <option value="us">United States</option>
        <option value="uk">United Kingdom</option>
        <option value="ca">Canada</option>
    </select>
    
    <!-- Checkbox -->
    <input type="checkbox" id="agree" name="agree">
    <label for="agree">I agree to terms</label>
    
    <!-- Radio buttons -->
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>
    
    <!-- Submit button -->
    <button type="submit">Submit</button>
</form>

🔑 Important Form Attributes:
- action: URL to send form data to
- method: GET or POST
- name: Field name (sent to server)
- required: Makes field required
- placeholder: Hint text
- value: Default value
""")

# ========== TABLES ==========
print("\n" + "=" * 60)
print("HTML TABLES")
print("=" * 60)

print("""
📊 Table Structure:

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>City</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>30</td>
            <td>New York</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>25</td>
            <td>London</td>
        </tr>
    </tbody>
</table>

Tags:
<table>  → Table container
<thead>  → Table header section
<tbody>  → Table body section
<tr>     → Table row
<th>     → Header cell (bold, centered)
<td>     → Data cell
""")

# ========== ATTRIBUTES ==========
print("\n" + "=" * 60)
print("COMMON HTML ATTRIBUTES")
print("=" * 60)

print("""
🏷️ Important Attributes:

GLOBAL (work on any element):
id="unique-id"        → Unique identifier
class="class-name"    → CSS class (can be multiple)
style="color: red;"   → Inline CSS
title="Tooltip text"  → Hover tooltip

LINKS (<a>):
href="url"            → Destination URL
target="_blank"       → Open in new tab

IMAGES (<img>):
src="path/to/image"   → Image source
alt="description"     → Alternative text
width="100"           → Width in pixels
height="100"          → Height in pixels

FORMS:
name="field_name"     → Field name for form data
value="default"       → Default value
placeholder="hint"    → Placeholder text
required              → Required field
disabled              → Disabled field
type="text"           → Input type

Example with multiple attributes:
<input type="email" 
       id="email" 
       name="email" 
       class="form-input" 
       placeholder="Enter email"
       required>
""")

# ========== PYTHON TEMPLATE EXAMPLE ==========
print("\n" + "=" * 60)
print("HTML TEMPLATES IN PYTHON")
print("=" * 60)

print("""
🐍 Using HTML in Python Web Frameworks:

Django Template Example:
─────────────────────────────────
<!DOCTYPE html>
<html>
<head>
    <title>{{ page_title }}</title>
</head>
<body>
    <h1>Hello, {{ user.name }}!</h1>
    
    {% if user.is_authenticated %}
        <p>Welcome back!</p>
    {% else %}
        <a href="/login">Please log in</a>
    {% endif %}
    
    <h2>Your Items:</h2>
    <ul>
    {% for item in items %}
        <li>{{ item.name }} - ${{ item.price }}</li>
    {% empty %}
        <li>No items found.</li>
    {% endfor %}
    </ul>
</body>
</html>
─────────────────────────────────

Template Syntax:
{{ variable }}        → Output variable value
{% if condition %}    → If statement
{% for item in list %} → Loop
{% include "file" %}  → Include another template
{% extends "base" %}  → Inherit from base template
{% block name %}      → Define/override block
""")

# ========== GENERATING HTML WITH PYTHON ==========
print("\n" + "=" * 60)
print("GENERATING HTML WITH PYTHON")
print("=" * 60)

# Simple HTML generation
def generate_user_card(name, email, role):
    """Generate an HTML card for a user"""
    return f'''<div class="user-card">
    <h3>{name}</h3>
    <p>Email: {email}</p>
    <span class="badge">{role}</span>
</div>'''

def generate_user_list(users):
    """Generate HTML list of users"""
    html = '<ul class="user-list">\n'
    for user in users:
        html += f'    <li>{user["name"]} - {user["email"]}</li>\n'
    html += '</ul>'
    return html

def generate_table(headers, rows):
    """Generate HTML table"""
    html = '<table>\n  <thead>\n    <tr>\n'
    for header in headers:
        html += f'      <th>{header}</th>\n'
    html += '    </tr>\n  </thead>\n  <tbody>\n'
    
    for row in rows:
        html += '    <tr>\n'
        for cell in row:
            html += f'      <td>{cell}</td>\n'
        html += '    </tr>\n'
    
    html += '  </tbody>\n</table>'
    return html

# Generate examples
print("📝 Generated User Card:")
print("-" * 40)
print(generate_user_card("John Doe", "john@example.com", "Admin"))

print("\n📝 Generated User List:")
print("-" * 40)
users = [
    {"name": "John", "email": "john@example.com"},
    {"name": "Jane", "email": "jane@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]
print(generate_user_list(users))

print("\n📝 Generated Table:")
print("-" * 40)
headers = ["Name", "Age", "City"]
rows = [
    ["John", "30", "New York"],
    ["Jane", "25", "London"],
    ["Bob", "35", "Paris"]
]
print(generate_table(headers, rows))

# ========== HTML ESCAPING ==========
print("\n" + "=" * 60)
print("HTML ESCAPING (SECURITY)")
print("=" * 60)

print("""
🔒 HTML Escaping - Prevent XSS Attacks!

When inserting user input into HTML, always escape special characters:

< → &lt;
> → &gt;
& → &amp;
" → &quot;
' → &#x27;

Why? User input could contain malicious code:
<script>alert('XSS Attack!')</script>

Without escaping, this would execute in the browser!
""")

import html

# Demonstrate escaping
user_input = '<script>alert("XSS")</script>'
escaped = html.escape(user_input)

print(f"Original: {user_input}")
print(f"Escaped:  {escaped}")

print("""
🐍 Python's html module:

import html

# Escape HTML
safe_text = html.escape(user_input)

# Unescape (if needed)
original = html.unescape(escaped_text)

Django templates auto-escape by default! ✅
""")

# ========== QUICK REFERENCE ==========
print("\n" + "=" * 60)
print("HTML QUICK REFERENCE")
print("=" * 60)

print("""
📋 Most Used Tags:

Structure:  <html> <head> <body> <div> <span>
Headings:   <h1> <h2> <h3> <h4> <h5> <h6>
Text:       <p> <br> <hr> <strong> <em>
Links:      <a href="url">text</a>
Images:     <img src="url" alt="text">
Lists:      <ul> <ol> <li>
Tables:     <table> <tr> <th> <td>
Forms:      <form> <input> <button> <select> <textarea>
Semantic:   <header> <nav> <main> <article> <footer>

📋 Form Input Types:

text, password, email, number, tel, url
date, time, datetime-local
checkbox, radio
file, hidden
submit, reset, button

📋 Essential Attributes:

id, class, style, title
href (links), src (images)
name, value, type (forms)
required, disabled, readonly
""")

print("\n" + "=" * 60)
print("✅ HTML Basics - Complete!")
print("=" * 60)
