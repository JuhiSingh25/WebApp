import unittest
from app import app
from app import app, integer_set 

class TestIntegerSetAPI(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def tearDown(self):
        # Reset the integer_set after each test
        integer_set.items_store.clear()

    def test_add_item_success(self):
        response = self.client.post('/add', json={'item': 1})
        print(f"Response data: {response.json}")  # Print the response body for debugging
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"status": "success", "itemId": 1, "message": "Item added successfully"})

    def test_add_item_duplicate(self):
        self.client.post('/add', json={'item': 1})
        response = self.client.post('/add', json={'item': 1})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"status": "error", "message": "Item already exists"})

    def test_add_item_invalid(self):
        response = self.client.post('/add', json={'item': "not an integer"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"status": "error", "message": "Invalid input, expected an integer"})

    def test_has_item_exists(self):
        self.client.post('/add', json={'item': 1})
        response = self.client.get('/has', query_string={'itemId': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "success", "exists": True})

    def test_has_item_not_exists(self):
        response = self.client.get('/has', query_string={'itemId': 2})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"status": "error", "exists": False})

    def test_has_item_invalid(self):
        response = self.client.get('/has', query_string={'itemId': 'not an integer'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"status": "error", "message": "Invalid itemId, expected an integer"})

    def test_remove_item_success(self):
        self.client.post('/add', json={'item': 1})
        response = self.client.post('/remove', json={'itemId': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "success", "message": "Item removed successfully"})

    def test_remove_item_not_exists(self):
        response = self.client.post('/remove', json={'itemId': 2})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"status": "error", "message": "Item not found"})

    def test_remove_item_invalid(self):
        response = self.client.post('/remove', json={'itemId': 'not an integer'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"status": "error", "message": "Invalid itemId, expected an integer"})

if __name__ == '__main__':
    unittest.main()
