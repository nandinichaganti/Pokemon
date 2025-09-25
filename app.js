// Function to load content based on the hash
function loadContent() {
    const hash = window.location.hash || "#home";
    const app = document.getElementById("app");
    document.body.classList.toggle("home-active", hash === "#home");

    // Fetch the corresponding HTML file
    fetch(`views/${hash.substring(1)}.html`)
        .then(response => response.text())
        .then(html => {
            app.innerHTML = html;
        })
        .catch(err => {
            app.innerHTML = "<h1>Page Not Found</h1>";
        });
}

// Load content when the page loads
window.addEventListener("load", loadContent);

// Load content when the hash changes
window.addEventListener("hashchange", loadContent);
