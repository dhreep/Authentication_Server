import socket

HOST = "10.50.0.60"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input("Enter a string: ").encode()
        s.sendall(data)
        data = s.recv(256)
        blah = str(data, 'UTF-8')
        print(blah)
