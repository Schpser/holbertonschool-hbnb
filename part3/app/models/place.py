from app.models.base_model import BaseModel
from app.models.user import User

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if len(title) == 0 or len(title) > 100:
            raise ValueError("title name must be between 1 and 100 characters")
        if not isinstance(price, (int, float)):
            raise ValueError("price must be a number")
        if price <= 0:
            raise ValueError("price must be postive value")
        if latitude < -90 or latitude > 90:
            raise ValueError ("Must be within the range of -90.0 to 90.0")
        if longitude < -180 or longitude > 180:
            raise ValueError("Must be within the range of -180.0 to 180.0")
        if not isinstance(owner, User):
            raise ValueError("owner must be a User instance")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def update(self, data):
        """Update place attributes with validation"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self):
        """Convert the object to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'amenities': [amenity.id for amenity in self.amenities],
            'created_at': self.created_at.isoformat() if hasattr(self, 'created_at') else None,
            'updated_at': self.updated_at.isoformat() if hasattr(self, 'updated_at') else None
        }
