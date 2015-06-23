#!/usr/bin/env python

import cv2
import sys, time
import numpy as np
from OSC import OSCClient, OSCMessage

FPS = 20.0
LOOP_PERIOD = 1.0/FPS

TENS_FREQ = 80
TENS_PERIOD = 1.0/TENS_FREQ

POWS = (4,27,18,24)
GPIOS = (17,22,23,25)
TENS_LEN = len(GPIOS)
powVals = [1]*TENS_LEN
gpioVals = [0]*TENS_LEN

(S,X,Y) = (0,0,0)
cascadeDetected = 0
FPA = 0.75
FPB = 1.0-FPA

SERVER_IP = '127.0.0.1'
SERVER_PORT = 1234
MSG_ADDRESS = '/b10s/cv'

mClient = None
mMessage = None

def setup():
    global prevFrame, frame, video_capture, mDetector, mCascade, mClient, mMessage

    mClient = OSCClient()
    mClient.connect( (SERVER_IP, SERVER_PORT) )
    mMessage = OSCMessage(MSG_ADDRESS)

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
    global prevFrame, frame, video_capture, mDetector, mCascade, mClient, mMessage
    global S,X,Y, cascadeDetected
    prevFrame = frame
    frameRGB = cv2.blur(video_capture.read()[1], (16,16))
    frame = cv2.cvtColor(frameRGB, cv2.COLOR_RGB2GRAY)
    diffFrame = cv2.absdiff(frame, prevFrame)

    ret, diffFrameThresh = cv2.threshold(diffFrame, 32, 255, cv2.THRESH_BINARY_INV)
    blobs = mDetector.detect(diffFrameThresh)

    (s,x,y) = (0,0,0)
    # get biggest blob (size,x,y)
    for blob in blobs:
        s0 = blob.size
        if(s0 > s):
            (s,(x,y)) = (s0, blob.pt)

    if mCascade is not None:
        cascadeResult = mCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # get cascade detector results and update (size, x, y)
        cascadeDetected *= 0.9
        if len(cascadeResult) > 0:
            (s,x,y) = (0,0,0)
            cascadeDetected = 3.0
        for (x0, y0, w0, h0) in cascadeResult:
            if(max(w0,h0) > s):
                (s,x,y) = (max(w0,h0), x0, y0)

    (S,X,Y) = (FPA*S+FPB*s, FPA*X+FPB*x, FPA*Y+FPB*y)
    cascadeToSend = 1.0 if cascadeDetected > 1.0 else 0.0
    mMessage.clearData()
    mMessage.append([X,Y,S, cascadeToSend])
    try:
        mClient.send( mMessage )
    except Exception as e:
        pass

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
        # TODO: update GPIOS
        # GPIO.output(GPIOS, tuple([tensWaveVal*v for v in gpioVals]))

        now = time.time()
        if (now-lastLoop > LOOP_PERIOD):
            lastLoop = now
            loop()
