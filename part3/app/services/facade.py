from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

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

        return self.user_repo.add(user)

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        return self.user_repo.update(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_repo.delete(user_id)

    def create_place(self, place_data):
        place_data_copy = place_data.copy()
        amenities_ids = place_data_copy.pop('amenities', [])
        
        place = Place(**place_data_copy)

        new_place = self.place_repo.add(place)
        
        for amenity_id in amenities_ids:
            amenity = self.get_amenity(amenity_id)
            if amenity:
                new_place.add_amenity(amenity)
        
        return new_place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        return self.place_repo.update(place_id, place_data)

    def delete_place(self, place_id):
        return self.place_repo.delete(place_id)

    def create_review(self, review_data):
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'], 
            place_id=review_data['place_id'],
            user_id=review_data['user_id']
        )
        
        return self.review_repo.add(review)

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        return self.amenity_repo.add(amenity)

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

facade = HBnBFacade()
