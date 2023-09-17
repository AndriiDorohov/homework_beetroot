#!/usr/bin/env python3 client
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        message = input('Enter message (or "exit" to quit): ')
        if message == 'exit':
            break
        message = message.encode('utf-8')
        addr = (HOST, PORT)

        s.sendto(message, addr)
        try:
            data, server = s.recvfrom(1024)
            print(f'ECHO: {data.decode("utf-8")}')
        except socket.timeout:
            print('REQUEST TIMED OUT')
