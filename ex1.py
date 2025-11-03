import numpy as np
from FFT import *
fs=44100
T=2
N = int(fs * T)
t = np.linspace(0, T, N, endpoint=False)
# x = 1.0 * np.sin(2*np.pi*50.0*t) + 0.6 * np.sin(2*np.pi*120.0*t)
f= 2000
f2= 15*1000
x=1*np.sin(2*np.pi*f*t)
x2=1*np.sin(2*np.pi*f2*t)
x3 =x+x2
freqs, magnitude, magnitude_db = compute_fft(x3, fs, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t, x3, fs , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')