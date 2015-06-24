(
SynthDef("different_tones", {
	arg freq = 440; // declare an argument and give it a default value
	var out;
	out = SinOsc.ar(freq)*0.3;
	Out.ar(0, out)
}).play
)