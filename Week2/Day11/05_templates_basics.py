"""
Day 11 - Django Templates Basics
=================================
Learn: Template syntax, variables, tags, filters, and inheritance

Key Concepts:
- Templates separate presentation from logic
- Django Template Language (DTL) for dynamic content
- Template inheritance for DRY code
- Filters transform output, tags add logic
"""

# ========== WHAT ARE TEMPLATES? ==========
print("=" * 60)
print("WHAT ARE TEMPLATES?")
print("=" * 60)

print("""
Templates are HTML files with Django Template Language (DTL).

Purpose:
--------
- Separate presentation (HTML) from logic (Python)
- Generate dynamic HTML content
- Reuse common HTML structures
- Keep code DRY (Don't Repeat Yourself)

Template Location:
------------------
Option 1: App-level templates (recommended)
myapp/
└── templates/
    └── myapp/        # Namespace to avoid conflicts
        └── home.html

Option 2: Project-level templates
myproject/
├── templates/        # Add to DIRS in settings
│   └── base.html
└── myapp/

In settings.py:
---------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Project templates
        'APP_DIRS': True,  # Enable app templates
        ...
    },
]
""")

# ========== TEMPLATE VARIABLES ==========
print("=" * 60)
print("TEMPLATE VARIABLES")
print("=" * 60)

print("""
Variables display data passed from views.

Syntax: {{ variable_name }}

View:
-----
def home(request):
    context = {
        'title': 'Welcome',
        'username': 'John',
        'age': 25,
        'is_premium': True,
        'posts': ['Post 1', 'Post 2'],
        'user': {'name': 'John', 'email': 'john@example.com'}
    }
    return render(request, 'home.html', context)

Template:
---------
<h1>{{ title }}</h1>
<p>Hello, {{ username }}!</p>
<p>Age: {{ age }}</p>

<!-- Access object attributes -->
<p>Name: {{ user.name }}</p>
<p>Email: {{ user.email }}</p>

<!-- Access list items by index -->
<p>First post: {{ posts.0 }}</p>

<!-- Access dict items by key -->
<p>User name: {{ user.name }}</p>

<!-- If variable doesn't exist, it shows nothing -->
<p>{{ nonexistent_var }}</p>  <!-- Shows empty string -->
""")

# ========== TEMPLATE TAGS ==========
print("=" * 60)
print("TEMPLATE TAGS")
print("=" * 60)

print("""
Tags add logic to templates.

Syntax: {% tag %}

1. If / Elif / Else
-------------------
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% elif user.is_guest %}
    <p>Hello, Guest!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}

<!-- Comparison operators -->
{% if age > 18 %}
    <p>Adult</p>
{% endif %}

{% if posts %}
    <p>Has posts</p>
{% endif %}

<!-- Boolean operators -->
{% if user.is_admin and user.is_active %}
    <a href="/admin/">Admin Panel</a>
{% endif %}

{% if not user.is_banned %}
    <p>Welcome!</p>
{% endif %}

{% if age >= 18 or has_permission %}
    <p>Access granted</p>
{% endif %}


2. For Loop
-----------
{% for post in posts %}
    <article>
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
    </article>
{% endfor %}

<!-- Empty fallback -->
{% for item in items %}
    <li>{{ item }}</li>
{% empty %}
    <li>No items found.</li>
{% endfor %}

<!-- Loop variables -->
{% for post in posts %}
    {{ forloop.counter }}     <!-- 1, 2, 3... -->
    {{ forloop.counter0 }}    <!-- 0, 1, 2... -->
    {{ forloop.revcounter }}  <!-- 3, 2, 1... -->
    {{ forloop.first }}       <!-- True if first -->
    {{ forloop.last }}        <!-- True if last -->
    {{ forloop.parentloop }}  <!-- Parent loop (nested) -->
{% endfor %}

<!-- Example: Numbered list -->
<ol>
{% for item in items %}
    <li>{{ forloop.counter }}. {{ item }}</li>
{% endfor %}
</ol>


3. URL Tag
----------
<!-- Named URL without parameters -->
<a href="{% url 'home' %}">Home</a>

<!-- Named URL with parameters -->
<a href="{% url 'post_detail' pk=post.id %}">Read More</a>

<!-- With namespace -->
<a href="{% url 'blog:post_list' %}">Blog</a>
<a href="{% url 'blog:post_detail' pk=5 %}">Post 5</a>

<!-- With multiple parameters -->
<a href="{% url 'archive' year=2024 month=3 %}">March 2024</a>


4. Static Tag
-------------
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/app.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">


5. Include Tag
--------------
<!-- Include another template -->
{% include 'partials/header.html' %}

<!-- Include with context -->
{% include 'partials/card.html' with title='Hello' %}


6. Comment Tag
--------------
<!-- HTML comment (visible in source) -->
{% comment %}
    This won't be rendered or visible.
    Multi-line comments work too.
{% endcomment %}

{# Single line comment #}


7. Other Useful Tags
--------------------
{% csrf_token %}      <!-- Required in forms -->
{% now "Y-m-d" %}     <!-- Current date -->
{% cycle 'odd' 'even' %}  <!-- Alternate values in loop -->
{% spaceless %}...{% endspaceless %}  <!-- Remove whitespace -->
""")

