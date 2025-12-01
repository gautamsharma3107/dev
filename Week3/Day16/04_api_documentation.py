"""
Day 16 - API Documentation in Django REST Framework
===================================================
Learn: drf-spectacular, OpenAPI schema, Swagger UI, ReDoc

Key Concepts:
- API documentation is essential for API consumers
- OpenAPI (Swagger) is the standard for REST API documentation
- drf-spectacular generates documentation from your code
- Good documentation includes examples, descriptions, and schema
"""

# ========== WHY API DOCUMENTATION? ==========
print("=" * 60)
print("WHY API DOCUMENTATION?")
print("=" * 60)

print("""
Benefits of Good API Documentation:
-----------------------------------
1. Helps developers understand your API
2. Reduces support requests
3. Enables faster integration
4. Serves as a contract between frontend and backend
5. Auto-generates client SDKs
6. Provides interactive testing interface

Popular Documentation Tools:
---------------------------
- drf-spectacular (Recommended for DRF)
- drf-yasg (Older, but still used)
- Built-in DRF browsable API
- Swagger/OpenAPI
- ReDoc
""")

# ========== SETUP DRF-SPECTACULAR ==========
print("\n" + "=" * 60)
print("SETUP DRF-SPECTACULAR")
print("=" * 60)

setup_code = '''
# Installation
# ------------
pip install drf-spectacular

# settings.py
# -----------
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'drf_spectacular',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'A comprehensive API for my application',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    
    # Additional settings
    'CONTACT': {
        'name': 'API Support',
        'email': 'support@example.com',
    },
    'LICENSE': {
        'name': 'MIT License',
    },
    
    # Authentication
    'SECURITY': [
        {'TokenAuth': []},
    ],
    
    # Tags for organizing endpoints
    'TAGS': [
        {'name': 'Auth', 'description': 'Authentication endpoints'},
        {'name': 'Users', 'description': 'User management'},
        {'name': 'Articles', 'description': 'Article operations'},
    ],
    
    # Swagger UI settings
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': True,
    },
}
'''

print(setup_code)

# ========== URL CONFIGURATION ==========
print("\n" + "=" * 60)
print("URL CONFIGURATION")
print("=" * 60)

urls_code = '''
# urls.py

from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # API endpoints
    path('api/', include('myapp.urls')),
    
    # Documentation endpoints
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # ReDoc (alternative documentation UI)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# Now visit:
# /api/docs/   - Swagger UI interface
# /api/redoc/  - ReDoc interface
# /api/schema/ - Raw OpenAPI schema (JSON/YAML)
'''

print(urls_code)

# ========== DOCUMENTING VIEWS ==========
print("\n" + "=" * 60)
print("DOCUMENTING VIEWS")
print("=" * 60)

documenting_views_code = '''
# views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse,
)
from drf_spectacular.types import OpenApiTypes
from .models import Article
from .serializers import ArticleSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all articles",
        description="Returns a paginated list of all articles.",
        tags=['Articles'],
    ),
    create=extend_schema(
        summary="Create a new article",
        description="Create a new article. Requires authentication.",
        tags=['Articles'],
    ),
    retrieve=extend_schema(
        summary="Get article details",
        description="Returns detailed information about a specific article.",
        tags=['Articles'],
    ),
    update=extend_schema(
        summary="Update an article",
        description="Update all fields of an existing article.",
        tags=['Articles'],
    ),
    partial_update=extend_schema(
        summary="Partially update an article",
        description="Update specific fields of an existing article.",
        tags=['Articles'],
    ),
    destroy=extend_schema(
        summary="Delete an article",
        description="Permanently delete an article.",
        tags=['Articles'],
    ),
)
class ArticleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing articles.
    
    Provides CRUD operations for Article model.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    @extend_schema(
        summary="Publish an article",
        description="Change article status to published.",
        request=None,
        responses={
            200: ArticleSerializer,
            404: OpenApiResponse(description="Article not found"),
        },
        tags=['Articles'],
    )
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.status = 'published'
        article.save()
        return Response(ArticleSerializer(article).data)
'''

print(documenting_views_code)

# ========== DOCUMENTING PARAMETERS ==========
print("\n" + "=" * 60)
print("DOCUMENTING QUERY PARAMETERS")
print("=" * 60)

parameters_code = '''
# views.py

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='category',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter by category',
                required=False,
                enum=['tech', 'science', 'sports', 'entertainment'],
            ),
            OpenApiParameter(
                name='status',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter by status',
                required=False,
                enum=['draft', 'published', 'archived'],
            ),
            OpenApiParameter(
                name='search',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Search in title and content',
                required=False,
            ),
            OpenApiParameter(
                name='ordering',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Order results. Prefix with - for descending.',
                required=False,
                enum=['created_at', '-created_at', 'title', '-title', 'views', '-views'],
            ),
            OpenApiParameter(
                name='page',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Page number',
                required=False,
            ),
            OpenApiParameter(
                name='page_size',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Number of results per page (max 100)',
                required=False,
            ),
        ],
        summary="List articles with filtering",
        tags=['Articles'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
'''

