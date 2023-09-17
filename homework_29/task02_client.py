import socket
import json

HOST = '127.0.0.1'
PORT = 65439

text_json = {"text": "It was 7 minutes after midnight.", "key": 3}
data = json.dumps(text_json)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Connected to', HOST)
    s.send(data.encode())
    msg = ''
    while True:
        data_in = s.recv(1024)
        msg += data_in.decode()
        if not data_in:
            break
    print("Sent text: ", text_json["text"])
    print("Answer:  ", msg)
