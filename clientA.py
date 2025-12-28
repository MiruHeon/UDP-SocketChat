import socket
import threading

HOST = "127.0.0.1"
PORT = 9001
PEER_PORT = 9002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

def receive():
    while True:
        data, _ = sock.recvfrom(1024)
        print(f"\n상대: {data.decode()}\n입력: ", end="")

threading.Thread(target=receive, daemon=True).start()

while True:
    msg = input("입력: ")
    sock.sendto(msg.encode(), (HOST, PEER_PORT))
