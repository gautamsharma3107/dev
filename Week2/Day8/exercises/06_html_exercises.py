"""
Day 8 - Exercise 6: HTML Exercises
==================================
Practice working with HTML for web templates
"""

print("=" * 60)
print("Exercise 6: HTML Basics")
print("=" * 60)

import html

# ============================================================
# Exercise 6.1: HTML Structure Analysis
# ============================================================

print("\n📝 Exercise 6.1: Analyze HTML Structure")
print("-" * 50)
print("""
Given the HTML below, identify and list:
1. All heading tags and their level
2. All form elements
3. All links (anchors)
4. The navigation structure
5. Any semantic HTML5 elements used
""")

sample_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Blog</title>
</head>
<body>
    <header>
        <h1>Welcome to My Blog</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <article>
            <h2>Latest Post</h2>
            <p>This is my latest blog post content.</p>
            <a href="/posts/1">Read more</a>
        </article>
        
        <aside>
            <h3>Subscribe</h3>
            <form action="/subscribe" method="POST">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <button type="submit">Subscribe</button>
            </form>
        </aside>
    </main>
    
    <footer>
        <p>&copy; 2024 My Blog</p>
        <a href="https://twitter.com/myblog">Follow on Twitter</a>
    </footer>
</body>
</html>
"""

print(sample_html)

# TODO: Write your answers as comments:
# 1. Headings:
# 
# 2. Form elements:
# 
# 3. Links:
# 
# 4. Navigation structure:
# 
# 5. Semantic HTML5 elements:
# 

# ============================================================
# Exercise 6.2: Generate HTML Elements
# ============================================================

print("\n📝 Exercise 6.2: Generate HTML with Python")
print("-" * 50)
print("""
Create functions to generate common HTML elements.
""")

def create_heading(level, text, class_name=None):
    """Create an HTML heading element (h1-h6)"""
    # TODO: Implement
    pass

def create_link(href, text, target="_self", class_name=None):
    """Create an anchor element"""
    # TODO: Implement
    pass

def create_image(src, alt, width=None, height=None):
    """Create an image element"""
    # TODO: Implement
    pass

def create_list(items, ordered=False, class_name=None):
    """Create an ordered or unordered list"""
    # TODO: Implement
    pass

def create_table(headers, rows, class_name=None):
    """Create an HTML table"""
    # TODO: Implement
    pass

# Test your functions:
# print(create_heading(1, "Welcome", "title"))
# print(create_link("/about", "About Us", "_blank", "nav-link"))
# print(create_image("photo.jpg", "Profile photo", 100, 100))
# print(create_list(["Item 1", "Item 2", "Item 3"]))
# print(create_list(["First", "Second"], ordered=True))
# print(create_table(["Name", "Age"], [["John", "30"], ["Jane", "25"]]))

# ============================================================
# Exercise 6.3: Create an HTML Form
# ============================================================

print("\n📝 Exercise 6.3: Create an HTML Form")
print("-" * 50)
print("""
Create a function that generates a complete HTML form for user registration.

Required fields:
- Username (text, required)
- Email (email, required)
- Password (password, required, min 8 chars)
- Confirm Password (password, required)
- Date of Birth (date)
- Gender (radio: Male/Female/Other)
- Country (select with options)
- Terms Agreement (checkbox, required)
- Submit button
""")

def create_registration_form(action="/register", method="POST"):
    """Generate a complete registration form"""
    # TODO: Implement
    pass

# Test:
# print(create_registration_form())

# ============================================================
# Exercise 6.4: HTML Escaping
# ============================================================

print("\n📝 Exercise 6.4: HTML Escaping and Security")
print("-" * 50)
print("""
Demonstrate proper HTML escaping to prevent XSS attacks.
""")

# Potentially malicious user inputs
user_inputs = [
    "Normal text",
    "<script>alert('XSS')</script>",
    "Hello <b>World</b>",
    "5 > 3 && 2 < 4",
    "\"quotes\" and 'apostrophes'",
    "<img src=x onerror=alert('XSS')>",
]

def safe_display(user_input):
    """
    Safely display user input by escaping HTML.
    Returns escaped string wrapped in a paragraph tag.
    """
    # TODO: Implement
    pass

# Test:
# for text in user_inputs:
#     print(f"Input: {text}")
#     print(f"Safe:  {safe_display(text)}")
#     print()

# ============================================================
# Exercise 6.5: Simple Template Engine
# ============================================================

print("\n📝 Exercise 6.5: Build a Simple Template Engine")
print("-" * 50)
print("""
Create a simple template engine that can:
1. Replace {{ variable }} with values
2. Handle {{ if condition }} blocks
3. Handle {{ for item in list }} loops
""")

def render_template(template, context):
    """
    Render a template string with context variables.
    
    Supports:
    - {{ variable }} - Variable substitution
    - {{ variable|escape }} - Escaped variable
    
    Args:
        template: Template string
        context: Dictionary of variables
        
    Returns:
        Rendered string
    """
    # TODO: Implement basic variable substitution
    pass

# Test templates:
# template1 = "<h1>Hello, {{ name }}!</h1><p>You have {{ count }} messages.</p>"
# context1 = {"name": "John", "count": 5}
# print(render_template(template1, context1))

# template2 = "<p>User input: {{ user_input|escape }}</p>"
# context2 = {"user_input": "<script>alert('XSS')</script>"}
# print(render_template(template2, context2))

# ============================================================
# Exercise 6.6: Build a Page Generator
# ============================================================

print("\n📝 Exercise 6.6: HTML Page Generator")
print("-" * 50)
print("""
Create a class that generates complete HTML pages.
""")

class HTMLPage:
    """Generate complete HTML pages"""
    
    def __init__(self, title="Untitled"):
        """Initialize with page title"""
        # TODO: Implement
        pass
    
    def add_meta(self, name, content):
        """Add meta tag"""
        # TODO: Implement
        pass
    
    def add_css(self, href):
        """Add CSS stylesheet link"""
        # TODO: Implement
        pass
    
    def add_js(self, src, defer=True):
        """Add JavaScript file"""
        # TODO: Implement
        pass
    
    def set_body_content(self, content):
        """Set the body content"""
        # TODO: Implement
        pass
    
    def render(self):
        """Render the complete HTML page"""
        # TODO: Implement
        pass

# Test:
# page = HTMLPage("My Website")
# page.add_meta("description", "A sample website")
# page.add_meta("viewport", "width=device-width, initial-scale=1")
# page.add_css("/styles/main.css")
# page.add_js("/scripts/app.js")
# page.set_body_content("""
#     <header><h1>Welcome</h1></header>
#     <main><p>Hello, World!</p></main>
#     <footer><p>&copy; 2024</p></footer>
# """)
# print(page.render())

