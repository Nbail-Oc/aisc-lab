from pathlib import Path
from urllib.request import urlopen

BASE_URL = "https://cn-lab.onrender.com"
FILES = [
    "README.txt",
    "Ports_and_Run_Instructions.txt",
    "PDFs/Experiment_02_TCP_IP_Utility_Commands.pdf",
    "PDFs/CN_Practical_Theory_Experiments_02-10.pdf",
    "PDFs/Experiment_03_DNS_with_Cisco_Packet_Tracer.pdf",
    "PDFs/Experiment_04_Hub_and_Switch_Topology.pdf",
    "PDFs/Practical_05_Static_Routing_GNS3.pdf",
    "PDFs/Experiment_07_EIGRP_Dynamic_Routing_GNS3.pdf",
    "PDFs/Experiment_08_TCP_Client_Server_Sockets.pdf",
    "PDFs/Experiment_09_UDP_File_Transfer.pdf",
    "PDFs/Experiment_10_Wireshark_Packet_Analysis.pdf",
    "Code/Experiment_08_TCP_Server.py",
    "Code/Experiment_08_TCP_Client.py",
    "Code/Experiment_09_UDP_Receiver.py",
    "Code/Experiment_09_UDP_Sender.py",
]

folder = Path.home() / "CN_LAB"
for name in FILES:
    destination = folder / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(f"{BASE_URL}/{name}") as response:
        destination.write_bytes(response.read())
    print("Downloaded:", destination)

print("\nFinished. Your files are in:", folder)
