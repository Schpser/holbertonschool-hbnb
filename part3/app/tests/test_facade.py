from app import create_app, db
from app.services.facade import HBnBFacade

app = create_app()
facade = HBnBFacade()

with app.app_context():
    print("🎯 TEST FACADE CORRIGÉE")
    print("=" * 30)
    
    user_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'password': 'password123'
    }
    
    user = facade.create_user(user_data)
    print(f"✅ User créé: {user.id} - {user.email}")
    
    place_data = {
        'title': 'Beautiful Apartment',
        'description': 'Lovely place in Paris',
        'price': 120.0,
        'latitude': 48.8566,
        'longitude': 2.3522,
        'owner_id': user.id
    }
    
    place = facade.create_place(place_data)
    print(f"✅ Place créée: {place.id} - {place.title}")
    
    review_data = {
        'text': 'Amazing place!',
        'rating': 5,
        'user_id': user.id,
        'place_id': place.id
    }
    
    review = facade.create_review(review_data)
    print(f"✅ Review créée: {review.id}")
    
    user_by_email = facade.get_user_by_email('john.doe@example.com')
    print(f"✅ User par email: {user_by_email.email}")
    
    places_by_owner = facade.get_places_by_owner(user.id)
    print(f"✅ Places par owner: {len(places_by_owner)}")
    
    reviews_by_place = facade.get_reviews_by_place(place.id)
    print(f"✅ Reviews par place: {len(reviews_by_place)}")
    
    print("🎉 FACADE FONCTIONNELLE !")