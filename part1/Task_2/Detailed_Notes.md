# 🔄 Sequence Diagrams - API Calls Documentation


## 🧩 API Call Descriptions

### 🔹 User Registration
**Role:** Handles new user account creation with proper validation and security measures.

**Key Steps:**
1. **📨 Client Request** : `POST /register` with email and password
2. **⚙️ Service Processing** : UserService validates email format and hashes password
3. **💾 Data Persistence** : New user record created in database
4. **📤 Response** : User data returned (excluding sensitive information) with `201 Created` status

**Security Considerations:**
- 🔒 Password hashing before storage
- 📧 Email validation to prevent invalid registrations
- 🔓 No authentication required for this endpoint

**Data Flow:**
```
Client → API → UserService → Database → UserService → API → Client
```

---

### 🏠 Place Creation  
**Role:** Manages authenticated property listing creation with ownership association.

**Key Steps:**
1. **🔐 Authentication** : JWT token verification to identify requesting user
2. **👤 Authorization** : User identity extracted for ownership assignment
3. **✅ Business Validation** : PlaceService validates property data and enriches with `owner_id`
4. **💾 Persistence** : Property record inserted with owner reference
5. **📤 Response** : Complete place object returned with `201 Created` status

**Authentication Requirements:**
- ✅ Valid JWT token required
- 👤 User must be authenticated
- 🏠 `owner_id` automatically assigned from token

**Business Rules:**
- Only users with `is_host=true` can create places
- Location data must be valid coordinates
- Price validation against business rules

---

### ⭐ Review Submission
**Role:** Handles user review creation with integrity checks and verification.

**Key Steps:**
1. **🔐 Authentication** : JWT token verification for user identification
2. **🛡️ Integrity Check** : ReviewService verifies user hasn't already reviewed this place
3. **✅ Validation** : Data validation and enrichment with `user_id`
4. **💾 Persistence** : Review record created with user and place references
5. **📤 Response** : Review object returned with `201 Created` status

**Business Logic:**
- 🚫 **One-review-per-user** constraint enforced
- ⭐ Rating validation (typically 1-5 scale)
- 📝 Comment moderation capabilities
- 🔍 Review verification system

**Error Scenarios:**
- `400 Bad Request` if user already reviewed this place
- `401 Unauthorized` if invalid/missing JWT token
- `404 Not Found` if referenced place doesn't exist

---

### 🔍 Fetching a List of Places
**Role:** Provides flexible property search with filtering and pagination capabilities.

**Key Steps:**
1. **📨 Client Request** : `GET /places` with optional query parameters
2. **🎛️ Filter Processing** : PlaceService parses and validates search criteria
3. **🔍 Database Query** : Selective retrieval based on filters
4. **📊 Result Formatting** : Data preparation and pagination
5. **📤 Response** : Place list returned with `200 OK` status

**Supported Filters:**
- 🏙️ City/location-based filtering
- 💰 Price range (`min_price`, `max_price`)
- 👥 Guest capacity (`max_guests`)
- 🛏️ Room count (`number_of_rooms`)
- 📍 Geographic proximity (via coordinates)

**Performance Considerations:**
- 🚀 Database indexing on filter columns
- 📄 Pagination support for large result sets
- 🔍 Efficient query optimization

---

## 🔄 Layer Interaction Patterns

### 🎯 Presentation Layer (API)
**Responsibilities:**
- 📡 Request routing and endpoint management
- 🔐 Initial authentication checks
- 📋 Input validation and sanitization
- 📦 Response formatting and HTTP status management

### ⚙️ Business Logic Layer (Services)
**Responsibilities:**
- 🧠 Core business rules enforcement
- 🔍 Data validation and enrichment
- 🔗 Relationship management between entities
- 🛡️ Security and access control logic

### 💾 Persistence Layer (Database)
**Responsibilities:**
- 💽 Data storage and retrieval
- 🔍 Query optimization and execution
- 💾 Transaction management
- 📊 Data integrity enforcement

---

## 🛡️ Security & Validation Patterns

### 🔐 Authentication Flow
```
Client → [JWT Token] → API → AuthService → [user_id] → Business Logic
```

### ✅ Validation Hierarchy
1. **📋 Input Validation** (API Layer) - Syntax checking
2. **🧠 Business Validation** (Service Layer) - Rule enforcement  
3. **💾 Data Validation** (Database Layer) - Integrity constraints

### 🚦 HTTP Status Code Usage
- `200 OK` - Successful retrieval operations
- `201 Created` - Successful resource creation
- `400 Bad Request` - Client-side validation errors
- `401 Unauthorized` - Authentication failures
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server-side issues

---

## 🎯 Design Principles Applied

### 🔒 Separation of Concerns
Each layer has distinct responsibilities, promoting maintainability and testability.

### 🚀 Performance Optimization
- Efficient database query patterns
- Minimal data transfer between layers
- Appropriate caching strategies

### 🔐 Security First
- Authentication at entry point
- Authorization throughout business logic
- Data validation at multiple layers

### 📈 Scalability Considerations
- Stateless service design
- Database connection pooling
- Horizontal scaling capabilities