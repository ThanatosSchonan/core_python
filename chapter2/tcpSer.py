from socket import *
from time import ctime
HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock,addr = tcpSerSock.accept()
    print("connected from:",addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data = str(data,'utf-8')
        print(data[:])
        dataStr = '[%s] %s' % (ctime(),data)
        tcpCliSock.send(bytes(dataStr,'utf-8'))
    tcpCliSock.close()
tcpSerSock.close()