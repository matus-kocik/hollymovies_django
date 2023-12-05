const currentYear = new Date().getFullYear();
document.getElementById("copywright-text").textContent = "© preco to nefunguje, ${currentYear}";

document.querySelectorAll('nav a').forEach(function(link) {
    if (window.location.href.includes(link.getAttribute('href'))) {
        link.classList.add('active');
    }
})

document.querySelector('.hamburger-menu').addEventListener('click', function() {
    document.querySelector('nav').classList.toggle('open');
});



/* © created by Matúš Kočik */