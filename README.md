# My Cars Backend

A Django REST Framework API for managing vehicle information with role-based access control.

## What is this?

This backend provides a complete car management API where:

- **Clients** can register and manage their personal vehicle information (brand, model, year, color, license plate, etc.)
- **Admins** have full control to manage all users and their vehicles through comprehensive endpoints

The API uses JWT (JSON Web Token) authentication for secure access and implements role-based permissions to ensure users can only access data they're authorized to access.

## Key Features

### For Vehicle Owners (Clients)
- Register and authenticate securely
- Add and manage their own vehicles
- Track vehicle details including brand, model, year, color, and license information
- Full CRUD operations on their own cars only
- Update personal profile and password

### For Administrators
- Full user management (create, view, update, delete users)
- Manage vehicles for any user
- View all clients and their associated vehicles
- System-wide vehicle and user oversight
- Admin-only endpoints for elevated operations

### Technical Features
- **JWT Authentication**: Secure token-based authentication with refresh tokens
- **Role-Based Access Control**: Client and Admin roles with appropriate permissions
- **RESTful API**: Standard REST endpoints following best practices
- **Normalized Database**: Separated CarDetails model for efficient data storage
- **Django Admin Interface**: Built-in admin panel for quick data management
- **Permission Classes**: Fine-grained permission control on all endpoints

## Use Cases

This backend is perfect for:
- Personal vehicle tracking applications
- Car dealership management systems
- Fleet management solutions
- Automotive service centers managing customer vehicles
- Any application requiring multi-user vehicle data management

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## Technology Stack

- **Framework**: Django 5.2.8 with Django REST Framework
- **Authentication**: JSON Web Tokens (JWT) via Simple JWT
- **Database**: SQLite (default) - easily configurable to PostgreSQL, MySQL, etc.
- **Python**: 3.14+

## Project Structure

```
My-Cars-backend/
├── backend/               # Main application
│   ├── models.py         # CarDetails, Car, and UserProfile models
│   ├── serializers.py    # API serializers for data validation
│   ├── views.py          # API viewsets and endpoints
│   ├── urls.py           # URL routing
│   ├── admin.py          # Django admin configuration
│   └── migrations/       # Database migrations
├── my_cars_backend/      # Django project settings
│   ├── settings.py       # Project configuration
│   └── urls.py           # Root URL configuration
└── manage.py             # Django management script
```

## API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `POST /api/token/` - Login and get JWT tokens
- `POST /api/token/refresh/` - Refresh access token
- `POST /api/logout/` - Logout and blacklist token
- `PUT /api/change-password/` - Change user password
- `GET /api/me/` - Get current user info

### Client Endpoints
- `GET /api/cars/` - List user's cars
- `POST /api/cars/` - Create new car
- `GET /api/cars/{id}/` - Get car details
- `PUT /api/cars/{id}/` - Update car
- `DELETE /api/cars/{id}/` - Delete car

### Admin Endpoints
- `GET /api/users/` - List all users
- `POST /api/users/` - Create new user
- `GET /api/users/{id}/` - Get user details
- `PUT /api/users/{id}/` - Update user
- `DELETE /api/users/{id}/` - Delete user
- `POST /api/cars/owner/{id}/` - Create car for specific user

## Database Models

### CarDetails Model
Stores vehicle specifications:
- Brand, Model, Year, Color

### Car Model
Main vehicle entity:
- Foreign key to User (owner)
- Foreign key to CarDetails
- License plate (unique identifier)
- Timestamps

### UserProfile Model
Extended user information:
- Role (Client/Admin)
- Contact information (phone, address)
- Timestamps

## Features Overview

### Authentication Flow
- User registration with role assignment
- Secure login with JWT tokens
- Token refresh mechanism
- Token blacklisting on logout
- Password change with validation

### Client Operations
- View personal vehicle collection
- Add new vehicles with complete details
- Edit existing vehicle information
- Delete vehicles with ownership verification
- Profile management

### Admin Operations
- Complete user management
- Vehicle management across all users
- Create cars on behalf of users
- System-wide data access
- User and vehicle CRUD operations

## License

MIT License