print("\n" + "=" * 60)
print("✅ Complete the exercises above!")
print("=" * 60)

"""
SOLUTIONS:

Exercise 6.1:
1. Headings: h1 (Welcome), h2 (Latest Post), h3 (Subscribe)
2. Form elements: form, label, input (email), button
3. Links: Home (/), About (/about), Contact (/contact), Read more (/posts/1), Twitter
4. Navigation: <nav> containing <ul> with 3 <li> items
5. Semantic HTML5: header, nav, main, article, aside, footer

Exercise 6.2:
def create_heading(level, text, class_name=None):
    class_attr = f' class="{class_name}"' if class_name else ''
    return f'<h{level}{class_attr}>{html.escape(text)}</h{level}>'

def create_link(href, text, target="_self", class_name=None):
    class_attr = f' class="{class_name}"' if class_name else ''
    target_attr = f' target="{target}"' if target != "_self" else ''
    return f'<a href="{href}"{target_attr}{class_attr}>{html.escape(text)}</a>'

def create_image(src, alt, width=None, height=None):
    attrs = [f'src="{src}"', f'alt="{html.escape(alt)}"']
    if width: attrs.append(f'width="{width}"')
    if height: attrs.append(f'height="{height}"')
    return f'<img {" ".join(attrs)}>'

def create_list(items, ordered=False, class_name=None):
    tag = 'ol' if ordered else 'ul'
    class_attr = f' class="{class_name}"' if class_name else ''
    items_html = ''.join(f'<li>{html.escape(item)}</li>' for item in items)
    return f'<{tag}{class_attr}>{items_html}</{tag}>'

def create_table(headers, rows, class_name=None):
    class_attr = f' class="{class_name}"' if class_name else ''
    header_html = '<tr>' + ''.join(f'<th>{html.escape(h)}</th>' for h in headers) + '</tr>'
    rows_html = ''
    for row in rows:
        rows_html += '<tr>' + ''.join(f'<td>{html.escape(str(c))}</td>' for c in row) + '</tr>'
    return f'<table{class_attr}><thead>{header_html}</thead><tbody>{rows_html}</tbody></table>'

Exercise 6.3:
def create_registration_form(action="/register", method="POST"):
    return f'''
<form action="{action}" method="{method}">
    <div>
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
    </div>
    <div>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" minlength="8" required>
    </div>
    <div>
        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" name="confirm_password" required>
    </div>
    <div>
        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob">
    </div>
    <div>
        <span>Gender:</span>
        <input type="radio" id="male" name="gender" value="male">
        <label for="male">Male</label>
        <input type="radio" id="female" name="gender" value="female">
        <label for="female">Female</label>
        <input type="radio" id="other" name="gender" value="other">
        <label for="other">Other</label>
    </div>
    <div>
        <label for="country">Country:</label>
        <select id="country" name="country">
            <option value="">Select...</option>
            <option value="us">United States</option>
            <option value="uk">United Kingdom</option>
            <option value="ca">Canada</option>
        </select>
    </div>
    <div>
        <input type="checkbox" id="terms" name="terms" required>
        <label for="terms">I agree to the Terms</label>
    </div>
    <button type="submit">Register</button>
</form>
'''

Exercise 6.4:
def safe_display(user_input):
    escaped = html.escape(user_input)
    return f'<p>{escaped}</p>'

Exercise 6.5:
import re

def render_template(template, context):
    def replace_var(match):
        var_name = match.group(1).strip()
        if '|escape' in var_name:
            var_name = var_name.replace('|escape', '').strip()
            return html.escape(str(context.get(var_name, '')))
        return str(context.get(var_name, ''))
    
    return re.sub(r'{{\s*(.*?)\s*}}', replace_var, template)

Exercise 6.6:
class HTMLPage:
    def __init__(self, title="Untitled"):
        self.title = title
        self.meta_tags = []
        self.css_links = []
        self.js_scripts = []
        self.body_content = ""
    
    def add_meta(self, name, content):
        self.meta_tags.append(f'<meta name="{name}" content="{content}">')
    
    def add_css(self, href):
        self.css_links.append(f'<link rel="stylesheet" href="{href}">')
    
    def add_js(self, src, defer=True):
        defer_attr = ' defer' if defer else ''
        self.js_scripts.append(f'<script src="{src}"{defer_attr}></script>')
    
    def set_body_content(self, content):
        self.body_content = content
    
    def render(self):
        meta = '\n    '.join(self.meta_tags)
        css = '\n    '.join(self.css_links)
        js = '\n    '.join(self.js_scripts)
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {meta}
    <title>{self.title}</title>
    {css}
</head>
<body>
{self.body_content}
    {js}
</body>
</html>'''
"""
