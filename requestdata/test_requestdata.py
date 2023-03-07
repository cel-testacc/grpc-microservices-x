import unittest
import json
from urllib.request import urlopen

class TestRequestData(unittest.TestCase):
    def test_render_json(self):
        homepage_json = json.load(urlopen("http://127.0.0.1:5000/getECData"))
        checkrow = ['2019-01-31 22:45:00', '61.3']
        self.assertIn(checkrow, homepage_json)

if __name__ == '__main__':
    unittest.main()