(
SynthDef.new(\fmSynth, {
	arg freq1=400, freq2=20, amp=10;
	var w1, w2, sig;
	w1 = PMOsc.ar(freq1, 0, 1);
	w2 = PMOsc.ar(freq2, 0, 1);
	sig = w1*w2*amp;
	Out.ar(0, sig);
	Out.ar(1, sig);
}).load(s);
)

x = Synth.new(\fmSynth);
x.set(\freq1, 250);
x.set(\freq2, 5.5);
x.set(\amp, 10);

x.free

