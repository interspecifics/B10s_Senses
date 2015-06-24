import sc
import time, random

seed = random.Random()


sc.start( verbose=1, spew=1 )
s = sc.sc.server ###################


pmosc = sc.Synth( "pmosc" )
pmosc.freq = 444, MouseY(1,150), MouseX(1, 15)

timeout = time.time() + 10 # 10 secs

while time.time() < timeout :
    time.sleep(0.5) # loop every half sec
    pmosc.amp = seed.random() # 0 to 1
    pmosc.freq = seed.randint(1000, 1500) 

    
pmosc.free()
sc.quit()

print "quiting"
