import numpy as np 

def generate_sine_wave(frequency, duration, time_shift, time_scale):
    t = np.linspace(0, duration, 100)
    wave = np.sin(2 * np.pi * frequency * t * time_scale + time_shift)
    return t, wave 

def generate_step_function(t, step_time):
    return np.where(t < step_time, 0, 1)

exit()