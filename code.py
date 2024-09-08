
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
f = 5

continuous_signal = np.sin(2 * np.pi * f * t)


fs1 = 35
fs2 = 8 

t_sampled1 = np.arange(0, 1, 1/fs1)
t_sampled2 = np.arange(0, 1, 1/fs2)
sampled_signal1 = np.sin(2 * np.pi * f * t_sampled1)
sampled_signal2 = np.sin(2 * np.pi * f * t_sampled2)

t_interp = np.linspace(0, 1, 1000)
reconstructed_signal1 = np.interp(t_interp, t_sampled1, sampled_signal1)
reconstructed_signal2 = np.interp(t_interp, t_sampled2, sampled_signal2)

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, continuous_signal, label='Continuous Signal', color='blue')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Continuous Signal')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, continuous_signal, label='Continuous Signal', color='blue')
plt.stem(t_sampled1, sampled_signal1, linefmt='r-', markerfmt='ro', basefmt=" ", label='Sampled Signal (fs = 20 Hz)', use_line_collection=True)
plt.stem(t_sampled2, sampled_signal2, linefmt='g-', markerfmt='go', basefmt=" ", label='Sampled Signal (fs = 8 Hz)', use_line_collection=True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Sampling of Continuous Signal')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, continuous_signal, label='Continuous Signal', color='blue')
plt.plot(t_interp, reconstructed_signal1, label='Reconstructed Signal (fs = 20 Hz)', color='red', linestyle='--')
plt.plot(t_interp, reconstructed_signal2, label='Reconstructed Signal (fs = 8 Hz)', color='green', linestyle='--')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Reconstruction of Sampled Signal')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
