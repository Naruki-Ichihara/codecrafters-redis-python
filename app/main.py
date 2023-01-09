# Uncomment this to pass the first stage
import socket

def create_server(port, ip="127.0.0.1"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen()
    return server

def main():
    #server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket = create_server(6379)
    client_connection, _ = server_socket.accept() # wait for client
    while True:
        client_connection.recv(1024)
        client_connection.send(b"+PONG\r\n")

if __name__ == "__main__":
    main()
