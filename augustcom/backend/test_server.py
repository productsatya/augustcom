#!/usr/bin/env python
"""
Test script to debug Django server startup
"""
import os
import sys
import django

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopcore.settings')

try:
    django.setup()
    print("✅ Django setup successful!")
    
    # Test imports
    from catalog.models import Category, Product
    print("✅ Models imported successfully!")
    
    # Test database connection
    from django.db import connection
    cursor = connection.cursor()
    print("✅ Database connection successful!")
    
    # Test API views
    from catalog.views import CategoryViewSet, ProductViewSet
    print("✅ Views imported successfully!")
    
    print("\n🎉 All tests passed! Django is ready to run.")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
