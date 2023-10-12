import socket

HOST = "10.52.1.147"  # The server's hostname or IP address
PORT = 10201  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(2048)
        blah = str(data, 'UTF-8')
        print(f"{blah}")
        if blah=="You are connected" or blah == "Closing Connection":
            s.close()
            exit(0)   
        elif blah == "Wrong choice." or blah=="Username already exists.":
            continue      
        data = input().encode()
        s.sendall(data)