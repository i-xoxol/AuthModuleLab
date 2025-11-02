
from flask import Flask, request, jsonify, send_from_directory
import auth
import user_registration

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/login.html')
def login_page():
    return send_from_directory('.', 'login.html')

@app.route('/register.html')
def register_page():
    return send_from_directory('.', 'register.html')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

@app.route('/register.js')
def register_script():
    return send_from_directory('.', 'register.js')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    users = auth.load_users('usersdb.json')
    user = auth.find_user(users, username)

    if user:
        # Hash the provided password with the user's salt
        password_hash = auth.get_hash(password + user.salt)
        if password_hash == user.hpass:
            return jsonify({'message': 'Login successful'})

    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if user_registration.register_user(username, password):
        return jsonify({'message': 'Registration successful'})
    else:
        return jsonify({'error': 'Username already exists'}), 409

if __name__ == '__main__':
    app.run(debug=True)
