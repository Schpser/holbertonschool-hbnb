#!/usr/bin/env python3
"""
Test suite for HBNB API endpoints.
Tests all REST API endpoints exactly as specified in the requirements.
"""
import unittest
import json
import sys
import os

# Add the parent directory to the path so we can import from app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.services.facade import HBnBFacade


class TestAPIEndpoints(unittest.TestCase):
    """Test cases for all API endpoints"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def setUp(self):
        """Reset facade for each test"""
        # Create a fresh facade instance for each test
        import app.services
        app.services.facade = HBnBFacade()
        
        # Store IDs for cross-endpoint testing
        self.user_ids = []
        self.amenity_ids = []
        self.place_ids = []
        self.review_ids = []

    def test_01_user_endpoints(self):
        """Test all User endpoints: POST, GET, GET all, PUT"""
        
        # POST /api/v1/users/
        print("\n=== Testing POST /api/v1/users/ ===")
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }
        response = self.client.post('/api/v1/users/', 
                                   data=json.dumps(user_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 201)
        user_json = json.loads(response.data)
        user_id = user_json['id']
        self.user_ids.append(user_id)
        print(f"✅ Created user with ID: {user_id}")
        
        # GET /api/v1/users/<user_id>
        print(f"\n=== Testing GET /api/v1/users/{user_id} ===")
        response = self.client.get(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        user_data = json.loads(response.data)
        self.assertEqual(user_data['first_name'], 'John')
        self.assertEqual(user_data['email'], 'john.doe@example.com')
        print("✅ Retrieved user successfully")
        
        # GET /api/v1/users/
        print("\n=== Testing GET /api/v1/users/ ===")
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        users = json.loads(response.data)
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)
        print(f"✅ Retrieved {len(users)} users")
        
        # PUT /api/v1/users/<user_id>
        print(f"\n=== Testing PUT /api/v1/users/{user_id} ===")
        update_data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        }
        response = self.client.put(f'/api/v1/users/{user_id}',
                                  data=json.dumps(update_data),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        print("✅ Updated user successfully")

    def test_02_amenity_endpoints(self):
        """Test all Amenity endpoints: POST, GET, GET all, PUT"""
        
        # POST /api/v1/amenities/
        print("\n=== Testing POST /api/v1/amenities/ ===")
        amenity_data = {"name": "Wi-Fi"}
        response = self.client.post('/api/v1/amenities/',
                                   data=json.dumps(amenity_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 201)
        amenity_json = json.loads(response.data)
        amenity_id = amenity_json['id']
        self.amenity_ids.append(amenity_id)
        print(f"✅ Created amenity with ID: {amenity_id}")
        
        # GET /api/v1/amenities/
        print("\n=== Testing GET /api/v1/amenities/ ===")
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        amenities = json.loads(response.data)
        self.assertIsInstance(amenities, list)
        print(f"✅ Retrieved {len(amenities)} amenities")
        
        # GET /api/v1/amenities/<amenity_id>
        print(f"\n=== Testing GET /api/v1/amenities/{amenity_id} ===")
        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        amenity_data = json.loads(response.data)
        self.assertEqual(amenity_data['name'], 'Wi-Fi')
        print("✅ Retrieved amenity successfully")
        
        # PUT /api/v1/amenities/<amenity_id>
        print(f"\n=== Testing PUT /api/v1/amenities/{amenity_id} ===")
        update_data = {"name": "Air Conditioning"}
        response = self.client.put(f'/api/v1/amenities/{amenity_id}',
                                  data=json.dumps(update_data),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        print("✅ Updated amenity successfully")

    def test_03_place_endpoints(self):
        """Test all Place endpoints: POST, GET, GET all, PUT"""
        
        # First create a user to be the owner
        user_data = {"first_name": "Alice", "last_name": "Smith", "email": "alice@example.com"}
        response = self.client.post('/api/v1/users/',
                                   data=json.dumps(user_data),
                                   content_type='application/json')
        user_id = json.loads(response.data)['id']
        
        # POST /api/v1/places/
        print("\n=== Testing POST /api/v1/places/ ===")
        place_data = {
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": user_id,
            "amenities": []
        }
        response = self.client.post('/api/v1/places/',
                                   data=json.dumps(place_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 201)
        place_json = json.loads(response.data)
        place_id = place_json['id']
        self.place_ids.append(place_id)
        print(f"✅ Created place with ID: {place_id}")
        
        # GET /api/v1/places/
        print("\n=== Testing GET /api/v1/places/ ===")
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)
        places = json.loads(response.data)
        self.assertIsInstance(places, list)
        print(f"✅ Retrieved {len(places)} places")
        
        # GET /api/v1/places/<place_id>
        print(f"\n=== Testing GET /api/v1/places/{place_id} ===")
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 200)
        place_data = json.loads(response.data)
        self.assertEqual(place_data['title'], 'Cozy Apartment')
        print("✅ Retrieved place successfully")
        
        # PUT /api/v1/places/<place_id>
        print(f"\n=== Testing PUT /api/v1/places/{place_id} ===")
        update_data = {
            "title": "Luxury Condo",
            "description": "An upscale place to stay",
            "price": 200.0
        }
        response = self.client.put(f'/api/v1/places/{place_id}',
                                  data=json.dumps(update_data),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        print("✅ Updated place successfully")

    def test_04_review_endpoints(self):
        """Test all Review endpoints: POST, GET, GET all, PUT, DELETE"""
        
        # Create prerequisites: user and place
        user_data = {"first_name": "Bob", "last_name": "Johnson", "email": "bob@example.com"}
        response = self.client.post('/api/v1/users/',
                                   data=json.dumps(user_data),
                                   content_type='application/json')
        user_id = json.loads(response.data)['id']
        
        owner_data = {"first_name": "Alice", "last_name": "Smith", "email": "alice2@example.com"}
        response = self.client.post('/api/v1/users/',
                                   data=json.dumps(owner_data),
                                   content_type='application/json')
        owner_id = json.loads(response.data)['id']
        
        place_data = {
            "title": "Test Place", "description": "Test", "price": 100.0,
            "latitude": 0, "longitude": 0, "owner_id": owner_id, "amenities": []
        }
        response = self.client.post('/api/v1/places/',
                                   data=json.dumps(place_data),
                                   content_type='application/json')
        place_id = json.loads(response.data)['id']
        
        # POST /api/v1/reviews/
        print("\n=== Testing POST /api/v1/reviews/ ===")
        review_data = {
            "text": "Great place to stay!",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        }
        response = self.client.post('/api/v1/reviews/',
                                   data=json.dumps(review_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 201)
        review_json = json.loads(response.data)
        review_id = review_json['id']
        self.review_ids.append(review_id)
        print(f"✅ Created review with ID: {review_id}")
        
        # GET /api/v1/reviews/
        print("\n=== Testing GET /api/v1/reviews/ ===")
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)
        reviews = json.loads(response.data)
        self.assertIsInstance(reviews, list)
        print(f"✅ Retrieved {len(reviews)} reviews")
        
        # GET /api/v1/reviews/<review_id>
        print(f"\n=== Testing GET /api/v1/reviews/{review_id} ===")
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        review_data = json.loads(response.data)
        self.assertEqual(review_data['text'], 'Great place to stay!')
        print("✅ Retrieved review successfully")
        
        # PUT /api/v1/reviews/<review_id>
        print(f"\n=== Testing PUT /api/v1/reviews/{review_id} ===")
        update_data = {
            "text": "Amazing stay!",
            "rating": 4
        }
        response = self.client.put(f'/api/v1/reviews/{review_id}',
                                  data=json.dumps(update_data),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 200)
        print("✅ Updated review successfully")
        
        # DELETE /api/v1/reviews/<review_id>
        print(f"\n=== Testing DELETE /api/v1/reviews/{review_id} ===")
        response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
        print("✅ Deleted review successfully")

    def test_05_place_reviews_endpoint(self):
        """Test GET /api/v1/places/<place_id>/reviews"""
        
        # Create prerequisites
        user_data = {"first_name": "Test", "last_name": "User", "email": "test@example.com"}
        response = self.client.post('/api/v1/users/',
                                   data=json.dumps(user_data),
                                   content_type='application/json')
        user_id = json.loads(response.data)['id']
        
        place_data = {
            "title": "Test Place", "description": "Test", "price": 100.0,
            "latitude": 0, "longitude": 0, "owner_id": user_id, "amenities": []
        }
        response = self.client.post('/api/v1/places/',
                                   data=json.dumps(place_data),
                                   content_type='application/json')
        place_id = json.loads(response.data)['id']
        
        # GET /api/v1/places/<place_id>/reviews
        print(f"\n=== Testing GET /api/v1/places/{place_id}/reviews ===")
        response = self.client.get(f'/api/v1/places/{place_id}/reviews')
        self.assertEqual(response.status_code, 200)
        reviews = json.loads(response.data)
        self.assertIsInstance(reviews, list)
        print(f"✅ Retrieved reviews for place: {len(reviews)} reviews")


if __name__ == '__main__':
    unittest.main(verbosity=2)