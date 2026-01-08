import socket
import threading

# Server configuration
HOST = '127.0.0.1'   # Localhost
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("🔵 Server started... Waiting for connections")

# Broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle individual client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

# Accept clients
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()
