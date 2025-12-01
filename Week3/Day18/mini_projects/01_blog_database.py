"""
MINI PROJECT 1: Blog Database System
=====================================
A complete blog database with relationships

Features:
1. Users, Posts, Comments, Tags tables
2. One-to-many and many-to-many relationships
3. Complex queries with JOINs
4. Full CRUD operations

Run this to see a complete blog database implementation!
"""

import sqlite3
import os
from datetime import datetime, timedelta
import random

print("=" * 60)
print("BLOG DATABASE SYSTEM")
print("=" * 60)

# Database setup
db_file = "blog.db"
conn = sqlite3.connect(db_file)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# ========== CREATE SCHEMA ==========
print("\n📝 Creating database schema...")

# Drop existing tables
for table in ["post_tags", "comments", "posts", "tags", "users"]:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Users table
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Posts table (one-to-many with users)
cursor.execute("""
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    status TEXT DEFAULT 'draft',
    views INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
)
""")

# Comments table (one-to-many with posts and users)
cursor.execute("""
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
)
""")

# Tags table
cursor.execute("""
CREATE TABLE tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
""")

# Post-Tags junction table (many-to-many)
cursor.execute("""
CREATE TABLE post_tags (
    post_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
)
""")

conn.commit()
print("✅ Schema created successfully!")

