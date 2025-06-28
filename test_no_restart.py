#!/usr/bin/env python3
"""
Test script to verify that sandbox operations don't trigger server restarts
"""

import os
import sys
import tempfile
import time
import shutil

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import PythonSandbox

def test_sandbox_isolation():
    """Test that sandbox operations don't create files that would trigger Flask reloader"""
    print("Testing sandbox isolation...")
    
    # Create sandbox instance
    sandbox = PythonSandbox()
    
    # Test Python code execution
    test_code = """
import os
import sys
print("Hello from sandbox!")
print(f"Current directory: {os.getcwd()}")
print(f"Python path: {sys.path[0]}")

# Try to create some files that might trigger reloader
with open("test_file.py", "w") as f:
    f.write("# This is a test file")

with open("core.py", "w") as f:
    f.write("# This simulates a core.py file")
"""
    
    print("Executing test code in sandbox...")
    result = sandbox.execute_python_code(test_code)
    
    print(f"Execution successful: {result['success']}")
    print(f"Output: {result['stdout']}")
    if result['stderr']:
        print(f"Errors: {result['stderr']}")
    
    # Check sandbox directory location
    print(f"Sandbox base directory: {sandbox.base_sandbox_dir}")
    
    # Verify it's in system temp, not in project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    temp_dir = tempfile.gettempdir()
    
    if project_dir.lower() in sandbox.base_sandbox_dir.lower():
        print("⚠️  WARNING: Sandbox is in project directory - may trigger restarts!")
    elif temp_dir.lower() in sandbox.base_sandbox_dir.lower():
        print("✅ GOOD: Sandbox is in system temp directory")
    else:
        print(f"❓ UNKNOWN: Sandbox location unclear - {sandbox.base_sandbox_dir}")
    
    # List sandbox contents
    if os.path.exists(sandbox.base_sandbox_dir):
        print(f"Sandbox contents:")
        for item in os.listdir(sandbox.base_sandbox_dir):
            item_path = os.path.join(sandbox.base_sandbox_dir, item)
            if os.path.isdir(item_path):
                print(f"  📁 {item}/")
                try:
                    for subitem in os.listdir(item_path):
                        print(f"    📄 {subitem}")
                except PermissionError:
                    print(f"    (Permission denied)")
            else:
                print(f"  📄 {item}")

if __name__ == "__main__":
    test_sandbox_isolation()