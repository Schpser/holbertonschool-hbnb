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
        self.review_repo = InMemoryRepository()

    def create_user(self, user_data):
        password = user_data.pop('password', None)
        user = User(**user_data)
        if password:
            user.hash_password(password)
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
        user = self.user_repo.get(user_id)
        if user:
            user.update(data)
            return user
        return None

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

        # Handle owner update
        if 'owner_id' in place_data:
            owner_id = place_data['owner_id']
            owner = self.user_repo.get(owner_id)
            if not owner:
                raise ValueError("Owner not found")
            place.owner = owner

        # Handle amenities update
        if 'amenities' in place_data:
            amenities_ids = place_data.get('amenities', [])
            place.amenities = []

            for amenity_id in amenities_ids:
                amenity = self.amenity_repo.get(amenity_id)
                if not amenity:
                    raise ValueError(f"Amenity with ID {amenity_id} not found")
                place.add_amenity(amenity)

        # Update other fields (excluding owner_id and amenities)
        updated_data = {k: v for k, v in place_data.items() if k not in ['owner_id', 'amenities']}
        place.update(updated_data)
        return place
    
    def create_review(self, review_data):
        user_id = review_data.get('user_id')
        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("User not found")

        place_id = review_data.get('place_id')
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")

        review_kwargs = {
            'text': review_data.get('text'),
            'rating': review_data.get('rating'),
            'user': user,
            'place': place
        }

        review = Review(**review_kwargs)
        self.review_repo.add(review)
        place.add_review(review)

        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return place.reviews

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError(f"Review with ID {review_id} not found")

        if 'user_id' in review_data:
            user_id = review_data['user_id']
            user = self.user_repo.get(user_id)
            if not user:
                raise ValueError("User not found")
            review.user = user
            review_data.pop('user_id')

        if 'place_id' in review_data:
            place_id = review_data['place_id']
            place = self.place_repo.get(place_id)
            if not place:
                raise ValueError("Place not found")
            review.place = place
            review_data.pop('place_id')

        review.update(review_data)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError(f"Review with ID {review_id} not found")

        if review.place and review in review.place.reviews:
            review.place.reviews.remove(review)

        self.review_repo.delete(review_id)
        return True
    