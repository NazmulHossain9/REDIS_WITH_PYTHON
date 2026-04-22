import socket

def main():
    print("Hello from redis-with-python!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        connection, _ = server_socket.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            if b"PING" in data.upper():
                connection.sendall(b"+PONG\r\n")

if __name__ == "__main__":
    main()
