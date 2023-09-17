import socket
import json

HOST = '127.0.0.1'
PORT = 65439

def caesar_cipher_encrypt(plaintext, key):
   ciphertext = ""
   for c in plaintext:
      if c.isalpha():
         ascii_code = ord(c)
         if c.isupper():
            ascii_code = (ascii_code - ord('A') + key) % 26 + ord('A')
         else:
            ascii_code = (ascii_code - ord('a') + key) % 26 + ord('a')
         ciphertext += chr(ascii_code)
      else:
         ciphertext += c
   return ciphertext

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('I am listening you connection')
    while True:
        conn, addr = s.accept()
        print('Connected -', addr)
        data = conn.recv(1024)
        if not data:
            break
        received_data = json.loads(data.decode('utf-8'))
        plaintext = received_data.get('text')
        key = received_data.get('key')
        text_answer = caesar_cipher_encrypt(plaintext, key)
        conn.send(text_answer.encode())
        print("I've finished")
        break
