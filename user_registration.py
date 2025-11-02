from auth import get_salt, get_hash, bytes_to_hex, load_users, save_users, find_user
from user import User

def create_user(username, password):
    salt = bytes_to_hex(get_salt(32))
    pass_salt = password + salt
    hashed_pass = get_hash(pass_salt)
    return User(username, hashed_pass, salt)

def register_user(username, password):
    users = load_users('usersdb.json')
    if find_user(users, username):
        return False  # User already exists

    new_user = create_user(username, password)
    users.append(new_user)
    save_users(users, 'usersdb.json')
    return True
