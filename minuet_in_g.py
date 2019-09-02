'''
    https://musescore.com/user/9292486/scores/2086106
'''

from music_generator import *

TEMPO = 120
TIME = (3,4)
KEY = G_MAJOR

MINUET_IN_G_VOICE_1_SECTION_1 = [
    # Bar 1, Measure 1
    Measure(TEMPO, TIME, KEY, [
        Quarter(D5),
        Eighth(G4),
        Eighth(A4),
        Eighth(B5),
        Eighth(C5)
    ]),

    # Bar 1, Measure 2
    Measure(TEMPO, TIME, KEY, [
        Quarter(D5),
        Quarter(G4), # todo: stocatto
        Quarter(G4)  # todo: stocatto
    ]),

    # Bar 1, Measure 3
    Measure(TEMPO, TIME, KEY, [
        Quarter(E5),
        Eighth(C5),
        Eighth(D5),
        Eighth(E5),
        Eighth(F5),
    ]),

    # Bar 1, Measure 4
    Measure(TEMPO, TIME, KEY, [
        Quarter(G5),
        Quarter(G4),
        Quarter(G4),
    ]),

    # Bar 1, Measure 5
    Measure(TEMPO, TIME, KEY, [
        Quarter(C5),
        Eighth(D5),
        Eighth(C5),
        Eighth(B4),
        Eighth(A4),
    ]),

    # Bar 1, Measure 6
    Measure(TEMPO, TIME, KEY, [
        Quarter(B4),
        Eighth(C5),
        Eighth(B4),
        Eighth(A4),
        Eighth(G4)
    ]),

    # Bar 1, Measure 7
    Measure(TEMPO, TIME, KEY, [
        Quarter(F4),
        Eighth(G4),
        Eighth(A4),
        Eighth(B4),
        Eighth(G4),
    ]),

    # Bar 1, Measure 8
    Measure(TEMPO, TIME, KEY, [
        Quarter(B4),
        Half(A4)
    ]),

    # Bar 2, Measure 1
    Measure(TEMPO, TIME, KEY, [
        Quarter(D5),
        Eighth(G4),
        Eighth(A4),
        Eighth(B5),
        Eighth(C5)
    ]),

    # Bar 2, Measure 2
    Measure(TEMPO, TIME, KEY, [
        Quarter(D5),
        Quarter(G4),
        Quarter(G4)
    ]),

    # Bar 2, Measure 3
    Measure(TEMPO, TIME, KEY, [
        Quarter(E5),
        Eighth(C5),
        Eighth(D5),
        Eighth(E5),
        Eighth(F5),
    ]),

    # Bar 2, Measure 4
    Measure(TEMPO, TIME, KEY, [
        Quarter(G5),
        Quarter(G4),
        Quarter(G4),
    ]),

    # Bar 2, Measure 5
    Measure(TEMPO, TIME, KEY, [
        Quarter(C5),
        Eighth(D5),
        Eighth(C5),
        Eighth(B4),
        Eighth(A4),
    ]),

    # Bar 2, Measure 6
    Measure(TEMPO, TIME, KEY, [
        Quarter(B4),
        Eighth(C5),
        Eighth(B4),
        Eighth(A4),
        Eighth(G4)
    ]),

    # Bar 2, Measure 7
    Measure(TEMPO, TIME, KEY, [
        Quarter(A4),
        Eighth(B4),
        Eighth(A4),
        Eighth(G4),
        Eighth(F4)
    ]),

    # Bar 2, Measure 8
    Measure(TEMPO, TIME, KEY, [
        Dot(Half(G4))
    ]),
]

MINUET_IN_G_VOICE_2_SECTION_1 = [
    # Bar 1, Measure 1
    Measure(TEMPO, TIME, KEY, [
        Half(G3),
        Quarter(A3)
    ]),

    # Bar 1, Measure 2
    Measure(TEMPO, TIME, KEY, [
        Dot(Half(B3))
    ]),

    # Bar 1, Measure 3
    Measure(TEMPO, TIME, KEY, [
        Dot(Half(C4))
    ]),

    # Bar 1, Measure 4
    Measure(TEMPO, TIME, KEY, [
        Dot(Half(B3))
    ]),

    # Bar 1, Measure 5
    Measure(TEMPO, TIME, KEY, [
        Dot(Half(A3))
    ]),

    # Bar 1, Measure 6
    Measure(TEMPO, TIME, KEY, [
        Dot(Half(G3))
    ]),

    # Bar 1, Measure 7
    Measure(TEMPO, TIME, KEY, [
        Quarter(D4),
        Quarter(B3),
        Quarter(G3),
    ]),

    # Bar 1, Measure 8
    Measure(TEMPO, TIME, KEY, [
        Quarter(D4),
        Eighth(B2),
        Eighth(C4),
        Eighth(B3),
        Eighth(A3),
    ]),

    # Bar 2, Measure 1
    Measure(TEMPO, TIME, KEY, [
        Half(B3),
        Quarter(A3)
    ]),

    # Bar 2, Measure 2
    Measure(TEMPO, TIME, KEY, [
        Quarter(G3),
        Quarter(B3),
        Quarter(G3)
    ]),

    # Bar 2, Measure 3
    Measure(TEMPO, TIME, KEY, [
        Dot(Half(C4))
    ]),

    # Bar 2, Measure 4
    Measure(TEMPO, TIME, KEY, [
        Quarter(B3),
        Eighth(C4),
        Eighth(B3),
        Eighth(A3),
        Eighth(G3),
    ]),

    # Bar 2, Measure 5
    Measure(TEMPO, TIME, KEY, [
        Half(A3),
        Quarter(F3)
    ]),

    # Bar 2, Measure 6
    Measure(TEMPO, TIME, KEY, [
        Half(G3),
        Quarter(B3)
    ]),

    # Bar 2, Measure 7
    Measure(TEMPO, TIME, KEY, [
        Quarter(C4),
        Quarter(D4),
        Quarter(D3)
    ]),

    # Bar 2, Measure 8
    Measure(TEMPO, TIME, KEY, [
        Half(G3),
        Quarter(G2)
    ]),
]

if __name__ == '__main__':
    voice_1 = []
    voice_1.extend(MINUET_IN_G_VOICE_1_SECTION_1)
    voice_1.extend(MINUET_IN_G_VOICE_1_SECTION_1)

    voice_2 = []
    voice_2.extend(MINUET_IN_G_VOICE_2_SECTION_1)
    voice_2.extend(MINUET_IN_G_VOICE_2_SECTION_1)

    #import music_generator.wav as wav
    #wav.serialize([[voice_1], [voice_2]], 'minuet_in_g.wav')

    import music_generator.arduino as arduino
    arduino.serialize([(12, [voice_1]), (10, [voice_2])], 'minuet_in_g.ino')
