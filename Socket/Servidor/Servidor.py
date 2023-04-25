import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',58310))
print('Aguardando conexao')
server.listen(1)

connection, address = server.accept()
print('conectado em: ', address)

namefile=connection.recv(1024).decode()

with open(namefile, 'rb') as file:
    for data in file.readlines():
        connection.sendall(data)

    print('Arquivo enviado')
