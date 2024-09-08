import socket

IP ='127.0.0.1'
PORT = 35461

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.bind((IP, PORT))
    print(f'Server is listening to {IP}:{PORT}')
    
    while True:
        data, client_add = s.recvfrom(1024)
        print(f'Recived message from {client_add} is {data.decode("utf-8")}')
        message = input('Enter your message : ')
        s.sendto(message.encode(), client_add)