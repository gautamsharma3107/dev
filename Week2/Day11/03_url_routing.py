"""
Day 11 - URL Routing in Django
===============================
Learn: URL patterns, path converters, named URLs, and namespacing

Key Concepts:
- URLconf maps URLs to views
- Path converters capture URL parameters
- Named URLs for reverse lookups
- Namespaces prevent naming conflicts
"""

# ========== URL ROUTING BASICS ==========
print("=" * 60)
print("URL ROUTING BASICS")
print("=" * 60)

print("""
Django uses URLconf (URL configuration) to route URLs to views.

Flow:
-----
Browser Request → urls.py → view function → Response

Example:
--------
User visits: http://example.com/blog/post/5/

Django checks urls.py patterns:
1. Matches 'blog/post/5/' 
2. Extracts '5' as parameter
3. Calls view function with pk=5
4. Returns response to browser
""")

# ========== URL PATTERNS ==========
print("=" * 60)
print("URL PATTERNS")
print("=" * 60)

print("""
URL patterns use the path() function:

from django.urls import path
from . import views

urlpatterns = [
    path('route/', views.function, name='name'),
]

Arguments:
----------
- 'route/': URL pattern (string)
- views.function: View function to call
- name='name': Named URL for reverse lookups

Examples:
---------
urlpatterns = [
    path('', views.home, name='home'),           # /
    path('about/', views.about, name='about'),   # /about/
    path('contact/', views.contact, name='contact'), # /contact/
]
""")

# ========== PATH CONVERTERS ==========
print("=" * 60)
print("PATH CONVERTERS")
print("=" * 60)

print("""
Path converters capture parts of the URL as parameters.

Syntax: <type:name>

Available Converters:
---------------------
str   - Matches any non-empty string, excluding '/'
       Default type if not specified
       Example: <str:username> or <username>

int   - Matches zero or any positive integer
       Example: <int:id> matches 0, 1, 123

slug  - Matches slug strings (letters, numbers, hyphens, underscores)
       Example: <slug:title> matches my-blog-post

uuid  - Matches formatted UUID
       Example: <uuid:pk> matches 075194d3-6885-417e-a8a8-6c931e272f00

path  - Matches any non-empty string, INCLUDING '/'
       Example: <path:file_path> matches docs/pdf/file.pdf

Examples in urls.py:
--------------------
urlpatterns = [
    # Integer ID
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # /post/1/, /post/42/
    
    # String username
    path('user/<str:username>/', views.profile, name='profile'),
    # /user/john/, /user/jane_doe/
    
    # Slug for SEO-friendly URLs
    path('article/<slug:slug>/', views.article, name='article'),
    # /article/my-first-post/, /article/django-tutorial/
    
    # UUID for unique identifiers
    path('item/<uuid:item_id>/', views.item, name='item'),
    
    # Path for file paths
    path('download/<path:file_path>/', views.download, name='download'),
    # /download/docs/manual.pdf/
]
""")

# ========== USING URL PARAMETERS IN VIEWS ==========
print("=" * 60)
print("USING URL PARAMETERS IN VIEWS")
print("=" * 60)

print("""
URL parameters are passed to view functions as arguments.

URL Pattern:
------------
path('post/<int:pk>/', views.post_detail, name='post_detail')

View Function:
--------------
def post_detail(request, pk):
    # pk is captured from URL
    # If URL is /post/5/, then pk = 5
    return HttpResponse(f"Viewing post {pk}")

Multiple Parameters:
--------------------
# urls.py
path('blog/<int:year>/<int:month>/', views.archive, name='archive')

# views.py
def archive(request, year, month):
    return HttpResponse(f"Archive for {month}/{year}")

# /blog/2024/3/ → year=2024, month=3
""")

# ========== NAMED URLS ==========
print("=" * 60)
print("NAMED URLS")
print("=" * 60)

print("""
Named URLs allow you to refer to URLs by name instead of path.

Why use named URLs?
-------------------
- URLs can change, but names stay the same
- Easier to maintain
- Less error-prone
- Works in templates and views

Defining named URLs:
--------------------
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.post, name='post_detail'),
]

Using in Templates:
-------------------
<!-- Basic URL -->
<a href="{% url 'home' %}">Home</a>

<!-- URL with parameter -->
<a href="{% url 'post_detail' pk=5 %}">View Post</a>

<!-- URL with multiple parameters -->
<a href="{% url 'archive' year=2024 month=3 %}">March 2024</a>

Using in Views (reverse):
-------------------------
from django.urls import reverse
from django.shortcuts import redirect

def my_view(request):
    # Get URL string
    url = reverse('home')  # Returns '/'
    url = reverse('post_detail', kwargs={'pk': 5})  # Returns '/post/5/'
    
    # Redirect using named URL
    return redirect('home')
    return redirect('post_detail', pk=5)
""")

# ========== URL NAMESPACING ==========
print("=" * 60)
print("URL NAMESPACING")
print("=" * 60)

print("""
Namespaces prevent URL name conflicts between apps.

Problem without namespaces:
---------------------------
# blog/urls.py
path('', views.home, name='home')

# shop/urls.py  
path('', views.home, name='home')  # Conflict!

Solution: App namespaces
------------------------

Step 1: Add app_name in app urls.py
-----------------------------------
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'  # Namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post, name='post_detail'),
]

# shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'  # Different namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product, name='product_detail'),
]

Step 2: Use namespace:name format
---------------------------------
# In templates
<a href="{% url 'blog:home' %}">Blog Home</a>
<a href="{% url 'shop:home' %}">Shop Home</a>
<a href="{% url 'blog:post_detail' pk=5 %}">View Post</a>

# In views
from django.urls import reverse

url = reverse('blog:home')
url = reverse('shop:product_detail', kwargs={'pk': 10})
redirect('blog:post_detail', pk=5)
""")

