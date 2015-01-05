#!/usr/bin/env python


'''
# -*- coding: cp1252 -*-.
'''

from socket import *
import base64
from Crypto.Cipher import AES
import os

HOST = '192.168.1.4'
PORT = 8000
BUFSIZ = 1024
ADDR = (HOST, PORT)

def encryption(privateInfo):
	BLOCK_SIZE = 16
	PADDING = '{'

	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	# secret = os.urandom(BLOCK_SIZE) # the right way
	secret = 'E\xb0o\r\xe3\xc8\x96\xae\x8dz\x87\xe6/\x02\xdfS'
	# print 'encryption key: ', secret

	cipher = AES.new(secret)

	encoded = EncodeAES(cipher, privateInfo)
	return encoded


while True:
	tcpCliSock = socket(AF_INET, SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	data = raw_input('> ')
	encrypted_data = encryption(data)
	if not data:
		break
	tcpCliSock.send('%s\r\n' % encrypted_data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data.strip()
	tcpCliSock.close()