print(parameters_code)

# ========== DOCUMENTING REQUEST/RESPONSE EXAMPLES ==========
print("\n" + "=" * 60)
print("REQUEST/RESPONSE EXAMPLES")
print("=" * 60)

examples_code = '''
# views.py

from drf_spectacular.utils import extend_schema, OpenApiExample


class ArticleViewSet(viewsets.ModelViewSet):
    
    @extend_schema(
        summary="Create a new article",
        examples=[
            OpenApiExample(
                name="Create Tech Article",
                description="Example of creating a technology article",
                value={
                    "title": "Introduction to Django REST Framework",
                    "content": "Django REST Framework is a powerful toolkit...",
                    "category": "tech",
                    "is_featured": False,
                },
                request_only=True,
            ),
            OpenApiExample(
                name="Successful Creation",
                description="Response after successful article creation",
                value={
                    "id": 1,
                    "title": "Introduction to Django REST Framework",
                    "content": "Django REST Framework is a powerful toolkit...",
                    "category": "tech",
                    "status": "draft",
                    "is_featured": False,
                    "created_at": "2024-01-15T10:30:00Z",
                    "author": {
                        "id": 1,
                        "username": "john_doe"
                    }
                },
                response_only=True,
                status_codes=['201'],
            ),
        ],
        tags=['Articles'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
'''

print(examples_code)

# ========== DOCUMENTING SERIALIZERS ==========
print("\n" + "=" * 60)
print("DOCUMENTING SERIALIZERS")
print("=" * 60)

serializer_code = '''
# serializers.py

from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import Article, User


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for article author information."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for Article model.
    
    Handles creation and display of articles with all related information.
    """
    author = AuthorSerializer(read_only=True)
    
    word_count = serializers.SerializerMethodField(
        help_text="Number of words in the content"
    )
    
    reading_time = serializers.SerializerMethodField(
        help_text="Estimated reading time in minutes"
    )
    
    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content', 'category', 'status',
            'is_featured', 'views', 'author', 'word_count',
            'reading_time', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'views', 'author', 'created_at', 'updated_at']
        extra_kwargs = {
            'title': {
                'help_text': 'Article title (max 200 characters)',
                'min_length': 5,
            },
            'content': {
                'help_text': 'Full article content in markdown format',
            },
            'category': {
                'help_text': 'Article category (tech, science, sports, etc.)',
            },
        }
    
    @extend_schema_field(OpenApiTypes.INT)
    def get_word_count(self, obj):
        """Calculate the number of words in the content."""
        return len(obj.content.split())
    
    @extend_schema_field(OpenApiTypes.INT)
    def get_reading_time(self, obj):
        """Estimate reading time (average 200 words per minute)."""
        words = len(obj.content.split())
        return max(1, words // 200)


class ArticleCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating articles.
    Separate from display serializer for cleaner documentation.
    """
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'is_featured']
'''

print(serializer_code)

# ========== AUTHENTICATION DOCUMENTATION ==========
print("\n" + "=" * 60)
print("DOCUMENTING AUTHENTICATION")
print("=" * 60)

auth_doc_code = '''
# settings.py

SPECTACULAR_SETTINGS = {
    # ... other settings ...
    
    # Define security schemes
    'SECURITY': [
        {'TokenAuth': []},
    ],
    
    'COMPONENTS': {
        'securitySchemes': {
            'TokenAuth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization',
                'description': 'Token-based authentication. Format: Token <your_token>'
            },
            'BearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT',
                'description': 'JWT authentication'
            },
        }
    },
}


# views.py - Specify authentication per view

from drf_spectacular.utils import extend_schema


class PublicView(APIView):
    """Public endpoint - no authentication required."""
    
    @extend_schema(
        security=[],  # No security required
        tags=['Public'],
    )
    def get(self, request):
        return Response({'message': 'Public endpoint'})


class ProtectedView(APIView):
    """Protected endpoint - requires token authentication."""
    
    @extend_schema(
        security=[{'TokenAuth': []}],
        tags=['Protected'],
    )
    def get(self, request):
        return Response({'message': 'Protected endpoint'})
'''

print(auth_doc_code)

# ========== CUSTOM SCHEMA GENERATION ==========
print("\n" + "=" * 60)
print("CUSTOM SCHEMA GENERATION")
print("=" * 60)

