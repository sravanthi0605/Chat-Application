import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name:")

# Receive messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection closed")
            client.close()
            break

# Send messages
def write():
    while True:
        message = f"{name}: {input('')}"
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
