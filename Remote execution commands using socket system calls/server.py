import socket
import subprocess

serverName = "127.0.0.1"
serverPort = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(1)
    print("The server is ready to receive")
    
    while True:
        connectionSocket, addr = serverSocket.accept()
        
        while True:
            request = connectionSocket.recv(1024).decode()
            print(f'Received the request:\n{request}')
            
            if request == "exit":
                connectionSocket.send('Session terminated'.encode())
                break
            
            status, output = subprocess.getstatusoutput(request)
            response = output if status == 0 else f'Error: {output}'
            connectionSocket.send(response.encode())
            
        print('Bye')
        connectionSocket.close()
