#!/usr/bin/env python

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
import base64
from Crypto.Cipher import AES
import os

HOST = ''
PORT = 8000
ADDR = (HOST, PORT)


def decryption(encryptedString):
	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	key = 'E\xb0o\r\xe3\xc8\x96\xae\x8dz\x87\xe6/\x02\xdfS'
	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryptedString)
	return decoded

class MyRequestHandler(SRH):
	def handle(self):
		print '... connected from: ', self.client_address
		recv_text = self.rfile.readline()
		self.wfile.write('[%s] Recieved: %s Decrypted: %s' % (ctime(),recv_text, decryption(recv_text)))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()


''' base code

import socket
import sys



serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF = address family, SOCK_STREAM = tcp
# binding time
serverSock.bind(("0.0.0.0",8000)) # 0.0.0.0 all available interfaces
serverSock.listen(2) # 2 = handle 2 clients conccurently
(client,(ip,port))=serverSock.accept() # accept == blocking

'''

