# Octaver 
converter between note name (C,D,...) and frequency
- if cmdline argument is digit, it understood as frequency. Octaver convert it to a note.
- if cmdline argument is alphanumeric, it understood as note name. Octaver convert it to frequency.

```
usage: octaver.py [-h] [-o OCTAVE] [-n NOTE] [-f FREQ] [note_spec ...]

convert between the note name and frequency

positional arguments:
  note_spec             specify the octave and the note or frequency. like 'O3A' / or '440'. The octave can be omitted (default O4).

options:
  -h, --help            show this help message and exit
  -o OCTAVE, --octave OCTAVE
                        set the octave (this takes precedence)
  -n NOTE, --note NOTE  set the note (this takes precedence)
  -f FREQ, --freq FREQ  set frequency (this takes precedence)
```
