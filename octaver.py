#!/usr/bin/env python
import math

## CONSTANTS

# list of notes. 
# enharmonic notes are placed sequently, 
# _ is placeholder (there's no enharmonics)
notes = "C _ C# Db D _ D# Eb E _ F _ F# Gb G _ G# Ab A _ A# Bb B _".split()

# compute basic frequency coefficient from note O4 A (=440Hz).
# alpha * (2 ** 1/12) ** n  =  440
#  where n = 12*3 + 9 = 45
# then,  alpha = 440 / ((2**(1/12)) ** 45)
alpha = 55 / ((2**(1/12)) ** 9)

# exports
def freq2note(hz):
    idx = int(math.log(hz/alpha) / math.log(2) *12 + 0.5)
    oct = int(idx / 12)+1
    note_idx = (idx % 12)*2
    note = notes[note_idx]
    if notes[note_idx+1] != "_":
        note += "(" + notes[note_idx+1] + ")"
    return oct, note

# exports
def note2freq(octave, note):
    idx = notes.index(arg) // 2
    f = alpha*2**((idx + (octave-1)*12)/12)
    return f

# UI
if __name__ == "__main__":
    import sys
    import os
    arg = sys.argv[1]

    if arg[0].isdigit():
        oct, note = freq2note(float(arg))
        print(f"O{oct} {note}")
    else:
        if arg[0].upper() == "O":
            octave = int(arg[1])
            if len(sys.argv) == 3:
                arg = sys.argv[2].capitalize()
            else:
                arg = "".join(arg[2:]).capitalize()
        else:
            print("> no octave specified, assuming O4", file=sys.stderr)
            arg = sys.argv[1].capitalize()
            octave = 4
        f = note2freq(octave, arg)
        if os.isatty(1):
            print(f"f = {f:.3f} Hz")
        else:
            print(f"{f:.4f}")
