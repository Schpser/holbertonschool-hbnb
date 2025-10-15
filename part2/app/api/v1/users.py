from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
    
    def get(self):
        """Retrieve a list of all users"""
        if not hasattr(facade, 'get_all_users'):
            return [], 200

        users = facade.get_all_users()
        result = []
        for u in users:
            result.append({
                'id': getattr(u, 'id', None),
                'first_name': getattr(u, 'first_name', None),
                'last_name': getattr(u, 'last_name', None),
                'email': getattr(u, 'email', None)
            })
        return result, 200

@api.route('/<string:user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Email already registered')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update a user"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        new_data = api.payload

        if 'email' in new_data and new_data['email'] != user.email:
            existing_user = facade.get_user_by_email(new_data['email'])
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already registered'}, 400
        updated = facade.update_user(user_id, new_data)
        if not updated:
            return {'error': 'User not found'}, 404

        return {
            'id': updated.id,
            'first_name': updated.first_name,
            'last_name': updated.last_name,
            'email': updated.email
        }, 200
