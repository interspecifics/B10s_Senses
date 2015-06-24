NetAddr.localAddr

(
SynthDef.new(\pulseTest, {
	arg ampHz=4, fund=40, maxPartial=4, width=0.5;
	var amp1, amp2,  freq1, freq2, sig1, sig2;
	amp1 = LFPulse.kr (ampHz,0,0.12) * 0.75;
	amp2 = LFPulse.kr (ampHz,0.5,0.12) * 0.75;
	freq1 = LFNoise0.kr(4).exprange(fund,fund*maxPartial).round(fund);
	freq2 = LFNoise0.kr(4).exprange(fund, fund*maxPartial).round(fund);
	freq1 = freq1 * LFPulse.kr(8, add:1);
	freq2 = freq2 * LFPulse.kr(6, add:1);
	sig1 = Pulse.ar(freq1, width, amp1);
	sig2 = Pulse.ar (freq2, width, amp2);
	sig1 = FreeVerb.ar(sig1, 0.7, 0.8, 0.25);
	sig2 = FreeVerb.ar(sig2, 0.7, 0.8, 0.25);
	Out.ar(0, sig1);
	Out.ar(1,sig2);
}).add;
)

(
OSCdef('pdlistener',{
	arg msg;
	Synth.new(\pulseTest, [\ampHz, 1.5, \fund, 20, \maxPartial,4, \width,msg[2]]);
}, "/print");
)

y = Synth.new(\pulseTest);
y.set(\ampHz, 0.3);
y.set(\fund, 10);
y.set(\maxPartial, 8);
y.set(\width,1.4);
y.free;

s.quit;
s.boot;