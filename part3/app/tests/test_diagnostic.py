from app import create_app, db

app = create_app()

with app.app_context():
    print("🔍 DIAGNOSTIC COMPLET")
    print("=" * 40)
    
    print(f"✅ db est initialisé: {db is not None}")
    
    import sqlalchemy as sa
    inspector = sa.inspect(db.engine)
    tables = inspector.get_table_names()
    print(f"📊 Tables: {tables}")
    
    from app.models.user import User
    print(f"🔍 User a 'query': {hasattr(User, 'query')}")
    print(f"🔍 User a '__table__': {hasattr(User, '__table__')}")
    print(f"🔍 User table name: {getattr(User, '__tablename__', 'NO TABLE NAME')}")
    
    from app.models.base_model import BaseModel
    print(f"🔍 BaseModel est abstract: {getattr(BaseModel, '__abstract__', False)}")
    print(f"🔍 BaseModel hérite de db.Model: {issubclass(BaseModel, db.Model)}")
    
    try:
        user = User(
            first_name="Diagnostic",
            last_name="Test", 
            email="diagnostic@example.com",
            password="test123"
        )
        print(f"✅ User instancié - ID: {user.id}")
        print(f"🔍 User a '_sa_instance_state': {hasattr(user, '_sa_instance_state')}")
    except Exception as e:
        print(f"❌ Erreur instanciation: {e}")
