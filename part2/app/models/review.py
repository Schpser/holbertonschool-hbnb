from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        if not text or len(text.strip()) == 0:
            raise ValueError("text is required")
        if not isinstance(rating, int):
            raise ValueError("rating must be an integer")
        if rating < 1 or rating > 5:
            raise ValueError("rating must be between 1 and 5")
        if not isinstance(place, Place):
            raise ValueError("place must be a Place instance")
        if not isinstance(user, User):
            raise ValueError("user must be a User instance")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
