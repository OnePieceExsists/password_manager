import unittest
from password_generator import PasswordGenerator
import string

class TestPasswordGenerator(unittest.TestCase):

    def test_default_length(self):
        gen = PasswordGenerator()
        pwd = gen.generate()
        self.assertEqual(len(pwd), 12)

    def test_custom_length(self):
        gen = PasswordGenerator(length=20)
        pwd = gen.generate()
        self.assertEqual(len(pwd), 20)

    def test_allowed_characters(self):
        gen = PasswordGenerator()
        pwd = gen.generate()
        allowed_chars = string.ascii_letters + string.digits + string.punctuation
        for c in pwd:
            self.assertIn(c, allowed_chars)

    def test_only_letters(self):
        gen = PasswordGenerator(use_digits=False, use_symbols=False)
        pwd = gen.generate()
        for c in pwd:
            self.assertIn(c, string.ascii_letters)

if __name__ == '__main__':
    unittest.main()
