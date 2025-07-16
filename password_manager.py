import json
import os

class PasswordManager:
    def __init__(self, filename='storage.json'):
        self.filename = filename
        self.passwords = self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.passwords, f, indent=4)

    def add_entry(self, website, username, password, description=""):
        entry = {
            "website": website,
            "username": username,
            "password": password,
            "description": description
        }
        self.passwords.append(entry)
        self.save()
