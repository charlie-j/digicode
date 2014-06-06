#!/usr/bin/env python
#-*- coding: utf-8 -*-



from time import sleep

from sys import exit

import RPi_GPIO

import signal

import time

 
#The class used to handle timeout while typing a code
class Timeout():

    """Timeout class using ALARM signal."""

    class Timeout(Exception):

        pass

 

    def __init__(self, sec):

        self.sec = sec

 

    def __enter__(self):

        signal.signal(signal.SIGALRM, self.raise_timeout)

        signal.alarm(self.sec)

 

    def __exit__(self, *args):

        signal.alarm(0)    # disable alarm

 

    def raise_timeout(self, *args):

        raise Timeout.Timeout()




#Initializing the keypad
kp = RPi_GPIO.keypad(columnCount = 3)



#First loop, waiting for a keypress to launch the timeout 
while True:

    digit = None

    while digit == None:

        digit = kp.getKey()
    if (digit=="#" ):
        print "Faudrait taper un code avant de valider"
        continue
    code = str(digit) 
    while True:
        try:
            with Timeout(2):
                digit = None        
                while digit == None:
                    digit = kp.getKey()

                #When the user validate by pressing #, we send the last four digit pressed to the output
                if (digit=="#" ):

                    print "Code tapé : %s" % (code[-4:])
                    break
                else:

                    code += str(digit)
                    


        except Timeout.Timeout:

            print "T'es trop lent"
            break




