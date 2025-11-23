/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            try {
                /* API CALL */
                const response = await fetch('http://localhost:5000/api/v1/auth/login', {
                    method: 'POST',
                    mode: 'cors',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        email: email,
                        password: password
                    })
                });
                
                const data = await response.json();

                if (response.ok) {
                    console.log('Token received:', data.access_token);
                    sessionStorage.setItem('token', data.access_token);
                    window.location.href = 'index.html';
                }
                else {
                    const errorMessage = document.getElementById('error-message');
                    if (data.error === 'Invalid credentials') {
                        errorMessage.textContent = 'Wrong email or password';
                    } else {
                        errorMessage.textContent = data.error || 'Login failed';
                    }
                    errorMessage.style.display = 'block';
                }
                
            } catch (error) {
                console.error('Error:', error);
                alert('Network error - please try again');
            }
        });
    }
    if (window.location.pathname.includes('index.html') || 
        window.location.pathname === '/' || 
        window.location.pathname.endsWith('/')) {
        checkAuth();
    }
    const logoutLink = document.getElementById('logout-link');
    if (logoutLink) {
        logoutLink.addEventListener('click', (event) => {
            event.preventDefault();
            logout();
        });
    }
    if (window.location.pathname.includes('place.html')) {
    const placeId = getPlaceIdFromURL();
    if (placeId) {
        loadPlaceDetails(placeId);
    } else {
        console.error('No place ID found in URL');
    }
      }

  const maxPriceSlider = document.getElementById('max-price');
  const priceDisplay = document.getElementById('price-display');

  if (maxPriceSlider && priceDisplay) {
      maxPriceSlider.addEventListener('input', function() {
          priceDisplay.textContent = `€${this.value}`;
          filterPlacesByMaxPrice(this.value);
      });
  }
});

function filterPlacesByMaxPrice(maxPrice) {
    const placeCards = document.querySelectorAll('.place-card');
    
    placeCards.forEach(card => {
        const priceText = card.querySelector('.place-price').textContent;
        const price = parseInt(priceText.match(/\d+/)) || 0;
        
        if (price <= parseInt(maxPrice)) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}

function getCookie(name) {
    return sessionStorage.getItem(name);
}

async function checkAuth() {
    const token = getCookie('token'); 
    const loginLink = document.getElementById('login-link');
    const logoutLink = document.getElementById('logout-link');
    
    if (token) {
        loginLink.style.display = 'none';
        logoutLink.style.display = 'block';
        console.log('✅ User connected !');
        const places = await fetchPlaces();
        displayPlaces(places);
    } else {
        loginLink.style.display = 'block';
        logoutLink.style.display = 'none';
        console.log('❌ User disconnected');
    }
}

async function fetchPlaces() {
    /* GET PLACES */
    try {
        const token = getCookie('token');
        const response = await fetch('http://localhost:5000/api/v1/places/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            throw new Error('Failed to fetch places');
        }
        
        const places = await response.json();
        return places;
        
    } catch (error) {
        console.error('Error fetching places:', error);
        return [];
    }
}
function displayPlaces(places) {
    /* CREATE DYNAMIC CARDS */
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = '';
    
    if (places.length === 0) {
        placesList.innerHTML = '<p>No places available</p>';
        return;
    }
    places.forEach(place => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        
        placeCard.innerHTML = `
            <img src="images/icon_bed.png" alt="Place" class="place-image">
            <div class="place-content">
              <h3 class="place-name">${place.title || 'Unnamed Place'}</h3>
              <p class="place-price">€${place.price || 'N/A'} / night</p>
              <p class="place-location">Location: ${place.latitude}, ${place.longitude}</p>
              <p class="place-description">${place.description || 'No description available'}</p>
              <button class="details-button" onclick="location.href='place.html?place_id=${place.id}'">View Details</button>
            </div>
        `;
        
        placesList.appendChild(placeCard);
    });
}

function displayPlaceDetails(place) {
    // Affiche les informations principales
    const placeDetails = document.getElementById('place-details');
    
    placeDetails.innerHTML = `
        <div class="place-info">
            <h2>${place.title || 'Unnamed Place'}</h2>
            
            <div class="place-meta">
                <p><strong>Host:</strong> ${place.owner?.first_name || 'Unknown'} ${place.owner?.last_name || ''}</p>
                <p><strong>Price:</strong> €${place.price || 'N/A'} / night</p>
                <p><strong>Location:</strong> ${place.latitude}, ${place.longitude}</p>
            </div>
            
            <div class="place-description">
                <h3>Description</h3>
                <p>${place.description || 'No description available'}</p>
            </div>
            
            <div class="place-amenities">
                <h3>Amenities</h3>
                <div class="amenities-list">
                    ${place.amenities && place.amenities.length > 0 
                        ? place.amenities.map(amenity => `
                            <span class="amenity">
                                <img src="images/icon_${amenity.name?.toLowerCase() || 'default'}.png" alt="${amenity.name}" class="amenity-icon">
                                ${amenity.name}
                            </span>
                        `).join('')
                        : '<p>No amenities listed</p>'
                    }
                </div>
            </div>
        </div>
    `;
    
    // Affiche les reviews
    const reviewsSection = document.getElementById('reviews');
    
    if (place.reviews && place.reviews.length > 0) {
        reviewsSection.innerHTML = `
            <h2>Traveler Reviews</h2>
            ${place.reviews.map(review => `
                <div class="review-card">
                    <div class="review-header">
                        <strong>User ${review.user_id}</strong>
                        <span class="rating">
                            <span class="rating-stars">${'★'.repeat(review.rating || 0)}${'☆'.repeat(5 - (review.rating || 0))}</span>
                            <span class="rating-number">${review.rating || 0}/5</span>
                        </span>
                    </div>
                    <p class="review-comment">"${review.text || 'No comment'}"</p>
                    <small class="review-date">Posted recently</small>
                </div>
            `).join('')}
        `;
    } else {
        reviewsSection.innerHTML = '<h2>Traveler Reviews</h2><p>No reviews yet</p>';
    }
}

function getPlaceIdFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('place_id');
}

async function loadPlaceDetails(placeId) {
    const place = await fetchPlaceDetails(placeId);
    
    if (place) {
        console.log('Place details loaded:', place);
        displayPlaceDetails(place);
    } else {
        alert('Failed to load place details');
    }
}

async function fetchPlaceDetails(placeId) {
    try {
        const token = getCookie('token');
        
        const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}/`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            throw new Error('Failed to fetch place details');
        }
        
        const place = await response.json();
        return place;
        
    } catch (error) {
        console.error('Error fetching place details:', error);
        return null;
    }
}

function logout() {
    sessionStorage.removeItem('token');
    alert('Logged out successfully! 👋');
    window.location.href = 'index.html';
}
