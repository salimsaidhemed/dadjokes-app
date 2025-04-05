import unittest
from app import create_app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def test_joke_endpoint(self):
        response = self.app.get('/api/joke')
        self.assertEqual(response.status_code, 200)
        self.assertIn('joke', response.get_json())

if __name__ == "__main__":
    unittest.main()
