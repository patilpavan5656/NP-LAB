import socket
import time

multicast_group = ('224.0.0.1', 4321)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 16)

while True:
    message = input("Enter message for multicast: ")
    print("Sending message")
    sock.sendto(message.encode(), multicast_group)
    time.sleep(1)