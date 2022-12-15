from Crypto.Cipher import AES

def decrypt(key, ciphertext, tag, nonce ):
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data