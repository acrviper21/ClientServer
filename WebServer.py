import socket
from dotenv import load_dotenv
import os

load_dotenv()

def start_server():
    # Get PC name
    host = socket.gethostname()
    print(f"The name of the local host is {host}")
    # Get IP from PC name
    IP = socket.gethostbyname(host)
    print(f"IP address of the localhost is {IP}")

    # Port number for server to run on
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    start_server()