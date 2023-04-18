import socket

from typing import Final


HOST: Final = "127.0.0.1" # localhost
PORT: Final = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()

  with conn:
    print(f'Connetcted by {addr}')
    while True:
      data = conn.recv(1024)
      if not data:
        break
      conn.sendall(data)