# ========== INCLUDING APP URLS ==========
print("=" * 60)
print("INCLUDING APP URLS")
print("=" * 60)

print("""
Use include() to reference app URLs from main urls.py.

Main urls.py (project level):
-----------------------------
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include app URLs
    path('blog/', include('blog.urls')),
    # All blog URLs start with /blog/
    
    path('shop/', include('shop.urls')),
    # All shop URLs start with /shop/
    
    # Include at root
    path('', include('pages.urls')),
    # Pages URLs at root level
]

Result:
-------
/admin/          → Django admin
/blog/           → blog.views.home
/blog/post/5/    → blog.views.post_detail (pk=5)
/shop/           → shop.views.home
/shop/product/1/ → shop.views.product_detail (pk=1)
/                → pages.views.home
/about/          → pages.views.about
""")

# ========== RE_PATH FOR REGEX ==========
print("=" * 60)
print("RE_PATH FOR COMPLEX PATTERNS")
print("=" * 60)

print("""
For complex URL patterns, use re_path() with regex.

from django.urls import re_path
from . import views

urlpatterns = [
    # 4-digit year
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    
    # Year and month
    re_path(
        r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
        views.month_archive
    ),
    
    # Optional trailing slash
    re_path(r'^about/?$', views.about),
]

Regex Reference:
----------------
^       - Start of string
$       - End of string
[0-9]   - Any digit
{4}     - Exactly 4 times
+       - One or more
*       - Zero or more
?       - Optional (zero or one)
(?P<name>pattern) - Named group

Note: Prefer path() when possible. It's simpler and faster.
Use re_path() only when you need regex flexibility.
""")

# ========== ERROR HANDLING URLS ==========
print("=" * 60)
print("CUSTOM ERROR PAGES")
print("=" * 60)

print("""
Django allows custom error pages (404, 500, etc.)

Step 1: Create error views
--------------------------
# views.py
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

Step 2: Set handlers in main urls.py
------------------------------------
# myproject/urls.py
from django.conf.urls import handler404, handler500

handler404 = 'myapp.views.custom_404'
handler500 = 'myapp.views.custom_500'

Step 3: Create templates
------------------------
# templates/404.html
<h1>Page Not Found</h1>
<p>Sorry, the page you requested doesn't exist.</p>

# templates/500.html
<h1>Server Error</h1>
<p>Something went wrong. Please try again later.</p>

Note: Error pages only work when DEBUG = False!
""")

# ========== PRACTICAL EXAMPLE ==========
print("=" * 60)
print("PRACTICAL: COMPLETE URL CONFIGURATION")
print("=" * 60)

print("""
Let's build a complete URL structure for a blog:

Project Structure:
------------------
myblog/
├── myblog/
│   └── urls.py          # Main URLconf
├── blog/
│   └── urls.py          # Blog app URLs
└── pages/
    └── urls.py          # Static pages URLs

Main urls.py:
-------------
# myblog/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('pages.urls', namespace='pages')),
]

Blog urls.py:
-------------
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    path('', views.post_list, name='post_list'),
    
    # /blog/post/5/
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # /blog/post/my-first-post/
    path('post/<slug:slug>/', views.post_by_slug, name='post_by_slug'),
    
    # /blog/category/python/
    path('category/<slug:category>/', views.category, name='category'),
    
    # /blog/archive/2024/03/
    path('archive/<int:year>/<int:month>/', views.archive, name='archive'),
    
    # /blog/author/john/
    path('author/<str:username>/', views.author_posts, name='author_posts'),
]

Pages urls.py:
--------------
# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

Using in Templates:
-------------------
<nav>
    <a href="{% url 'pages:home' %}">Home</a>
    <a href="{% url 'blog:post_list' %}">Blog</a>
    <a href="{% url 'pages:about' %}">About</a>
</nav>

<article>
    <a href="{% url 'blog:post_detail' pk=post.id %}">
        {{ post.title }}
    </a>
    <a href="{% url 'blog:category' category='python' %}">Python</a>
    <a href="{% url 'blog:author_posts' username=post.author.username %}">
        By {{ post.author }}
    </a>
</article>
""")

# ========== URL BEST PRACTICES ==========
print("=" * 60)
print("URL BEST PRACTICES")
print("=" * 60)

print("""
1. Use Descriptive Names
------------------------
❌ path('p/', views.post, name='p')
✅ path('posts/', views.post_list, name='post_list')

2. Use Trailing Slashes Consistently
------------------------------------
Django adds trailing slashes by default.
Be consistent: either all URLs have them or none.

3. Use Namespaces
-----------------
Always add app_name to prevent conflicts.

4. Keep URLs RESTful
--------------------
GET  /posts/        → List all posts
GET  /posts/5/      → View post 5
POST /posts/        → Create new post
PUT  /posts/5/      → Update post 5
DELETE /posts/5/    → Delete post 5

5. Use Meaningful Path Converters
---------------------------------
❌ path('post/<pk>/', ...)      # Unclear type
✅ path('post/<int:pk>/', ...)  # Clear: integer

6. Organize URLs Logically
--------------------------
Group related URLs together.
Use include() for app URLs.

7. Use Named URLs Everywhere
----------------------------
Never hardcode URLs in templates or views.
{% url 'name' %} in templates
reverse('name') in views
""")

print("\n" + "=" * 60)
print("✅ URL Routing - Complete!")
print("=" * 60)
print("\nNext: Learn about function-based views (04_views_basics.py)")
