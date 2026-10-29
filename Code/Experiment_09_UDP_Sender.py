import socket
import struct

SERVER_IP = "192.168.1.20"  # replace with the receiver computer's IP
SERVER_PORT = 5000
BUFFER_SIZE = 1024
HEADER_SIZE = 4

filename = input("File to send (for example sample.txt): ")
server = (SERVER_IP, SERVER_PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(2)

name = filename.encode()
client.sendto(struct.pack("!I", len(name)) + name, server)
sequence = 0

try:
    with open(filename, "rb") as source:
        while True:
            chunk = source.read(BUFFER_SIZE)
            if not chunk:
                break
            packet = struct.pack("!I", sequence) + chunk
            while True:
                client.sendto(packet, server)
                try:
                    ack, address = client.recvfrom(HEADER_SIZE)
                    if struct.unpack("!I", ack)[0] == sequence:
                        break
                except socket.timeout:
                    print("Timeout; resending packet", sequence)
            sequence += 1

    while True:
        client.sendto(b"END", server)
        try:
            reply, address = client.recvfrom(BUFFER_SIZE)
            if reply == b"END_ACK":
                break
        except socket.timeout:
            print("Timeout; resending END")
    print("File transfer complete.")
except FileNotFoundError:
    print("File not found:", filename)
finally:
    client.close()
