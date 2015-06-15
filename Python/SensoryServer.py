//sistema local que corre dentro Raspy 
// declarando argumentos

from opencv.OpenCV import OpenCv
from OSC import OSCClient, OSCMessage
import scsynth
import opencv 

// iniciar servidor OpenCV 

// Iniciar un puerto de comunicación 
OSC_OUT_HOST = "localhost"
OSC_OUT_PORT = 57000;

// vOrganizar los mensajes OSC 
Recognition_List = 'facedetection, distance, shape, positio, color, size'

// Iniciar un serviro OSC 

if __name__ == "__main__":
   mOscClient = OSCClient()
   mOscClient.connect( (OSC_OUT_HOST,OSC_OUT_PORT) )
   mOscMessage = OSCMessage()


// vamos a organizar los mensajes OSC (facedetection, ditance, object, shape, position)  

// vamos a iniciar el synth sc

// wrap de mensajes OpenCV a mensajes Synth 

// transmision de puerto serial al raspbery controlado por el objeto position.

// serial envia una oscilacion por los GPIO pins de acuerdo a la postion 

