import threading
import socket

def handle_connection(client_connection):
    while True:
        try:
            client_connection.recv(1024)
            client_connection.send(b"+PONG\r\n")
        except ConnectionError:
            break


def create_server(port, ip="127.0.0.1"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen()
    return server

def main():
    server_socket = create_server(6379)
    while True:
        client_connection, _ = server_socket.accept()
        threading.Thread(target=handle_connection, args=(client_connection,)).start()

if __name__ == "__main__":
    main()
