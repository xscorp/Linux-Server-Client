#!/usr/bin/env python3
import socket
import sys

def printUsage():
	print("[ERROR]: Invalid number of arguments!")
	print(
	"\nUSAGE:\n"+
	"______\n\n"+
	"$ ./client.py [Host IP to connect to] [port to connect to]\n"+
	"[NOTE] You need to be root for using port below 1025\n\n")
	sys.exit()
	
def errorExit():
	client_socket.close()
	sys.exit()

if len(sys.argv) != 3:
	printUsage()

#check if the port number entered by user is numeric or not
try:
	port = int(sys.argv[2])
except ValueError:
	print("Invalid value of port! Port must be numeric!")
	sys.exit()

#host to connect to
host = sys.argv[1]

#creating socket
try:
	client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM , 0)
except socket.error:
	print("Error occured in socket.socket() : " , socket.error)
	client_socket = None
	sys.exit()
else:	
	print("[+]TCP IPV4 socket created")
	

#connecting to server
try:
	client_socket.connect((host , port))
except socket.error:
	print("Error occured in connect() : " , socket.error)
	errorExit()
else:
	print("[+]Connected to remote host" , host)
	

#talking to server
server_message = ""
while True:
	try:
		server_message = client_socket.recv(1024)	
		if len(server_message) == 0:		#0 bytes received
			print("\n\nConnection closed by the server!")
			errorExit()
			
	except socket.error:
		print("[ERROR]: recv(): " , socket.error)
		errorExit()
		
	except:
		print("\n[+]Connection closed!")
		errorExit()
		
	else:
		print("\nThey:")
		#data received is of type 'byte'. Decode it in either ASCII or UTF-8
		print(server_message.decode("ascii"))
		
	print("\nYou:")
	try:
		#the data must be sent in the form of byte string and not string
		#To convert data to byte string, encode() is used
		client_socket.sendall(input().encode())
	except socket.error:
		print("\n\n[ERROR]: sendall(): " , socket.error)
		errorExit()
		
	except:
		print("\n[+]You closed the connection!\n")
		errorExit()
		
		
#closing the socket
client_socket.close()
