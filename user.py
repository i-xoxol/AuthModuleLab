class User:
    def __init__(self, username, hpass, salt):
        self.username = username
        self.hpass = hpass
        self.salt = salt

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username.lower() == other.username.lower()

    def __str__(self):
        return f"User: {self.username}, {self.hpass}, {self.salt}"
