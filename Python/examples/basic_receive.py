
import sc
import time, threading
import OSC


receive_address = 'localhost', 11112
s = OSC.OSCServer(receive_address) # basic
s.addDefaultHandlers()

xb = 0
yb = 0
sb = 0
xh = 0
yh = 0
sh = 0


def blob_handler(addr, tags, stuff, source):
    global xb, yb, sb
    print "---"
    print "xb %s" % stuff[0]
    print "yb %s" % stuff[1]
    print "sb %s" % stuff[2]
    print "---"
    xb = stuff[0]
    yb = stuff[1]
    sb = stuff[2]



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


s.addMsgHandler("/b10s/blob",  blob_handler) # adding our function
s.addMsgHandler("/b10s/haar", haar_handler) # adding our function



# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
    print addr


# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()
sc.start(spew=1)
pulseTest = sc.Synth( "pulseTest" )


try :
    while True :
        time.sleep(5)
        pulseTest.maxPartial = xb
        pulseTest.fund = yb
        pulseTest.ampHz = sb


except KeyboardInterrupt :
    print "\nClosing OSCServer."
    s.close()
    print "Waiting for Server-thread to finish"
    st.join() ##!!!
    print "Done"
