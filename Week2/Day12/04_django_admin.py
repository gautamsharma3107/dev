"""
Day 12 - Django Admin Setup
============================
Learn: Setting up and customizing Django admin interface

Key Concepts:
- Django admin provides a ready-to-use admin interface
- Register models to make them manageable through admin
- Customize admin display, filters, and search
"""

# ========== DJANGO ADMIN ==========

print("=" * 60)
print("DJANGO ADMIN SETUP")
print("=" * 60)

print("""
WHAT IS DJANGO ADMIN?
====================
Django comes with a powerful admin interface that lets you:
- View, add, edit, and delete model data
- Search and filter records
- Manage users and permissions

It's automatically generated from your models!

SETUP STEPS:
1. Ensure 'django.contrib.admin' is in INSTALLED_APPS
2. Run migrations: python manage.py migrate
3. Create superuser: python manage.py createsuperuser
4. Register your models in admin.py
5. Access at: http://localhost:8000/admin/
""")

# ========== BASIC ADMIN REGISTRATION ==========

print("\n" + "=" * 60)
print("BASIC ADMIN REGISTRATION")
print("=" * 60)

BASIC_ADMIN = '''
# blog/admin.py

from django.contrib import admin
from .models import Post, Category, Tag, Comment


# Method 1: Simple registration
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)


# Method 2: Using decorator (preferred)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
'''

print(BASIC_ADMIN)

# ========== CUSTOMIZING MODEL ADMIN ==========

print("\n" + "=" * 60)
print("CUSTOMIZING MODEL ADMIN")
print("=" * 60)

CUSTOM_ADMIN = '''
# blog/admin.py - Full customization example

from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model"""
    
    # List display - columns shown in list view
    list_display = ['name', 'slug', 'post_count']
    
    # Make fields editable directly in list view
    list_editable = ['slug']
    
    # Search fields
    search_fields = ['name', 'description']
    
    # Auto-populate slug from name
    prepopulated_fields = {'slug': ('name',)}
    
    # Order of fields in edit form
    fields = ['name', 'slug', 'description']
    
    # Custom method to show post count
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Number of Posts'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'post_count']
    search_fields = ['name']
    
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Posts'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin configuration for Post model"""
    
    # ===== LIST VIEW SETTINGS =====
    
    # Columns in list view
    list_display = [
        'title', 
        'author', 
        'category', 
        'is_published',
        'views',
        'created_at',
        'status_badge'
    ]
    
    # Filters in sidebar
    list_filter = [
        'is_published', 
        'created_at', 
        'category',
        'author'
    ]
    
    # Search functionality
    search_fields = ['title', 'content', 'author__username']
    
    # Clickable fields (link to edit page)
    list_display_links = ['title']
    
    # Editable fields in list view
    list_editable = ['is_published']
    
    # Default ordering
    ordering = ['-created_at']
    
    # Items per page
    list_per_page = 25
    
    # Date hierarchy navigation
    date_hierarchy = 'created_at'
    
    # ===== EDIT VIEW SETTINGS =====
    
    # Auto-populate slug
    prepopulated_fields = {'slug': ('title',)}
    
    # Raw ID widget for ForeignKey (faster for many users)
    raw_id_fields = ['author']
    
    # Filter horizontal for ManyToMany
    filter_horizontal = ['tags']
    # OR use filter_vertical = ['tags']
    
    # Read-only fields
    readonly_fields = ['created_at', 'updated_at', 'views']
    
    # Organize fields into fieldsets
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Content', {
            'fields': ('content', 'excerpt'),
            'classes': ('wide',)  # CSS classes
        }),
        ('Taxonomy', {
            'fields': ('tags',),
            'classes': ('collapse',)  # Collapsible section
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_date'),
        }),
        ('Metadata', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # ===== CUSTOM METHODS =====
    
    def status_badge(self, obj):
        """Show colored status badge"""
        if obj.is_published:
            color = 'green'
            text = 'Published'
        else:
            color = 'orange'
            text = 'Draft'
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 10px; '
            'border-radius: 3px;">{}</span>',
            color, text
        )
    status_badge.short_description = 'Status'
    
    # ===== CUSTOM ACTIONS =====
    
    actions = ['make_published', 'make_draft']
    
    @admin.action(description='Mark selected posts as published')
    def make_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'{count} posts marked as published.')
    
    @admin.action(description='Mark selected posts as draft')
    def make_draft(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'{count} posts marked as draft.')
    
    # ===== AUTO-SET AUTHOR =====
    
    def save_model(self, request, obj, form, change):
        """Auto-set author to current user for new posts"""
        if not change:  # New object
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'post', 'created_at', 'is_approved']
    list_filter = ['is_approved', 'created_at']
    list_editable = ['is_approved']
    search_fields = ['author_name', 'email', 'content']
    readonly_fields = ['created_at']
    
    actions = ['approve_comments', 'reject_comments']
    
    @admin.action(description='Approve selected comments')
    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    
    @admin.action(description='Reject selected comments')
    def reject_comments(self, request, queryset):
        queryset.update(is_approved=False)
'''

