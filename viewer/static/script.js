const currentYear = new Date().getFullYear();
document.getElementById("copywright-text").textContent = `© created by Matúš Kočik, ${currentYear}`;

/* document.querySelectorAll('nav a').forEach(function(link) {
    if (window.location.href.includes(link.getAttribute('href'))) {
        link.classList.add('active');
    }
}) */

document.querySelector('.hamburger-menu').addEventListener('click', function() {
    document.querySelector('nav').classList.toggle('open');
});
