"""
EXERCISES: Serializers
======================
Complete all exercises below
"""

# Exercise 1: Basic ModelSerializer
# TODO: Create a serializer for the following model

print("Exercise 1: Basic ModelSerializer")
print("-" * 40)

print("""
Given this model:

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

Create a ProductSerializer that:
1. Includes all fields
2. Makes 'id' and 'created_at' read-only

Write your code below:
""")

# Your code here:
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = # TODO: specify which fields to include (e.g., '__all__' or a list)
#         read_only_fields = # TODO: specify read-only fields as a list


# Exercise 2: Custom Validation
# TODO: Add validation to the serializer

print("\n\nExercise 2: Custom Validation")
print("-" * 40)

print("""
Add validation methods to the ProductSerializer:

1. validate_price: Price must be greater than 0
2. validate_stock: Stock cannot be negative
3. validate_name: Name must be at least 3 characters

Write your validation methods:
""")

# Your code here:
# def validate_price(self, value):
#     pass

# def validate_stock(self, value):
#     pass

# def validate_name(self, value):
#     pass


# Exercise 3: SerializerMethodField
# TODO: Add computed fields

print("\n\nExercise 3: SerializerMethodField")
print("-" * 40)

print("""
Add these computed fields to ProductSerializer:

1. discounted_price - 15% off the regular price
2. in_stock - Boolean, True if stock > 0
3. price_with_tax - Price + 10% tax

Write your code:
""")

# Your code here:
# discounted_price = serializers.SerializerMethodField()
# 
# def get_discounted_price(self, obj):
#     pass


# Exercise 4: Nested Serializer
# TODO: Create nested serializers

print("\n\nExercise 4: Nested Serializers")
print("-" * 40)

print("""
Given these models:

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

Create:
1. CategorySerializer with all fields
2. ProductSerializer with nested category

The product response should look like:
{
    "id": 1,
    "name": "Laptop",
    "category": {
        "id": 1,
        "name": "Electronics",
        "description": "Electronic devices"
    },
    "price": "999.99"
}

Write your serializers:
""")

# Your code here:
# class CategorySerializer(serializers.ModelSerializer):
#     pass

# class ProductSerializer(serializers.ModelSerializer):
#     pass


# Exercise 5: Different Serializers
# TODO: Create list and detail serializers

print("\n\nExercise 5: List vs Detail Serializers")
print("-" * 40)

print("""
Create two serializers for Product:

1. ProductListSerializer (for list view):
   - Only include: id, name, price, is_active
   
2. ProductDetailSerializer (for detail view):
   - Include all fields
   - Add computed field: days_since_created

This pattern is useful for:
- Showing less data in list views (faster)
- Showing full data in detail views

Write your serializers:
""")

# Your code here:
# class ProductListSerializer(serializers.ModelSerializer):
#     pass

# class ProductDetailSerializer(serializers.ModelSerializer):
#     pass
