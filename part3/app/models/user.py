from flask_bcrypt import Bcrypt
from flask_restx.api import current_app
from app.models.base_model import BaseModel
import re

bcrypt = Bcrypt()

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password=None, is_admin=False):
        super().__init__()

        if len(first_name) == 0 or len(first_name) > 50:
            raise ValueError("first name must be between 1 and 50 characters")
        if len(last_name) == 0 or len(last_name) > 50:
            raise ValueError("last name must be between 1 and 50 characters")
        if not isinstance(is_admin, bool):
            raise ValueError("is_admin must be a boolean")
        if not email:
            raise ValueError("email is required")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("invalid email format")
 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []

    # Add 'Peppering Method' :

    def hash_password(self, password, pepper):
        peppered_password = password + pepper
        self.password = bcrypt.generate_password_hash(peppered_password).decode('utf-8')

    def verify_password(self, password, pepper):
        if not self.password:
            return False

        peppered_password = password + pepper
        return bcrypt.check_password_hash(self.password, peppered_password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

