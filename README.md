# Open Sensory Substitution 
Repository for the 0SS OPEN SENSORY SUNTITUTION project
In this project we are using OpenCV to detect blobs from a video camara attached to the Raspberry Pi, this detections is later tranfor into sound using SuperCollider and SC.VO.3.1 for python and electrical impulses using GPIOS. 

# HARDWARE:
- RaspberryPi B+
- Camara module for raspberry 
- Micro sd cards  
- Electro-tactil transducers 
- Lithium baterrys for the raspberry 

# RASPBIAN IMAGE WITH LIBRARIES AND CODE:
http://interspecifics.cc/downloads/OSSraspi.dmg

#Libraries and installs

- OpenCV for python : http://docs.opencv.org/index.html
OpenCV is a library of computer vision allows the process and detection of specific properties of diferent tipes of images, as movement, blobs, or detection of specific objetcs. 

- SuperCollider: http://supercollider.github.io/development/building-raspberrypi.html
SuperCollider is a programming language for real time audio synthesis and algorithmic composition.
The language interpreter runs in a cross platform IDE (OS X/Linux/Windows) and communicates via Open Sound Control with one or more synthesis servers. The SuperCollider synthesis server runs in a separate process or even on a separate machine so it is ideal for realtime networked music.

- SC.V0.3.1 : http://www.ixi-software.net/content/download/sc/sc-0.3.1.zip
the scosc module converts standard python types to supercollider osc messages.

In order to play sounds in musical time, we have to send OSC messages with timestamps. Because the server has a limited message buffer (1024), we have to send messages as a stream in real-time. The challenge is getting the messages in early enough that the server can process them, while not sending too many as to override the buffer. We also have to take latency into account, which makes this a much bigger bundle of fun.
