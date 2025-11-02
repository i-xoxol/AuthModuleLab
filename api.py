
# Import necessary modules from Flask and other files
from flask import Flask, request, jsonify, send_from_directory
import auth
import user_registration
import os

# Create a Flask application instance
app = Flask(__name__)

# --- In-memory Session Store ---
# In a real-world application, use a more robust session management solution
# like a database or a cache (e.g., Redis).
sessions = {}

# --- Helper Functions ---

# Verify a session token.
def verify_token(token):
    return sessions.get(token)

# --- Static File Routes ---

# Serve the main welcome page
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve the login page
@app.route('/login.html')
def login_page():
    return send_from_directory('.', 'login.html')

# Serve the registration page
@app.route('/register.html')
def register_page():
    return send_from_directory('.', 'register.html')

# Serve the main JavaScript file for the login page
@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

# Serve the JavaScript file for the registration page
@app.route('/register.js')
def register_script():
    return send_from_directory('.', 'register.js')

# Serve the CSS file
@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

# --- API Routes ---

# Handle user login
@app.route('/login', methods=['POST'])
def login():
    # Get the JSON data from the request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Load users from the database
    users = auth.load_users('usersdb.json')
    # Find the user by username
    user = auth.find_user(users, username)

    # If the user exists, verify the password
    if user:
        # Hash the provided password with the user's salt
        password_hash = auth.get_hash(password + user.salt)
        # Compare the hashed password with the stored hash
        if password_hash == user.hpass:
            # Generate a session token
            token = os.urandom(24).hex()
            # Store the session token with the username
            sessions[token] = username
            # Return a success message and the session token
            return jsonify({'message': 'Login successful', 'token': token})

    # Return an error if the credentials are not valid
    return jsonify({'error': 'Invalid credentials'}), 401

# Handle user registration
@app.route('/register', methods=['POST'])
def register():
    # Get the JSON data from the request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Register the new user
    if user_registration.register_user(username, password):
        return jsonify({'message': 'Registration successful'})
    else:
        # Return an error if the username already exists
        return jsonify({'error': 'Username already exists'}), 409

# Protected profile endpoint
@app.route('/profile')
def profile():
    # Get the session token from the request headers
    token = request.headers.get('Authorization')
    # Verify the session token
    username = verify_token(token)
    if username:
        return jsonify({'message': f'Welcome, {username}!'})
    else:
        return jsonify({'error': 'Invalid or expired token'}), 401

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
