from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCloSock = socket(AF_INET,SOCK_STREAM)
tcpCloSock.connect(ADDR)

while True:
    data = input('> ')
    data = bytes(data,'utf-8')
    if not data:
        break
    tcpCloSock.send(data)
    data = tcpCloSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCloSock.close()