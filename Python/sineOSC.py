import sc
import time,threading
import OSC

receive_address = '127.0.0.1', 9000
# OSC Server.
s = OSC.OSCServer(receive_address) # basic
# an /'error' handler, an '/info' handler.
# And, if the client supports it, a '/subscribe' & '/unsubscribe' handler
s.addDefaultHandlers()


# define a message-handler function for the server to call.
def printing_handler(addr, tags, stuff, source):
    print "---"
    print "received new osc msg from %s" % OSC.getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags %s" % tags
    print "data %s" % stuff
    print "---"

s.addMsgHandler("/print", printing_handler) # adding our function


# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
    print addr


# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()

try :
    while 1 :
        time.sleep(5)

print 'hello world........'

sc.start( verbose=1, spew=1 )

sine = sc.Synth( "sine" )

sine.freq = 444

time.sleep(5) # stay here for 5 secs while sine plays
    
sine.free()
sc.quit()

print 'seeya world! .......'


