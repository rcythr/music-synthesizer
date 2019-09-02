
from fractions import Fraction
from functools import reduce

_default_wave_function = 'sine'
def set_default_wave_function(f):
    global _default_wave_function
    _default_wave_function = f

_default_envelope_function = 'exp_falloff'
def set_default_envelope_function(f):
    global _default_envelope_function
    _default_envelope_function = f

# Accidental contstants
FLAT = -1
NATURAL = 0
SHARP = 1

# Key Signatures
class KeySignature:
    __slots__ = ('sharps', 'flats')

    def __init__(self, sharps, flats):
        self.sharps = sharps
        self.flats = flats

C_MAJOR = A_MINOR = KeySignature(set(), set())
G_MAJOR = E_MINOR = KeySignature({'F'}, set())
D_MAJOR = B_MINOR = KeySignature({'F', 'C'},set())
A_MAJOR = F_SHARP_MINOR = KeySignature({'F', 'C', 'G'}, set())
E_MAJOR = C_SHARP_MINOR = KeySignature({'F', 'C', 'G', 'D'}, set())
B_MAJOR = G_SHARP_MINOR = KeySignature({'F', 'C', 'G', 'D', 'A'}, set())
F_SHARP_MAJOR = D_SHARP_MINOR = KeySignature({'F', 'C', 'G', 'D', 'A', 'E'},set())
C_SHARP_MAJOR = KeySignature({'F', 'C', 'G', 'D', 'A', 'E', 'B'}, set())
C_FLAT_MAJOR = KeySignature(set(), {'B', 'E', 'A', 'D', 'G', 'C', 'F'})
G_FLAT_MAJOR = E_FLAT_MINOR = KeySignature(set(), {'B', 'E', 'A', 'D', 'G', 'C'})
D_FLAT_MAJOR = B_FLAT_MINOR = KeySignature(set(), {'B', 'E', 'A', 'D', 'G'})
A_FLAT_MAJOR = F_MINOR = KeySignature(set(), {'B', 'E', 'A', 'D'})
E_FLAT_MAJOR = C_MINOR = KeySignature(set(), {'B', 'E', 'A'})
B_FLAT_MAJOR = G_MINOR = KeySignature(set(), {'B', 'E'})
F_MAJOR = D_MINOR = KeySignature(set(), {'B'})

B0 = 'B0'
C1 = 'C1'
D1 = 'D1'
E1 = 'E1'
F1 = 'F1'
G1 = 'G1'
A1 = 'A1'
B1 = 'B1'
C2 = 'C2'
D2 = 'D2'
E2 = 'E2'
F2 = 'F2'
G2 = 'G2'
A2 = 'A2'
B2 = 'B2'
C3 = 'C3'
D3 = 'D3'
E3 = 'E3'
F3 = 'F3'
G3 = 'G3'
A3 = 'A3'
B3 = 'B3'
C4 = 'C4'
D4 = 'D4'
E4 = 'E4'
F4 = 'F4'
G4 = 'G4'
A4 = 'A4'
B4 = 'B4'
C5 = 'C5'
D5 = 'D5'
E5 = 'E5'
F5 = 'F5'
G5 = 'G5'
A5 = 'A5'
B5 = 'B5'
C6 = 'C6'
D6 = 'D6'
E6 = 'E6'
F6 = 'F6'
G6 = 'G6'
A6 = 'A6'
B6 = 'B6'
C7 = 'C7'
D7 = 'D7'
E7 = 'E7'
F7 = 'F7'
G7 = 'G7'
A7 = 'A7'
B7 = 'B7'
C8 = 'C8'
D8 = 'D8'

