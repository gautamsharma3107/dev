"""
MINI PROJECT 2: Configuration Manager
=====================================
A JSON-based configuration manager with validation

Features:
1. Load/Save JSON config
2. Get/Set values with dot notation
3. Validate config schema
4. Default values
5. Custom exceptions
"""

import json
import os

print("=" * 50)
print("CONFIGURATION MANAGER")
print("=" * 50)

# Custom exceptions
class ConfigError(Exception):
    """Base config exception"""
    pass

class ConfigNotFoundError(ConfigError):
    """Config file not found"""
    pass

class ConfigValidationError(ConfigError):
    """Config validation failed"""
    pass

class ConfigManager:
    """Manages application configuration"""
    
    def __init__(self, filename="config.json"):
        self.filename = filename
        self.config = {}
        self.defaults = {}
    
    def set_defaults(self, defaults):
        """Set default configuration values"""
        # TODO: Implement
        pass
    
    def load(self):
        """Load configuration from file"""
        # TODO: Implement with error handling
        pass
    
    def save(self):
        """Save configuration to file"""
        # TODO: Implement with error handling
        pass
    
    def get(self, key, default=None):
        """Get config value using dot notation
        Example: config.get('database.host')
        """
        # TODO: Implement
        pass
    
    def set(self, key, value):
        """Set config value using dot notation"""
        # TODO: Implement
        pass
    
    def validate(self, schema):
        """Validate config against schema"""
        # TODO: Implement
        pass

# Example usage
def main():
    config = ConfigManager("app_config.json")
    
    # Set defaults
    config.set_defaults({
        "app_name": "MyApp",
        "version": "1.0",
        "database": {
            "host": "localhost",
            "port": 5432
        },
        "debug": False
    })
    
    # TODO: Demonstrate all features
    print("Implement ConfigManager features!")

if __name__ == "__main__":
    main()
