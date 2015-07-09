# Open Sensory Substitution 
Repository for the 0SS_ OPEN SENSORY SUNTITUTION.
In this project we are using OpenCV to detect blobs from a video camara attached to the Raspberry Pi, this detections is later tranform into sound using SuperCollider and SC.VO.3.1 for python and electrical impulses using GPIOS. 

# HARDWARE:
- RaspberryPi B+
- Camara module for raspberry 
- Micro sd cards  
- Electro-tactil transducers 
- Lithium baterrys for the raspberry 

# RASPBIAN IMAGE WITH LIBRARIES AND CODE:
The following image contains all the libraries necessary to round the OSS, incluiding the python scripts to comunicate OpenCV with SuperCollider. 

- http://interspecifics.cc/downloads/OSSraspi.dmg

#Libraries and installs

- OpenCV for python 
  http://docs.opencv.org/index.html
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.

- SuperCollider: 
  http://supercollider.github.io/development/building-raspberrypi.html
SuperCollider is a programming language for real time audio synthesis and algorithmic composition.
The language interpreter runs in a cross platform IDE (OS X/Linux/Windows) and communicates via Open Sound Control with one or more synthesis servers. The SuperCollider synthesis server runs in a separate process or even on a separate machine so it is ideal for realtime networked music.

- SC.V0.3.1 
  http://www.ixi-software.net/content/download/sc/sc-0.3.1.zip
The scosc module converts standard python types to supercollider osc messages.
In order to play sounds in musical time, we have to send OSC messages with timestamps. Because the server has a limited message buffer (1024), we have to send messages as a stream in real-time. The challenge is getting the messages in early enough that the server can process them, while not sending too many as to override the buffer. We also have to take latency into account, which makes this a much bigger bundle of fun.

#HOW TO RUN THE SOFTWARE

- $ ssh pi@sensory1.local
- $ password: 1234
- $ cd B10s_Senses
- $ cd B10s_Senses/Python 
- $ cd B10s_Senses/Python/examples 
- $ cd ..
- $ cd B10s_Senses/Python
- $ ./prepServer.sh 
- $ sudo python b10sOpenCv.py


#Python + SuperCollider examples

In the following example with show a regular synthdef from supercollider using the sclang lenguage:

___________________________

(
SynthDef("PMCrotale", {
arg midi = 60, tone = 3, art = 1, amp = 0.8, pan = 0;
var env, out, mod, freq;
freq = midi.midicps;
env = Env.perc(0, art);
mod = 5 + (1/IRand(2, 6));
out = PMOsc.ar(freq, mod*freq,
	pmindex: EnvGen.kr(env, timeScale: art, levelScale: tone),
	mul: EnvGen.kr(env, timeScale: art, levelScale: 0.3));
out = Pan2.ar(out, pan);
out = out * EnvGen.kr(env, timeScale: 1.3*art,
	levelScale: Rand(0.1, 0.5), doneAction:2);
Out.ar(0, out); //Out.ar(bus, out);
}).add;
)


Synth("PMCrotale", ["midi", rrand(48, 72).round(1), "tone", rrand(1, 6)])

In this case we invoque using a regular synth argument.

___________________________

Using python tu interface:

import sc
import time, random

seed = random.Random()


sc.start( verbose=1, spew=1 )
s = sc.sc.server ###################

PMCrotale = sc.Synth( "PMCrotale" )
PMCrotale.freq = 400


timeout = time.time() + 10 # 10 secs

while time.time() < timeout :
    time.sleep(0.5) # loop every half sec
    PMCrotale.midi = seed.randint( 40, 90 )
    PMCrotale.tono =  10
    PMCrotale.art = 1



PMCrotale.free()
sc.quit()

print 'seeya world! ...........'
