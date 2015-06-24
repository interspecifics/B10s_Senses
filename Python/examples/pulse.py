import sc
import time, random

seed = random.Random()

sc.start( verbose=1, spew=1 )
s = sc.sc.server

pulse = sc.Synth("pulseTest")
pulse = ampHz = 0.4

timeout = time.time() + 10 # 10 secs

while time.time() < timeout :
    time.sleep(0.5)
    pulse.fund(20)
    pulse.maxPartial(9)
    pulse.width(0.8)

pulse.free()
sc.quit()


print "cerrando"
