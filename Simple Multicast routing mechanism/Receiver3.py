from socket import *
import struct

socketfd = socket(AF_INET, SOCK_DGRAM,0)
socketfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
port = 4321
socketfd.bind(("", port))
group = '224.0.0.1'
mreq = struct.pack("!4sl", inet_aton(group), INADDR_ANY)
socketfd.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
print("Waiting for Message")
while True:
    print(socketfd.recv(1024).decode())