# Python Program to Get IP Address
import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from diffiehellman import DiffieHellman
# add encryption
# add all code to main
# add database instead of dictionary
# add passing of authentication key
# add concurrency
# handle keyboard interrupt 
import uuid
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# print("Your Computer Name is:" + hostname)
# print("Server IP Address is:" + IPAddr)

def aes_encrypt(data,key)->bytes:
    cipher = AES.new(key, AES.MODE_GCM)
    # Encrypt the message
    ciphertext, tag = cipher.encrypt_and_digest(data)
    # Send the encrypted message
    encrypted_data = cipher.nonce + ciphertext + tag
    return encrypted_data

def aes_decrypt(encrypted_data,key)->bytes:
    nonce = encrypted_data[:16]  # Assuming a 128-bit nonce
    ciphertext = encrypted_data[16:-16]
    tag = encrypted_data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # Decrypt the message
    decrypted_data = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)  # Verifies the authentication tag
        # print("Decryption successful")
        return decrypted_data    
    except ValueError:
        print("Authentication failed. The data may be tampered.")
        exit(0)

userdict={ "user1":"one", "user2":"two" , "user3":"three" }
IPAddr="10.52.4.14"
port = 10200
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((IPAddr,port))
    s.listen(5)
    conn,addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        i=0
         # Key generation and encryption setup:
        key_pair = DiffieHellman(group=14, key_bits=32) # automatically generate one key pair              
        # generate shared key based on the other side's public key
        client_public = conn.recv(1024)
        server_shared_key = key_pair.generate_shared_key(client_public) 
        # get own public key and send to server
        server_public = key_pair.get_public_key() 
        conn.sendall(server_public) 

        # Use a KDF to derive an AES key from the shared key
        password = server_shared_key
        salt = b'salt'  # You should use a different salt
        key = PBKDF2(password, salt, dkLen=32, count=1000000)       
        
        while True:
            conn.sendall(aes_encrypt(data=b"Enter your username",key=key))
            data = aes_decrypt(encrypted_data=conn.recv(256), key=key)
            username = str(data, 'UTF-8')
            if username in userdict:
                while(True):
                    conn.sendall(aes_encrypt(data=b"Enter your password",key=key))
                    data = aes_decrypt(encrypted_data=conn.recv(256), key=key)
                    pwd = str(data, 'UTF-8')
                    # print("Recieved Passwd",key=key))
                    if userdict[username]==pwd:
                        # print(f"sending Passwd: {pwd}",key=key))
                        conn.sendall(aes_encrypt(data=b"You are connected",key=key))
                        # print("Passwd sent",key=key))
                        unique_id=uuid.uuid4()
                        auth_key=str(unique_id).encode()
                        # add authentication key to the database
                        conn.sendall(aes_encrypt(data=auth_key,key=key))
                        conn.close() 
                        exit(0)
                    else:
                        conn.sendall(aes_encrypt(data=b"Wrong Password Enter password again?(Y/N): ",key=key))
                        choice = aes_decrypt(encrypted_data=conn.recv(256), key=key)
                        choice = str(choice, 'UTF-8')
                        if(choice=="N" or choice=="n"):
                            conn.sendall(aes_encrypt(data=b"Closing Connection",key=key))
                            conn.close()
                            exit(0)
                        elif(choice=="Y" or choice=="y"):
                            continue 
                        else:
                            conn.sendall(aes_encrypt(data=b"Wrong choice.",key=key)) 
                            continue                                   
            else:
                conn.sendall(aes_encrypt(data=b"A) Register \nB) Re-enter username \nC) Exit \nEnter choice: ",key=key))
                choice = aes_decrypt(encrypted_data=conn.recv(256), key=key)
                choice = str(choice, 'UTF-8')
                if(choice=="C" or choice=="c"):
                    conn.sendall(aes_encrypt(data=b"Closing Connection",key=key))
                    conn.close()
                    exit(0)
                elif(choice=="B" or choice=="b"):
                    continue
                elif(choice=="A" or choice=="a"):
                    while(True):
                        conn.sendall(aes_encrypt(data=b"Enter new username: ",key=key))
                        reg_username = aes_decrypt(encrypted_data=conn.recv(256), key=key)
                        reg_username = str(reg_username, 'UTF-8')
                        if(reg_username in userdict):
                            conn.sendall(aes_encrypt(data=b"Username already exists.",key=key))
                            continue
                        conn.sendall(aes_encrypt(data=b"Enter new password: ",key=key))
                        reg_pwd = aes_decrypt(encrypted_data=conn.recv(256), key=key)
                        reg_pwd = str(reg_pwd, 'UTF-8')
                        userdict[reg_username]=reg_pwd
                        conn.sendall(aes_encrypt(data=b"Successfully Registered! Login?(Y/N):",key=key))
                        choice = aes_decrypt(encrypted_data=conn.recv(256), key=key)
                        choice = str(choice, 'UTF-8')
                        if(choice=="N" or choice=="n"):
                            conn.sendall(aes_encrypt(data=b"Closing Connection",key=key))
                            conn.close()
                            exit(0)
                        elif(choice=="Y" or choice=="y"):
                            break
                        else:
                            conn.sendall(aes_encrypt(data=b"Wrong choice.",key=key)) 
                            break  
                else:
                    conn.sendall(aes_encrypt(data=b"Wrong choice.",key=key))
                    continue
                
