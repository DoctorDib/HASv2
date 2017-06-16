#!/usr/bin/python
from flask import Flask, request, render_template


from time import gmtime, strftime
import threading, socket, time
import os

app = Flask(__name__)

pinList = [2, 3]

tick = 0

checkLoop = False

timeOut = False
AFK = True

back = True
dayLight = True

sleep = False






#=============================
message = ""

serversocket = socket.socket(
                        socket.AF_INET, socket.SOCK_STREAM) 

host = "151.80.140.199"
port = 5005                                  

serversocket.bind((host, port))                                  
serversocket.listen(5)
#==============================



#=========================================
global light1

global light2
#=========================================




#dayLightSave = False

def background():

    global dayLight
    global sleep
    global tick
    global back
    
    while True:
        
        hour = int(strftime("%H"))
        if hour >= 8 and hour <= 17:
            sleep = False
            dayLight = True
            
        elif hour > 18 and hour <= 24 or hour >= 1 and hour < 8:
            dayLight = False
            

     

def sendToPi():


    
    while True:
        conn, addr = serversocket.accept()
        print 'Connected by', addr
        conn.send("confirm")
        conn.close()



        

        clientsocket,addr = serversocket.accept()      

        print("Got a connection from %s" % str(addr))
                
        light1Message = str(light1)

        light2Message = str(light2)
        
        clientsocket.send(light1Message.encode('ascii') + " " + light2Message.encode('ascii'))

        clientsocket.close()
        




@app.route('/')
def main():
    global back
    
    if back == True:
        return render_template("index.html")
    else:
        return render_template("out.html")




@app.route('/ProcessL1On', methods=['L1On'])
def Light1On():
    global back
    if back == True:
        print "ON"
        light1 = True
    elif back == False:
        print "FAILED: to turn on light 1"
    
	
@app.route('/ProcessL1Off', methods=['L1Off'])
def Light1Off():
    light1 = False
	
	
@app.route('/ProcessL2On', methods=['L2On'])
def Light2On():
    global back

    print back
    if back == True:
        print "ON"
        light2 = True
    elif back == False:
        print "FAILED: to turn on light 2"
    
	
@app.route('/ProcessL2Off', methods=['L2Off'])
def Light2Off():
    light2 = False

@app.route('/ProcessOFF', methods=['OFF'])
def OFF():
    light1 = False
    light2 = False

@app.route('/ProcessSLEEP', methods=['SLEEP'])
def sleep():
    global sleep
    print "Good night"
    sleep = True
    OFF()

@app.route('/ProcessWAKE', methods=['WAKE'])
def wake():
    global sleep
    print "Good morning"
    sleep = False
    ON()
    

@app.route('/ProcessON', methods=['ON'])
def ON():
    global dayLight
    if dayLight == False:
        light1 = True
        light2 = True


def mainSetup():
    t = threading.Thread(target=background)
    t.start()

    p = threading.Thread(target=sendToPi)
    p.start()

    
    launch()


def launch():
    print "...Launching Systems..."
    print "...Launching Web Server..."
    app.run(host='151.80.140.199')
    print "Web application can be found: 192.168.0.29:5000"
    
    print "Enjoy!"
    main()

mainSetup()
