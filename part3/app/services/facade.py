from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self._users = {}
        self._places = {}
        self._reviews = {}
        self._amenities = {}
        self._next_id = 1

    def create_user(self, user_data):
        user_data_copy = user_data.copy()
        password = user_data_copy.pop('password', None)
        
        user = User(
            first_name=user_data_copy['first_name'],
            last_name=user_data_copy['last_name'],
            email=user_data_copy['email'],
            is_admin=user_data_copy.get('is_admin', False)
        )

        if password:
            user.hash_password(password)
        
        user.id = str(self._next_id)
        self._next_id += 1
        self._users[user.id] = user
        return user

    def get_user(self, user_id):
        return self._users.get(user_id)

    def get_all_users(self):
        return list(self._users.values())

    def get_user_by_email(self, email):
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            return None

        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.hash_password(user_data['password'])
        
        return user

    def delete_user(self, user_id):
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False

    def create_place(self, place_data):
        place_data_copy = place_data.copy()

        amenities_ids = place_data_copy.pop('amenities', [])

        place_data_copy['amenities'] = []
        place = Place(**place_data_copy)
        place.id = str(self._next_id)
        self._next_id += 1

        for amenity_id in amenities_ids:
            amenity = self.get_amenity(amenity_id)
            if amenity:
                place.add_amenity(amenity)
        
        self._places[place.id] = place
        return place

    def get_place(self, place_id):
        return self._places.get(place_id)

    def get_all_places(self):
        return list(self._places.values())

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if not place:
            return None
        
        for key, value in place_data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        return place

    def delete_place(self, place_id):
        if place_id in self._places:
            del self._places[place_id]
            return True
        return False

    def create_review(self, review_data):
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'], 
            place_id=review_data['place_id'],
            user_id=review_data['user_id']
        )
        
        review.id = str(self._next_id)
        self._next_id += 1
        self._reviews[review.id] = review
        return review

    def get_reviews_by_place(self, place_id):
        return [review for review in self._reviews.values() if review.place_id == place_id]

    def get_all_reviews(self):
        return list(self._reviews.values())

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        amenity.id = str(self._next_id)
        self._next_id += 1
        self._amenities[amenity.id] = amenity
        return amenity

    def get_amenity(self, amenity_id):
        return self._amenities.get(amenity_id)

    def get_all_amenities(self):
        return list(self._amenities.values())

facade = HBnBFacade()
