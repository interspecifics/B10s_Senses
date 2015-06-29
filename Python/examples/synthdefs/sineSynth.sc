(
SynthDef("sineSynth", {
	arg freq=440, amp=2.0;
	var out;
	out = SinOsc.ar(freq)*amp;
	Out.ar(0, out);
	Out.ar(1, out);
}).load(s);
)

x = Synth.new("sine");
x.set("amp", 1.0);
x.free;
