from socket import *
import time

#Step 1 - Create a TCP/IP socket.
#This socket is used to connect to any TCP/IP socket server
clnt_sock = socket(AF_INET,SOCK_STREAM)

#Step 2 - Connect the socket to the server
clnt_sock.connect(('localhost',5700))

#Step 3 - Receive the welcome message from the serverr
msg = clnt_sock.recv(1024)
print(msg)

#This client does not sleep

#Step 4 - Send a string to the server
msg = "Hello to server from client 2"
clnt_sock.send(msg.encode())

#Step 5 - Receive the reversed string from the server and print
msg = clnt_sock.recv(1024)
print(msg)

clnt_sock.close()
