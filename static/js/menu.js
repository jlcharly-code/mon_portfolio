// Menu mobile (hamburger)
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('nav-menu-active');
    hamburger.classList.toggle('hamburger-active');
});

// Ferme le menu si on clique sur un lien
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('nav-menu-active');
        hamburger.classList.remove('hamburger-active');
    });
});