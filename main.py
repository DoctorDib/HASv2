#!/usr/bin/python
from flask import Flask, request, render_template


from time import gmtime, strftime
import threading, socket, time
import os

import threading
from threading import Thread

app = Flask(__name__)

pinList = [2, 3]

tick = 0

checkLoop = False

timeOut = False
AFK = True

back = True
dayLight = True

sleep = False



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


def sendToPi(light1Settings, light2Settings):
    global addr
    message = ""

    serversocket = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM) 

    host = "151.80.140.199"
    port = 7600                                 

    serversocket.bind((host, port))                                  
    serversocket.listen(5)

    print "TelNet has been set, open connection to " + str(host) + ":" + str(port)


    conn, addr = serversocket.accept()
    print 'Connected by', addr
    conn.send("confirm")
    conn.close()

    clientsocket,addr = serversocket.accept()
    
    

    print("Got a connection from %s" % str(addr))
                    
    light1Message = str(light1Settings)

    light2Message = str(light2Settings)
            
    clientsocket.send(light1Message.encode('ascii') + " " + light2Message.encode('ascii'))

    
        




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
        sendToPi(True, "")
    elif back == False:
        print "FAILED: to turn on light 1"
    
	
@app.route('/ProcessL1Off', methods=['L1Off'])
def Light1Off():
    sendToPi(False, "")
	
	
@app.route('/ProcessL2On', methods=['L2On'])
def Light2On():
    global back

    print back
    if back == True:
        print "ON"
        sendToPi("", True)
    elif back == False:
        print "FAILED: to turn on light 2"
    
	
@app.route('/ProcessL2Off', methods=['L2Off'])
def Light2Off():
    sendToPi("", False)

@app.route('/ProcessOFF', methods=['OFF'])
def OFF():
    sendToPi(False, False)

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
        sendToPi(True, True)


def mainSetup():
    print "Preparing"
    #Thread(target = background()).start()
    print "1"
    #Thread(target = telnetSet()).start()
    print "2"
    #Thread(target = sendToPi(False, False)).start()
    print "3"
    


    print "Setup complete - Booting up..."
    launch()


def launch():
    print "...Launching Systems..."
    print "...Launching Web Server..."
    app.run(host='151.80.140.199')
    print "Web application can be found: 192.168.0.29:5000"
    
    print "Boot up complete"
    main()

mainSetup()
