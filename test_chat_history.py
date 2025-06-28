#!/usr/bin/env python3
"""
Test script to verify chat history functionality
"""

import json
import os
import time
from main import save_chat_to_history, get_user_chat_history, generate_chat_name

def test_chat_history():
    """Test the chat history system"""
    print("🧪 Testing Chat History System")
    print("=" * 50)
    
    # Test user email
    test_email = "test@example.com"
    
    # Create test chat data
    test_messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello, can you help me with data analysis?"},
        {"role": "assistant", "content": "Of course! I'd be happy to help you with data analysis."}
    ]
    
    # Test chat name generation
    print("1. Testing chat name generation...")
    chat_name = generate_chat_name(test_messages)
    print(f"   Generated name: '{chat_name}'")
    
    # Test saving chat
    print("\n2. Testing save chat to history...")
    chat_data = {
        'id': 'test-chat-123',
        'name': chat_name,
        'messages': test_messages,
        'created_at': time.time(),
        'updated_at': time.time()
    }
    
    # Note: This will fail if user doesn't exist, which is expected
    try:
        result = save_chat_to_history(test_email, chat_data)
        print(f"   Save result: {result}")
    except Exception as e:
        print(f"   Expected error (user doesn't exist): {e}")
    
    # Test getting chat history
    print("\n3. Testing get chat history...")
    try:
        history = get_user_chat_history(test_email)
        print(f"   Chat history length: {len(history)}")
    except Exception as e:
        print(f"   Error getting history: {e}")
    
    print("\n✅ Chat history tests completed!")

def test_name_generation():
    """Test various chat name generation scenarios"""
    print("\n🏷️  Testing Chat Name Generation")
    print("=" * 50)
    
    test_cases = [
        {
            "messages": [
                {"role": "user", "content": "Can you create a chart from my data?"}
            ],
            "expected_type": "Data Visualization"
        },
        {
            "messages": [
                {"role": "user", "content": "Help me write a Python function"}
            ],
            "expected_type": "Code Discussion"
        },
        {
            "messages": [
                {"role": "user", "content": "I uploaded a CSV file, can you analyze it?"}
            ],
            "expected_type": "Data Analysis"
        },
        {
            "messages": [
                {"role": "user", "content": "What is machine learning?"}
            ],
            "expected_type": "Help & Questions"
        },
        {
            "messages": [
                {"role": "user", "content": "I'm getting an error in my code"}
            ],
            "expected_type": "Troubleshooting"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        name = generate_chat_name(test_case["messages"])
        print(f"{i}. Message: '{test_case['messages'][0]['content'][:50]}...'")
        print(f"   Generated: '{name}'")
        print(f"   Expected type: {test_case['expected_type']}")
        print()

if __name__ == "__main__":
    test_chat_history()
    test_name_generation()
    
    print("\n🎯 Manual Testing Instructions:")
    print("1. Start the app: python main.py")
    print("2. Register/login with a user account")
    print("3. Start a conversation")
    print("4. Click 'New Chat' - should save current chat to history")
    print("5. Check sidebar for the saved chat")
    print("6. Click on a saved chat - should load it")
    print("7. Try rename/delete functions")
    print("\n🔧 If issues persist:")
    print("- Check browser console for JavaScript errors")
    print("- Check server logs for Python errors")
    print("- Verify users.json file structure")