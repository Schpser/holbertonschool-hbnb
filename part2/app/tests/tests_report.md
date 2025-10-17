git checkout# 📊 HBnB API Testing Report

## ✅ Successful Tests

### 1. API Endpoints Tests

```http
# ✅ POST /api/v1/users/
# 201 Created - User creation with valid data
POST /api/v1/users/
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com"
}

# ✅ POST /api/v1/users/  
# 400 Bad Request - Invalid email validation
POST /api/v1/users/
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "invalid-email"
}

# ✅ POST /api/v1/users/
# 400 Bad Request - Required fields validation  
POST /api/v1/users/
Content-Type: application/json

{
  "first_name": "",
  "last_name": "Doe",
  "email": "test@example.com"
}

# ✅ GET /api/v1/users/{id}
# 404 Not Found - Retrieval of non-existent user
GET /api/v1/users/non-existent-id

# ✅ GET /api/v1/users/
# 200 OK - Retrieval of all users
GET /api/v1/users/

# ✅ POST /api/v1/places/
# 201 Created - Place creation with relationships
POST /api/v1/places/
Content-Type: application/json

{
  "title": "Cozy Apartment",
  "description": "A nice place",
  "price": 100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id": "user-uuid",
  "amenities": ["amenity-uuid"]
}

# ✅ POST /api/v1/places/
# 400 Bad Request - Invalid price validation
POST /api/v1/places/
Content-Type: application/json

{
  "title": "Invalid Place",
  "price": -100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id": "user-uuid",
  "amenities": []
}

# ✅ POST /api/v1/amenities/
# 201 Created - Amenity creation
POST /api/v1/amenities/
Content-Type: application/json

{
  "name": "Wi-Fi"
}

# ✅ POST /api/v1/reviews/
# 201 Created - Review creation
POST /api/v1/reviews/
Content-Type: application/json

{
  "text": "Great place!",
  "rating": 5,
  "user_id": "user-uuid",
  "place_id": "place-uuid"
}

# ✅ DELETE /api/v1/reviews/{id}
# 200 OK - Review deletion
DELETE /api/v1/reviews/review-uuid
```

# ✅ Complete User → Place → Review flow
# User creation
POST /api/v1/users/
{"first_name": "Alice", "last_name": "Smith", "email": "alice@example.com"}

# Place creation  
POST /api/v1/places/
{"title": "Luxury Villa", "price": 200.0, "latitude": 48.8566, "longitude": 2.3522, "owner_id": "user-uuid", "amenities": []}

# Review creation
POST /api/v1/reviews/
{"text": "Amazing stay!", "rating": 5, "user_id": "user-uuid", "place_id": "place-uuid"}

# ✅ Entity relationship management
GET /api/v1/places/place-uuid
# Returns place with owner details and reviews

✅ Correct HTTP status codes
200 OK - Successful requests
201 Created - Resource created
400 Bad Request - Validation errors
404 Not Found - Resource not found
500 Internal Server Error - Server errors

✅ Email format validation
POST /api/v1/users/
{"email": "invalid-email"} → 400 Bad Request

✅ Positive price required  
POST /api/v1/places/
{"price": -100.0} → 400 Bad Request

✅ Latitude/Longitude within valid ranges
POST /api/v1/places/
{"latitude": 100.0} → 400 Bad Request
{"longitude": 200.0} → 400 Bad Request

✅ Ratings between 1 and 5
POST /api/v1/reviews/
{"rating": 6} → 400 Bad Request

✅ Required fields not empty
POST /api/v1/amenities/
{"name": ""} → 400 Bad Request

## 🎯 Feature Coverage

```
Feature	Status	Tests
Users CRUD	✅	5 tests
Places CRUD	✅	2 tests
Amenities CRUD	✅	2 tests
Reviews CRUD	✅	3 tests
Validation	✅	8 tests
Relations	✅	4 tests
Error Handling	✅	6 tests
```