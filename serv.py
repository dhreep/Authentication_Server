# Python Program to Get IP Address
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Server IP Address is:" + IPAddr)
port = 65432
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((IPAddr,port))
    s.listen(5)
    conn,addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        i=0
        while True:
            
            data = conn.recv(256)
            blah = str(data, 'UTF-8')
            print(blah)            
            if not data:
                break            
            print(i)
            i+=1
            data = input("Enter a string: ").encode()
            conn.sendall(data)

