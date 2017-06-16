import socket, time

def recieve():
    pastAnswer = ""  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = "localhost"                        
    port = 6545

    s.connect((host, port))
    tm = s.recv(1024)                                     
    s.close()
    answer = tm.decode('ascii')
    print answer

    timer()




def timer():
    ping = 5
    while ping > 0:
        time.sleep(1)
        
        print ping
        ping -= 1
    recieve()
   

recieve()


    



