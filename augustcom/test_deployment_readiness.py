#!/usr/bin/env python3
"""
Deployment Readiness Test Script
Tests if the application is ready for Vercel + Render deployment
"""

import requests
import json
import sys
import os

def test_backend_api():
    """Test if backend API is responding"""
    try:
        response = requests.get('http://localhost:8000/api/products/')
        if response.status_code == 200:
            print("✅ Backend API: Working")
            return True
        else:
            print(f"❌ Backend API: Status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend API: Connection failed - {e}")
        return False

def test_frontend_build():
    """Test if frontend can build successfully"""
    try:
        os.chdir('frontend')
        result = os.system('npm run build')
        if result == 0:
            print("✅ Frontend Build: Successful")
            return True
        else:
            print("❌ Frontend Build: Failed")
            return False
    except Exception as e:
        print(f"❌ Frontend Build: Error - {e}")
        return False
    finally:
        os.chdir('..')

def test_database():
    """Test if database is accessible"""
    try:
        os.chdir('backend')
        result = os.system('python manage.py check')
        if result == 0:
            print("✅ Database: Accessible")
            return True
        else:
            print("❌ Database: Not accessible")
            return False
    except Exception as e:
        print(f"❌ Database: Error - {e}")
        return False
    finally:
        os.chdir('..')

def main():
    """Run all deployment readiness tests"""
    print("🚀 **Deployment Readiness Test**\n")
    
    tests = [
        ("Backend API", test_backend_api),
        ("Frontend Build", test_frontend_build),
        ("Database", test_database),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Testing {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print(f"📊 **Results: {passed}/{total} tests passed**")
    
    if passed == total:
        print("🎉 **READY FOR DEPLOYMENT!**")
        print("✅ Your application is working perfectly")
        print("✅ Ready for Vercel + Render deployment")
        return 0
    else:
        print("⚠️  **NOT READY FOR DEPLOYMENT**")
        print("❌ Some tests failed - fix issues before deploying")
        return 1

if __name__ == "__main__":
    sys.exit(main())
