from socket import *

serverName = "0:0:0:0:0:0:0:1"
serverPort = 12000

clientSocket = socket(AF_INET6, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = str(input("Enter file name : "))
clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(1024).decode()
print ('From Server:', filecontents)

clientSocket.close()