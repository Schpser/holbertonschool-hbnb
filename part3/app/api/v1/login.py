from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade

auth_namespace = Namespace('auth', description='Authentication operations')

login_model = auth_namespace.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@auth_namespace.route('/login')
class Login(Resource):
    @auth_namespace.expect(login_model, validate=True)
    def post(self):
        """Logs in a user and returns an access token"""
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = facade.get_user_by_email(email)

        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        
        return {'error': 'Invalid credentials'}, 401
