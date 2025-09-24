# 🏗️ Business Logic Layer - Class Diagram Documentation

## 📄 Explanatory Notes

---

### 🧩 Entity Descriptions

#### **🔹 BaseModel (Abstract Class)**
- **Role:** Serves as the foundation for all business entities, providing common functionality and ensuring consistency across the system.
- **Key Attributes:**
    - `id` (UUID): Universal unique identifier following UUID4 standard
    - `created_at` (datetime): Automatic timestamp for entity creation
    - `updated_at` (datetime): Automatic timestamp for last modification
- **Key Methods:**
    - `save()`: Handles persistence logic with automatic timestamp updates
    - `delete()`: Manages entity removal with proper cleanup

---

#### **👤 User**
- **Role:** Represents all system users (guests, hosts, administrators) and manages user-related business logic.
- **Key Attributes:**
    - `is_host` (bool): Determines if user can create and manage rental properties
    - `is_admin` (bool): Grants administrative privileges when true
    - `password_hash` (private): Securely stored authentication credential
- **Key Methods:**
    - `become_host()`: Transforms regular user into host with appropriate permissions
    - `verify_password()`: Handles secure authentication validation
    - `get_places()`: Retrieves all properties owned by the user (host functionality)

---

#### **🏠 Place**
- **Role:** Manages rental property information, availability, and pricing logic.
- **Key Attributes:**
    - `price_per_night` (float): Dynamic pricing information
    - `max_guests` (int): Capacity constraints for booking validation
    - `is_available` (bool): Controls property visibility and bookability
- **Key Methods:**
    - `check_availability()`: Core business logic for reservation conflicts
    - `get_amenities()`: Provides associated amenities for search and display
    - `set_price()`: Manages pricing updates with validation

---

#### **⭐ Review**
- **Role:** Handles user feedback system with verification and moderation capabilities.
- **Key Attributes:**
    - `rating` (int): Quality assessment (typically 1-5 scale)
    - `is_verified` (bool): Ensures review authenticity
    - `comment` (string): Detailed user feedback
- **Key Methods:**
    - `update_review()`: Allows limited-time modifications by authors
    - `verify()`: Implements review validation process

---

#### **🛋️ Amenity**
- **Role:** Manages property features and facilities for search and filtering.
- **Key Attributes:**
    - `name` (string): Feature identification
    - `icon_url` (string): Visual representation for UI

---

#### **🔗 AmenityPlace (Association Class)**
- **Role:** Manages the many-to-many relationship between properties and amenities.
- **Key Attributes:**
    - `place_id`, `amenity_id`: Foreign keys maintaining relationship integrity

---

## 🔄 Relationship Explanations

### 🏷️ Inheritance Relationships (Generalizations)
- The `BaseModel <|-- [Entity]` relationships implement the inheritance pattern, allowing all business entities to share common functionality while maintaining the Open/Closed principle. This design:
    - Reduces code duplication
    - Ensures consistent behavior across entities
    - Simplifies future extensions

### 🤝 Association Relationships
- **User -- Place (owns):**  
    A bidirectional association where users can own multiple properties, and each property has exactly one owner. This enables host functionality and property management.
- **User -- Review (writes):**  
    Establishes authorship of reviews, ensuring each review is traceable to its author while allowing users to write multiple reviews.
- **Place -- Review (has):**  
    Connects properties to their reviews, enabling rating calculations and property reputation management.

### 🧱 Composition Relationships
- **Place *-- AmenityPlace** and **Amenity *-- AmenityPlace:**  
    These strong compositions ensure that the relationship records cannot exist independently of their associated Place and Amenity. This maintains referential integrity and supports cascade operations.

### 🔗 Dependency Relationships
- The `..>` dependencies represent temporary usage relationships where methods in one class utilize another class:
    - `User.get_places()` depends on `Place` class
    - `User.get_reviews()` depends on `Review` class
    - `Place.get_amenities()` depends on `Amenity` class

    These dependencies ensure loose coupling while maintaining necessary collaborations between entities.

---

## 🧠 Business Logic Contributions

- **User Role Management:**  
    The `is_host` attribute combined with ownership associations enables the host/guest duality.
- **Review Integrity:**  
    Associations between User-Review-Place ensure authentic, traceable feedback.
- **Property Management:**  
    The composition pattern maintains data consistency for property features.
- **Search Capabilities:**  
    Amenity relationships enable advanced filtering and property discovery.

---

> 📝 **Summary:**  
> The diagram successfully represents a domain model that supports key business operations like property listing, booking availability checks, user authentication, and review management while maintaining scalability for future enhancements.
