import socket
sock = socket.socket()
ip = input("server ip: ")
sock.connect((ip, 8000))
print("you have connected to server sucessfully")
namey = input("what should others call you: ")
sock.send((namey).encode())
while True:
    m = sock.recv(1024).decode()
    print(m)
    me = input("you: ")
    sock.send((namey + ": " + me).encode())