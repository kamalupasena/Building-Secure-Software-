// Fake login check with hardcoded check
const username = prompt("Username:");
const password = prompt("Password:");

if (username === "admin" && password === "admin123") {
    alert("Welcome!");
} else {
    alert("Access denied.");
}