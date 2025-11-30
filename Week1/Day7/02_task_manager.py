"""
Day 7 - CLI Task Manager
========================
A command-line task management application with file storage

Features:
- Add, view, update, and delete tasks
- Mark tasks as complete
- Filter by status and priority
- Save/load from JSON file
- Full error handling

Skills Used:
- Variables and data types
- Lists and dictionaries
- Functions with parameters
- File handling (JSON)
- Exception handling
- Input validation
"""

import json
import os
from datetime import datetime

# ========== CONFIGURATION ==========
DATA_FILE = "tasks.json"

# ========== DATA STRUCTURE ==========
"""
Each task has:
{
    "id": int,
    "title": str,
    "description": str,
    "priority": str ("high", "medium", "low"),
    "completed": bool,
    "created_at": str (ISO format)
}
"""

# ========== HELPER FUNCTIONS ==========

def load_tasks():
    """Load tasks from JSON file, return empty list if file doesn't exist"""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Warning: Tasks file is corrupted. Starting fresh.")
        return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
        return True
    except IOError as e:
        print(f"❌ Error saving tasks: {e}")
        return False

def get_next_id(tasks):
    """Get the next available task ID"""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def validate_priority(priority):
    """Validate priority value"""
    valid_priorities = ["high", "medium", "low"]
    return priority.lower() in valid_priorities

def format_task(task):
    """Format a task for display"""
    status = "✅" if task["completed"] else "⬜"
    priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}
    priority = priority_emoji.get(task["priority"], "⚪")
    
    return f"""
    {status} [{task['id']}] {task['title']} {priority}
       Description: {task['description'] or 'No description'}
       Priority: {task['priority'].capitalize()}
       Created: {task['created_at']}
    """

# ========== CORE FUNCTIONS ==========

