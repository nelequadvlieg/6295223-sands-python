import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from signals import generate_sine_wave, generate_step_function

time, sine1 = generate_sine_wave(frequency=1, duration=1, time_shift=0, time_scale=1)
plt.figure()
plt.plot(time, sine1)
plt.title("Sinusoidal Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

time_vals = np.linspace(-1, 1, 100)
step = generate_step_function(time_vals, step_time=0)
plt.figure()
plt.plot(time_vals, step)
plt.title("Step Function")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

t_shift, sine2 = generate_sine_wave(1, 1, time_shift=0.5, time_scale=1)
plt.figure()
plt.plot(t_shift, sine2)
plt.title("Time-Shifted Sinusoidal Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

t_mod, sine3 = generate_sine_wave(1, 1, 0.5, 2)
plt.figure()
plt.plot(t_mod, sine3)
plt.title("Time-Shifted and Time-Scaled Sinusoidal Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
print("Script finished, waiting for you to close the plot windows.")