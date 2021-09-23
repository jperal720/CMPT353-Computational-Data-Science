import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

N_SAMPLES = 500

input_range = np.linspace(0, 2 * np.pi, N_SAMPLES, dtype=np.float32)

signal = np.sin(input_range)

noise = np.random.normal(0, 1, N_SAMPLES)

assert noise.shape == signal.shape

noisy_signal = signal + noise/5

plt.plot(input_range, noisy_signal, 'b.', alpha=0.5)
plt.plot(input_range, signal, 'r-', linewidth=4)
plt.legend(['Sensor Readings', 'Truth'])
plt.xlabel('Time')
plt.ylabel('Value of thing we care about')
plt.show()

del signal

filtered = lowess(noisy_signal, input_range, frac=0.1)

plt.plot(input_range, noisy_signal, 'b.', alpha=0.5)
plt.plot(filtered[:, 0], filtered[:, 1], 'r-', linewidth=4)
plt.legend(['Sensor readings', 'Reconstructed signal'])
plt.show()