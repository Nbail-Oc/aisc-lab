import socket

HOST = "localhost"  # same as the server; use server IP across computers
PORT = 12345         # same port as the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = "Hello Server! My name is a student."
client.send(message.encode())

reply = client.recv(1024).decode()
print("Reply from server:", reply)
client.close()
