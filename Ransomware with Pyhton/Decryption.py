import os
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

files = os.listdir()
def decryption():
    for file in files:
        if file.endswith(".txt"):
            f = open(file,"rb")
            encrypted = f.read()
            f = open(file,"wb")
            decrypted_txt = decrypt(encrypted)
            f.write(decrypted_txt)

def decrypt(encrypted):
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
        decrypted = private_key.decrypt(
        base64.b64decode(encrypted),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted

decryption()