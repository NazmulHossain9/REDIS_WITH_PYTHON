import socket

def main():
    print("Hello from redis-with-python!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket.accept() # wait for client
    connection, _ = server_socket.accept()
    connection.sendall(b"+PONG\r\n")



if __name__ == "__main__":
    main()
