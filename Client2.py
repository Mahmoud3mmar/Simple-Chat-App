from socket import *
from time import *


server = socket(AF_INET,SOCK_STREAM)
server.bind(('localhost',12000))
server.listen()
print('server is listening at 12000')


connection,address=server.accept()
print('connected to client')
print("Enter Your Name :")
name = str(input());

while True:
    data = input(name+':')
    connection.send(bytes(data + ' ' + ctime(), 'utf-8'))
    print('data sent')
    recData = connection.recv(1024).decode()
    print("Client :", recData)

connection.close()
