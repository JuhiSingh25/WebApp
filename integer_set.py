class IntegerSet:
    def __init__(self):
        self.items_store = set()

    def add_item(self, item):
        if item in self.items_store:
            return {"status": "error", "message": "Item already exists"}, False
        self.items_store.add(item)
        return {"status": "success", "itemId": item, "message": "Item added successfully"}, True

    def has_item(self, item_id):
        if item_id in self.items_store:
            return {"status": "success", "exists": True}
        return {"status": "error", "exists": False}

    def remove_item(self, item_id):
        if item_id in self.items_store:
            self.items_store.remove(item_id)
            return {"status": "success", "message": "Item removed successfully"}
        else:
            return {"status": "error", "message": "Item not found"}
