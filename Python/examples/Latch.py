import sc
import time, random

sc.start( verbose=1, spew=1 )
s = sc.sc.server

Latch = sc.Synth( "Latch" )
Latch = rate = 9

timeout = time.time() + 10 # 10 secs

while time.time() < timeout :
    time.sleep(0.5)
    Latch.rate(20)

Latch.free()
sc.quit()


print "cerrando"
