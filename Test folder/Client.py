import socket, time, sys

def send(mes1, mes2):
    pastAnswer = ""  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = "151.80.140.199"                        
    port = 2526


    try:
        s.connect((host, port))
        tm = s.recv(1024)

        ##
        message = str(mes1)
        message2 = str(mes2)
        
        
        print (sys.stderr, 'sending "%s"' % message)
        s.send(message.encode('ascii') + " " + message2.encode('ascii') + "\n")
        ##

        
        s.close()
        

    except:
        s.close()



def timer():
    ping = 5
    while ping > 0:
        time.sleep(1)
        
        print ping
        ping -= 1
    recieve()
   


    



