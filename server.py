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






# Локальный хост - используется для установления IP соединения.
# AF_INET - используется для связи испольузя IP(есть и другие средства связи).
# SOCK_STREAM - транспортный протокол типа TPC
# SOCK_DGRAM - транспортнйы проток типа UDP 
# decode - преобразования байтовых выражений в строку
# encode - преобразование строковых(или других типов данных) в байты