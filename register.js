
// Add an event listener to the registration form to handle submission.
document.getElementById('registerForm').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior.
    event.preventDefault();

    // Get the username and password from the form.
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Get the message element to display feedback to the user.
    const messageElement = document.getElementById('message');

    // Send a POST request to the /register endpoint.
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    // Parse the JSON response.
    .then(response => response.json())
    // Handle the response data.
    .then(data => {
        if (data.message) {
            // Redirect to the main page with a success message.
            window.location.href = '/?registration=success';
        } else {
            // Display an error message.
            messageElement.textContent = data.error;
            messageElement.style.color = 'red';
        }
    })
    // Handle any errors that occur during the fetch.
    .catch(error => {
        console.error('Error:', error);
        messageElement.textContent = 'An error occurred. Please try again.';
        messageElement.style.color = 'red';
    });
});
