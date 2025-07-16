import string
import secrets

class PasswordGenerator:
    def __init__(self, length=12, use_digits=True, use_symbols=True):
        self.length = length
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def generate(self):
        chars = string.ascii_letters
        if self.use_digits:
            chars += string.digits
        if self.use_symbols:
            chars += string.punctuation
        return ''.join(secrets.choice(chars) for _ in range(self.length))
