# 🏠 HBnB - Part 3: Authentication & Database Integration

![HBnB - Auth & DB](HBnB%20-%20Auth%20%26%20DB.png)

A secure, database-backed RESTful API for the HBnB management system with JWT authentication and SQLAlchemy ORM.

## 🚀 Features

- **JWT Authentication** - Secure token-based user authentication
- **Role-Based Access Control** - Admin and user permission levels
- **Database Persistence** - SQLite (development) / MySQL (production)
- **Password Security** - Bcrypt hashing with pepper
- **SQLAlchemy ORM** - Object-relational mapping for all entities
- **User Management** - Secure registration and profile management
- **Place Management** - CRUD operations with ownership validation
- **Review System** - Authenticated user reviews with rating validation
- **Amenity System** - Admin-managed property features
- **RESTful API** - Industry-standard REST architecture
- **Auto-generated Documentation** - Interactive Swagger/OpenAPI docs

## 📚 API Documentation

Once the application is running, access the interactive API documentation at:

```
http://localhost:5000/api/v1/
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- SQLite3 (included with Python)

### 1. Clone the repository

```bash
git clone https://github.com/Schpser/holbertonschool-hbnb.git
cd holbertonschool-hbnb/part3
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

### 4. Configure environment variables

Create a `.env` file in the project root:

```bash
SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_key_here
PEPPER=your_pepper_value_here
DATABASE_URL=sqlite:///hbnb_dev.db
```

### 5. Initialize the database

```bash
# Create database schema
sqlite3 instance/hbnb_dev.db < schema.sql

# Load initial data (admin user and amenities)
sqlite3 instance/hbnb_dev.db < initial_data.sql

# OR create admin user programmatically
python create_admin.py
```

## 🏃‍♂️ Quick Start

Start the development server:

```bash
python run.py
# or
flask run
```

The API will be available at:

```
http://localhost:5000/api/v1/
```

## 📋 API Endpoints

### Authentication

```http
POST   /api/v1/auth/login          # User login, returns JWT token
```

### Users

```http
GET    /api/v1/users/              # List all users (Public)
POST   /api/v1/users/              # Create a new user (Admin only)
GET    /api/v1/users/{user_id}     # Get user details (Public)
PUT    /api/v1/users/{user_id}     # Update user (Owner or Admin)
```

### Places

```http
GET    /api/v1/places/             # List all places (Public)
POST   /api/v1/places/             # Create a new place (Authenticated)
GET    /api/v1/places/{place_id}   # Get place details (Public)
PUT    /api/v1/places/{place_id}   # Update place (Owner or Admin)
DELETE /api/v1/places/{place_id}   # Delete place (Owner or Admin)
```

### Reviews

```http
GET    /api/v1/reviews/                  # List all reviews (Public)
POST   /api/v1/reviews/                  # Create a new review (Authenticated)
GET    /api/v1/reviews/{review_id}       # Get review details (Public)
PUT    /api/v1/reviews/{review_id}       # Update review (Author or Admin)
DELETE /api/v1/reviews/{review_id}       # Delete review (Author or Admin)
GET    /api/v1/places/{place_id}/reviews # Get reviews for a place (Public)
```

### Amenities

```http
GET    /api/v1/amenities/              # List all amenities (Public)
POST   /api/v1/amenities/              # Create a new amenity (Admin only)
GET    /api/v1/amenities/{amenity_id}  # Get amenity details (Public)
PUT    /api/v1/amenities/{amenity_id}  # Update amenity (Admin only)
```

## 🎯 Usage Examples

### Login and Get Token

```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
    -H "Content-Type: application/json" \
    -d '{
        "email": "admin@hbnb.io",
        "password": "admin1234"
    }'
```

### Create a User (Admin)

```bash
curl -X POST http://localhost:5000/api/v1/users/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_JWT_TOKEN" \
    -d '{
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "securepassword123"
    }'
```

### Create a Place (Authenticated)

```bash
curl -X POST http://localhost:5000/api/v1/places/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_JWT_TOKEN" \
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

### Create a Review (Authenticated)

```bash
curl -X POST http://localhost:5000/api/v1/reviews/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_JWT_TOKEN" \
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

#### API tests

```bash
python -m unittest app/tests/test_api.py -v
```

#### Model tests

```bash
python -m unittest app/tests/test_all_models.py -v
```

### Test coverage

The test suite includes:

- ✅ Authentication and authorization testing
- ✅ JWT token validation
- ✅ Database CRUD operations
- ✅ Relationship integrity tests
- ✅ Access control validation
- ✅ Error handling testing

## 🏗️ Project Structure

