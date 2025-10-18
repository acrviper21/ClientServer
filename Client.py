import socket
from dotenv import load_dotenv
import os 
import sys
from colorama import Fore

load_dotenv()

def start_client():
    # Default text color
    default_text_color = Fore.RESET
    text_color = default_text_color

    # Allow user to choose a username
    username = input("Hello, please enter a username: ")
    
    SERVER_IP = os.getenv("SERVER_IP")
    SERVER_PORT = os.getenv("SERVER_PORT")
    client_socket = socket.socket()

    # Try connecting to server
    # If server not connected exit
    try:
        client_socket.connect((SERVER_IP, int(SERVER_PORT)))
        client_socket.send(username.encode())
        #message = input(f"{text_color}{username} {default_text_color}-> ")
    except ConnectionRefusedError:
        print("Cannot connect to server...")
        print("Try again later. Exiting...")
        sys.exit(1)

    while True:    
        message = input(f"{text_color}{username} {default_text_color}-> ")

        if message.lower().strip() == "\\blue":
            text_color = Fore.BLUE
            continue
        elif message.lower().strip() == "\\green":
            text_color = Fore.GREEN
            continue
        elif message.lower().strip() == "\\red":
            text_color = Fore.RED
            continue
        elif message.lower().strip() == "\\default":
            text_color = Fore.RESET
            continue

        try:
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()

            # If server shuts down then exit
            if data.lower().strip() == "exit":
                print("Server is closing.")
                client_socket.close()
                break

            # If client shuts down let server know
            elif message.lower().strip() == "exit":
                print(f"Server: {data}")
                client_socket.close()
                break
            # Else just print the server message
            else:
                print(f"Server: {data}")

        except BrokenPipeError:
            print("Server is currently down.")
            print("Try again later. Exiting...")
            client_socket.close()
            sys.exit(1)


        

    # Close connections
    client_socket.close()


if __name__ == '__main__':
    start_client() 