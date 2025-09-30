import numpy as np
from scipy.signal import sawtooth

import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 10000)

plt.figure(1)
sawtooth1 = sawtooth(t, 1.0)
plt.plot(t, sawtooth1)
plt.title("Sawtooth 1")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.figure(2)
sawtooth2 = sawtooth(t, 0.5)
plt.plot(t, sawtooth2)
plt.title("Sawtooth 2")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.figure(3)
sawtooth3 = sawtooth(t, 0.0)
plt.plot(t, sawtooth3)
plt.title("Sawtooth 3")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from Signals import pulse
from Signals import periodic_pulse

t = np.linspace(-5, 5, 10000)

plt.figure(1)
single_pulse = pulse(t-2, 1.0)
plt.plot(t, single_pulse)
plt.title("Single pulse")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.figure(2)
multi_pulse = pulse(t/4, 2.0) + pulse(t-3, 1.0)
plt.plot(t, multi_pulse)
plt.title("Multi pulse")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


t2 = np.linspace(-10, 10, 10000)

plt.figure(3)
periodic_pulse = periodic_pulse(t2, 0.5)
plt.plot(t2, periodic_pulse)
plt.title("Periodic pulse")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()



import matplotlib.pyplot as plt
import numpy as np
from Signals import generate_sine_wave

# Parameters
frequency = 5          # Hz
duration = 2           # seconds
sample_rate = 100      # samples per second

# Generate the sine wave
t, waveform = generate_sine_wave(frequency, duration, sample_rate)

# Print the first 10 samples
print(waveform[:10])

# Plot the sine wave
plt.plot(t, waveform)
plt.title("5 Hz Sine Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()