"""
EXERCISES: Django Models
=========================
Complete all exercises below to practice Django models.
"""

# Exercise 1: Create a Product Model
# TODO: Create a Product model with the following fields:
# - name (CharField, max 200 characters)
# - description (TextField)
# - price (DecimalField, 10 digits total, 2 decimal places)
# - quantity (PositiveIntegerField, default 0)
# - is_available (BooleanField, default True)
# - created_at (DateTimeField, auto-set on creation)
# - updated_at (DateTimeField, auto-set on update)

print("Exercise 1: Product Model")
print("-" * 40)

EXERCISE_1 = '''
# Write your model code here (for blog/models.py):

from django.db import models

class Product(models.Model):
    # Your code here
    pass
'''

print(EXERCISE_1)
print("# Complete the Product model with all required fields")


# Exercise 2: Add Model Meta Options
# TODO: Add Meta class to Product model with:
# - ordering by name (alphabetically)
# - verbose_name 'Product'
# - verbose_name_plural 'Products'

print("\n\nExercise 2: Model Meta Options")
print("-" * 40)
print("# Add Meta class to your Product model with ordering and verbose names")


# Exercise 3: Add __str__ Method
# TODO: Add __str__ method to Product that returns:
# "{name} - ${price}"

print("\n\nExercise 3: __str__ Method")
print("-" * 40)
print("# Add __str__ method that displays product name and price")


# Exercise 4: Add Custom Methods
# TODO: Add these methods to Product:
# - is_in_stock(): returns True if quantity > 0
# - get_display_price(): returns price formatted as "$XX.XX"

print("\n\nExercise 4: Custom Model Methods")
print("-" * 40)
print("# Add is_in_stock() and get_display_price() methods")


# Exercise 5: Create Category Model with ForeignKey
# TODO: Create a Category model and add a ForeignKey to Product:
# Category fields:
# - name (CharField, max 100, unique)
# - slug (SlugField, unique)
# 
# Add to Product:
# - category (ForeignKey to Category, SET_NULL on delete)

print("\n\nExercise 5: Category with ForeignKey")
print("-" * 40)
print("# Create Category model and add ForeignKey to Product")


# ========== SOLUTION TEMPLATE ==========

print("\n\n" + "=" * 60)
print("EXPECTED SOLUTION STRUCTURE")
print("=" * 60)

SOLUTION = '''
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    def is_in_stock(self):
        """Check if product is in stock"""
        return self.quantity > 0
    
    def get_display_price(self):
        """Return formatted price"""
        return f"${self.price:.2f}"
'''

print(SOLUTION)
