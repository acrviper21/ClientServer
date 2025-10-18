import socket
from dotenv import load_dotenv
import os 

load_dotenv()

def start_client():
    #Allow user to choose a username
    username = input("Hello, please enter a username: ")
    
    SERVER_IP = os.getenv("SERVER_IP")
    SERVER_PORT = os.getenv("SERVER_PORT")
    client_socket = socket.socket()
    client_socket.connect((SERVER_IP, int(SERVER_PORT)))

    client_socket.send(username.encode())

    message = input(f"{username} -> ")

    while True:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        if message.lower().strip() == "exit":
            print(f"Server: {data}")
            break

        print(f"Server: {data}")
        message = input(f"{username} -> ")

    # Close connections
    client_socket.close()


if __name__ == '__main__':
    start_client() 