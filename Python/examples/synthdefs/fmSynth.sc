(
SynthDef.new(\fmSynth, {
	arg freq1=400, freq2=20;
	var w1, w2, sig;
	w1 = PMOsc.ar(freq1, 0, 1);
	w2 = PMOsc.ar(freq2, 0, 1);
	sig = w1*w2*10;
	Out.ar(0, sig);
	Out.ar(1, sig);
}).load(s);
)

x = Synth.new(\fmSynth);
x.set(\freq1, 150);
x.set(\freq2, 5.5);

x.free

// use arrays for signals, does the same thing>
(
SynthDef.new(\fmSynth, { arg freq1=400, freq2=20, amp = 1;
	var w1, w2, sig;
	w1 = PMOsc.ar(freq1, 0, 1);
	w2 = PMOsc.ar(freq2, 0, 1);
	sig = w1*w2* amp;
	Out.ar(0, [sig, sig]);
}).add;
)

// add mod freq control
(
SynthDef.new(\fmSynth, { arg freq1=400, freq2=20, modfreq = 10, moddepth = 1, amp = 1;
	var w1, w2, sig;
	w1 = PMOsc.ar(freq1, modfreq, moddepth);
	w2 = PMOsc.ar(freq2, modfreq, moddepth);
	sig = w1*w2* amp;
	Out.ar(0, [sig, sig]);
}).add;
)

x = Synth(\fmSynth);
x.set(\freq1, 300)
x.set(\freq2, 30)
x.set(\modfreq, 20)
x.set(\moddepth, 0)
x.set(\moddepth, 3)

Ndef(\fmSynth, { arg freq1=400, freq2=20, modfreq = 10, moddepth = 1, amp = 1;
	var w1, w2, sig;
	w1 = PMOsc.ar(freq1, modfreq, moddepth);
	w2 = PMOsc.ar(freq2, modfreq, moddepth);
	sig = w1*w2* amp;
	[sig, sig]
});

Ndef(\fmSynth).play;
Ndef(\fmSynth).stop(4);

Ndef(\fmSynth).stop(4);


Ndef(\fmSynth, { arg freq1=400, freq2=20, modfreq = 10, moddepth = 1, amp = 1;
	var w1, w2, sig;
	w1 = PMOsc.ar(freq1, modfreq, moddepth);
	w2 = PMOsc.ar(freq2, modfreq, moddepth);
	sig = w1*w2* amp;
	sig
});

Ndef(\fmSynth).stop(0.01);

Ndef(\fmSynth).objects[0].synthDef.name

Ndef(\fmSynth, \fmSynth);

Spec.add(\freq1, [200, 2000, \exp]);
Spec.add(\freq2, \freq1);
Spec.add(\modfreq, [0.2, 200, \exp]);

Ndef(\fmSynth).gui(8);
