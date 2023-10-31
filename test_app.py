import os
import unittest
from app import app

class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_hello_world_default(self):
        os.environ = {}
        response = self.app.get('/')
        data = response.data.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, 'Hello, World!')

    def test_hello_world_custom_name(self):
        os.environ['NAME'] = 'Alice'
        response = self.app.get('/')
        data = response.data.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, 'Hello, Alice!')

if __name__ == '__main__':
    unittest.main()
