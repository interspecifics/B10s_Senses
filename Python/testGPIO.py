#!/usr/bin/env python

import sys, time
import RPi.GPIO as GPIO

FPS = 20.0
LOOP_PERIOD = 1.0/FPS

TENS_FREQ = 80
TENS_PERIOD = 1.0/TENS_FREQ

GPIOS = (4,17,27,22, 18,23,24,25, 5,6,13,19, 12,16,20,21)
TENS_LEN = len(GPIOS)
gpioVals = [[0]*TENS_LEN]
TENS_DIM = (4, 4)

if(TENS_DIM[0]*TENS_DIM[1] > TENS_LEN):
    print "Something wrong with matrix dimensions. Check GPIO and TENS_DIM."
    sys.exit(0)

lastChange = 0
mLoc = 0

GPIO.setmode(GPIO.BCM)
for pin in GPIOS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

def loop():
    global lastChange, mLoc
    now = time.time()
    if(now - lastChange > 0.5):
        lastChange = now
        mLoc = (mLoc + 1)%TENS_LEN
        gpioVals = [[0]*TENS_LEN]
        gpioVals[mLoc] = 1
        print gpioVals

lastLoop = 0
while True:
    tensWaveVal = int(time.time()/TENS_PERIOD)%2
    GPIO.output(GPIOS, tuple([tensWaveVal*v for v in gpioVals]))

    now = time.time()
    if (now-lastLoop > LOOP_PERIOD):
        lastLoop = now
        loop()
