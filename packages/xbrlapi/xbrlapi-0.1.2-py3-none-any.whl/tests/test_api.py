# tests/test_api.py
import unittest
from xbrlapi.api import set_api_key, get_data

class TestXbrlApi(unittest.TestCase):

    def setUp(self):
        set_api_key("your_test_api_key")

    def test_get_data(self):
        # Replace with appropriate test values
        data = get_data("NATIONAL INSTRUMENTS CORP", "2022-12-31", "InventoryNet")
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
