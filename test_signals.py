import pytest
import numpy as np
from signals import generate_sine_wave, generate_step_function

def test_generate_sine_wave():
    """Test sine wave generation with basic parameters."""
    t, wave = generate_sine_wave(frequency=1, duration=1, time_shift=0, time_scale=1)
    
    assert len(t) == 100
    assert len(wave) == 100
    assert wave.min() >= -1
    assert wave.max() <= 1
    assert isinstance(t, np.ndarray)
    assert isinstance(wave, np.ndarray)

def test_generate_step_function():
    """Test step function generation."""
    t = np.linspace(-1, 1, 100)
    step = generate_step_function(t, step_time=0)
    
    assert len(step) == 100
    assert step.min() == 0
    assert step.max() == 1
    assert np.all(step[t < 0] == 0)
    assert np.all(step[t > 0] == 1)

def test_sine_wave_time_shift():
    """Test sine wave with time shift."""
    t, wave_shifted = generate_sine_wave(1, 1, time_shift=0.5, time_scale=1)
    t, wave_normal = generate_sine_wave(1, 1, time_shift=0, time_scale=1)
    
    
    assert len(wave_shifted) == len(wave_normal)