from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model, validate=True)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload
        
        # Check if amenity with same name already exists
        existing_amenities = facade.get_all_amenities()
        for amenity in existing_amenities:
            if amenity.name == amenity_data['name']:
                return {'error': 'Amenity name already exists'}, 400
        
        new_amenity = facade.create_amenity(amenity_data)
        return {
            'id': new_amenity.id,
            'name': new_amenity.name
        }, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        result = []
        for amenity in amenities:
            result.append({
                'id': amenity.id,
                'name': amenity.name
            })
        return result, 200

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        
        return {
            'id': amenity.id,
            'name': amenity.name
        }, 200

    @api.expect(amenity_model, validate=True)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        
        new_data = api.payload
        
        # Check if new name already exists (but not for the same amenity)
        existing_amenities = facade.get_all_amenities()
        for existing_amenity in existing_amenities:
            if existing_amenity.name == new_data['name'] and existing_amenity.id != amenity_id:
                return {'error': 'Amenity name already exists'}, 400
        
        updated_amenity = facade.update_amenity(amenity_id, new_data)
        if not updated_amenity:
            return {'error': 'Amenity not found'}, 404
        
        return {
            'id': updated_amenity.id,
            'name': updated_amenity.name
        }, 200