import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65534))
server_socket.listen()

print('Server is listening on port 65432...')
conn, addr = server_socket.accept()
with conn:
    print(info)
    print('Connected by', addr)
    data = conn.recv(1024)
    print(data)
    conn.sendall(data)

