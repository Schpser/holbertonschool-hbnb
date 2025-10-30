from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()

        if not text or len(text.strip()) == 0:
            raise ValueError("text is required")
        if not isinstance(rating, int):
            raise ValueError("rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")

        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    def update(self, data):
        """Update review attributes with validation"""
        for key, value in data.items():
            if key == 'text':
                if not value or len(value.strip()) == 0:
                    raise ValueError("text is required")
                if len(value) > 1000:
                    raise ValueError("text must be at most 1000 characters")
                self.text = value
            elif key == 'rating':
                if not isinstance(value, int) or value < 1 or value > 5:
                    raise ValueError("rating must be an integer between 1 and 5")
                self.rating = value

    def to_dict(self):
        """Convert the object to dictionary"""
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'created_at': self.created_at.isoformat() if hasattr(self, 'created_at') else None,
            'updated_at': self.updated_at.isoformat() if hasattr(self, 'updated_at') else None
        }
