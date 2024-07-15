import os
import zlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b85encode, b85decode

def generate_key(password):
    return password.encode()[:32].ljust(32, b'\0')

def encrypt_data(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return iv + encryptor.update(data) + encryptor.finalize()

def decrypt_data(data, key):
    iv, ciphertext = data[:16], data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def adaptive_compress(data):
    compressed = zlib.compress(data)
    return compressed

def adaptive_decompress(data):
    try:
        return zlib.decompress(data)
    except zlib.error:
        try:
            decoded = b85decode(data)
            return zlib.decompress(decoded)
        except:
            return data

def encode(data, key):
    encoded_data = encrypt_data(data.encode('utf-8'), generate_key(key))
    return adaptive_compress(encoded_data)

def decode(data, key):
    decompressed_data = adaptive_decompress(data)
    return decrypt_data(decompressed_data, generate_key(key)).decode('utf-8')

if __name__ == "__main__":
    print("This module provides functions for encrypting (encode) and decrypting (decode) data.")
    print("Please use this module as an import in another script.")
