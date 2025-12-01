"""
MINI PROJECT 1: Todo API
========================
Build a complete REST API for a Todo application

Requirements:
- Todo model with: title, description, is_completed, priority, due_date, created_at
- Full CRUD operations
- Filter by is_completed
- Filter by priority (low, medium, high)
- Search by title
- Order by due_date, priority

Steps:
1. Create the model
2. Create the serializer
3. Create the viewset
4. Set up URLs
5. Test with browsable API
"""

print("=" * 60)
print("MINI PROJECT: Todo API")
print("=" * 60)

# ========== STEP 1: MODEL ==========
print("""
STEP 1: Create the Model (models.py)
------------------------------------

class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='medium'
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
""")


# ========== STEP 2: SERIALIZER ==========
print("""
STEP 2: Create the Serializer (serializers.py)
----------------------------------------------

from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    days_until_due = serializers.SerializerMethodField()
    
    class Meta:
        model = Todo
        fields = [
            'id', 'title', 'description', 'is_completed',
            'priority', 'due_date', 'days_until_due',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_days_until_due(self, obj):
        if obj.due_date:
            from datetime import date
            delta = obj.due_date - date.today()
            return delta.days
        return None
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters"
            )
        return value


class TodoListSerializer(serializers.ModelSerializer):
    \"\"\"Simplified serializer for list view.\"\"\"
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'is_completed', 'priority', 'due_date']
""")


# ========== STEP 3: VIEWSET ==========
print("""
STEP 3: Create the ViewSet (views.py)
-------------------------------------

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'priority', 'created_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return TodoListSerializer
        return TodoSerializer
    
    def get_queryset(self):
        queryset = Todo.objects.all()
        
        # Filter by completion status
        is_completed = self.request.query_params.get('is_completed')
        if is_completed is not None:
            queryset = queryset.filter(
                is_completed=is_completed.lower() == 'true'
            )
        
        # Filter by priority
        priority = self.request.query_params.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def completed(self, request):
        \"\"\"Get all completed todos.\"\"\"
        todos = self.queryset.filter(is_completed=True)
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        \"\"\"Get all pending todos.\"\"\"
        todos = self.queryset.filter(is_completed=False)
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def overdue(self, request):
        \"\"\"Get overdue todos.\"\"\"
        from datetime import date
        todos = self.queryset.filter(
            is_completed=False,
            due_date__lt=date.today()
        )
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        \"\"\"Toggle todo completion status.\"\"\"
        todo = self.get_object()
        todo.is_completed = not todo.is_completed
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def complete_all(self, request):
        \"\"\"Mark all todos as completed.\"\"\"
        updated = self.queryset.filter(is_completed=False).update(
            is_completed=True
        )
        return Response({'message': f'{updated} todos marked as completed'})
    
    @action(detail=False, methods=['delete'])
    def clear_completed(self, request):
        \"\"\"Delete all completed todos.\"\"\"
        deleted, _ = self.queryset.filter(is_completed=True).delete()
        return Response(
            {'message': f'{deleted} completed todos deleted'},
            status=status.HTTP_204_NO_CONTENT
        )
""")


# ========== STEP 4: URLS ==========
print("""
STEP 4: Set Up URLs (urls.py)
-----------------------------

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Generated endpoints:
# GET    /api/todos/           - List all todos
# POST   /api/todos/           - Create a todo
# GET    /api/todos/{id}/      - Get a todo
# PUT    /api/todos/{id}/      - Update a todo
# PATCH  /api/todos/{id}/      - Partial update
# DELETE /api/todos/{id}/      - Delete a todo
# GET    /api/todos/completed/ - Get completed todos
# GET    /api/todos/pending/   - Get pending todos
# GET    /api/todos/overdue/   - Get overdue todos
# POST   /api/todos/{id}/toggle_complete/ - Toggle status
# POST   /api/todos/complete_all/  - Complete all
# DELETE /api/todos/clear_completed/ - Clear completed
""")


# ========== STEP 5: TEST ==========
print("""
STEP 5: Test Your API
---------------------

# Create a todo
curl -X POST http://127.0.0.1:8000/api/todos/ \\
  -H "Content-Type: application/json" \\
  -d '{
    "title": "Learn DRF",
    "description": "Complete Day 15 exercises",
    "priority": "high",
    "due_date": "2024-12-31"
  }'

# List todos
curl http://127.0.0.1:8000/api/todos/

# Filter by priority
curl "http://127.0.0.1:8000/api/todos/?priority=high"

# Search
curl "http://127.0.0.1:8000/api/todos/?search=DRF"

# Toggle completion
curl -X POST http://127.0.0.1:8000/api/todos/1/toggle_complete/

# Get pending
curl http://127.0.0.1:8000/api/todos/pending/
""")


print("\n" + "=" * 60)
print("✅ Todo API Mini Project Complete!")
print("=" * 60)
print("""
What you've learned:
- Creating models with choices
- Custom serializer fields
- ViewSet with custom actions
- Filtering and searching
- Bulk operations

Challenge: Add a 'category' field with a separate Category model!
""")