# ========== TEMPLATE FILTERS ==========
print("=" * 60)
print("TEMPLATE FILTERS")
print("=" * 60)

print("""
Filters modify variable output.

Syntax: {{ variable|filter }}

String Filters:
---------------
{{ name|lower }}          <!-- john doe -->
{{ name|upper }}          <!-- JOHN DOE -->
{{ name|title }}          <!-- John Doe -->
{{ name|capfirst }}       <!-- John doe -->
{{ text|truncatewords:30 }}   <!-- First 30 words... -->
{{ text|truncatechars:100 }}  <!-- First 100 chars... -->
{{ text|wordcount }}      <!-- Number of words -->
{{ text|linebreaks }}     <!-- <p> tags for line breaks -->
{{ text|linebreaksbr }}   <!-- <br> for line breaks -->
{{ text|striptags }}      <!-- Remove HTML tags -->
{{ slug|slugify }}        <!-- my-slug-here -->

Number Filters:
---------------
{{ price|floatformat:2 }}     <!-- 123.46 -->
{{ number|add:5 }}            <!-- Add 5 -->
{{ items|length }}            <!-- List length -->

Date Filters:
-------------
{{ date|date:"Y-m-d" }}       <!-- 2024-03-15 -->
{{ date|date:"F j, Y" }}      <!-- March 15, 2024 -->
{{ date|date:"D, M d" }}      <!-- Fri, Mar 15 -->
{{ date|time:"H:i" }}         <!-- 14:30 -->
{{ date|timesince }}          <!-- 2 days ago -->

Default Values:
---------------
{{ value|default:"N/A" }}     <!-- Shows "N/A" if empty -->
{{ value|default_if_none:"None" }}  <!-- Only if None -->

List Filters:
-------------
{{ items|first }}             <!-- First item -->
{{ items|last }}              <!-- Last item -->
{{ items|random }}            <!-- Random item -->
{{ items|join:", " }}         <!-- a, b, c -->
{{ items|slice:":5" }}        <!-- First 5 items -->

Boolean Filters:
----------------
{{ value|yesno:"Yes,No,Maybe" }}

Escaping:
---------
{{ html_content|safe }}       <!-- Render HTML (be careful!) -->
{{ text|escape }}             <!-- HTML escape -->
{{ json_data|json_script:"data" }}  <!-- Safe JSON for JS -->

Chaining Filters:
-----------------
{{ name|lower|truncatewords:10 }}
{{ text|striptags|truncatechars:100 }}
""")

# ========== TEMPLATE INHERITANCE ==========
print("=" * 60)
print("TEMPLATE INHERITANCE")
print("=" * 60)

