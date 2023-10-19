import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet,InvalidToken

def getKey()->bytes:
    password_provided = "password"  # This is input in the form of a string
    password = password_provided.encode()  # Convert to type bytes
    salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    return key

def encryptToStore(key,plaintext:str)->str:
    result = ""
    for char in plaintext:
        ascii_value = ord(char)
        incremented_ascii_value = ascii_value + 3
        incremented_char = chr(incremented_ascii_value)
        result += incremented_char
    return result

def decryptFromStore(key,enctext:str)->str:
    result = ""
    if type(enctext) == int:
        return str(enctext)
    for char in enctext:
        ascii_value = ord(char)
        incremented_ascii_value = ascii_value - 3
        incremented_char = chr(incremented_ascii_value)
        result += incremented_char
    return result


# def main():
#     plaintext = "My name is Dhruv".encode()
#     key = getKey()
#     enctxt = encryptToStore(key=key,plaintext=plaintext)
#     print(enctxt.decode())
#     print(decryptFromStore(key=key,enctext=enctxt).decode())
#     print("END")

# if __name__ == "__main__":
#     main()