```
holbertonschool-hbnb/part3/
├── app/
│   ├── __init__.py              # Flask application factory
│   ├── models/                  # SQLAlchemy models
│   │   ├── base_model.py        # Base entity with common attributes
│   │   ├── user.py              # User model with password hashing
│   │   ├── place.py             # Place entity
│   │   ├── review.py            # Review entity
│   │   ├── amenity.py           # Amenity entity
│   │   └── association.py       # Many-to-many relationships
│   ├── services/                # Business logic
│   │   ├── facade.py            # Facade pattern implementation
│   │   └── repositories/        # Database repositories
│   │       ├── user_repository.py
│   │       ├── place_repository.py
│   │       ├── review_repository.py
│   │       └── amenity_repository.py
│   ├── persistence/             # Data access layer
│   │   └── repository.py        # SQLAlchemy base repository
│   └── api/                     # API routes
│       └── v1/
│           ├── auth.py          # Authentication endpoints
│           ├── users.py         # User endpoints
│           ├── places.py        # Place endpoints
│           ├── amenities.py     # Amenity endpoints
│           └── reviews.py       # Review endpoints
├── tests/                       # Test suites
│   ├── test_api.py
│   └── test_all_models.py
├── config.py                    # Configuration classes
├── run.py                       # Application entry point
├── requirements.txt             # Project dependencies
├── schema.sql                   # Database schema definition
├── initial_data.sql             # Initial data seeding
├── create_admin.py              # Admin user creation script
└── README.md                    # This file
```

## 🔧 Data Models

### User

- `id` (UUID) - Unique identifier
- `first_name` (string) - User's first name (1-50 characters)
- `last_name` (string) - User's last name (1-50 characters)
- `email` (string) - Valid email address (unique)
- `password` (string) - Hashed password (bcrypt)
- `is_admin` (boolean) - Administrator flag
- `created_at` (datetime) - Creation timestamp
- `updated_at` (datetime) - Last update timestamp

### Place

- `id` (UUID) - Unique identifier
- `title` (string) - Place title (1-100 characters)
- `description` (string) - Place description
- `price` (float) - Price per night (positive number)
- `latitude` (float) - Geographic coordinate (-90 to 90)
- `longitude` (float) - Geographic coordinate (-180 to 180)
- `owner_id` (UUID) - Foreign key to User
- `amenities` (list) - Many-to-many with Amenity
- `reviews` (list) - One-to-many with Review

### Review

- `id` (UUID) - Unique identifier
- `text` (string) - Review content (1-1000 characters, required)
- `rating` (integer) - Rating score (1-5)
- `user_id` (UUID) - Foreign key to User (author)
- `place_id` (UUID) - Foreign key to Place
- `created_at` (datetime) - Creation timestamp
- `updated_at` (datetime) - Last update timestamp

### Amenity

- `id` (UUID) - Unique identifier
- `name` (string) - Amenity name (1-50 characters, unique)
- `created_at` (datetime) - Creation timestamp
- `updated_at` (datetime) - Last update timestamp

## � Database Architecture Diagram

The following diagram illustrates the complete database architecture with all entities, relationships, and the three-layer architecture pattern used in this project:

![HBnB Architecture Diagram](HBnB%20P3.png)

This diagram shows:
- **Presentation Layer**: API endpoints and request handling
- **Business Logic Layer**: Services and repositories
- **Data Layer**: SQLAlchemy models and database relationships

## �🛡️ Security Features

- **Password Hashing** - Bcrypt with pepper for additional security layer
- **JWT Tokens** - Secure, stateless authentication mechanism
- **Token Expiration** - Configurable token lifetime (default: 1 hour)
- **Role-Based Access** - `is_admin` flag for privilege control
- **Input Validation** - Comprehensive data validation at all levels
- **SQL Injection Protection** - SQLAlchemy ORM prevents SQL injection
- **Ownership Validation** - Users can only modify their own resources

## 🔒 Access Control Rules

### Public Access
- Read operations: GET all users, places, reviews, amenities

### Authenticated Users
- Create places and reviews
- Update own places and reviews
- Update own profile (except email and password)
- Cannot review own places
- Cannot review same place twice

### Administrators
- All authenticated user privileges
- Create new users
- Modify any user's data (including email and password)
- Create and modify amenities
- Bypass ownership restrictions on places and reviews

## 🐛 Troubleshooting

### Common Issues

**Database not found:**

```bash
# Create instance directory and initialize database
mkdir -p instance
sqlite3 instance/hbnb_dev.db < schema.sql
```

**JWT token expired:**

```bash
# Login again to get a new token
curl -X POST http://localhost:5000/api/v1/auth/login \
    -H "Content-Type: application/json" \
    -d '{"email": "your@email.com", "password": "yourpassword"}'
```

**Port already in use:**

```bash
# Kill process on port 5000
sudo lsof -t -i tcp:5000 | xargs kill -9
```

**Module not found errors:**

```bash
# Ensure you're in the correct directory
cd holbertonschool-hbnb/part3

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

Flask, SQLAlchemy, and Flask-JWT-Extended communities