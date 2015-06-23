#!/usr/bin/env python

import sys, time
import RPi.GPIO as GPIO

FPS = 20.0
LOOP_PERIOD = 1.0/FPS

TENS_FREQ = 60
TENS_PERIOD = 1.0/TENS_FREQ

POWS = (4,27,18,24)
GPIOS = (17,22,23,25)

TENS_LEN = len(GPIOS)
powVals = [1]*TENS_LEN
gpioVals = [0]*TENS_LEN

lastChange = 0
mLoc = 0

GPIO.setmode(GPIO.BCM)
for pin in (POWS+GPIOS):
    GPIO.setup(pin, GPIO.OUT)

def loop():
    global lastChange, mLoc, powVals, gpioVals
    now = time.time()
    if(now - lastChange > 2.0):
        lastChange = now
        mLoc = (mLoc + 1)%TENS_LEN
        powVals = [1]*TENS_LEN
        gpioVals = [0]*TENS_LEN
        powVals[mLoc] = 0
        gpioVals[mLoc] = 1

lastLoop = 0
while True:
    now = time.time()
    tensWaveVal = int((now/TENS_PERIOD)%2)
    GPIO.output(POWS, tuple([tensWaveVal*v for v in powVals]))
    GPIO.output(GPIOS, tuple([tensWaveVal*v for v in gpioVals]))

    if (now-lastLoop > LOOP_PERIOD):
        lastLoop = now
        loop()
