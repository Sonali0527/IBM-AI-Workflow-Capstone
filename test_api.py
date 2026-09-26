import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_predict_specific_country(self):
        res = self.client.post('/predict', json={"country":"United Kingdom", "date":"2019-08-01"})
        self.assertEqual(res.status_code, 200)
        self.assertIn('predicted_revenue', res.get_json())

    def test_predict_all_countries(self):
        res = self.client.post('/predict', json={"country":"all", "date":"2019-08-01"})
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
