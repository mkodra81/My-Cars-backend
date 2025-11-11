# API Changes - UserViewSet Integration

## Overview
The user registration and account deletion endpoints have been consolidated into a single `UserViewSet`, following the same pattern as `CarViewSet`.

## API Endpoint Changes

### OLD Endpoints (Deprecated)
- `POST /api/register/` - Register new user
- `DELETE /api/delete-account/` - Delete account

### NEW Endpoints

#### User Management (UserViewSet)
- `POST /api/users/` - Register new user (public access)
- `GET /api/users/` - List all users (authenticated, admin only)
- `GET /api/users/{id}/` - Get user details (authenticated)
- `PUT /api/users/{id}/` - Update user (authenticated, owner or admin)
- `PATCH /api/users/{id}/` - Partial update user (authenticated, owner or admin)
- `DELETE /api/users/{id}/` - Delete user account (authenticated, owner or admin)

#### Other Endpoints (Unchanged)
- `GET /api/me/` - Get current user info
- `PUT /api/change-password/` - Change password

#### Car Management (CarViewSet)
- `POST /api/cars/` - Create new car
- `GET /api/cars/` - List all cars
- `GET /api/cars/{id}/` - Get car details
- `PUT /api/cars/{id}/` - Update car
- `PATCH /api/cars/{id}/` - Partial update car
- `DELETE /api/cars/{id}/` - Delete car

## Migration Guide

### Registration
**Before:**
```bash
POST /api/register/
```

**After:**
```bash
POST /api/users/
```

### Account Deletion
**Before:**
```bash
DELETE /api/delete-account/
```

**After:**
```bash
DELETE /api/users/{user_id}/
# Example: DELETE /api/users/1/
```

## Permissions
- **Create (POST /api/users/)**: Public access (AllowAny)
- **List/Retrieve/Update/Delete**: Authenticated users only
- **Delete**: Users can only delete their own account (unless staff/admin)

## Benefits
1. ✅ Consistent API design (all resources follow RESTful ViewSet pattern)
2. ✅ Automatic route generation via Django REST Framework router
3. ✅ Support for additional CRUD operations if needed
4. ✅ Better alignment with REST principles

