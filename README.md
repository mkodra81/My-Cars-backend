```
POST /api/admin/users/
Authorization: Bearer <admin_access_token>
Content-Type: application/json

{
  "username": "jane_smith",
  "email": "jane@example.com",
  "first_name": "Jane",
  "last_name": "Smith",
  "password": "password123",
  "password2": "password123",
  "role": "client",
  "phone": "555-5678",
  "address": "456 Oak Ave"
}
```

#### Update a Client
```
PUT /api/admin/users/{user_id}/
Authorization: Bearer <admin_access_token>
Content-Type: application/json

{
  "username": "jane_smith",
  "email": "jane@example.com",
  "first_name": "Jane",
  "last_name": "Smith",
  "is_active": true,
  "role": "client",
  "phone": "555-9999"
}
```

#### Delete a Client
```
DELETE /api/admin/users/{user_id}/
Authorization: Bearer <admin_access_token>
```

#### List Cars for a Specific User
```
GET /api/admin/users/{user_id}/cars/
Authorization: Bearer <admin_access_token>
```

#### Create a Car for a User
```
POST /api/admin/users/{user_id}/cars/
Authorization: Bearer <admin_access_token>
Content-Type: application/json

{
  "brand": "Honda",
  "model": "Civic",
  "year": 2022,
  "color": "Silver",
  "license": "XYZ789",
  "mileage": 5000
}
```

#### Update a User's Car
```
PUT /api/admin/users/{user_id}/cars/{car_id}/
Authorization: Bearer <admin_access_token>
Content-Type: application/json

{
  "brand": "Honda",
  "model": "Civic",
  "year": 2022,
  "color": "Black",
  "license": "XYZ789",
  "mileage": 6000
}
```

#### Delete a User's Car
```
DELETE /api/admin/users/{user_id}/cars/{car_id}/
Authorization: Bearer <admin_access_token>
```

#### Upload Image to a User's Car
```
POST /api/admin/users/{user_id}/cars/{car_id}/upload-image/
Authorization: Bearer <admin_access_token>
Content-Type: multipart/form-data

image: <file>
```

## Models

### UserProfile
- `user`: OneToOne relationship with Django User
- `role`: Choice field (client/admin)
- `phone`: Optional phone number
- `address`: Optional address
- `created_at`: Auto timestamp
- `updated_at`: Auto timestamp

### Car
- `owner`: Foreign key to User
- `brand`: Car manufacturer
- `model`: Car model
- `year`: Manufacturing year
- `color`: Car color (optional)
- `license`: License plate (unique)
- `vin`: Vehicle Identification Number (optional)
- `mileage`: Current mileage in kilometers
- `image`: Car image (optional)
- `notes`: Additional notes (optional)
- `created_at`: Auto timestamp
- `updated_at`: Auto timestamp

## Response Format

### Success Response
```json
{
  "id": 1,
  "brand": "Toyota",
  "model": "Camry",
  "year": 2023,
  "color": "Blue",
  "license": "ABC123",
  "vin": "1HGBH41JXMN109186",
  "mileage": 15000,
  "owner": 2,
  "owner_name": "John Doe",
  "owner_username": "john_doe",
  "image": "/media/cars/car_123.jpg",
  "notes": "Excellent condition",
  "created_at": "2025-11-10T10:30:00Z",
  "updated_at": "2025-11-10T15:45:00Z"
}
```

### Error Response
```json
{
  "detail": "Error message here"
}
```

or

```json
{
  "field_name": ["Error message for this field"]
}
```

## Authentication

All protected endpoints require a JWT access token in the Authorization header:

```
Authorization: Bearer <access_token>
```

Access tokens expire after 60 minutes. Use the refresh token to get a new access token.

## Security Notes

1. Always use HTTPS in production
2. Keep your SECRET_KEY secure
3. Set `DEBUG = False` in production
4. Configure `ALLOWED_HOSTS` properly
5. Use strong passwords
6. Regularly rotate JWT tokens

## Testing

You can test the API using:
- Postman
- cURL
- Python requests library
- Django REST Framework browsable API (when logged in)

Access the browsable API at: `http://localhost:8000/api/`

## Admin Panel

Access Django admin panel at: `http://localhost:8000/admin/`

Use your superuser credentials to log in.

## License

This project is licensed under the MIT License.
# My Cars Backend API

A comprehensive Django REST API for managing cars with role-based access control (Client and Admin).

## Features

### General Features
- User registration and authentication (JWT-based)
- Password change functionality
- Role-based access control (Client/Admin)

### Client Features
- View their own cars only
- Create new cars
- Edit existing cars
- Delete cars
- Upload car images

### Admin Features
- View all clients
- Create, edit, and delete users
- View detailed user information
- Manage cars for any user
- Add, edit, or delete cars for specific users

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

When prompted, make sure to note the username and password for admin access.

### 4. Run the Development Server

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

## API Endpoints

### Authentication

#### Register a New User
```
POST /api/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "securePassword123",
  "password2": "securePassword123",
  "role": "client",  // optional, defaults to "client"
  "phone": "555-1234",  // optional
  "address": "123 Main St"  // optional
}
```

#### Login (Get JWT Token)
```
POST /api/token/
Content-Type: application/json

{
  "username": "john_doe",
  "password": "securePassword123"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Refresh Token
```
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Change Password
```
PUT /api/change-password/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "old_password": "oldPassword123",
  "new_password": "newPassword456"
}
```

#### Logout
```
POST /api/logout/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Get Current User Info
```
GET /api/me/
Authorization: Bearer <access_token>
```

### Client Car Management

#### List My Cars
```
GET /api/cars/
Authorization: Bearer <access_token>
```

#### Create a New Car
```
POST /api/cars/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "brand": "Toyota",
  "model": "Camry",
  "year": 2023,
  "color": "Blue",
  "license": "ABC123",
  "vin": "1HGBH41JXMN109186",  // optional
  "mileage": 15000,
  "notes": "Excellent condition"  // optional
}
```

#### Get Car Details
```
GET /api/cars/{car_id}/
Authorization: Bearer <access_token>
```

#### Update a Car
```
PUT /api/cars/{car_id}/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "brand": "Toyota",
  "model": "Camry",
  "year": 2023,
  "color": "Red",
  "license": "ABC123",
  "mileage": 16000
}
```

#### Partial Update a Car
```
PATCH /api/cars/{car_id}/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "mileage": 17000,
  "notes": "Oil changed"
}
```

#### Delete a Car
```
DELETE /api/cars/{car_id}/
Authorization: Bearer <access_token>
```

#### Upload Car Image
```
POST /api/cars/{car_id}/upload-image/
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

image: <file>
```

### Admin Endpoints

**Note:** All admin endpoints require an admin role (superuser or user with role='admin')

#### List All Clients
```
GET /api/admin/users/
Authorization: Bearer <admin_access_token>
```

#### Get Client Details (with their cars)
```
GET /api/admin/users/{user_id}/
Authorization: Bearer <admin_access_token>
```

#### Create a New Client

