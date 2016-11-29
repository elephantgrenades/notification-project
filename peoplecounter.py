###################################################
###################################################
#########  People Counter v1-1 ############
###################################################

################################
###Setting up Python Modules####
################################
import sys
import time
import datetime
import RPi.GPIO as GPIO
import mechanize
import os
import subprocess






################################
##### Setting up GPIO pins #####
################################
h1 = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(h1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

################################
######Setting up Counters ######
################################
peoplecount = 0
uploadcount = 0
door = 1    # <- Use this to designate multiple doors for tracking
location = 'Location'  # <- Use this to designate multiple locations for tracking in one form

################################
######## Setup Mechanize #######
###############################
br = mechanize.Browser()

###################################################
############# MAIN BODY OF PROGRAM ################
###################################################
while True:

## This waits for a specified minute of the hour, checks if anyone has been detected since the last upload, then uploads the data to a Google Form.
   if time.strftime("%M") in ("13", "28", "45", "58") and peoplecount > 0 and uploadcount == 0:
      try:
         url = "https://docs.google.com/forms/d/e/1FAIpQLScgYGjkXsF-1iE87c2JlpYkLbz9TcDx3D0pV-PVtvekBOO8VA/formResponse?ifq&entry.1570763274=%s&entry.1428120565=%s&entry.802789063=%s&submit=Submit&fbzx=4499308717411757586" % (location, door, peoplecount)
         response = br.open(url)
         print "People count uploaded with value %s on door %s at %s" % (peoplecount, door, location)
         uploadcount = 1
         peoplecount = 0
         print "values reset"
         sys.exit
      except:
         print "Cannot Access Page"
             

   elif time.strftime("%M") in ("14", "29", "46", "59") and uploadcount == 1:
      uploadcount = 0
          
   elif GPIO.input(h1) == True:
      peoplecount = peoplecount + 1
      print "Motion Detected: Door %s at %s on %s. Count is %s" % (door, time.strftime("%H:%M:%S"), time.strftime("%A"), peoplecount)
#      subprocess.call("./basic.py", shell=True)
      
      os.system ("rsync -avgz /home/pi/frog.txt pi@172.23.0.30:/home/pi/")
      sys.exit
         
      time.sleep(3)



