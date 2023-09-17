#!/usr/bin/env python3 server.py
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        message, address = s.recvfrom(1024)
        if message.decode('utf-8') == 'exit':
            break
        s.sendto(message, address)
