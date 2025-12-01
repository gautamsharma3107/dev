"""
MINI PROJECT 3: Task Management API
=====================================
Create a REST API for a task management system

Requirements:
1. JWT authentication (using simplejwt)
2. Users can only see their own tasks
3. Task assignment to team members
4. Filtering by status, priority, due date
5. Search in task title and description
6. Pagination with custom response format
7. API documentation with examples

Models:
-------
- User (Django built-in)
- Task: title, description, status, priority, assignee, creator, due_date, created_at

Status choices: todo, in_progress, review, done
Priority choices: low, medium, high, urgent

API Endpoints:
--------------
- POST /api/auth/register/     - User registration
- POST /api/auth/token/        - Get JWT token pair
- POST /api/auth/token/refresh/ - Refresh access token
- GET /api/tasks/              - List user's tasks (with filtering)
- POST /api/tasks/             - Create task
- GET /api/tasks/{id}/         - Get task detail
- PUT /api/tasks/{id}/         - Update task
- DELETE /api/tasks/{id}/      - Delete task
- POST /api/tasks/{id}/assign/ - Assign task to user
- POST /api/tasks/{id}/status/ - Update task status
- GET /api/tasks/my-assigned/  - Tasks assigned to current user
- GET /api/tasks/my-created/   - Tasks created by current user

Filtering Options:
------------------
- ?status=in_progress
- ?priority=high
- ?due_before=2024-12-31
- ?due_after=2024-01-01
- ?assignee=username
- ?search=bug fix
- ?ordering=-priority,due_date

Documentation:
--------------
- Complete Swagger documentation
- Request/response examples for all endpoints
"""

# Your code here

print("=" * 50)
print("TASK MANAGEMENT API")
print("=" * 50)
print("""
Implement the task management API with:
1. JWT authentication
2. User-specific task access
3. Task assignment functionality
4. Advanced filtering
5. Complete documentation

Start by creating:
1. models.py - Task model with choices
2. serializers.py - Task and auth serializers
3. permissions.py - Task access permissions
4. filters.py - Task filters
5. pagination.py - Custom pagination
6. views.py - ViewSets with custom actions
7. urls.py - URL routing

Good luck! 🚀
""")

# TODO: Implement the task management API
