from flask_restx import Namespace, Resource, fields
from app.services import facade

amenity_namespace = Namespace('amenities', description='Amenity operations')

amenity_model = amenity_namespace.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@amenity_namespace.route('/')
class AmenityList(Resource):
    @amenity_namespace.expect(amenity_model, validate=True)
    @amenity_namespace.response(201, 'Amenity successfully created')
    @amenity_namespace.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = amenity_namespace.payload
        
        if not amenity_data.get('name'):
            return {'error': 'Amenity name is required'}, 400
        
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return {
                'id': new_amenity.id,
                'name': new_amenity.name
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': f'Internal server error: {str(e)}'}, 500

    @amenity_namespace.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return [{
            'id': amenity.id,
            'name': amenity.name
        } for amenity in amenities], 200

@amenity_namespace.route('/<amenity_id>')
class AmenityResource(Resource):
    @amenity_namespace.response(200, 'Amenity details retrieved successfully')
    @amenity_namespace.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return {
            'id': amenity.id,
            'name': amenity.name
        }, 200

    @amenity_namespace.expect(amenity_model, validate=True)
    @amenity_namespace.response(200, 'Amenity updated successfully')
    @amenity_namespace.response(404, 'Amenity not found')
    @amenity_namespace.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = amenity_namespace.payload
        
        existing_amenity = facade.get_amenity(amenity_id)
        if not existing_amenity:
            return {'error': 'Amenity not found'}, 404
        
        if not amenity_data.get('name'):
            return {'error': 'Amenity name is required'}, 400
        
        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
            if updated_amenity:
                return {
                    'id': updated_amenity.id,
                    'name': updated_amenity.name
                }, 200
            else:
                return {'error': 'Amenity not found'}, 404
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': f'Internal server error: {str(e)}'}, 500
            