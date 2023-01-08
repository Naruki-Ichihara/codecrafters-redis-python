# Uncomment this to pass the first stage
import socket

def create_server(port, ip="localhost"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    return server

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    #server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket = create_server(6379)
    client_connection, _ = server_socket.accept() # wait for client
    client_connection.recv(1024)
    client_connection.send(b"+PONG\r\n")

if __name__ == "__main__":
    main()
