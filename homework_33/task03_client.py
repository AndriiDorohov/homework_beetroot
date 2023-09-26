import socket


def main():
    host = "127.0.0.1"
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = input("Input message (or 'exit'): ")
        if message.lower() == "exit":
            break

        client.send(message.encode())
        data = client.recv(1024)
        print("Server answer" + data.decode())

    client.close()


if __name__ == "__main__":
    main()
