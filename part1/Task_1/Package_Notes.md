# 🏗️ Business Logic Layer - Class Diagram Documentation

---

## 🧩 Entity Descriptions

### 🔹 BaseModel (Abstract Class)
**Role:** Serves as the foundation for all business entities, providing common functionality and ensuring consistency across the system.

**Key Attributes:**
- `id` (UUID): Universal unique identifier following UUID4 standard
- `created_at` (datetime): Automatic timestamp for entity creation
- `updated_at` (datetime): Automatic timestamp for last modification

**Key Methods:**
- `save()`: Handles persistence logic with automatic timestamp updates
- `delete()`: Manages entity removal with proper cleanup

---

### 👤 User
**Role:** Represents all system users (guests, hosts, administrators) and manages user-related business logic.

**Key Attributes:**
- `first_name`, `last_name` (string): Personal identification information
- `email` (private): Primary contact and authentication identifier
- `phone_number` (private): Optional contact information
- `profile_picture` (string): Avatar/image URL for user recognition
- `is_host` (bool): Determines if user can create and manage rental properties
- `is_admin` (bool): Grants administrative privileges when true
- `password_hash` (private): Securely stored authentication credential

**Key Methods:**
- `get_email()`: Controlled access to private email with privacy considerations
- `set_email()`: Validates and updates email address
- `become_host()`: Transforms regular user into host with appropriate permissions
- `verify_password()`: Handles secure authentication validation
- `get_places()`: Retrieves all properties owned by the user (host functionality)
- `get_reviews()`: Fetches all reviews written by the user

---

### 🏠 Place
**Role:** Manages rental property information, availability, and pricing logic.

**Key Attributes:**
- `title` (string): Property name/headline for listings
- `description` (string): Detailed property information
- `price_per_night` (private): Dynamic pricing information with controlled access
- `max_guests` (private): Capacity constraints for booking validation
- `number_of_rooms` (private): Room count for search filtering
- `address` (private): Physical location with privacy protection
- `latitude`, `longitude` (private): Geographic coordinates for mapping
- `owner_id` (UUID): Reference to property owner (User)
- `is_available` (private): Controls property visibility and bookability

**Key Methods:**
- `get_price()`: Provides controlled access to pricing information
- `set_price()`: Manages pricing updates with validation rules
- `check_availability()`: Core business logic for reservation date conflicts
- `get_amenities()`: Provides associated amenities for search and display

---

### ⭐ Review
**Role:** Handles user feedback system with verification and moderation capabilities.

**Key Attributes:**
- `place_id` (UUID): Reference to reviewed property
- `user_id` (UUID): Reference to review author
- `rating` (private): Quality assessment (typically 1-5 scale) with access control
- `comment` (private): Detailed user feedback with moderation needs
- `is_verified` (private): Ensures review authenticity through verification process

**Key Methods:**
- `get_rating()`: Controlled access to rating value
- `get_comment()`: Controlled access to review text
- `update_review()`: Allows limited-time modifications by authors with validation
- `verify()`: Implements review validation process for authenticity

---

### 🛋️ Amenity
**Role:** Manages property features and facilities for search and filtering.

**Key Attributes:**
- `name` (string): Feature identification for search and display
- `description` (string): Detailed explanation of the amenity
- `icon_url` (string): Visual representation for UI consistency

---

### 🔗 AmenityPlace (Association Class)
**Role:** Manages the many-to-many relationship between properties and amenities with additional business logic potential.

**Key Attributes:**
- `place_id` (UUID): Foreign key maintaining relationship to Place
- `amenity_id` (UUID): Foreign key maintaining relationship to Amenity

---

## 🔄 Relationship Explanations

### 🏷️ Inheritance Relationships (Generalizations)
The `BaseModel <|-- [Entity]` relationships implement the inheritance pattern, allowing all business entities to share common functionality while maintaining the Open/Closed principle. This design:
- Reduces code duplication across User, Place, Amenity, and Review
- Ensures consistent behavior across all business entities
- Simplifies future extensions and maintenance
- Provides uniform persistence mechanism through `save()`/`delete()` methods

---

### 🤝 Association Relationships

- **User -- Place (owns):**
    - A bidirectional association where users can own multiple properties (1..*), and each property has exactly one owner.
    - Enables host functionality through the `is_host` attribute validation
    - Property management capabilities for hosts
    - Ownership verification for booking and modification operations

- **User -- Review (writes):**
    - Establishes authorship of reviews (1..*), ensuring each review is traceable to its author while allowing users to write multiple reviews.
    - Supports review authenticity and accountability
    - User review history tracking
    - Moderation and content management

- **Place -- Review (has):**
    - Connects properties to their reviews (1..*), enabling:
        - Rating calculations and average score computations
        - Property reputation management
        - Review filtering and sorting by property

---

### 🧱 Composition Relationships

- **Place -- AmenityPlace** and **Amenity -- AmenityPlace:**
    - These strong compositions ensure that the relationship records cannot exist independently of their associated Place and Amenity.
    - Maintains referential integrity through cascade operations
    - Data consistency for property-amenity relationships
    - Proper cleanup when properties or amenities are removed

---

### 🔗 Dependency Relationships

The `..>` dependencies represent temporary usage relationships where methods in one class utilize another class:
- `User.get_places()` depends on Place class for property retrieval
- `User.get_reviews()` depends on Review class for review history
- `Place.get_amenities()` depends on Amenity class for feature listing

These dependencies ensure loose coupling while maintaining necessary collaborations between entities, following the principle of separation of concerns.

---

## 🧠 Business Logic Contributions

- **User Role Management:**  
    The `is_host` attribute combined with ownership associations enables the host/guest duality, supporting role-based access control and functionality.

- **Privacy and Access Control:**  
    Private attributes with getter/setter methods (email, password, pricing) enforce business rules and data protection.

- **Review Integrity System:**  
    Associations between User-Review-Place ensure authentic, traceable feedback with verification mechanisms.

- **Property Management Ecosystem:**  
    The composition pattern maintains data consistency for property features and supports advanced search capabilities.

- **Geospatial Capabilities:**  
    Latitude/longitude attributes enable location-based services and mapping integrations.

- **Dynamic Pricing Strategy:**  
    Controlled price access and modification methods support flexible pricing models.

- **Capacity Planning:**  
    `max_guests` and room count attributes enable intelligent booking validation and property matching.
