from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Enter: Bearer <your_token>'
    }
}

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    api = Api(app, 
              version='1.0', 
              title='HBnB API', 
              description='HBnB Application API', 
              doc='/docs/',
              authorizations=authorizations,
              security='Bearer Auth')

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    with app.app_context():

        from app.models.user import User
        from app.models.place import Place  
        from app.models.review import Review
        from app.models.amenity import Amenity

        db.create_all()
        print("✅ Tables créées avec succès!")

    from app.api.v1.users import user_namespace as users_ns
    from app.api.v1.amenities import amenity_namespace
    from app.api.v1.places import place_namespace
    from app.api.v1.reviews import review_namespace
    from app.api.v1.auth import api as auth_ns
    
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(amenity_namespace, path='/api/v1/amenities')
    api.add_namespace(place_namespace, path='/api/v1/places')
    api.add_namespace(review_namespace, path='/api/v1/reviews')
    
    return app
