#!/usr/bin/env python

import sc
import time, threading
import OSC

FPS = 20.0
LOOP_PERIOD = 1.0/FPS
lastLoop = 0

receive_address = '192.168.1.165', 1234
s = OSC.OSCServer(receive_address)
s.addDefaultHandlers()

xb = 0
yb = 0
sb = 0
xh = 0
yh = 0
sh = 0
notasynth = False

def blob_handler(addr, tags, stuff, source):
    global xb, yb, sb, notasynth
    print "---"
    print "xb %s" % stuff[0]
    print "yb %s" % stuff[1]
    print "sb %s" % stuff[2]
    print "---"
    xb = stuff[0]
    yb = stuff[1]
    sb = stuff[2]
    notasynth = True


def haar_handler(addr, tags, stuff, source):
    global xh, yh, sh
    print "---"
    print "xh %s" % stuff[0]
    print "yh %s" % stuff[1]
    print "sh %s" % stuff[2]
    print "---"
    xh = stuff[0]
    yh = stuff[1]
    sh = stuff[2]


s.addMsgHandler("/b10s/blob",  blob_handler)
s.addMsgHandler("/b10s/haar", haar_handler)


# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
    print addr


# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()
sc.start(spew=1)
# sine = sc.Synth( "sine" )
Latch = sc.Synth ( "Latch")

try :
    while True :
        now = time.time()
        if(now-lastLoop > LOOP_PERIOD):
            lastLoop = now
            Latch.rate = xb*20+1
            # sine.freq = xb*600+120
            #sine.amp = yb*2+1
            time.sleep(LOOP_PERIOD/2)

except KeyboardInterrupt :
    print "\nClosing OSCServer."
    s.close()
    Latch.free()
    sc.quit()
    print "Waiting for Server-thread to finish"
    st.join()
    print "Done"
