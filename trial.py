from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

key = b'0000000000000101'
print(key)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
nonce = cipher.nonce
print(ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce)
d = cipher.decrypt_and_verify(ciphertext, tag)
print(d)