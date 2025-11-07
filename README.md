# Signal Creation and Manipulation Project
This Python project focuses on generating, modifying, and visualizing basic signals.
It includes a collection of functions for signal generation as well as scripts that demonstrate how these signals can be plotted and manipulated.
## Features
- Generate sinusoidal waves with customizable frequency, duration, time shift, and time scaling
- Generate unit step functions with configurable step time
- Visualize signals with matplotlib plots
- Comprehensive test suite with pytest
## Signals Covered
The project creates and displays:
- A sinusoidal signal
- A unit step function
- A time-shifted sinusoidal signal
- A time-shifted and time-scaled sinusoidal signal

## Quick start
bash

pip install numpy matplotlib

'''python script.py'''

pytest


## How to Run
To run the project, ensure you have Python installed along with the required libraries (numpy, matplotlib).
The repository contains multiple Python files:

One file defines all the signal functions.

Other files demonstrate plotting and transformations of the signals.

Run a file using:

python <filename>.py


This will open plots of the signals with time on the x-axis and amplitude on the y-axis

## Project Structure
signals.py - Core signal generation functions
script.py - Demonstration scripts with plots
test_signals.py - Test suite
pyproject.toml - Project configuration

## Usage example
python
from signals import generate_sine_wave, generate_step_function

# Generate signals
time, sine_wave = generate_sine_wave(frequency=1, duration=2, time_shift=0.5)
time_vals = np.linspace(-1, 1, 100)
step = generate_step_function(time_vals, step_time=0)
