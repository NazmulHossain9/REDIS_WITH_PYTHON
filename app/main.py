import socket
import time
import queue
import threading

pending_queue = queue.Queue()

def is_internet_available():
    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except Exception:
        return False

def queue_processor():
    while True:
        if not pending_queue.empty() and is_internet_available():
            connection, data = pending_queue.get()
            print(f"Processing queued command: {data}")
            if b"PING" in data.upper():
                connection.sendall(b"+PONG\r\n")
            else:
                connection.sendall(b"-ERR unknown command\r\n")
        time.sleep(1)

def handle_connection(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        if is_internet_available():
            if b"PING" in data.upper():
                print("Received PING")
                connection.sendall(b"+PONG\r\n")
            else:
                print(f"Received unknown command: {data}")
                connection.sendall(b"-ERR unknown command\r\n")
        else:
            print(f"No internet, queuing: {data}")
            pending_queue.put((connection, data))
    connection.close()

def main():
    print("Hello from redis-with-python!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True, backlog=5)

    threading.Thread(target=queue_processor, daemon=True).start()

    while True:
        connection, _ = server_socket.accept()
        threading.Thread(target=handle_connection, args=(connection,), daemon=True).start()

if __name__ == "__main__":
    main()
