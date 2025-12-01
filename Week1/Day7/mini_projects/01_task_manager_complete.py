"""
MINI PROJECT: CLI Task Manager with File Storage
================================================
Week 1 Capstone Project

This is a complete implementation of the Task Manager CLI application.
It demonstrates:
- Variables and data types
- Lists and dictionaries
- Functions with parameters and returns
- File handling (JSON)
- Exception handling
- Input validation
- Menu-driven interface

Features:
1. Add tasks with title, description, priority, and due date
2. View tasks with filtering and sorting
3. Mark tasks as complete
4. Delete tasks
5. Search tasks
6. Statistics dashboard
7. Persistent storage with JSON
"""

import json
import os
from datetime import datetime

# ========== CONFIGURATION ==========

class Config:
    """Application configuration"""
    DATA_FILE = "task_manager_data.json"
    PRIORITIES = ["high", "medium", "low"]
    STATUSES = ["pending", "completed"]
    
    # Display settings
    PRIORITY_COLORS = {
        "high": "🔴",
        "medium": "🟡",
        "low": "🟢"
    }
    STATUS_ICONS = {
        "pending": "⬜",
        "completed": "✅"
    }

# ========== DATA LAYER ==========

class TaskStorage:
    """Handles all data persistence operations"""
    
    def __init__(self, filename):
        self.filename = filename
    
    def load(self):
        """Load tasks from JSON file"""
        try:
            if not os.path.exists(self.filename):
                return []
            
            with open(self.filename, "r") as f:
                data = json.load(f)
                return data.get("tasks", [])
        except json.JSONDecodeError as e:
            print(f"⚠️ Warning: Data file corrupted - {e}")
            return []
        except IOError as e:
            print(f"❌ Error reading file: {e}")
            return []
    
    def save(self, tasks):
        """Save tasks to JSON file"""
        try:
            data = {
                "version": "1.0",
                "updated_at": datetime.now().isoformat(),
                "tasks": tasks
            }
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=2)
            return True
        except IOError as e:
            print(f"❌ Error saving file: {e}")
            return False
    
    def backup(self):
        """Create a backup of the data file"""
        if os.path.exists(self.filename):
            backup_name = f"{self.filename}.backup"
            try:
                with open(self.filename, "r") as src:
                    with open(backup_name, "w") as dst:
                        dst.write(src.read())
                return True
            except IOError:
                return False
        return False

# ========== TASK MODEL ==========

