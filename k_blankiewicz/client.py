import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("10.3.101.65", 65432))


client_socket.sendall(b'Hello, world')
data = client_socket.recv(1024)
print('Received', repr(data))
client_socket.close()

