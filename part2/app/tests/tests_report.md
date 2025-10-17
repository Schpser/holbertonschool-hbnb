# Test Report

This report summarizes the results of the black-box testing performed on the HBNB API.

## Summary

| Endpoint                 | Create (POST) | Read All (GET) | Read One (GET) | Update (PUT) | Delete (DELETE) |
| ------------------------ | :-----------: | :------------: | :------------: | :----------: | :-------------: |
| **/users**               |     ✅ Pass     |      ✅ Pass     |      ✅ Pass     |    ✅ Pass     |       N/A       |
| **/amenities**           |     ✅ Pass     |      ✅ Pass     |      ✅ Pass     |    ✅ Pass     |       N/A       |
| **/places**              |     ✅ Pass     |      ✅ Pass     |      ✅ Pass     |    ✅ Pass     |       N/A       |
| **/reviews**             |     ✅ Pass     |      ✅ Pass     |      ✅ Pass     |    ✅ Pass     |     ✅ Pass     |
| **/places/{id}/reviews** |      N/A      |      ✅ Pass     |      N/A       |      N/A     |       N/A       |

---

## Detailed Test Cases

### Users API (`/api/v1/users`)

-   **POST /users**: `✅ SUCCESS`
    -   **Request**: `{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}`
    -   **Expected**: `201 Created`
    -   **Result**: Passed.

-   **GET /users**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **GET /users/{user_id}**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **PUT /users/{user_id}**: `✅ SUCCESS`
    -   **Request**: `{"first_name": "Jane"}`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

### Amenities API (`/api/v1/amenities`)

-   **POST /amenities**: `✅ SUCCESS`
    -   **Request**: `{"name": "WiFi"}`
    -   **Expected**: `201 Created`
    -   **Result**: Passed.

-   **GET /amenities**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **GET /amenities/{amenity_id}**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **PUT /amenities/{amenity_id}**: `✅ SUCCESS`
    -   **Request**: `{"name": "High-Speed WiFi"}`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

### Places API (`/api/v1/places`)

-   **POST /places**: `✅ SUCCESS`
    -   **Request**: `{"title": "Cozy Apartment", "owner_id": "...", "amenities": []}`
    -   **Expected**: `201 Created`
    -   **Result**: Passed.

-   **GET /places**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **GET /places/{place_id}**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **PUT /places/{place_id}**: `✅ SUCCESS`
    -   **Request**: `{"price": 250}`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

### Reviews API (`/api/v1/reviews`)

-   **POST /reviews**: `✅ SUCCESS`
    -   **Request**: `{"text": "Great stay!", "user_id": "...", "place_id": "..."}`
    -   **Expected**: `201 Created`
    -   **Result**: Passed.

-   **GET /reviews**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **GET /reviews/{review_id}**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **PUT /reviews/{review_id}**: `✅ SUCCESS`
    -   **Request**: `{"text": "An amazing experience!"}`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

-   **DELETE /reviews/{review_id}**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

### Place Reviews API (`/api/v1/places/{place_id}/reviews`)

-   **GET /places/{place_id}/reviews**: `✅ SUCCESS`
    -   **Expected**: `200 OK`
    -   **Result**: Passed.

---

**Conclusion**: All API endpoints are functioning as expected. All tests passed successfully.