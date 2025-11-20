# My Cars Backend API

A Django REST Framework API for managing vehicle information with role-based access control.

## What is this?

This backend provides a complete car management system where:

- **Clients** can register and manage their personal vehicle information (brand, model, year, color, license plate, etc.)
- **Admins** have full control to manage all users and their vehicles

The API uses JWT (JSON Web Token) authentication for secure access and implements role-based permissions to ensure users can only access data they're authorized to see.

## Key Features

### For Vehicle Owners (Clients)
- Register and authenticate securely
- Add and manage their own vehicles
- Track vehicle details including brand, model, year, color, and license information
- Upload vehicle images
- Full CRUD operations on their own cars only

### For Administrators
- Full user management (create, view, update, delete users)
- Manage vehicles for any user
- View all clients and their associated vehicles
- Comprehensive oversight of the entire system

### Technical Features
- **JWT Authentication**: Secure token-based authentication with refresh tokens
- **Role-Based Access Control**: Client and Admin roles with appropriate permissions
- **RESTful API**: Standard REST endpoints following best practices
- **Database Models**: 
  - `CarDetails`: Stores vehicle specifications (brand, model, year, color)
  - `Car`: Main car entity with foreign key to CarDetails and owner
  - `UserProfile`: Extended user information with role, phone, and address
- **Django Admin Interface**: Built-in admin panel for quick data management

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
│   └── migrations/       # Database migrations
├── my_cars_backend/      # Django project settings
│   ├── settings.py       # Project configuration
│   └── urls.py           # Root URL configuration
└── manage.py             # Django management script
```

## API Overview

The API provides endpoints for:

- **Authentication**: Registration, login, logout, token refresh, password change
- **Client Endpoints**: CRUD operations on user's own vehicles
- **Admin Endpoints**: User management and vehicle management for all users

All endpoints return JSON responses and use JWT tokens for authentication.

## Database Schema

### CarDetails Model
Stores vehicle specifications that can be shared across multiple cars:
- Brand, Model, Year, Color

### Car Model
Main vehicle entity linked to an owner and car details:
- Foreign key to User (owner)
- Foreign key to CarDetails
- License plate (unique identifier)
- Timestamps

### UserProfile Model
Extended user information:
- Role (Client/Admin)
- Contact information (phone, address)
- Timestamps

## License

MIT License