custom_schema_code = '''
# schema.py

from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import extend_schema


class CustomSchemaExtension(OpenApiViewExtension):
    """
    Custom extension to modify schema generation.
    """
    target_class = 'myapp.views.SpecialView'
    
    def view_replacement(self):
        class Fixed(self.target_class):
            @extend_schema(
                operation_id='special_operation',
                description='Custom description',
            )
            def get(self, request):
                return super().get(request)
        return Fixed


# For function-based views

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view


@extend_schema(
    summary="Get current user",
    description="Returns the currently authenticated user's information.",
    responses={
        200: UserSerializer,
        401: OpenApiResponse(description="Not authenticated"),
    },
    tags=['Users'],
)
@api_view(['GET'])
def get_current_user(request):
    """Get the current authenticated user."""
    return Response(UserSerializer(request.user).data)


# Excluding views from documentation

@extend_schema(exclude=True)
class InternalView(APIView):
    """This view won't appear in documentation."""
    pass


# Deprecating endpoints

@extend_schema(
    deprecated=True,
    summary="Old endpoint (deprecated)",
    description="This endpoint is deprecated. Use /api/v2/articles/ instead.",
)
class OldArticleView(APIView):
    pass
'''

print(custom_schema_code)

# ========== GENERATING SCHEMA FILES ==========
print("\n" + "=" * 60)
print("GENERATING SCHEMA FILES")
print("=" * 60)

print("""
Generate OpenAPI Schema:
------------------------
# Generate YAML schema
python manage.py spectacular --file schema.yml

# Generate JSON schema  
python manage.py spectacular --file schema.json --format json

# Validate schema
python manage.py spectacular --validate

Using Generated Schema:
-----------------------
1. Import into Postman for testing
2. Generate client SDKs (using openapi-generator)
3. Use for API contract testing
4. Share with frontend developers
""")

# ========== ERROR RESPONSE DOCUMENTATION ==========
print("\n" + "=" * 60)
print("ERROR RESPONSE DOCUMENTATION")
print("=" * 60)

error_doc_code = '''
# serializers.py

from rest_framework import serializers


class ErrorResponseSerializer(serializers.Serializer):
    """Standard error response format."""
    error = serializers.CharField(help_text="Error type")
    detail = serializers.CharField(help_text="Detailed error message")
    code = serializers.CharField(help_text="Error code for programmatic handling")


class ValidationErrorSerializer(serializers.Serializer):
    """Validation error response format."""
    field_name = serializers.ListField(
        child=serializers.CharField(),
        help_text="List of validation errors for this field"
    )


# views.py

from drf_spectacular.utils import extend_schema, OpenApiResponse


class ArticleViewSet(viewsets.ModelViewSet):
    
    @extend_schema(
        responses={
            200: ArticleSerializer,
            400: ValidationErrorSerializer,
            401: ErrorResponseSerializer,
            403: ErrorResponseSerializer,
            404: ErrorResponseSerializer,
            500: ErrorResponseSerializer,
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
'''

print(error_doc_code)

# ========== VERSIONING DOCUMENTATION ==========
print("\n" + "=" * 60)
print("API VERSIONING IN DOCUMENTATION")
print("=" * 60)

versioning_code = '''
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
    'DEFAULT_VERSION': 'v1',
}

# urls.py

urlpatterns = [
    path('api/v1/', include('myapp.urls_v1')),
    path('api/v2/', include('myapp.urls_v2')),
    
    # Separate docs for each version
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema-v1')),
    path('api/v2/docs/', SpectacularSwaggerView.as_view(url_name='schema-v2')),
]


# Or use tags to separate versions in one doc

@extend_schema(tags=['Articles v1'])
class ArticleViewSetV1(viewsets.ModelViewSet):
    pass


@extend_schema(tags=['Articles v2'])
class ArticleViewSetV2(viewsets.ModelViewSet):
    pass
'''

print(versioning_code)

print("\n" + "=" * 60)
print("✅ API Documentation - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. drf-spectacular is the recommended documentation tool
2. Use @extend_schema to customize documentation
3. Document parameters, examples, and responses
4. Set up Swagger UI and ReDoc endpoints
5. Generate schema files for sharing

Best Practices:
--------------
1. Write clear descriptions for all endpoints
2. Include request/response examples
3. Document all query parameters
4. Show error responses
5. Keep documentation updated with code changes
6. Use tags to organize endpoints

Documentation URLs:
------------------
/api/docs/   - Swagger UI (interactive testing)
/api/redoc/  - ReDoc (clean documentation)
/api/schema/ - Raw OpenAPI schema

Congratulations! You've completed Day 16! 🎉
""")
