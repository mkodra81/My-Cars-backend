# My Cars Backend - Setup Complete! ✅

## Project Overview

A complete Django REST Framework backend for managing cars with role-based access control.

### Key Features Implemented:

✅ **User Management**
- User registration with profile (client/admin roles)
- JWT-based authentication
- Password change functionality
- User profile with phone and address

✅ **Client Features**
- View only their own cars
- Create, edit, and delete cars
- Upload car images
- Manage car details (brand, model, year, color, license, VIN, mileage, notes)

✅ **Admin Features**
- View all client users
- Create, edit, and delete users
- View detailed user information with their cars
- Manage cars for any user (create, edit, delete)
- Upload images for any user's car

## Quick Start Guide

### 1. Make sure dependencies are installed:
```bash
pip install -r requirements.txt
```

### 2. Database is already migrated ✅

### 3. Create Admin User

**Option A: Using Python script**
```bash
python create_admin.py
```

**Option B: Using Django command**
```bash
python manage.py createsuperuser
```
Then manually set the role to 'admin' in the admin panel.

**Option C: Default admin credentials**
If you used the setup, an admin user should already exist:
- Username: `admin`
- Password: `admin123`
- Email: `admin@example.com`

### 4. Start the Server
```bash
python manage.py runserver
```

The API will be available at: `http://localhost:8000`

## Testing the API

### Method 1: Using the test script
```bash
python test_api.py
```

### Method 2: Using Postman or cURL

#### 1. Register a new client:
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"testuser\",\"email\":\"test@example.com\",\"first_name\":\"Test\",\"last_name\":\"User\",\"password\":\"TestPass123!\",\"password2\":\"TestPass123!\"}"
```

#### 2. Login to get JWT token:
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"testuser\",\"password\":\"TestPass123!\"}"
```

#### 3. Use the access token for authenticated requests:
```bash
curl -X GET http://localhost:8000/api/cars/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## API Endpoints Summary

### Authentication
- `POST /api/register/` - Register new user
- `POST /api/token/` - Login (get JWT tokens)
- `POST /api/token/refresh/` - Refresh access token
- `PUT /api/change-password/` - Change password
- `POST /api/logout/` - Logout (blacklist refresh token)
- `GET /api/me/` - Get current user info

### Client Car Management
- `GET /api/cars/` - List my cars
- `POST /api/cars/` - Create a new car
- `GET /api/cars/{id}/` - Get car details
- `PUT /api/cars/{id}/` - Update car
- `PATCH /api/cars/{id}/` - Partial update car
- `DELETE /api/cars/{id}/` - Delete car
- `POST /api/cars/{id}/upload-image/` - Upload car image

### Admin User Management
- `GET /api/admin/users/` - List all clients
- `POST /api/admin/users/` - Create a new client
- `GET /api/admin/users/{id}/` - Get user details with their cars
- `PUT /api/admin/users/{id}/` - Update user
- `DELETE /api/admin/users/{id}/` - Delete user

### Admin Car Management (for specific users)
- `GET /api/admin/users/{user_id}/cars/` - List user's cars
- `POST /api/admin/users/{user_id}/cars/` - Create car for user
- `GET /api/admin/users/{user_id}/cars/{car_id}/` - Get car details
- `PUT /api/admin/users/{user_id}/cars/{car_id}/` - Update user's car
- `DELETE /api/admin/users/{user_id}/cars/{car_id}/` - Delete user's car
- `POST /api/admin/users/{user_id}/cars/{car_id}/upload-image/` - Upload image

## Database Models

### UserProfile
- Links to Django User model
- `role`: 'client' or 'admin'
- `phone`: Optional phone number
- `address`: Optional address
- Timestamps (created_at, updated_at)

### Car
- `owner`: Foreign key to User
- `brand`: Car manufacturer
- `model`: Car model name
- `year`: Manufacturing year
- `color`: Car color
- `license`: License plate (unique)
- `vin`: Vehicle ID Number (optional)
- `mileage`: Current mileage in km
- `image`: Car photo (optional)
- `notes`: Additional notes (optional)
- Timestamps (created_at, updated_at)

## Django Admin Panel

Access at: `http://localhost:8000/admin/`

Login with superuser credentials to:
- View and manage all users
- View and manage all cars
- View user profiles
- Access Django's built-in admin features

## Project Structure

```
my_cars_backend/
├── backend/                    # Main app
│   ├── models.py              # UserProfile & Car models
│   ├── serializers.py         # API serializers
│   ├── views.py               # API views & viewsets
│   ├── urls.py                # API URL routing
│   ├── admin.py               # Django admin configuration
│   └── migrations/            # Database migrations
├── my_cars_backend/           # Project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
├── media/                     # Uploaded files (car images)
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── create_admin.py            # Admin user creation script
├── create_admin.bat           # Windows batch script
├── test_api.py                # API testing script
├── README.md                  # API documentation
└── .gitignore                 # Git ignore file
```

## Security Features

✅ JWT token authentication
✅ Token blacklisting on logout
✅ Password validation
✅ Role-based access control
✅ CORS headers configured
✅ Admin-only endpoints protected

## Next Steps

1. **Test the API** using `test_api.py` or Postman
2. **Create frontend** to consume this API
3. **Deploy to production** (remember to change settings for production)
4. **Add more features** like car maintenance records, service history, etc.

## Production Checklist

Before deploying to production:
- [ ] Set `DEBUG = False` in settings.py
- [ ] Change `SECRET_KEY` to a secure random value
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up proper CORS_ALLOWED_ORIGINS
- [ ] Use PostgreSQL instead of SQLite
- [ ] Configure media/static files hosting (S3, etc.)
- [ ] Set up HTTPS
- [ ] Use environment variables for sensitive data
- [ ] Set up proper logging
- [ ] Configure email backend for notifications

## Support

For issues or questions:
1. Check the README.md for API documentation
2. Review the test_api.py for usage examples
3. Check Django logs for errors

---

**Project Status: ✅ READY FOR USE**

The backend is fully functional and ready for frontend integration or API testing!

