
// Add an event listener to the login form to handle submission.
document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior.
    event.preventDefault();

    // Get the username and password from the form.
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Get the message element to display feedback to the user.
    const messageElement = document.getElementById('message');

    // Send a POST request to the /login endpoint.
    fetch('/login', {
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
        if (data.token) {
            // Display a success message.
            messageElement.textContent = data.message;
            messageElement.style.color = 'green';
            // Store the session token in local storage.
            localStorage.setItem('token', data.token);
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

// Add an event listener to the 'Get Profile' button.
document.getElementById('getProfileBtn').addEventListener('click', function() {
    // Get the session token from local storage.
    const token = localStorage.getItem('token');
    // Get the profile element to display the profile information.
    const profileElement = document.getElementById('profile');

    // If the token is not available, display an error message.
    if (!token) {
        profileElement.textContent = 'You are not logged in.';
        profileElement.style.color = 'red';
        return;
    }

    // Send a GET request to the /profile endpoint with the session token in the Authorization header.
    fetch('/profile', {
        headers: {
            'Authorization': token
        }
    })
    // Parse the JSON response.
    .then(response => response.json())
    // Handle the response data.
    .then(data => {
        if (data.message) {
            // Display the profile information.
            profileElement.textContent = data.message;
            profileElement.style.color = 'green';
        } else {
            // Display an error message.
            profileElement.textContent = data.error;
            profileElement.style.color = 'red';
        }
    })
    // Handle any errors that occur during the fetch.
    .catch(error => {
        console.error('Error:', error);
        profileElement.textContent = 'An error occurred. Please try again.';
        profileElement.style.color = 'red';
    });
});
