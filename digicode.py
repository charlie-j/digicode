#!/usr/bin/env python
#-*- coding: utf-8 -*-



## ######################################################

##

## Package:             matrix_keypad

## Script:              matrix_keypad_demo2.py

##

## Author:              Chris Crumpacker

## Date:                August 2013

##

## Project page:        http://crumpspot.blogspot.com/p/keypad-matrix-python-package.html

## PyPI package:        https://pypi.python.org/pypi/matrix_keypad

##

## Notes:               This demo shows how to loop waiting for keypresses

##                      and add to a set variable. Adapted from code from

##                      Jeff Highsmith for his PiLarm that can be found here:

##                      https://github.com/BabyWrassler/PiNopticon/blob/master/keypadd.py

##

## ######################################################



from time import sleep

from sys import exit



## Select which board/IO version by commenting the unused version 



# from matrix_keypad import MCP230xx

import RPi_GPIO

import signal

import time

 

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



# from matrix_keypad import BBb_GPIO

 

## Initialize the keypad class.

##   Uncommont the matching initialzation to the imported package from above

##   Use the **optional** variable "columnCount" to change it from a 3x4 to a 4x4 keypad



# kp = MCP230xx.keypad(address = 0x21, num_gpios = 8, columnCount = 4)

kp = RPi_GPIO.keypad(columnCount = 3)

# kp = BBb_GPIO.keypad(columnCount = 3)





# Setup variables

attempt = "0000"

passcode = "1912"

counter = 0





import getpass

while True:

    digit = None

    while digit == None:

        digit = kp.getKey()

    try:

        with Timeout(5):

            code = str(digit)

            while True:

                digit = None

                while digit == None:

                    digit = kp.getKey()

                if (digit=="#" ):

                    print "Code tapé : %s" % (code[-4:])
                    sleep(0.5)
                else:

                    code += str(digit)
                    sleep(0.1)


    except Timeout.Timeout:

        print "T'es trop lent"