class Task:
    """Represents a single task"""
    
    _id_counter = 0
    
    @classmethod
    def set_id_counter(cls, tasks):
        """Set ID counter based on existing tasks"""
        if tasks:
            cls._id_counter = max(t.get("id", 0) for t in tasks)
    
    @classmethod
    def get_next_id(cls):
        """Generate next task ID"""
        cls._id_counter += 1
        return cls._id_counter
    
    @staticmethod
    def create(title, description="", priority="medium", due_date=None):
        """Create a new task dictionary"""
        return {
            "id": Task.get_next_id(),
            "title": title.strip(),
            "description": description.strip(),
            "priority": priority.lower(),
            "status": "pending",
            "due_date": due_date,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
    
    @staticmethod
    def validate(title, priority):
        """Validate task data"""
        errors = []
        
        if not title or not title.strip():
            errors.append("Title cannot be empty")
        
        if priority.lower() not in Config.PRIORITIES:
            errors.append(f"Priority must be one of: {', '.join(Config.PRIORITIES)}")
        
        return errors

# ========== TASK MANAGER ==========

class TaskManager:
    """Main task management logic"""
    
    def __init__(self):
        self.storage = TaskStorage(Config.DATA_FILE)
        self.tasks = self.storage.load()
        Task.set_id_counter(self.tasks)
    
    def add(self, title, description="", priority="medium", due_date=None):
        """Add a new task"""
        # Validate
        errors = Task.validate(title, priority)
        if errors:
            return False, errors
        
        # Create and save
        task = Task.create(title, description, priority, due_date)
        self.tasks.append(task)
        self.storage.save(self.tasks)
        
        return True, task
    
    def get(self, task_id):
        """Get task by ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
    
    def update(self, task_id, **updates):
        """Update task fields"""
        task = self.get(task_id)
        if not task:
            return False, "Task not found"
        
        # Validate priority if provided
        if "priority" in updates:
            if updates["priority"].lower() not in Config.PRIORITIES:
                return False, "Invalid priority"
            updates["priority"] = updates["priority"].lower()
        
        # Apply updates
        for key, value in updates.items():
            if key in task and value is not None:
                task[key] = value
        
        self.storage.save(self.tasks)
        return True, task
    
    def complete(self, task_id):
        """Mark task as completed"""
        task = self.get(task_id)
        if not task:
            return False, "Task not found"
        
        if task["status"] == "completed":
            return True, "Already completed"
        
        task["status"] = "completed"
        task["completed_at"] = datetime.now().isoformat()
        self.storage.save(self.tasks)
        
        return True, task
    
    def delete(self, task_id):
        """Delete a task"""
        task = self.get(task_id)
        if not task:
            return False, "Task not found"
        
        self.tasks.remove(task)
        self.storage.save(self.tasks)
        
        return True, task
    
    def list(self, status=None, priority=None, sort_by="created_at"):
        """List tasks with optional filters and sorting"""
        result = self.tasks.copy()
        
        # Filter by status
        if status:
            result = [t for t in result if t["status"] == status]
        
        # Filter by priority
        if priority:
            result = [t for t in result if t["priority"] == priority]
        
        # Sort
        if sort_by == "priority":
            priority_order = {"high": 0, "medium": 1, "low": 2}
            result.sort(key=lambda t: priority_order.get(t["priority"], 3))
        elif sort_by == "created_at":
            result.sort(key=lambda t: t["created_at"], reverse=True)
        elif sort_by == "due_date":
            result.sort(key=lambda t: t["due_date"] or "9999")
        
        return result
    
    def search(self, query):
        """Search tasks by title or description"""
        query = query.lower()
        return [
            t for t in self.tasks
            if query in t["title"].lower() or query in t["description"].lower()
        ]
    
    def statistics(self):
        """Get task statistics"""
        if not self.tasks:
            return None
        
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["status"] == "completed")
        pending = total - completed
        
        by_priority = {
            p: sum(1 for t in self.tasks if t["priority"] == p)
            for p in Config.PRIORITIES
        }
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": (completed / total * 100) if total > 0 else 0,
            "by_priority": by_priority
        }

# ========== CLI INTERFACE ==========

class TaskManagerCLI:
    """Command-line interface for Task Manager"""
    
    def __init__(self):
        self.manager = TaskManager()
    
    def display_banner(self):
        """Display welcome banner"""
        print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   📋 TASK MANAGER - Week 1 Capstone Project                   ║
║                                                               ║
║   A complete CLI task management application                  ║
║   Built with Python fundamentals from Week 1                  ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
        """)
    
    def display_menu(self):
        """Display main menu"""
        print("""
┌─────────────────────────────────────────┐
│              MAIN MENU                  │
├─────────────────────────────────────────┤
│  1. ➕ Add New Task                     │
│  2. 📋 View All Tasks                   │
│  3. ⏳ View Pending Tasks               │
│  4. ✅ View Completed Tasks             │
│  5. ✓  Mark Task Complete               │
│  6. ✏️  Update Task                      │
│  7. 🗑️  Delete Task                      │
│  8. 🔍 Search Tasks                     │
│  9. 📊 View Statistics                  │
│  0. 💾 Save & Exit                      │
└─────────────────────────────────────────┘
        """)
    
    def format_task(self, task):
        """Format a single task for display"""
        status_icon = Config.STATUS_ICONS.get(task["status"], "⬜")
        priority_icon = Config.PRIORITY_COLORS.get(task["priority"], "⚪")
        
        due = f" 📅 Due: {task['due_date']}" if task.get("due_date") else ""
        
        return f"""
    {status_icon} [{task['id']:03d}] {task['title']} {priority_icon}
       {task['description'] or 'No description'}
       Priority: {task['priority'].capitalize()} | Status: {task['status'].capitalize()}{due}
       Created: {task['created_at'][:19]}
        """
    
    def display_tasks(self, tasks, title="Tasks"):
        """Display a list of tasks"""
        print(f"\n{'=' * 55}")
        print(f"  {title} ({len(tasks)} items)")
        print("=" * 55)
        
        if not tasks:
            print("\n  No tasks found.\n")
            return
        
        for task in tasks:
            print(self.format_task(task))
    
    def get_input(self, prompt, required=True, options=None):
        """Get validated user input"""
        while True:
            value = input(prompt).strip()
            
            if not value and required:
                print("  ❌ This field is required")
                continue
            
            if not value:
                return ""
            
            if options and value.lower() not in options:
                print(f"  ❌ Choose from: {', '.join(options)}")
                continue
            
            return value
    
    def get_int(self, prompt):
        """Get integer input"""
        while True:
            try:
                return int(input(prompt).strip())
            except ValueError:
                print("  ❌ Please enter a valid number")
    
    def handle_add(self):
        """Handle adding a new task"""
        print("\n--- ➕ Add New Task ---\n")
        
        title = self.get_input("  Title: ")
        description = self.get_input("  Description (optional): ", required=False)
        priority = self.get_input("  Priority (high/medium/low): ",
                                  options=Config.PRIORITIES)
        due_date = self.get_input("  Due date YYYY-MM-DD (optional): ", required=False)
        
        success, result = self.manager.add(title, description, priority, due_date or None)
        
        if success:
            print(f"\n  ✅ Task added successfully! (ID: {result['id']})")
        else:
            print(f"\n  ❌ Failed to add task:")
            for error in result:
                print(f"     - {error}")
    
    def handle_complete(self):
        """Handle marking a task complete"""
        print("\n--- ✓ Mark Task Complete ---\n")
        
        task_id = self.get_int("  Enter Task ID: ")
        success, result = self.manager.complete(task_id)
        
        if success:
            if result == "Already completed":
                print(f"\n  ℹ️ Task is already completed")
            else:
                print(f"\n  ✅ Task '{result['title']}' marked complete!")
        else:
            print(f"\n  ❌ {result}")
    
    def handle_update(self):
        """Handle updating a task"""
        print("\n--- ✏️ Update Task ---\n")
        
        task_id = self.get_int("  Enter Task ID: ")
        task = self.manager.get(task_id)
        
        if not task:
            print("\n  ❌ Task not found")
            return
        
        print(f"\n  Current task: {task['title']}")
        print("  (Press Enter to keep current value)\n")
        
        title = self.get_input(f"  New title [{task['title']}]: ", required=False)
        description = self.get_input(f"  New description [{task['description'][:30]}...]: ", 
                                     required=False)
        priority = self.get_input(f"  New priority [{task['priority']}]: ",
                                  required=False, options=Config.PRIORITIES + [""])
        
        updates = {}
        if title:
            updates["title"] = title
        if description:
            updates["description"] = description
        if priority:
            updates["priority"] = priority
        
        if updates:
            success, result = self.manager.update(task_id, **updates)
            if success:
                print(f"\n  ✅ Task updated successfully!")
            else:
                print(f"\n  ❌ {result}")
        else:
            print("\n  ℹ️ No changes made")
    
    def handle_delete(self):
        """Handle deleting a task"""
        print("\n--- 🗑️ Delete Task ---\n")
        
        task_id = self.get_int("  Enter Task ID: ")
        task = self.manager.get(task_id)
        
        if not task:
            print("\n  ❌ Task not found")
            return
        
        print(f"\n  Task: {task['title']}")
        confirm = self.get_input("  Are you sure? (yes/no): ", options=["yes", "no"])
        
        if confirm.lower() == "yes":
            success, result = self.manager.delete(task_id)
            if success:
                print(f"\n  🗑️ Task deleted!")
            else:
                print(f"\n  ❌ {result}")
        else:
            print("\n  ℹ️ Deletion cancelled")
    
    def handle_search(self):
        """Handle searching tasks"""
        print("\n--- 🔍 Search Tasks ---\n")
        
        query = self.get_input("  Search query: ")
        results = self.manager.search(query)
        
        self.display_tasks(results, f"Search Results for '{query}'")
    
    def handle_statistics(self):
        """Handle displaying statistics"""
        stats = self.manager.statistics()
        
        if not stats:
            print("\n  No tasks to analyze")
            return
        
        print(f"""
╔═══════════════════════════════════════════════════════════════╗
║                      📊 STATISTICS                            ║
╠═══════════════════════════════════════════════════════════════╣
║  Total Tasks:      {stats['total']:>5}                                    ║
║  Completed:        {stats['completed']:>5} ({stats['completion_rate']:.1f}%)                           ║
║  Pending:          {stats['pending']:>5}                                    ║
╠═══════════════════════════════════════════════════════════════╣
║  By Priority:                                                 ║
║    🔴 High:        {stats['by_priority']['high']:>5}                                    ║
║    🟡 Medium:      {stats['by_priority']['medium']:>5}                                    ║
║    🟢 Low:         {stats['by_priority']['low']:>5}                                    ║
╚═══════════════════════════════════════════════════════════════╝
        """)
    
    def run(self):
        """Main application loop"""
        self.display_banner()
        print(f"  📂 Loaded {len(self.manager.tasks)} task(s)")
        
        while True:
            self.display_menu()
            choice = self.get_input("  Enter choice (0-9): ",
                                    options=[str(i) for i in range(10)])
            
            if choice == "1":
                self.handle_add()
            elif choice == "2":
                tasks = self.manager.list(sort_by="priority")
                self.display_tasks(tasks, "All Tasks")
            elif choice == "3":
                tasks = self.manager.list(status="pending", sort_by="priority")
                self.display_tasks(tasks, "Pending Tasks")
            elif choice == "4":
                tasks = self.manager.list(status="completed")
                self.display_tasks(tasks, "Completed Tasks")
            elif choice == "5":
                self.handle_complete()
            elif choice == "6":
                self.handle_update()
            elif choice == "7":
                self.handle_delete()
            elif choice == "8":
                self.handle_search()
            elif choice == "9":
                self.handle_statistics()
            elif choice == "0":
                self.manager.storage.save(self.manager.tasks)
                print("\n  💾 Tasks saved successfully!")
                print("  👋 Goodbye!\n")
                break

# ========== MAIN ENTRY POINT ==========

if __name__ == "__main__":
    app = TaskManagerCLI()
    app.run()
