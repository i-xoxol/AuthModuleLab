
import unittest
import os
from user_registration import create_user, register_user
from auth import load_users, find_user

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        # Create a dummy users.json file for testing
        self.test_db = 'test_users.json'
        with open(self.test_db, 'w') as f:
            f.write('[]')

    def tearDown(self):
        # Remove the dummy users.json file
        os.remove(self.test_db)

    def test_create_user(self):
        user = create_user("testuser", "testpassword")
        self.assertEqual(user.username, "testuser")
        self.assertIsNotNone(user.hpass)
        self.assertIsNotNone(user.salt)

    def test_register_user_new(self):
        result = register_user("newuser", "newpassword", self.test_db)
        self.assertTrue(result)
        users = load_users(self.test_db)
        self.assertIsNotNone(find_user(users, "newuser"))

    def test_register_user_existing(self):
        # Register a user first
        register_user("existinguser", "password", self.test_db)
        # Try to register the same user again
        result = register_user("existinguser", "password", self.test_db)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
