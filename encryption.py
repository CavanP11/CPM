from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Derive a key from the master password and salt
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,  # 32 bytes for AES-256
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())  # Return raw bytes

# Encrypt data using the derived key
def encrypt_data(data, key):
    iv = os.urandom(16)  # AES requires a 16-byte initialization vector (IV)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
    return base64.urlsafe_b64encode(iv + ciphertext)  # Combine IV and ciphertext

# Decrypt data using the derived key
def decrypt_data(encrypted_data, key):
    encrypted_data = base64.urlsafe_b64decode(encrypted_data)
    iv = encrypted_data[:16]  # Extract IV
    ciphertext = encrypted_data[16:]  # Extract ciphertext
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode()
