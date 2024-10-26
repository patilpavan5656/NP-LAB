import socket

serverName = "127.0.0.1"
serverPort = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.connect((serverName, serverPort))

    while True:
        command = input('Enter the command (or "exit" to quit):\n')
        if not command:
            print("Empty command")
            continue
        
        clientSocket.send(command.encode())
        response = clientSocket.recv(1024).decode()
        print(f'From Server:\n{response}')
        
        if command == "exit":
            break
