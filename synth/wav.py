
from math import sin, tau, e
import random
import struct
import wave
import itertools
import functools

SAMPLING_FREQ = 44100
SAMPLING_FREQ_PER_MIN = SAMPLING_FREQ * 60
SAMPLE_SIZE = 2

# Wave Generators
def _wave_sine(f):
    f = float(f)
    tauf_per_sample = tau * f / SAMPLING_FREQ
    for i in itertools.count(0):
        yield sin(tauf_per_sample * i)

def _wave_square(f):
    samples_per_cycle = (SAMPLING_FREQ // f)
    samples_per_half_cycle = samples_per_cycle // 2
    for i in itertools.cycle(range(samples_per_cycle)):
        if i <= samples_per_half_cycle:
            yield 1.0
        else:
            yield -1.0

def _wave_triangle(f):
    samples_per_cycle = (SAMPLING_FREQ // f)
    for i in itertools.cycle(range(samples_per_cycle)):
        i /= samples_per_cycle
        if i > 0.0 and i <= 0.25:
            yield 4.0 * i
        elif i > 0.25 and i <= 0.75:
            yield -4.0 * i + 2.0
        elif i > 0.75 and i <= 1.0:
            yield 4.0 * i - 4.0

def _wave_saw(f):
    samples_per_cycle = (SAMPLING_FREQ // f)
    for i in itertools.cycle(range(samples_per_cycle)):
        i /= samples_per_cycle
        if i > 0.0 and i <= 0.50:
            yield 2 * i
        elif i > 0.25:
            yield 2 * i - 2.0

# Enveloping Generators
def _envelope_linear_falloff(sample_generator, n_samples):
    amp = 1.0
    falloff = 1.0 / n_samples
    for i, s in zip(range(n_samples), sample_generator):
        amp -= falloff
        yield amp * s

def _envelope_exp_falloff(sample_generator, n_samples):
    step = 1 / n_samples
    for i, s in zip(range(n_samples), sample_generator):
        amp = e ** (-5 * i * step)
        yield amp * s

WAVE_FUNCTION_LOOKUP = {
    'sine': _wave_sine,
    'square': _wave_square,
    'triangle': _wave_triangle,
    'saw': _wave_saw
}

ENVELOPE_FUNCTION_LOOKUP = {
    'none': lambda sample_generator, n_samples: itertools.islice(sample_generator, n_samples),
    'linear_falloff': _envelope_linear_falloff,
    'exp_falloff': _envelope_exp_falloff
}

def _voice(voice):
    for measure in voice:
        samples_per_beat = (SAMPLING_FREQ_PER_MIN / measure.tempo)
        for note in measure.notes:
            num_samples = samples_per_beat * note.length * measure.time_signature[1]
            f = note.hz()
            if f is 0:
                yield from itertools.repeat(0.0, int(num_samples))
            else:
                wave = note.wave_function
                if isinstance(wave, str):
                    wave = WAVE_FUNCTION_LOOKUP[wave]

                envelope = note.envelope_function
                if isinstance(envelope, str):
                    envelope = ENVELOPE_FUNCTION_LOOKUP[envelope]
                yield from envelope(wave(f), int(num_samples))

def _channel(voices):
    num_voices = len(voices)
    yield from map(lambda x: x / num_voices, map(sum, itertools.zip_longest(*(_voice(voice) for voice in voices), fillvalue=0.0)))

def _roundrobin(iterables):
    num_active = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = itertools.cycle(itertools.islice(nexts, num_active))

def _clamp(v, min, max):
    if v < min:
        return min
    if v > max:
        return max
    return v

def serialize(channels, output_filename):
    with wave.open(output_filename, 'w') as w:
        w.setparams((len(channels), 2, SAMPLING_FREQ, None, 'NONE', 'not compressed'))

        amp_max = float(int((2 ** (SAMPLE_SIZE * 8)) / 2) - 1)

        for sample in _roundrobin([_channel(x) for x in channels]):
            s = int(amp_max * _clamp(sample, -1.0, 1.0))
            w.writeframesraw(struct.pack('h', s))
