from app import create_app, db
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
import sqlalchemy as sa

app = create_app()

with app.app_context():
    print("=== TEST 1 : Vérification des tables ===")
    inspector = sa.inspect(db.engine)
    tables = inspector.get_table_names()
    print("📊 Tables dans la base :", tables)
    
    print("=== TEST 2 : Création User avec email UNIQUE ===")
    user = User(
        first_name="NewTest", 
        last_name="User",
        email="newtest@example.com",
        password="test123"
    )
    user.save()
    print(f"✅ User créé avec ID: {user.id}")
    
    print("=== TEST 3 : Création Place ===")
    place = Place(
        title="Beautiful Apartment",
        description="Lovely place in the city",
        price=120.0,
        latitude=48.8566,
        longitude=2.3522,
        owner_id=user.id
    )
    place.save()
    print(f"✅ Place créée avec ID: {place.id}")
    
    print("=== TEST 4 : Création Review ===")
    review = Review(
        text="Amazing place! Highly recommend!",
        rating=5,
        place_id=place.id,
        user_id=user.id
    )
    review.save()
    print(f"✅ Review créée avec ID: {review.id}")
    
    print("=== TEST 5 : Création Amenity ===")
    amenity = Amenity(name="Swimming Pool")
    amenity.save()
    print(f"✅ Amenity créée avec ID: {amenity.id}")
    
    print("=== TEST 6 : Vérification récupération ===")
    saved_user = db.session.get(User, user.id)
    saved_place = db.session.get(Place, place.id)
    saved_review = db.session.get(Review, review.id)
    saved_amenity = db.session.get(Amenity, amenity.id)
    
    print(f"🔍 User: {saved_user.email}")
    print(f"🔍 Place: {saved_place.title}")
    print(f"🔍 Review: {saved_review.text[:30]}...")
    print(f"🔍 Amenity: {saved_amenity.name}")
    
    print("🎉 TOUS LES MODÈLES FONCTIONNENT ! La tâche 7 est COMPLÈTE !")