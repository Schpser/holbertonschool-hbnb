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
                document.cookie = `token=${data.access_token}; path=/; max-age=86400`; // 24h
                window.location.href = 'index.html';
            }
                else {
                alert('Login failed: ' + (data.error || 'Unknown error'));
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
});

function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [cookieName, cookieValue] = cookie.trim().split('=');
        if (cookieName === name) {
            return decodeURIComponent(cookieValue);
        }
    }
    return null;
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
        const response = await fetch('http://localhost:5000/api/v1/places', {
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
                <h3 class="place-name">${place.name || 'Unnamed Place'}</h3>
                <p class="place-price">€${place.price_per_night || 'N/A'} / night</p>
                <p class="place-description">${place.description || 'No description available'}</p>
                <button class="details-button" onclick="viewPlaceDetails('${place.id}')">View Details</button>
            </div>
        `;
        
        placesList.appendChild(placeCard);
    });
}

function logout() {
    document.cookie = 'token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
    alert('Logged out successfully! 👋');
    window.location.href = 'index.html';
}
