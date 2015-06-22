#!/usr/bin/env python

import cv2
import sys, time
import numpy as np

FPS = 20.0
LOOP_PERIOD = 1.0/FPS

TENS_FREQ = 80
TENS_PERIOD = 1.0/TENS_FREQ

GPIOS = [[4,17,27,22], [18,23,24,25], [5,6,13,19], [12,16,20,21]]
TENS_DIM = (len(GPIOS),len(GPIOS[0]))
gpioVals = [[0]*TENS_DIM[1] for x in range(TENS_DIM[0])]

def setup():
    global prevFrame, frame, video_capture, mDetector, mCascade
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3,320)
    video_capture.set(4,240)

    prevFrame = cv2.cvtColor(video_capture.read()[1], cv2.COLOR_RGB2GRAY)
    frame = cv2.cvtColor(video_capture.read()[1], cv2.COLOR_RGB2GRAY)

    # Setup SimpleBlobDetector parameters.
    mParams = cv2.SimpleBlobDetector_Params()
    mParams.minThreshold = 10;
    mParams.maxThreshold = 32;
    mParams.filterByArea = True
    mParams.minArea = 32
    mParams.filterByCircularity = True
    mParams.minCircularity = 0.001
    mParams.filterByConvexity = True
    mParams.minConvexity = 0.001
    mParams.filterByInertia = True
    mParams.minInertiaRatio = 0.001

    mDetector = cv2.SimpleBlobDetector(mParams)
    mCascade = None

    if len(sys.argv) > 1:
        mCascade = cv2.CascadeClassifier(sys.argv[1])
    else:
        print "Please provide a cascade file if you want to do face/body detection."

def loop():
    global prevFrame, frame, video_capture, mDetector, mCascade
    prevFrame = frame
    frameRGB = cv2.blur(video_capture.read()[1], (16,16))
    frame = cv2.cvtColor(frameRGB, cv2.COLOR_RGB2GRAY)
    diffFrame = cv2.absdiff(frame, prevFrame)

    ret, diffFrameThresh = cv2.threshold(diffFrame, 32, 255, cv2.THRESH_BINARY_INV)
    blobs = mDetector.detect(diffFrameThresh)
    print len(blobs)
    # TODO: get biggest blob size,x,y

    if mCascade is not None:
        cascadeResult = mCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        # TODO: get detected size,x,y

        # Draw a rectangle around the faces
        for (x, y, w, h) in cascadeResult:
            cv2.rectangle(frameRGB, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    img = cv2.drawKeypoints(diffFrameThresh, blobs, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('_', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cleanUp()
        sys.exit(0)

def cleanUp():
    global video_capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    lastLoop = 0
    setup()
    while True:
        tensWaveVal = int(time.time()/TENS_PERIOD)%2
        #TODO: update GPIOS
        for y in range(TENS_DIM[0]):
            for x in range(TENS_DIM[1]):
                pass
                # TODO: gpio.output(GPIO[y][x], gpioVals[y][x]*tensWaveVals)

        now = time.time()
        if (now-lastLoop > LOOP_PERIOD):
            lastLoop = now
            loop()
