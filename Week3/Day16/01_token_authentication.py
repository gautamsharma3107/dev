"""
Day 16 - Token Authentication in Django REST Framework
=======================================================
Learn: Token-based authentication, JWT basics, securing API endpoints

Key Concepts:
- Token authentication is stateless and ideal for APIs
- Tokens are sent in the Authorization header
- TokenAuthentication is built into DRF
- JWT provides additional security features
"""

# ========== SETUP TOKEN AUTHENTICATION ==========
print("=" * 60)
print("TOKEN AUTHENTICATION SETUP")
print("=" * 60)

print("""
STEP 1: Install Required Packages
---------------------------------
pip install djangorestframework
pip install djangorestframework-simplejwt  # For JWT (optional)

STEP 2: Update settings.py
--------------------------
""")

settings_code = '''
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',  # Add this for token auth
    # Your apps
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Optional: for browsable API
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
'''

print(settings_code)

print("""
STEP 3: Run migrations
----------------------
python manage.py migrate

This creates the authtoken_token table in your database.
""")

# ========== CREATING TOKENS ==========
print("\n" + "=" * 60)
print("CREATING AND MANAGING TOKENS")
print("=" * 60)

print("""
Method 1: Using Django Admin
----------------------------
1. Go to /admin/
2. Navigate to "Tokens"
3. Click "Add Token"
4. Select user and save

Method 2: Using Django Shell
----------------------------
python manage.py shell
""")

shell_code = '''
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Get or create a user
user = User.objects.get(username='testuser')

# Create a token for the user
token, created = Token.objects.get_or_create(user=user)
print(f"Token: {token.key}")
'''

print(shell_code)

print("""
Method 3: Using Signals (Auto-create tokens for new users)
----------------------------------------------------------
""")

signals_code = '''
# models.py or signals.py

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Automatically create a token when a new user is created."""
    if created:
        Token.objects.create(user=instance)
'''

print(signals_code)

# ========== TOKEN LOGIN ENDPOINT ==========
print("\n" + "=" * 60)
print("TOKEN LOGIN ENDPOINT")
print("=" * 60)

print("""
Built-in Token Obtain View
--------------------------
DRF provides a built-in view to obtain tokens via POST request.
""")

urls_code = '''
# urls.py

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # ... your other urls
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
'''

print(urls_code)

print("""
Usage:
------
POST /api/token/
Content-Type: application/json

{
    "username": "testuser",
    "password": "testpassword123"
}

Response:
---------
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
""")

# ========== USING TOKENS IN REQUESTS ==========
print("\n" + "=" * 60)
print("USING TOKENS IN API REQUESTS")
print("=" * 60)

print("""
Include the token in the Authorization header:

HTTP Header Format:
-------------------
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

Example with curl:
------------------
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \\
     http://localhost:8000/api/protected/

Example with Python requests:
-----------------------------
""")

requests_code = '''
import requests

token = "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
headers = {"Authorization": f"Token {token}"}

response = requests.get(
    "http://localhost:8000/api/protected/",
    headers=headers
)
print(response.json())
'''

print(requests_code)

# ========== CUSTOM TOKEN LOGIN VIEW ==========
print("\n" + "=" * 60)
print("CUSTOM TOKEN LOGIN VIEW")
print("=" * 60)

custom_login_code = '''
# views.py

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes([AllowAny])
def custom_login(request):
    """
    Custom login endpoint that returns token and user info.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Please provide both username and password'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    if not user.is_active:
        return Response(
            {'error': 'Account is disabled'},
            status=status.HTTP_403_FORBIDDEN
        )
    
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'token': token.key,
        'user_id': user.pk,
        'username': user.username,
        'email': user.email,
    })


@api_view(['POST'])
def logout(request):
    """
    Logout endpoint - deletes the user's token.
    """
    request.user.auth_token.delete()
    return Response({'message': 'Successfully logged out'})
'''

print(custom_login_code)

# ========== TOKEN REGISTRATION VIEW ==========
print("\n" + "=" * 60)
print("REGISTRATION WITH TOKEN")
print("=" * 60)

registration_code = '''
# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user': {
                'id': user.pk,
                'username': user.username,
                'email': user.email,
            },
            'message': 'User registered successfully'
        })
'''

print(registration_code)

# ========== JWT AUTHENTICATION (ADVANCED) ==========
print("\n" + "=" * 60)
print("JWT AUTHENTICATION (ADVANCED)")
print("=" * 60)

print("""
JWT (JSON Web Tokens) provides additional features:
- Token expiration
- Refresh tokens
- Token blacklisting
- Better security

Installation:
-------------
pip install djangorestframework-simplejwt
""")

jwt_settings_code = '''
# settings.py

from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
'''

print(jwt_settings_code)

jwt_urls_code = '''
# urls.py

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
'''

print(jwt_urls_code)

print("""
JWT Usage:
----------
1. Obtain tokens: POST /api/token/ with username/password
   Returns: {"access": "...", "refresh": "..."}

2. Use access token: 
   Authorization: Bearer <access_token>

3. Refresh token when access expires: POST /api/token/refresh/
   Body: {"refresh": "<refresh_token>"}

4. Verify token: POST /api/token/verify/
   Body: {"token": "<token>"}
""")

# ========== PROTECTED VIEW EXAMPLE ==========
print("\n" + "=" * 60)
print("PROTECTED VIEW EXAMPLE")
print("=" * 60)

protected_view_code = '''
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    """
    This view requires authentication.
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({
            'message': 'Hello, authenticated user!',
            'user': {
                'id': request.user.id,
                'username': request.user.username,
                'email': request.user.email,
            }
        })


class PublicView(APIView):
    """
    This view is accessible without authentication.
    """
    permission_classes = []  # Or use AllowAny
    
    def get(self, request):
        return Response({
            'message': 'This endpoint is public!',
        })
'''

print(protected_view_code)

print("\n" + "=" * 60)
print("✅ Token Authentication - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. TokenAuthentication is stateless and ideal for APIs
2. Tokens should be stored securely on the client
3. Always use HTTPS in production
4. Consider JWT for additional features like expiration
5. Create registration and login endpoints for your API

Next: Learn about Permissions in 02_permissions.py
""")
