#!/bin/bash

BASE_URL="http://localhost:5000/api/v1"

echo "=== Testing HBnB API Endpoints ==="
echo

# Test Users
echo "1. Testing User Endpoints"
echo "------------------------"

echo "Creating valid user..."
curl -X POST "$BASE_URL/users/" -H "Content-Type: application/json" -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}'
echo
echo

echo "Creating user with invalid email..."
curl -X POST "$BASE_URL/users/" -H "Content-Type: application/json" -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "invalid-email"
}'
echo
echo

echo "Creating user with empty fields..."
curl -X POST "$BASE_URL/users/" -H "Content-Type: application/json" -d '{
    "first_name": "",
    "last_name": "",
    "email": ""
}'
echo
echo

# Test Amenities
echo "2. Testing Amenity Endpoints"
echo "---------------------------"

echo "Creating valid amenity..."
curl -X POST "$BASE_URL/amenities/" -H "Content-Type: application/json" -d '{
    "name": "Wi-Fi"
}'
echo
echo

echo "Creating amenity with empty name..."
curl -X POST "$BASE_URL/amenities/" -H "Content-Type: application/json" -d '{
    "name": ""
}'
echo
echo

# Test error cases
echo "3. Testing Error Cases"
echo "---------------------"

echo "Getting non-existent user..."
curl -X GET "$BASE_URL/users/non-existent-id"
echo
echo

echo "Getting non-existent place..."
curl -X GET "$BASE_URL/places/non-existent-id"
echo
echo

echo "=== Manual Testing Complete ==="
