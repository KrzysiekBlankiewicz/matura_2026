import socket
import random

def casino(color, number, bet):
    win_num = random.randint(1,36)
    win_col = random.randint(0,1)
    if color==win_col and number==win_num:
        return bet*1000
    elif color==win_col:
        return bet*10
    elif number==win_num:
        return bet*100
    else:
        return 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 6767))
server_socket.listen()

print('Server is listening on port 6767...')
conn, addr = server_socket.accept()
with conn:
    print('Connected by', addr)
    data = conn.recv(1024).decode().strip()
    parts = data.split()
    color = int(parts[0])
    number = int(parts[1])
    bet = int(parts[2])
    result = casino(color, number, bet)
    conn.sendall(str(result).encode())
