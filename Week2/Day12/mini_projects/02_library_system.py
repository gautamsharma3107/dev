"""
MINI PROJECT 2: Library Management System
==========================================
Build a library management system with books, authors, and borrowing.

Requirements:
1. Create models for: Author, Book, Member, BorrowRecord
2. Books can have multiple authors (ManyToMany)
3. Members can borrow books
4. Track borrowing history
5. Set up admin for management
"""

print("=" * 60)
print("MINI PROJECT: Library Management System")
print("=" * 60)

# ========== MODELS ==========

print("""
MODELS CODE (library/models.py)
===============================
""")

MODELS_CODE = '''
from django.db import models
from django.utils import timezone
from datetime import timedelta


class Author(models.Model):
    """Book author"""
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    @property
    def book_count(self):
        return self.books.count()


class Book(models.Model):
    """Library book"""
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('biography', 'Biography'),
        ('technology', 'Technology'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=300)
    isbn = models.CharField(max_length=13, unique=True)
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    @property
    def is_available(self):
        return self.available_copies > 0
    
    def borrow(self):
        """Decrease available copies"""
        if self.available_copies > 0:
            self.available_copies -= 1
            self.save()
            return True
        return False
    
    def return_book(self):
        """Increase available copies"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            self.save()


class Member(models.Model):
    """Library member"""
    MEMBERSHIP_CHOICES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('student', 'Student'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    membership_type = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_CHOICES,
        default='basic'
    )
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    @property
    def books_borrowed(self):
        """Get currently borrowed books count.
        
        Note: For performance, consider using annotation when querying
        multiple members: Member.objects.annotate(
            borrowed_count=Count('borrow_records', filter=Q(borrow_records__returned_date__isnull=True))
        )
        """
        return self.borrow_records.filter(returned_date__isnull=True).count()
    
    @property
    def can_borrow(self):
        """Check if member can borrow more books.
        
        Calls books_borrowed property which executes a query.
        Cache the result if checking multiple times.
        """
        limits = {'basic': 2, 'premium': 5, 'student': 3}
        return self.books_borrowed < limits.get(self.membership_type, 2)


class BorrowRecord(models.Model):
    """Record of book borrowing"""
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='borrow_records'
    )
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='borrow_records'
    )
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-borrowed_date']
    
    def __str__(self):
        return f'{self.member.name} - {self.book.title}'
    
    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = timezone.now().date() + timedelta(days=14)
        super().save(*args, **kwargs)
    
    @property
    def is_overdue(self):
        if self.returned_date:
            return False
        return timezone.now().date() > self.due_date
    
    @property
    def days_overdue(self):
        if self.returned_date:
            return 0
        today = timezone.now().date()
        if today <= self.due_date:
            return 0
        return (today - self.due_date).days
'''

print(MODELS_CODE)

# ========== ADMIN ==========

print("""
ADMIN CODE (library/admin.py)
=============================
""")

ADMIN_CODE = '''
from django.contrib import admin
from django.utils.html import format_html
from .models import Author, Book, Member, BorrowRecord


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count', 'birth_date']
    search_fields = ['name']
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Books'


class BorrowRecordInline(admin.TabularInline):
    model = BorrowRecord
    extra = 0
    readonly_fields = ['borrowed_date']
    raw_id_fields = ['member']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'genre', 'total_copies', 
                    'available_copies', 'availability_status']
    list_filter = ['genre', 'authors']
    search_fields = ['title', 'isbn']
    filter_horizontal = ['authors']
    
    inlines = [BorrowRecordInline]
    
    def availability_status(self, obj):
        if obj.is_available:
            return format_html(
                '<span style="color: green;">✓ Available ({}/{})</span>',
                obj.available_copies, obj.total_copies
            )
        return format_html('<span style="color: red;">✗ Unavailable</span>')
    availability_status.short_description = 'Status'


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'membership_type', 
                    'books_borrowed', 'is_active', 'joined_date']
    list_filter = ['membership_type', 'is_active']
    search_fields = ['name', 'email']
    list_editable = ['is_active']


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['book', 'member', 'borrowed_date', 
                    'due_date', 'returned_date', 'status']
    list_filter = ['borrowed_date', 'returned_date']
    search_fields = ['book__title', 'member__name']
    raw_id_fields = ['book', 'member']
    date_hierarchy = 'borrowed_date'
    
    def status(self, obj):
        if obj.returned_date:
            return format_html('<span style="color: green;">Returned</span>')
        if obj.is_overdue:
            return format_html(
                '<span style="color: red;">Overdue ({} days)</span>',
                obj.days_overdue
            )
        return format_html('<span style="color: orange;">Borrowed</span>')
    status.short_description = 'Status'
    
    actions = ['mark_returned']
    
    @admin.action(description='Mark as returned')
    def mark_returned(self, request, queryset):
        from django.utils import timezone
        for record in queryset.filter(returned_date__isnull=True):
            record.returned_date = timezone.now().date()
            record.save()
            record.book.return_book()


admin.site.site_header = "Library Management System"
'''

print(ADMIN_CODE)

# ========== ORM QUERIES ==========

print("""
ORM QUERY PRACTICE
==================
""")

ORM_QUERIES = '''
# Sample ORM queries to practice:

# 1. Get all available books
Book.objects.filter(available_copies__gt=0)

# 2. Get books by a specific author
author = Author.objects.get(name='J.K. Rowling')
author.books.all()

# 3. Get books with multiple authors
from django.db.models import Count
Book.objects.annotate(author_count=Count('authors')).filter(author_count__gt=1)

# 4. Get overdue borrow records
from django.utils import timezone
BorrowRecord.objects.filter(
    returned_date__isnull=True,
    due_date__lt=timezone.now().date()
)

# 5. Get member's borrowing history
member = Member.objects.get(pk=1)
member.borrow_records.all()

# 6. Get most borrowed books
Book.objects.annotate(
    borrow_count=Count('borrow_records')
).order_by('-borrow_count')[:10]

# 7. Get active members who can still borrow
Member.objects.filter(is_active=True)

# 8. Books by genre with counts
Book.objects.values('genre').annotate(count=Count('id'))

# 9. Members with overdue books
Member.objects.filter(
    borrow_records__returned_date__isnull=True,
    borrow_records__due_date__lt=timezone.now().date()
).distinct()
'''

print(ORM_QUERIES)

# ========== TASKS ==========

print("""
PRACTICE TASKS
==============

1. Create the project and app
2. Add models and run migrations
3. Set up admin
4. Add sample data:
   - 5 authors
   - 10 books
   - 5 members
   - Several borrow records
5. Practice queries in Django shell
6. Add custom admin actions
""")

print("\n" + "=" * 60)
print("✅ Library System Project Complete!")
print("=" * 60)
