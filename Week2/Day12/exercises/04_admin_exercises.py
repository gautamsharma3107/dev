"""
EXERCISES: Django Admin
========================
Complete all exercises below to practice Django admin customization.
"""

# Exercise 1: Basic Admin Registration
# TODO: Register models in admin

print("Exercise 1: Basic Admin Registration")
print("-" * 40)

print("""
Given these models, write the admin.py code to register them:

# models.py
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

Write your admin.py code:
_______________________
""")


# Exercise 2: List Display Customization
# TODO: Customize the list view

print("\n\nExercise 2: List Display Customization")
print("-" * 40)

print("""
For the Book model, create a BookAdmin with:
- Display columns: title, author, price, published_date
- Filter by: published_date, author
- Search by: title, author__name
- Order by: -published_date
- Show 20 items per page
- Add date hierarchy on published_date

Write your BookAdmin code:
_______________________
""")


# Exercise 3: Fieldsets and Edit View
# TODO: Organize edit form with fieldsets

print("\n\nExercise 3: Fieldsets and Edit View")
print("-" * 40)

print("""
For an Article model, create fieldsets:
- "Basic Info" section: title, slug (prepopulated from title)
- "Content" section: summary, body (wide style)
- "Publishing" section: status, publish_date (collapsible)
- "Metadata" section: created_at, updated_at (read-only, collapsible)

Write the fieldsets configuration:
_______________________
""")


# Exercise 4: Custom Admin Actions
# TODO: Create custom admin actions

print("\n\nExercise 4: Custom Admin Actions")
print("-" * 40)

print("""
Create two custom actions for Post model:
1. 'archive_posts' - Set status to 'archived' for selected posts
2. 'feature_posts' - Set is_featured to True for selected posts

Write the action methods:
_______________________
""")


# Exercise 5: Inline Admin
# TODO: Set up inline editing

print("\n\nExercise 5: Inline Admin")
print("-" * 40)

print("""
Given these models:
- Order (customer_name, total_amount, created_at)
- OrderItem (order, product_name, quantity, price)

Create admin configuration so OrderItems can be edited 
directly on the Order edit page using TabularInline.

Write your code:
_______________________
""")


# Exercise 6: Custom Methods in List Display
# TODO: Add custom display methods

print("\n\nExercise 6: Custom Display Methods")
print("-" * 40)

print("""
For a Product model with: name, price, cost, is_active

Add custom columns to list_display:
1. 'profit_margin' - Calculate (price - cost) / price * 100
2. 'status_icon' - Show ✓ if active, ✗ if inactive (use format_html)

Write the custom methods:
_______________________
""")


# ========== ANSWERS ==========

print("\n\n" + "=" * 60)
print("ANSWERS (Check after attempting)")
print("=" * 60)

ANSWERS = '''
Exercise 1:
from django.contrib import admin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)

# OR with decorators:
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


Exercise 2:
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'published_date']
    list_filter = ['published_date', 'author']
    search_fields = ['title', 'author__name']
    ordering = ['-published_date']
    list_per_page = 20
    date_hierarchy = 'published_date'


Exercise 3:
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug')
        }),
        ('Content', {
            'fields': ('summary', 'body'),
            'classes': ('wide',)
        }),
        ('Publishing', {
            'fields': ('status', 'publish_date'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


Exercise 4:
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ['archive_posts', 'feature_posts']
    
    @admin.action(description='Archive selected posts')
    def archive_posts(self, request, queryset):
        count = queryset.update(status='archived')
        self.message_user(request, f'{count} posts archived.')
    
    @admin.action(description='Feature selected posts')
    def feature_posts(self, request, queryset):
        count = queryset.update(is_featured=True)
        self.message_user(request, f'{count} posts featured.')


Exercise 5:
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'total_amount', 'created_at']
    inlines = [OrderItemInline]


Exercise 6:
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'cost', 'profit_margin', 'status_icon']
    
    def profit_margin(self, obj):
        if obj.price > 0:
            margin = (obj.price - obj.cost) / obj.price * 100
            return f"{margin:.1f}%"
        return "N/A"
    profit_margin.short_description = 'Margin'
    
    def status_icon(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green;">✓</span>')
        return format_html('<span style="color: red;">✗</span>')
    status_icon.short_description = 'Active'
'''

print(ANSWERS)
