# easyRTML/encryption.py
from cryptography.fernet import Fernet
import os
def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    encrypted_file_path = file_path.replace('.json', '.bin')
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.remove(file_path)
    return encrypted_file_path

def decrypt_file(encrypted_file_path, key):
    fernet = Fernet(key)
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet.decrypt(encrypted)
    decrypted_file_path = encrypted_file_path.replace('.bin', '.json')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    return decrypted_file_path
