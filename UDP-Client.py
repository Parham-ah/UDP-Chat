import socket

IP = '127.0.0.1'
PORT = 35461

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    while True:
        message = input('Enter your message : ')
        s.sendto(message.encode(), (IP, PORT))
        data, server_add = s.recvfrom(1024)
        print(f"Recived message from server : {data.decode('utf-8')}")