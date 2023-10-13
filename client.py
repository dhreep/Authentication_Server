import socket

HOST = "10.52.4.14"  # The server's hostname or IP address
PORT = 10200 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(2048)
        blah = str(data, 'UTF-8')
        print(f"{blah}")
        if blah == "Closing Connection":
            s.close()
            exit(0)   
        elif blah == "Wrong choice." or blah=="Username already exists.":
            continue      
        elif blah=="You are connected":
            auth_key = s.recv(256)
            blah = str(data, 'UTF-8')
            s.close()
            break
        data = input().encode()
        s.sendall(data)
    #key has been received
    print(auth_key)