def add_task(tasks, title, description="", priority="medium"):
    """Add a new task to the list"""
    if not title.strip():
        print("❌ Error: Task title cannot be empty")
        return False
    
    if not validate_priority(priority):
        print("❌ Error: Priority must be 'high', 'medium', or 'low'")
        return False
    
    task = {
        "id": get_next_id(tasks),
        "title": title.strip(),
        "description": description.strip(),
        "priority": priority.lower(),
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(task)
    print(f"✅ Task added: '{task['title']}' (ID: {task['id']})")
    return True

def list_tasks(tasks, filter_status=None, filter_priority=None):
    """List all tasks with optional filters"""
    if not tasks:
        print("📋 No tasks found. Add some tasks to get started!")
        return
    
    # Apply filters
    filtered = tasks
    if filter_status == "completed":
        filtered = [t for t in filtered if t["completed"]]
    elif filter_status == "pending":
        filtered = [t for t in filtered if not t["completed"]]
    
    if filter_priority:
        filtered = [t for t in filtered if t["priority"] == filter_priority.lower()]
    
    if not filtered:
        print("📋 No tasks match the current filters.")
        return
    
    print(f"\n{'=' * 50}")
    print(f"📋 TASK LIST ({len(filtered)} tasks)")
    print("=" * 50)
    
    # Sort by priority (high -> medium -> low)
    priority_order = {"high": 0, "medium": 1, "low": 2}
    sorted_tasks = sorted(filtered, key=lambda t: priority_order.get(t["priority"], 3))
    
    for task in sorted_tasks:
        print(format_task(task))

def get_task_by_id(tasks, task_id):
    """Find a task by ID"""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def complete_task(tasks, task_id):
    """Mark a task as completed"""
    task = get_task_by_id(tasks, task_id)
    if not task:
        print(f"❌ Error: Task with ID {task_id} not found")
        return False
    
    if task["completed"]:
        print(f"ℹ️ Task '{task['title']}' is already completed")
        return True
    
    task["completed"] = True
    print(f"✅ Task '{task['title']}' marked as completed!")
    return True

def delete_task(tasks, task_id):
    """Delete a task by ID"""
    task = get_task_by_id(tasks, task_id)
    if not task:
        print(f"❌ Error: Task with ID {task_id} not found")
        return False
    
    tasks.remove(task)
    print(f"🗑️ Task '{task['title']}' deleted!")
    return True

def update_task(tasks, task_id, title=None, description=None, priority=None):
    """Update a task's details"""
    task = get_task_by_id(tasks, task_id)
    if not task:
        print(f"❌ Error: Task with ID {task_id} not found")
        return False
    
    if title:
        task["title"] = title.strip()
    if description is not None:
        task["description"] = description.strip()
    if priority:
        if not validate_priority(priority):
            print("❌ Error: Priority must be 'high', 'medium', or 'low'")
            return False
        task["priority"] = priority.lower()
    
    print(f"✅ Task '{task['title']}' updated!")
    return True

def get_statistics(tasks):
    """Get task statistics"""
    if not tasks:
        print("📊 No tasks to analyze")
        return
    
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    
    high = sum(1 for t in tasks if t["priority"] == "high")
    medium = sum(1 for t in tasks if t["priority"] == "medium")
    low = sum(1 for t in tasks if t["priority"] == "low")
    
    print(f"""
{'=' * 50}
📊 TASK STATISTICS
{'=' * 50}
Total Tasks:     {total}
Completed:       {completed} ({completed/total*100:.1f}%)
Pending:         {pending} ({pending/total*100:.1f}%)

By Priority:
  🔴 High:       {high}
  🟡 Medium:     {medium}
  🟢 Low:        {low}
{'=' * 50}
""")

# ========== INTERACTIVE MENU ==========

def display_menu():
    """Display the main menu"""
    print("""
╔════════════════════════════════════════╗
║         📋 TASK MANAGER                ║
╠════════════════════════════════════════╣
║  1. Add New Task                       ║
║  2. List All Tasks                     ║
║  3. List Pending Tasks                 ║
║  4. List Completed Tasks               ║
║  5. Mark Task as Complete              ║
║  6. Update Task                        ║
║  7. Delete Task                        ║
║  8. View Statistics                    ║
║  9. Save & Exit                        ║
╚════════════════════════════════════════╝
""")

def get_user_input(prompt, required=True, valid_options=None):
    """Get validated user input"""
    while True:
        value = input(prompt).strip()
        
        if not value and required:
            print("❌ This field is required")
            continue
        
        if not value and not required:
            return ""
        
        if valid_options and value.lower() not in valid_options:
            print(f"❌ Please choose from: {', '.join(valid_options)}")
            continue
        
        return value

def get_int_input(prompt):
    """Get integer input with validation"""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("❌ Please enter a valid number")

def interactive_add(tasks):
    """Interactive task addition"""
    print("\n--- Add New Task ---")
    title = get_user_input("Title: ")
    description = get_user_input("Description (optional): ", required=False)
    priority = get_user_input("Priority (high/medium/low): ", 
                              valid_options=["high", "medium", "low"])
    
    if add_task(tasks, title, description, priority):
        save_tasks(tasks)

def interactive_complete(tasks):
    """Interactive task completion"""
    print("\n--- Mark Task Complete ---")
    task_id = get_int_input("Enter Task ID: ")
    if complete_task(tasks, task_id):
        save_tasks(tasks)

def interactive_update(tasks):
    """Interactive task update"""
    print("\n--- Update Task ---")
    task_id = get_int_input("Enter Task ID: ")
    
    task = get_task_by_id(tasks, task_id)
    if not task:
        print(f"❌ Task with ID {task_id} not found")
        return
    
    print(f"Current: {task['title']}")
    new_title = get_user_input("New title (press Enter to keep): ", required=False)
    
    print(f"Current: {task['description'] or 'No description'}")
    new_desc = get_user_input("New description (press Enter to keep): ", required=False)
    
    print(f"Current: {task['priority']}")
    new_priority = get_user_input("New priority (press Enter to keep): ", 
                                   required=False,
                                   valid_options=["high", "medium", "low", ""])
    
    if update_task(tasks, task_id, 
                   title=new_title or None,
                   description=new_desc if new_desc else None,
                   priority=new_priority or None):
        save_tasks(tasks)

def interactive_delete(tasks):
    """Interactive task deletion"""
    print("\n--- Delete Task ---")
    task_id = get_int_input("Enter Task ID: ")
    
    task = get_task_by_id(tasks, task_id)
    if task:
        confirm = get_user_input(f"Delete '{task['title']}'? (yes/no): ",
                                 valid_options=["yes", "no"])
        if confirm.lower() == "yes":
            if delete_task(tasks, task_id):
                save_tasks(tasks)

def main():
    """Main application loop"""
    print("""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  Welcome to Task Manager - Your CLI Task Organizer!        ║
║                                                            ║
║  Manage your tasks efficiently from the command line.      ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Load existing tasks
    tasks = load_tasks()
    print(f"📂 Loaded {len(tasks)} task(s) from {DATA_FILE}")
    
    while True:
        display_menu()
        choice = get_user_input("Enter choice (1-9): ", 
                               valid_options=[str(i) for i in range(1, 10)])
        
        if choice == "1":
            interactive_add(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks, filter_status="pending")
        elif choice == "4":
            list_tasks(tasks, filter_status="completed")
        elif choice == "5":
            interactive_complete(tasks)
        elif choice == "6":
            interactive_update(tasks)
        elif choice == "7":
            interactive_delete(tasks)
        elif choice == "8":
            get_statistics(tasks)
        elif choice == "9":
            save_tasks(tasks)
            print("\n👋 Tasks saved! Goodbye!\n")
            break

# ========== RUN APPLICATION ==========

if __name__ == "__main__":
    main()
