
from flask import Flask, request, jsonify, send_from_directory
import auth

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

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

if __name__ == '__main__':
    app.run(debug=True)
