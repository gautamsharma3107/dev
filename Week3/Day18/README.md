# Day 18: Database Advanced Topics

## 📚 Topics Covered

### Part 1: PostgreSQL Setup
1. PostgreSQL vs SQLite comparison
2. Installation and setup
3. psycopg2 driver basics
4. Connection management

### Part 2: Database Relationships
1. One-to-Many relationships
2. Many-to-Many relationships
3. Foreign keys and constraints
4. Join queries

### Part 3: Query Optimization
1. Query analysis with EXPLAIN
2. Indexing strategies
3. N+1 query problem
4. Pagination techniques

### Part 4: NoSQL Databases
1. MongoDB basics (document-oriented)
2. Redis for caching (key-value)
3. When to use SQL vs NoSQL

## 📁 File Structure
```
Day18/
├── 01_postgresql_setup.py
├── 02_db_relationships.py
├── 03_query_optimization.py
├── 04_mongodb_basics.py
├── 05_redis_caching.py
├── exercises/
│   ├── 01_relationship_exercises.py
│   └── 02_optimization_exercises.py
├── mini_projects/
│   ├── 01_blog_database.py
│   └── 02_caching_layer.py
├── day18_assessment.py
├── CHEATSHEET.md
└── README.md
```

## 🎯 Learning Objectives
- [ ] Set up and connect to PostgreSQL
- [ ] Understand and implement database relationships
- [ ] Optimize queries using indexes and EXPLAIN
- [ ] Understand the N+1 problem and solutions
- [ ] Get introduced to MongoDB document model
- [ ] Understand Redis caching concepts
- [ ] Know when to use SQL vs NoSQL

## ⏱️ Estimated Time: 4-5 hours

## 🚀 Study Order
1. Complete tutorial 01 (PostgreSQL Setup)
2. Complete tutorial 02 (Database Relationships)
3. Complete tutorial 03 (Query Optimization)
4. Complete tutorial 04 (MongoDB Basics)
5. Complete tutorial 05 (Redis Caching)
6. Complete exercises
7. Build mini projects
8. Take assessment (need 70% to pass)

## 📋 Prerequisites
- Day 10: SQL Essentials
- Basic understanding of CRUD operations
- Python file handling (Day 4)

## 🔧 Required Setup
```bash
# PostgreSQL (optional - SQLite is fine)
pip install psycopg2-binary

# MongoDB (optional)
pip install pymongo

# Redis (optional)  
pip install redis

# For exercises, SQLite is used by default
# No additional setup required!
```
