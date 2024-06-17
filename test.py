import unittest
from app import app

class TestApp(unittest.TestCase):


    def setUp(self):
        self.app = app.test_client()


    def test_1(self):
        response = self.app.post('/', data={'grad': "100", 'precision': '2', 'units': 'degrees'})
        self.assertEqual(response.status_code, 200)


    def test_2(self):
        response = self.app.post('/', data={'grad': None, 'precision': None, 'units': ''})
        self.assertEqual(response.status_code, 400)


    def test_3(self):
        response = self.app.post('/', data={'grad': None, 'precision': '2', 'units': 'degrees'})
        self.assertEqual(response.status_code, 400)


    def test_4(self):
        response = self.app.post('/', data={'grad': '100', 'precision': None, 'units': 'degrees'})
        self.assertEqual(response.status_code, 400)


    def test_5(self):
        response = self.app.post('/', data={'grad': '100', 'precision': '2', 'units': None})
        self.assertEqual(response.status_code, 400)


    def test_6(self):
        response = self.app.post('/', data={'grad': None, 'precision': None, 'units': None})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()