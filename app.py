# app.py

from flask import Flask, request, jsonify
from integer_set import IntegerSet

app = Flask(__name__)
integer_set = IntegerSet()

@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    item = data.get('item')
    if integer_set.add_item(item):
        return jsonify({"message": "Item added successfully"}), 201
    return jsonify({"message": "Item already exists"}), 200

@app.route('/remove', methods=['POST'])
def remove_item():
    data = request.get_json()
    item = data.get('item')
    if integer_set.remove_item(item):
        return jsonify({"message": "Item removed successfully"}), 200
    return jsonify({"message": "Item not found"}), 404

@app.route('/has', methods=['GET'])
def has_item():
    item = int(request.args.get('item'))
    if integer_set.has_item(item):
        return jsonify({"message": "Item exists"}), 200
    return jsonify({"message": "Item does not exist"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
