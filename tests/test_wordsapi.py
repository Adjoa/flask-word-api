import unittest
import os
import json
from app import create_app

class WordsAPITestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        
    def test_wordsapi_creation(self):
        res = self.client().get('/words')
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main() 