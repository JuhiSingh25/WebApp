import unittest
from integer_set import IntegerSet
from app import app

class TestIntegerSet(unittest.TestCase):

    def test_add_item(self):
        s = IntegerSet()
        self.assertTrue(s.add_item(1))
        self.assertFalse(s.add_item(1))
    
    def test_remove_item(self):
        s = IntegerSet()
        s.add_item(1)
        self.assertTrue(s.remove_item(1))
        self.assertFalse(s.remove_item(1))
    
    def test_has_item(self):
        s = IntegerSet()
        s.add_item(1)
        self.assertTrue(s.has_item(1))
        self.assertFalse(s.has_item(2))

class TestFlaskAPI(unittest.TestCase):
    
    def setUp(self):
        # Creates a test client for the Flask application
        self.app = app.test_client()
        self.app.testing = True
    
    def test_add_item(self):
        response = self.app.post('/add', json={"item": 1})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"message": "Item added successfully"})
        
        response = self.app.post('/add', json={"item": 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Item already exists"})
    
    def test_remove_item(self):
        self.app.post('/add', json={"item": 1})
        
        response = self.app.post('/remove', json={"item": 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Item removed successfully"})
        
        response = self.app.post('/remove', json={"item": 2})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"message": "Item not found"})
    
    def test_has_item(self):
        self.app.post('/add', json={"item": 1})
        
        response = self.app.get('/has?item=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Item exists"})
        
        response = self.app.get('/has?item=2')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"message": "Item does not exist"})

if __name__ == '__main__':
    unittest.main()
