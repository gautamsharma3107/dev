"""
MINI PROJECT 1: E-commerce Product Catalog
===========================================
Build a product catalog system with categories and reviews.

Requirements:
1. Create models for: Category, Product, Review
2. Products belong to categories
3. Products can have multiple reviews
4. Set up admin to manage all models
5. Practice ORM queries

Follow the step-by-step instructions below.
"""

print("=" * 60)
print("MINI PROJECT: E-commerce Product Catalog")
print("=" * 60)

# ========== STEP 1: PROJECT SETUP ==========

print("""
STEP 1: PROJECT SETUP
=====================

1. Create a new Django project:
   django-admin startproject ecommerce
   cd ecommerce

2. Create the shop app:
   python manage.py startapp shop

3. Add 'shop' to INSTALLED_APPS in settings.py
""")

# ========== STEP 2: CREATE MODELS ==========

print("""
STEP 2: CREATE MODELS
=====================

Create these models in shop/models.py:
""")

MODELS_CODE = '''
# shop/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """Product category"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    @property
    def product_count(self):
        return self.products.count()


class Product(models.Model):
    """Product in the catalog"""
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    sku = models.CharField(max_length=50, unique=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        return self.stock > 0
    
    @property
    def current_price(self):
        if self.discount_price:
            return self.discount_price
        return self.price
    
    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum(r.rating for r in reviews) / len(reviews)
        return 0


class Review(models.Model):
    """Product review"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.reviewer_name} - {self.product.name} ({self.rating}★)'
'''

print(MODELS_CODE)

# ========== STEP 3: CREATE ADMIN ==========

print("""
STEP 3: SET UP ADMIN
====================

Create admin configuration in shop/admin.py:
""")

ADMIN_CODE = '''
# shop/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_count', 'is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products'


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ['created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'price', 'stock', 
        'is_in_stock_display', 'is_active', 'is_featured'
    ]
    list_filter = ['category', 'is_active', 'is_featured', 'created_at']
    list_editable = ['is_active', 'is_featured']
    search_fields = ['name', 'sku', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 25
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'category', 'sku')
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price')
        }),
        ('Inventory', {
            'fields': ('stock',)
        }),
        ('Details', {
            'fields': ('description', 'image_url'),
            'classes': ('wide',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ReviewInline]
    
    actions = ['make_featured', 'remove_featured']
    
    def is_in_stock_display(self, obj):
        if obj.is_in_stock:
            return format_html('<span style="color: green;">✓ In Stock</span>')
        return format_html('<span style="color: red;">✗ Out of Stock</span>')
    is_in_stock_display.short_description = 'Stock Status'
    
    @admin.action(description='Mark as featured')
    def make_featured(self, request, queryset):
        queryset.update(is_featured=True)
    
    @admin.action(description='Remove from featured')
    def remove_featured(self, request, queryset):
        queryset.update(is_featured=False)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'reviewer_name', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    list_editable = ['is_approved']
    search_fields = ['reviewer_name', 'reviewer_email', 'content']
    readonly_fields = ['created_at']
    
    actions = ['approve_reviews']
    
    @admin.action(description='Approve selected reviews')
    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)


# Customize admin site
admin.site.site_header = "E-commerce Admin"
admin.site.site_title = "Shop Admin"
admin.site.index_title = "Product Catalog Management"
'''

print(ADMIN_CODE)

# ========== STEP 4: PRACTICE ORM QUERIES ==========

print("""
STEP 4: PRACTICE ORM QUERIES
============================

After setup, run: python manage.py shell

Practice these queries:
""")

ORM_PRACTICE = '''
# Import models
from shop.models import Category, Product, Review

# Create sample data
electronics = Category.objects.create(name='Electronics', slug='electronics')
clothing = Category.objects.create(name='Clothing', slug='clothing')

Product.objects.create(
    category=electronics,
    name='Laptop',
    slug='laptop',
    description='A powerful laptop',
    price=999.99,
    sku='LAP001',
    stock=10
)

# Query examples to practice:

# 1. Get all active products
Product.objects.filter(is_active=True)

# 2. Get products under $100
Product.objects.filter(price__lt=100)

# 3. Get products with discount
Product.objects.filter(discount_price__isnull=False)

# 4. Get out-of-stock products
Product.objects.filter(stock=0)

# 5. Get featured products in Electronics
Product.objects.filter(category__name='Electronics', is_featured=True)

# 6. Get top-rated products (with approved reviews)
from django.db.models import Avg
Product.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')

# 7. Get products with their review counts
from django.db.models import Count
Product.objects.annotate(review_count=Count('reviews'))

# 8. Get categories with product counts
Category.objects.annotate(product_count=Count('products'))

# 9. Search products
from django.db.models import Q
Product.objects.filter(Q(name__icontains='laptop') | Q(description__icontains='laptop'))

# 10. Get products optimized for display (with related data)
Product.objects.select_related('category').prefetch_related('reviews').filter(is_active=True)
'''

print(ORM_PRACTICE)

# ========== TASKS ==========

print("""
PRACTICE TASKS
==============

1. Add 3 categories (Electronics, Clothing, Books)
2. Add 5 products in each category
3. Add reviews to some products
4. Use admin to manage data
5. Practice all the ORM queries above
6. Try to write your own queries:
   - Get all products sorted by price
   - Get the most reviewed products
   - Get categories with at least 3 products
   - Get products created in the last 7 days
""")

print("\n" + "=" * 60)
print("✅ Mini Project Setup Complete!")
print("=" * 60)
