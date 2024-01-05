import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.71', 55555))
#s.connect(('127.0.0.1', 55555))

message = s.recv(1024)
s.close()

print(message.decode())