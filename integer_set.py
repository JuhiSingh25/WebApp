# integer_set.py

class IntegerSet:
    def __init__(self):
        self.data = [] 

    def add_item(self, item):
        if item not in self.data:  
            self.data.append(item)
            return True 
        return False

    def remove_item(self, item):
        if item in self.data:
            self.data.remove(item)
            return True
        return False

    def has_item(self, item):
        return item in self.data