print("""
Template inheritance lets you create a base template and extend it.

Base Template (base.html):
--------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        <nav>
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'about' %}">About</a>
        </nav>
    </header>
    
    <main>
        {% block content %}
        <!-- Child templates override this -->
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 My Site</p>
    </footer>
    
    {% block extra_js %}{% endblock %}
</body>
</html>


Child Template (home.html):
---------------------------
{% extends 'base.html' %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
<h1>Welcome to My Site!</h1>
<p>This is the home page.</p>
{% endblock %}


Another Child (about.html):
---------------------------
{% extends 'base.html' %}

{% block title %}About - My Site{% endblock %}

{% block extra_css %}
<style>
    .about-section { background: #f0f0f0; }
</style>
{% endblock %}

{% block content %}
<section class="about-section">
    <h1>About Us</h1>
    <p>Learn more about our company.</p>
</section>
{% endblock %}


Using block.super:
------------------
{% block title %}{{ block.super }} - More Info{% endblock %}
<!-- Outputs: "My Site - More Info" -->


Multiple Levels of Inheritance:
-------------------------------
base.html
    └── blog/base.html (extends base.html)
            └── blog/post_list.html (extends blog/base.html)
""")

# ========== PRACTICAL TEMPLATE EXAMPLES ==========
print("=" * 60)
print("PRACTICAL TEMPLATE EXAMPLES")
print("=" * 60)

print("""
1. Post List with Pagination
----------------------------
{% extends 'base.html' %}

{% block content %}
<h1>Blog Posts</h1>

{% for post in posts %}
<article class="post">
    <h2>
        <a href="{% url 'blog:post_detail' pk=post.id %}">
            {{ post.title }}
        </a>
    </h2>
    <p class="meta">
        By {{ post.author.username }} | 
        {{ post.created_at|date:"M d, Y" }}
    </p>
    <p>{{ post.content|truncatewords:50 }}</p>
</article>
{% empty %}
<p>No posts yet.</p>
{% endfor %}

<!-- Pagination -->
{% if page_obj.has_previous %}
<a href="?page={{ page_obj.previous_page_number }}">Previous</a>
{% endif %}

<span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>

{% if page_obj.has_next %}
<a href="?page={{ page_obj.next_page_number }}">Next</a>
{% endif %}
{% endblock %}


2. Form with CSRF Token
-----------------------
{% extends 'base.html' %}

{% block content %}
<h1>Contact Us</h1>

<form method="post">
    {% csrf_token %}
    
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>
    
    <button type="submit">Send</button>
</form>
{% endblock %}


3. Conditional Display
----------------------
{% block content %}
<h1>Dashboard</h1>

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    
    {% if user.is_staff %}
        <a href="{% url 'admin:index' %}">Admin Panel</a>
    {% endif %}
    
    {% if notifications %}
        <div class="notifications">
            <h3>Notifications ({{ notifications|length }})</h3>
            <ul>
            {% for notification in notifications %}
                <li class="{% if notification.unread %}unread{% endif %}">
                    {{ notification.message }}
                </li>
            {% endfor %}
            </ul>
        </div>
    {% endif %}
{% else %}
    <p><a href="{% url 'login' %}">Log in</a> to see your dashboard.</p>
{% endif %}
{% endblock %}


4. Include with Partials
------------------------
<!-- templates/partials/post_card.html -->
<article class="card">
    <h3>{{ post.title }}</h3>
    <p>{{ post.content|truncatewords:20 }}</p>
    <a href="{% url 'blog:post_detail' pk=post.id %}">Read more</a>
</article>

<!-- templates/blog/home.html -->
{% block content %}
<h1>Latest Posts</h1>
<div class="grid">
{% for post in posts %}
    {% include 'partials/post_card.html' with post=post %}
{% endfor %}
</div>
{% endblock %}
""")

# ========== STATIC FILES IN TEMPLATES ==========
print("=" * 60)
print("USING STATIC FILES")
print("=" * 60)

print("""
Static files: CSS, JavaScript, images

Setup in settings.py:
---------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

File Structure:
---------------
myproject/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── images/
│       └── logo.png
└── myapp/
    └── static/
        └── myapp/
            └── css/
                └── app_style.css

Using in Templates:
-------------------
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link rel="stylesheet" href="{% static 'myapp/css/app_style.css' %}">
</head>
<body>
    <!-- Image -->
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    
    <!-- JavaScript -->
    <script src="{% static 'js/app.js' %}"></script>
</body>
</html>

Remember:
- Always use {% load static %} at top of template
- Use {% static 'path' %} not hardcoded paths
- Run collectstatic for production
""")

# ========== COMPLETE TEMPLATE EXAMPLE ==========
print("=" * 60)
print("COMPLETE EXAMPLE: BLOG TEMPLATES")
print("=" * 60)

