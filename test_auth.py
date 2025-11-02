import unittest
import os
import json
from auth import get_salt, get_hash, bytes_to_hex, user_to_json, json_to_user, find_user, save_users, load_users
from user import User

class TestAuth(unittest.TestCase):

    def test_get_salt(self):
        salt1 = get_salt(32)
        self.assertIsNotNone(salt1)
        self.assertEqual(len(salt1), 32)
        salt2 = get_salt(32)
        self.assertNotEqual(salt1, salt2)

    def test_get_hash(self):
        test_string = "TEST"
        test_hash = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2"
        hash_result = get_hash(test_string)
        self.assertEqual(hash_result, test_hash)

    def test_bytes_to_hex(self):
        byte_array = b'\x01\x02\x03'
        hex_string = bytes_to_hex(byte_array)
        self.assertEqual(hex_string, "010203")

    def test_json_to_user(self):
        json_string = '{"username": "user1", "hpass": "password", "salt": "somesalt"}'
        user = User("user1", "password", "somesalt")
        user_from_json = json_to_user(json_string)
        self.assertEqual(user, user_from_json)

    def test_user_to_json(self):
        user = User("user1", "password", "somesalt")
        json_string = user_to_json(user)
        user_from_json = json_to_user(json_string)
        self.assertEqual(user, user_from_json)

    def test_find_user(self):
        users = [
            User("user1", "pass1", "salt1"),
            User("user2", "pass2", "salt2"),
            User("user3", "pass3", "salt3"),
        ]
        found_user = find_user(users, "user2")
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.username, "user2")
        not_found_user = find_user(users, "user4")
        self.assertIsNone(not_found_user)

    def test_find_user_empty_list(self):
        users = []
        not_found_user = find_user(users, "user1")
        self.assertIsNone(not_found_user)

    def test_save_load_users(self):
        users_to_save = [
            User("user1", "pass1", "salt1"),
            User("user2", "pass2", "salt2"),
            User("user3", "pass3", "salt3"),
        ]
        filepath = "test_users.json"
        save_users(users_to_save, filepath)
        loaded_users = load_users(filepath)
        self.assertEqual(len(users_to_save), len(loaded_users))
        for i in range(len(users_to_save)):
            self.assertEqual(users_to_save[i], loaded_users[i])
        os.remove(filepath)

    def test_load_users_non_existent_file(self):
        loaded_users = load_users("non_existent_file.json")
        self.assertEqual(loaded_users, [])

    def test_load_users_empty_file(self):
        filepath = "empty_file.json"
        with open(filepath, 'w') as f:
            f.write("")
        loaded_users = load_users(filepath)
        self.assertEqual(loaded_users, [])
        os.remove(filepath)

    def test_load_users_corrupted_file(self):
        filepath = "corrupted_file.json"
        with open(filepath, 'w') as f:
            f.write("this is not json")
        loaded_users = load_users(filepath)
        self.assertEqual(loaded_users, [])
        os.remove(filepath)

if __name__ == '__main__':
    unittest.main()
