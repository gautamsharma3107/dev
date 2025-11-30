# Day 16 Quick Reference Cheat Sheet

## Token Authentication

```python
# settings.py
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# urls.py
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/token/', obtain_auth_token),
]

# Create token
from rest_framework.authtoken.models import Token
token, created = Token.objects.get_or_create(user=user)

# Use token in requests
# Header: Authorization: Token 9944b09199c62bcf...
```

## Permissions

```python
from rest_framework.permissions import (
    AllowAny,              # Anyone
    IsAuthenticated,       # Logged in users
    IsAdminUser,           # Staff users only
    IsAuthenticatedOrReadOnly,  # Logged in or read-only
)

# View-level permissions
class MyView(APIView):
    permission_classes = [IsAuthenticated]

# Custom permission
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

# Action-level permissions
def get_permissions(self):
    if self.action == 'list':
        return [AllowAny()]
    return [IsAuthenticated()]
```

## Filtering

```python
# Install: pip install django-filter

# settings.py
INSTALLED_APPS = ['django_filters']

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# views.py
class ArticleViewSet(viewsets.ModelViewSet):
    filterset_fields = ['category', 'status']  # ?category=tech
    search_fields = ['title', 'content']       # ?search=django
    ordering_fields = ['created_at', 'views']  # ?ordering=-views
    ordering = ['-created_at']                 # Default ordering
```

## Custom FilterSet

```python
import django_filters

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    min_views = django_filters.NumberFilter(field_name='views', lookup_expr='gte')
    max_views = django_filters.NumberFilter(field_name='views', lookup_expr='lte')
    
    class Meta:
        model = Article
        fields = ['category', 'title', 'min_views', 'max_views']
```

## Pagination

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Custom pagination
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Usage: ?page=2&page_size=20
```

## Pagination Types

```python
# PageNumberPagination - ?page=2
# LimitOffsetPagination - ?limit=10&offset=20
# CursorPagination - ?cursor=cD0yMDI...

# Disable pagination
class MyViewSet(viewsets.ModelViewSet):
    pagination_class = None
```

## API Documentation (drf-spectacular)

```python
# Install: pip install drf-spectacular

# settings.py
INSTALLED_APPS = ['drf_spectacular']

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'VERSION': '1.0.0',
}

# urls.py
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema')),
]
```

## Documenting Views

```python
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

@extend_schema(
    summary="List articles",
    description="Returns paginated articles",
    parameters=[
        OpenApiParameter(name='category', type=str, description='Filter by category'),
    ],
    examples=[
        OpenApiExample(name='Example', value={'title': 'Hello'}),
    ],
    tags=['Articles'],
)
def list(self, request):
    pass

# Exclude from docs
@extend_schema(exclude=True)
class InternalView(APIView):
    pass
```

## JWT Authentication

```python
# Install: pip install djangorestframework-simplejwt

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

# Header: Authorization: Bearer <access_token>
```

## Common Patterns

```python
# Owner-only access
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

# Multiple filters combined
# GET /api/articles/?category=tech&search=python&ordering=-views&page=2

# Custom pagination response
def get_paginated_response(self, data):
    return Response({
        'count': self.page.paginator.count,
        'results': data
    })
```

## Quick Commands

```bash
# Generate schema
python manage.py spectacular --file schema.yml

# Validate schema
python manage.py spectacular --validate

# Create token for user
python manage.py drf_create_token <username>
```

---
**Keep this handy for quick reference!** 🔐🚀
