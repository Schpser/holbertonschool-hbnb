from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        if not name or len(name.strip()) == 0:
            raise ValueError("name is required")
        if len(name) > 50:
            raise ValueError("name must be at most 50 characters")

        self.name = name
        
    def update(self, data):
            """Update amenity attributes"""
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)