print("""
Project Structure:
------------------
blog/
└── templates/
    └── blog/
        ├── base.html
        ├── home.html
        ├── post_list.html
        └── post_detail.html


base.html:
----------
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Blog{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
</head>
<body>
    <header>
        <h1>My Blog</h1>
        <nav>
            <a href="{% url 'blog:home' %}">Home</a>
            <a href="{% url 'blog:post_list' %}">Posts</a>
        </nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 My Blog. All rights reserved.</p>
    </footer>
</body>
</html>


home.html:
----------
{% extends 'blog/base.html' %}

{% block title %}Welcome - My Blog{% endblock %}

{% block content %}
<section class="hero">
    <h2>Welcome to {{ site_name|default:"My Blog" }}!</h2>
    <p>Discover interesting articles about Django and Python.</p>
    <a href="{% url 'blog:post_list' %}" class="btn">Browse Posts</a>
</section>

{% if featured_posts %}
<section class="featured">
    <h3>Featured Posts</h3>
    {% for post in featured_posts %}
    <article>
        <h4>{{ post.title }}</h4>
        <p>{{ post.content|truncatechars:150 }}</p>
        <a href="{% url 'blog:post_detail' pk=post.id %}">Read more</a>
    </article>
    {% endfor %}
</section>
{% endif %}
{% endblock %}


post_list.html:
---------------
{% extends 'blog/base.html' %}

{% block title %}All Posts - My Blog{% endblock %}

{% block content %}
<h2>All Posts</h2>

{% if posts %}
    {% for post in posts %}
    <article class="post-card">
        <h3>
            <a href="{% url 'blog:post_detail' pk=post.id %}">
                {{ post.title }}
            </a>
        </h3>
        <div class="meta">
            <span>By {{ post.author|default:"Anonymous" }}</span>
            <span>{{ post.created_at|date:"M d, Y" }}</span>
        </div>
        <p>{{ post.content|truncatewords:30 }}</p>
    </article>
    {% endfor %}
{% else %}
    <p>No posts available yet. Check back soon!</p>
{% endif %}
{% endblock %}


post_detail.html:
-----------------
{% extends 'blog/base.html' %}

{% block title %}{{ post.title }} - My Blog{% endblock %}

{% block content %}
<article class="post-detail">
    <header>
        <h2>{{ post.title }}</h2>
        <p class="meta">
            By {{ post.author|default:"Anonymous" }} | 
            {{ post.created_at|date:"F j, Y" }}
        </p>
    </header>
    
    <div class="content">
        {{ post.content|linebreaks }}
    </div>
    
    <footer>
        <a href="{% url 'blog:post_list' %}">&larr; Back to Posts</a>
    </footer>
</article>
{% endblock %}
""")

# ========== TEMPLATE BEST PRACTICES ==========
print("=" * 60)
print("TEMPLATE BEST PRACTICES")
print("=" * 60)

print("""
1. Use Template Inheritance
---------------------------
Create a base.html and extend it everywhere.

2. Keep Logic Out of Templates
------------------------------
❌ {% if user.posts.count > 0 and user.is_active %}
✅ {% if show_posts %}  (calculated in view)

3. Use Meaningful Block Names
-----------------------------
❌ {% block a %}
✅ {% block sidebar_content %}

4. Always Use {% url %} Tag
---------------------------
❌ <a href="/blog/post/5/">
✅ <a href="{% url 'blog:post_detail' pk=5 %}">

5. Escape User Input
--------------------
Django auto-escapes, but be careful with |safe filter.

6. Use {% static %} for Static Files
------------------------------------
❌ <img src="/static/logo.png">
✅ <img src="{% static 'logo.png' %}">

7. Comment Your Templates
-------------------------
{# This explains what this section does #}

8. Organize with Includes
-------------------------
{% include 'partials/navbar.html' %}
{% include 'partials/footer.html' %}

9. Use Template Context Processors
----------------------------------
For data needed in every template (site name, user, etc.)
""")

print("\n" + "=" * 60)
print("✅ Django Templates Basics - Complete!")
print("=" * 60)
print("\nNext: Complete the exercises and build the mini-project!")
