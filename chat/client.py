import socket
import random
import sys
import time
from threading import Thread
from datetime import datetime
from colorama import init, Fore


init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
          Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
          ]

client_color = random.choice(colors)

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65430
SERVER_SEPERATOR = '<SEP>'

commands = """All available commands:
/list Get all rooms
/create room_name password Create new room
/join room_name password Join to existing room
/rename room_name new_room_name Rename room by administrator
/exit Exit from current room
/close Close program"""

def new_name(connection: socket.socket):
    global name
    while True:
        connection.send(name.encode('utf-8'))
        time.sleep(5)
        server_message = connection.recv(2048).decode('utf-8')
        if server_message:
            break
        else:
            name = input()
        print(f'\n{server_message}')

def listen_server(connection: socket.socket):
    while True:
        server_message = connection.recv(2048).decode('utf-8')
        print(f'\n{server_message}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((SERVER_HOST, SERVER_PORT))

    name = input('Enter your name: ')
    listen = Thread(target=listen_server, args=(server,), daemon=True)
    listen.start()
    listen.join()

    listen = Thread(target=listen_server, args=(server,), daemon=True)
    listen.start()

    while True:
        message = input() #[+]
        print('[+]', message)
        if message.split()[0] in ['/list', '/create', '/join', '/rename', '/rename']:
            server.send(message.encode('utf-8'))
        elif message == '/close':
            server.close()
            time.sleep(3)
            sys.exit()
        else:
            message_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            message_format = f'{client_color}[{message_date}] {name}{SERVER_SEPERATOR}{message}{Fore.RESET}'
            server.send(message_format.encode('utf-8'))
