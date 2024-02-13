#!/usr/bin/env python
import sys
import math

interval = "C C# D D# E F F# G G# A A# B".split()
# alpha * (2 ** 1/12) ** n  =  440
#  n = 12 + 12 + 9 (cddeffgga)
#  alpha = 440 / 2 ** 1/12 ** 33
alpha = 440 / ((2**(1/12)) ** 33)

arg = sys.argv[1]
if arg.isdigit():
    hz = int(arg)
    # alpha * (2 ** 1/12) ** idx  =  hz
    # hz/alpha = (2 ** 1/12) ** idx
    # log(hz/alpha) = idx * log(2**1/12)
    # log(hz/alpha) / log(2 ** 1/12) = idx
    idx = int(math.log(hz/alpha) / math.log(2)*12)

    print(f"O{int(idx/12)} {interval[idx % 12]}")
else:
    if arg[0].upper() == "O":
        octave = int(arg[1])
        if len(sys.argv) == 3:
            arg = sys.argv[2].upper()
        else:
            arg = "".join(arg[2:]).upper()
    else:
        arg = sys.argv[1].upper()
        print("> no octave specified, assuming O2")
        octave = 2
    idx = interval.index(arg)
    print(f"f = {alpha*2**((idx + octave*12)/12):.3f} Hz")


