# Represents a user with username, hashed password, and salt.
class User:
    # Initialize a new User object.
    def __init__(self, username, hpass, salt):
        self.username = username  # The user's username.
        self.hpass = hpass      # The user's hashed password.
        self.salt = salt        # The salt used to hash the password.

    # Check if two User objects are equal based on their username (case-insensitive).
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username.lower() == other.username.lower()

    # Return a string representation of the User object.
    def __str__(self):
        return f"User: {self.username}, {self.hpass}, {self.salt}"
