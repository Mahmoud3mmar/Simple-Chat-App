from socket import *
client=socket()
client.connect(('localhost',12000))
print('connected to server')


print("Enter Your Name :")
name = str(input());

while True:
    recData = client.recv(1024).decode()
    print('server:', recData)
    data = input(name+':')
    print('data sent')
    client.send(bytes(data, 'utf-8'))





client.close()