import socket
import multiprocessing

PORT = 4444

def handle_client(clientSocket, cliAddr, cnt):
    print(f"Connection accepted from {cliAddr[0]}:{cliAddr[1]}")
    print(f"Clients connected: {cnt}\n")

    clientSocket.send(b"hi client")
    clientSocket.close()

def main():
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddr = ('127.0.0.1', PORT)
    sockfd.bind(serverAddr)
    sockfd.listen(10)

    print("Listening...\n")

    cnt = 0
    while True:
        clientSocket, cliAddr = sockfd.accept()
        cnt += 1

        process = multiprocessing.Process(target=handle_client, args=(clientSocket, cliAddr, cnt))
        process.start()

if __name__ == "__main__":
    main()