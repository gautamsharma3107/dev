"""
EXERCISES: Protecting Views
===========================
Complete all exercises below
"""

# Exercise 1: Basic login_required decorator
# TODO: Create a dashboard view that:
# - Requires user to be logged in
# - Shows user's username and email
# - Displays recent activity

print("Exercise 1: Protected Dashboard View")
print("-" * 40)

# Your code here - create dashboard_view with @login_required




# Exercise 2: Class-based view with LoginRequiredMixin
# TODO: Create a ListView that:
# - Requires login
# - Shows only items belonging to current user
# - Uses LoginRequiredMixin

print("\n\nExercise 2: Protected ListView")
print("-" * 40)

# Your code here - create MyItemsListView class




# Exercise 3: Owner-only access with UserPassesTestMixin
# TODO: Create an UpdateView that:
# - Requires login
# - Only allows the item's owner to edit
# - Redirects with error message if unauthorized

print("\n\nExercise 3: Owner-Only UpdateView")
print("-" * 40)

# Your code here - create ItemUpdateView class




# Exercise 4: Custom decorator
# TODO: Create a decorator that:
# - Checks if user is a premium subscriber
# - Redirects to upgrade page if not premium
# - Shows appropriate message

print("\n\nExercise 4: Custom Premium Decorator")
print("-" * 40)

# Your code here - create premium_required decorator




# Exercise 5: Permission-based protection
# TODO: Create a view that:
# - Requires 'blog.add_post' permission
# - Returns 403 Forbidden if user lacks permission
# - Works with both function and class-based views

print("\n\nExercise 5: Permission-Based View")
print("-" * 40)

# Your code here - create permission-protected view
