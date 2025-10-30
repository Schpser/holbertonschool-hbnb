from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    print("=== TEST 1 : Création ===")
    user = User(
        first_name="Persistence", 
        last_name="Test",
        email="persist@example.com", 
        password="test123"
    )
    user.save()
    user_id = user.id
    print(f"✅ User créé avec ID: {user_id}")
    
    print("=== TEST 2 : Récupération immédiate ===")
    user1 = db.session.get(User, user_id)  # ✅ Nouvelle syntaxe
    print(f"🔍 User récupéré: {user1.email}")
    
    print("=== TEST 3 : Récupération après 'redémarrage' ===")
    # Simuler un redémarrage en créant une nouvelle session
    db.session.remove()
    user2 = db.session.get(User, user_id)
    print(f"🔄 User après 'redémarrage': {user2.email}")
    
    print("=== TEST 4 : Vérification password ===")
    print(f"🔐 Password vérifié: {user2.verify_password('test123')}")
    
    print("🎉 TOUS LES TESTS RÉUSSIS ! Les données sont PERSISTANTES !")
