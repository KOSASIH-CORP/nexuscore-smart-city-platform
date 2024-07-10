import hashlib
from cryptography.fernet import Fernet

class SymmetricEncryption:
    def __init__(self, key):
        self.key = key
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher_suite.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data).decode()
