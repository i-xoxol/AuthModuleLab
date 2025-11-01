from auth import get_salt, get_hash, bytes_to_hex
from user import User

def create_user(username, password):
    salt = bytes_to_hex(get_salt(32))
    pass_salt = password + salt
    hashed_pass = get_hash(pass_salt)
    return User(username, hashed_pass, salt)
