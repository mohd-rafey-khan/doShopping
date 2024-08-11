from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64
from loguru import logger
import json


class AESCipher:
    def __init__(self):
        self.key = b'\x9f9\x90@\xd8\xf1\xe7j\x0f\xff\xdb\xb3\x8b]\x89I'

    def encrypt(self, data):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(b'\0' * 16), backend=default_backend())
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()

        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')

        return encrypted_data_base64

    def decrypt(self, encrypted_data):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(b'\0' * 16), backend=default_backend())
        decryptor = cipher.decryptor()

        encrypted_data_bytes = base64.b64decode(encrypted_data.encode('utf-8'))

        decrypted_data = decryptor.update(encrypted_data_bytes) + decryptor.finalize()

        decrypted_data_hex = decrypted_data.hex()

        unpadder = padding.PKCS7(128).unpadder()
        original_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return original_data




