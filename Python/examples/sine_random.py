import sc
import time, random

seed = random.Random()


sc.start( verbose=1, spew=1 )
s = sc.sc.server ###################


sine = sc.Synth( "sine" )
sine.freq = 444

timeout = time.time() + 10 # 10 secs

while time.time() < timeout :
    time.sleep(0.5) # loop every half sec
    sine.amp = seed.random() # 0 to 1
    sine.freq = seed.randint(1000, 1500) 

    
sine.free()
sc.quit()

print "quiting"
