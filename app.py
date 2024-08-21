from flask import Flask, request, jsonify
from integer_set import IntegerSet

app = Flask(__name__)
integer_set = IntegerSet()

@app.route('/add', methods=['POST'])
def add_item():
    data = request.get_json()
    item = data.get('item')
    if item is None or not isinstance(item, int):
        return jsonify({"status": "error", "message": "Invalid input, expected an integer"}), 400

    response, success = integer_set.add_item(item)
    status_code = 201 if success else 400
    return jsonify(response), status_code

@app.route('/has', methods=['GET'])
def has_item():
    item_id = request.args.get('itemId')
    if not item_id:
        return jsonify({"status": "error", "message": "itemId parameter is required"}), 400

    try:
        item_id = int(item_id)  # Convert to integer for comparison
    except ValueError:
        return jsonify({"status": "error", "message": "Invalid itemId, expected an integer"}), 400

    response = integer_set.has_item(item_id)
    status_code = 200 if response["exists"] else 404
    return jsonify(response), status_code

@app.route('/remove', methods=['POST'])
def remove_item():
    data = request.get_json()
    item_id = data.get('itemId')
    if not item_id:
        return jsonify({"status": "error", "message": "itemId is required"}), 400

    try:
        item_id = int(item_id)  # Convert to integer for comparison
    except ValueError:
        return jsonify({"status": "error", "message": "Invalid itemId, expected an integer"}), 400

    response = integer_set.remove_item(item_id)
    status_code = 200 if response["status"] == "success" else 404
    return jsonify(response), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
