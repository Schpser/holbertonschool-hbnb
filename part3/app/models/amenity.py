from app import db
from .base_model import BaseModel
from sqlalchemy.orm import validates

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(255), nullable=False, unique=True)

    @validates('name')
    def validate_name(self, key, name):
        if not name or len(name.strip()) == 0:
            raise ValueError("Amenity name cannot be empty")
        if len(name) > 255:
            raise ValueError("Amenity name must be less than 255 characters")
        return name.strip()

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'name': self.name
        })
        return base_dict
