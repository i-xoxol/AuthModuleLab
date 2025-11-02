
# Import necessary modules from Flask and other files
from flask import Flask, request, jsonify, send_from_directory
import auth
import user_registration

# Create a Flask application instance
app = Flask(__name__)

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
            return jsonify({'message': 'Login successful'})

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

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
