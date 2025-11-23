// test-simple.js - Version ultra simplifiée
console.log("🔄 test-simple.js chargé");

document.addEventListener('DOMContentLoaded', () => {
    console.log("✅ DOM chargé - PAS DE BOUCLE");
    
    // Juste l'essentiel
    const loginLink = document.getElementById('login-link');
    const logoutLink = document.getElementById('logout-link');
    
    if (loginLink) loginLink.style.display = 'block';
    if (logoutLink) logoutLink.style.display = 'none';
    
    console.log("🎯 Configuration de base terminée");
});
