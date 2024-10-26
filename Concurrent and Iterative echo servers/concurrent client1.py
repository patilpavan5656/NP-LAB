import socket

PORT = 4444

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddr = ('127.0.0.1', PORT)

try:
    clientSocket.connect(serverAddr)
    print("Connected to Server.\n")

    while True:
        data = clientSocket.recv(1024)

        if not data:
            break

        print(f"Server: {data.decode('utf-8')}")

except Exception as e:
    print(f"Error in connection: {e}")

finally:
    clientSocket.close()