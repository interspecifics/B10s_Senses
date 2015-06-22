#!/usr/bin/env python

import sys, time

FPS = 20.0
LOOP_PERIOD = 1.0/FPS

TENS_FREQ = 80
TENS_PERIOD = 1.0/TENS_FREQ

GPIOS = [[4,17,27,22], [18,23,24,25], [5,6,13,19], [12,16,20,21]]
TENS_DIM = (len(GPIOS),len(GPIOS[0]))
TENS_LEN = TENS_DIM[0] * TENS_DIM[1]
gpioVals = [[0]*TENS_DIM[1] for x in range(TENS_DIM[0])]

lastChange = 0
mLoc = 0

def loop():
    global lastChange, mLoc
    now = time.time()
    if(now - lastChange > 0.5):
        lastChange = now
        mLoc = (mLoc + 1)%TENS_LEN
        for y in range(TENS_DIM[0]):
            for x in range(TENS_DIM[1]):
                gpioVals[y][x] = 0
        (cy, cx) = (mLoc/TENS_DIM[1], mLoc%TENS_DIM[1])
        gpioVals[cy][cx] = 1
        print gpioVals

while True:
    tensWaveVal = int(time.time()/TENS_PERIOD)%2
    #TODO: update GPIOS
    for y in range(TENS_DIM[0]):
        for x in range(TENS_DIM[1]):
            pass
            # TODO: gpio.output(GPIO[y][x], gpioVals[y][x]*tensWaveVals)

    loopStart = time.time()
    loop()
    loopTime = time.time() - loopStart
    time.sleep(max(LOOP_PERIOD - loopTime, 0))

