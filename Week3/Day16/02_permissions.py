"""
Day 16 - Permissions in Django REST Framework
==============================================
Learn: Permission classes, custom permissions, object-level permissions

Key Concepts:
- Permissions determine whether a request should be granted or denied access
- DRF provides several built-in permission classes
- You can create custom permission classes for specific needs
- Object-level permissions check access on specific objects
"""

# ========== PERMISSION BASICS ==========
print("=" * 60)
print("PERMISSION BASICS")
print("=" * 60)

print("""
Permissions in DRF:
-------------------
- Run after authentication
- Determine if the request should be permitted
- Return True (allow) or False (deny)
- Can be set globally or per-view

Permission Flow:
----------------
1. Request comes in
2. Authentication runs first (who is the user?)
3. Permissions run next (is this user allowed?)
4. If both pass, view is executed
""")

# ========== BUILT-IN PERMISSIONS ==========
print("\n" + "=" * 60)
print("BUILT-IN PERMISSION CLASSES")
print("=" * 60)

print("""
DRF provides these built-in permission classes:

1. AllowAny
   - Allows unrestricted access
   - Good for public endpoints
   
2. IsAuthenticated
   - Only authenticated users
   - Most common permission
   
3. IsAdminUser
   - Only admin users (is_staff=True)
   - For admin-only endpoints
   
4. IsAuthenticatedOrReadOnly
   - Authenticated users get full access
   - Anonymous users can only read (GET, HEAD, OPTIONS)
   
5. DjangoModelPermissions
   - Maps to Django's model permissions
   - POST requires 'add', PUT/PATCH requires 'change', DELETE requires 'delete'
   
6. DjangoModelPermissionsOrAnonReadOnly
   - Like above, but allows anonymous read
   
7. DjangoObjectPermissions
   - Per-object permissions using django-guardian
""")

# ========== SETTING PERMISSIONS GLOBALLY ==========
print("\n" + "=" * 60)
print("GLOBAL PERMISSION SETTINGS")
print("=" * 60)

global_settings_code = '''
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Require auth by default
    ],
}

# Alternative global settings:

# Allow anyone (not recommended for production)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Admin only by default
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
}
'''

print(global_settings_code)

# ========== VIEW-LEVEL PERMISSIONS ==========
print("\n" + "=" * 60)
print("VIEW-LEVEL PERMISSIONS")
print("=" * 60)

view_level_code = '''
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny, 
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)


class PublicView(APIView):
    """Anyone can access this view."""
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({'message': 'Public endpoint'})


class PrivateView(APIView):
    """Only authenticated users can access."""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': f'Hello, {request.user.username}!'})


class AdminOnlyView(APIView):
    """Only admin users (is_staff=True) can access."""
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        return Response({'message': 'Admin area'})


class ReadOnlyOrAuthenticatedView(APIView):
    """Anyone can read, only authenticated can modify."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        return Response({'message': 'Anyone can read this'})
    
    def post(self, request):
        return Response({'message': 'Only authenticated users can create'})
'''

print(view_level_code)

# ========== PERMISSIONS WITH VIEWSETS ==========
print("\n" + "=" * 60)
print("PERMISSIONS WITH VIEWSETS")
print("=" * 60)

viewset_code = '''
# views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint for articles.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]  # All actions require auth


class AdminArticleViewSet(viewsets.ModelViewSet):
    """
    Admin-only article management.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUser]
'''

print(viewset_code)

# ========== ACTION-LEVEL PERMISSIONS ==========
print("\n" + "=" * 60)
print("ACTION-LEVEL PERMISSIONS (Different per action)")
print("=" * 60)

action_level_code = '''
# views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Different permissions for different actions.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_permissions(self):
        """
        Return different permissions based on action.
        """
        if self.action == 'list':
            # Anyone can list articles
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            # Anyone can view a single article
            permission_classes = [AllowAny]
        elif self.action in ['create', 'update', 'partial_update']:
            # Only authenticated users can create/edit
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            # Only admins can delete
            permission_classes = [IsAdminUser]
        else:
            # Default to IsAuthenticated
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
'''

print(action_level_code)

# ========== CUSTOM PERMISSION CLASSES ==========
print("\n" + "=" * 60)
print("CUSTOM PERMISSION CLASSES")
print("=" * 60)

