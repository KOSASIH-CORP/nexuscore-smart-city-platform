import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_key_pair():
    # Generate RSA key pair
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = key.public_key().public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
    )
    return private_key, public_key

def asymmetric_encrypt(data, public_key):
    # Encrypt data using public key
    encrypted_data = cryptography.fernet.encrypt(data, public_key)
    return encrypted_data

def asymmetric_decrypt(encrypted_data, private_key):
    # Decrypt data using private key
    decrypted_data = cryptography.fernet.decrypt(encrypted_data, private_key)
    return decrypted_data
