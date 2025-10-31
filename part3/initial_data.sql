-- HBnB Initial Data
-- Admin user and basic amenities

-- Admin User (password: admin1234 hashed with bcrypt)
INSERT INTO users (id, first_name, last_name, email, password, is_admin, created_at, updated_at)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin', 
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$LQv3c1yqBWVHxkd2g8a9HeYgJCYOWMtgzFdsBFk8Udmjr5qR4O.S6', -- admin1234
    TRUE,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- Initial Amenities
INSERT INTO amenities (id, name, created_at, updated_at) VALUES
('a1b2c3d4-e5f6-7890-abcd-ef1234567890', 'WiFi', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('b2c3d4e5-f6g7-8901-bcde-f23456789012', 'Swimming Pool', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('c3d4e5f6-g7h8-9012-cdef-345678901234', 'Air Conditioning', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('d4e5f6g7-h8i9-0123-defg-456789012345', 'Kitchen', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('e5f6g7h8-i9j0-1234-efgh-567890123456', 'Free Parking', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('f6g7h8i9-j0k1-2345-fghi-678901234567', 'Hot Tub', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Sample regular user
INSERT INTO users (id, first_name, last_name, email, password, is_admin, created_at, updated_at)
VALUES (
    '47d8150f-eee4-4d4c-a842-0a598470abcd',
    'John',
    'Traveler',
    'john.traveler@example.com',
    '$2b$12$OtherHashExample1234567890ABCDEFGHIJK',
    FALSE,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);
