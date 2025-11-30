"""
MINI PROJECT 3: Log File Analyzer
=================================
Analyze application log files

Features:
1. Parse log files
2. Filter by level (INFO, WARNING, ERROR)
3. Search by keyword
4. Generate statistics
5. Export filtered results
"""

import os
from datetime import datetime
from contextlib import contextmanager

print("=" * 50)
print("LOG FILE ANALYZER")
print("=" * 50)

# Sample log format: [2024-01-15 10:30:45] [INFO] Message here

class LogEntry:
    """Represents a single log entry"""
    
    def __init__(self, timestamp, level, message):
        self.timestamp = timestamp
        self.level = level
        self.message = message
    
    def __str__(self):
        return f"[{self.timestamp}] [{self.level}] {self.message}"

class LogAnalyzer:
    """Analyzes log files"""
    
    def __init__(self):
        self.entries = []
    
    def parse_line(self, line):
        """Parse a log line into LogEntry"""
        # TODO: Implement parsing
        # Format: [2024-01-15 10:30:45] [INFO] Message
        pass
    
    def load_file(self, filename):
        """Load and parse a log file"""
        # TODO: Implement with error handling
        pass
    
    def filter_by_level(self, level):
        """Return entries matching level"""
        # TODO: Implement
        pass
    
    def filter_by_date(self, start_date, end_date):
        """Return entries within date range"""
        # TODO: Implement
        pass
    
    def search(self, keyword):
        """Search entries by keyword"""
        # TODO: Implement
        pass
    
    def get_statistics(self):
        """Return log statistics"""
        # TODO: Return count by level, time range, etc.
        pass
    
    def export_filtered(self, entries, filename):
        """Export filtered entries to file"""
        # TODO: Implement
        pass

@contextmanager
def log_analyzer_session(filename):
    """Context manager for log analysis"""
    analyzer = LogAnalyzer()
    try:
        analyzer.load_file(filename)
        yield analyzer
    finally:
        print(f"Processed {len(analyzer.entries)} entries")

# Create sample log for testing
def create_sample_log():
    """Create a sample log file for testing"""
    log_content = """[2024-01-15 10:30:45] [INFO] Application started
[2024-01-15 10:30:46] [INFO] Loading configuration
[2024-01-15 10:30:47] [WARNING] Config file not found, using defaults
[2024-01-15 10:31:00] [INFO] Database connected
[2024-01-15 10:31:15] [ERROR] Failed to fetch user data
[2024-01-15 10:31:20] [INFO] Retrying connection
[2024-01-15 10:31:25] [INFO] User data loaded
[2024-01-15 10:32:00] [WARNING] High memory usage detected
[2024-01-15 10:33:00] [ERROR] Connection timeout
[2024-01-15 10:33:05] [INFO] Application shutting down
"""
    with open("sample.log", "w") as f:
        f.write(log_content)
    print("Created sample.log")

def main():
    # Create sample log
    create_sample_log()
    
    # TODO: Demonstrate analyzer features
    print("Implement LogAnalyzer features!")
    
    # Cleanup
    if os.path.exists("sample.log"):
        os.remove("sample.log")

if __name__ == "__main__":
    main()
