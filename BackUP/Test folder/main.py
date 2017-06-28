#!/usr/bin/python
from flask import Flask, request, render_template


from time import gmtime, strftime
import threading, socket, time
import os, sys

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


def sendToPi(lightSet):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = "151.80.140.199"                        
    port = 2526

    try:
        s.connect((host, port))
        tm = s.recv(1024)

        ##
        message = lightSet
        
        
        print (sys.stderr, 'sending "%s"' % message)
        s.send(message.encode('ascii') + "\n")
        ##

        
        s.close()
        

    except:
        s.close()




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
        sendToPi("l1On")
    elif back == False:
        print "FAILED: to turn on light 1"
    
	
@app.route('/ProcessL1Off', methods=['L1Off'])
def Light1Off():
    sendToPi("l1Off")
	
	
@app.route('/ProcessL2On', methods=['L2On'])
def Light2On():
    global back

    print back
    if back == True:
        print "ON"
        sendToPi("l2On")
    elif back == False:
        print "FAILED: to turn on light 2"
    
	
@app.route('/ProcessL2Off', methods=['L2Off'])
def Light2Off():
    sendToPi("l2Off")

@app.route('/ProcessOFF', methods=['OFF'])
def OFF():
    sendToPi("BOTHOFF")

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
        sendToPi("BOTHON")


def mainSetup():
    print "Preparing"
    #Thread(target = background()).start()
    print "1"
    #Thread(target = telnetSet()).start()
    print "2"
    Thread(target = sendToPi("BOTHOFF")).start()
    print "3"
    


    print "Setup complete - Booting up..."
    launch()


def launch():
    print "...Launching Systems..."
    print "...Launching Web Server..."
    app.run(host='151.80.140.199')
    print "Web application can be found: 151.80.140.199:5000"
    
    print "Boot up complete"
    main()

mainSetup()
