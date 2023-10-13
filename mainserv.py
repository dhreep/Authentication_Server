# Python Program to Get IP Address

# add encryption
# add database instead of dictionary
# add passing of authentication key
# add concurrency
# handle keyboard interrupt 
import uuid
import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# print("Your Computer Name is:" + hostname)
# print("Server IP Address is:" + IPAddr)

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
        while True:
            conn.sendall(b"Enter your username")
            data = conn.recv(256)
            username = str(data, 'UTF-8')
            if username in userdict:
                while(True):
                    conn.sendall(b"Enter your password")
                    data = conn.recv(256)
                    pwd = str(data, 'UTF-8')
                    # print("Recieved Passwd")
                    if userdict[username]==pwd:
                        # print(f"sending Passwd: {pwd}")
                        conn.sendall(b"You are connected")
                        # print("Passwd sent")
                        unique_id=uuid.uuid4()
                        auth_key=str(unique_id).encode()
                        # add authentication key to the database
                        conn.sendall(auth_key)
                        conn.close() 
                        exit(0)
                    else:
                        conn.sendall(b"Wrong Password Enter password again?(Y/N): ")
                        choice = conn.recv(256)
                        choice = str(choice, 'UTF-8')
                        if(choice=="N" or choice=="n"):
                            conn.sendall(b"Closing Connection")
                            conn.close()
                            exit(0)
                        elif(choice=="Y" or choice=="y"):
                            continue 
                        else:
                            conn.sendall(b"Wrong choice.") 
                            continue                                   
            else:
                conn.sendall(b"A) Register \nB) Re-enter username \nC) Exit \nEnter choice: ")
                choice = conn.recv(256)
                choice = str(choice, 'UTF-8')
                if(choice=="C" or choice=="c"):
                    conn.sendall(b"Closing Connection")
                    conn.close()
                    exit(0)
                elif(choice=="B" or choice=="b"):
                    continue
                elif(choice=="A" or choice=="a"):
                    while(True):
                        conn.sendall(b"Enter new username: ")
                        reg_username = conn.recv(256)
                        reg_username = str(reg_username, 'UTF-8')
                        if(reg_username in userdict):
                            conn.sendall(b"Username already exists.")
                            continue
                        conn.sendall(b"Enter new password: ")
                        reg_pwd = conn.recv(256)
                        reg_pwd = str(reg_pwd, 'UTF-8')
                        userdict[reg_username]=reg_pwd
                        conn.sendall(b"Successfully Registered! Login?(Y/N):")
                        choice = conn.recv(256)
                        choice = str(choice, 'UTF-8')
                        if(choice=="N" or choice=="n"):
                            conn.sendall(b"Closing Connection")
                            conn.close()
                            exit(0)
                        elif(choice=="Y" or choice=="y"):
                            break
                        else:
                            conn.sendall(b"Wrong choice.") 
                            break  
                else:
                    conn.sendall(b"Wrong choice.")
                    continue
                
