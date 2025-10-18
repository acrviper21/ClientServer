import socket
from dotenv import load_dotenv
import os 
import sys

load_dotenv()

def start_client():
    #Allow user to choose a username
    username = input("Hello, please enter a username: ")
    
    SERVER_IP = os.getenv("SERVER_IP")
    SERVER_PORT = os.getenv("SERVER_PORT")
    client_socket = socket.socket()

    # Try connecting to server
    # If server not connected exit
    try:
        client_socket.connect((SERVER_IP, int(SERVER_PORT)))
        client_socket.send(username.encode())
        message = input(f"{username} -> ")
    except ConnectionRefusedError:
        print("Cannot connect to server...")
        print("Try again later. Exiting...")
        sys.exit(1)

    while True:
        try:
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
        except BrokenPipeError:
            print("Server is currently down.")
            print("Try again later. Exiting...")
            client_socket.close()
            sys.exit(1)

        if data.lower().strip() == "exit":
            print("Server is closing.")
            client_socket.close()
            break
            

        if message.lower().strip() == "exit":
            print(f"Server: {data}")
            client_socket.close()
            break

        print(f"Server: {data}")
        message = input(f"{username} -> ")

    # Close connections
    client_socket.close()


if __name__ == '__main__':
    start_client() 