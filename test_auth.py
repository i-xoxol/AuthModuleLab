import unittest
import os
import json
from auth import get_salt, get_hash, bytes_to_hex, user_to_json, json_to_user, find_user, save_users, load_users
from user import User

# Test suite for the authentication module functions.
class TestAuth(unittest.TestCase):

    # Test the get_salt function.
    def test_get_salt(self):
        # Generate a salt of 32 bytes.
        salt1 = get_salt(32)
        # Assert that the salt is not None.
        self.assertIsNotNone(salt1)
        # Assert that the length of the salt is 32 bytes.
        self.assertEqual(len(salt1), 32)
        # Generate another salt.
        salt2 = get_salt(32)
        # Assert that the two salts are different (randomness).
        self.assertNotEqual(salt1, salt2)

    # Test the get_hash function.
    def test_get_hash(self):
        # Define a test string and its expected SHA-256 hash.
        test_string = "TEST"
        test_hash = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2"
        # Calculate the hash of the test string.
        hash_result = get_hash(test_string)
        # Assert that the calculated hash matches the expected hash.
        self.assertEqual(hash_result, test_hash)

    # Test the bytes_to_hex function.
    def test_bytes_to_hex(self):
        # Define a byte array and its expected hexadecimal string representation.
        byte_array = b'\x01\x02\x03'
        hex_string = bytes_to_hex(byte_array)
        # Assert that the converted hexadecimal string is correct.
        self.assertEqual(hex_string, "010203")

    # Test the json_to_user function.
    def test_json_to_user(self):
        # Define a JSON string representing a user.
        json_string = '{"username": "user1", "hpass": "password", "salt": "somesalt"}'
        # Create a User object with the same data.
        user = User("user1", "password", "somesalt")
        # Convert the JSON string back to a User object.
        user_from_json = json_to_user(json_string)
        # Assert that the converted User object is equal to the original User object.
        self.assertEqual(user, user_from_json)

    # Test the user_to_json function.
    def test_user_to_json(self):
        # Create a User object.
        user = User("user1", "password", "somesalt")
        # Convert the User object to a JSON string.
        json_string = user_to_json(user)
        # Convert the JSON string back to a User object.
        user_from_json = json_to_user(json_string)
        # Assert that the round-trip conversion results in an equal User object.
        self.assertEqual(user, user_from_json)

    # Test the find_user function with a list of users.
    def test_find_user(self):
        # Create a list of User objects.
        users = [
            User("user1", "pass1", "salt1"),
            User("user2", "pass2", "salt2"),
            User("user3", "pass3", "salt3"),
        ]
        # Try to find an existing user.
        found_user = find_user(users, "user2")
        # Assert that the user was found.
        self.assertIsNotNone(found_user)
        # Assert that the username of the found user is correct.
        self.assertEqual(found_user.username, "user2")
        # Try to find a non-existent user.
        not_found_user = find_user(users, "user4")
        # Assert that the non-existent user was not found.
        self.assertIsNone(not_found_user)

    # Test the find_user function with an empty list of users.
    def test_find_user_empty_list(self):
        # Create an empty list of users.
        users = []
        # Try to find a user in the empty list.
        not_found_user = find_user(users, "user1")
        # Assert that no user was found.
        self.assertIsNone(not_found_user)

    # Test the save_users and load_users functions.
    def test_save_load_users(self):
        # Create a list of users to save.
        users_to_save = [
            User("user1", "pass1", "salt1"),
            User("user2", "pass2", "salt2"),
            User("user3", "pass3", "salt3"),
        ]
        # Define a temporary filepath for the test database.
        filepath = "test_users.json"
        # Save the users to the file.
        save_users(users_to_save, filepath)
        # Load the users from the file.
        loaded_users = load_users(filepath)
        # Assert that the number of saved and loaded users is the same.
        self.assertEqual(len(users_to_save), len(loaded_users))
        # Assert that each saved user is equal to its corresponding loaded user.
        for i in range(len(users_to_save)):
            self.assertEqual(users_to_save[i], loaded_users[i])
        # Clean up: remove the temporary test database file.
        os.remove(filepath)

    # Test loading users from a non-existent file.
    def test_load_users_non_existent_file(self):
        # Attempt to load users from a file that does not exist.
        loaded_users = load_users("non_existent_file.json")
        # Assert that an empty list is returned.
        self.assertEqual(loaded_users, [])

    # Test loading users from an empty file.
    def test_load_users_empty_file(self):
        # Define a temporary filepath for an empty file.
        filepath = "empty_file.json"
        # Create an empty file.
        with open(filepath, 'w') as f:
            f.write("")
        # Attempt to load users from the empty file.
        loaded_users = load_users(filepath)
        # Assert that an empty list is returned.
        self.assertEqual(loaded_users, [])
        # Clean up: remove the temporary empty file.
        os.remove(filepath)

    # Test loading users from a corrupted JSON file.
    def test_load_users_corrupted_file(self):
        # Define a temporary filepath for a corrupted file.
        filepath = "corrupted_file.json"
        # Create a file with invalid JSON content.
        with open(filepath, 'w') as f:
            f.write("this is not json")
        # Attempt to load users from the corrupted file.
        loaded_users = load_users(filepath)
        # Assert that an empty list is returned.
        self.assertEqual(loaded_users, [])
        # Clean up: remove the temporary corrupted file.
        os.remove(filepath)

# Run the tests if the script is executed directly.
if __name__ == '__main__':
    unittest.main()
