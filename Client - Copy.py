import socket, time



def send():
    pastAnswer = ""
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    host = "151.80.140.199"                        
    port = 9000

    s.connect((host, port))
    tm = s.recv(1024)                                     

    s.close()

    answer = tm.decode('ascii')

        


    if answer != pastAnswer:
        pastAnswer = answer
        print(answer)

    timer()


def timer():
    ping = 5
    while ping > 0:
        time.sleep(1)
        
        print ping
        ping -= 1
    send()

timer()

    



