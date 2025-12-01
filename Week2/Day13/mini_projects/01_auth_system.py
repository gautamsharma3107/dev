"""
MINI PROJECT 1: User Authentication System
==========================================
Build a complete user authentication system for any web application.

Requirements:
1. User Registration with email verification concept
2. Login with remember me functionality
3. Logout with confirmation
4. Password reset flow
5. User profile page
6. Account settings (change email, password)

This project focuses on authentication only (no models required).
"""

print("=" * 60)
print("MINI PROJECT: USER AUTHENTICATION SYSTEM")
print("=" * 60)

PROJECT_STRUCTURE = '''
Create the following file structure:

auth_project/
├── auth_project/
│   ├── settings.py
│   └── urls.py
├── accounts/
│   ├── forms.py      # Custom forms
│   ├── views.py      # Custom views
│   ├── urls.py       # URL patterns
│   └── templates/
│       └── registration/
│           ├── login.html
│           ├── logout.html
│           ├── register.html
│           ├── profile.html
│           ├── settings.html
│           ├── password_reset.html
│           ├── password_reset_done.html
│           ├── password_reset_confirm.html
│           └── password_reset_complete.html
└── templates/
    └── base.html
'''

print(PROJECT_STRUCTURE)

print("\n" + "=" * 60)
print("IMPLEMENTATION GUIDE")
print("=" * 60)

print("""
Step 1: Create forms.py
- CustomUserCreationForm (with email)
- UserProfileForm (for profile updates)
- UserSettingsForm (for email/password changes)

Step 2: Create views.py
- register_view
- login_view (custom)
- logout_view (with confirmation)
- profile_view
- settings_view (change email/password)

Step 3: Create urls.py
- /register/
- /login/
- /logout/
- /profile/
- /settings/
- /password-reset/ (and related URLs)

Step 4: Create templates
- base.html with navigation
- All registration templates

Step 5: Configure settings.py
- LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
- EMAIL_BACKEND (for development)
""")

print("\n" + "=" * 60)
print("BONUS CHALLENGES")
print("=" * 60)

print("""
1. Add "Remember Me" checkbox to login form
2. Add email verification on registration
3. Add social login buttons (UI only)
4. Add account deletion functionality
5. Add login attempt limiting (basic)
6. Add two-factor authentication concept
""")

print("\n" + "=" * 60)
print("START CODING BELOW")
print("=" * 60)

# TODO: Implement your authentication system here
