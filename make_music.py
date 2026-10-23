"""Create an original, gentle instrumental bed for the portfolio demo videos."""

import math
from pathlib import Path

import numpy as np
import wave

RATE = 44100
BPM = 76
BEAT = 60 / BPM
BAR = 4 * BEAT
CHORDS = [
    (48, [60, 64, 67, 71]),
    (45, [57, 60, 64, 67]),
    (41, [53, 57, 60, 64]),
    (43, [55, 59, 62, 64]),
]
MELODY = [
    (0.5, 76, 0.72), (1.5, 79, 0.62), (2.5, 83, 0.82),
    (3.5, 79, 0.55), (4.5, 76, 0.70), (5.5, 72, 0.65),
    (6.5, 76, 0.85), (7.5, 79, 0.58), (8.5, 81, 0.72),
    (9.5, 84, 0.88), (10.5, 81, 0.63), (11.5, 76, 0.70),
    (12.5, 74, 0.66), (13.5, 79, 0.82), (14.5, 83, 0.72),
    (15.5, 79, 0.62),
]


def midi_hz(note):
    return 440.0 * (2 ** ((note - 69) / 12))


def add_note(track, start, note, length, gain, pan, seed):
    """Add a rounded, softly struck additive-synthesis note."""
    i0 = int(start * RATE)
    count = min(len(track) - i0, int((length + 0.7) * RATE))
    if count <= 0:
        return
    t = np.arange(count, dtype=np.float32) / RATE
    freq = midi_hz(note)
    attack = np.minimum(t / 0.025, 1.0)
    decay = 0.73 + 0.27 * np.exp(-t / 0.42)
    release = np.ones_like(t)
    rel = t > length
    release[rel] = np.exp(-(t[rel] - length) / 0.34)
    envelope = attack * decay * release
    phase = (seed % 359) * (math.tau / 359)
    tone = (
        np.sin(math.tau * freq * t + phase)
        + 0.23 * np.sin(math.tau * freq * 2.01 * t + phase * 0.7)
        + 0.075 * np.sin(math.tau * freq * 3.98 * t + phase * 1.3)
    ) * envelope * gain
    left = math.sqrt((1 - pan) * 0.5)
    right = math.sqrt((1 + pan) * 0.5)
    track[i0:i0 + count, 0] += tone * left
    track[i0:i0 + count, 1] += tone * right


def build(duration=136.0):
    n = round(duration * RATE)
    stereo = np.zeros((n, 2), dtype=np.float32)
    t = np.arange(n, dtype=np.float32) / RATE
    bar_num = np.mod((t / BAR).astype(np.int32), 4)
    local = np.mod(t, BAR)

    for i, (bass, chord) in enumerate(CHORDS):
        select = bar_num == i
        tt = local[select]
        if not len(tt):
            continue
        envelope = np.minimum(tt / 0.8, 1.0) * (0.78 + 0.22 * np.exp(-tt / 5.8))
        pad = np.zeros_like(tt)
        for j, note in enumerate(chord):
            f = midi_hz(note)
            pad += (0.50 / (1 + j * 0.28)) * np.sin(math.tau * f * tt + j * 0.47)
            pad += 0.11 * np.sin(math.tau * (f * 2.003) * tt + j * 0.3)
        stereo[select, 0] += pad * envelope * 0.027
        stereo[select, 1] += pad * envelope * 0.027
        bass_wave = np.sin(math.tau * midi_hz(bass) * tt) * envelope * 0.022
        stereo[select, 0] += bass_wave
        stereo[select, 1] += bass_wave

    for bar_i, (_, chord) in enumerate(CHORDS):
        for beat_i in range(4):
            note = chord[(beat_i + 1) % len(chord)] + 12
            start = bar_i * BAR + beat_i * BEAT + 0.07
            add_note(stereo, start, note, 0.30, 0.038,
                     -0.24 if beat_i % 2 == 0 else 0.24, bar_i * 11 + beat_i)

    for repeat in range(8):
        for j, (beat, note, duration_beats) in enumerate(MELODY):
            start = repeat * 4 * BAR + beat * BEAT
            add_note(stereo, start, note, duration_beats * BEAT, 0.052,
                     -0.12 if j % 2 else 0.12, repeat * 31 + j)

    dry = stereo.copy()
    for delay, amount in [(0.19, 0.13), (0.37, 0.075), (0.61, 0.035)]:
        d = int(delay * RATE)
        stereo[d:, 0] += dry[:-d, 1] * amount
        stereo[d:, 1] += dry[:-d, 0] * amount

    fade = int(RATE * 2)
    stereo[:fade] *= np.linspace(0, 1, fade, dtype=np.float32)[:, None]
    peak = float(np.max(np.abs(stereo)))
    if peak:
        stereo *= 0.72 / peak
    return np.clip(stereo, -0.98, 0.98)


if __name__ == "__main__":
    out = Path(__file__).parent / "assets" / "music" / "robot-demo-theme.wav"
    samples = build()
    pcm = (samples * 32767).astype("<i2")
    with wave.open(str(out), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(RATE)
        wav.writeframes(pcm.tobytes())
    print(f"Wrote {out} ({len(samples) / RATE:.1f}s, peak {np.max(np.abs(samples)):.2f})")
