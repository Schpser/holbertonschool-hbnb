from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()

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
        print(f"DEBUG: Update user_id: '{user_id}' with data: {data}")
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

    def create_place(self, place_data):
        owner_id = place_data.get('owner_id')
        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        amenities_ids = place_data.pop('amenities', [])
        
        place_kwargs = {
            'title': place_data.get('title'),
            'description': place_data.get('description', ''),
            'price': place_data.get('price'),
            'latitude': place_data.get('latitude'),
            'longitude': place_data.get('longitude'),
            'owner': owner
        }

        place = Place(**place_kwargs)
        self.place_repo.add(place)

        for amenity_id in amenities_ids:
            amenity = self.amenity_repo.get(amenity_id)
            if not amenity:
                self.place_repo.delete(place.id)
                raise ValueError(f"Amenity with ID {amenity_id} not found")
            place.add_amenity(amenity)

        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError(f"Place with ID {place_id} not found")

        if 'owner_id' in place_data:
            owner_id = place_data['owner_id']
            owner = self.user_repo.get(owner_id)
            if not owner:
                raise ValueError("Owner not found")

            place.owner = owner

        if 'amenities' in place_data:
            amenities_ids = place_data.pop('amenities')
            place.amenities = []

            for amenity_id in amenities_ids:
                amenity = self.amenity_repo.get(amenity_id)
                if not amenity:
                    raise ValueError(f"Amenity with ID {amenity_id} not found")
                place.add_amenity(amenity)

        updated_data = {k: v for k, v in place_data.items() if k != 'owner_id'}
        place.update(updated_data)
        return place