from typing import Dict
from models import Contact

class InMemoryStorage:
    def __init__(self):
        self.contacts: Dict[str, Contact] = {}

    def create(self, contacts):
        for contact in contacts:
            self.contacts[contact.id] = contact
        return contacts

    def update(self, updates):
        updated = []
        for item in updates:
            contact = self.contacts.get(item["id"])
            if contact:
                contact.name = item.get("name", contact.name)
                contact.phone = item.get("phone", contact.phone)
                contact.email = item.get("email", contact.email)
                updated.append(contact)
        return updated

    def delete(self, ids):
        count = 0
        for cid in ids:
            if cid in self.contacts:
                del self.contacts[cid]
                count += 1
        return count

    def search(self, query):
        return [c for c in self.contacts.values() if query.lower() in c.name.lower()]
