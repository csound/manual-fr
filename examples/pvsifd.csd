<CsoundSynthesizer>
<CsOptions>
; Select audio/midi flags here according to platform
-odac  ;;;realtime audio out
;-iadc    ;;;uncomment -iadc if realtime audio input is needed too
; For Non-realtime ouput leave only the line below:
; -o pvsifd.wav -W ;;; for file output any platform
</CsOptions>
<CsInstruments>

sr = 44100
ksmps = 32
nchnls = 2
0dbfs  = 1

instr 1

ifftsize    =   p4
ihopsize    =   p5
ain	diskin2  "drumsMlp.wav", 1, 0, 1                  
fs1,fsi2 pvsifd  ain, ifftsize, ihopsize, 1		; pvsifd analysis
fst	partials fs1, fsi2, .1, 1,3, 500	; partial tracking
aout	resyn    fst, 1, 1.5, 500, 1		; resynthesis (up a 5th)
	outs	aout, aout

endin
</CsInstruments>
<CsScore>
;sine
f1 0 4096 10 1
;           size    hop
i 1 0 2     2048    512  
i 1 3 2     1024    256      
e
</CsScore>
</CsoundSynthesizer>
