import sc
import time, threading
import OSC

receive_address = 'localhost', 11112
s = OSC.OSCServer(receive_address) # basic
s.addDefaultHandlers()


def printing_handler(addr, tags, stuff, source):
    print "---"
    print "received new osc msg from %s" % OSC.getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags %s" % tags
    print "data %s" % stuff
    print "---"
    valor = stuff

s.addMsgHandler("/print", printing_handler) # adding our function

print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
    print addr

print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()

valor = 0
try :
    while True :
        sc.start( verbose=1, spew=1 )
        sine = sc.Synth( "sine" )
        sine.freq = valor
        time.sleep(5)

except KeyboardInterrupt :
    print "\nClosing OSCServer."
    s.close()
    print "Waiting for Server-thread to finish"
    st.join() ##!!!
    print "Done"
    sine.free()
    sc.quit()

print 'seeya world! ...........'
