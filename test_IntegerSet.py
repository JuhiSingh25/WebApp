import unittest
from integer_set import IntegerSet

class TestIntegerSet(unittest.TestCase):

    def setUp(self):
        self.integer_set = IntegerSet()

    def test_add_item(self):
        response, success = self.integer_set.add_item(1)
        self.assertTrue(success)
        self.assertEqual(response, {"status": "success", "itemId": 1, "message": "Item added successfully"})

        response, success = self.integer_set.add_item(1)
        self.assertFalse(success)
        self.assertEqual(response, {"status": "error", "message": "Item already exists"})

    def test_has_item(self):
        self.integer_set.add_item(1)
        response = self.integer_set.has_item(1)
        self.assertEqual(response, {"status": "success", "exists": True})

        response = self.integer_set.has_item(2)
        self.assertEqual(response, {"status": "error", "exists": False})

    def test_remove_item(self):
        self.integer_set.add_item(1)
        response = self.integer_set.remove_item(1)
        self.assertEqual(response, {"status": "success", "message": "Item removed successfully"})

        response = self.integer_set.remove_item(1)
        self.assertEqual(response, {"status": "error", "message": "Item not found"})

if __name__ == '__main__':
    unittest.main()
