from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        if hasattr(self.user_repo, 'get_all'):
            return self.user_repo.get_all()
        return []
    
    def update_user(self, user_id, data):
        return self.user_repo.update(user_id, data)

    def delete_user(self, user_id):
        self.user_repo.delete(user_id)
