"""
MINI PROJECT 1: Student Grade Manager
=====================================
A complete student grade management system using files

Features:
1. Add students with grades
2. Save/Load from CSV
3. Calculate statistics
4. Generate reports
5. Error handling throughout
"""

import csv
import json
import os

print("=" * 50)
print("STUDENT GRADE MANAGER")
print("=" * 50)

# Data structure
students = []

# TODO: Implement these functions

def add_student(name, grades):
    """Add student with grades dict {'subject': score}"""
    pass

def save_to_csv(filename):
    """Save students to CSV file"""
    pass

def load_from_csv(filename):
    """Load students from CSV file"""
    pass

def get_student_average(name):
    """Get average grade for a student"""
    pass

def get_class_statistics():
    """Return class stats: avg, highest, lowest"""
    pass

def generate_report(output_file):
    """Generate text report of all students"""
    pass

# Main menu
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Save to File")
        print("4. Load from File")
        print("5. View Statistics")
        print("6. Generate Report")
        print("7. Exit")
        
        choice = input("Choice: ")
        
        # TODO: Implement menu logic with error handling
        
        if choice == "7":
            break

if __name__ == "__main__":
    main()
