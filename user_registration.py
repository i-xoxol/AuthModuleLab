# Import necessary functions from the auth module and the User class
from auth import get_salt, get_hash, bytes_to_hex, load_users, save_users, find_user
from user import User

# --- User Creation and Registration ---

# Create a new User object with a hashed password and salt.
def create_user(username, password):
    # Generate a 32-byte salt and convert it to a hex string.
    salt = bytes_to_hex(get_salt(32))
    # Concatenate the password and salt.
    pass_salt = password + salt
    # Hash the password-salt combination.
    hashed_pass = get_hash(pass_salt)
    # Return a new User object.
    return User(username, hashed_pass, salt)

# Register a new user.
def register_user(username, password):
    # Load the list of existing users from the database file.
    users = load_users('usersdb.json')
    # Check if a user with the same username already exists.
    if find_user(users, username):
        return False  # User already exists

    # Create a new user.
    new_user = create_user(username, password)
    # Add the new user to the list.
    users.append(new_user)
    # Save the updated list of users to the database file.
    save_users(users, 'usersdb.json')
    # Return True to indicate successful registration.
    return True
