import numpy as np
from scipy import signal

import matplotlib.pyplot as plt

# ---------- Signal Generators ----------

def generate_sine(freq=1, amp=1, duration=1, sampling_rate=1000):
    """
    Generate a sinusoidal signal.
    """
    t = np.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
    x = amp * np.sin(2 * np.pi * freq * t)
    return t, x

def generate_step(duration=1, sampling_rate=1000):
    """
    Generate a unit step signal.
    """
    t = np.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
    x = np.heaviside(t, 1)  # step starts at 0
    return t, x

# ---------- Signal Operations ----------

def time_shift(t, x, shift):
    """
    Shift signal in time by 'shift' units.
    """
    return t + shift, x

def time_scale(t, x, scale):
    """
    Scale signal in time by 'scale' factor.
    """
    return t * scale, x

# ---------- Plotting Helper ----------

def plot_signal(t, x, title="Signal", filename=None):
    """
    Plot and optionally save a signal.
    """
    plt.figure()
    plt.plot(t, x)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    if filename:
        plt.savefig(filename, dpi=150)
    plt.show()