import unittest
import os
import json
from password_manager import PasswordManager

class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_storage.json'
        self.pm = PasswordManager(filename=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_entry_and_save(self):
        self.pm.add_entry('example.com', 'user1', 'pass123', 'desc')
        self.assertEqual(len(self.pm.passwords), 1)

        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data[0]['website'], 'example.com')

    def test_load_existing(self):
        # Simulate existing data
        data = [{"website": "loaded.com", "username": "loaded_user", "password": "loaded_pwd"}]
        with open(self.test_file, 'w') as f:
            json.dump(data, f)

        new_pm = PasswordManager(filename=self.test_file)
        self.assertEqual(len(new_pm.passwords), 1)
        self.assertEqual(new_pm.passwords[0]['website'], 'loaded.com')

if __name__ == '__main__':
    unittest.main()
