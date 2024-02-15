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

    note = [notes[note_idx]]
    enh = notes[note_idx+1]
    if enh != "_":
        note.append(enh)

    return oct, note

# exports
def note2freq(octave, note):
    try:
        idx = notes.index(note) // 2
    except ValueError as ex:
        ex.args = ("no such note : " + note,)
        raise
    f = alpha*2**((idx + (octave-1)*12)/12)
    return f

# UI
if __name__ == "__main__":
    import sys
    import os
    import argparse

    parser = argparse.ArgumentParser(description="convert between the note name and frequency")
    parser.add_argument('note_spec', nargs="*", help="""specify the octave and the note 
                        or frequency.\n like 'O3A' / or '440'. The octave can be omitted (default O4).""")
    parser.add_argument('-o', '--octave', help="set the octave (this takes precedence)", default = 4)
    parser.add_argument('-n', '--note',   help="set the note (this takes precedence)")
    parser.add_argument('-f', '--freq',   help="set frequency (this takes precedence)")
    opt = parser.parse_args()

    freq=None
    note=None
    octv=None

    # process note_spec part
    for elem in opt.note_spec:
        if elem[0].isalpha():
            if elem[0].upper() == "O":
                octv = int("".join([c for c in elem[1:] if c.isdigit()]))
                elem = "".join([c for c in elem[1:] if not c.isdigit()])
            note = elem.capitalize()
        else:
            try:
                freq = float(elem)
            except ValueError:
                parser.error("only accept decimal value")

    if opt.freq:
        freq = float(opt.freq)
    if opt.note:
        note = opt.note.capitalize()
    if not octv:
        octv= int(opt.octave)

    if freq and note:
        parser.error("both frequency and note name are supplied. Only one of these can be specified.")

## note -> freq
    if note:
        try:
            f = note2freq(octv, note)
        except Exception as ex:
            parser.error(ex)
        if os.isatty(1):
            print(f"f = {f:.3f} Hz")
        else:
            print(f"{f:.4f}")
## freq -> note
    elif freq:
        oct, note = freq2note(freq)
        print(f"-o{oct} {' '.join(note)}")
    else:
        parser.print_usage()
