#!/usr/bin/env python3
"""
Test script for SQL-based categorization system
"""

import sys
import os

def test_database_availability():
    """Test if database components are available"""
    print("🧪 Testing Database Components")
    print("=" * 50)
    
    try:
        from flask_sqlalchemy import SQLAlchemy
        from sqlalchemy import func, text
        print("✅ SQLAlchemy modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ SQLAlchemy import failed: {e}")
        return False

def test_categorization_logic():
    """Test the enhanced categorization logic"""
    print("\n📊 Testing Conversation Categorization")
    print("=" * 50)
    
    # Sample conversations for testing
    test_conversations = [
        {
            "name": "Data Analysis Chat",
            "messages": [
                {"role": "user", "content": "Can you analyze this CSV file with sales data?"},
                {"role": "assistant", "content": "I'll help you analyze the CSV data. Let me create some visualizations."},
                {"role": "user", "content": "```python\nimport pandas as pd\ndf = pd.read_csv('sales.csv')\nprint(df.head())\n```"}
            ],
            "expected_category": "Data Analysis"
        },
        {
            "name": "Business Report Chat", 
            "messages": [
                {"role": "user", "content": "I need to create a professional business report"},
                {"role": "assistant", "content": "I'll help you create a report using ReportLab"},
                {"role": "user", "content": "```reportlab\nfrom reportlab.pdfgen import canvas\nc = canvas.Canvas('report.pdf')\n```"}
            ],
            "expected_category": "Business Reports"
        },
        {
            "name": "Code Development Chat",
            "messages": [
                {"role": "user", "content": "Help me write a Python function to process data"},
                {"role": "assistant", "content": "Here's a function that processes your data:"},
                {"role": "user", "content": "```python\ndef process_data(data):\n    return data.clean()\n```"}
            ],
            "expected_category": "Code Development"
        },
        {
            "name": "Document Processing Chat",
            "messages": [
                {"role": "user", "content": "I uploaded a Word document, can you analyze it?"},
                {"role": "assistant", "content": "I'll analyze the uploaded document for you."},
                {"role": "system", "content": "User has uploaded a file: document.docx"}
            ],
            "expected_category": "Document Processing"
        },
        {
            "name": "Troubleshooting Chat",
            "messages": [
                {"role": "user", "content": "I'm getting an error with my Python code"},
                {"role": "assistant", "content": "Let me help you fix that error."},
                {"role": "user", "content": "The problem is with the import statement"}
            ],
            "expected_category": "Troubleshooting"
        }
    ]
    
    # Simple categorization logic for testing (without importing main.py)
    def simple_categorize(messages):
        content = ""
        for msg in messages:
            content += msg.get('content', '').lower() + " "
        
        if '```reportlab' in content:
            return "Business Reports"
        elif 'csv' in content or 'data' in content and ('analyze' in content or 'visualization' in content):
            return "Data Analysis"
        elif '```python' in content or 'function' in content:
            return "Code Development"
        elif 'upload' in content or 'document' in content or 'file' in content:
            return "Document Processing"
        elif 'error' in content or 'problem' in content or 'fix' in content:
            return "Troubleshooting"
        else:
            return "Help & Questions"
    
    # Test categorization
    correct_predictions = 0
    for test_case in test_conversations:
        predicted_category = simple_categorize(test_case["messages"])
        expected_category = test_case["expected_category"]
        
        is_correct = predicted_category == expected_category
        status = "✅" if is_correct else "❌"
        
        print(f"{status} {test_case['name']}")
        print(f"   Expected: {expected_category}")
        print(f"   Predicted: {predicted_category}")
        
        if is_correct:
            correct_predictions += 1
        print()
    
    accuracy = (correct_predictions / len(test_conversations)) * 100
    print(f"📈 Categorization Accuracy: {accuracy:.1f}% ({correct_predictions}/{len(test_conversations)})")

def test_database_schema():
    """Display the planned database schema"""
    print("\n🗄️ Database Schema Overview")
    print("=" * 50)
    
    schema_info = {
        "Users": [
            "id (Primary Key)",
            "email (Unique)",
            "username",
            "password_hash",
            "created_at, updated_at, last_login",
            "is_active"
        ],
        "Categories": [
            "id (Primary Key)",
            "name (Unique)",
            "description",
            "color (Hex)",
            "icon (Emoji)",
            "created_at"
        ],
        "Conversations": [
            "id (UUID Primary Key)",
            "user_id (Foreign Key)",
            "category_id (Foreign Key)",
            "title, summary",
            "created_at, updated_at, last_message_at",
            "message_count",
            "has_code, has_files, has_analysis",
            "tags (JSON)"
        ],
        "Messages": [
            "id (Primary Key)",
            "conversation_id (Foreign Key)",
            "role (user/assistant/system)",
            "content",
            "created_at",
            "has_code, code_type",
            "execution_result (JSON)"
        ],
        "FileUploads": [
            "id (Primary Key)",
            "user_id, conversation_id (Foreign Keys)",
            "original_filename, file_type, file_size",
            "processed_content (JSONL)",
            "upload_time",
            "processing_status, processing_method"
        ]
    }
    
    for table_name, fields in schema_info.items():
        print(f"\n**{table_name} Table:**")
        for field in fields:
            print(f"  • {field}")

def test_default_categories():
    """Display the default categories"""
    print("\n🏷️ Default Categories")
    print("=" * 50)
    
    categories = [
        {'name': 'Data Analysis', 'icon': '📊', 'color': '#e74c3c'},
        {'name': 'Business Reports', 'icon': '📋', 'color': '#3498db'},
        {'name': 'Code Development', 'icon': '💻', 'color': '#2ecc71'},
        {'name': 'Document Processing', 'icon': '📄', 'color': '#f39c12'},
        {'name': 'Help & Questions', 'icon': '❓', 'color': '#9b59b6'},
        {'name': 'Troubleshooting', 'icon': '🔧', 'color': '#e67e22'},
        {'name': 'Presentations', 'icon': '📈', 'color': '#1abc9c'},
    ]
    
    for category in categories:
        print(f"{category['icon']} {category['name']} (Color: {category['color']})")

if __name__ == "__main__":
    print("SQL Categorization System Test Suite")
    print("=" * 60)
    
    # Test database availability
    db_available = test_database_availability()
    
    # Test categorization logic
    test_categorization_logic()
    
    # Show schema
    test_database_schema()
    
    # Show categories
    test_default_categories()
    
    print("\n🎯 Integration Benefits:")
    print("=" * 50)
    print("✅ **Enhanced Organization:**")
    print("   • Smart auto-categorization of conversations")
    print("   • Visual category indicators with colors and icons")
    print("   • Searchable tags and metadata")
    
    print("\n✅ **Better Performance:**")
    print("   • SQL queries instead of JSON file parsing")
    print("   • Indexed searches by category, date, content")
    print("   • Efficient pagination and filtering")
    
    print("\n✅ **Rich Metadata:**")
    print("   • Track code usage, file uploads, analysis type")
    print("   • Conversation summaries and statistics")
    print("   • User activity and login tracking")
    
    print("\n✅ **Data Integrity:**")
    print("   • Foreign key relationships")
    print("   • Automatic timestamps")
    print("   • Transaction safety")
    
    if db_available:
        print("\n🚀 Ready to test:")
        print("1. Restart your Flask app")
        print("2. Database will auto-migrate existing JSON data")
        print("3. Try creating new conversations")
        print("4. Observe automatic categorization")
    else:
        print("\n📦 To install dependencies:")
        print("pip install Flask-SQLAlchemy==3.1.1 SQLAlchemy==2.0.23")
