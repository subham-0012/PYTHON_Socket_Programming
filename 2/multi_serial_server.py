from socket import *

#Step 1 - Create a TCP/IP socket.
#This socket is used in listening for connections
srvr_sock = socket(AF_INET,SOCK_STREAM)

#Step 2 - Bind the socket - Argument is an address tuple
srvr_sock.bind(('localhost',5500))

#Step 3 - Make the socket listen for valid connections
srvr_sock.listen(5)#5 is the number of clients that could be queued before rejection
print("Server started....")

while True:
    #Step 4 - Socket accepts when a valid client connects
    tpl = srvr_sock.accept() 

    #Server sends a welcome message
    wel_msg = "Welcome client %s"%tpl[1][0]
    conn = tpl[0]
    conn.send(wel_msg.encode())

    #Receive the reply from client
    rec_msg=conn.recv(1024)
    print(rec_msg)
    conn.close()











