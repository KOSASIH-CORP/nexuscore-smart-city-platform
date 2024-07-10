import numpy as np
from pyfhel import PyFHELEncrypt

class HomomorphicEncryption:
    def __init__(self, context):
        self.context = context
        self.encryptor = PyFHELEncrypt(self.context)

    def encrypt(self, plaintext):
        ciphertext = self.encryptor.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = self.encryptor.decrypt(ciphertext)
        return plaintext

    def evaluate(self, ciphertext1, ciphertext2):
        result = self.encryptor.evaluate_add(ciphertext1, ciphertext2)
        return result