custom_permission_code = '''
# permissions.py

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """
    message = "You must be the owner to perform this action."
    
    def has_object_permission(self, request, view, obj):
        # obj.owner should be the user field on your model
        return obj.owner == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow anyone to read, but only owners can modify.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only to the owner
        return obj.owner == request.user


class IsPremiumUser(permissions.BasePermission):
    """
    Allow access only to premium users.
    """
    message = "This feature is only available for premium users."
    
    def has_permission(self, request, view):
        # Check if user has premium status
        # Assumes User model has is_premium field or profile with premium status
        return (
            request.user.is_authenticated and 
            getattr(request.user, 'is_premium', False)
        )


class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Allow access to authors of the content or admin users.
    """
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.author == request.user


class HasAPIKey(permissions.BasePermission):
    """
    Check for valid API key in headers.
    """
    message = "Valid API key required."
    
    def has_permission(self, request, view):
        api_key = request.headers.get('X-API-KEY')
        # In production, validate against database
        valid_keys = ['key123', 'key456']  # Example only!
        return api_key in valid_keys


class RateLimitPermission(permissions.BasePermission):
    """
    Simple rate limiting permission.
    """
    message = "Rate limit exceeded. Try again later."
    
    def has_permission(self, request, view):
        from django.core.cache import cache
        
        if not request.user.is_authenticated:
            return True  # Let throttling handle anonymous users
        
        cache_key = f"rate_limit_{request.user.id}"
        request_count = cache.get(cache_key, 0)
        
        if request_count >= 100:  # 100 requests per minute
            return False
        
        cache.set(cache_key, request_count + 1, 60)  # Expire in 60 seconds
        return True
'''

print(custom_permission_code)

# ========== USING CUSTOM PERMISSIONS ==========
print("\n" + "=" * 60)
print("USING CUSTOM PERMISSIONS")
print("=" * 60)

using_custom_code = '''
# views.py

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner, IsOwnerOrReadOnly, IsPremiumUser
from .models import Article, Profile
from .serializers import ArticleSerializer, ProfileSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Articles - only owners can edit their own articles.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    """
    Profile - only owner can view/edit their profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class PremiumContentView(generics.ListAPIView):
    """
    Premium content - only premium users can access.
    """
    queryset = Article.objects.filter(is_premium=True)
    serializer_class = ArticleSerializer
    permission_classes = [IsPremiumUser]
'''

print(using_custom_code)

# ========== COMBINING PERMISSIONS ==========
print("\n" + "=" * 60)
print("COMBINING MULTIPLE PERMISSIONS")
print("=" * 60)

combining_code = '''
# views.py

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner, IsPremiumUser


class SensitiveDataView(APIView):
    """
    Multiple permissions - ALL must pass (AND logic).
    """
    permission_classes = [IsAuthenticated, IsAdminUser]  # Must be authenticated AND admin


class MyResourceView(viewsets.ModelViewSet):
    """
    Owner check + authentication required.
    """
    permission_classes = [IsAuthenticated, IsOwner]


# For OR logic, create a custom permission:

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom OR permission - either owner OR admin.
    """
    def has_object_permission(self, request, view, obj):
        # Admin can do anything
        if request.user.is_staff:
            return True
        # Otherwise, must be owner
        return obj.owner == request.user


# Or use third-party: pip install django-rest-condition

from rest_condition import Or, And

class MyView(APIView):
    permission_classes = [Or(IsOwner, IsAdminUser)]  # Owner OR Admin
'''

print(combining_code)

# ========== OBJECT-LEVEL PERMISSIONS ==========
print("\n" + "=" * 60)
print("OBJECT-LEVEL PERMISSIONS")
print("=" * 60)

object_level_code = '''
# permissions.py

from rest_framework import permissions


class IsPostAuthor(permissions.BasePermission):
    """
    Object-level permission to only allow authors to edit their posts.
    
    has_permission() - Called for list and create
    has_object_permission() - Called for retrieve, update, delete
    """
    
    def has_permission(self, request, view):
        # Allow any authenticated user to list or create
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions only for the author
        return obj.author == request.user


# views.py

from rest_framework import generics
from .permissions import IsPostAuthor
from .models import Post
from .serializers import PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a post.
    Only the author can edit or delete.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthor]
    
    # Important: For object permissions to work with updates,
    # make sure to call self.check_object_permissions()
    # GenericAPIView does this automatically for detail views
'''

print(object_level_code)

# ========== PERMISSION DENIED CUSTOMIZATION ==========
print("\n" + "=" * 60)
print("CUSTOMIZING PERMISSION DENIED RESPONSES")
print("=" * 60)

denied_customization_code = '''
# permissions.py

from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    """
    Permission with custom error message.
    """
    message = "You don't have permission to perform this action."
    
    def has_permission(self, request, view):
        if not request.user.has_perm('app.can_access'):
            self.message = "You need the 'can_access' permission."
            return False
        return True


# For more control, create a custom exception handler:

# exceptions.py
from rest_framework.views import exception_handler
from rest_framework.exceptions import PermissionDenied

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc, PermissionDenied):
        response.data = {
            'error': 'Permission Denied',
            'detail': str(exc.detail),
            'code': 'permission_denied'
        }
    
    return response


# settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'myapp.exceptions.custom_exception_handler'
}
'''

print(denied_customization_code)

print("\n" + "=" * 60)
print("✅ Permissions - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Permissions run after authentication
2. Use built-in permissions when possible
3. Create custom permissions for specific needs
4. Use has_permission() for view-level checks
5. Use has_object_permission() for object-level checks
6. Combine permissions for complex access control

Best Practices:
--------------
- Default to IsAuthenticated globally
- Use AllowAny sparingly and explicitly
- Always validate object ownership
- Test permissions thoroughly
- Document your permission requirements

Next: Learn about Filtering and Pagination in 03_filtering_pagination.py
""")
