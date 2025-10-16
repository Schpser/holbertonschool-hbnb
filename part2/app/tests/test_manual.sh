#!/bin/bash

# Arrêt immédiat si une commande échoue (bonne pratique)
set -e

echo "===================================================================="
echo "🚀 HBNB API TEST - SYNTAXE ROBUSTE (Extraction par grep/sed)"
echo "===================================================================="
echo

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Adresse de base de l'API (à ajuster si nécessaire)
API_URL="http://localhost:5000/api/v1"

print_step() { echo -e "${BLUE}▶ $1${NC}"; }
print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_info() { echo -e "${YELLOW}ℹ️  $1${NC}"; }

# Fonction pour extraire l'ID (Syntaxe robuste par grep/sed)
extract_id() {
    # Extrait la valeur de la clé "id" du JSON de manière plus directe
    echo "$1" | grep -o '"id": "[^"]*"' | sed -E 's/"id": "([^"]*)".*/\1/' || echo "ERROR"
}

# Variable pour stocker un ID de placeholder
PLACEHOLDER_ID="3fa85f64-5717-4562-b3fc-2c963f66afa6"

# ============================================================================
# 1. TEST USERS
# ============================================================================
print_step "1. TEST USERS"

# POST /api/v1/users/ (Création)
echo "Création user (John Doe)..."
USER_DATA='{"first_name": "John","last_name": "Doe","email": "john.doe@example.com"}'
USER_RESPONSE=$(curl -s -X POST "$API_URL/users/" \
    -H "Content-Type: application/json" \
    -d "$USER_DATA")
echo "Réponse API: $USER_RESPONSE" # Affichage brut de la réponse

USER_ID=$(extract_id "$USER_RESPONSE")
if [ "$USER_ID" = "ERROR" ]; then
    print_error "❌ Échec critique: Extraction de USER_ID impossible. Stop."
    exit 1
fi
print_success "User ID (John): $USER_ID"
echo

# GET /api/v1/users/<user_id>
echo "GET user by ID (John)..."
curl -s -X GET "$API_URL/users/$USER_ID"
echo

# GET /api/v1/users/ (Liste)
echo "GET tous les users..."
curl -s -X GET "$API_URL/users/" 
echo

# PUT /api/v1/users/<user_id> (Mise à jour)
echo "UPDATE user (vers Jane Doe)..."
USER_UPDATE_DATA='{"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"}'
curl -s -X PUT "$API_URL/users/$USER_ID" \
    -H "Content-Type: application/json" \
    -d "$USER_UPDATE_DATA"
echo

---

# ============================================================================
# 2. TEST AMENITIES
# ============================================================================
print_step "2. TEST AMENITIES"

# POST /api/v1/amenities/ (Création Wi-Fi)
echo "Création amenity 1 (Wi-Fi)..."
AM1_DATA='{"name": "Wi-Fi"}'
AM1_RESPONSE=$(curl -s -X POST "$API_URL/amenities/" \
    -H "Content-Type: application/json" -d "$AM1_DATA")
echo "Réponse API: $AM1_RESPONSE"

AM1_ID=$(extract_id "$AM1_RESPONSE")
if [ "$AM1_ID" = "ERROR" ]; then 
    print_error "❌ Échec critique: Extraction de AMENITY_ID impossible. Stop."
    exit 1
fi
print_success "Amenity ID (Wi-Fi): $AM1_ID"
echo

# GET /api/v1/amenities/ (Liste)
echo "GET toutes les amenities..."
curl -s -X GET "$API_URL/amenities/"
echo

# GET /api/v1/amenities/<amenity_id>
echo "GET amenity by ID (Wi-Fi)..."
curl -s -X GET "$API_URL/amenities/$AM1_ID"
echo

# PUT /api/v1/amenities/<amenity_id> (Mise à jour)
echo "UPDATE amenity (vers Air Conditioning)..."
AM_UPDATE_DATA='{"name": "Air Conditioning"}'
curl -s -X PUT "$API_URL/amenities/$AM1_ID" \
    -H "Content-Type: application/json" \
    -d "$AM_UPDATE_DATA"
echo

---

# ============================================================================
# 3. TEST PLACES
# ============================================================================
print_step "3. TEST PLACES"

