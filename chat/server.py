import os
import socket
from threading import Thread

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432
SERVER_SEPERATOR = "<SEP>"

client_socket = set()
client_database = {}  # {connection: 'new_room'}
rooms = {}  # {name: password}
room_admin = {}  # {connection: 'new_room'}


def listen_commands():
    while True:
        message = input()
        if message == "exit":
            for client in client_socket:
                client.close()
            break
        elif message == "rooms":
            print([])
        else:
            print("Command not found")
    os._exit(1)


def listen_client(connection: socket.socket):
    while True:
        try:
            message = connection.recv(2048).decode("utf-8")
            print("enter", message)
            if message.startswith("/"):
                if len(message.split()) == 3:
                    command, first, second = tuple(message.split())
                else:
                    command, first, second = message, None, None
            else:
                command, first, second = message, None, None
        except Exception as error:
            print(f"[!] Error {error}")
            connection.close()
            client_socket.remove(connection)
            break
        match command:
            case "/list":
                connection.send(str(rooms.keys()).encode("utf-8"))
            case "/create":
                rooms[first] = second
                client_database[connection] = first
                room_admin[connection] = first
                connection.send(f"Reconnect to {first}".encode("utf-8"))
            case "/join":
                if rooms.get(first) == second:
                    client_database[connection] = first
                    connection.send(f"Reconnect to {first}".encode("utf-8"))
                else:
                    connection.send("Wrong name or password".encode("utf-8"))
            case "/rename":
                if room_admin.get(connection) == first:
                    rooms[second] = rooms[first]
                    del rooms[first]
                    for client, room in client_database.items():
                        if room == first:
                            client_database[client] = second
                    connection.send(
                        f"Room {first} was renamed to {second}".encode("utf-8")
                    )
                else:
                    connection.send("You are not admin of this room".encode("utf-8"))
            case "/exit":
                current_room = client_database[connection]
                client_database[connection] = "default"
                connection.send(f"Logout from {current_room}".encode("utf-8"))
            case command.startswith("/check"):
                pass
            case _:
                room_client = dict(
                    filter(
                        lambda x: client_database[connection] == x[1],
                        client_database.items(),
                    )
                )
                message = message.replace(SERVER_SEPERATOR, ": ")
                for client in room_client:
                    if client != connection:
                        client.send(message.encode("utf-8"))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_:
    socket_.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_.bind((SERVER_HOST, SERVER_PORT))
    socket_.listen(5)

    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    administrator = Thread(target=listen_commands)
    administrator.start()

    while True:
        connection, address = socket_.accept()
        print(f"[+] Client {address} connected")
        client_socket.add(connection)
        client_database[connection] = "default"

        client = Thread(target=listen_client, args=(connection,), daemon=True)
        client.start()