print(CUSTOM_ADMIN)

# ========== INLINE ADMIN ==========

print("\n" + "=" * 60)
print("INLINE ADMIN (Edit Related Objects)")
print("=" * 60)

INLINE_ADMIN = '''
# blog/admin.py - Inline admin

from django.contrib import admin
from .models import Post, Comment, Category


# Tabular inline (horizontal layout)
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Number of empty forms to display
    readonly_fields = ['created_at']
    fields = ['author_name', 'email', 'content', 'is_approved', 'created_at']


# Stacked inline (vertical layout)
class CommentStackedInline(admin.StackedInline):
    model = Comment
    extra = 0
    readonly_fields = ['created_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    
    # Add inline to edit comments directly from post page
    inlines = [CommentInline]


# For ManyToMany through table
class PostInline(admin.TabularInline):
    model = Post.tags.through  # Through model
    extra = 0
'''

print(INLINE_ADMIN)

# ========== CUSTOMIZING ADMIN SITE ==========

print("\n" + "=" * 60)
print("CUSTOMIZING ADMIN SITE")
print("=" * 60)

CUSTOMIZE_SITE = '''
# blog/admin.py or project/admin.py

from django.contrib import admin

# Customize admin site header and title
admin.site.site_header = "My Blog Administration"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to Blog Admin"


# Custom admin site (advanced)
class MyAdminSite(admin.AdminSite):
    site_header = "Custom Admin"
    site_title = "Custom Admin Portal"
    index_title = "Dashboard"
    
    def get_app_list(self, request, app_label=None):
        """Customize the order of apps in admin"""
        app_list = super().get_app_list(request, app_label)
        # Custom ordering logic here
        return app_list


# In urls.py, use custom admin
# admin_site = MyAdminSite(name='myadmin')
# urlpatterns = [
#     path('admin/', admin_site.urls),
# ]
'''

print(CUSTOMIZE_SITE)

# ========== ADMIN PERMISSIONS ==========

print("\n" + "=" * 60)
print("ADMIN PERMISSIONS")
print("=" * 60)

print("""
DJANGO ADMIN PERMISSIONS:
=========================

1. Superuser (is_superuser=True)
   - Full access to everything

2. Staff (is_staff=True)
   - Can access admin site
   - Permissions control what they can do

3. Model Permissions (per model):
   - add: Can add new objects
   - change: Can edit existing objects
   - delete: Can delete objects
   - view: Can view objects (read-only)

CUSTOMIZING PERMISSIONS IN ADMIN:
""")

PERMISSIONS_CODE = '''
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        """Control who can add posts"""
        return request.user.is_superuser or request.user.groups.filter(name='Editors').exists()
    
    def has_change_permission(self, request, obj=None):
        """Control who can edit posts"""
        if obj is None:
            return True
        # Only author or superuser can edit
        return obj.author == request.user or request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        """Control who can delete posts"""
        return request.user.is_superuser
    
    def has_view_permission(self, request, obj=None):
        """Control who can view posts"""
        return True  # Everyone with admin access can view
    
    def get_queryset(self, request):
        """Filter queryset based on user"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Non-superusers only see their own posts
        return qs.filter(author=request.user)
'''

print(PERMISSIONS_CODE)

# ========== COMMANDS ==========

print("\n" + "=" * 60)
print("ESSENTIAL COMMANDS")
print("=" * 60)

print("""
# Create superuser (admin account)
python manage.py createsuperuser

# Create user from shell
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_superuser('admin', 'admin@example.com', 'password123')

# Change password
python manage.py changepassword username

# Access admin site
http://localhost:8000/admin/
""")

print("\n" + "=" * 60)
print("✅ Django Admin Setup - Complete!")
print("=" * 60)
