import numpy as np 

def generate_sine_wave(frequency, duration, time_shift, time_scale):
    """
    Generate a sinusoidal wave signal.
    
    Parameters:
    frequency (float): Frequency of the sine wave in Hz
    duration (float): Duration of the signal in seconds
    time_shift (float): Time shift applied to the signal
    time_scale (float): Time scaling factor
    
    Returns:
    tuple: (time_array, wave_array) containing time values and corresponding wave amplitudes
    """
    t = np.linspace(0, duration, 100)
    wave = np.sin(2 * np.pi * frequency * t * time_scale + time_shift)
    return t, wave 

def generate_step_function(t, step_time):
    """
    Generate a sinusoidal wave signal.
    
    Parameters:
    frequency (float): Frequency of the sine wave in Hz
    duration (float): Duration of the signal in seconds
    time_shift (float): Time shift applied to the signal
    time_scale (float): Time scaling factor
    
    Returns:
    tuple: (time_array, wave_array) containing time values and corresponding wave amplitudes
    """
    return np.where(t < step_time, 0, 1)

exit()