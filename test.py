import unittest
import json
import time
import app
import functions
import ipdb

class teste(unittest.TestCase):

    def test_cityTest(self):
        city_name = "sao-paulo"
        response = self.app.get(f'/temperature/{city_name}')
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data['city.name', str])
        self.assertIsInstance(data['min'], float)
        self.assertIsInstance(data['max'], float)
        self.assertIsInstance(data['avg'], float)
        self.assertIsInstance(data['feels_like'], float)

if __name__ == '__main__':
    unittest.main()
