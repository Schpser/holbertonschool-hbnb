# 🏠 HBnB - Holberton BnB API

A RESTful API for a BnB (Bed and Breakfast) management system built with Flask and Flask-RESTX.

## 🚀 Features

- **User Management** - Create, read, update users
- **Place Management** - Manage rental properties with detailed information
- **Amenity System** - Handle property amenities and features
- **Review System** - User reviews and ratings (1-5 stars)
- **RESTful API** - Fully compliant REST API with proper HTTP status codes
- **Data Validation** - Comprehensive input validation and error handling
- **Auto-generated Documentation** - Interactive Swagger/OpenAPI documentation
- **In-Memory Storage** - No database required for development

## 📚 API Documentation

Once the application is running, access the interactive API documentation at:

```
http://localhost:5000/api/v1/
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### 1. Clone the repository

```bash
git clone https://github.com/Schpser/holbertonschool-hbnb.git
cd holbertonschool-hbnb/part2
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Quick Start

Start the development server:

```bash
flask run
# or
python -m flask run
```

The API will be available at:

```
http://localhost:5000/api/v1/
```

## 📋 API Endpoints

### Users

```http
GET    /api/v1/users/                 # List all users
POST   /api/v1/users/                 # Create a new user
GET    /api/v1/users/{user_id}        # Get user details
PUT    /api/v1/users/{user_id}        # Update user information
```

### Places

```http
GET    /api/v1/places/                 # List all places
POST   /api/v1/places/                 # Create a new place
GET    /api/v1/places/{place_id}       # Get place details with owner and amenities
PUT    /api/v1/places/{place_id}       # Update place information
```

### Amenities

```http
GET    /api/v1/amenities/              # List all amenities
POST   /api/v1/amenities/              # Create a new amenity
GET    /api/v1/amenities/{amenity_id}  # Get amenity details
PUT    /api/v1/amenities/{amenity_id}  # Update amenity information
```

### Reviews

```http
GET    /api/v1/reviews/                  # List all reviews
POST   /api/v1/reviews/                  # Create a new review
GET    /api/v1/reviews/{review_id}       # Get review details
PUT    /api/v1/reviews/{review_id}       # Update review information
DELETE /api/v1/reviews/{review_id}       # Delete a review
GET    /api/v1/places/{place_id}/reviews # Get reviews for a specific place
```

## 🎯 Usage Examples

### Create a User

```bash
curl -X POST http://localhost:5000/api/v1/users/ \
    -H "Content-Type: application/json" \
    -d '{
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    }'
```

### Create a Place

```bash
curl -X POST http://localhost:5000/api/v1/places/ \
    -H "Content-Type: application/json" \
    -d '{
        "title": "Cozy Apartment",
        "description": "A beautiful apartment in the city center",
        "price": 120.0,
        "latitude": 48.8566,
        "longitude": 2.3522,
        "owner_id": "user-uuid-here",
        "amenities": ["amenity-uuid-here"]
    }'
```

### Create a Review

```bash
curl -X POST http://localhost:5000/api/v1/reviews/ \
    -H "Content-Type: application/json" \
    -d '{
        "text": "Amazing place with great amenities!",
        "rating": 5,
        "user_id": "user-uuid-here",
        "place_id": "place-uuid-here"
    }'
```

## 🧪 Testing

### Run all tests

```bash
python -m unittest discover app/tests/ -v
```

### Run specific test suites

#### Model tests

```bash
python -m unittest app/tests/test_models.py -v
```

#### API endpoint tests

```bash
python -m unittest app/tests/test_endpoints.py -v
```

### Test coverage

The test suite includes:

- ✅ 18 total tests (9 model tests + 9 endpoint tests)
- ✅ 100% test pass rate
- ✅ Data validation testing
- ✅ Error handling testing
- ✅ Relationship testing

## 🏗️ Project Structure

```
holbertonschool-hbnb/
├── app/
│   ├── __init__.py              # Flask application factory
│   ├── models/                  # Data models
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── amenity.py
│   │   └── review.py
│   ├── services/                # Business logic
│   │   └── facade.py
│   ├── persistence/             # Data access layer
│   │   ├── __init__.py
│   │   └── repository.py
│   └── api/                     # API routes
│       └── v1/
│           ├── users.py
│           ├── places.py
│           ├── amenities.py
│           └── reviews.py
├── tests/                       # Test suites
│   ├── test_models.py
│   └── test_endpoints.py
├── requirements.txt             # Project dependencies
└── README.md                    # This file
```

## 🔧 Data Models

### User

- `id` (UUID) - Unique identifier
- `first_name` (string) - User's first name (1-50 characters)
- `last_name` (string) - User's last name (1-50 characters)
- `email` (string) - Valid email address
- `created_at` (datetime) - Creation timestamp
- `updated_at` (datetime) - Last update timestamp

### Place

- `id` (UUID) - Unique identifier
- `title` (string) - Place title (1-100 characters)
- `description` (string) - Place description
- `price` (float) - Price per night (positive number)
- `latitude` (float) - Geographic coordinate (-90 to 90)
- `longitude` (float) - Geographic coordinate (-180 to 180)
- `owner` (User) - Property owner
- `amenities` (list) - List of Amenity objects
- `reviews` (list) - List of Review objects

### Amenity

- `id` (UUID) - Unique identifier
- `name` (string) - Amenity name (1-50 characters, required)

### Review

- `id` (UUID) - Unique identifier
- `text` (string) - Review content (1-1000 characters, required)
- `rating` (integer) - Rating score (1-5)
- `user` (User) - Review author
- `place` (Place) - Reviewed place

## 🛡️ Validation Rules

- **Users:** Email format validation, name length limits
- **Places:** Price must be positive, latitude/longitude bounds
- **Amenities:** Name required and length limits
- **Reviews:** Rating between 1-5, text content required

## 🐛 Troubleshooting

### Common Issues

**Port already in use:**

```bash
# Kill process on port 5000
sudo lsof -t -i tcp:5000 | xargs kill -9
```

**Module not found errors:**

```bash
# Ensure you're in the correct directory
cd holbertonschool-hbnb/part2

# Reinstall dependencies
pip install -r requirements.txt
```

**Virtual environment issues:**

```bash
# Reactivate virtual environment
source venv/bin/activate
```

## 🤝 Contributing

- Fork the repository
- Create a feature branch: `git checkout -b feature/amazing-feature`
- Commit changes: `git commit -m 'Add amazing feature'`
- Push to branch: `git push origin feature/amazing-feature`
- Open a Pull Request

## 📄 License

This project is part of the Holberton School curriculum.

## 👥 Authors

Rpok & Schps

## 🙏 Acknowledgments

Holberton School staff and peers

Flask and Flask-RESTX communities