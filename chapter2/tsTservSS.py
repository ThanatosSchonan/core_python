from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = 'localhost'
PORT = 21567
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print "...connected from:",self.client_address
        while True:
            str = self.rfile.readline()
            print str,
            self.wfile.write('[%s] %s' % (ctime(),str))
tcpServ = TCP(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()