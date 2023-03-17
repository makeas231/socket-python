import socket
from typing import Final



HOST: Final = "127.0.0.1" # Hostname сервера или IP сервера
PORT: Final = 8000 # Порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(b'Hello world')
  data = s.recv(1024) # прочитать ответ сервера

print(f'Received {data}')
        