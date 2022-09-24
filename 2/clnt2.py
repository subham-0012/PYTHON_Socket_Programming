from socket import *
import time

#Step 1 - Create a TCP/IP socket.
#This socket is used to connect to any TCP/IP socket server
clnt_sock = socket(AF_INET,SOCK_STREAM)

#Step 2 - Connect the socket to the server
clnt_sock.connect(('localhost',5500))

#Step 3 - Receive the welcome message from the serverr
msg = clnt_sock.recv(1024)
print(msg)

#This client does not sleep

#Step 4 - Sends reply
rep = "Client2: Starting to talk...."
clnt_sock.send(rep.encode())

#Step 5 - Close the socket
clnt_sock.close()
