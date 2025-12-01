"""
Day 11 - Function-Based Views in Django
========================================
Learn: Creating views, handling requests, returning responses

Key Concepts:
- Views handle HTTP requests and return responses
- Function-based views (FBVs) are simple functions
- HttpRequest contains all request data
- HttpResponse sends data back to client
"""

# ========== WHAT IS A VIEW? ==========
print("=" * 60)
print("WHAT IS A VIEW?")
print("=" * 60)

print("""
A view is a Python function that:
1. Takes a web request (HttpRequest)
2. Returns a web response (HttpResponse)

Flow:
-----
User Request → URL Routing → View → Response

Simple View:
------------
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")

The 'request' parameter:
- Always the first parameter
- Contains all HTTP request information
- Headers, method, body, user, etc.
""")

# ========== BASIC VIEW EXAMPLES ==========
print("=" * 60)
print("BASIC VIEW EXAMPLES")
print("=" * 60)

print("""
1. Simple Text Response
-----------------------
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my website!")


2. HTML Response
----------------
def about(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head><title>About</title></head>
    <body>
        <h1>About Us</h1>
        <p>We are a Django learning site.</p>
    </body>
    </html>
    '''
    return HttpResponse(html)


3. View with Template (Recommended)
-----------------------------------
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


4. View with Context Data
-------------------------
def blog_list(request):
    context = {
        'title': 'My Blog',
        'posts': ['Post 1', 'Post 2', 'Post 3']
    }
    return render(request, 'blog/list.html', context)
""")

# ========== THE REQUEST OBJECT ==========
print("=" * 60)
print("THE HttpRequest OBJECT")
print("=" * 60)

print("""
The request object contains all HTTP request information.

Common Attributes:
------------------
request.method      # 'GET', 'POST', 'PUT', 'DELETE'
request.path        # '/blog/post/5/'
request.GET         # Query parameters dict (from URL)
request.POST        # POST data dict (from forms)
request.FILES       # Uploaded files
request.user        # Current user (if authenticated)
request.session     # Session dict
request.COOKIES     # Cookie dict
request.META        # HTTP headers and server info
request.content_type  # Content type of request body
request.body        # Raw request body (bytes)

Example - Accessing Request Data:
---------------------------------
def my_view(request):
    # Get HTTP method
    method = request.method
    
    # Get query parameter: /search/?q=django
    search_query = request.GET.get('q', '')
    
    # Get POST data from form
    if request.method == 'POST':
        username = request.POST.get('username', '')
    
    # Get current user
    if request.user.is_authenticated:
        user_name = request.user.username
    
    # Get client IP
    ip = request.META.get('REMOTE_ADDR')
    
    # Get user agent
    user_agent = request.META.get('HTTP_USER_AGENT')
    
    return HttpResponse(f"Method: {method}, Query: {search_query}")
""")

# ========== RESPONSE TYPES ==========
print("=" * 60)
print("RESPONSE TYPES")
print("=" * 60)

print("""
Django provides various response types:

1. HttpResponse - Basic Response
--------------------------------
from django.http import HttpResponse

def plain_text(request):
    return HttpResponse("Plain text response")

def html_response(request):
    return HttpResponse("<h1>HTML Response</h1>")

def with_status(request):
    return HttpResponse("Created!", status=201)

def with_content_type(request):
    return HttpResponse(
        "Some data",
        content_type='text/plain'
    )


2. JsonResponse - JSON Data
---------------------------
from django.http import JsonResponse

def api_data(request):
    data = {
        'name': 'Django',
        'version': '4.2',
        'features': ['ORM', 'Templates', 'Admin']
    }
    return JsonResponse(data)

def api_list(request):
    items = [1, 2, 3, 4, 5]
    return JsonResponse(items, safe=False)  # safe=False for non-dict


3. HttpResponseRedirect - Redirect
----------------------------------
from django.http import HttpResponseRedirect
from django.urls import reverse

def old_page(request):
    return HttpResponseRedirect('/new-page/')

def redirect_named(request):
    url = reverse('blog:home')
    return HttpResponseRedirect(url)


4. Shortcuts - redirect()
-------------------------
from django.shortcuts import redirect

def my_view(request):
    # Redirect to URL
    return redirect('/some/url/')
    
    # Redirect to named URL
    return redirect('blog:post_list')
    
    # Redirect with arguments
    return redirect('blog:post_detail', pk=5)
    
    # Redirect to external URL
    return redirect('https://example.com')


5. Other Response Types
-----------------------
from django.http import (
    HttpResponseNotFound,      # 404
    HttpResponseForbidden,     # 403
    HttpResponseBadRequest,    # 400
    HttpResponseServerError,   # 500
)

def forbidden_view(request):
    return HttpResponseForbidden("Access denied")
""")

