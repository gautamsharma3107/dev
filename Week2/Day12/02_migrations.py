"""
Day 12 - Django Migrations
===========================
Learn: Creating and managing migrations, database schema changes

Key Concepts:
- Migrations are Django's way of propagating model changes to database
- makemigrations creates migration files
- migrate applies migrations to the database
"""

# ========== DJANGO MIGRATIONS ==========

print("=" * 60)
print("DJANGO MIGRATIONS")
print("=" * 60)

print("""
WHAT ARE MIGRATIONS?
====================
Migrations are Django's way of propagating changes you make to your
models (adding a field, deleting a model, etc.) into your database schema.

They are designed to be mostly automatic, but you'll need to know when
to make migrations, when to run them, and common problems you might face.

MIGRATION WORKFLOW:
==================
1. Make changes to your models (models.py)
2. Create migrations: python manage.py makemigrations
3. Review the migration file (optional but recommended)
4. Apply migrations: python manage.py migrate
""")

# ========== MIGRATION COMMANDS ==========

print("\n" + "=" * 60)
print("ESSENTIAL MIGRATION COMMANDS")
print("=" * 60)

MIGRATION_COMMANDS = """
# Create migrations for all apps
python manage.py makemigrations

# Create migrations for specific app
python manage.py makemigrations blog

# Apply all pending migrations
python manage.py migrate

# Apply migrations for specific app
python manage.py migrate blog

# Show migration status
python manage.py showmigrations

# Show SQL for a migration (without running it)
python manage.py sqlmigrate blog 0001

# Reverse a migration (rollback)
python manage.py migrate blog 0001  # Go back to migration 0001

# Reverse all migrations for an app
python manage.py migrate blog zero
"""

print(MIGRATION_COMMANDS)

# ========== MIGRATION FILE STRUCTURE ==========

print("\n" + "=" * 60)
print("MIGRATION FILE EXAMPLE")
print("=" * 60)

MIGRATION_EXAMPLE = '''
# This is what a migration file looks like
# File: blog/migrations/0001_initial.py

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """
    Initial migration for the blog app.
    Creates the Post model.
    """
    
    # Dependencies (migrations that must run before this one)
    initial = True
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]
    
    # Operations to perform
    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
    ]
'''

print(MIGRATION_EXAMPLE)

# ========== COMMON MIGRATION OPERATIONS ==========

print("\n" + "=" * 60)
print("COMMON MIGRATION OPERATIONS")
print("=" * 60)

MIGRATION_OPERATIONS = '''
# Creating a model
migrations.CreateModel(
    name='Post',
    fields=[
        ('id', models.BigAutoField(primary_key=True)),
        ('title', models.CharField(max_length=200)),
    ],
)

# Deleting a model
migrations.DeleteModel(name='OldModel')

# Adding a field
migrations.AddField(
    model_name='post',
    name='slug',
    field=models.SlugField(default='temp', unique=True),
)

# Removing a field
migrations.RemoveField(
    model_name='post',
    name='old_field',
)

# Altering a field
migrations.AlterField(
    model_name='post',
    name='title',
    field=models.CharField(max_length=300),  # Changed from 200 to 300
)

# Renaming a field
migrations.RenameField(
    model_name='post',
    old_name='content',
    new_name='body',
)

# Adding index
migrations.AddIndex(
    model_name='post',
    index=models.Index(fields=['title', 'created_at'], name='title_date_idx'),
)
'''

print(MIGRATION_OPERATIONS)

# ========== HANDLING MIGRATION ISSUES ==========

print("\n" + "=" * 60)
print("HANDLING COMMON MIGRATION ISSUES")
print("=" * 60)

print("""
ISSUE 1: Adding non-nullable field to existing table
-----------------------------------------------------
When you add a required field to a model that already has data:

Solution A: Provide a default value
    new_field = models.CharField(max_length=100, default='')

Solution B: Make it nullable
    new_field = models.CharField(max_length=100, null=True, blank=True)

Solution C: Provide default during migration (interactive)
    Django will ask you to provide a default value when running makemigrations


ISSUE 2: Conflicting migrations
-------------------------------
Multiple developers create migrations on the same model:

Solution: Merge migrations
    python manage.py makemigrations --merge


ISSUE 3: Migration dependencies
-------------------------------
Sometimes migrations need to run in a specific order:

Solution: Edit the migration file's dependencies list
    dependencies = [
        ('blog', '0002_add_author'),
        ('auth', '0012_alter_user'),
    ]


ISSUE 4: Fake migrations (database already modified)
----------------------------------------------------
If you manually modified the database:

    python manage.py migrate --fake blog 0003

This marks migrations as applied without running them.


ISSUE 5: Reset migrations (development only!)
---------------------------------------------
To completely reset migrations (DANGER - DATA LOSS!):

    # 1. Delete all migration files except __init__.py
    # 2. Delete the database
    # 3. Run makemigrations
    # 4. Run migrate
""")

# ========== BEST PRACTICES ==========

print("\n" + "=" * 60)
print("MIGRATION BEST PRACTICES")
print("=" * 60)

print("""
1. ALWAYS commit migration files to version control
   - Migrations are part of your codebase
   - Team members need them to sync their databases

2. Review migration files before applying
   - Check what SQL will be executed: python manage.py sqlmigrate app_name 0001
   - Make sure operations are correct

3. Never edit migrations that have been applied in production
   - Create new migrations instead
   - Editing applied migrations can cause inconsistencies

4. Test migrations on a copy of production data
   - Before deploying to production
   - Catch data migration issues early

5. Use data migrations for complex data changes
   - Create custom migrations with RunPython
   - Move data when changing schema

6. Keep migrations small and focused
   - One logical change per migration
   - Easier to debug and rollback

7. Name migrations descriptively
   python manage.py makemigrations --name add_slug_to_post
""")

# ========== DATA MIGRATIONS ==========

print("\n" + "=" * 60)
print("DATA MIGRATIONS (ADVANCED)")
print("=" * 60)

DATA_MIGRATION_EXAMPLE = '''
# Custom data migration example
# File: blog/migrations/0003_populate_slugs.py

from django.db import migrations
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    """
    Populate slug field for existing posts.
    """
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        if not post.slug:
            post.slug = slugify(post.title)
            post.save()


def reverse_slugs(apps, schema_editor):
    """
    Reverse function (optional but recommended).
    """
    Post = apps.get_model('blog', 'Post')
    Post.objects.all().update(slug='')


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_post_slug'),
    ]
    
    operations = [
        migrations.RunPython(populate_slugs, reverse_slugs),
    ]
'''

print(DATA_MIGRATION_EXAMPLE)

print("\n" + "=" * 60)
print("✅ Django Migrations - Complete!")
print("=" * 60)
