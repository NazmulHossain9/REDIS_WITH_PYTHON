import socket
import time

def is_internet_available():
    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except Exception:
        return False

def main():
    print("Hello from redis-with-python!")

    # server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket = socket.create_server(("localhost", 6379), reuse_address=True)
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True, backlog=5)

    while True:
        connection, _ = server_socket.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            if b"PING" in data.upper():
                print("Received PING")
                if not is_internet_available():
                    print("No internet, waiting...")
                    while not is_internet_available():
                        time.sleep(1)
                    print("Internet back!")
                connection.sendall(b"+PONG\r\n")
            else:
                print(f"Received unknown command: {data}")
                connection.sendall(b"-ERR unknown command\r\n")
        connection.close()
            

if __name__ == "__main__":
    main()
