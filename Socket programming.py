#!/bin/python3
import socket

HOST= ' 192.168.1.2'
PORT=4545

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#think of AF_INET as ipv4 and sock_SREAM as port
s.connect((HOST,PORT))
