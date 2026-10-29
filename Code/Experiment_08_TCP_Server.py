import socket

HOST = "localhost"  # same computer; use server IP for another computer
PORT = 12345         # server and client must use the same port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Server waiting for connection...")

client, address = server.accept()
print("Client connected:", address)

message = client.recv(1024).decode()
print("Message from client:", message)

reply = "Hello Client! Your message has been received."
client.send(reply.encode())

client.close()
server.close()
