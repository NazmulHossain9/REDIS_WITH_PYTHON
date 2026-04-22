import socket

def main():
    print("Hello from redis-with-python!")
    server_socket= socket.create_server(('localhost', 6379), reuse_port=True)
    server_socket.accept()  # This will block until a client connects
    # print("Client connected!") # wait for client


if __name__ == "__main__":
    main()
