from flask import Flask, request, make_response
from flask_cors import CORS
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

def create_app():
    app = Flask(__name__)
    CORS(app, resources={
        r"/api/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"],
            "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Origin"],
            "expose_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True,
            "max_age": 600
        }
    })

    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.headers.add("Access-Control-Allow-Headers", "*")
            response.headers.add("Access-Control-Allow-Methods", "*")
            return response

    app.config.from_object('config.DevelopmentConfig')

    api = Api(app, 
              version='1.0', 
              title='HBnB API', 
              description='HBnB Application API', 
              doc='/docs/',
              authorizations=authorizations,
              security='Bearer Auth',
              serve_challenge_on_401=True)

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    with app.app_context():
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