# POST /api/v1/places/ (Création)
echo "Création place (Cozy Apartment)..."
PLACE_JSON=$(cat <<EOF
{
  "title": "Cozy Apartment",
  "description": "A nice place to stay",
  "price": 100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id": "$USER_ID"
}
EOF
)

PLACE_RESPONSE=$(curl -s -X POST "$API_URL/places/" \
    -H "Content-Type: application/json" -d "$PLACE_JSON")
echo "Réponse API: $PLACE_RESPONSE"

PLACE_ID=$(extract_id "$PLACE_RESPONSE")
if [ "$PLACE_ID" = "ERROR" ]; then
    print_error "❌ Échec critique: Extraction de PLACE_ID impossible. Stop."
    exit 1
fi
print_success "Place ID: $PLACE_ID"
echo

# GET /api/v1/places/ (Liste)
echo "GET toutes les places..."
curl -s -X GET "$API_URL/places/"
echo

# GET /api/v1/places/<place_id>
echo "GET place by ID (Cozy Apartment)..."
curl -s -X GET "$API_URL/places/$PLACE_ID"
echo

# PUT /api/v1/places/<place_id> (Mise à jour)
echo "UPDATE place (vers Luxury Condo)..."
PLACE_UPDATE_DATA='{"title": "Luxury Condo", "description": "An upscale place to stay", "price": 200.0}'
curl -s -X PUT "$API_URL/places/$PLACE_ID" \
    -H "Content-Type: application/json" \
    -d "$PLACE_UPDATE_DATA"
echo

---

# ============================================================================
# 4. TEST REVIEWS
# ============================================================================
print_step "4. TEST REVIEWS"

# POST /api/v1/reviews/ (Création)
echo "Création review (Great place to stay!)..."
REVIEW_JSON=$(cat <<EOF
{
    "text": "Great place to stay!",
    "rating": 5,
    "user_id": "$USER_ID",
    "place_id": "$PLACE_ID"
}
EOF
)

REVIEW_RESPONSE=$(curl -s -X POST "$API_URL/reviews/" \
    -H "Content-Type: application/json" -d "$REVIEW_JSON")
echo "Réponse API: $REVIEW_RESPONSE"

REVIEW_ID=$(extract_id "$REVIEW_RESPONSE")
if [ "$REVIEW_ID" = "ERROR" ]; then
    print_error "❌ Échec création review. Les tests suivants pourraient échouer."
    REVIEW_ID="$PLACEHOLDER_ID"
fi
print_success "Review ID: $REVIEW_ID"
echo

# GET /api/v1/reviews/ (Liste)
echo "GET toutes les reviews..."
curl -s -X GET "$API_URL/reviews/"
echo

# GET /api/v1/reviews/<review_id>
echo "GET review by ID (Great place to stay!)..."
curl -s -X GET "$API_URL/reviews/$REVIEW_ID"
echo

# PUT /api/v1/reviews/<review_id> (Mise à jour)
echo "UPDATE review (vers Amazing stay!)..."
REVIEW_UPDATE_DATA='{"text": "Amazing stay!", "rating": 4}'
curl -s -X PUT "$API_URL/reviews/$REVIEW_ID" \
    -H "Content-Type: application/json" \
    -d "$REVIEW_UPDATE_DATA"
echo

# GET /api/v1/places/<place_id>/reviews
echo "GET reviews par place..."
curl -s -X GET "$API_URL/places/$PLACE_ID/reviews"
echo

# DELETE /api/v1/reviews/<review_id>
echo "DELETE review..."
curl -s -X DELETE "$API_URL/reviews/$REVIEW_ID"
echo

---

# ============================================================================
# 5. RAPPORT FINAL
# ============================================================================
print_step "📊 RAPPORT FINAL"

print_success "Tests terminés. Vérifiez les codes de retour et les IDs ci-dessous."

echo
echo "===================================================================="
print_info "IDs utilisés dans les tests (si extraits):"
print_info "User: $USER_ID"
print_info "Amenity: $AM1_ID" 
print_info "Place: $PLACE_ID"
print_info "Review: $REVIEW_ID"
echo "===================================================================="