# ========== BLOG API CLASS ==========
class BlogDB:
    """Blog database operations"""
    
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
    
    # User operations
    def create_user(self, username, email, bio=None):
        self.cursor.execute(
            "INSERT INTO users (username, email, bio) VALUES (?, ?, ?)",
            (username, email, bio)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return self.cursor.fetchone()
    
    # Post operations
    def create_post(self, title, content, author_id, tags=None, status='draft'):
        self.cursor.execute(
            """INSERT INTO posts (title, content, author_id, status, published_at) 
               VALUES (?, ?, ?, ?, ?)""",
            (title, content, author_id, status, 
             datetime.now() if status == 'published' else None)
        )
        post_id = self.cursor.lastrowid
        
        if tags:
            for tag_name in tags:
                tag_id = self._get_or_create_tag(tag_name)
                self.cursor.execute(
                    "INSERT INTO post_tags (post_id, tag_id) VALUES (?, ?)",
                    (post_id, tag_id)
                )
        
        self.conn.commit()
        return post_id
    
    def _get_or_create_tag(self, name):
        self.cursor.execute("SELECT id FROM tags WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        self.cursor.execute("INSERT INTO tags (name) VALUES (?)", (name,))
        return self.cursor.lastrowid
    
    def get_post_with_details(self, post_id):
        """Get post with author and tags"""
        self.cursor.execute("""
            SELECT p.*, u.username as author_name,
                   GROUP_CONCAT(t.name) as tags
            FROM posts p
            JOIN users u ON p.author_id = u.id
            LEFT JOIN post_tags pt ON p.id = pt.post_id
            LEFT JOIN tags t ON pt.tag_id = t.id
            WHERE p.id = ?
            GROUP BY p.id
        """, (post_id,))
        return self.cursor.fetchone()
    
    def increment_views(self, post_id):
        self.cursor.execute(
            "UPDATE posts SET views = views + 1 WHERE id = ?",
            (post_id,)
        )
        self.conn.commit()
    
    # Comment operations
    def add_comment(self, post_id, author_id, content):
        self.cursor.execute(
            "INSERT INTO comments (post_id, author_id, content) VALUES (?, ?, ?)",
            (post_id, author_id, content)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_post_comments(self, post_id):
        """Get comments with author names"""
        self.cursor.execute("""
            SELECT c.*, u.username as author_name
            FROM comments c
            JOIN users u ON c.author_id = u.id
            WHERE c.post_id = ?
            ORDER BY c.created_at DESC
        """, (post_id,))
        return self.cursor.fetchall()
    
    # Advanced queries
    def get_recent_posts(self, limit=10):
        """Get recent published posts with author and stats"""
        self.cursor.execute("""
            SELECT p.id, p.title, p.views, p.created_at,
                   u.username as author,
                   COUNT(DISTINCT c.id) as comment_count,
                   GROUP_CONCAT(DISTINCT t.name) as tags
            FROM posts p
            JOIN users u ON p.author_id = u.id
            LEFT JOIN comments c ON p.id = c.post_id
            LEFT JOIN post_tags pt ON p.id = pt.post_id
            LEFT JOIN tags t ON pt.tag_id = t.id
            WHERE p.status = 'published'
            GROUP BY p.id
            ORDER BY p.created_at DESC
            LIMIT ?
        """, (limit,))
        return self.cursor.fetchall()
    
    def get_user_stats(self, user_id):
        """Get user statistics"""
        self.cursor.execute("""
            SELECT 
                u.username,
                COUNT(DISTINCT p.id) as post_count,
                COUNT(DISTINCT c.id) as comment_count,
                COALESCE(SUM(p.views), 0) as total_views
            FROM users u
            LEFT JOIN posts p ON u.id = p.author_id
            LEFT JOIN comments c ON u.id = c.author_id
            WHERE u.id = ?
            GROUP BY u.id
        """, (user_id,))
        return self.cursor.fetchone()
    
    def get_popular_tags(self, limit=10):
        """Get most used tags"""
        self.cursor.execute("""
            SELECT t.name, COUNT(pt.post_id) as post_count
            FROM tags t
            JOIN post_tags pt ON t.id = pt.tag_id
            GROUP BY t.id
            ORDER BY post_count DESC
            LIMIT ?
        """, (limit,))
        return self.cursor.fetchall()
    
    def search_posts(self, query):
        """Search posts by title or content"""
        search = f"%{query}%"
        self.cursor.execute("""
            SELECT p.id, p.title, p.views, u.username
            FROM posts p
            JOIN users u ON p.author_id = u.id
            WHERE p.status = 'published' 
              AND (p.title LIKE ? OR p.content LIKE ?)
            ORDER BY p.views DESC
        """, (search, search))
        return self.cursor.fetchall()

# ========== DEMO ==========
blog = BlogDB(conn)

print("\n📝 Creating sample data...")

# Create users
users = [
    ("alice", "alice@blog.com", "Python enthusiast"),
    ("bob", "bob@blog.com", "Web developer"),
    ("charlie", "charlie@blog.com", "Data scientist"),
]
user_ids = []
for username, email, bio in users:
    user_ids.append(blog.create_user(username, email, bio))
print(f"✅ Created {len(users)} users")

# Create posts
posts_data = [
    ("Getting Started with Python", "Python is a great language...", user_ids[0], 
     ["python", "tutorial", "beginners"], "published"),
    ("Advanced SQL Techniques", "Let's explore complex queries...", user_ids[0], 
     ["sql", "database", "tutorial"], "published"),
    ("Building REST APIs", "REST APIs are essential...", user_ids[1], 
     ["api", "python", "web"], "published"),
    ("Machine Learning Basics", "ML is transforming...", user_ids[2], 
     ["ml", "python", "data-science"], "published"),
    ("Draft Post", "Work in progress...", user_ids[0], 
     ["draft"], "draft"),
]
post_ids = []
for title, content, author_id, tags, status in posts_data:
    post_ids.append(blog.create_post(title, content, author_id, tags, status))
print(f"✅ Created {len(posts_data)} posts")

# Add comments
comments_data = [
    (post_ids[0], user_ids[1], "Great article!"),
    (post_ids[0], user_ids[2], "Very helpful, thanks!"),
    (post_ids[1], user_ids[1], "I learned a lot from this."),
    (post_ids[2], user_ids[0], "Nice explanation!"),
    (post_ids[2], user_ids[2], "Looking forward to more!"),
]
for post_id, author_id, content in comments_data:
    blog.add_comment(post_id, author_id, content)
print(f"✅ Added {len(comments_data)} comments")

# Simulate views
for post_id in post_ids[:4]:
    for _ in range(random.randint(10, 100)):
        blog.increment_views(post_id)
print("✅ Added random views to posts")

# ========== DEMONSTRATE QUERIES ==========
print("\n" + "=" * 60)
print("QUERY DEMONSTRATIONS")
print("=" * 60)

# Recent posts
print("\n📰 Recent Published Posts:")
print("-" * 60)
for row in blog.get_recent_posts(5):
    print(f"  [{row[2]} views] {row[1]}")
    print(f"    by {row[4]} | {row[5]} comments | tags: {row[6]}")

# Post details
print("\n📝 Post Details (ID=1):")
print("-" * 60)
post = blog.get_post_with_details(1)
print(f"  Title: {post[1]}")
print(f"  Author: {post[8]}")
print(f"  Status: {post[4]}")
print(f"  Views: {post[5]}")
print(f"  Tags: {post[9]}")

# Comments
print("\n💬 Comments on Post 1:")
print("-" * 60)
for comment in blog.get_post_comments(1):
    print(f"  {comment[5]}: {comment[3]}")

# User stats
print("\n👤 User Stats (alice):")
print("-" * 60)
stats = blog.get_user_stats(1)
print(f"  Username: {stats[0]}")
print(f"  Posts: {stats[1]}")
print(f"  Comments: {stats[2]}")
print(f"  Total Views: {stats[3]}")

# Popular tags
print("\n🏷️ Popular Tags:")
print("-" * 60)
for tag, count in blog.get_popular_tags(5):
    print(f"  #{tag}: {count} posts")

# Search
print("\n🔍 Search 'python':")
print("-" * 60)
for post in blog.search_posts("python"):
    print(f"  [{post[2]} views] {post[1]} by {post[3]}")

# ========== CLEANUP ==========
print("\n" + "=" * 60)
conn.close()
if os.path.exists(db_file):
    os.remove(db_file)
print("✅ Blog database demo complete! Database cleaned up.")
