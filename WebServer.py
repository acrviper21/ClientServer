import socket
from dotenv import load_dotenv
import os

load_dotenv()

def start_server():
    max_clients = 1   
 
    # Get IP from PC name
    SERVER_IP = os.getenv("SERVER_IP")

    # Port number for server to run on
    SERVER_PORT = os.getenv("SERVER_PORT")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, int(SERVER_PORT)))

    # How many clients the server can listen for simultaneously
    server_socket.listen(max_clients)

    print("Waiting on client to connect")

    conn, address = server_socket.accept()

    client = {conn: conn.recv(1024).decode()}

    while True:
        # Receive data stream
        data = conn.recv(1024).decode()

        print(f"{client[conn]}: {data}")

        # Goodbye greeting for client leaving
        if data.lower().strip() == "exit":
            conn.send("Goodbye".encode())
      
        # Send data back to client
        message = input("Server -> ")
        conn.send(message.encode())
        if message.lower().strip() == "exit":
            print("Shutting down server...")
            break
        conn.send(message.encode())


    # Close connection
    conn.close()

if __name__ == '__main__':
    start_server()