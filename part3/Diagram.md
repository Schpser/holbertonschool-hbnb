Part 3 Diagram

---
config:
  layout: elk
---
erDiagram
    USER {
        UUID4 id PK
        string first_name
        string last_name
        string email
        string password
        boolean is_admin
        datetime created_at
        datetime updated_at
    }
    PLACE {
        UUID4 id PK
        string title
        string description
        decimal price
        decimal latitude
        decimal longitude
        UUID4 owner_id FK
        datetime created_at
        datetime updated_at
    }
    REVIEW {
        UUID4 id PK
        string text
        int rating
        UUID4 user_id FK
        UUID4 place_id FK
        datetime created_at
        datetime updated_at
    }
    AMENITY {
        UUID4 id PK
        string name
        datetime created_at
        datetime updated_at
    }
    PLACE_AMENITY {
        UUID4 place_id PK,FK
        UUID4 amenity_id PK,FK
    }
    USER ||--o{ PLACE : owns
    USER ||--o{ REVIEW : writes
    PLACE ||--o{ REVIEW : receives
    PLACE ||--o{ PLACE_AMENITY : has
    AMENITY ||--o{ PLACE_AMENITY : includes
