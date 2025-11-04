import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen()

def ruletka(kolor , numer ,kwota):
    winnumer = random.randint(1 , 10)
    kolor=["red" , "black"]
    winkolor = random.choice(kolor)
    if kolor == winkolor:
        if numer == winnumer:
            kwota = kwota*1000
        else:
            kwota = kwota*2
    else:
        kwota = 0
        
print('Server is listening on port 65432...')
conn, addr = server_socket.accept()
with conn:
    print('Connected by', addr)
    data = conn.recv(1024)
    dane = list(map(int ,data))
    conn.sendall(ruletka(data[0] , int(data[1]) , int(data[2])))
    
