import hashlib
import os
import json
from user import User

def get_salt(length):
    return os.urandom(length)

def get_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def bytes_to_hex(byte_array):
    return byte_array.hex()

def user_to_json(user):
    return json.dumps(user.__dict__, indent=4)

def json_to_user(json_string):
    user_dict = json.loads(json_string)
    return User(user_dict['username'], user_dict['hpass'], user_dict['salt'])

def find_user(user_list, username):
    for user in user_list:
        if user.username.lower() == username.lower():
            return user
    return None

def save_users(user_list, filepath):
    with open(filepath, 'w') as f:
        json.dump([user.__dict__ for user in user_list], f, indent=4)

def load_users(filepath):
    try:
        with open(filepath, 'r') as f:
            user_dicts = json.load(f)
            return [User(user_dict['username'], user_dict['hpass'], user_dict['salt']) for user_dict in user_dicts]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
