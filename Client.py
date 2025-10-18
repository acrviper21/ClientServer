import socket
from dotenv import load_dotenv
import os 

def start_client():
    username = input("Hello, please enter a username: ")
    print(username)
    SERVER_IP = os.getenv("SERVER_IP")
    SERVER_PORT = os.getenv("SERVER_PORT")
    client_socket = socket.socket()
    client_socket.connect((SERVER_IP, SERVER_PORT))


if __name__ == '__main__':
    start_client() 