# ========== RENDER SHORTCUT ==========
print("=" * 60)
print("THE render() SHORTCUT")
print("=" * 60)

print("""
render() is the most common way to return responses.

Syntax:
-------
render(request, template_name, context=None, status=200)

Parameters:
-----------
- request: The HttpRequest object
- template_name: Path to template file
- context: Dictionary of data for template
- status: HTTP status code (default 200)

Examples:
---------
from django.shortcuts import render

# Basic render
def home(request):
    return render(request, 'home.html')

# With context
def blog_list(request):
    posts = ['Post 1', 'Post 2', 'Post 3']
    return render(request, 'blog/list.html', {'posts': posts})

# With status code
def custom_404(request):
    return render(request, '404.html', status=404)

# Full example
def profile(request):
    context = {
        'user': request.user,
        'title': 'Profile Page',
        'is_premium': True,
        'posts_count': 42
    }
    return render(request, 'users/profile.html', context)
""")

# ========== URL PARAMETERS ==========
print("=" * 60)
print("HANDLING URL PARAMETERS")
print("=" * 60)

print("""
URL parameters are passed as function arguments.

URL Pattern:
------------
path('post/<int:pk>/', views.post_detail, name='post_detail')

View:
-----
def post_detail(request, pk):
    # pk is captured from URL
    return HttpResponse(f"Viewing post #{pk}")


Multiple Parameters:
--------------------
# urls.py
path('archive/<int:year>/<int:month>/', views.archive)

# views.py
def archive(request, year, month):
    return HttpResponse(f"Archive: {month}/{year}")


Different Types:
----------------
# String parameter
path('user/<str:username>/', views.profile)

def profile(request, username):
    return HttpResponse(f"Profile: {username}")


# Slug parameter
path('article/<slug:slug>/', views.article)

def article(request, slug):
    return HttpResponse(f"Article: {slug}")


Optional Parameters with Defaults:
----------------------------------
# urls.py - Two patterns for optional parameter
path('posts/', views.post_list, name='post_list'),
path('posts/page/<int:page>/', views.post_list, name='post_list_page'),

# views.py
def post_list(request, page=1):
    return HttpResponse(f"Page {page}")
""")

# ========== HANDLING HTTP METHODS ==========
print("=" * 60)
print("HANDLING HTTP METHODS")
print("=" * 60)

print("""
Check request.method to handle different HTTP methods.

GET and POST:
-------------
def contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Process data...
        return redirect('success')
    else:
        # Display form (GET request)
        return render(request, 'contact.html')


Using Decorators:
-----------------
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET, require_POST

@require_GET
def list_items(request):
    # Only accepts GET requests
    return render(request, 'items/list.html')

@require_POST
def create_item(request):
    # Only accepts POST requests
    return redirect('items:list')

@require_http_methods(["GET", "POST"])
def item_form(request):
    # Accepts only GET and POST
    if request.method == 'POST':
        # Process form
        pass
    return render(request, 'items/form.html')
""")

# ========== QUERY PARAMETERS ==========
print("=" * 60)
print("HANDLING QUERY PARAMETERS")
print("=" * 60)

print("""
Query parameters come from URL: ?key=value&other=data

Accessing Query Parameters:
---------------------------
# URL: /search/?q=django&page=2&sort=date

def search(request):
    # Get single parameter
    query = request.GET.get('q', '')        # 'django'
    
    # Get with default value
    page = request.GET.get('page', 1)       # '2' (string!)
    
    # Convert to integer
    page = int(request.GET.get('page', 1))  # 2
    
    # Get sort order
    sort = request.GET.get('sort', 'date')  # 'date'
    
    # Check if parameter exists
    if 'q' in request.GET:
        # Do search
        pass
    
    # Get multiple values (checkboxes)
    # URL: ?tags=python&tags=django&tags=web
    tags = request.GET.getlist('tags')      # ['python', 'django', 'web']
    
    return render(request, 'search.html', {
        'query': query,
        'page': page,
        'sort': sort
    })


Practical Example - Filtered List:
----------------------------------
def product_list(request):
    # Get filter parameters
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort_by = request.GET.get('sort', 'name')
    
    # Start with all products (mock data)
    products = ['Product A', 'Product B', 'Product C']
    
    # Apply filters (in real app, query database)
    # ...
    
    return render(request, 'products/list.html', {
        'products': products,
        'filters': {
            'category': category,
            'min_price': min_price,
            'max_price': max_price,
            'sort_by': sort_by
        }
    })
""")

