from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce
    return ciphertext, tag, nonce