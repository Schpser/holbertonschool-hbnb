from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        print(f"DEBUG: Research user_id: '{user_id}'")
        print(f"DEBUG: IDs available: {list(self.user_repo._storage.keys())}")
        result = self.user_repo.get(user_id)
        print(f"DEBUG: User found: {result}")
        return result

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def get_all_users(self):
        if hasattr(self.user_repo, 'get_all'):
            return self.user_repo.get_all()
        return []
    
    def update_user(self, user_id, data):
        print(f"DEBUG: Update user_id: '{user_id}' avec data: {data}")
        result = self.user_repo.update(user_id, data)
        print(f"DEBUG: Update result: {result}")
        user = self.user_repo.get(user_id)
        print(f"DEBUG: Uptdated User: {user}")
        return user

    def delete_user(self, user_id):
        self.user_repo.delete(user_id)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            amenity.update(amenity_data)
            return amenity
        return None
