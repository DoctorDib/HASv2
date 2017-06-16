# server.py 
import socket, time                                        
import time

message = ""

serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

host = "151.80.140.199"                          
port = 9000                                     

serversocket.bind((host, port))                                  
serversocket.listen(5)                                           




clientsocket,addr = serversocket.accept()      

print("Got a connection from %s" % str(addr))
        
message = "GoodBye"
Message1 = "HI"

        
clientsocket.send(message.encode('ascii') + " " + Message1.encode('ascii'))
clientsocket.close()
