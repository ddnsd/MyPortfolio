document.addEventListener('DOMContentLoaded', function () {
    // Check if localStorage is available
    if (typeof localStorage !== 'undefined') {
        // Retrieve the theme preference from local storage
        const themePreference = localStorage.getItem('themePreference');

        // Set the initial theme based on the stored preference
        if (themePreference === 'dark') {
            document.body.classList.add('dark-theme');
        } else {
            document.body.classList.remove('dark-theme');
        }
    }
});

function toggleTheme() {
    const body = document.body;
    const themeSwitch = document.getElementById('themeSwitch');

    // Toggle the dark-mode class on the body
    body.classList.toggle('dark-mode');

    // Check if the body now has the dark-mode class
    if (body.classList.contains('dark-mode')) {
        // If it does, store the dark theme preference and update the button text
        localStorage.setItem('themePreference', 'dark');
        themeSwitch.textContent = 'Switch to Light Mode';
    } else {
        // If it doesn't, store the light theme preference and update the button text
        localStorage.setItem('themePreference', 'light');
        themeSwitch.textContent = 'Switch to Dark Mode';
    }
}

// When the page loads, apply the stored theme preference
window.onload = function() {
    const body = document.body;
    const themeSwitch = document.getElementById('themeSwitch');
    const themePreference = localStorage.getItem('themePreference');

    if (themePreference === 'dark') {
        body.classList.add('dark-mode');
        themeSwitch.textContent = 'Switch to Light Mode';
    } else {
        body.classList.remove('dark-mode');
        themeSwitch.textContent = 'Switch to Dark Mode';
    }
};