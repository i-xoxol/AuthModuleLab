
import unittest
import json
from api import app, sessions

class TestApi(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        # Clear the sessions after each test
        sessions.clear()

    def test_login_valid_credentials(self):
        # Register a user first
        self.app.post('/register', data=json.dumps({'username': 'testuser', 'password': 'testpassword'}), content_type='application/json')
        # Attempt to login with valid credentials
        response = self.app.post('/login', data=json.dumps({'username': 'testuser', 'password': 'testpassword'}), content_type='application/json')
        data = json.loads(response.data)
        # Assert that the login was successful and a token was returned
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', data)

    def test_login_invalid_credentials(self):
        # Attempt to login with invalid credentials
        response = self.app.post('/login', data=json.dumps({'username': 'wronguser', 'password': 'wrongpassword'}), content_type='application/json')
        # Assert that the login failed
        self.assertEqual(response.status_code, 401)

    def test_profile_valid_token(self):
        # Register and login a user to get a token
        self.app.post('/register', data=json.dumps({'username': 'testuser', 'password': 'testpassword'}), content_type='application/json')
        response = self.app.post('/login', data=json.dumps({'username': 'testuser', 'password': 'testpassword'}), content_type='application/json')
        token = json.loads(response.data)['token']
        # Access the profile endpoint with the token
        response = self.app.get('/profile', headers={'Authorization': token})
        data = json.loads(response.data)
        # Assert that the profile was accessed successfully
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Welcome, testuser!')

    def test_profile_invalid_token(self):
        # Access the profile endpoint with an invalid token
        response = self.app.get('/profile', headers={'Authorization': 'invalidtoken'})
        # Assert that the access was denied
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
