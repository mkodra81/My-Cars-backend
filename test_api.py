"""
Test script to verify API endpoints

This script creates test users and tests the main API endpoints.
Make sure the server is running before executing this script.

Usage:
    python test_api.py
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def print_response(title, response):
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")

def test_api():
    print("Starting API Tests...")

    # Test 1: Register a new client
    print("\n1. Registering a new client user...")
    register_data = {
        "username": "test_client",
        "email": "client@example.com",
        "first_name": "Test",
        "last_name": "Client",
        "password": "TestPass123!",
        "password2": "TestPass123!",
        "role": "client",
        "phone": "555-1234",
        "address": "123 Test Street"
    }
    response = requests.post(f"{BASE_URL}/register/", json=register_data)
    print_response("Register Client", response)

    # Test 2: Login as client
    print("\n2. Logging in as client...")
    login_data = {
        "username": "test_client",
        "password": "TestPass123!"
    }
    response = requests.post("http://localhost:8000/api/token/", json=login_data)
    print_response("Client Login", response)

    if response.status_code == 200:
        client_token = response.json()["access"]
        client_refresh = response.json()["refresh"]
        headers = {"Authorization": f"Bearer {client_token}"}

        # Test 3: Get current user info
        print("\n3. Getting current user info...")
        response = requests.get(f"{BASE_URL}/me/", headers=headers)
        print_response("Current User Info", response)

        # Test 4: Create a car
        print("\n4. Creating a car...")
        car_data = {
            "brand": "Toyota",
            "model": "Camry",
            "year": 2023,
            "color": "Blue",
            "license": "TEST123",
            "vin": "1HGBH41JXMN109186",
            "mileage": 15000,
            "notes": "Test car"
        }
        response = requests.post(f"{BASE_URL}/cars/", json=car_data, headers=headers)
        print_response("Create Car", response)

        car_id = None
        if response.status_code == 201:
            car_id = response.json()["id"]

        # Test 5: List client's cars
        print("\n5. Listing client's cars...")
        response = requests.get(f"{BASE_URL}/cars/", headers=headers)
        print_response("List Cars", response)

        # Test 6: Update car
        if car_id:
            print(f"\n6. Updating car {car_id}...")
            update_data = {
                "brand": "Toyota",
                "model": "Camry",
                "year": 2023,
                "color": "Red",
                "license": "TEST123",
                "mileage": 16000
            }
            response = requests.put(f"{BASE_URL}/cars/{car_id}/", json=update_data, headers=headers)
            print_response("Update Car", response)

        # Test 7: Change password
        print("\n7. Changing password...")
        password_data = {
            "old_password": "TestPass123!",
            "new_password": "NewPass456!"
        }
        response = requests.put(f"{BASE_URL}/change-password/", json=password_data, headers=headers)
        print_response("Change Password", response)

        # Test 8: Logout
        print("\n8. Logging out...")
        logout_data = {"refresh": client_refresh}
        response = requests.post(f"{BASE_URL}/logout/", json=logout_data, headers=headers)
        print_response("Logout", response)

    # Test 9: Try to register an admin user (should default to client)
    print("\n9. Registering another user...")
    register_data2 = {
        "username": "test_user2",
        "email": "user2@example.com",
        "first_name": "User",
        "last_name": "Two",
        "password": "TestPass123!",
        "password2": "TestPass123!"
    }
    response = requests.post(f"{BASE_URL}/register/", json=register_data2)
    print_response("Register User 2", response)

    print("\n" + "="*60)
    print("API Tests Complete!")
    print("="*60)
    print("\nNote: To test admin endpoints, create a superuser with:")
    print("python manage.py createsuperuser")
    print("\nThen login with those credentials to get an admin token.")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("\nERROR: Cannot connect to the server.")
        print("Make sure the Django server is running:")
        print("python manage.py runserver")
    except Exception as e:
        print(f"\nERROR: {e}")

