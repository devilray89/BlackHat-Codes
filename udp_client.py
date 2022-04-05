#!/usr/bin/python3

import socket

target_host = "127.0.0.1"
target_port = 9998

#create socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send data
client.sendto(b"AAABBBCC",(target_host,target_port))

#receive some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
