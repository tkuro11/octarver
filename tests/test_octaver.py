import pytest
from octarver import freq2note, note2freq

class TestFreq2Note:
    """Test conversion from frequency to note name"""
    
    def test_440hz_is_a4(self):
        """440Hz should be A4"""
        oct, note = freq2note(440)
        assert oct == 4
        assert 'A' in note
    
    def test_880hz_is_a5(self):
        """880Hz should be A5 (one octave above 440Hz)"""
        oct, note = freq2note(880)
        assert oct == 5
        assert 'A' in note
    
    def test_220hz_is_a3(self):
        """220Hz should be A3"""
        oct, note = freq2note(220)
        assert oct == 3
        assert 'A' in note


class TestNote2Freq:
    """Test conversion from note name to frequency"""
    
    def test_a4_is_440hz(self):
        """A4 should be 440Hz"""
        freq = note2freq(4, 'A')
        assert abs(freq - 440.0) < 0.01
    
    def test_chromatic_scale_ascending(self):
        """Chromatic scale from C4 to B4 should be in ascending order"""
        freqs = []
        notes_seq = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        for note in notes_seq:
            freqs.append(note2freq(4, note))
        
        # Verify all frequencies are in ascending order
        for i in range(len(freqs) - 1):
            assert freqs[i] < freqs[i+1]
    
    def test_invalid_note_raises_error(self):
        """Invalid note name should raise ValueError"""
        with pytest.raises(ValueError):
            note2freq(4, 'X')
    
    def test_octave_affects_frequency(self):
        """Same note in different octaves should differ by power of 2"""
        a3 = note2freq(3, 'A')
        a4 = note2freq(4, 'A')
        a5 = note2freq(5, 'A')
        
        # Each octave doubles the frequency
        assert abs(a4 / a3 - 2.0) < 0.01
        assert abs(a5 / a4 - 2.0) < 0.01

class TestRoundTrip:
    """Test round-trip conversions maintain consistency"""
    
    def test_note_to_freq_to_note(self):
        """Note → frequency → note should return to original note and octave"""
        test_cases = [
            (3, 'C'), (4, 'A'), (5, 'G'), (6, 'B'), (2, 'F#')
        ]
        
        for original_oct, original_note in test_cases:
            freq = note2freq(original_oct, original_note)
            recovered_oct, recovered_note = freq2note(freq)
            
            assert recovered_oct == original_oct, \
                f"Octave mismatch for {original_note}{original_oct}: got {recovered_oct}"
            assert original_note in recovered_note[0], \
                f"Note mismatch for {original_note}{original_oct}: got {recovered_note}"
    
    def test_freq_to_note_to_freq(self):
        """Frequency from note → frequency should be consistent"""
        # Only test with actual note frequencies (no arbitrary intermediate values)
        notes_seq = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        for octave in [3, 4, 5]:
            for note in notes_seq:
                original_freq = note2freq(octave, note)
                recovered_oct, recovered_note = freq2note(original_freq)
                
                # Convert back to verify consistency
                recovered_freq = note2freq(recovered_oct, recovered_note[0])
                assert abs(original_freq - recovered_freq) < 0.01, \
                    f"Frequency mismatch for {note}{octave}"
