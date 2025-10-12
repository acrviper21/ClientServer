import socket
from dotenv import load_dotenv
import os

load_dotenv()

def start_server():
    max_clients = 1   

    # Get PC name
    host = socket.gethostname()
    print(f"The name of the local host is {host}")
    # Get IP from PC name
    SERVER_IP = socket.gethostbyname(host)
    print(f"IP address of the localhost is {SERVER_IP}")

    # Port number for server to run on
    SERVER_PORT = os.getenv("SERVER_PORT")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, int(SERVER_PORT)))

    # How many clients the server can listen for simultaneously
    server_socket.listen(max_clients)

    conn, address = server_socket.accept()

    while True:
        # Receive data stream
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"{"user"}: {str(data)}")
        # Send data back to client
        conn.send(data.encode())

    # Close connection
    conn.close()

if __name__ == '__main__':
    start_server()