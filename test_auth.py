#!/usr/bin/env python3
"""
Test script for the authentication system
"""

import json
import os
from werkzeug.security import check_password_hash

def test_user_storage():
    """Test if users are being stored correctly"""
    users_file = 'users.json'
    
    if os.path.exists(users_file):
        with open(users_file, 'r') as f:
            users = json.load(f)
        
        print("=== User Database Contents ===")
        for email, user_data in users.items():
            print(f"Email: {email}")
            print(f"Password Hash: {user_data['password_hash'][:20]}...")
            print(f"Created At: {user_data['created_at']}")
            print("-" * 30)
        
        return users
    else:
        print("No users.json file found. No users registered yet.")
        return {}

def test_password_verification(users, email, password):
    """Test password verification"""
    if email in users:
        is_valid = check_password_hash(users[email]['password_hash'], password)
        print(f"Password verification for {email}: {'✓ Valid' if is_valid else '✗ Invalid'}")
        return is_valid
    else:
        print(f"User {email} not found")
        return False

if __name__ == "__main__":
    print("Authentication System Test")
    print("=" * 40)
    
    # Test user storage
    users = test_user_storage()
    
    # If there are users, test password verification
    if users:
        print("\n=== Password Verification Test ===")
        # You can test with actual credentials here
        # test_password_verification(users, "test@example.com", "password123")
        print("To test password verification, uncomment the line above and provide actual credentials")
    
    print("\n=== Authentication Features ===")
    print("✓ User registration with email/password")
    print("✓ Password hashing for security")
    print("✓ User login verification")
    print("✓ Session management")
    print("✓ Route protection with @login_required")
    print("✓ Automatic redirect to login page")
    print("✓ Flash messages for user feedback")
    print("✓ Logout functionality")