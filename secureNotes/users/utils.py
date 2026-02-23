import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from django.conf import settings


def getAesKey():
    return settings.SECRET_KEY[:32].encode()


def encryptData(plain_text):
    key = getAesKey()
    aesgcm = AESGCM(key)

    nonce = os.urandom(12) 
    ciphertext = aesgcm.encrypt(nonce, plain_text.encode(), None)

    return base64.b64encode(nonce + ciphertext).decode()


def decryptData(encrypted_text):
    key = getAesKey()
    aesgcm = AESGCM(key)

    decoded = base64.b64decode(encrypted_text.encode())
    nonce = decoded[:12]
    ciphertext = decoded[12:]

    decrypted = aesgcm.decrypt(nonce, ciphertext, None)
    return decrypted.decode()