# Octarver

### Octave Range Converter

A lightweight command-line tool for converting between musical note names and frequencies across octave ranges.

## Why Octarver?

While libraries like `librosa` provide note-frequency conversion functions, Octarver is designed specifically as a **lightweight CLI tool** for quick conversions:

- **Lightweight**: No heavy dependencies (unlike librosa's 100MB+ install)
- **Fast**: Instant command-line results without writing Python code
- **Simple**: Purpose-built for one task, does it well
- **Portable**: Easy to use in shell scripts and workflows

Perfect for musicians, audio engineers, and students who need quick frequency-note conversions without importing a full audio analysis library.

## Features

- Convert frequency (Hz) to note name (e.g., 440 → A4)
- Convert note name to frequency (e.g., A4 → 440Hz)
- Supports octave specification (O1-O8)
- Based on equal temperament with A4 = 440Hz

## Installation
```bash
pip install octarver
```

Or install from source:
```bash
git clone https://github.com/tkuro11/octarver.git
cd octarver
pip install -e .
```

## Usage
```bash
usage: octarver [-h] [-o OCTAVE] [-n NOTE] [-f FREQ] [note_spec ...]

convert between the note name and frequency

positional arguments:
  note_spec             specify the octave and the note or frequency. 
                        Examples: 'O3A', 'C#', '440'
                        The octave can be omitted (default O4).

options:
  -h, --help            show this help message and exit
  -o OCTAVE, --octave OCTAVE
                        set the octave (this takes precedence)
  -n NOTE, --note NOTE  set the note (this takes precedence)
  -f FREQ, --freq FREQ  set frequency (this takes precedence)
```

## Examples

### Frequency to Note
```bash
$ octarver 440
A4: 440.00 Hz

$ octarver 523.25
C5: 523.25 Hz

$ octarver 880
A5: 880.00 Hz
```

### Note to Frequency
```bash
$ octarver A4
A4: 440.00 Hz

$ octarver O5C
C5: 523.25 Hz

$ octarver C#
C#4: 277.18 Hz

$ octarver O3G#
G#3: 207.65 Hz
```

### Using Options
```bash
$ octarver -o 5 -n C
C5: 523.25 Hz

$ octarver -f 440
A4: 440.00 Hz
```

## Technical Details

- **Tuning Standard**: A4 = 440Hz (ISO 16:1975)
- **Temperament**: 12-tone equal temperament
- **Frequency Range**: Supports octaves O1 through O8
- **Formula**: f = 440 × 2^((n-49)/12), where n is the number of semitones from A4

## Roadmap

### ✅ v0.1.x (Current)
Simple, lightweight frequency-note converter with A4=440Hz and 12-tone equal temperament.

### 🔲 v0.2.x (Next Major Release)
**Alternative Tunings** - Add support for:
- Custom A4 reference frequencies
  - A4 = 442Hz (Modern orchestral pitch, common in Europe)
  - A4 = 415Hz (Baroque pitch for historical performance)
  - A4 = 432Hz (Alternative tuning)
  - A4 = 435Hz (French standard, 1859)
- Historical and alternative tuning systems (Just intonation, Pythagorean, etc.)
- Integration with [pitchtools](https://pypi.org/project/pitchtools/)
- Optional advanced features: `pip install octarver[advanced]`

### 🔲 v0.3.x (Future)
**Enhanced Features** - Additional functionality:
- MIDI note number conversion
- Cent deviation display for tuning accuracy
- Batch processing from files
- Multiple output formats (JSON, CSV)

### 💡 Ideas Under Consideration
- Interactive REPL mode for quick conversions
- Harmonic series calculations
- Chord frequency analysis

---

**Note**: The roadmap is subject to change based on user feedback and feature requests. 
Please [open an issue](https://github.com/tkuro11/octarver/issues) if you have suggestions!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

tkuro11

## Links

- Repository: https://github.com/tkuro11/octarver
- Issues: https://github.com/tkuro11/octarver/issues
- PyPI: https://pypi.org/project/octarver/ (coming soon)
