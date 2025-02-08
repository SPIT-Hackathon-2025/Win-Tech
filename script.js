// Category tabs functionality
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
    });
});

// Search functionality
const searchInput = document.querySelector('.search-bar input');
searchInput.addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    // Add search logic here
    console.log('Searching for:', searchTerm);
});

// Bike card interactions
document.querySelectorAll('.bike-card').forEach(card => {
    card.addEventListener('click', () => {
        // Add bike selection logic here
        console.log('Selected bike:', card.querySelector('h3').textContent);
    });
});
