from flask import Flask, request
import json
import threading
import subprocess
import os

from sys import executable




app = Flask(__name__)


def background():
   print "DOWNLOADING NEW UPDATE"
   
   os.system("pkill gnome-terminal")

   os.chdir("/root/HAS")
   return_code = subprocess.call("sudo git pull origin master", shell=True) 

   p = os.system("gnome-terminal -e 'bash -c \"sudo python main.py ; exec bash\"'")





  

@app.route('/',methods=['POST'])
def foo():
   data = json.loads(request.data)


   print "New commit by: {}".format(data['commits'][0]['author']['name'])
   return background()


def mainSetup():
 
   
   app.run(host= '151.80.140.199', port=6000, debug=False)




mainSetup()


