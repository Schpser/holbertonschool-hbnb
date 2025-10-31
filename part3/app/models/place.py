from app import db
from .base_model import BaseModel
from sqlalchemy.orm import validates
from .association import place_amenity

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    reviews = db.relationship('Review', backref='place', lazy=True, cascade='all, delete-orphan')
    amenities = db.relationship('Amenity', secondary=place_amenity, 
                               backref=db.backref('places', lazy=True), lazy=True)

    @validates('title')
    def validate_title(self, key, title):
        if not title or len(title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        if len(title) > 255:
            raise ValueError("Title must be less than 255 characters")
        return title.strip()

    @validates('price')
    def validate_price(self, key, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        return price

    @validates('latitude')
    def validate_latitude(self, key, latitude):
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        return latitude

    @validates('longitude')
    def validate_longitude(self, key, longitude):
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        return longitude

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'title': self.title,
            'description': self.description,
            'price': float(self.price) if self.price else None,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner_id,
            'amenities': [amenity.to_dict() for amenity in self.amenities] if self.amenities else []
        })
        return base_dict
