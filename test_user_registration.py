
import unittest
import os
from user_registration import create_user, register_user
from auth import load_users, find_user

# Test suite for the user registration module functions.
class TestUserRegistration(unittest.TestCase):

    # Set up method to run before each test.
    def setUp(self):
        # Define a temporary database file for testing.
        self.test_db = 'test_users.json'
        # Create an empty JSON file to simulate an empty user database.
        with open(self.test_db, 'w') as f:
            f.write('[]')

    # Tear down method to run after each test.
    def tearDown(self):
        # Remove the temporary database file after each test.
        os.remove(self.test_db)

    # Test the create_user function.
    def test_create_user(self):
        # Create a new user.
        user = create_user("testuser", "testpassword")
        # Assert that the username is correctly set.
        self.assertEqual(user.username, "testuser")
        # Assert that the hashed password is not None.
        self.assertIsNotNone(user.hpass)
        # Assert that the salt is not None.
        self.assertIsNotNone(user.salt)

    # Test the register_user function with a new user.
    def test_register_user_new(self):
        # Attempt to register a new user.
        result = register_user("newuser", "newpassword", self.test_db)
        # Assert that the registration was successful.
        self.assertTrue(result)
        # Load the users from the test database.
        users = load_users(self.test_db)
        # Assert that the newly registered user can be found.
        self.assertIsNotNone(find_user(users, "newuser"))

    # Test the register_user function with an existing user.
    def test_register_user_existing(self):
        # Register a user first.
        register_user("existinguser", "password", self.test_db)
        # Attempt to register the same user again.
        result = register_user("existinguser", "password", self.test_db)
        # Assert that the registration of the existing user failed.
        self.assertFalse(result)

# Run the tests if the script is executed directly.
if __name__ == '__main__':
    unittest.main()
