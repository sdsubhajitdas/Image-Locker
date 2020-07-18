import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def readSalt():
    """Reads the user generated salt file"""
    salt = ""
    with open("salt","r") as file:
        salt = file.readline()
    
    return str.encode(salt)



def getPasswordGeneratedKey(password):
    """Uses user given password to generate key for encryption"""
    password = str.encode(password)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=readSalt(),
        iterations=100000,
        backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key
