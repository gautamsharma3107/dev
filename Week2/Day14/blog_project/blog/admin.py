from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin configuration for Post model."""
    list_display = ['title', 'author', 'date_posted', 'date_updated']
    list_filter = ['date_posted', 'author']
    search_fields = ['title', 'content']
    date_hierarchy = 'date_posted'
