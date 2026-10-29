import socket
import struct
from pathlib import Path

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024
HEADER_SIZE = 4

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print("UDP file receiver started; waiting for file...")

data, sender = server.recvfrom(BUFFER_SIZE)
name_length = struct.unpack("!I", data[:HEADER_SIZE])[0]
filename = Path(data[HEADER_SIZE:HEADER_SIZE + name_length].decode()).name
output_name = "received_" + filename
expected = 0

with open(output_name, "wb") as output:
    while True:
        data, address = server.recvfrom(BUFFER_SIZE + HEADER_SIZE)
        if data == b"END":
            server.sendto(b"END_ACK", sender)
            break

        sequence = struct.unpack("!I", data[:HEADER_SIZE])[0]
        if sequence == expected:
            output.write(data[HEADER_SIZE:])
            ack = sequence
            expected += 1
        else:
            ack = max(0, expected - 1)  # acknowledge the last saved packet
        server.sendto(struct.pack("!I", ack), sender)

print("File received:", output_name)
server.close()