# ========== ERROR HANDLING ==========
print("=" * 60)
print("ERROR HANDLING IN VIEWS")
print("=" * 60)

print("""
Handle errors gracefully in views.

404 Not Found:
--------------
from django.http import Http404
from django.shortcuts import get_object_or_404

def post_detail(request, pk):
    # Option 1: Raise Http404
    try:
        post = get_post_by_id(pk)  # Your function
    except PostNotFound:
        raise Http404("Post does not exist")
    
    # Option 2: get_object_or_404 (for models)
    from .models import Post
    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'post_detail.html', {'post': post})


Try-Except in Views:
--------------------
def process_data(request):
    try:
        # Risky operation
        result = do_something_risky()
        return JsonResponse({'result': result})
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Server error'}, status=500)


Custom Error Views:
-------------------
# views.py
def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

# urls.py (main)
handler404 = 'myapp.views.handler404'
handler500 = 'myapp.views.handler500'
""")

# ========== PRACTICAL EXAMPLE ==========
print("=" * 60)
print("PRACTICAL: COMPLETE VIEWS FOR BLOG")
print("=" * 60)

print("""
Let's create a complete set of views for a blog app.

# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404

# Mock data (replace with database models later)
POSTS = [
    {'id': 1, 'title': 'First Post', 'content': 'Hello Django!', 'author': 'john'},
    {'id': 2, 'title': 'Second Post', 'content': 'Learning views', 'author': 'jane'},
    {'id': 3, 'title': 'Third Post', 'content': 'URL routing is fun', 'author': 'john'},
]

def get_post(pk):
    for post in POSTS:
        if post['id'] == pk:
            return post
    return None


# Home page
def home(request):
    return render(request, 'blog/home.html', {
        'title': 'Welcome to My Blog'
    })


# List all posts
def post_list(request):
    # Handle search
    search = request.GET.get('q', '')
    
    if search:
        filtered_posts = [p for p in POSTS if search.lower() in p['title'].lower()]
    else:
        filtered_posts = POSTS
    
    return render(request, 'blog/post_list.html', {
        'posts': filtered_posts,
        'search': search
    })


# Single post detail
def post_detail(request, pk):
    post = get_post(pk)
    if not post:
        raise Http404("Post not found")
    
    return render(request, 'blog/post_detail.html', {
        'post': post
    })


# Posts by author
def author_posts(request, username):
    author_posts = [p for p in POSTS if p['author'] == username]
    
    return render(request, 'blog/author_posts.html', {
        'author': username,
        'posts': author_posts
    })


# API endpoint - JSON response
def api_posts(request):
    return JsonResponse({'posts': POSTS})


def api_post_detail(request, pk):
    post = get_post(pk)
    if not post:
        return JsonResponse({'error': 'Not found'}, status=404)
    return JsonResponse(post)


# Contact form (GET and POST)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Process the form (send email, save to DB, etc.)
        # ...
        
        return redirect('blog:contact_success')
    
    return render(request, 'blog/contact.html')


def contact_success(request):
    return render(request, 'blog/contact_success.html')
""")

# ========== VIEW BEST PRACTICES ==========
print("=" * 60)
print("VIEW BEST PRACTICES")
print("=" * 60)

print("""
1. Keep Views Thin
------------------
❌ Bad: Business logic in views
✅ Good: Views only handle request/response, logic in services

2. Use Shortcuts
----------------
❌ Bad: HttpResponse with hand-written HTML
✅ Good: render() with templates

3. Handle Errors Gracefully
---------------------------
Always handle potential errors and return appropriate status codes.

4. Validate Input
-----------------
Never trust user input. Always validate and sanitize.

5. Use Decorators
-----------------
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required

@login_required
@require_GET
def my_view(request):
    pass

6. Return Appropriate Status Codes
----------------------------------
200 - OK (default)
201 - Created
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
500 - Server Error

7. Use Context Processors
-------------------------
For data needed in every template (user, settings, etc.)
""")

print("\n" + "=" * 60)
print("✅ Function-Based Views - Complete!")
print("=" * 60)
print("\nNext: Learn about templates (05_templates_basics.py)")
