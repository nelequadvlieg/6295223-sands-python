import numpy as np

def sine_wave(f, duration, shift=0, scale=1, points=100):
    """
    Generate a sine wave with frequency f, duration, optional time shift and scaling.
    """
    time = np.linspace(0, duration, points)
    y = np.sin(2 * np.pi * f * (time * scale) + shift)
    return time, y

def step_function(time, threshold=0):
    """
    Generate a unit step function where the step occurs at 'threshold'.
    """
    step = (time >= threshold).astype(int)
    return step
exit()