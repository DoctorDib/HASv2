from bluetooth import *

import RPi.GPIO as GPIO

import socket



GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)


auth = "74:A5:28:FA:51:B7"

bConnected = False
tick = False
back = False
daylight = False


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
            print "day"
        elif hour > 18 and hour <= 24 or hour >= 1 and hour < 8:
            dayLight = False
            print "night"

        print dayLight
        print hour



    
        nearby_devices = discover_devices(lookup_names = True)
        print "found %d devices" % len(nearby_devices)
        print str(nearby_devices)

        for addr in nearby_devices:
            for i in addr:
                print i
                print "i"
                    
       

        if len(nearby_devices) == 0:
            if back == True and tick == 3:
                print "-------------------------------------------------"
                print "================================================="
                print "                   GOOD BYE                      "
                print "================================================="
                print "-------------------------------------------------"

            if tick == 3:
                back = False
                BOTHOFF()
                tick += 1
            elif tick == 5:
                tick = 0
                
            else:
                tick += 1
                print tick
                
            
        else:
            tick = 0
            for name, addr in nearby_devices:
                if sleep == False and name == auth:
                    
                    print "ACCEPTED"
                    
                    if back == False:
                        print "-------------------------------------------------"
                        print "================================================="
                        print "                 WELCOME BACK                    "
                        print "================================================="
                        print "-------------------------------------------------"

                                
                    if dayLight == False and back == False:
                        print "================================================="
                        print "              NIGHT MODE - ACTIVE                "
                        print "================================================="
                        back = True
                        BOTHON()
                    elif dayLight == True and back == False:
                        print "================================================="
                        print "              DAY MODE - ACTIVE                  "
                        print "================================================="
                        back = True
                        BOTHOFF()
                    elif back == True:
                        print "SKIPPED"
                    else:
                        print "Error"
               
                else:
                    print "**SLEEP MODE ACTIVE**"


def light1On():
    global back
    
    if back == True:
        print "ON"
        GPIO.output(2, GPIO.LOW)
    elif back == False:
        print "FAILED: to turn on light 1"
        
    main()

def light1Off():
    print "LIGHT 1 OFF"
    GPIO.output(2, GPIO.HIGH)
    main()

def light2On():
    global back

    if back == True:
        print "ON"
        GPIO.output(3, GPIO.LOW)
    elif back == False:
        print "FAILED: to turn on light 2"
        
    main()

def light2Off():
    print "LIGHT 2 OFF"
    GPIO.output(3, GPIO.HIGH)
    main()

def plugOn():
    global back

    if back == True:
        print "ON"
        GPIO.output(1, GPIO.LOW)
    elif back == False:
        print "FAILED: to turn on plug"
        
    main()

def plugOff():
    print "PLUG OFF"
    GPIO.output(1, GPIO.HIGH)
    main()

def BOTHON():
    print "BOTH ON"
    GPIO.output(3, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    main()

def BOTHOFF():
    print "BOTH OFF"
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.HIGH)
    main()
    
def main():
    socket = socket.socket()
    
    host = '151.80.140.199'
    port = 2526 

    socket.connect((host, port))
    while True:
        answer = socket.recv(1024)
        print answer

        if "BOTHON" in answer:
            BOTHON()
        elif "BOTHOFF" in answer:
            BOTHOFF()
        
        elif "l1On" in answer: 
           print "Light 1 On"
           light1On()
        elif "l1Off" in answer: 
           print "Light 1 Off"
           light1Off()
        elif "l2On" in answer: 
           print "Light 2 On"
           light2On()
        elif "l2Off" in answer: 
           print "Light 2 Off"
           light2Off()
        elif "plugOn" in answer:
            print "Plug On"
            plugOn()
        elif "plugOff" in answer:
            print "Plug Off"
            plugOff()
        else:
            print "COMMAND UNKNOWN"

    socket.close()


def setup():
    t = threading.Thread(target=background)
    t.start()
    main()
    
