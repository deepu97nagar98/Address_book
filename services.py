from models import Contact
from storage import InMemoryStorage

class AddressBookService:
    def __init__(self):
        self.db = InMemoryStorage()

    def create_contacts(self, contact_data):
        contacts = [Contact(**c) for c in contact_data]
        return self.db.create(contacts)

    def update_contacts(self, update_data):
        return self.db.update(update_data)

    def delete_contacts(self, ids):
        return self.db.delete(ids)

    def search_contacts(self, query):
        return self.db.search(query)
