import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 65534))




color = int(input("dawaj color ziomek"))
liczba = int(input("liczba od 0 do 64"))
hajs = int(input("ile betujesz ?(do 1024)"))


info = color.to_bytes(1,"big") + liczba.to_bytes(5,"big") + hajs.to_bytes(10,"big")

client_socket.send(info)



data = client_socket.recv(1024)
print('Received', repr(data))
client_socket.close()

