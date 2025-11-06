import wave
from scipy.io import wavfile
import numpy as np
from FFT import *
import sounddevice as sd
from filtros import *
import matplotlib.pyplot as plt
import control as ctrl
f0=1500
Q=0.1
# ---------Arquivo1---------
arquivo1 = wave.open("projeto8/file_example_WAV_1MG.wav")
rate1, audio1 = wavfile.read("projeto8/file_example_WAV_1MG.wav")
audio1_mono = paraMono(audio1)

b1, a1 = filtro_passa_baixa(f0, Q, rate1)
audiofiltrado_1= trata_audio(audio1_mono, b1, a1)

T1=  float(len(audio1)/rate1)
N1 = len(audio1)
t1 = np.linspace(0, T1,N1, endpoint=False)

# ---------------Arquivo2---------------
arquivo2 = wave.open("projeto8\Gravando (2).wav")
rate2, audio2 = wavfile.read("projeto8\Gravando (2).wav")
audio2_mono = paraMono(audio2)
Q=5
b2, a2 = filtro_passa_baixa(f0, Q, rate2)
audiofiltrado_2= trata_audio(audio2_mono, b2, a2)

T2=  float(len(audio2)/rate2)
N2 = len(audio2)
t2 = np.linspace(0, T2,N2, endpoint=False)
# ---------------Arquivo3--------------------------
arquivo3 = wave.open("projeto8\Gravando (4) (online-audio-converter.com).wav")
rate3, audio3 = wavfile.read("projeto8\Gravando (4) (online-audio-converter.com).wav")
audio3_mono = paraMono(audio3)

Q=10

b3, a3 = filtro_passa_baixa(f0, Q, rate3)
audiofiltrado_3= trata_audio(audio3_mono, b3, a3)

T3=  float(len(audio3)/rate3)
N3 = len(audio3)
t3 = np.linspace(0, T3,N3, endpoint=False)

freqs, magnitude, magnitude_db = compute_fft(audiofiltrado_1, rate1, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t1, audiofiltrado_1, rate1 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(audiofiltrado_2, rate2, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t2, audiofiltrado_2, rate2 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(audiofiltrado_3, rate3, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t3, audiofiltrado_3, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

plt.show()