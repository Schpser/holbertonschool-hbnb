#!/usr/bin/env python3
"""Tests for the models"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
import unittest

class TestUserModel(unittest.TestCase):

    def test_user_creation(self):
        """Test creating a user with valid data"""
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.is_admin, False)

    def test_user_invalid_email(self):
        """Test creating a user with invalid email"""
        with self.assertRaises(ValueError) as context:
            User(first_name="John", last_name="Doe", email="invalid-email")
        self.assertIn("invalid email format", str(context.exception))

    def test_user_empty_first_name(self):
        """Test creating a user with empty first name"""
        with self.assertRaises(ValueError) as context:
            User(first_name="", last_name="Doe", email="test@example.com")
        self.assertIn("first name must be between 1 and 50 characters", str(context.exception))

class TestPlaceModel(unittest.TestCase):

    def test_place_creation(self):
        """Test creating a place with valid data"""
        owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
        place = Place(
            title="Cozy Apartment", 
            description="A nice place to stay", 
            price=100, 
            latitude=37.7749, 
            longitude=-122.4194, 
            owner=owner
        )
        self.assertEqual(place.title, "Cozy Apartment")
        self.assertEqual(place.price, 100)
        self.assertEqual(len(place.reviews), 0)

    def test_place_invalid_price(self):
        """Test creating a place with invalid price"""
        owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
        with self.assertRaises(ValueError) as context:
            Place(title="Test", description="Test", price=-100, latitude=37.7, longitude=-122.4, owner=owner)
        self.assertIn("price must be postive value", str(context.exception))

class TestAmenityModel(unittest.TestCase):

    def test_amenity_creation(self):
        """Test creating an amenity with valid data"""
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")

    def test_amenity_empty_name(self):
        """Test creating an amenity with empty name"""
        with self.assertRaises(ValueError) as context:
            Amenity(name="")
        self.assertIn("name is required", str(context.exception))

class TestReviewModel(unittest.TestCase):

    def test_review_creation(self):
        """Test creating a review with valid data"""
        owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
        place = Place(title="Test", description="Test", price=100, latitude=37.7, longitude=-122.4, owner=owner)
        review = Review(text="Great stay!", rating=5, place=place, user=owner)
        
        self.assertEqual(review.text, "Great stay!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.place, place)
        self.assertEqual(review.user, owner)

    def test_review_invalid_rating(self):
        """Test creating a review with invalid rating"""
        owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
        place = Place(title="Test", description="Test", price=100, latitude=37.7, longitude=-122.4, owner=owner)
        
        with self.assertRaises(ValueError) as context:
            Review(text="Test", rating=6, place=place, user=owner)
        self.assertIn("rating must be between 1 and 5", str(context.exception))

if __name__ == '__main__':
    unittest.main()