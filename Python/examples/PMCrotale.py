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



PMCrotale.free()
sc.quit()

print 'seeya world! ...........'
