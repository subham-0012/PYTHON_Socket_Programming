from socket import *
import threading
#Step 1 - Create a TCP/IP socket.
#This socket is used in listening for connections
srvr_sock = socket(AF_INET,SOCK_STREAM)
#Step 2 - Bind the socket - Argument is an address tuple
srvr_sock.bind(('localhost',5700))
#Step 3 - Make the socket listen for valid connections
srvr_sock.listen(5)#5 is the number of clients that could be queued before rejection
print("Server started....")
#One client-server talking  - work handled by thread
def clientTalking(*tpl):
    #Server sends a welcome message
    wel_msg = "Welcome client %s"%tpl[1][0]
    conn = tpl[0]
    conn.send(wel_msg.encode())
    #Receive the reply from client
    rec_msg=conn.recv(1024)
    print(rec_msg)    #Reverse the reply and send it back
    b_msg = str(rec_msg)[::-1].encode()
    conn.send(b_msg)
    conn.close()
while True:
    #Step 4 - Socket accepts when a valid cient connects
    tpl_clnt = srvr_sock.accept() #same as >>>a,b = srvr_sock.accept()
    #The result of accpet is a tuple of two elements
    #First element is another socket object for talking between the server and client
    #Second element is the address tuple (ip, port) of the client
    #Every client-server talking is handled by a thread
    thrd = threading.Thread(target=clientTalking,args=tpl_clnt)
    thrd.start()












