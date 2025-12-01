"""
EXERCISES: Database Relationships
=================================
Complete all 5 exercises below
"""

# Exercise 1: One-to-Many Relationship
# TODO: Create SQLAlchemy models for Author and Book:
# - Author: id, name
# - Book: id, title, author_id (FK to Author)
# - One Author can have many Books

print("Exercise 1: One-to-Many Relationship")
print("-" * 40)
# Your code here:




# Exercise 2: Many-to-Many Relationship
# TODO: Create SQLAlchemy models for Student and Course:
# - Student: id, name
# - Course: id, title
# - Students can enroll in many Courses
# - Courses can have many Students
# - Create the association table

print("\n\nExercise 2: Many-to-Many Relationship")
print("-" * 40)
# Your code here:




# Exercise 3: Nested Pydantic Schemas
# TODO: Create Pydantic schemas for the Author/Book relationship:
# - AuthorBase, AuthorCreate, Author
# - BookBase, BookCreate, Book
# - BookWithAuthor (includes author details)
# - AuthorWithBooks (includes list of books)

print("\n\nExercise 3: Nested Pydantic Schemas")
print("-" * 40)
# Your code here:




# Exercise 4: Create with Relationship
# TODO: Write a function to create a Book with an Author:
# - Accept book data and author_id
# - Verify author exists
# - Create and return the book with author data

print("\n\nExercise 4: Create with Relationship")
print("-" * 40)
# Your code here:




# Exercise 5: Query with Eager Loading
# TODO: Write a function to get all books with their authors:
# - Use joinedload for eager loading
# - Return list of books with author data included

print("\n\nExercise 5: Query with Eager Loading")
print("-" * 40)
# Your code here:
