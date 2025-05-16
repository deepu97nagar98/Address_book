from flask import Blueprint, request, jsonify
from services import AddressBookService

book = Blueprint('book', __name__)
service = AddressBookService()

@book.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    result = service.create_contacts(data)
    return jsonify([c.__dict__ for c in result])

@book.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    result = service.update_contacts(data)
    return jsonify([c.__dict__ for c in result])

@book.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    count = service.delete_contacts(data)
    return jsonify({"deleted": count})

@book.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    result = service.search_contacts(data['query'])
    return jsonify([c.__dict__ for c in result])