# Notes
NOTES = [
    # Octave 0
    (B0, 31),

    # Octave 1
    (C1, 33),
    (None, 35),
    (D1, 37),
    (None, 39),
    (E1, 41),
    (F1, 44),
    (None, 46),
    (G1, 49),
    (None, 52),
    (A1, 55),
    (None, 58),
    (B1, 62),

    # Octave 2
    (C2, 65),
    (None, 69),
    (D2, 73),
    (None, 78),
    (E2, 82),
    (F2, 87),
    (None, 93),
    (G2, 98),
    (None, 104),
    (A2, 110),
    (None, 117),
    (B2, 123),

    # Octave 3
    (C3, 131),
    (None, 139),
    (D3, 147),
    (None, 156),
    (E3, 165),
    (F3, 175),
    (None, 185),
    (G3, 196),
    (None, 208),
    (A3, 220),
    (None, 233),
    (B3, 247),

    # Octave 4
    (C4, 262),
    (None, 277),
    (D4, 294),
    (None, 311),
    (E4, 330),
    (F4, 349),
    (None, 370),
    (G4, 392),
    (None, 415),
    (A4, 440),
    (None, 466),
    (B4, 494),

    # Octave 5
    (C5, 523),
    (None, 554),
    (D5, 587),
    (None, 622),
    (E5, 659),
    (F5, 698),
    (None, 740),
    (G5, 784),
    (None, 831),
    (A5, 880),
    (None, 932),
    (B5, 988),

    # Octave 6
    (C6, 1047),
    (None, 1109),
    (D6, 1175),
    (None, 1245),
    (E6, 1319),
    (F6, 1397),
    (None, 1480),
    (G6, 1568),
    (None, 1661),
    (A6, 1760),
    (None, 1865),
    (B6, 1976),

    # Octave 7
    (C7, 2093),
    (None, 2217),
    (D7, 2349),
    (None, 2489),
    (E7, 2637),
    (F7, 2794),
    (None, 2960),
    (G7, 3136),
    (None, 3322),
    (A7, 3520),
    (None, 3729),
    (B7, 3951),

    # Octave 8
    (C8, 4186),
    (None, 4435),
    (D8, 4699),
    (None, 4978)
]

# Note Index by Name Lookup. Useful for applying accidental offsets to notes.
NOTE_BY_NAME = {}
for i, (name, value) in enumerate(NOTES):
    if name is not None:
        NOTE_BY_NAME[name] = i

class Note:
    __slots__ = ('length', 'note', 'accidental', 'wave_function', 'envelope_function')

    def __init__(self, length, note, accidental=None, wave_function=None, envelope_function=None):
        if wave_function is None:
            wave_function = _default_wave_function
        if envelope_function is None:
            envelope_function = _default_envelope_function

        self.length = length
        self.note = note
        self.accidental = accidental
        self.wave_function = wave_function
        self.envelope_function = envelope_function

    def hz(self):
        accidental = self.accidental
        if accidental is None:
            accidental = 0

        # Rest has no Hz.
        if self.note == 'REST':
            return 0

        # Determine the note from the table.
        idx = NOTE_BY_NAME[self.note] + accidental

        # If we're outside the supported range, treat this as a rest.
        if idx < 0 or idx >= len(NOTES):
            return 0

        # Return the Hz from the table.
        return NOTES[idx][1]

# lengths
def Dot(note):
    note.length *= Fraction(3,2)
    return note

def Whole(note, accidental=None):
    return Note(Fraction(1,1), note, accidental)

def Half(note, accidental=None):
    return Note(Fraction(1,2), note, accidental)

def Quarter(note, accidental=None):
    return Note(Fraction(1,4), note, accidental)

def Eighth(note, accidental=None):
    return Note(Fraction(1/8), note, accidental)

def Sixteenth(note, accidental=None):
    return Note(Fraction(1/16), note, accidental)

class Measure:
    __slots__ = ('tempo', 'time_signature', 'key', 'notes')

    def __init__(self, tempo, time_signature, key, notes):
        # Propagate the accidentals across the measure to make life easier later.
        active_accidentals = {}
        self.notes = []
        for note in notes:
            if note.accidental is None:
                letter = note.note[0]
                if letter in key.sharps:
                    self.notes.append(Note(note.length, note.note, SHARP))
                elif letter in key.flats:
                    self.notes.append(Note(note.length, note.note, FLAT))
                elif note.note in active_accidentals:
                    self.notes.append(Note(note.length, note.note, active_accidentals[note.note]))
                else:
                    self.notes.append(Note(note.length, note.note, NATURAL))
            else:
                active_accidentals[note.note] = note.accidental
                self.notes.append(note)

        self.tempo = tempo
        self.time_signature = time_signature
        self.key = key

    def is_time_valid(self):
        return Fraction(*self.time_signature) == reduce(lambda a, b: a + b.length, notes, Fraction(0,1))
