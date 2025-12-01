"""
EXERCISES: Django Migrations
=============================
Complete all exercises below to understand Django migrations.
"""

# Exercise 1: Migration Commands
# TODO: Write the commands for each scenario

print("Exercise 1: Migration Commands")
print("-" * 40)

print("""
What command would you use for each scenario?

1. Create migrations for all apps:
   Your answer: _______________________

2. Create migrations only for the 'shop' app:
   Your answer: _______________________

3. Apply all pending migrations:
   Your answer: _______________________

4. Show the status of all migrations:
   Your answer: _______________________

5. View the SQL that a specific migration will run (shop app, migration 0001):
   Your answer: _______________________

6. Rollback to a specific migration (shop app, migration 0002):
   Your answer: _______________________

7. Create a migration with a custom name:
   Your answer: _______________________
""")


# Exercise 2: Handle Non-Nullable Field
# TODO: Explain how to add a non-nullable field to an existing model

print("\n\nExercise 2: Adding Non-Nullable Field")
print("-" * 40)

print("""
You have an existing Product model with data in the database.
You want to add a new required field 'sku' (stock keeping unit).

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Want to add: sku = models.CharField(max_length=50, unique=True)

What are your options? Write the code for each approach:

Option A (Provide a default):
_______________________

Option B (Make it nullable first):
_______________________

Option C (Handle in migration interactively):
_______________________
""")


# Exercise 3: Reading Migration File
# TODO: Analyze a migration file and explain what it does

print("\n\nExercise 3: Reading Migration File")
print("-" * 40)

MIGRATION_FILE = '''
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_percent',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name', 'price'], name='product_name_price_idx'),
        ),
    ]
'''

print(MIGRATION_FILE)
print("""
Questions:
1. What app is this migration for?
   Answer: _______________________

2. What migrations must run before this one?
   Answer: _______________________

3. List all changes this migration makes:
   a) _______________________
   b) _______________________
   c) _______________________
""")


# Exercise 4: Data Migration
# TODO: Write a data migration to populate existing records

print("\n\nExercise 4: Data Migration")
print("-" * 40)

print("""
You've added a 'slug' field to your Category model.
Existing categories don't have slugs populated.

Write a data migration function to populate slugs from names:

from django.db import migrations
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    # Your code here
    pass


def reverse_slugs(apps, schema_editor):
    # Your code here
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0003_category_slug'),
    ]
    
    operations = [
        migrations.RunPython(populate_slugs, reverse_slugs),
    ]
""")


# Exercise 5: Troubleshooting Migrations
# TODO: Identify the issue and solution for each scenario

print("\n\nExercise 5: Troubleshooting")
print("-" * 40)

print("""
For each scenario, identify the problem and solution:

Scenario A:
Error: django.db.utils.OperationalError: no such column: shop_product.category_id

Problem: _______________________
Solution: _______________________


Scenario B:
Error: django.db.utils.IntegrityError: NOT NULL constraint failed

Problem: _______________________
Solution: _______________________


Scenario C:
CommandError: Conflicting migrations detected; multiple leaf nodes in the migration graph

Problem: _______________________
Solution: _______________________
""")


# ========== ANSWERS ==========

print("\n\n" + "=" * 60)
print("ANSWERS (Check after attempting)")
print("=" * 60)

print("""
Exercise 1 Answers:
1. python manage.py makemigrations
2. python manage.py makemigrations shop
3. python manage.py migrate
4. python manage.py showmigrations
5. python manage.py sqlmigrate shop 0001
6. python manage.py migrate shop 0002
7. python manage.py makemigrations --name add_sku_field

Exercise 2 Answers:
Option A: sku = models.CharField(max_length=50, unique=True, default='SKU-0000')
Option B: First add with null=True, then populate, then remove null=True
Option C: Django will prompt for a one-off default during makemigrations

Exercise 3 Answers:
1. shop app
2. shop migration 0002_product_category
3. Changes: 
   a) Adds discount_percent field with default 0
   b) Changes name field max_length from 200 to 300
   c) Adds database index on name and price fields

Exercise 4 Answer:
def populate_slugs(apps, schema_editor):
    Category = apps.get_model('shop', 'Category')
    for cat in Category.objects.all():
        cat.slug = slugify(cat.name)
        cat.save()

Exercise 5 Answers:
A: Migrations not applied. Run: python manage.py migrate
B: Adding non-nullable field without default. Add default or null=True
C: Multiple developers created migrations. Run: python manage.py makemigrations --merge
""")
