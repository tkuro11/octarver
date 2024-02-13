#!/usr/bin/env python
import sys
import os
import math

notes = "C _ C# Db D _ D# Eb E _ F _ F# Gb G _ G# Ab A _ A# Bb B _".split()
# compute basic frequency coefficient from note A (=440Hz).
# alpha * (2 ** 1/12) ** n  =  440
#  where n = 12 + 12 + 9 = 33
alpha = 110 / (4*((2**(1/12)) ** 9))

arg = sys.argv[1]
if arg[0].isdigit():
    hz = float(arg)
    idx = int(math.log(hz/alpha) / math.log(2) *12 + 0.5)

    print(f"O{int(idx/12)} {notes[(idx % 12)*2]}")
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

    idx = notes.index(arg)//2
    f = alpha*2**((idx + octave*12)/12)
    if os.isatty(1):
        print(f"f = {f:.3f} Hz")
    else:
        print(f"{f:.4f}")
