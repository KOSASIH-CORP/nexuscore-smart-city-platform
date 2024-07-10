import cryptography

class NetworkSecurity:
    def __init__(self, private_key, certificate):
        self.private_key = private_key
        self.certificate = certificate

    def encrypt_data(self, data):
        encrypted_data = cryptography.fernet.encrypt(data, self.private_key)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = cryptography.fernet.decrypt(encrypted_data, self.private_key)
        return decrypted_data
